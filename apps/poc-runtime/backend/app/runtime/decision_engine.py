# implements: runtime-spec, runtime/DECISION_ENGINE.md

"""Decision engine — six governed actions with narrow refuse semantics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.audit.schema import DecisionAction
from app.config.settings import load_runtime_config
from app.connectors.saleswon.base import ConnectorNotConfigured
from app.intent.schemas import Intent
from app.security.user_context import ScopeDenied


REFUSE_STATUSES = frozenset(
    {"scope_denied", "unsupported_action", "unsafe_write", "missing_authority"}
)


@dataclass
class DecisionResult:
    decision_action: DecisionAction
    confidence_score: float
    status: str | None = None
    source_references: list[str] | None = None
    context: dict[str, Any] | None = None


class DecisionEngine:
    def __init__(self) -> None:
        config = load_runtime_config()
        thresholds = config.get("governance", {}).get("confidence_thresholds", {})
        self._high = thresholds.get("high", 0.85)
        self._medium = thresholds.get("medium", 0.60)

    def decide_read(
        self,
        intent: Intent,
        confidence: float,
        records: list[Any] | None = None,
        connector_error: Exception | None = None,
    ) -> DecisionResult:
        if connector_error:
            if isinstance(connector_error, ConnectorNotConfigured):
                return DecisionResult(
                    decision_action=DecisionAction.RETRIEVE,
                    confidence_score=confidence,
                    status="connector_pending_credentials",
                    source_references=[],
                    context={"intent": intent.value},
                )
            return DecisionResult(
                decision_action=DecisionAction.ESCALATE,
                confidence_score=confidence,
                status="retrieval_error",
                source_references=[],
            )

        refs = [getattr(r, "sys_id", str(r)) for r in (records or [])]
        if confidence >= self._high:
            return DecisionResult(
                decision_action=DecisionAction.ANSWER,
                confidence_score=confidence,
                source_references=refs,
                context={"records": records or []},
            )
        if confidence >= self._medium:
            return DecisionResult(
                decision_action=DecisionAction.ANSWER,
                confidence_score=confidence,
                status="answer_with_caveat",
                source_references=refs,
                context={"records": records or []},
            )
        return DecisionResult(
            decision_action=DecisionAction.ASK,
            confidence_score=confidence,
            status="low_confidence",
        )

    def decide_ask(
        self, missing_fields: list[str], confidence: float
    ) -> DecisionResult:
        return DecisionResult(
            decision_action=DecisionAction.ASK,
            confidence_score=confidence,
            context={"missing_fields": missing_fields},
        )

    def decide_refuse(self, status: str, confidence: float = 1.0) -> DecisionResult:
        if status not in REFUSE_STATUSES:
            raise ValueError(f"Invalid refuse status: {status}")
        return DecisionResult(
            decision_action=DecisionAction.REFUSE,
            confidence_score=confidence,
            status=status,
            source_references=[],
        )

    def decide_unsupported(self, confidence: float) -> DecisionResult:
        return self.decide_refuse("unsupported_action", confidence)

    def decide_recommend(
        self, proposed_action: dict[str, Any], confidence: float
    ) -> DecisionResult:
        return DecisionResult(
            decision_action=DecisionAction.RECOMMEND,
            confidence_score=confidence,
            context={"proposed_action": proposed_action},
        )

    def decide_write_result(
        self,
        confidence: float,
        connector_error: Exception | None = None,
        write_result: Any | None = None,
    ) -> DecisionResult:
        if connector_error:
            if isinstance(connector_error, ConnectorNotConfigured):
                return DecisionResult(
                    decision_action=DecisionAction.RETRIEVE,
                    confidence_score=confidence,
                    status="connector_pending_credentials",
                    source_references=[],
                )
            return DecisionResult(
                decision_action=DecisionAction.ESCALATE,
                confidence_score=confidence,
                status="write_error",
            )
        sys_id = getattr(write_result, "sys_id", None)
        refs = [sys_id] if sys_id else []
        return DecisionResult(
            decision_action=DecisionAction.ANSWER,
            confidence_score=confidence,
            source_references=refs,
            context={"write_result": write_result},
        )

    @staticmethod
    def from_scope_denied(error: ScopeDenied) -> DecisionResult:
        return DecisionResult(
            decision_action=DecisionAction.REFUSE,
            confidence_score=1.0,
            status=error.reason,
            source_references=[],
        )
