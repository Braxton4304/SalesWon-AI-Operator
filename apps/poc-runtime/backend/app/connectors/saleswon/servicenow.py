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
        # TODO: real table name — e.g. opportunity table in ServiceNow SOM
        # TODO: field mapping per platform/DATA_DICTIONARY.md opportunity object
        return self._adapter.query_table(
            table="TODO_opportunity_table",
            filters=filters or {},
            ctx=ctx,
        )

    def search_activities(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        self._ensure_configured()
        # TODO: real table name — e.g. task or activity table
        # TODO: field mapping per platform/DATA_DICTIONARY.md activity object
        return self._adapter.query_table(
            table="TODO_activity_table",
            filters=filters or {},
            ctx=ctx,
        )

    def search_accounts(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        self._ensure_configured()
        # TODO: real table name — e.g. customer_account
        # TODO: field mapping per platform/DATA_DICTIONARY.md account object
        return self._adapter.query_table(
            table="TODO_account_table",
            filters=filters or {},
            ctx=ctx,
        )

    def get_record(
        self, ctx: CurrentUserContext, object_type: str, sys_id: str
    ) -> Record:
        self._ensure_configured()
        # TODO: map object_type to ServiceNow table
        table_map = {
            "opportunity": "TODO_opportunity_table",
            "activity": "TODO_activity_table",
            "account": "TODO_account_table",
        }
        table = table_map.get(object_type, f"TODO_{object_type}_table")
        return self._adapter.get_record(table=table, sys_id=sys_id, ctx=ctx)

    def update_activity(
        self, ctx: CurrentUserContext, sys_id: str, patch: dict[str, Any]
    ) -> WriteResult:
        self._ensure_configured()
        # TODO: real table name and field mapping for activity updates
        return self._adapter.update_record(
            table="TODO_activity_table",
            sys_id=sys_id,
            patch=patch,
            ctx=ctx,
        )
