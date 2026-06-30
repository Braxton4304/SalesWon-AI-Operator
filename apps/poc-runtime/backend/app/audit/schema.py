# implements: governance-spec, runtime/GOVERNANCE.md

"""Audit record schema and JSONL logger."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class DecisionAction(str, Enum):
    ANSWER = "answer"
    ASK = "ask"
    RETRIEVE = "retrieve"
    ESCALATE = "escalate"
    REFUSE = "refuse"
    RECOMMEND = "recommend"


class AuditOutcome(str, Enum):
    SUCCESS = "success"
    PENDING = "pending"
    ESCALATED = "escalated"
    REFUSED = "refused"
    ERROR = "error"


class AuditRecord(BaseModel):
    """
    implements: governance-spec audit_required_fields
    """

    tenant_id: str
    correlation_id: str = Field(default_factory=lambda: str(uuid4()))
    actor: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    decision_action: DecisionAction
    confidence_score: float = 0.0
    source_references: list[str] = Field(default_factory=list)
    outcome: AuditOutcome
    agent_id: str = "poc-runtime"
    request_summary: str = ""
    status: str | None = None
    intent: str | None = None
    filters: dict[str, Any] | None = None
    target_object: str | None = None
    proposed_action: dict[str, Any] | None = None
    confirmation: bool | None = None

    def to_jsonl(self) -> str:
        return self.model_dump_json()
