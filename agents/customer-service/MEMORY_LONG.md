# Long Memory

## Scope (Cross-Session)

- Rep preferred draft length (brief vs. detailed)
- Standard greeting/closing preferences (within EMAIL_STYLE_GUIDE)
- Frequently used assignment groups for escalation suggestions
- Account-specific handling notes approved by manager ("Acme Corp — always CC their CSM lead")
- Preferred triage depth (full ITIL breakdown vs. summary-only)

## Not Stored

- Case field values (ServiceNow source of truth)
- Customer PII aggregates without policy approval per [policies/PII_POLICY.md](../../policies/PII_POLICY.md)
- SLA breach outcomes (re-fetch from CRM)

## Retrieval Triggers

- User returns to same account within 30 days
- Rep asks "draft like last time for this account"
- Rep consistently requests expanded ITIL rationale

## Organization Memory (Tenant-Level)

- Default SLA tier definitions (Layer 4)
- Escalation contact roster (Layer 4)
- Approved macro snippets for common case types
- ITIL impact/urgency definitions when customized per deployment

## Planned Storage

Azure SQL `memory.user_preferences`, `memory.org_decisions` per MEMORY_MODEL.md.

```yaml
memory_long_version: "1.0.0"
agent_id: customer-service
storage: azure_sql
pii_policy: policies/PII_POLICY.md
```
