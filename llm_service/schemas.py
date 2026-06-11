from pydantic import BaseModel
from typing import List, Dict, Optional


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
    processing_time: str  # formatted string e.g. "0.42"
    sources: List[str] = []


class UrlInjectionRequest(BaseModel):
    urls: List[str]


class InjectJobResponse(BaseModel):
    """Returned when AMQP is configured — injection handled asynchronously."""
    status: str          # "queued"
    job_id: str
    message: str
    url_count: int


class InjectSyncResponse(BaseModel):
    """Returned when AMQP is NOT configured — synchronous fallback."""
    status: str          # "success" | "partial_success"
    message: str
    added_count: int
    errors: Optional[List[str]] = None


class DeleteRequest(BaseModel):
    url: str


class MetadataQueryResponse(BaseModel):
    metadata_counts: Dict[str, int]


class HealthResponse(BaseModel):
    status: str          # "healthy" | "degraded" | "unhealthy"
    qdrant: str
    amqp: str
    version: str = "1.0.0"


class DebugPoint(BaseModel):
    id: str
    payload: Dict
    vector: List[float]


class DebugResponse(BaseModel):
    points: List[DebugPoint]
