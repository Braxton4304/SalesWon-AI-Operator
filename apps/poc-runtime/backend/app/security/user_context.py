# implements: governance-spec, runtime/SECURITY.md

"""User context and scope enforcement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from fastapi import Header, HTTPException

from app.config.settings import get_settings


@dataclass
class CurrentUserContext:
    user_id: str
    tenant_id: str
    roles: list[str] = field(default_factory=lambda: ["sales_rep"])


def get_current_user_context(
    x_user_id: str | None = Header(default=None, alias="X-User-Id"),
) -> CurrentUserContext:
    if not x_user_id:
        raise HTTPException(status_code=400, detail="X-User-Id header is required")
    settings = get_settings()
    return CurrentUserContext(user_id=x_user_id, tenant_id=settings.tenant_id)


class ScopeDenied(Exception):
    def __init__(self, reason: str = "scope_denied") -> None:
        self.reason = reason
        super().__init__(reason)


class ScopeEnforcer:
    """Forces tenant and owner filters on reads; validates ownership on writes."""

    def apply_read_filters(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        scoped = dict(filters or {})
        scoped["tenant_id"] = ctx.tenant_id
        scoped["owner"] = ctx.user_id
        return scoped

    def assert_record_visible(
        self, ctx: CurrentUserContext, record: dict[str, Any]
    ) -> None:
        record_tenant = record.get("tenant_id")
        if record_tenant and record_tenant != ctx.tenant_id:
            raise ScopeDenied("scope_denied")

        owner = record.get("owner")
        team = record.get("team_visibility") or []
        if owner and owner != ctx.user_id and ctx.user_id not in team:
            raise ScopeDenied("scope_denied")

    def assert_update_allowed(
        self, ctx: CurrentUserContext, record: dict[str, Any]
    ) -> None:
        self.assert_record_visible(ctx, record)
        owner = record.get("owner")
        if owner and owner != ctx.user_id:
            raise ScopeDenied("scope_denied")

    def assert_authority(
        self, ctx: CurrentUserContext, required_roles: list[str] | None = None
    ) -> None:
        if not required_roles:
            return
        if not any(role in ctx.roles for role in required_roles):
            raise ScopeDenied("missing_authority")
