# Decision Model

Agent-specific prioritization. **Runtime [DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md) governs** — this file adjusts weights within allowed actions.

## Priority Order

1. **Customer risk signals** — P1/P2 cases, executive escalations, renewal opp + open cases (CUSTOMER_RISK_GUIDE)
2. **Meeting urgency** — User-provided meeting date within 7 days elevates completeness requirement
3. **Revenue context** — Open pipeline amount and stage progression on account
4. **Relationship completeness** — Missing economic buyer or champion on active late-stage opp
5. **User explicit scope** — Named account, opp, or meeting attendees override generic research depth

## Scenario Matrix

| Scenario | Action |
|----------|--------|
| Account name/ID given, record found | answer with full OUTPUT_SCHEMA |
| Account name ambiguous (multiple matches) | ask with candidate list |
| Meeting prep with attendees named | enrich relationship_map for attendees + MEETING_PREPARATION structure |
| Strategic/tier-1 account flag in CRM | deeper relationship_map + risk scan; escalate if confidence < 0.70 after retrieve |
| Sparse contact data | answer with assumptions labeled; recommend research questions to fill gaps |
| Multiple open P1 cases | elevate risks severity; include in account_brief headline |
| Required account fields missing | retrieve related opps/contacts once, then missing_data |
| External market question (news, stock) | refuse — outside Phase 1 scope |

## Weighted Scoring (Research Depth)

| Factor | Weight | Source |
|--------|--------|--------|
| Account tier / strategic flag | 1.0 | CRM account |
| Open pipeline value | 0.9 | CRM opportunity |
| Service risk score | 0.9 | CUSTOMER_RISK_GUIDE |
| Meeting within 7 days | 0.85 | User request |
| Contact coverage (roles mapped) | 0.8 | CRM contact + activity |
| Activity recency | 0.7 | CRM activity |

## Business Reasoning Weights

Revenue 0.9, Sales Velocity 1.0, Customer Retention 0.85, Manager Visibility 0.75

## Cannot Override

- governance-spec confidence thresholds
- data-spec write permissions (account: none)
- escalation-framework mandatory triggers
