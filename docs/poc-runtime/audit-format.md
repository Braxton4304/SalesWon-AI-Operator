# Audit Log Format

Implements: [governance-spec](../../specifications/governance-spec.md), [runtime/GOVERNANCE.md](../../runtime/GOVERNANCE.md)

## Storage

Default path: `apps/poc-runtime/backend/audit/events.jsonl`

One JSON object per line. Configurable via `AUDIT_LOG_PATH`.

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `tenant_id` | string | Resolved tenant |
| `correlation_id` | uuid | Unique audit ID (returned as `audit_id` in API) |
| `actor` | string | User ID from `X-User-Id` |
| `timestamp` | ISO8601 UTC | Event time |
| `decision_action` | string | One of 6 runtime actions |
| `confidence_score` | float | 0.0–1.0 |
| `source_references` | array | CRM sys_ids (empty when connector pending) |
| `outcome` | string | `success`, `pending`, `escalated`, `refused`, `error` |
| `status` | string | Disambiguates action reason |

## POC Extensions

| Field | Purpose |
|-------|---------|
| `intent` | Classified intent |
| `filters` | Scoped read filters applied |
| `target_object` | CRM object type |
| `proposed_action` | Draft write payload |
| `confirmation` | Whether user confirmed a write |

## Example — Connector Pending

```json
{
  "tenant_id": "dev-tenant",
  "correlation_id": "550e8400-e29b-41d4-a716-446655440000",
  "actor": "alice",
  "timestamp": "2026-06-30T22:00:00+00:00",
  "decision_action": "retrieve",
  "confidence_score": 0.88,
  "source_references": [],
  "outcome": "pending",
  "status": "connector_pending_credentials",
  "intent": "search_opportunities",
  "request_summary": "read: search_opportunities"
}
```

## Example — Scope Denied

```json
{
  "decision_action": "refuse",
  "status": "scope_denied",
  "outcome": "refused",
  "source_references": []
}
```
