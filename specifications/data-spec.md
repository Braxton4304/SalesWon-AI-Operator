---
spec_version: "1.0.0"
spec_id: data-spec
title: SalesWon AI Data Specification
---

# Data Specification

Defines the contract for CRM object access, field requirements, permissions, confidence rules, and ownership — separate from platform layout because ServiceNow/SalesWon data access is central to every agent.

## Scope

This spec governs:

- CRM objects agents may read or write
- Required and optional fields per object
- Read/write permissions (including draft-only writes)
- Data confidence rules per object and field
- Missing-data behavior
- User ownership and visibility rules
- Source-of-truth rules

Implementation: [platform/DATA_DICTIONARY.md](../platform/DATA_DICTIONARY.md).

## CRM Objects (v1 Baseline)

| Object | Primary Use | Default Read | Default Write |
|--------|-------------|--------------|---------------|
| `opportunity` | Sales pipeline | Yes | Draft only |
| `account` | Customer organization | Yes | No |
| `contact` | People | Yes | No |
| `case` | Customer service | Yes | Draft only |
| `activity` | Tasks, calls, emails | Yes | Draft only |
| `lead` | Pre-qualification | Yes | Draft only |

Customer-specific extensions are Layer 4 configuration; they MUST extend this spec, not override it silently.

## Field Contract

Every object entry in the data dictionary MUST declare:

```yaml
object: opportunity
purpose: Sales pipeline tracking
readable: true
writable: draft_only          # none | draft_only | full
confidence: high              # high | medium | low | field_dependent
required_fields:
  - amount
  - probability
  - close_date
  - owner
optional_fields:
  - stage
  - description
  - next_step
source_of_truth: servicenow   # servicenow | rag | customer_config
missing_data_behavior: ask    # ask | retrieve | escalate | refuse
ownership_rule: record_owner  # record_owner | team | role_based
visibility_rule: tenant_scope
```

## Read/Write Permission Levels

| Level | Meaning |
|-------|---------|
| `none` | Read or write forbidden; agent may reference via retrieve only if policy allows |
| `read` | Read permitted; no writes |
| `draft_only` | Agent may propose changes; human or workflow must commit |
| `full` | Reserved for approved automation workflows (not default for v1 agents) |

## Data Confidence Rules

Confidence for CRM-backed assertions:

- **High** — All required fields present; record updated within freshness window (TBD per object)
- **Medium** — Required fields present but stale or partial optional context
- **Low** — Missing required fields or conflicting sources
- **Field-dependent** — Confidence computed per field (e.g. `amount` present but `probability` null)

When confidence is low, runtime MUST follow `missing_data_behavior` — never fabricate field values.

## Missing-Data Behavior

| Behavior | When to use |
|----------|-------------|
| `ask` | User can supply missing context |
| `retrieve` | Data may exist in related records or RAG |
| `escalate` | Missing data blocks safe action |
| `refuse` | Policy forbids proceeding without data |

## Ownership and Visibility

- **Record owner** — User sees records they own or their team owns (ServiceNow ACL)
- **Team** — Visibility scoped to assignment group
- **Role-based** — Manager vs. rep visibility (Layer 4 config)
- **Tenant scope** — All queries MUST filter by tenant; cross-tenant access forbidden

## Source-of-Truth Rules

When multiple sources exist, precedence is:

1. ServiceNow CRM record (authoritative for transactional data)
2. Customer configuration (Layer 4) for business rules and stage definitions
3. RAG / knowledge base for procedural and product knowledge
4. Agent inference — **never** source of truth for CRM field values

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: data-spec
baseline_objects:
  - id: opportunity
    readable: true
    writable: draft_only
    confidence: high
    required_fields: [amount, probability, close_date, owner]
    missing_data_behavior: ask
    source_of_truth: servicenow
  - id: account
    readable: true
    writable: none
    confidence: high
    required_fields: [name]
    missing_data_behavior: retrieve
    source_of_truth: servicenow
  - id: contact
    readable: true
    writable: none
    confidence: high
    required_fields: [name]
    missing_data_behavior: ask
    source_of_truth: servicenow
  - id: case
    readable: true
    writable: draft_only
    confidence: high
    required_fields: [short_description, state, assigned_to]
    missing_data_behavior: escalate
    source_of_truth: servicenow
  - id: activity
    readable: true
    writable: draft_only
    confidence: medium
    required_fields: [type, due_date]
    missing_data_behavior: ask
    source_of_truth: servicenow
  - id: lead
    readable: true
    writable: draft_only
    confidence: medium
    required_fields: [name, status]
    missing_data_behavior: ask
    source_of_truth: servicenow
write_levels: [none, read, draft_only, full]
missing_data_behaviors: [ask, retrieve, escalate, refuse]
source_of_truth_precedence:
  - servicenow
  - customer_config
  - rag
  - agent_inference_forbidden_for_crm_fields
dictionary_implementation: platform/DATA_DICTIONARY.md
```

## References

- Implements: [governance-spec.md](governance-spec.md) (tenant isolation, confidence)
- Implemented by: [platform/DATA_DICTIONARY.md](../platform/DATA_DICTIONARY.md), [platform/servicenow.md](../platform/servicenow.md), [platform/database.md](../platform/database.md)
