# Organizational Memory

Implements: [specifications/workforce-spec.md](../specifications/workforce-spec.md)

**Company memory** — consumed by every Digital Employee. Not user memory (see MEMORY_SHORT/LONG).

## Contents

### Major Customers / Strategic Accounts

- Layer 4 configuration pointers (account tiers, strategic flags)
- Never store live CRM field values here — query ServiceNow

### Preferred Processes

- Case handling tiers (CUSTOMER_SERVICE_FRAMEWORK)
- Opportunity stage definitions (Layer 4)
- Approval matrix summary (policies/APPROVAL_POLICY.md)

### Corporate Standards

- Sales methodology default: MEDDIC primary, SPIN for discovery, Sandler checkpoints for qualification
- Communication: COMMUNICATION_STANDARD, EMAIL_STYLE_GUIDE
- Executive summaries: EXECUTIVE_SUMMARY_STANDARD

### Terminology

- Opportunity, Case, Activity, Lead — per data-spec naming
- Forecast categories: Commit, Best Case, Pipeline (Layer 4 labels)

### Product Catalog

- Layer 4 product/SKU references for qualification
- RAG knowledge base index paths

### Historical Lessons (Aggregated)

- No raw PII
- Patterns: "Enterprise deals stall without economic buyer by stage 3"
- Updated via manager review + ADR — not agent self-write in Phase 1

## Consumption Rules

1. Organizational memory **supplements** CRM — never overrides CRM facts
2. Conflicts: CRM wins; flag in TRUST_MODEL assumptions
3. Loaded in RUNTIME_CONTEXT after system prompt, before agent prompt (Layer 4 org config slot)

## Machine-Readable Contract

```yaml
org_memory_version: "1.0.0"
source_of_truth_for_crm_fields: servicenow
consumers: all_digital_employees
update_authority: platform_team_layer_4
pii_allowed: false
```
