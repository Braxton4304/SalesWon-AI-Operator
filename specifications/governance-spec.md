---
spec_version: "1.0.0"
spec_id: governance-spec
title: SalesWon AI Governance Specification
---

# Governance Specification

Defines audit, confidence, escalation, security, and tenant isolation requirements for all SalesWon AI operations.

## Governed AI Principles

AI MUST NOT execute or respond without:

1. Audit log entry
2. Confidence score
3. Source grounding (CRM, KB, or explicit policy reference)
4. Deterministic escalation path when below threshold
5. Tenant scope validation
6. Policy check (capabilities + limitations)

Model-only answers without grounding are **forbidden**.

## Confidence Scoring

| Band | Range | Behavior |
|------|-------|----------|
| High | ≥ 0.85 | Answer or recommend |
| Medium | 0.60–0.84 | Answer with caveats; recommend human review for writes |
| Low | < 0.60 | Ask, retrieve, or escalate — do not assert facts |

Thresholds are configurable in `runtime/CONFIG.yaml`; defaults above are normative for v1.

## Escalation Triggers

- Confidence below threshold
- Write permission denied by data-spec
- User explicitly requests human
- Policy violation detected
- Repeated retrieval failure (≥ 3 attempts)
- Sensitive data classification (TBD per customer)

## Security Requirements

- No secrets in source control
- Azure Key Vault for credentials
- Managed Identity preferred over connection strings
- Least-privilege RBAC on every Azure resource
- Tenant isolation: every query filters by tenant; frontend never passes trusted tenant_id

## Audit Record

Every critical operation MUST record:

- `tenant_id`
- `correlation_id`
- `actor` (user or agent ID)
- `timestamp` (UTC)
- `decision_action` (from runtime-spec)
- `confidence_score`
- `source_references`
- `outcome`

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: governance-spec
governed_ai:
  requires:
    - audit_log
    - confidence_score
    - source_grounding
    - escalation_path
    - tenant_scope
    - policy_check
  forbids:
    - model_only_answers
confidence_bands:
  high:
    min: 0.85
    actions: [answer, recommend]
  medium:
    min: 0.60
    max: 0.84
    actions: [answer_with_caveat, recommend_human_review_for_writes]
  low:
    max: 0.59
    actions: [ask, retrieve, escalate]
escalation_triggers:
  - confidence_below_threshold
  - write_permission_denied
  - user_requests_human
  - policy_violation
  - retrieval_failure_threshold: 3
audit_required_fields:
  - tenant_id
  - correlation_id
  - actor
  - timestamp
  - decision_action
  - confidence_score
  - source_references
  - outcome
security:
  secrets_in_source: forbidden
  credential_store: azure_key_vault
  identity: managed_identity_preferred
  tenant_isolation: required
```

## References

- Implements: none (cross-cutting contract)
- Implemented by: [runtime/GOVERNANCE.md](../runtime/GOVERNANCE.md), [runtime/SECURITY.md](../runtime/SECURITY.md), [shared/confidence-scoring.md](../shared/confidence-scoring.md), [shared/escalation-framework.md](../shared/escalation-framework.md)
