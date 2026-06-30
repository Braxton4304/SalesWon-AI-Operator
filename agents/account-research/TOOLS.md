# Tools

Tool definitions for this agent. Future SDK will enforce allowlist against runtime CONFIG.

## Allowed Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `query_account` | Retrieve account profile, tier, industry, hierarchy | Any account-backed request |
| `query_contacts` | List contacts for account with roles and recency | Relationship map, meeting prep |
| `query_opportunities` | Open opps for account (stage, amount, close date) | opportunity_context, buying signals |
| `query_cases` | Open/recent cases for account | service_context, CUSTOMER_RISK_GUIDE |
| `query_activities` | Activities for account or contact (last N) | Engagement history, meeting prep |
| `query_crm` | Generic read per data-spec | Cross-object lookups |
| `retrieve_knowledge` | RAG search on playbooks, product docs | Methodology, white-space product lists |
| `draft_activity` | Propose research or meeting prep task | recommend only |
| `escalate` | Route to human | Per ESCALATION.md |

## Tool Sequences

### Standard Account Brief

```text
query_account → query_contacts → query_opportunities → query_cases → query_activities
```

### Meeting Prep (named attendees)

```text
query_account → query_contacts (filter attendees) → query_activities (last 5) → query_opportunities
```

## Required Field Checks

| Object | Required Before Asserting |
|--------|---------------------------|
| Account | name (minimum); tier/industry preferred |
| Contact | name; title/role preferred for relationship_map |
| Opportunity | amount, probability, close_date for pipeline assertions |

## Tool Rules

1. Query account before asserting account facts
2. Never call write tools with `commit: true` in Phase 1
3. Log all tool calls in audit record
4. Max 3 retrieve cycles per DECISION_ENGINE before escalate
5. Relationship role labels require contact + activity evidence or must be marked assumed

## TBD

- ServiceNow API tool signatures and pagination
- Contact hierarchy / org chart API if available in tenant
