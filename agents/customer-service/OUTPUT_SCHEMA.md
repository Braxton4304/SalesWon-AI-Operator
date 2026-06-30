# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

Every response MUST validate against this schema.

## Processing Pipeline

```text
Input
  │
  ├─ Parse user request (case number, account, triage type, draft request)
  ├─ Resolve case/account/contact identifiers
  └─ decision_action: ask if case number or account ambiguous
  │
Processing
  │
  ├─ Retrieve: query_case → query_account → query_contact → query_account_cases (if needed)
  ├─ Optional: retrieve_knowledge for resolution procedures
  ├─ Apply CUSTOMER_SERVICE_FRAMEWORK sentiment and tier rules
  ├─ Assess ITIL impact + urgency (case fields or reasoned inference)
  ├─ Compute DECISION_MODEL priority_score (35/30/15/10/10)
  ├─ Derive severity from priority_score bands
  ├─ Evaluate SLA proximity → sla_status in case_summary
  ├─ Check ESCALATION.md triggers → escalation_required + escalation_reason
  ├─ Assemble case_summary structured object
  ├─ Generate suggested_customer_response when draft requested
  └─ Propose recommended_action (draft or escalation routing)
  │
Output
  │
  ├─ CustomerServiceAgentOutput JSON (all required fields)
  ├─ summary: human-readable rep headline
  └─ source_records: field-level audit trail
  │
Confidence
  │
  ├─ Compute per TRUST_MODEL factor table
  ├─ Reduce for missing required fields, inferred ITIL, stale case data
  └─ Band: high ≥0.85 | medium 0.60–0.84 | low <0.60
  │
Escalation
  │
  ├─ confidence < 0.60 after 3 retrieves → decision_action: escalate
  ├─ mandatory trigger fired → escalation_required: true
  └─ Include escalation payload per ESCALATION.md when escalating
  │
Audit
  │
  ├─ Log tool calls, decision_action, confidence, sources
  ├─ source_records authoritative for factual assertions
  └─ Persist per governance-spec audit record
```

## Machine-Readable Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CustomerServiceAgentOutput",
  "type": "object",
  "required": [
    "summary",
    "confidence",
    "sources",
    "decision_action",
    "case_summary",
    "customer_sentiment",
    "severity",
    "impact",
    "urgency",
    "recommended_action",
    "escalation_required",
    "escalation_reason",
    "missing_data",
    "suggested_customer_response",
    "source_records"
  ],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Rep-facing headline — case status, SLA posture, or triage finding"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "description": "Overall response confidence per TRUST_MODEL"
    },
    "sources": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "id"],
        "properties": {
          "type": { "enum": ["crm", "kb", "policy"] },
          "id": { "type": "string" },
          "label": { "type": "string" }
        }
      }
    },
    "decision_action": {
      "enum": ["answer", "ask", "retrieve", "escalate", "refuse", "recommend"]
    },
    "case_summary": {
      "type": "object",
      "required": ["case_number", "state", "short_description"],
      "properties": {
        "case_number": { "type": "string" },
        "sys_id": { "type": "string" },
        "state": { "type": "string" },
        "short_description": { "type": "string" },
        "priority": { "enum": ["critical", "high", "moderate", "low", "unknown"] },
        "assigned_to": { "type": "string" },
        "account": { "type": "string" },
        "contact": { "type": "string" },
        "opened_at": { "type": "string", "format": "date-time" },
        "last_public_update": { "type": "string", "format": "date-time" },
        "priority_score": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "DECISION_MODEL weighted score"
        },
        "sla_status": {
          "type": "object",
          "properties": {
            "state": { "enum": ["on_track", "at_risk", "breached", "not_applicable"] },
            "time_remaining_minutes": { "type": ["number", "null"] },
            "policy_name": { "type": "string" }
          }
        },
        "work_notes_summary": { "type": "string" },
        "related_cases": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "case_number": { "type": "string" },
              "state": { "type": "string" },
              "priority": { "type": "string" },
              "severity": { "enum": ["critical", "high", "medium", "low"] }
            }
          }
        }
      }
    },
    "customer_sentiment": {
      "enum": ["positive", "neutral", "frustrated", "angry", "unknown"]
    },
    "severity": {
      "enum": ["critical", "high", "medium", "low"],
      "description": "Derived from DECISION_MODEL priority_score bands"
    },
    "impact": {
      "type": "object",
      "required": ["level", "rationale"],
      "properties": {
        "level": { "enum": ["high", "medium", "low"] },
        "rationale": { "type": "string" },
        "source": { "enum": ["crm_field", "inferred", "user_provided"] }
      }
    },
    "urgency": {
      "type": "object",
      "required": ["level", "rationale"],
      "properties": {
        "level": { "enum": ["high", "medium", "low"] },
        "rationale": { "type": "string" },
        "source": { "enum": ["crm_field", "inferred", "user_provided"] }
      }
    },
    "recommended_action": {
      "type": "object",
      "required": ["type", "description"],
      "properties": {
        "type": {
          "enum": ["email_draft", "work_note", "state_change", "follow_up_task", "escalation", "monitor", "none"]
        },
        "description": { "type": "string" },
        "target_record_id": { "type": "string" },
        "draft_payload": {
          "type": "object",
          "properties": {
            "subject": { "type": "string" },
            "body": { "type": "string" },
            "proposed_state": { "type": "string" },
            "suggested_assignee_group": { "type": "string" }
          }
        }
      }
    },
    "escalation_required": { "type": "boolean" },
    "escalation_reason": {
      "type": ["string", "null"],
      "description": "Null when escalation_required is false; trigger ID + rationale when true"
    },
    "missing_data": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["field", "object", "impact"],
        "properties": {
          "field": { "type": "string" },
          "object": { "enum": ["case", "account", "contact", "activity", "sla"] },
          "impact": { "type": "string" }
        }
      }
    },
    "suggested_customer_response": {
      "type": ["object", "null"],
      "description": "Null when no draft requested; populated per EMAIL_STYLE_GUIDE when drafting",
      "properties": {
        "subject": { "type": "string" },
        "body": { "type": "string" },
        "tone": { "enum": ["empathetic", "informational", "apologetic", "confirmatory"] },
        "requires_human_send": { "type": "boolean", "const": true }
      }
    },
    "source_records": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["object", "id"],
        "properties": {
          "object": { "enum": ["case", "account", "contact", "activity", "kb", "policy"] },
          "id": { "type": "string" },
          "label": { "type": "string" },
          "fields_used": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "clarifying_question": {
      "type": "string",
      "description": "Required when decision_action is ask"
    }
  }
}
```

## Example (Demo — At-Risk P2 Case with Draft)

```json
{
  "summary": "Case INC0012345 is In Progress (P2), assigned to Jane Doe, SLA at risk with 90 minutes remaining. ITIL: high impact, high urgency — severity critical. Recommend immediate customer update and Tier 2 review.",
  "confidence": 0.91,
  "sources": [
    { "type": "crm", "id": "abc123def456", "label": "INC0012345" },
    { "type": "crm", "id": "acct789", "label": "Acme Manufacturing" },
    { "type": "policy", "id": "customer_service_framework", "label": "CUSTOMER_SERVICE_FRAMEWORK" }
  ],
  "decision_action": "recommend",
  "case_summary": {
    "case_number": "INC0012345",
    "sys_id": "abc123def456",
    "state": "In Progress",
    "short_description": "Production API integration failing — orders not syncing",
    "priority": "high",
    "assigned_to": "Jane Doe",
    "account": "Acme Manufacturing",
    "contact": "Sarah Chen",
    "opened_at": "2026-06-28T14:22:00Z",
    "last_public_update": "2026-06-29T09:15:00Z",
    "priority_score": 0.87,
    "sla_status": {
      "state": "at_risk",
      "time_remaining_minutes": 90,
      "policy_name": "P2 Response"
    },
    "work_notes_summary": "Engineering investigating API timeout; customer reported 200+ failed orders since 06/28."
  },
  "customer_sentiment": "frustrated",
  "severity": "critical",
  "impact": {
    "level": "high",
    "rationale": "Production order sync failure affecting enterprise-wide order processing",
    "source": "crm_field"
  },
  "urgency": {
    "level": "high",
    "rationale": "No workaround; revenue-impacting outage ongoing 36+ hours",
    "source": "inferred"
  },
  "recommended_action": {
    "type": "email_draft",
    "description": "Send customer status update acknowledging impact and confirming engineering escalation",
    "target_record_id": "abc123def456",
    "draft_payload": {
      "subject": "Update on your request INC0012345 — production API issue",
      "body": "Dear Sarah,\n\nThank you for your patience. I understand the production API integration issue is significantly impacting your order processing, and I want to provide a clear update.\n\nOur engineering team is actively investigating the API timeout errors reported since June 28. We have escalated this internally given the production impact.\n\nNext step: We will provide a technical update within the next 2 hours. Could you confirm whether the failure rate has changed since your last report?\n\nBest regards,\nJane Doe\nCustomer Support"
    }
  },
  "escalation_required": true,
  "escalation_reason": "SLA-IMMINENT: P2 response SLA at risk (90 min remaining) with high impact production outage; VIP account Acme Manufacturing per account tier",
  "missing_data": [],
  "suggested_customer_response": {
    "subject": "Update on your request INC0012345 — production API issue",
    "body": "Dear Sarah,\n\nThank you for your patience. I understand the production API integration issue is significantly impacting your order processing, and I want to provide a clear update.\n\nOur engineering team is actively investigating the API timeout errors reported since June 28. We have escalated this internally given the production impact.\n\nNext step: We will provide a technical update within the next 2 hours. Could you confirm whether the failure rate has changed since your last report?\n\nBest regards,\nJane Doe\nCustomer Support",
    "tone": "empathetic",
    "requires_human_send": true
  },
  "source_records": [
    { "object": "case", "id": "abc123def456", "label": "INC0012345", "fields_used": ["state", "priority", "impact", "urgency", "assigned_to", "short_description"] },
    { "object": "account", "id": "acct789", "label": "Acme Manufacturing", "fields_used": ["name", "tier", "strategic_flag"] },
    { "object": "contact", "id": "con456", "label": "Sarah Chen", "fields_used": ["name", "email"] },
    { "object": "policy", "id": "customer_service_framework", "label": "CUSTOMER_SERVICE_FRAMEWORK", "fields_used": ["sentiment_handling", "sla_tiers"] }
  ]
}
```

## Field Notes

- `confidence` reflects overall response quality per [TRUST_MODEL.md](TRUST_MODEL.md)
- `escalation_reason` is null (JSON null) when `escalation_required` is false
- `suggested_customer_response` is null when user did not request a draft
- `missing_data` is always an array — empty when complete
- `priority_score` in case_summary uses DECISION_MODEL weights summing to 100%
- `severity` derived from priority_score per DECISION_MODEL bands
- `source_records` is the authoritative audit trail; `sources` remains for runtime compatibility
- `recommended_action.type: none` valid for informational answers with no next action

```yaml
output_schema_version: "1.0.0"
agent_id: customer-service
primary_artifacts: [case_summary, suggested_customer_response]
pipeline_stages: [input, processing, output, confidence, escalation, audit]
decision_model_weights: [35, 30, 15, 10, 10]
```
