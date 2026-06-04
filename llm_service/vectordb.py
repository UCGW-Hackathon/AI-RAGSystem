from typing import List ,Dict, Tuple, Any
from fastapi import HTTPException
from config import settings
import os

if settings.USER_AGENT:
    os.environ.setdefault("USER_AGENT", settings.USER_AGENT)

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import FieldCondition, Filter, MatchValue, PayloadSchemaType, VectorParams, Distance
from collections import defaultdict
import json
import re
import requests

import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=settings.EMBEDDINGS_MODEL,
        model_kwargs={'device': "cpu"}
    )

def get_qdrant_client():
    if settings.QDRANT_URL:
        return QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
        )

    return QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)


INDEXED_PAYLOAD_FIELDS = [
    "doc_type",
    "service_code",
    "category",
    "source_url",
    "source_key",
]


def ensure_payload_indexes(client: QdrantClient) -> None:
    """
    Create keyword indexes for fields commonly used in exact filters.
    LangChain stores document metadata under `metadata.*`, while older/manual
    points may store fields directly, so index both shapes.
    """
    for field in INDEXED_PAYLOAD_FIELDS:
        for key in (field, f"metadata.{field}"):
            try:
                client.create_payload_index(
                    collection_name=settings.COLLECTION_NAME,
                    field_name=key,
                    field_schema=PayloadSchemaType.KEYWORD,
                )
            except Exception as exc:
                message = str(exc).lower()
                if "already exists" not in message and "index" not in message:
                    logger.debug("Skipping payload index %s: %s", key, exc)


def _normalize_service_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    metadata = payload.get("metadata") if isinstance(payload.get("metadata"), dict) else {}
    merged = {**payload, **metadata}
    if "source" not in merged:
        merged["source"] = merged.get("source_url")
    return merged


def _build_exact_filter(code: str, nested: bool = True) -> Filter:
    prefix = "metadata." if nested else ""
    return Filter(
        must=[
            FieldCondition(
                key=f"{prefix}doc_type",
                match=MatchValue(value="service_fixed_price"),
            ),
            FieldCondition(
                key=f"{prefix}service_code",
                match=MatchValue(value=code),
            ),
        ]
    )


def _service_fixed_price_filter() -> Filter:
    return Filter(
        should=[
            FieldCondition(key="metadata.doc_type", match=MatchValue(value="service_fixed_price")),
            FieldCondition(key="doc_type", match=MatchValue(value="service_fixed_price")),
        ]
    )


def lookup_service_codes(codes: List[str]) -> List[Dict[str, Any]]:
    """
    Exact service lookup by service_code. This intentionally avoids vector search.
    """
    client = get_qdrant_client()
    ensure_payload_indexes(client)
    records = []

    for code in dict.fromkeys(code.upper() for code in codes):
        found = []
        for nested in (True, False):
            points, _ = client.scroll(
                collection_name=settings.COLLECTION_NAME,
                scroll_filter=_build_exact_filter(code, nested=nested),
                limit=10,
                with_payload=True,
                with_vectors=False,
            )
            if points:
                found = points
                break

        for point in found:
            record = _normalize_service_payload(point.payload or {})
            record["point_id"] = str(point.id)
            records.append(record)

    return records


def search_service_fixed_prices(query: str, limit: int = 4) -> List[Dict[str, Any]]:
    """
    Semantic search for fixed-price services, constrained to service_fixed_price docs.
    """
    client = get_qdrant_client()
    ensure_payload_indexes(client)

    lexical_records = _lexical_search_service_fixed_prices(client, query, limit=limit)
    if lexical_records:
        return lexical_records

    embeddings = get_embeddings()
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding=embeddings,
    )
    docs = vector_store.similarity_search(query, k=limit, filter=_service_fixed_price_filter())
    return [_normalize_service_payload(doc.metadata or {}) | {"page_content": doc.page_content} for doc in docs]


def _lexical_search_service_fixed_prices(client: QdrantClient, query: str, limit: int = 4) -> List[Dict[str, Any]]:
    query_text = query.lower()
    query_tokens = {
        token
        for token in re.findall(r"[a-zA-Z0-9]+", query_text)
        if len(token) > 1 and token not in {"rp", "berapa", "harga", "biaya", "jasa", "layanan"}
    }
    if not query_tokens:
        return []

    points, _ = client.scroll(
        collection_name=settings.COLLECTION_NAME,
        scroll_filter=_service_fixed_price_filter(),
        limit=1000,
        with_payload=True,
        with_vectors=False,
    )

    scored = []
    for point in points:
        record = _normalize_service_payload(point.payload or {})
        searchable = " ".join(
            str(value or "")
            for value in (
                record.get("service_code"),
                record.get("service_name"),
                record.get("category"),
                record.get("page_content"),
            )
        ).lower()

        searchable_tokens = set(re.findall(r"[a-zA-Z0-9]+", searchable))
        score = sum(1 for token in query_tokens if token in searchable_tokens)
        if query_text in searchable:
            score += 5
        if record.get("service_name") and str(record["service_name"]).lower() in query_text:
            score += 3

        if score:
            record["point_id"] = str(point.id)
            scored.append((score, record))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [record for _, record in scored[:limit]]


def _jsonl_url_to_documents(source_url: str) -> List[Document]:
    response = requests.get(source_url, timeout=30)
    response.raise_for_status()

    documents = []
    for line_number, raw_line in enumerate(response.text.splitlines(), start=1):
        raw_line = raw_line.strip()
        if not raw_line:
            continue

        item = json.loads(raw_line)
        metadata = {
            "doc_type": item.get("doc_type"),
            "service_code": item.get("service_code"),
            "service_name": item.get("service_name"),
            "category": item.get("category"),
            "harga_patokan": item.get("harga_patokan"),
            "unit": item.get("unit"),
            "source_key": item.get("source_key"),
            "source_confidence": item.get("source_confidence"),
            "source_url": item.get("source_url"),
            "source": source_url,
            "jsonl_line": line_number,
        }
        metadata = {key: value for key, value in metadata.items() if value is not None}
        page_content = item.get("embedding_text") or json.dumps(item, ensure_ascii=False)
        documents.append(Document(page_content=page_content, metadata=metadata))

    return documents

def add_urls_to_vectorstore(urls: List[str], vector_store: QdrantVectorStore = None) -> Tuple[int, List[str]]:
    errors = []
    total_added_chunks = 0
    
    try:
        if vector_store is None:
            embeddings = get_embeddings()
            client = get_qdrant_client()
            if not client.collection_exists(settings.COLLECTION_NAME):
                vector_size = len(embeddings.embed_query("sample text"))
                client.create_collection(
                    collection_name=settings.COLLECTION_NAME,
                    vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
                )
            ensure_payload_indexes(client)
            vector_store = QdrantVectorStore(
                client=client,
                collection_name=settings.COLLECTION_NAME,
                embedding=embeddings,
            )
    except Exception as e:
        logger.error(f"Vector store initialization failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Vector store initialization failed: {str(e)}")

    for a_url in urls:
        try:
            logger.info("Processing URL: %s", a_url)
            if a_url.lower().split("?", 1)[0].endswith(".jsonl"):
                doc_splits = _jsonl_url_to_documents(a_url)
            else:
                docs = WebBaseLoader(a_url).load()
                docs_list = [docs] if not isinstance(docs, list) else docs

                for doc in docs_list:
                    doc.page_content = re.sub(r'\s+', ' ', doc.page_content.strip())

                text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                    chunk_size=200, chunk_overlap=50
                )
                doc_splits = text_splitter.split_documents(docs_list)
                
                for doc in doc_splits:
                    doc.metadata.pop("description", None)  # Safely remove description

            logger.info("Created %s chunks from URL: %s", len(doc_splits), a_url)

            vector_store.add_documents(
                documents=doc_splits, 
                wait=True
            )
            total_added_chunks += len(doc_splits)
            logger.info("Added %s documents to vector store", len(doc_splits))

        except Exception as e:
            error_msg = f"Failed processing URL {a_url}: {str(e)}"
            logger.error(error_msg)
            errors.append(error_msg)
            continue  # Continue with next URL

    return total_added_chunks, errors


def initialize_vectorstore():
    embeddings = get_embeddings()
    client = get_qdrant_client()

    if not client.collection_exists(settings.COLLECTION_NAME):
        vector_size = len(embeddings.embed_query("sample text"))

        client.create_collection(
            collection_name=settings.COLLECTION_NAME,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )
    ensure_payload_indexes(client)

    vector_store = QdrantVectorStore(
        client=client,
        collection_name=settings.COLLECTION_NAME,
        embedding=embeddings,
    )
                
    return vector_store.as_retriever()


def get_metadata_counts() -> Dict[str, int]:
    """Get counts of chunks by metadata"""
    client = get_qdrant_client()
    counts = defaultdict(int)
    
    # Scroll through all points to collect metadata counts
    next_offset = None
    while True:
        points, next_offset = client.scroll(
            collection_name=settings.COLLECTION_NAME,
            limit=1000,
            offset=next_offset,
            with_payload=True
        )
        
        if not points:
            break
            
        for point in points:
            # Check different possible ways metadata might be stored
            if point.payload:
                # Try direct source field
                if 'source' in point.payload:
                    source = point.payload['source']
                    counts[source] += 1
                # Try metadata.source field
                elif 'metadata' in point.payload and isinstance(point.payload['metadata'], dict):
                    metadata = point.payload['metadata']
                    if 'source' in metadata:
                        source = metadata['source']
                        counts[source] += 1
        
        if next_offset is None:
            break
            
    return dict(counts)

def delete_by_metadata(metadata_value: str) -> int:
    """Delete vectors by metadata value using a more direct approach
    
       There are better ways , but i prefer with  more control
    """
    client = get_qdrant_client()
    
    # Scroll through all points to find those with matching metadata
    points_to_delete = []
    next_offset = None
    
    while True:
        points, next_offset = client.scroll(
            collection_name=settings.COLLECTION_NAME,
            limit=1000,
            offset=next_offset,
            with_payload=True
        )
        
        if not points:
            break
            
        for point in points:
            # Check different possible ways metadata might be stored
            payload = point.payload
            if payload:
                # Check direct source field
                if "source" in payload and payload["source"] == metadata_value:
                    points_to_delete.append(point.id)
                # Check nested metadata.source field
                elif ("metadata" in payload and 
                      isinstance(payload["metadata"], dict) and 
                      "source" in payload["metadata"] and 
                      payload["metadata"]["source"] == metadata_value):
                    points_to_delete.append(point.id)
        
        if next_offset is None:
            break
    
    logger.info("Found %s points to delete", len(points_to_delete))
    
    # Delete the points by their IDs
    if points_to_delete:
        client.delete(
            collection_name=settings.COLLECTION_NAME,
            points_selector=points_to_delete
        )
    
    return len(points_to_delete)

