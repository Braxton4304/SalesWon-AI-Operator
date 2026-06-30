# Explainability

When user asks **"Why did you recommend this?"** or **"Why is this critical?"** respond with:

## Template

1. **Recommendation restated** — follow_up_priority + recommended_timing + action type
2. **Priority score breakdown** — overdue_severity, revenue_weight, close_date_proximity per DECISION_MODEL
3. **Evidence** — source_records with specific dates: "Task act456 due 2026-06-25 (5 days overdue); opp closes 2026-07-11"
4. **Authority check** — "Draft only; you approve send per AUTHORITY.md" or escalation path if pricing involved
5. **What would change it** — "If activity marked Complete, priority drops"; "If close_date slips 30+ days, timing relaxes to 5 days"

## Example Response (Natural Language)

> **Critical follow-up today** because your call task on Acme Expansion is 5 days past due (due 2026-06-25) and the opportunity closes in 11 days ($120K, Proposal stage). Priority score: 88/100 — overdue severity 32/40, revenue weight 26/30, close proximity 18/20. Sources: activity act456, opportunity opp789, contact Sarah Chen. This is a draft recommendation only; you send after review. **Would change if:** the task were completed in ServiceNow, or close date moved beyond 30 days.

## Field Mapping for Structured Explainability

| User question | Highlight fields |
|---------------|------------------|
| Why this priority? | follow_up_priority, reason, DECISION_MODEL breakdown |
| Why now? | recommended_timing, cadence rules |
| Why this message? | suggested_message, EMAIL_LIBRARY template used |
| Why escalate? | escalation_required, ESCALATION.md trigger |
| What data missing? | missing_data, confidence |

## Anti-Patterns

- Do not cite priority_score without showing inputs
- Do not claim customer sentiment without activity note evidence
- Do not hide escalation_required when pricing discussed
