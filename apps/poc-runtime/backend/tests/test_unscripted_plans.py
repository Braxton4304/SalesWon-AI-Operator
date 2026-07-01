# implements: governance-spec, runtime-spec

"""Unscripted agent planning scenario tests (mocked LLM plans)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from app.audit.logger import AuditLogger
from app.audit.schema import DecisionAction
from app.connectors.saleswon.base import ConnectorNotConfigured, Record, SalesWonConnector, WriteResult
from app.llm.base import LLMProvider
from app.planning.schema import ActionPlan
from app.runtime.prompt_compiler import CompiledPrompt
from app.security.user_context import CurrentUserContext
from app.workflows.chat_orchestrator import ChatOrchestrator


FIXTURES = Path(__file__).parent / "fixtures" / "plans"


class MockConnector(SalesWonConnector):
    def __init__(self, configured: bool = False, owner: str = "alice") -> None:
        self.configured = configured
        self.owner = owner

    def _check(self) -> None:
        if not self.configured:
            raise ConnectorNotConfigured("not configured")

    def search_opportunities(self, ctx, filters=None):
        self._check()
        return []

    def search_activities(self, ctx, filters=None):
        self._check()
        return []

    def search_accounts(self, ctx, filters=None):
        self._check()
        return []

    def get_record(self, ctx, object_type, sys_id):
        self._check()
        return Record(
            sys_id=sys_id,
            object_type=object_type,
            fields={"sys_id": sys_id},
            owner=self.owner,
            tenant_id=ctx.tenant_id,
        )

    def update_activity(self, ctx, sys_id, patch):
        self._check()
        return WriteResult(sys_id=sys_id, object_type="activity", status="updated", fields=patch)


class MockPlanLLM(LLMProvider):
    def __init__(self, plan: ActionPlan) -> None:
        self._plan = plan

    def plan(self, compiled: CompiledPrompt) -> ActionPlan:
        return self._plan

    def generate_response(self, plan, execution, compiled) -> str:
        return f"[mock narrative for {plan.intent}]"


def _load_plan(name: str) -> ActionPlan:
    data = json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))
    return ActionPlan.model_validate(data)


@pytest.fixture
def alice_ctx():
    return CurrentUserContext(user_id="alice", tenant_id="dev-tenant")


@pytest.fixture
def audit_tmp(tmp_path):
    return AuditLogger(str(tmp_path / "audit.jsonl"))


def _orchestrator_with_plan(plan: ActionPlan, connector: MockConnector, logger: AuditLogger):
    llm = MockPlanLLM(plan)
    return ChatOrchestrator(connector=connector, llm=llm)


def test_quarter_deals_retrieve_pending(alice_ctx, audit_tmp):
    plan = _load_plan("quarter_deals")
    orch = _orchestrator_with_plan(plan, MockConnector(configured=False), audit_tmp)
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=audit_tmp):
        response = orch.handle_message(alice_ctx, "What deals are closing this quarter?")
    assert response.decision_action == DecisionAction.RETRIEVE
    assert response.status == "connector_pending_credentials"
    assert response.primary_agent == "sales-rep"


def test_overdue_activities_plan(alice_ctx, audit_tmp):
    plan = _load_plan("overdue_activities")
    orch = _orchestrator_with_plan(plan, MockConnector(configured=False), audit_tmp)
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=audit_tmp):
        response = orch.handle_message(alice_ctx, "Which accounts have overdue activities?")
    assert response.decision_action == DecisionAction.RETRIEVE
    assert response.status == "connector_pending_credentials"


def test_move_followup_friday_recommend_or_ask(alice_ctx, audit_tmp):
    plan = _load_plan("move_followup_friday")
    orch = _orchestrator_with_plan(plan, MockConnector(configured=False), audit_tmp)
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=audit_tmp):
        response = orch.handle_message(alice_ctx, "Move my Acme follow-up to Friday.")
    assert response.decision_action in (DecisionAction.RECOMMEND, DecisionAction.ASK)


def test_mark_acme_call_complete_recommend(alice_ctx, audit_tmp):
    plan = _load_plan("mark_acme_complete")
    orch = _orchestrator_with_plan(plan, MockConnector(configured=False), audit_tmp)
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=audit_tmp):
        response = orch.handle_message(alice_ctx, "Mark the Acme call complete.")
    assert response.decision_action == DecisionAction.RECOMMEND
    assert response.pending_confirmation_id


def test_wrong_user_activity_scope_denied(alice_ctx, audit_tmp):
    plan = _load_plan("wrong_user_update")
    orch = _orchestrator_with_plan(
        plan, MockConnector(configured=True, owner="bob"), audit_tmp
    )
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=audit_tmp):
        with patch("app.workflows.activity_update.get_audit_logger", return_value=audit_tmp):
            sys_id = "a" * 32
            response = orch.handle_message(
                alice_ctx, f"Mark activity sys_id={sys_id} complete for Acme"
            )
    assert response.decision_action == DecisionAction.REFUSE
    assert response.status == "scope_denied"
