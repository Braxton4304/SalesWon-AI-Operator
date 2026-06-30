# Output Schema

Implements: [specifications/agent-spec.md](../../specifications/agent-spec.md)

Every response MUST validate against this schema. Customer Service, Sales Rep, and Sales Manager agents extend with role-specific fields.

## Machine-Readable Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ReferenceAgentOutput",
  "type": "object",
  "required": ["summary", "confidence", "sources", "decision_action"],
  "properties": {
    "summary": {
      "type": "string",
      "description": "Human-readable response summary"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
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
    "recommended_action": {
      "type": "object",
      "description": "Required when decision_action is recommend",
      "properties": {
        "type": { "type": "string" },
        "target_record_id": { "type": "string" },
        "draft_payload": { "type": "object" }
      }
    },
    "clarifying_question": {
      "type": "string",
      "description": "Required when decision_action is ask"
    }
  }
}
```

## Role Extensions (Examples)

### Customer Service Agent (future)

Add: `customer_sentiment`, `case_priority`, `sla_status`

### Sales Rep Agent (future)

Add: `opportunity_health`, `next_best_action`

### Sales Manager Agent (future)

Add: `pipeline_summary`, `forecast_risk`, `team_coverage`

Copy this file and extend `properties` when creating role-specific agents.
