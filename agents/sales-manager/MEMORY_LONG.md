# Long Memory

Implements: [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md) — long tier

## Scope

- Manager communication preferences: brief vs. detailed, table vs. narrative, metric emphasis
- Preferred rollup period default (monthly, quarterly, fiscal year)
- Historical coaching style approvals ("Jordan responds well to data-first 1:1 structure")
- Repeated manager_actions the user accepted without edit
- Organization forecast definitions referenced repeatedly (Layer 4 commit rules when configured)
- Executive brief audience defaults (always include coverage ratio, always exclude prospecting pipeline)

## Not Stored Here

- CRM record values (source of truth is ServiceNow)
- Pipeline totals or forecast figures (always re-query)
- Full conversation transcripts (short tier + audit logs)
- Quota or compensation numbers unless user explicitly saves as preference label only

## Retrieval

Long memory is retrieved selectively — not injected in full into RUNTIME_CONTEXT. Typical triggers:

- User returns for recurring weekly pipeline review
- User asks "same format as last time"
- User has standing rep coaching preferences

## Agent-Specific Preferences

| Preference | Example | Effect |
|------------|---------|--------|
| `default_period` | Q3 FY26 | Pre-fill period in pipeline_summary |
| `coaching_depth` | concise \| detailed | rep_coaching_items item count |
| `risk_threshold` | surface critical + high only | forecast_risks filter |
| `exec_brief_sections` | metrics, risks, actions | EXECUTIVE_SUMMARY_STANDARD subset |
| `hygiene_on_commit_only` | true | data_hygiene_issues filter |
| `include_service_risk` | true | query_cases in default sequence |

## Planned Storage

Azure SQL per MEMORY_MODEL.md — schema TBD.

```yaml
memory_long_version: "1.0.0"
agent_id: sales-manager
storage: azure_sql_planned
pii_policy: preferences_only_no_crm_values
```
