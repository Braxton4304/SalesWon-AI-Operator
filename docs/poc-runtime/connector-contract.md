# SalesWon Connector Contract

Implements: [data-spec](../../specifications/data-spec.md), [platform/servicenow.md](../../platform/servicenow.md)

## Interface

Location: `apps/poc-runtime/backend/app/connectors/saleswon/base.py`

```python
class SalesWonConnector(ABC):
    def search_opportunities(ctx, filters) -> list[Record]
    def search_activities(ctx, filters) -> list[Record]
    def search_accounts(ctx, filters) -> list[Record]
    def get_record(ctx, object_type, sys_id) -> Record
    def update_activity(ctx, sys_id, patch) -> WriteResult
```

Every method receives `CurrentUserContext` — callers must never bypass scope enforcement.

## Exception Taxonomy

| Exception | Meaning | User-facing action |
|-----------|---------|-------------------|
| `ConnectorNotConfigured` | Credentials not provisioned | `retrieve` + `connector_pending_credentials` |
| `ScopeDenied` | Record not visible to user | `refuse` + `scope_denied` |
| `RecordNotFound` | Scoped record does not exist | `escalate` or `ask` |

## ServiceNow Adapter Shell

Location: `apps/poc-runtime/backend/app/connectors/servicenow/`

Required env vars:

- `SERVICENOW_INSTANCE_URL`
- `SERVICENOW_CLIENT_ID`
- `SERVICENOW_CLIENT_SECRET`
- `SERVICENOW_USERNAME` or `SERVICENOW_PASSWORD_OR_TOKEN`

TODO markers in code indicate where real table names and field mappings will be wired per [platform/DATA_DICTIONARY.md](../../platform/DATA_DICTIONARY.md).

## Activation

When all ServiceNow env vars are set, the adapter performs live HTTP calls. Until then, `_ensure_configured()` raises `ConnectorNotConfigured` — no mock records are returned.
