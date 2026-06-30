# Quality

Correctness, completeness, and hallucination avoidance criteria for this agent.

## Correctness

- [ ] Account tier, industry, and pipeline totals match ServiceNow records
- [ ] Contact names and titles match CRM — role labels marked inferred when not in CRM
- [ ] Case priority and state match case records
- [ ] Opportunity amount, stage, close_date, probability match opp records
- [ ] Buying signals cite verifiable CRM events (stage change, new opp, activity)
- [ ] Risk severity aligns with CUSTOMER_RISK_GUIDE signal definitions
- [ ] Tenant and visibility rules respected

## Completeness

- [ ] All required OUTPUT_SCHEMA fields present (including empty arrays where applicable)
- [ ] account_brief.snapshot populated or gaps listed in missing_data
- [ ] relationship_map includes all contacts with recent activity when available
- [ ] service_context covers open P1/P2 when cases exist
- [ ] recommended_research_questions address identified missing_data gaps
- [ ] Meeting prep includes agenda and recent activities when requested

## Hallucination Avoidance

- [ ] No contact roles presented as confirmed without CRM or activity evidence
- [ ] No external market/news claims in Phase 1
- [ ] assumptions array populated whenever inference used
- [ ] White-space products grounded in KB or explicit assumption
- [ ] No fabricated case or opp IDs in source_records

## Demo Scenarios

| # | Scenario | Expected Output |
|---|----------|-----------------|
| 1 | Full account brief — Tier-1 with open pipeline | Complete schema; buying signals + risks |
| 2 | Relationship map — sparse contacts | Inferred roles in assumptions; research questions to fill gaps |
| 3 | Service health focus — multiple P2 cases | service_context red/yellow; risks severity high |
| 4 | Meeting prep — named CIO + VP | meeting_prep with agenda; attendee enrichment |
| 5 | Ambiguous account name | decision_action: ask with disambiguation |
| 6 | External news request | decision_action: refuse; explain Phase 1 CRM scope |
| 7 | Strategic account + incomplete data | confidence < 0.70; escalate or retrieve after 3 attempts |

## Evaluation Harness (Planned)

Automated validation against OUTPUT_SCHEMA + golden account datasets. See [architecture/domains/testing-deployment](../../architecture/domains/testing-deployment/README.md).
