# Long Memory

Implements: [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md) — long tier

## Scope

- User preferred brief format (executive bullets vs. detailed narrative)
- Default sections to include (e.g., always include service_context)
- Frequently researched accounts (pinned by user — IDs only, not CRM values)
- Preferred relationship map depth (minimal vs. full org coverage)
- Manager vs. rep audience preference for tone and length

## Not Stored Here

- CRM record values (source of truth is ServiceNow)
- Full account brief text (regenerate from CRM each session)
- Full conversation transcripts (short tier + audit logs)

## Org Memory (Layer 4)

- Account tier definitions and strategic account list
- Product catalog for white-space analysis
- Industry-specific discovery question templates
- Strategic account escalation contacts

## Retrieval

Long memory is retrieved selectively — not injected in full into RUNTIME_CONTEXT.

## Agent-Specific Notes

If user consistently edits research questions to be shorter, adapt recommended_research_questions count (default 5, reduce to 3).
