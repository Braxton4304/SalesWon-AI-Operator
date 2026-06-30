# implements: runtime-spec, data-spec

"""Intent classification schemas."""

from __future__ import annotations

from enum import Enum


class Intent(str, Enum):
    SEARCH_OPPORTUNITIES = "search_opportunities"
    SEARCH_ACTIVITIES = "search_activities"
    SEARCH_ACCOUNTS = "search_accounts"
    GET_RECORD = "get_record"
    UPDATE_ACTIVITY = "update_activity"
    UNKNOWN = "unknown"
