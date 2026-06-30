# Explainability

When user asks **"Why did you recommend this?"** respond with:

## Response Structure

1. **Recommendation restated** — e.g., "I recommend scheduling an executive alignment call with the economic buyer because Acme Expansion is at_risk with a blocking MEDDIC gap and closes in 12 days."
2. **Priority score breakdown** — DECISION_MODEL factors with weights: close-date 30%, revenue 20%, qualification 15%, activity 15%, health 10%, user focus 10%
3. **Evidence** — cite `source_records` (opp, activity, contact IDs and fields)
4. **Authority check** — confirm action is within [AUTHORITY.md](AUTHORITY.md) (analyze/recommend/draft only; rep sends and commits)
5. **What would change the recommendation** — e.g., "Economic buyer contact added to CRM would clear blocking gap and reduce qualification factor; activity within 7 days would lower activity_recency score."

## Explainability by Output Field

| Field | Explain With |
|-------|--------------|
| opportunity_summary.headline | Top deal finding from CRM fields |
| deal_health | PIPELINE_HEALTH_MODEL signal combination |
| qualification_gaps | MEDDIC/SPIN/Sandler element + missing CRM evidence |
| next_best_action.priority_score | DECISION_MODEL weighted formula (show factor contributions) |
| next_best_action.action | Linked gap or health signal driving action |
| recommended_questions | Gap addressed + methodology purpose |
| suggested_follow_up | Action type and target record rationale |
| pipeline_rankings | priority_score comparison across opps |
| confidence | TRUST_MODEL factor table |
| escalation_required | ESCALATION.md trigger matched |
| missing_data | Field absent and impact on scoring |

## Example (Demo)

**User:** "Why schedule an executive call on Acme Expansion?"

**Agent explainability response:**

1. **Restated:** Schedule executive alignment with economic buyer — priority_score 84/100 — because this $120K Proposal-stage opp closes in 12 days with no economic buyer in CRM and 18 days since last activity.
2. **Priority breakdown:**
   - Close-date urgency (12 days): 30% × 0.867 = 0.260
   - Revenue ($54K weighted / rep max): 20% × 0.675 = 0.135
   - Qualification gap (blocking economic_buyer): 15% × 1.0 = 0.150
   - Activity recency (18 days): 15% × 0.857 = 0.129
   - Deal health (at_risk): 10% × 0.65 = 0.065
   - User explicit focus (named opp): 10% × 1.0 = 0.100
   - **Total: 0.839 → 84/100**
3. **Evidence:** opp789 (Proposal, $120K, 45%, close 2026-07-12); act550 last activity 2026-06-12; no contact with role economic_buyer.
4. **Authority:** Recommend meeting and draft email only — I cannot send email or update CRM; you commit in ServiceNow.
5. **Would change if:** Economic buyer added to CRM (qualification factor → 0); activity logged within 14 days (activity factor drops ~40%) — estimated priority_score below 60.

## Methodology Explainability

When user asks "Why this MEDDIC gap?":

- Cite stage-appropriate MEDDIC requirement from [DECISION_MODEL.md](DECISION_MODEL.md)
- Show CRM field checked and value found/absent in source_records
- Link recommended_questions to specific gap element

## Anti-Patterns

- "Because the AI determined..." without CRM citation
- priority_score without DECISION_MODEL factor breakdown
- qualification_gaps without methodology and severity
- suggested_follow_up presented as already sent
- deal_health label without PIPELINE_HEALTH_MODEL basis

```yaml
explainability_version: "1.1.0"
agent_id: sales-rep
priority_formula_reference: DECISION_MODEL.md
methodologies: [meddic, spin, sandler]
```
