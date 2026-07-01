# implements: platform/servicenow.md, platform/DATA_DICTIONARY.md

"""ServiceNow-backed SalesWon connector shell."""

from __future__ import annotations

from typing import Any

from app.config.settings import get_settings
from app.connectors.saleswon.base import (
    ConnectorNotConfigured,
    Record,
    SalesWonConnector,
    WriteResult,
)
from app.connectors.servicenow.adapter import ServiceNowAdapter
from app.planning.mapping_loader import get_table
from app.security.user_context import CurrentUserContext


class ServiceNowSalesWonConnector(SalesWonConnector):
    def __init__(self, adapter: ServiceNowAdapter | None = None) -> None:
        self._adapter = adapter or ServiceNowAdapter()
        self._settings = get_settings()

    def _ensure_configured(self) -> None:
        if not self._settings.servicenow_configured:
            raise ConnectorNotConfigured(
                "ServiceNow credentials not configured. Set SERVICENOW_* env vars."
            )

    def search_opportunities(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        self._ensure_configured()
        return self._adapter.query_table(
            table=get_table("opportunity"),
            filters=filters or {},
            ctx=ctx,
        )

    def search_activities(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        self._ensure_configured()
        return self._adapter.query_table(
            table=get_table("activity"),
            filters=filters or {},
            ctx=ctx,
        )

    def search_accounts(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        self._ensure_configured()
        return self._adapter.query_table(
            table=get_table("account"),
            filters=filters or {},
            ctx=ctx,
        )

    def get_record(
        self, ctx: CurrentUserContext, object_type: str, sys_id: str
    ) -> Record:
        self._ensure_configured()
        table = get_table(object_type)
        return self._adapter.get_record(table=table, sys_id=sys_id, ctx=ctx)

    def update_activity(
        self, ctx: CurrentUserContext, sys_id: str, patch: dict[str, Any]
    ) -> WriteResult:
        self._ensure_configured()
        return self._adapter.update_record(
            table=get_table("activity"),
            sys_id=sys_id,
            patch=patch,
            ctx=ctx,
        )
