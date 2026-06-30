# Capabilities

What this agent **is allowed** to do. Must align with [data-spec](../../specifications/data-spec.md) permissions.

## Allowed Actions

### Pipeline Visibility

- Read manager-scoped team pipeline views, opportunities, accounts, and activities
- Produce `pipeline_summary` with weighted pipeline, coverage ratio, stage distribution, and forecast category breakdown
- Score deal health per [PIPELINE_HEALTH_MODEL.md](../../shared/PIPELINE_HEALTH_MODEL.md) signals
- Run PIPELINE_INSPECTION_GUIDE checklist on team opps and aggregate findings

### Forecast Risk Assessment

- Identify `forecast_risks` — commit/best-case deals with health signals at_risk or critical
- Correlate close-date slip, activity recency, probability/stage mismatch, and single-threading
- Include CUSTOMER_RISK_GUIDE service posture when account cases affect forecast deals
- Rank `top_intervention_opportunities` by DECISION_MODEL weighted score

### Rep Coaching

- Generate `rep_coaching_items` — rep-specific, constructive coaching per PIPELINE_INSPECTION_GUIDE
- Highlight rep-level patterns: stale commit deals, hygiene gaps, activity cadence variance
- Recommend coaching topics tied to evidence — not personality judgments

### Executive Reporting

- Produce manager and exec briefings per [EXECUTIVE_SUMMARY_STANDARD.md](../../shared/EXECUTIVE_SUMMARY_STANDARD.md)
- Structure headline, metrics, highlights, risks, actions, and source appendix
- Note confidence band when required opp fields are missing

### Data Hygiene

- Flag `data_hygiene_issues` — missing amount, probability, close_date, owner, forecast category
- Prioritize hygiene fixes on commit-category and near-term close deals

### Recommendations

- Propose `manager_actions` — 1:1 topics, pipeline reviews, forecast call agenda items (recommend only)
- Recommend rep follow-up priorities consumable by Sales Rep and Follow-Up agents (human-mediated)

## Tools

See [TOOLS.md](TOOLS.md). Tool list must match runtime allowlist when SDK is implemented.

## Shared Knowledge

| Shared Asset | Usage |
|--------------|-------|
| PIPELINE_HEALTH_MODEL | Deal and aggregate health scoring |
| PIPELINE_INSPECTION_GUIDE | Inspection checklist → coaching output |
| EXECUTIVE_SUMMARY_STANDARD | Brief structure for exec responses |
| SALES_PLAYBOOK ch. 9–10 | Customer risk and forecasting context |
| ACTIVITY_PRIORITIZATION | Manager intervention priority stack |
| ROI_SCORING_MODEL | Weighted ranking of intervention opps |
| CUSTOMER_RISK_GUIDE | Service risk in forecast_risks |
| COMMUNICATION_STANDARD | Tone and clarity for coaching language |

```yaml
capabilities_version: "1.0.0"
agent_id: sales-manager
crm_access: [opportunity, account, activity, team_pipeline_view]
write_access: none
phase: 1_reactive
```
