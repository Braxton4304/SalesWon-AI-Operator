# Metrics

Operational and business metrics for this agent. Feeds platform observability and improvement loops.

## Operational Metrics

| Metric | Description | Target (Phase 1 pilot) |
|--------|-------------|--------------------------|
| Schema compliance rate | OUTPUT_SCHEMA validation pass % | ≥ 99% |
| Source grounding rate | Responses with ≥1 source_record per factual section | ≥ 98% |
| Hallucination incidents | Fabricated CRM fields detected | 0 |
| Mean confidence | Average confidence score | ≥ 0.82 |
| Retrieval rate | % of turns using retrieve action | Track |
| Escalation rate | % of turns ending in escalate | < 8% |
| Ask/disambiguation rate | Ambiguous account requests | Track |

## Quality Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Brief completeness | Required sections populated from CRM | ≥ 90% |
| Assumption labeling rate | Inferences tagged in assumptions | 100% |
| Risk flag precision | Risks matching CUSTOMER_RISK_GUIDE on audit sample | ≥ 85% |
| Research question count | Default 3–5 SPIN questions per brief | 100% compliance |

## Usage Metrics

| Metric | Description |
|--------|-------------|
| Brief acceptance rate | User uses output without major rewrite |
| Section skip rate | User requests subset (e.g., service only) |
| Handoff citation rate | Sales Rep/Manager references account_brief (Phase 2) |
| Repeat account research | Same account researched within 7 days |

## Business Metrics

| Metric | Description | Link |
|--------|-------------|------|
| Meeting prep time saved | User-reported minutes saved vs. manual research | Pilot survey |
| Discovery quality uplift | Rep rates research questions useful | ≥ 75% |
| Expansion signal conversion | Buying signals → opp progression (Phase 2 analytics) | ACCOUNT_PLANNING |
| Service-risk early detection | P1/P2 flagged before rep meeting | CUSTOMER_RISK_GUIDE |
| Pipeline influenced | Open pipeline on researched accounts | CRM rollup |

## Collection

Planned: `platform/observability.md` + Azure App Insights. Audit records per governance-spec.

```yaml
metrics_version: "1.0.0"
agent_id: account-research
primary_artifact: account_brief
```
