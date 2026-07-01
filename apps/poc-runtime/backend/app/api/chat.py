# implements: platform/api.md, governance-spec

"""Chat API schemas and routes."""

from __future__ import annotations

from pydantic import BaseModel, Field

from app.audit.schema import DecisionAction
from app.security.user_context import CurrentUserContext, get_current_user_context
from app.workflows.chat_orchestrator import get_chat_orchestrator
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    response_payload: str
    decision_action: DecisionAction
    confidence_score: float
    source_references: list[str] = Field(default_factory=list)
    audit_id: str
    status: str | None = None
    pending_confirmation_id: str | None = None
    proposed_action: dict | None = None
    session_id: str | None = None
    primary_agent: str | None = None


@router.post("", response_model=ChatResponse)
def post_chat(
    body: ChatRequest,
    ctx: CurrentUserContext = Depends(get_current_user_context),
) -> ChatResponse:
    orchestrator = get_chat_orchestrator()
    result = orchestrator.handle_message(ctx, body.message, body.session_id)
    return ChatResponse(
        response_payload=result.response_payload,
        decision_action=result.decision_action,
        confidence_score=result.confidence_score,
        source_references=result.source_references,
        audit_id=result.audit_id,
        status=result.status,
        pending_confirmation_id=result.pending_confirmation_id,
        proposed_action=result.proposed_action,
        session_id=result.session_id,
        primary_agent=result.primary_agent,
    )
