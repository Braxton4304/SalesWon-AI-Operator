# implements: governance-spec, runtime-spec, data-spec

"""Pytest tests for POC runtime."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.audit.logger import AuditLogger
from app.audit.schema import AuditOutcome, DecisionAction
from app.connectors.saleswon.base import ConnectorNotConfigured, Record, SalesWonConnector, WriteResult
from app.intent.schemas import Intent
from app.llm.rule_based import RuleBasedLLMProvider
from app.runtime.decision_engine import DecisionEngine
from app.security.user_context import CurrentUserContext, ScopeEnforcer
from app.workflows.activity_update import ActivityUpdateWorkflow
from app.workflows.chat_orchestrator import ChatOrchestrator


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


@pytest.fixture
def alice_ctx():
    return CurrentUserContext(user_id="alice", tenant_id="dev-tenant")


@pytest.fixture
def audit_tmp(tmp_path):
    log_path = tmp_path / "audit.jsonl"
    return AuditLogger(str(log_path)), log_path


def test_decision_engine_connector_pending_read():
    engine = DecisionEngine()
    result = engine.decide_read(
        Intent.SEARCH_OPPORTUNITIES,
        0.88,
        connector_error=ConnectorNotConfigured(),
    )
    assert result.decision_action == DecisionAction.RETRIEVE
    assert result.status == "connector_pending_credentials"
    assert result.source_references == []


def test_decision_engine_refuse_only_for_allowed_statuses():
    engine = DecisionEngine()
    result = engine.decide_refuse("scope_denied")
    assert result.decision_action == DecisionAction.REFUSE
    assert result.status == "scope_denied"

    with pytest.raises(ValueError):
        engine.decide_refuse("connector_pending_credentials")


def test_scope_enforcer_blocks_cross_owner(alice_ctx):
    enforcer = ScopeEnforcer()
    record = {"owner": "bob", "tenant_id": "dev-tenant", "team_visibility": []}
    with pytest.raises(Exception) as exc:
        enforcer.assert_record_visible(alice_ctx, record)
    assert exc.value.reason == "scope_denied"


def test_scope_enforcer_applies_read_filters(alice_ctx):
    enforcer = ScopeEnforcer()
    filters = enforcer.apply_read_filters(alice_ctx, {"stage": "open"})
    assert filters["tenant_id"] == "dev-tenant"
    assert filters["owner"] == "alice"
    assert filters["stage"] == "open"


def test_audit_logger_writes_jsonl(audit_tmp, alice_ctx):
    logger, log_path = audit_tmp
    from app.audit.schema import AuditRecord

    record = AuditRecord(
        tenant_id=alice_ctx.tenant_id,
        actor=alice_ctx.user_id,
        decision_action=DecisionAction.RETRIEVE,
        confidence_score=0.88,
        outcome=AuditOutcome.PENDING,
        status="connector_pending_credentials",
    )
    logger.write(record)
    lines = log_path.read_text(encoding="utf-8").strip().split("\n")
    parsed = json.loads(lines[0])
    assert parsed["decision_action"] == "retrieve"
    assert parsed["status"] == "connector_pending_credentials"


def test_activity_update_ask_missing_fields(alice_ctx, audit_tmp):
    logger, _ = audit_tmp
    llm = RuleBasedLLMProvider()
    workflow = ActivityUpdateWorkflow(
        connector=MockConnector(configured=False),
        llm=llm,
    )
    from app.memory.short_term import SessionState

    session = SessionState(session_id="test-session")
    with patch("app.workflows.activity_update.get_audit_logger", return_value=logger):
        response = workflow.prepare_update(
            alice_ctx, session, {"account_name": "ACME"}, 0.90
        )
    assert response.decision_action == DecisionAction.ASK
    assert session.pending_intent == Intent.UPDATE_ACTIVITY.value


def test_activity_update_recommend_then_connector_pending(alice_ctx, audit_tmp):
    logger, _ = audit_tmp
    llm = RuleBasedLLMProvider()
    workflow = ActivityUpdateWorkflow(
        connector=MockConnector(configured=False),
        llm=llm,
    )
    from app.memory.short_term import SessionState
    from app.runtime.clarification import ClarificationStore

    store = ClarificationStore()
    workflow._clarification = store
    session = SessionState(session_id="test-session")

    fields = {
        "sys_id": "a" * 32,
        "account_name": "ACME",
        "status": "done",
    }

    with patch("app.workflows.activity_update.get_audit_logger", return_value=logger):
        prep = workflow.prepare_update(alice_ctx, session, fields, 0.90)
    assert prep.decision_action == DecisionAction.RECOMMEND
    assert prep.pending_confirmation_id

    pending = store.get(prep.pending_confirmation_id)
    assert pending is not None

    with patch("app.workflows.activity_update.get_audit_logger", return_value=logger):
        confirmed = workflow.execute_confirmed(alice_ctx, session, pending)
    assert confirmed.decision_action == DecisionAction.RETRIEVE
    assert confirmed.status == "connector_pending_credentials"


def test_chat_orchestrator_read_connector_pending(alice_ctx, audit_tmp):
    logger, _ = audit_tmp
    orchestrator = ChatOrchestrator(
        connector=MockConnector(configured=False),
        llm=RuleBasedLLMProvider(),
    )
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=logger):
        response = orchestrator.handle_message(alice_ctx, "show my open opportunities")
    assert response.decision_action == DecisionAction.RETRIEVE
    assert response.status == "connector_pending_credentials"
    assert response.source_references == []


def test_chat_orchestrator_unsupported_action(alice_ctx, audit_tmp):
    logger, _ = audit_tmp
    orchestrator = ChatOrchestrator(
        connector=MockConnector(configured=False),
        llm=RuleBasedLLMProvider(),
    )
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=logger):
        response = orchestrator.handle_message(alice_ctx, "send email to customer")
    assert response.decision_action == DecisionAction.REFUSE
    assert response.status == "unsupported_action"


def test_chat_orchestrator_scope_denied(alice_ctx, audit_tmp):
    logger, _ = audit_tmp
    orchestrator = ChatOrchestrator(
        connector=MockConnector(configured=True, owner="bob"),
        llm=RuleBasedLLMProvider(),
    )
    sys_id = "b" * 32
    with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=logger):
        response = orchestrator.handle_message(
            alice_ctx, f"get record sys_id={sys_id}"
        )
    assert response.decision_action == DecisionAction.REFUSE
    assert response.status == "scope_denied"


@pytest.fixture
def client(audit_tmp):
    logger, log_path = audit_tmp
    with patch("app.audit.logger.get_audit_logger", return_value=logger):
        with patch("app.workflows.chat_orchestrator.get_audit_logger", return_value=logger):
            with patch("app.workflows.activity_update.get_audit_logger", return_value=logger):
                from app.main import app

                yield TestClient(app), log_path


def test_chat_api_happy_path(client):
    test_client, log_path = client
    response = test_client.post(
        "/chat",
        json={"message": "show my open opportunities"},
        headers={"X-User-Id": "alice"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["decision_action"] == "retrieve"
    assert data["status"] == "connector_pending_credentials"
    assert data["source_references"] == []
    assert log_path.exists()
