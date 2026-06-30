# Long Memory

Implements: [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md) — long tier

## Scope

- User communication preferences (detail level, format)
- Historical decisions approved by user ("always CC manager on escalations")
- Learned patterns (aggregated, no raw PII)
- Organization policies referenced repeatedly

## Not Stored Here

- CRM record values (source of truth is ServiceNow)
- Full conversation transcripts (short tier + audit logs)

## Retrieval

Long memory is retrieved selectively — not injected in full into RUNTIME_CONTEXT.

## Agent-Specific Notes

*(What long-term preferences matter for this role)*

## Planned Storage

Azure SQL per MEMORY_MODEL.md — schema TBD.
