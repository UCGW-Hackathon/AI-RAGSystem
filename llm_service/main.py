import sys
import warnings
import uuid
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

warnings.filterwarnings(
    "ignore",
    message=r"The default value of `allowed_objects` will change in a future version.*",
)
warnings.filterwarnings("ignore", module=r"langgraph\.checkpoint\.base.*")

from schemas import (
    QuestionRequest,
    AnswerResponse,
    UrlInjectionRequest,
    InjectJobResponse,
    InjectSyncResponse,
    DeleteRequest,
    MetadataQueryResponse,
    HealthResponse,
)
from vectordb import (
    add_urls_to_vectorstore,
    delete_by_metadata,
    get_metadata_counts,
    get_qdrant_client,
    lookup_service_codes,
    search_service_fixed_prices,
)
from graph import GraphBuilder
from tools import get_retriever_tool, refresh_retriever
from config import settings
from typing import Any

import os
import time
import logging
import re


LOG_LEVEL = settings.LOG_LEVEL
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger("agentic_rag_api")
SERVICE_CODE_RE = re.compile(r"\b[A-Z]{2}-\d{3}\b")
PRICE_QUERY_RE = re.compile(r"\b(harga|biaya|tarif|ongkos|jasa|layanan|cuci|service)\b", re.IGNORECASE)

APP_VERSION = "1.0.0"


# ------------------------------------------------------------------------------
# AMQP Publisher (lazy-init, connection pooled per process)
# ------------------------------------------------------------------------------
_amqp_connection = None
_amqp_channel = None
_amqp_lock = None


def _get_amqp_lock():
    global _amqp_lock
    import threading
    if _amqp_lock is None:
        _amqp_lock = threading.Lock()
    return _amqp_lock


def _get_amqp_channel():
    """Return a live AMQP channel, reconnecting if necessary."""
    global _amqp_connection, _amqp_channel
    import pika

    with _get_amqp_lock():
        try:
            if _amqp_channel and _amqp_channel.is_open:
                return _amqp_channel
        except Exception:
            pass

        params = pika.URLParameters(settings.CLOUDAMQP_URL)
        params.socket_timeout = 5
        _amqp_connection = pika.BlockingConnection(params)
        _amqp_channel = _amqp_connection.channel()

        # Declare exchange + queue + DLQ
        _amqp_channel.exchange_declare(
            exchange=settings.AMQP_EXCHANGE,
            exchange_type="direct",
            durable=True,
        )
        # Dead-letter queue
        dlq_name = f"{settings.AMQP_QUEUE_INJECT}.dlq"
        _amqp_channel.queue_declare(queue=dlq_name, durable=True)

        _amqp_channel.queue_declare(
            queue=settings.AMQP_QUEUE_INJECT,
            durable=True,
            arguments={
                "x-dead-letter-exchange": "",
                "x-dead-letter-routing-key": dlq_name,
                "x-message-ttl": 3_600_000,  # 1 hour TTL
            },
        )
        _amqp_channel.queue_bind(
            queue=settings.AMQP_QUEUE_INJECT,
            exchange=settings.AMQP_EXCHANGE,
            routing_key=settings.AMQP_QUEUE_INJECT,
        )

        logger.info("AMQP channel established (queue=%s)", settings.AMQP_QUEUE_INJECT)
        return _amqp_channel


def _publish_inject_job(job_id: str, urls: list[str]) -> None:
    """Publish inject job to AMQP queue."""
    import pika

    channel = _get_amqp_channel()
    payload = json.dumps({"job_id": job_id, "urls": urls})
    channel.basic_publish(
        exchange=settings.AMQP_EXCHANGE,
        routing_key=settings.AMQP_QUEUE_INJECT,
        body=payload,
        properties=pika.BasicProperties(
            delivery_mode=2,  # persistent
            content_type="application/json",
            message_id=job_id,
        ),
    )
    logger.info("Published inject job %s with %d URLs", job_id, len(urls))


# ------------------------------------------------------------------------------
# Lifespan
# ------------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    _init_locks()
    logger.info("Starting Agentic RAG API v%s ...", APP_VERSION)
    logger.info("AMQP enabled: %s", settings.USE_AMQP)
    logger.info("Startup complete. RAG graph will be built lazily on first use.")

    yield

    logger.info("Shutting down Agentic RAG API.")
    # Close AMQP connection gracefully
    global _amqp_connection
    try:
        if _amqp_connection and _amqp_connection.is_open:
            _amqp_connection.close()
            logger.info("AMQP connection closed.")
    except Exception as exc:
        logger.warning("Error closing AMQP connection: %s", exc)


app = FastAPI(
    title="Agentic RAG API",
    version=APP_VERSION,
    description="Production-grade RAG system with async URL injection via CloudAMQP",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ------------------------------------------------------------------------------
# Global Graph State (hot-swappable)
# ------------------------------------------------------------------------------
_graph_lock = None
_graph = None
_tools = None
_last_refresh_ts = 0.0
_refresh_cooldown_sec = 5.0


def _init_locks():
    global _graph_lock
    import threading

    if _graph_lock is None:
        _graph_lock = threading.RLock()


def _build_graph(tools) -> Any:
    """Compile and return a graph using the provided tools and selected LLM."""
    graph_builder = GraphBuilder(
        tools,
        llm_model=settings.LLM_MODEL,
        gemini_api_key=settings.GEMINI_API_KEY,
    )
    return graph_builder.compile()


def _ensure_graph_visualization(graph) -> None:
    """Generate and persist a visualization image of the graph. Best-effort."""
    try:
        os.makedirs(settings.DOCUMENTS_DIR, exist_ok=True)
        graph_image_path = os.path.join(settings.DOCUMENTS_DIR, "graph.png")
        png_bytes = graph.get_graph(xray=True).draw_mermaid_png()
        with open(graph_image_path, "wb") as f:
            f.write(png_bytes)
        logger.info("Saved graph visualization to %s", graph_image_path)
    except Exception as e:
        logger.warning("Failed to generate graph visualization: %s", e)


def _compile_global_graph(refresh_tools: bool = False) -> None:
    """Build or rebuild the global tools and graph."""
    global _graph, _tools

    if refresh_tools:
        _tools = get_retriever_tool(refresh=True)
    else:
        _tools = _tools or get_retriever_tool(refresh=False)

    _graph = _build_graph(_tools)
    _ensure_graph_visualization(_graph)
    logger.info("Graph compiled with model=%s", settings.LLM_MODEL)


def _maybe_refresh_graph_debounced(force: bool = False) -> bool:
    """Recompile the graph if enough time has elapsed since the last refresh."""
    global _last_refresh_ts
    now = time.perf_counter()
    if not force and (now - _last_refresh_ts) < _refresh_cooldown_sec:
        return False

    _compile_global_graph(refresh_tools=True)
    _last_refresh_ts = now
    return True


# ------------------------------------------------------------------------------
# Background tasks
# ------------------------------------------------------------------------------
def refresh_retriever_background(force_graph_refresh: bool = True):
    """Refresh retriever and optionally recompile the graph."""
    try:
        logger.info("Refreshing retriever in background...")
        if force_graph_refresh:
            _maybe_refresh_graph_debounced(force=True)
        else:
            refresh_retriever()
        logger.info("Retriever refresh complete.")
    except Exception as e:
        logger.exception("Background retriever refresh failed: %s", e)


# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------
def _extract_sources_from_artifact(artifact) -> list[str]:
    sources = []
    if not artifact:
        return sources

    docs = artifact if isinstance(artifact, list) else [artifact]
    for doc in docs:
        metadata = getattr(doc, "metadata", None) or {}
        source = metadata.get("source")
        if source and source not in sources:
            sources.append(source)
    return sources


def _run_graph_answer(graph, user_question: str) -> tuple[str, list[str]]:
    """Run LangGraph and return only the final answer plus retrieved sources."""
    final_answer = None
    sources = []

    for chunk in graph.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_question,
                }
            ]
        }
    ):
        if "retrieve" in chunk:
            messages = chunk["retrieve"].get("messages", [])
            if messages:
                artifact = getattr(messages[-1], "artifact", None)
                for source in _extract_sources_from_artifact(artifact):
                    if source not in sources:
                        sources.append(source)

        if "generate_answer" in chunk:
            messages = chunk["generate_answer"].get("messages", [])
            if messages:
                final_answer = messages[-1].content

        if "generate_query_or_respond" in chunk and final_answer is None:
            messages = chunk["generate_query_or_respond"].get("messages", [])
            if messages and not getattr(messages[-1], "tool_calls", None):
                final_answer = messages[-1].content

    return final_answer or "I don't know.", sources


def detect_service_codes(question: str) -> list[str]:
    return list(dict.fromkeys(match.upper() for match in SERVICE_CODE_RE.findall(question.upper())))


def parse_service_price_inputs(question: str) -> dict[str, int]:
    prices = {}
    for code in detect_service_codes(question):
        pattern = re.compile(
            rf"\b{re.escape(code)}\b\s*(?:=|:)?\s*(?:Rp\s*)?([0-9][0-9.,]*)",
            re.IGNORECASE,
        )
        match = pattern.search(question)
        if match:
            raw_price = re.sub(r"[^\d]", "", match.group(1))
            if raw_price:
                prices[code] = int(raw_price)
    return prices


def evaluate_price(harga_input: int, harga_patokan: int, tolerance: float = 0.35) -> dict:
    selisih = harga_input - harga_patokan
    selisih_persen = round((selisih / harga_patokan) * 100, 2) if harga_patokan else None
    batas_toleransi = round(harga_patokan * (1 + tolerance)) if harga_patokan else None
    status = "wajar" if harga_patokan and harga_input <= batas_toleransi else "overprice"
    return {
        "harga_input": harga_input,
        "harga_patokan": harga_patokan,
        "selisih": selisih,
        "selisih_persen": selisih_persen,
        "batas_toleransi_35": batas_toleransi,
        "status": status,
    }


def _format_currency(value) -> str:
    if value is None:
        return "-"
    value = int(value)
    prefix = "-Rp" if value < 0 else "Rp"
    return f"{prefix}{abs(value):,}".replace(",", ".")


def _format_exact_service_answer(codes: list[str], records: list[dict], price_inputs: dict[str, int]) -> tuple[str, list[str]]:
    by_code = {record.get("service_code"): record for record in records}
    sources = []
    lines = ["Berikut hasil berdasarkan knowledge base SiTukang:"]
    total_input = 0
    total_patokan = 0
    statuses = []

    for index, code in enumerate(codes, start=1):
        record = by_code.get(code)
        if not record:
            lines.append(f"{index}. {code}")
            lines.append("   Data harga untuk kode ini belum tersedia di knowledge base SiTukang.")
            continue

        source = record.get("source")
        if source and source not in sources:
            sources.append(source)

        harga_patokan = int(record.get("harga_patokan") or 0)
        total_patokan += harga_patokan
        lines.append(f"{index}. {record.get('service_name', code)}")
        lines.append(f"   Service code: {code}.")
        lines.append(f"   Harga patokan: {_format_currency(harga_patokan)} {record.get('unit', '')}.")
        lines.append(f"   Source key: {record.get('source_key', '-')}.")
        lines.append(f"   Source confidence: {record.get('source_confidence', '-')}.")

        if code in price_inputs:
            harga_input = price_inputs[code]
            total_input += harga_input
            evaluation = evaluate_price(harga_input, harga_patokan)
            statuses.append(evaluation["status"])
            lines.append(f"   Harga input: {_format_currency(harga_input)}.")
            lines.append(
                f"   Selisih: {_format_currency(evaluation['selisih'])} "
                f"atau {evaluation['selisih_persen']}%."
            )
            lines.append(f"   Batas toleransi +35%: {_format_currency(evaluation['batas_toleransi_35'])}.")
            lines.append(f"   Status: {evaluation['status']}.")

    if price_inputs and total_patokan:
        total_eval = evaluate_price(total_input, total_patokan)
        if "overprice" in statuses:
            decision = "perlu klarifikasi / overprice sebagian"
        elif statuses and all(status == "wajar" for status in statuses):
            decision = "pengajuan wajar"
        else:
            decision = total_eval["status"]

        lines.append("")
        lines.append("Keputusan akhir:")
        lines.append(
            f"Total harga input adalah {_format_currency(total_input)}, "
            f"total harga patokan {_format_currency(total_patokan)}, "
            f"dengan selisih {_format_currency(total_eval['selisih'])} "
            f"atau {total_eval['selisih_persen']}%. "
            f"Batas toleransi +35% adalah {_format_currency(total_eval['batas_toleransi_35'])}. "
            f"Status akhir: {decision}."
        )
    if sources:
        lines.append("")
        lines.append("Data diambil dari database harga jasa SiTukang.")

    return "\n".join(lines), sources


def _format_service_search_answer(records: list[dict]) -> tuple[str, list[str]]:
    if not records:
        return "Data harga jasa yang relevan belum ditemukan.", []

    sources = []
    lines = ["Layanan fixed price yang paling relevan:"]
    for index, record in enumerate(records, start=1):
        source = record.get("source")
        if source and source not in sources:
            sources.append(source)
        lines.append(
            f"{index}. {record.get('service_name', '-')}\n"
            f"   Service code: {record.get('service_code', '-')}.\n"
            f"   Harga patokan: {_format_currency(record.get('harga_patokan'))} {record.get('unit', '')}.\n"
            f"   Kategori: {record.get('category', '-')}.\n"
            f"   Source key: {record.get('source_key', '-')}."
        )
    if sources:
        lines.append("")
        lines.append("Data diambil dari database harga jasa SiTukang.")
    return "\n".join(lines), sources


# ------------------------------------------------------------------------------
# Routes — Health
# ------------------------------------------------------------------------------
@app.get("/health", response_model=HealthResponse, tags=["ops"])
async def health_check():
    """
    Liveness / readiness probe.
    Azure Container Apps calls this to determine if the container is healthy.
    """
    qdrant_status = "ok"
    amqp_status = "ok" if not settings.USE_AMQP else "unchecked"

    # Check Qdrant connectivity
    try:
        client = get_qdrant_client()
        client.get_collections()
    except Exception as exc:
        logger.warning("Qdrant health check failed: %s", exc)
        qdrant_status = f"error: {exc}"

    # Check AMQP connectivity (only if configured)
    if settings.USE_AMQP:
        try:
            _get_amqp_channel()
            amqp_status = "ok"
        except Exception as exc:
            logger.warning("AMQP health check failed: %s", exc)
            amqp_status = f"error: {exc}"

    overall = "healthy" if "error" not in qdrant_status and "error" not in amqp_status else "degraded"
    return HealthResponse(
        status=overall,
        qdrant=qdrant_status,
        amqp=amqp_status,
        version=APP_VERSION,
    )


# ------------------------------------------------------------------------------
# Routes — Ask
# ------------------------------------------------------------------------------
@app.post("/ask", response_model=AnswerResponse, tags=["rag"])
async def ask_question(request: QuestionRequest):
    """
    Ask a question to the Agentic RAG pipeline.
    Returns the final answer and simple source citations.
    """
    start = time.perf_counter()
    try:
        question = request.question.strip()
        if not question:
            raise HTTPException(status_code=400, detail="Question cannot be empty")

        service_codes = detect_service_codes(question)
        if service_codes:
            records = lookup_service_codes(service_codes)
            price_inputs = parse_service_price_inputs(question)
            answer_text, sources = _format_exact_service_answer(service_codes, records, price_inputs)
            elapsed = time.perf_counter() - start
            return AnswerResponse(answer=answer_text, sources=sources, processing_time=f"{elapsed:.2f}")

        if PRICE_QUERY_RE.search(question):
            records = search_service_fixed_prices(question)
            answer_text, sources = _format_service_search_answer(records)
            elapsed = time.perf_counter() - start
            return AnswerResponse(answer=answer_text, sources=sources, processing_time=f"{elapsed:.2f}")

        global _graph
        if _graph is None:
            _compile_global_graph(refresh_tools=False)

        answer_text, sources = _run_graph_answer(_graph, question)
        elapsed = time.perf_counter() - start
        return AnswerResponse(answer=answer_text, sources=sources, processing_time=f"{elapsed:.2f}")
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Error in /ask: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error")


# ------------------------------------------------------------------------------
# Routes — Inject (async via AMQP or sync fallback)
# ------------------------------------------------------------------------------
@app.post("/inject", status_code=202, tags=["knowledge"])
async def inject_urls(request: UrlInjectionRequest, background_tasks: BackgroundTasks):
    """
    Inject URLs into the vector store.

    - **With CloudAMQP configured**: Returns 202 immediately; a separate worker
      container processes the injection asynchronously.
    - **Without CloudAMQP**: Falls back to synchronous processing (may be slow).
    """
    if not request.urls:
        raise HTTPException(status_code=400, detail="No URLs provided")

    # ── Async path via AMQP ──────────────────────────────────────────────────
    if settings.USE_AMQP:
        try:
            job_id = str(uuid.uuid4())
            _publish_inject_job(job_id, request.urls)
            return InjectJobResponse(
                status="queued",
                job_id=job_id,
                message=f"Job queued. {len(request.urls)} URL(s) will be processed by the worker.",
                url_count=len(request.urls),
            )
        except Exception as e:
            logger.exception("Failed to publish inject job to AMQP: %s", e)
            raise HTTPException(status_code=503, detail="Message broker unavailable. Try again later.")

    # ── Sync fallback (no AMQP) ──────────────────────────────────────────────
    try:
        added_count, errors = add_urls_to_vectorstore(request.urls)
        background_tasks.add_task(refresh_retriever_background, True)

        if errors:
            return InjectSyncResponse(
                status="partial_success",
                message=f"Added {added_count} chunks with {len(errors)} error(s)",
                added_count=added_count,
                errors=errors,
            )
        return InjectSyncResponse(
            status="success",
            message=f"Successfully added {added_count} chunks",
            added_count=added_count,
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Unexpected error in /inject: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error")


# ------------------------------------------------------------------------------
# Routes — Delete
# ------------------------------------------------------------------------------
@app.post("/delete_by_metadata", tags=["knowledge"])
async def delete_by_metadata_endpoint(request: DeleteRequest, background_tasks: BackgroundTasks):
    """Delete vectors by metadata value (e.g., URL)."""
    try:
        if not request.url:
            raise HTTPException(status_code=400, detail="Missing 'url' in request")

        deleted_count = delete_by_metadata(request.url)
        background_tasks.add_task(refresh_retriever_background, True)

        if deleted_count > 0:
            return {
                "message": f"Successfully deleted {deleted_count} chunks with metadata '{request.url}'",
                "deleted_count": deleted_count,
                "status": "success",
            }
        else:
            return {
                "message": f"No chunks found with metadata '{request.url}'",
                "deleted_count": 0,
                "status": "no_match",
            }
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Error in /delete_by_metadata: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error")


# ------------------------------------------------------------------------------
# Routes — Metadata / Debug
# ------------------------------------------------------------------------------
@app.get("/metadata/counts", response_model=MetadataQueryResponse, tags=["knowledge"])
async def get_metadata_counts_endpoint():
    """Get counts of chunks by metadata source."""
    try:
        counts = get_metadata_counts()
        return MetadataQueryResponse(metadata_counts=counts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/debug/points", tags=["debug"])
async def debug_points(limit: int = 1000):
    """Debug endpoint to inspect what's stored in Qdrant."""
    try:
        client = get_qdrant_client()
        points, _ = client.scroll(
            collection_name=settings.COLLECTION_NAME,
            limit=limit,
            with_payload=True,
            with_vectors=False,
        )
        debug_points = [
            {"id": str(point.id), "payload": point.payload}
            for point in points
        ]
        return {"count": len(debug_points), "points": debug_points}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/config", tags=["ops"])
async def get_config():
    """Return current model configuration (no secrets)."""
    ss = settings.EMBEDDINGS_MODEL
    return {
        "llm_model": settings.LLM_MODEL,
        "embeddings_model": ss.rsplit("/", 1)[-1],
        "amqp_enabled": settings.USE_AMQP,
        "version": APP_VERSION,
    }


# ------------------------------------------------------------------------------
# Static files — serve embedded Vue dist
# ------------------------------------------------------------------------------
app.mount("/", StaticFiles(directory=str(BASE_DIR / "dist"), html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
