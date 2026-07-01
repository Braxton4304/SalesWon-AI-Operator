# implements: runtime-spec

"""Plan execution result — separate module to avoid import cycles."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.intent.schemas import Intent
from app.runtime.decision_engine import DecisionResult


@dataclass
class PlanExecutionResult:
    decision: DecisionResult
    intent: Intent
    records: list[Any] = field(default_factory=list)
    proposed_action: dict[str, Any] | None = None
    pending_confirmation_id: str | None = None
    primary_agent: str = "sales-rep"
    response_payload: str | None = None
    audit_id: str | None = None
