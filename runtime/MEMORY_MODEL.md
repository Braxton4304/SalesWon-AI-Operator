# Memory Model

Implements: [specifications/runtime-spec.md](../specifications/runtime-spec.md)

## Tiers

### Short Memory

| Attribute | Value |
|-----------|-------|
| Scope | Current conversation, current task |
| Agent file | `MEMORY_SHORT.md` |
| Storage (planned) | Session / ephemeral cache |
| TTL | 120 minutes (CONFIG.yaml) |
| Max turns | 20 |

Used in RUNTIME_CONTEXT layer 7 (conversation history).

### Long Memory

| Attribute | Value |
|-----------|-------|
| Scope | User preferences, historical decisions, learned behavior, organization memory |
| Agent file | `MEMORY_LONG.md` |
| Storage (planned) | Azure SQL |
| Retention | 365 days default (CONFIG.yaml) |

Not injected in full — retrieved selectively when relevant.

## Azure SQL Mapping (Planned)

| Table (planned) | Tier | Content |
|-----------------|------|---------|
| `memory.short_sessions` | Short | Session transcripts (encrypted) |
| `memory.user_preferences` | Long | Detail level, communication style |
| `memory.org_decisions` | Long | Approved playbook deviations |
| `memory.learned_patterns` | Long | Aggregated behavior (no PII) |

Schema details: [architecture/domains/database-design](../architecture/domains/database-design/README.md).

## Rules

1. Short memory NEVER persists CRM field values as truth — re-fetch from ServiceNow.
2. Long memory updates require audit entry when used in decisions.
3. GDPR deletion requests purge long memory by `user_id` + `tenant_id`.

## Machine-Readable Contract

```yaml
implements: runtime-spec
tiers:
  short:
    agent_file: MEMORY_SHORT.md
    storage: session
    max_turns: 20
    ttl_minutes: 120
  long:
    agent_file: MEMORY_LONG.md
    storage: azure_sql
    retention_days: 365
```
