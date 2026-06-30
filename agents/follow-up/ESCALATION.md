# Escalation

Implements: [shared/escalation-framework.md](../../shared/escalation-framework.md)

## Mandatory (escalation_required: true)

| Condition | Route To |
|-----------|----------|
| Customer requests discount or pricing exception in follow-up context | Sales manager / deal desk |
| Legal, contract, or compliance language needed in suggested_message | Legal + manager |
| Hostile or threatening customer language in activity notes | Manager + CS liaison |
| Confidence < 0.60 on due_date, last activity, or opp close_date | Manager review before send |
| Activity assignee dispute or ownership conflict | Sales ops |

## Conditional

| Condition | Route To |
|-----------|----------|
| Critical overdue on strategic account (Layer 4 list) | Account team + manager |
| Stale opp > $250K with close ≤ 14 days | Sales Rep Agent for deal strategy + manager heads-up |
| Objection: "using competitor" with renewal at risk | Sales Rep + Account Research for differentiation |
| Repeated overdue on same opp (3+ in 30 days) | Manager coaching |

## Output Behavior

- Set `decision_action: escalate` when human approval required before customer contact
- Set `escalation_required: true` on any pricing/legal trigger even if decision_action is recommend
- Include routing target in `recommended_action.type: escalation` with draft_payload.notes

## Not Escalated (handle in-agent)

- Standard overdue reminders without pricing/legal
- Cadence timing questions
- Hygiene follow-ups on low-value early-stage opps
- Missing non-blocking contact fields → ask first
