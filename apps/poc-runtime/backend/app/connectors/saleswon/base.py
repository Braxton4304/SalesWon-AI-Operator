# implements: data-spec, platform/servicenow.md

"""SalesWon connector contract and exceptions."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from app.security.user_context import CurrentUserContext


class ConnectorNotConfigured(Exception):
    """Raised when connector credentials are not yet provisioned."""


class RecordNotFound(Exception):
    """Raised when a scoped record cannot be found."""


@dataclass
class Record:
    sys_id: str
    object_type: str
    fields: dict[str, Any] = field(default_factory=dict)
    owner: str | None = None
    tenant_id: str | None = None
    team_visibility: list[str] = field(default_factory=list)


@dataclass
class WriteResult:
    sys_id: str
    object_type: str
    status: str
    fields: dict[str, Any] = field(default_factory=dict)


class SalesWonConnector(ABC):
    """
    implements: data-spec baseline_objects
    methods: search_opportunities, search_activities, search_accounts, get_record, update_activity
    """

    @abstractmethod
    def search_opportunities(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        ...

    @abstractmethod
    def search_activities(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        ...

    @abstractmethod
    def search_accounts(
        self, ctx: CurrentUserContext, filters: dict[str, Any] | None = None
    ) -> list[Record]:
        ...

    @abstractmethod
    def get_record(
        self, ctx: CurrentUserContext, object_type: str, sys_id: str
    ) -> Record:
        ...

    @abstractmethod
    def update_activity(
        self, ctx: CurrentUserContext, sys_id: str, patch: dict[str, Any]
    ) -> WriteResult:
        ...
