# Sales Playbook

**Enterprise sales knowledge** — imported by all sales-facing agents. Not prompts; operational playbook content.

Implements: [specifications/platform-spec.md](../specifications/platform-spec.md)

## Chapters

### 1. Discovery

- Understand customer business model and pain points
- Identify economic buyer, technical buyer, champion
- Document in CRM (activity + opportunity notes)
- **TBD:** Discovery question frameworks per vertical

### 2. Qualification

- BANT / MEDDIC alignment (see SALES_METHODOLOGIES.md)
- Go/no-go criteria before proposal investment
- **TBD:** Minimum qualification score for pipeline inclusion

### 3. Proposal

- Value proposition tied to customer metrics
- Executive summary per EXECUTIVE_SUMMARY_STANDARD.md
- **TBD:** Proposal template references

### 4. Negotiation

- Authority limits and approval workflows (Layer 4)
- Never commit pricing outside configured bounds
- **TBD:** Objection handling patterns

### 5. Objection Handling

- Acknowledge, clarify, respond with evidence
- Escalate pricing/legal objections per escalation-framework
- **TBD:** Common objection library

### 6. Executive Sponsorship

- When to engage executive stakeholders
- Multi-threading account strategy
- **TBD:** Executive engagement triggers

### 7. Renewals

- Renewal timeline (90/60/30 day checkpoints)
- Risk signals from case history and usage
- **TBD:** Renewal health scoring

### 8. Expansion

- Upsell/cross-sell signals from pipeline and cases
- **TBD:** Expansion play triggers

### 9. Customer Risk

- Churn indicators: case volume, sentiment, engagement gaps
- Link to CUSTOMER_SERVICE_FRAMEWORK.md
- **TBD:** Risk score thresholds

### 10. Forecasting

- Commit vs. best case vs. pipeline definitions
- Manager visibility per PIPELINE_HEALTH_MODEL.md
- **TBD:** Forecast category rules (Layer 4)

## Agent Usage

| Agent | Primary Chapters |
|-------|------------------|
| Sales Rep | Discovery, Qualification, Proposal, Objection |
| Sales Manager | Forecasting, Pipeline Health, Executive Summary |
| Customer Service | Customer Risk, Renewals (supporting) |

## Machine-Readable Contract

```yaml
implements: platform-spec
playbook_version: "1.0.0"
chapters:
  - discovery
  - qualification
  - proposal
  - negotiation
  - objection_handling
  - executive_sponsorship
  - renewals
  - expansion
  - customer_risk
  - forecasting
content_status: outline  # Full content TBD per customer vertical
```
