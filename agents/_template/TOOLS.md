# Tools

Tool definitions for this agent. Future SDK will enforce allowlist against runtime CONFIG.

## Allowed Tools (v1 Template)

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `query_crm` | Read ServiceNow per data-spec | Any CRM-backed question |
| `retrieve_knowledge` | RAG search | Procedural / product questions |
| `draft_record` | Propose CRM update | draft_only objects only |
| `escalate` | Route to human | Per ESCALATION.md |

## Tool Rules

1. Query CRM before asserting facts about records
2. Never call write tools with `commit: true` in v1
3. Log all tool calls in audit record

## TBD

- ServiceNow API tool signatures
- Rate limits and pagination
