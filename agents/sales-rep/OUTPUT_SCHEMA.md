# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

Every response MUST validate against this schema.

## Processing Pipeline

```text
Input
  │
  ├─ Parse rep request (opp name/ID, pipeline scope, meeting prep, objection type)
  ├─ Resolve visibility boundary (authenticated rep's pipeline)
  └─ decision_action: ask if opp ambiguous or scope unclear
  │
Processing
  │
  ├─ Retrieve: query_opportunity → query_activities → query_contacts
  ├─ Optional: query_account, query_lead, retrieve_knowledge
  ├─ Apply MEDDIC/SPIN/Sandler gap analysis → qualification_gaps
  ├─ Score deal_health per PIPELINE_HEALTH_MODEL
  ├─ Compute priority_score per DECISION_MODEL (weights sum 100%)
  ├─ Generate next_best_action + recommended_questions
  ├─ Assemble opportunity_summary
  └─ Propose suggested_follow_up (draft email or activity — recommend only)
  │
Output
  │
  ├─ SalesRepAgentOutput JSON (all required fields)
  ├─ summary: human-readable rep headline
  └─ source_records: field-level audit trail
  │
Confidence
  │
  ├─ Compute per TRUST_MODEL factor table
  ├─ Reduce for missing required fields, stale activity data, inferred roles
  └─ Band: high ≥0.85 | medium 0.60–0.84 | low <0.60
  │
Escalation
  │
  ├─ Set escalation_required when mandatory triggers fire
  ├─ confidence < 0.60 after 3 retrieves → decision_action: escalate
  ├─ pricing/discount request → refuse + escalation_required
  └─ Include escalation_payload per ESCALATION.md when escalating
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
  "title": "SalesRepAgentOutput",
  "type": "object",
  "required": [
    "summary",
    "confidence",
    "sources",
    "decision_action",
    "opportunity_summary",
    "deal_health",
    "qualification_gaps",
    "next_best_action",
    "recommended_questions",
    "suggested_follow_up",
    "missing_data",
    "escalation_required",
    "source_records"
  ],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Rep-facing headline — deal posture and primary recommendation"
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
    "opportunity_summary": {
      "type": "object",
      "required": ["opportunity_id", "name", "stage"],
      "properties": {
        "opportunity_id": { "type": "string" },
        "name": { "type": "string" },
        "account_id": { "type": "string" },
        "account_name": { "type": "string" },
        "stage": { "type": "string" },
        "amount": { "type": "number" },
        "probability": { "type": "number", "minimum": 0, "maximum": 100 },
        "weighted_amount": { "type": "number" },
        "close_date": { "type": "string", "format": "date" },
        "days_to_close": { "type": "integer" },
        "owner": { "type": "string" },
        "next_step": { "type": "string" },
        "forecast_category": {
          "enum": ["commit", "best_case", "pipeline", "omitted", "unknown"]
        },
        "competitors": {
          "type": "array",
          "items": { "type": "string" }
        },
        "key_contacts": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "contact_id": { "type": "string" },
              "name": { "type": "string" },
              "role_label": { "type": "string" }
            }
          }
        },
        "last_activity_date": { "type": "string", "format": "date" },
        "days_since_activity": { "type": "integer" },
        "headline": { "type": "string" }
      }
    },
    "deal_health": {
      "enum": ["healthy", "at_risk", "critical", "not_applicable"],
      "description": "Per PIPELINE_HEALTH_MODEL — use not_applicable for pipeline-only or lead requests"
    },
    "qualification_gaps": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["field", "methodology", "severity"],
        "properties": {
          "field": { "type": "string" },
          "methodology": {
            "enum": ["MEDDIC", "SPIN", "Sandler", "CRM"]
          },
          "severity": {
            "enum": ["blocking", "important", "nice_to_have"]
          },
          "rationale": { "type": "string" },
          "crm_field": { "type": "string" },
          "recommended_action": { "type": "string" }
        }
      }
    },
    "next_best_action": {
      "type": "object",
      "required": ["action", "rationale", "priority_score"],
      "properties": {
        "action": { "type": "string" },
        "rationale": { "type": "string" },
        "priority_score": {
          "type": "number",
          "minimum": 0,
          "maximum": 100,
          "description": "DECISION_MODEL weighted score × 100"
        },
        "priority_score_factors": {
          "type": "object",
          "properties": {
            "close_date_urgency": { "type": "number" },
            "revenue_at_stake": { "type": "number" },
            "qualification_gap_severity": { "type": "number" },
            "activity_recency_gap": { "type": "number" },
            "deal_health_severity": { "type": "number" },
            "user_explicit_focus": { "type": "number" }
          }
        },
        "due_within_days": { "type": "integer" },
        "activity_type": {
          "enum": ["call", "email", "meeting", "crm_update", "discovery", "other"]
        },
        "related_contact_id": { "type": "string" },
        "related_opportunity_id": { "type": "string" }
      }
    },
    "recommended_questions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["question", "methodology", "purpose"],
        "properties": {
          "question": { "type": "string" },
          "methodology": {
            "enum": ["MEDDIC", "SPIN", "Sandler"]
          },
          "purpose": { "type": "string" },
          "target_contact_role": { "type": "string" },
          "addresses_gap": { "type": "string" }
        }
      }
    },
    "suggested_follow_up": {
      "type": "object",
      "properties": {
        "type": {
          "enum": ["email_draft", "activity_task", "opportunity_update", "none"]
        },
        "target_record_id": { "type": "string" },
        "target_record_type": {
          "enum": ["opportunity", "contact", "lead", "activity"]
        },
        "subject": { "type": "string" },
        "body_or_description": { "type": "string" },
        "due_date": { "type": "string", "format": "date" },
        "draft_payload": { "type": "object" }
      }
    },
    "missing_data": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["field", "impact"],
        "properties": {
          "field": { "type": "string" },
          "impact": { "type": "string" },
          "suggested_resolution": { "type": "string" }
        }
      }
    },
    "escalation_required": {
      "type": "boolean",
      "description": "True when mandatory escalation triggers per ESCALATION.md"
    },
    "escalation_payload": {
      "type": "object",
      "properties": {
        "reason": { "type": "string" },
        "route_to": { "type": "string" },
        "urgency": { "enum": ["standard", "high", "critical"] }
      }
    },
    "source_records": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["record_type", "record_id", "fields_used"],
        "properties": {
          "record_type": {
            "enum": ["opportunity", "account", "contact", "activity", "lead", "case", "kb"]
          },
          "record_id": { "type": "string" },
          "label": { "type": "string" },
          "fields_used": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "field": { "type": "string" },
                "value": { "type": "string" },
                "confidence": {
                  "enum": ["confirmed", "inferred", "unknown"]
                }
              }
            }
          },
          "retrieved_at": { "type": "string", "format": "date-time" }
        }
      }
    },
    "clarifying_question": { "type": "string" },
    "pipeline_rankings": {
      "type": "array",
      "description": "Present for 'what should I do today' requests",
      "items": {
        "type": "object",
        "properties": {
          "opportunity_id": { "type": "string" },
          "name": { "type": "string" },
          "priority_score": { "type": "number" },
          "deal_health": {
            "enum": ["healthy", "at_risk", "critical"]
          },
          "next_action_summary": { "type": "string" }
        }
      }
    }
  }
}
```

## Example (Deal Review)

```json
{
  "summary": "Acme Expansion is At Risk: $120K at 45%, closes in 12 days, no activity in 18 days. Schedule economic buyer call.",
  "confidence": 0.91,
  "sources": [
    { "type": "crm", "id": "opp789", "label": "Acme Expansion FY26" },
    { "type": "policy", "id": "meddic", "label": "MEDDIC Qualification" }
  ],
  "decision_action": "recommend",
  "opportunity_summary": {
    "opportunity_id": "opp789",
    "name": "Acme Expansion FY26",
    "account_id": "acct101",
    "account_name": "Acme Corp",
    "stage": "Proposal",
    "amount": 120000,
    "probability": 45,
    "weighted_amount": 54000,
    "close_date": "2026-07-12",
    "days_to_close": 12,
    "owner": "jordan.rep",
    "next_step": "Follow up on demo feedback",
    "forecast_category": "pipeline",
    "key_contacts": [
      { "contact_id": "con55", "name": "Sam Lee", "role_label": "champion" }
    ],
    "last_activity_date": "2026-06-12",
    "days_since_activity": 18,
    "headline": "Late-stage opp stalling — missing economic buyer engagement"
  },
  "deal_health": "at_risk",
  "qualification_gaps": [
    {
      "field": "economic_buyer",
      "methodology": "MEDDIC",
      "severity": "blocking",
      "rationale": "Proposal stage with no economic_buyer contact in CRM",
      "crm_field": "contact.role",
      "recommended_action": "Identify and engage budget authority before close"
    }
  ],
  "next_best_action": {
    "action": "Schedule executive alignment call with economic buyer",
    "rationale": "Late stage without C-level contact; close date in 12 days",
    "priority_score": 84,
    "priority_score_factors": {
      "close_date_urgency": 0.26,
      "revenue_at_stake": 0.135,
      "qualification_gap_severity": 0.15,
      "activity_recency_gap": 0.129,
      "deal_health_severity": 0.065,
      "user_explicit_focus": 0.1
    },
    "due_within_days": 3,
    "activity_type": "meeting",
    "related_opportunity_id": "opp789"
  },
  "recommended_questions": [
    {
      "question": "Who owns the budget approval for this expansion, and what criteria will they use to decide?",
      "methodology": "MEDDIC",
      "purpose": "Identify economic buyer and decision criteria",
      "target_contact_role": "champion",
      "addresses_gap": "economic_buyer"
    },
    {
      "question": "What happens if this initiative is delayed past Q3 — impact on your team's goals?",
      "methodology": "SPIN",
      "purpose": "Implication — create urgency",
      "target_contact_role": "champion",
      "addresses_gap": "identify_pain"
    }
  ],
  "suggested_follow_up": {
    "type": "email_draft",
    "target_record_id": "con55",
    "target_record_type": "contact",
    "subject": "Acme Expansion — executive alignment next steps",
    "body_or_description": "Hi Sam, following our demo I'd like to schedule a brief call with your budget owner to align on timeline and success metrics before our July 12 target...",
    "draft_payload": { "template": "post_demo_executive_intro" }
  },
  "missing_data": [],
  "escalation_required": false,
  "source_records": [
    {
      "record_type": "opportunity",
      "record_id": "opp789",
      "label": "Acme Expansion FY26",
      "fields_used": [
        { "field": "amount", "value": "120000", "confidence": "confirmed" },
        { "field": "probability", "value": "45", "confidence": "confirmed" },
        { "field": "close_date", "value": "2026-07-12", "confidence": "confirmed" },
        { "field": "stage", "value": "Proposal", "confidence": "confirmed" }
      ]
    },
    {
      "record_type": "activity",
      "record_id": "act550",
      "label": "Demo follow-up email",
      "fields_used": [
        { "field": "completed_date", "value": "2026-06-12", "confidence": "confirmed" }
      ]
    }
  ]
}
```

## Field Population Rules

| Request Type | Primary Fields | Optional / Empty |
|--------------|----------------|------------------|
| Single opp review | All required | pipeline_rankings empty |
| Pipeline today | pipeline_rankings + condensed opportunity_summary per top opp | suggested_follow_up per top opp optional |
| Meeting prep | opportunity_summary + suggested_follow_up | qualification_gaps if not requested |
| Objection coaching | next_best_action + recommended_questions | suggested_follow_up if draft requested |
| Discount request | escalation_required=true, refuse | suggested_follow_up none |

## Validation Notes

- `priority_score` uses DECISION_MODEL weights summing to 100%
- `qualification_gaps` must reference real CRM/methodology fields — empty array if fully qualified
- `recommended_questions` empty array when not discovery/qualification context
- `suggested_follow_up.type: none` when no draft appropriate
- `deal_health: not_applicable` for lead-only or pipeline-list-only responses
- `escalation_required` must align with ESCALATION.md mandatory triggers

```yaml
output_schema_version: "1.1.0"
agent_id: sales-rep
required_role_fields:
  - opportunity_summary
  - deal_health
  - qualification_gaps
  - next_best_action
  - recommended_questions
  - suggested_follow_up
  - confidence
  - missing_data
  - escalation_required
  - source_records
decision_model_weights_sum: 100
```
