# Decision Model

## Priority Formula

Follow-ups ranked by composite score (0–100), aligned with ACTIVITY_PRIORITIZATION and ROI_SCORING_MODEL when opportunity linked:

```text
priority_score =
  overdue_severity (0–40)
  + revenue_weight (0–30)      # amount × probability normalized when opp present
  + close_date_proximity (0–20)
  + activity_type_weight (0–10) # call/meeting > email > task hygiene
```

## Overdue Severity Bands

| Days overdue | Points |
|--------------|--------|
| 1–2 | 15 |
| 3–5 | 25 |
| 6–10 | 32 |
| 11+ | 40 |

## Cadence / Timing Rules

| Input | recommended_timing |
|-------|-------------------|
| Overdue activity | Immediate (same business day) unless user capacity noted |
| Stale opp, close ≤ 14 days | Within 24 hours |
| Stale opp, mid-stage | Within 2–3 business days |
| Post-meeting, no next task | Within 48 hours of meeting activity date |
| Objection noted ("need to think") | 3–5 business days with decision-process ask |
| No due_date on activity | ask user or infer from opp stage cadence table (CAPABILITIES) |

## Scenario Matrix

| Scenario | Action |
|----------|--------|
| "My overdue list" | query_overdue_activities → ranked recommend |
| Activity ID or opp name given | query + single follow-up recommend |
| Email draft requested | draft_email → decision_action recommend |
| Missing contact for email | ask or query_contact |
| Pricing objection in notes | suggest objection-aware message; escalation_required if discount needed |
| Activity already Complete | answer — not overdue; suggest next cadence if opp open |
| No CRM activities found | ask if record exists or retrieve by alternate ID |
| Confidence < 0.60 on dates | escalate or ask per confidence-scoring |

## Business Reasoning Weights

Sales Velocity 1.0, Activity Effectiveness 1.0, Revenue 0.85, Customer Retention 0.6

## follow_up_priority Mapping

| priority_score | follow_up_priority |
|----------------|-------------------|
| ≥ 80 | critical |
| 60–79 | high |
| 40–59 | moderate |
| < 40 | low |
