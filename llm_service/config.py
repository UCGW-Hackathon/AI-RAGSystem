import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def _parse_origins(raw: str | None) -> list[str]:
    """Parse comma-separated CORS origins from env var."""
    if not raw:
        return ["*"]
    return [origin.strip() for origin in raw.split(",") if origin.strip()]



@dataclass
class Settings:
    # Qdrant
    QDRANT_URL: str | None = os.getenv("QDRANT_URL")
    QDRANT_API_KEY: str | None = os.getenv("QDRANT_API_KEY")
    QDRANT_HOST: str = os.getenv("QDRANT_HOST", "qdrant")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 6333))
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "my_collection")

    # Embeddings & LLM
    EMBEDDINGS_MODEL: str = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gemini-flash-lite-latest")
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    # App
    USER_AGENT: str = os.getenv("USER_AGENT", "SiTukang-RAG/1.0")
    DOCUMENTS_DIR: str = os.getenv("DOCUMENTS_DIR", "/app/documents")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

    # CORS — comma-separated list, e.g. "https://app.example.com,https://staging.example.com"
    ALLOWED_ORIGINS_RAW: str | None = os.getenv("ALLOWED_ORIGINS")

    # CloudAMQP / RabbitMQ
    # Format: amqps://user:password@host/vhost  (use amqp:// for local dev)
    CLOUDAMQP_URL: str | None = os.getenv("CLOUDAMQP_URL")
    AMQP_QUEUE_INJECT: str = os.getenv("AMQP_QUEUE_INJECT", "rag.inject")
    AMQP_EXCHANGE: str = os.getenv("AMQP_EXCHANGE", "rag")

    # Worker
    WORKER_PREFETCH_COUNT: int = int(os.getenv("WORKER_PREFETCH_COUNT", 1))
    WORKER_MAX_RETRIES: int = int(os.getenv("WORKER_MAX_RETRIES", 3))

    @property
    def ALLOWED_ORIGINS(self) -> list[str]:
        return _parse_origins(self.ALLOWED_ORIGINS_RAW)

    @property
    def USE_AMQP(self) -> bool:
        """True when CloudAMQP is configured — enables async injection."""
        return bool(self.CLOUDAMQP_URL)


settings = Settings()
