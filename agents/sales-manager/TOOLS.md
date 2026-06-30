# Tools

Tool definitions for this agent. Future SDK will enforce allowlist against runtime CONFIG.

## Allowed Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| `query_team_pipeline` | Manager-scoped rollup: weighted pipeline, stage distribution, forecast categories | Any team pipeline or coverage request |
| `query_opportunities` | Team opps with stage, amount, probability, close_date, owner, forecast category | Deal health, forecast_risks, intervention ranking |
| `query_activities` | Activities by opp, rep, or date range | Activity recency, rep cadence analysis |
| `query_accounts` | Account tier and linked opps in team scope | Strategic value, account-level rollup |
| `query_cases` | Open cases for accounts with forecast opps | CUSTOMER_RISK_GUIDE correlation |
| `query_crm` | Generic read per data-spec | Cross-object lookups, rep filter |
| `retrieve_knowledge` | RAG on playbooks, PIPELINE_INSPECTION_GUIDE, forecasting definitions | Methodology and coaching language |
| `escalate` | Route to human | Per ESCALATION.md |

## Tool Sequences

### Standard Team Pipeline Review

```text
query_team_pipeline → query_opportunities (team filter) → query_activities (recency) → apply PIPELINE_HEALTH_MODEL
```

### Rep Coaching Session Prep

```text
query_opportunities (owner filter) → query_activities (rep + opp) → PIPELINE_INSPECTION_GUIDE checklist → rep_coaching_items
```

### Executive Forecast Brief

```text
query_team_pipeline → query_opportunities (commit + best_case) → query_cases (forecast accounts) → EXECUTIVE_SUMMARY_STANDARD assembly
```

### Forecast Risk Deep Dive

```text
query_opportunities (close_date window + forecast category) → query_activities → query_cases (linked accounts) → DECISION_MODEL scoring
```

## Required Field Checks

Per [data-spec](../../specifications/data-spec.md) and PIPELINE_INSPECTION_GUIDE:

| Object | Required Before Asserting |
|--------|---------------------------|
| Opportunity | amount, probability, close_date, owner for health scores and rollups |
| Team pipeline view | period, team_id or manager scope for aggregate metrics |
| Activity | completed_date or due_date for recency calculations |
| Account | name minimum; tier for strategic weighting when available |

Missing fields → `data_hygiene_issues` + confidence reduction; never invent values.

## Tool Rules

1. Query team_pipeline or opportunities before asserting pipeline totals
2. Never call write tools — Phase 1 read-only
3. Log all tool calls in audit record
4. Max 3 retrieve cycles per DECISION_ENGINE before escalate
5. Rep coaching must link to opp or activity source_records
6. Coverage ratio requires quota from CRM or Layer 4 — if absent, report weighted pipeline only

```yaml
tools_version: "1.0.0"
agent_id: sales-manager
allowed_tools:
  - query_team_pipeline
  - query_opportunities
  - query_activities
  - query_accounts
  - query_cases
  - query_crm
  - retrieve_knowledge
  - escalate
write_tools: []
```
