# User Scope Enforcement

Implements: [data-spec](../../specifications/data-spec.md), [runtime/SECURITY.md](../../runtime/SECURITY.md)

## CurrentUserContext

Every `/chat` request requires the `X-User-Id` header. In production this will come from Entra ID / SSO. For the POC, the React UI exposes a dev-time user ID field stored in `localStorage`.

```python
CurrentUserContext(
    user_id="alice",
    tenant_id="dev-tenant",  # from TENANT_ID env var
    roles=["sales_rep"],
)
```

The frontend **never** passes `tenant_id` — tenant is resolved server-side per governance-spec.

## ScopeEnforcer

Location: `apps/poc-runtime/backend/app/security/user_context.py`

### Read Path

Every connector read receives filters augmented with:

```python
{
    "tenant_id": ctx.tenant_id,
    "owner": ctx.user_id,
    **user_filters,
}
```

When a record is returned, `assert_record_visible` validates:

- `record.tenant_id == ctx.tenant_id`
- `record.owner == ctx.user_id` OR `ctx.user_id in record.team_visibility`

Failure → `refuse` + `scope_denied`

### Write Path

Before any update:

1. Fetch target record via connector
2. `assert_update_allowed` — owner must match user
3. Build draft → `recommend` → user confirms → execute write

## Refuse vs Retrieve

| Condition | Action |
|-----------|--------|
| User cannot see record | `refuse` + `scope_denied` |
| Connector not configured | `retrieve` + `connector_pending_credentials` |
| Unsupported intent | `refuse` + `unsupported_action` |

This separation keeps demo behavior clean: scope violations are policy blocks; missing credentials are infrastructure pending state.
