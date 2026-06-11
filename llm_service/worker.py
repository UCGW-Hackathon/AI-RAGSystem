"""
AMQP Worker — AI-RAGSystem
Subscribes to the `rag.inject` queue on CloudAMQP and processes URL injection
jobs asynchronously. Runs as a separate container alongside the FastAPI service.

Usage:
    python worker.py

Environment variables (same as main service + CLOUDAMQP_URL required):
    CLOUDAMQP_URL       amqps://user:pass@host/vhost
    AMQP_QUEUE_INJECT   rag.inject  (default)
    AMQP_EXCHANGE       rag         (default)
    WORKER_PREFETCH_COUNT  1        (default, one job at a time)
    WORKER_MAX_RETRIES     3        (default)
"""

import sys
import json
import logging
import os
import signal
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

import pika
import pika.exceptions

from config import settings
from vectordb import add_urls_to_vectorstore, initialize_vectorstore

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger("rag_worker")

# ── Shutdown flag ─────────────────────────────────────────────────────────────
_shutdown = False


def _handle_sigterm(signum, frame):
    global _shutdown
    logger.info("Received SIGTERM — initiating graceful shutdown.")
    _shutdown = True


signal.signal(signal.SIGTERM, _handle_sigterm)
signal.signal(signal.SIGINT, _handle_sigterm)


# ── AMQP helpers ──────────────────────────────────────────────────────────────
def _connect(retry_delay: float = 5.0) -> pika.BlockingConnection:
    """Establish AMQP connection with infinite retry (exits on _shutdown)."""
    if not settings.CLOUDAMQP_URL:
        raise RuntimeError(
            "CLOUDAMQP_URL is not set. Worker cannot start without a message broker."
        )

    params = pika.URLParameters(settings.CLOUDAMQP_URL)
    params.socket_timeout = 10
    params.heartbeat = 60
    params.blocked_connection_timeout = 300

    while not _shutdown:
        try:
            connection = pika.BlockingConnection(params)
            logger.info("Connected to CloudAMQP broker.")
            return connection
        except Exception as exc:
            logger.warning(
                "AMQP connection failed (%s). Retrying in %.0fs...", exc, retry_delay
            )
            time.sleep(retry_delay)

    raise RuntimeError("Worker shutting down before connection was established.")


def _setup_channel(connection: pika.BlockingConnection) -> pika.channel.Channel:
    """Declare exchange, DLQ, and main queue; set QoS."""
    channel = connection.channel()

    dlq_name = f"{settings.AMQP_QUEUE_INJECT}.dlq"

    # Dead-letter queue (messages land here after exhausting retries)
    channel.queue_declare(queue=dlq_name, durable=True)

    # Main exchange
    channel.exchange_declare(
        exchange=settings.AMQP_EXCHANGE,
        exchange_type="direct",
        durable=True,
    )

    # Main queue with DLQ routing
    channel.queue_declare(
        queue=settings.AMQP_QUEUE_INJECT,
        durable=True,
        arguments={
            "x-dead-letter-exchange": "",
            "x-dead-letter-routing-key": dlq_name,
            "x-message-ttl": 3_600_000,  # 1 hour
        },
    )
    channel.queue_bind(
        queue=settings.AMQP_QUEUE_INJECT,
        exchange=settings.AMQP_EXCHANGE,
        routing_key=settings.AMQP_QUEUE_INJECT,
    )

    # Process one message at a time (prevent overloading on heavy embedding jobs)
    channel.basic_qos(prefetch_count=settings.WORKER_PREFETCH_COUNT)

    logger.info(
        "Channel ready — exchange=%s queue=%s dlq=%s",
        settings.AMQP_EXCHANGE,
        settings.AMQP_QUEUE_INJECT,
        dlq_name,
    )
    return channel


# ── Job processing ────────────────────────────────────────────────────────────
def _get_retry_count(properties: pika.BasicProperties) -> int:
    """Extract x-retry-count header from message properties."""
    headers = properties.headers or {}
    return int(headers.get("x-retry-count", 0))


def _process_job(body: bytes) -> None:
    """
    Parse and process a single inject job.
    Raises on failure so the caller can handle ack/nack.
    """
    payload = json.loads(body)
    job_id = payload.get("job_id", "unknown")
    urls: list[str] = payload.get("urls", [])

    logger.info("Processing job_id=%s  urls=%d", job_id, len(urls))

    if not urls:
        logger.warning("Job %s has no URLs — skipping.", job_id)
        return

    added, errors = add_urls_to_vectorstore(urls)
    logger.info("Job %s: added=%d  errors=%d", job_id, added, len(errors))

    if errors:
        # Log each error but don't fail the whole job if some URLs succeeded
        for err in errors:
            logger.warning("Job %s URL error: %s", job_id, err)

    # Refresh the in-process retriever if the worker is collocated with the API
    # (no-op when running in a separate container, API refreshes on next request)
    try:
        initialize_vectorstore()
        logger.info("Job %s: vectorstore refreshed.", job_id)
    except Exception as exc:
        logger.warning("Job %s: vectorstore refresh failed: %s", job_id, exc)


def _on_message(
    channel: pika.channel.Channel,
    method: pika.spec.Basic.Deliver,
    properties: pika.BasicProperties,
    body: bytes,
) -> None:
    """Callback invoked for each AMQP message."""
    retry_count = _get_retry_count(properties)
    logger.debug(
        "Received message delivery_tag=%s retry=%d", method.delivery_tag, retry_count
    )

    try:
        _process_job(body)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        logger.info("Message acked (delivery_tag=%s)", method.delivery_tag)

    except json.JSONDecodeError as exc:
        # Malformed message — send to DLQ immediately (no retry)
        logger.error("Malformed JSON in message — sending to DLQ: %s", exc)
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    except Exception as exc:
        logger.exception("Job processing failed (retry=%d): %s", retry_count, exc)

        if retry_count < settings.WORKER_MAX_RETRIES:
            # Requeue with incremented retry count
            updated_headers = dict(properties.headers or {})
            updated_headers["x-retry-count"] = retry_count + 1

            channel.basic_publish(
                exchange=settings.AMQP_EXCHANGE,
                routing_key=settings.AMQP_QUEUE_INJECT,
                body=body,
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    content_type=properties.content_type or "application/json",
                    message_id=properties.message_id,
                    headers=updated_headers,
                ),
            )
            channel.basic_ack(delivery_tag=method.delivery_tag)
            logger.warning(
                "Job requeued (retry %d/%d)", retry_count + 1, settings.WORKER_MAX_RETRIES
            )
        else:
            # Exhausted retries — send to DLQ
            logger.error(
                "Job exceeded max retries (%d) — sending to DLQ.", settings.WORKER_MAX_RETRIES
            )
            channel.basic_nack(delivery_tag=method.delivery_tag, requeue=False)


# ── Main loop ─────────────────────────────────────────────────────────────────
def run_worker() -> None:
    logger.info(
        "RAG Worker starting — queue=%s  max_retries=%d",
        settings.AMQP_QUEUE_INJECT,
        settings.WORKER_MAX_RETRIES,
    )

    while not _shutdown:
        connection = None
        try:
            connection = _connect()
            channel = _setup_channel(connection)

            channel.basic_consume(
                queue=settings.AMQP_QUEUE_INJECT,
                on_message_callback=_on_message,
                auto_ack=False,
            )

            logger.info("Worker ready — waiting for messages. Press Ctrl+C to exit.")

            while not _shutdown:
                connection.process_data_events(time_limit=1)

        except pika.exceptions.AMQPConnectionError as exc:
            logger.warning("AMQP connection lost: %s — reconnecting...", exc)
            time.sleep(3)

        except Exception as exc:
            logger.exception("Unexpected worker error: %s", exc)
            time.sleep(5)

        finally:
            if connection and not connection.is_closed:
                try:
                    connection.close()
                except Exception:
                    pass

    logger.info("Worker stopped gracefully.")


if __name__ == "__main__":
    run_worker()
