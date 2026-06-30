# Short Memory

Implements: [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md) — short tier

## Scope

- Current conversation turns and manager request intent
- Resolved scope references: team_id, quarter/period, named rep, forecast category filter
- In-progress pipeline inspection state (opps scored, checklist items pending)
- Executive brief context: target meeting date, audience (VP, CRO, board)
- Last retrieved team_pipeline snapshot timestamp (re-fetch if stale > 15 min)

## Retention

- Max 20 turns (runtime CONFIG)
- TTL 120 minutes
- Cleared on session end

## Session Context Keys

| Key | Example | Use |
|-----|---------|-----|
| `team_scope` | "EMEA Enterprise" | Filter all CRM queries |
| `period` | "Q3 FY26" | pipeline_summary period label |
| `rep_filter` | "Jordan Lee" | rep_coaching_items focus |
| `forecast_filter` | "commit" | forecast_risks subset |
| `brief_audience` | "CRO forecast call" | EXECUTIVE_SUMMARY_STANDARD tone |
| `inspection_progress` | opp IDs scored | Avoid duplicate scoring in multi-turn review |

## Rules

- Do not treat short memory as CRM source of truth — re-fetch on new turn if data may have changed
- Do not store secrets, compensation data, or PII beyond session necessity
- Clear rep_filter when manager switches to full-team view explicitly
- Pipeline totals in memory are hints only — always re-query for final OUTPUT_SCHEMA

## Agent-Specific Notes

Tracks multi-step pipeline review workflows: e.g., turn 1 team rollup → turn 2 drill into Jordan's at-risk deals → turn 3 exec brief synthesis. Preserve scored opp list to maintain consistent priority_score ordering across turns.

```yaml
memory_short_version: "1.0.0"
agent_id: sales-manager
max_turns: 20
ttl_minutes: 120
```
