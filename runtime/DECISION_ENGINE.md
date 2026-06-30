# Decision Engine

Implements: [specifications/runtime-spec.md](../specifications/runtime-spec.md)

Governing logic for how the runtime chooses an action — not simply "answer the question."

## Decision Actions

| Action | When | Next Step |
|--------|------|-----------|
| **answer** | Confidence ≥ threshold; required data present; policy allows | Emit OUTPUT_SCHEMA payload |
| **ask** | Missing required fields; ambiguous intent; user can clarify | Structured clarifying question |
| **retrieve** | Data may exist in CRM or KB; retrieval attempts < max | Fetch per data-spec; re-evaluate |
| **escalate** | Confidence low after retrieval; policy blocks; user requests human | Route per escalation-framework |
| **refuse** | Action forbidden by LIMITATIONS or data-spec write rules | Explain refusal with policy ref |
| **recommend** | Safe to propose but not execute (draft_only writes) | OUTPUT_SCHEMA with recommended_action |

## Decision Flow

```text
User Request
    → Parse intent
    → Check capabilities + limitations
    → Check data-spec permissions
    → Assess data completeness + confidence
    → Select action
    → If answer/recommend: validate OUTPUT_SCHEMA
    → Write audit record
    → Return
```

## Rules

1. **Never fabricate CRM fields** — if missing, use ask/retrieve/escalate per data-spec `missing_data_behavior`.
2. **Retrieve before escalate** — up to `max_retrieval_attempts` (default 3) unless policy forbids.
3. **Draft-only writes** — always `recommend`, never direct commit.
4. **Low confidence** — default to `ask` or `escalate`, not `answer`.

## Machine-Readable Contract

```yaml
implements: runtime-spec
actions:
  answer:
    requires: [confidence_gte_threshold, required_fields_present, policy_allowed]
  ask:
    triggers: [missing_required_fields, ambiguous_intent]
  retrieve:
    triggers: [incomplete_crm_context, kb_may_help]
    max_attempts: 3
  escalate:
    triggers: [confidence_below_threshold, retrieval_exhausted, user_request, policy_block]
  refuse:
    triggers: [capability_denied, write_forbidden, security_violation]
  recommend:
    triggers: [draft_only_write, safe_proposal]
default_on_ambiguity: ask
```

## Agent Override

Agents may define prioritization in `DECISION_MODEL.md` but **cannot** add new actions or bypass governance.
