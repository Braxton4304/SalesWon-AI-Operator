# Short Memory

## Scope (This Session)

- Active case number(s) and sys_ids under discussion
- Current draft in progress (`suggested_customer_response`, work note) for edit iterations
- User role context (rep vs. lead) if stated
- Account/contact resolved for current thread
- Last computed ITIL impact/urgency/severity for active case

## Retention

Per [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md): max 20 turns, 120-minute TTL.

## Session Rules

- Re-query case on new turn if user may have updated ServiceNow externally
- Clear draft context when user switches to different case number
- Store case summary hash to detect stale context ("Case was updated since last summary — refreshing.")
- Do not cache SLA timers beyond one turn — recompute from fresh query

## Typical Task States

| State | Description |
|-------|-------------|
| `triaging` | Gathering case + account context; computing ITIL scores |
| `drafting_reply` | Iterating on customer email |
| `sla_review` | Computing breach risk and sla_proximity factor |
| `escalation_prep` | Building handoff payload with escalation_reason |

## Do Not Store

- Full work note history (re-fetch)
- Customer PII beyond session necessity per PII_POLICY
- Committed case field values (ServiceNow is source of truth)

```yaml
memory_short_version: "1.0.0"
agent_id: customer-service
ttl_minutes: 120
max_turns: 20
```
