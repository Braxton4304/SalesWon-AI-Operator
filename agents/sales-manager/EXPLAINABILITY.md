# Explainability

When user asks **"Why did you recommend this?"** respond with:

## Response Structure

1. **Recommendation restated** — e.g., "I ranked Acme Expansion as top intervention because it is a commit deal with high priority_score (0.78) driven by activity recency and service risk."
2. **Priority score breakdown** — DECISION_MODEL factors with weights: forecast category 25%, health 20%, revenue 18%, close-date 15%, activity 10%, hygiene 7%, service risk 5%
3. **Evidence** — cite `source_records` (team view, opp, activity, case IDs and fields)
4. **Authority check** — confirm action is within [AUTHORITY.md](AUTHORITY.md) (read/analyze/recommend only; human commits forecast)
5. **What would change the recommendation** — e.g., "Activity logged within 7 days would reduce activity_recency signal and lower priority_score."

## Explainability by Output Field

| Field | Explain With |
|-------|--------------|
| pipeline_summary.headline | Top coverage or risk finding from metrics |
| pipeline_summary.coverage_ratio | weighted_pipeline / quota — cite team view source_record |
| forecast_risks.health | PIPELINE_HEALTH_MODEL signal combination |
| forecast_risks.priority_score | DECISION_MODEL weighted formula (show factor contributions) |
| forecast_risks.signals | Specific checklist or health model trigger per signal |
| top_intervention_opportunities | priority_score ranking + urgency rationale |
| rep_coaching_items | Rep opp pattern + PIPELINE_INSPECTION_GUIDE finding |
| data_hygiene_issues | Missing field + checklist_item reference |
| manager_actions | Linked forecast_risks or hygiene issues driving action |
| confidence | TRUST_MODEL factor table |

## Example (Demo)

**User:** "Why is Acme Expansion my top intervention?"

**Agent explainability response:**

1. **Restated:** Acme Expansion FY26 is ranked #2 intervention (priority_score 0.78) because it is a $250K commit deal closing in 15 days with deteriorating activity and service posture.
2. **Priority breakdown:**
   - Forecast category (commit): 25% × 1.0 = 0.25
   - Health (at_risk): 20% × 0.65 = 0.13
   - Revenue ($250K / $400K max): 18% × 0.625 = 0.1125
   - Close-date (15 days): 15% × 0.833 = 0.125
   - Activity (19 days stale): 10% × 0.905 = 0.0905
   - Hygiene (1 missing field): 7% × 0.20 = 0.014
   - Service risk (P2 open): 5% × 1.0 = 0.05
   - **Total: 0.78**
3. **Evidence:** opp789 (Proposal, commit, close 2026-07-15); act550 last activity 19 days ago; cs2001 P2 case In Progress.
4. **Authority:** Assessment and manager_actions only — I cannot commit or downgrade forecast category; recommend 1:1 and CS escalation.
5. **Would change if:** Activity within 14 days on commit deal (activity_recency signal cleared); P2 case resolved (service_risk signal cleared) — estimated priority_score would drop below 0.55.

## Anti-Patterns

- "Because the AI determined..." without CRM citation
- Priority score without DECISION_MODEL factor breakdown
- Coaching criticism without linked opportunity evidence
- Coverage ratio cited when quota was not in source_records

```yaml
explainability_version: "1.0.0"
agent_id: sales-manager
priority_formula_reference: DECISION_MODEL.md
```
