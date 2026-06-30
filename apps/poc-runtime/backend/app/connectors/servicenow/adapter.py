# implements: platform/servicenow.md

"""ServiceNow REST adapter shell — no live HTTP until credentials are supplied."""

from __future__ import annotations

from typing import Any

import httpx

from app.connectors.saleswon.base import ConnectorNotConfigured, Record, WriteResult
from app.connectors.servicenow.config import ServiceNowConfig
from app.security.user_context import CurrentUserContext


class ServiceNowAdapter:
    def __init__(self, config: ServiceNowConfig | None = None) -> None:
        self._config = config or ServiceNowConfig.from_settings()
        self._client = httpx.Client(timeout=30.0)

    def _ensure_configured(self) -> None:
        if not self._config.is_configured:
            raise ConnectorNotConfigured(
                "ServiceNow adapter not configured. Set SERVICENOW_* env vars."
            )

    def _request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        self._ensure_configured()
        # TODO: OAuth 2.0 token flow — exchange client_id/secret for access token
        # TODO: attach Bearer token or Basic auth per instance policy
        url = f"{self._config.instance_url.rstrip('/')}{path}"
        headers = kwargs.pop("headers", {})
        # TODO: inject Authorization header from token exchange
        return self._client.request(method, url, headers=headers, **kwargs)

    def query_table(
        self,
        table: str,
        filters: dict[str, Any],
        ctx: CurrentUserContext,
    ) -> list[Record]:
        self._ensure_configured()
        # TODO: build sysparm_query from filters + ctx tenant/owner ACL alignment
        _ = ctx
        response = self._request("GET", f"/api/now/table/{table}", params=filters)
        response.raise_for_status()
        payload = response.json().get("result", [])
        return [
            Record(
                sys_id=item.get("sys_id", ""),
                object_type=table,
                fields=item,
                owner=item.get("assigned_to") or item.get("owner"),
                tenant_id=ctx.tenant_id,
            )
            for item in payload
        ]

    def get_record(
        self, table: str, sys_id: str, ctx: CurrentUserContext
    ) -> Record:
        self._ensure_configured()
        response = self._request("GET", f"/api/now/table/{table}/{sys_id}")
        response.raise_for_status()
        item = response.json().get("result", {})
        return Record(
            sys_id=item.get("sys_id", sys_id),
            object_type=table,
            fields=item,
            owner=item.get("assigned_to") or item.get("owner"),
            tenant_id=ctx.tenant_id,
        )

    def update_record(
        self,
        table: str,
        sys_id: str,
        patch: dict[str, Any],
        ctx: CurrentUserContext,
    ) -> WriteResult:
        self._ensure_configured()
        _ = ctx
        response = self._request(
            "PATCH", f"/api/now/table/{table}/{sys_id}", json=patch
        )
        response.raise_for_status()
        item = response.json().get("result", {})
        return WriteResult(
            sys_id=item.get("sys_id", sys_id),
            object_type=table,
            status="updated",
            fields=item,
        )
