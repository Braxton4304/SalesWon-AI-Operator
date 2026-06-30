# Database (Azure SQL)

Implements: [specifications/data-spec.md](../specifications/data-spec.md), [runtime/MEMORY_MODEL.md](../runtime/MEMORY_MODEL.md)

## Purpose

Azure SQL stores platform data — **not** CRM source of truth (ServiceNow remains authoritative for Layer 5).

## Planned Schemas

| Schema | Tables | Purpose |
|--------|--------|---------|
| `audit` | `events` | Governance audit log |
| `memory` | `short_sessions`, `user_preferences`, `org_decisions` | Memory tiers |
| `feedback` | `user_edits`, `acceptances` | METRICS.md loop |
| `metrics` | `agent_daily_rollups` | Observability |

## Tenant Isolation

Every table includes `tenant_id`. Design for Row Level Security from day one.

## TBD

- Migration tooling
- Retention and GDPR deletion procedures
- Connection via Managed Identity

## Related

- [architecture/domains/database-design](../architecture/domains/database-design/README.md)
