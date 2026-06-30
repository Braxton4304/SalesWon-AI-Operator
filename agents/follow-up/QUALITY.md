# Quality

## Correctness

- [ ] due_date and days_overdue match ServiceNow activity record
- [ ] related_opportunity amount, stage, close_date match CRM
- [ ] Overdue filter excludes Complete/Closed/Cancelled states
- [ ] Stale opp claims cite verifiable last_activity_date

## Completeness

- [ ] reason references specific CRM dates and fields
- [ ] recommended_timing is actionable (not "soon")
- [ ] suggested_message includes context from last interaction when available
- [ ] source_records lists every record used in reasoning
- [ ] missing_data populated when required fields absent

## Hallucination Avoidance

- [ ] No contact names or emails unless in CRM or user-provided
- [ ] follow_up_priority derived from DECISION_MODEL score, not arbitrary
- [ ] Objection framing matches CUSTOMER_OBJECTION_LIBRARY — no invented discount offers

## Governance

- [ ] escalation_required true when pricing/legal commitment requested
- [ ] decision_action recommend for drafts; never implies sent
- [ ] confidence band aligns with confidence-scoring.md

## Demo Scenarios

1. **Overdue list** — Rep asks "What's overdue?" → ranked critical/high items with source_records
2. **Re-engagement draft** — Stale opp, post-demo → EMAIL_LIBRARY structured suggested_message
3. **Cadence timing** — "When to follow up on negotiation opp closing in 10 days?" → recommended_timing within 24h
4. **Pricing objection** — Activity notes cite price → value recap message + escalation_required true
5. **Missing contact** — Email requested, no contact email → ask with missing_data populated
6. **Completed task** — User asks about closed activity → answer not overdue, suggest next cadence
