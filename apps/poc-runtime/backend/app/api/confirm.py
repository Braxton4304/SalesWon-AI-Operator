# implements: platform/api.md, governance-spec

"""Confirmation API for pending write actions."""

from __future__ import annotations

from pydantic import BaseModel

from app.audit.schema import DecisionAction
from app.security.user_context import CurrentUserContext, get_current_user_context
from app.workflows.chat_orchestrator import get_chat_orchestrator
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/chat", tags=["chat"])


class ConfirmRequest(BaseModel):
    pending_confirmation_id: str
    session_id: str | None = None


class ConfirmResponse(BaseModel):
    response_payload: str
    decision_action: DecisionAction
    confidence_score: float
    source_references: list[str]
    audit_id: str
    status: str | None = None


@router.post("/confirm", response_model=ConfirmResponse)
def post_confirm(
    body: ConfirmRequest,
    ctx: CurrentUserContext = Depends(get_current_user_context),
) -> ConfirmResponse:
    orchestrator = get_chat_orchestrator()
    result = orchestrator.handle_confirm(
        ctx, body.pending_confirmation_id, body.session_id
    )
    return ConfirmResponse(
        response_payload=result.response_payload,
        decision_action=result.decision_action,
        confidence_score=result.confidence_score,
        source_references=result.source_references,
        audit_id=result.audit_id,
        status=result.status,
    )
