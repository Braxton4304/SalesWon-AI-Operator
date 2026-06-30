# Short Memory

Implements: [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md) — short tier

## Scope

- Active account sys_id and name
- Meeting prep context (date, attendee contact IDs) if in progress
- Partial brief sections already delivered (avoid redundant re-query)
- User-requested focus (e.g., "service health only" vs. full brief)
- Disambiguation resolution (selected account from candidate list)

## Retention

- Max 20 turns (runtime CONFIG)
- TTL 120 minutes
- Cleared on session end

## Task States

`account_brief`, `relationship_map`, `meeting_prep`, `buying_signals`, `service_health`, `research_questions`

## Rules

- Re-fetch account/opportunity/case data when user may have updated CRM mid-session
- Do not treat short memory as CRM source of truth
- Do not store secrets or PII beyond session necessity

## Agent-Specific Notes

When user pivots from full brief to meeting prep on same account, reuse cached contact and activity queries if TTL < 5 minutes and user has not indicated CRM updates.
