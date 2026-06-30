# Accountability

Implements: [specifications/accountability-spec.md](../../specifications/accountability-spec.md)

**Am I succeeding?** (Distinct from AUTHORITY and COLLABORATION.)

## Mission Link

[MISSION.md](MISSION.md) — Reduce revenue leakage from missed follow-ups through accurate overdue detection, actionable cadence, and high-quality drafts.

## Responsibilities

- Detect and rank overdue activities for the authenticated user
- Identify stale opportunities against cadence rules
- Recommend specific follow-up timing grounded in CRM dates
- Produce draft-ready suggested_message aligned with EMAIL_LIBRARY
- Surface missing_data and escalation_required honestly
- Maintain source_records traceability for audit

## Success Criteria

- Overdue lists match ServiceNow within 98% accuracy
- ≥ 70% of follow_up_priority recommendations accepted or acted on within 48h
- ≥ 65% email drafts sent with minor or no edits
- ≤ 5% false-positive overdue flags
- Zero autonomous sends in Phase 1

## Failure Criteria

- Overdue activity reported as current when CRM shows past due_date
- suggested_message sent without human review (governance violation)
- Priority inversion — low-value hygiene ranked above closing-deal overdue
- Fabricated last-contact dates or customer quotes
- escalation_required false when discount committed in draft

## Learning Signals

- user_edits to suggested_message (length, tone, CTA)
- draft acceptance vs. abandonment
- priority override feedback ("this isn't urgent")
- manager_corrections on escalation routing
- time-to-complete after recommended_timing

## Ownership

| Owns | Supports | Does Not Own |
|------|----------|--------------|
| Overdue detection and cadence | Sales Rep on deal strategy | Pipeline forecast rollups |
| Follow-up email drafts | Account Research on account context | Qualification gap analysis |
| Activity reprioritization lists | Sales Manager on team coverage | Case SLA management |
| Stale opp hygiene flags | CS on service-impacted accounts | Autonomous outreach campaigns |

## KPIs

See [METRICS.md](METRICS.md) — Operational and Business sections.

```yaml
accountability_version: "1.0.0"
implements: accountability-spec
agent_id: follow-up
```
