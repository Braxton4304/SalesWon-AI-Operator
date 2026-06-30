# Short Memory

Implements: [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md) — short tier

## Scope

- Current conversation turns
- Current task context (e.g. "drafting email for case INC001")
- Resolved entity references for this session (opportunity ID, case number)

## Retention

- Max 20 turns (runtime CONFIG)
- TTL 120 minutes
- Cleared on session end

## Rules

- Do not treat short memory as CRM source of truth — re-fetch on new turn if data may have changed
- Do not store secrets or PII beyond session necessity

## Agent-Specific Notes

*(What task context this agent tracks — e.g. "multi-step case resolution workflow state")*
