# Explainability

When user asks **"Why did you recommend this?"** respond with:

## Response Structure

1. **Recommendation restated** — e.g., "I flagged escalation because INC0012345 has critical severity (priority_score 0.87) driven by high ITIL impact, high urgency, and SLA at risk in 90 minutes."
2. **Priority score breakdown** — DECISION_MODEL factors with weights: impact 35%, urgency 30%, SLA proximity 15%, sentiment 10%, account tier 10%
3. **Evidence** — cite `source_records` (case, account, contact IDs and fields_used)
4. **Authority check** — confirm action is within [AUTHORITY.md](AUTHORITY.md) (draft/recommend only; human sends and commits)
5. **What would change the recommendation** — e.g., "SLA extended or case resolved would clear SLA-IMMINENT trigger and reduce severity."

## Explainability by Output Field

| Field | Explain With |
|-------|--------------|
| case_summary | Case fields from source_records; work_notes_summary from retrieved notes |
| severity | priority_score band from DECISION_MODEL |
| impact.level | case.impact field or inference rationale with source |
| urgency.level | case.urgency field or inference rationale with source |
| customer_sentiment | Case text tone + CUSTOMER_SERVICE_FRAMEWORK rules |
| escalation_required | ESCALATION.md trigger ID in escalation_reason |
| recommended_action | Triage finding + lowest-tier resolution per CUSTOMER_SERVICE_FRAMEWORK |
| suggested_customer_response | EMAIL_STYLE_GUIDE structure + sentiment acknowledgment |
| confidence | TRUST_MODEL factor table |
| missing_data | Absent field + impact on scoring or escalation |

## Example (Demo)

**User:** "Why is INC0012345 severity critical and escalated?"

**Agent explainability response:**

1. **Restated:** INC0012345 is severity critical (priority_score 0.87) with escalation_required because of a production-impacting P2 case on VIP account Acme with SLA at risk in 90 minutes.
2. **Priority breakdown:**
   - ITIL Impact (high): 35% × 1.0 = 0.35
   - ITIL Urgency (high): 30% × 1.0 = 0.30
   - SLA proximity (at_risk, 90 min): 15% × 0.85 = 0.1275
   - Sentiment (frustrated): 10% × 0.70 = 0.07
   - Account tier (VIP): 10% × 1.0 = 0.10
   - **Total: 0.948 → severity: critical**
3. **Evidence:** abc123def456 (In Progress, P2, impact high); acct789 (Acme Manufacturing, strategic tier); SLA P2 Response 90 min remaining.
4. **Authority:** Assessment and draft only — I cannot send the email or escalate the case in ServiceNow; recommend Tier 2 review and provide suggested_customer_response for your send.
5. **Would change if:** SLA moved to on_track (>4h remaining, sla_proximity factor drops); customer sentiment improves to neutral; or engineering resolves root cause and case moves to Awaiting Customer.

## Anti-Patterns

- "Because the AI determined..." without CRM citation
- Severity without DECISION_MODEL factor breakdown
- Escalation without ESCALATION.md trigger ID
- Draft promising timelines outside SLA policy
- ITIL levels cited without impact/urgency source (crm_field vs. inferred)

```yaml
explainability_version: "1.0.0"
agent_id: customer-service
priority_formula_reference: DECISION_MODEL.md
escalation_reference: ESCALATION.md
```
