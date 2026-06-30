# Metrics

Operational metrics for this agent. Feeds platform observability and improvement loops.

## Quality Metrics

| Metric | Description | Target (TBD) |
|--------|-------------|--------------|
| Schema compliance rate | OUTPUT_SCHEMA validation pass % | > 99% |
| Source grounding rate | Responses with ≥1 source | > 95% |
| Hallucination incidents | Fabricated CRM fields detected | 0 |

## Usage Metrics

| Metric | Description |
|--------|-------------|
| Acceptance rate | User accepts recommendation without edit |
| User edit rate | User modifies draft before send |
| Escalation rate | % of turns ending in escalate |
| Average confidence | Mean confidence score |
| Retrieval rate | % of turns using retrieve action |

## Business Metrics

| Metric | Description |
|--------|-------------|
| ROI impact | TBD — link to ROI_SCORING_MODEL |
| SLA impact | TBD — for service agents |
| Pipeline impact | TBD — for sales agents |

## Collection

Planned: `platform/observability.md` + Azure App Insights. Audit records per governance-spec.
