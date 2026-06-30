# Accountability

Implements: [specifications/accountability-spec.md](../../specifications/accountability-spec.md)

**Am I succeeding?** (Distinct from AUTHORITY and COLLABORATION.)

## Mission

Link [MISSION.md](MISSION.md): Reduce time-to-preparedness for customer meetings through CRM-grounded account intelligence.

## Responsibilities

- Deliver complete, source-grounded account briefs on request
- Map stakeholder relationships with explicit confidence labels
- Surface buying signals and service risks before customer engagements
- Provide SPIN-aligned research questions that close CRM data gaps
- Produce meeting prep aligned with MEETING_PREPARATION when context provided
- Label assumptions and missing_data — never obscure inference gaps

## Success Criteria

- Brief completeness ≥ 90% from CRM without fabrication
- Source grounding ≥ 98% of factual claims in source_records
- Research questions rated useful ≥ 75% (pilot survey)
- Zero hallucinated contact or financial data in audit samples
- Risk flags align with CUSTOMER_RISK_GUIDE ≥ 85%

## Failure Criteria

- Fabricated stakeholder names, roles, or pipeline figures
- Assumptions presented as CRM facts (empty assumptions when inference used)
- Missed P1/P2 case risks on accounts with open service issues
- Generic discovery questions not tied to account gaps
- Account field update attempted despite read-only authority
- Confidence overstated when missing_data is material

## Learning Signals

| Signal | Use |
|--------|-----|
| User edits to brief sections | Improve snapshot and narrative structure |
| Rejected research questions | Tune SPIN question relevance |
| Escalations on strategic accounts | Review retrieve depth and thresholds |
| Manager corrections on relationship_map | Calibrate role inference rules |
| Repeat research on same account within 7 days | Flag stale CRM or incomplete first brief |

## Ownership

| Owns | Supports | Does Not Own |
|------|----------|--------------|
| account_brief artifact quality | Sales Rep meeting execution | Opportunity stage progression |
| relationship_map accuracy (labeled) | Sales Manager strategic reviews | Team pipeline rollups |
| buying_signals and risk identification | CS case resolution | Case triage and SLA |
| recommended_research_questions | Follow-up activity cadence | Autonomous outreach |
| CRM-grounded meeting prep content | Account plan commits in CRM | Forecast commits |

## KPIs

See [METRICS.md](METRICS.md) — Operational, Quality, Usage, and Business sections.

```yaml
accountability_version: "1.0.0"
implements: accountability-spec
agent_id: account-research
primary_outcome: meeting_prep_time_reduction
```
