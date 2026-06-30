# Runtime Context Assembly

Implements: [specifications/runtime-spec.md](../specifications/runtime-spec.md)

**Single source of truth** for what context is assembled before every LLM call.

## Assembly Order

```text
1. System Prompt
        ↓
2. Agent Prompt
        ↓
3. Customer Configuration
        ↓
4. ServiceNow / CRM Data
        ↓
5. Knowledge Retrieval (RAG)
        ↓
6. User Behavior Signals
        ↓
7. Conversation History (Short Memory)
        ↓
8. Current User Request
```

## Layer Details

### 1. System Prompt

- Platform identity and governed AI rules
- governance-spec requirements (no model-only answers)
- Tenant scope reminder
- Source: `runtime/GOVERNANCE.md`, `specifications/governance-spec.md`

### 2. Agent Prompt

- Assembled from agent `PROMPTS.md`, `IDENTITY.md`, `MISSION.md`, `BEHAVIOR.md`
- Agent-specific capabilities and limitations
- OUTPUT_SCHEMA reminder

### 3. Customer Configuration

- Layer 4: sales stages, products, approval rules, escalation contacts
- Not stored in this repo; injected at deployment time

### 4. ServiceNow / CRM Data

- Retrieved per [specifications/data-spec.md](../specifications/data-spec.md)
- Only objects and fields permitted for this agent + user role
- Includes freshness metadata for confidence scoring

### 5. Knowledge Retrieval

- RAG results from product docs, playbooks, policies
- `shared/SALES_PLAYBOOK.md` and customer KB
- Never overrides CRM field values (source-of-truth rules)

### 6. User Behavior Signals

- Recent actions, preferred detail level, role patterns
- Source: `platform/user-behavior.md`

### 7. Conversation History

- Short memory tier only (see MEMORY_MODEL.md)
- Truncated to `max_turns` from CONFIG.yaml

### 8. Current User Request

- Raw user message + structured intent (if parsed)

## Machine-Readable Contract

```yaml
implements: runtime-spec
context_layers:
  - id: system_prompt
    source: [runtime/GOVERNANCE.md, specifications/governance-spec.md]
    required: true
  - id: agent_prompt
    source: [agents/{id}/PROMPTS.md, IDENTITY.md, MISSION.md]
    required: true
  - id: customer_configuration
    source: layer_4_deployment
    required: true
  - id: crm_data
    source: [platform/servicenow.md, specifications/data-spec.md]
    required: conditional
  - id: knowledge_retrieval
    source: [platform/rag.md, shared/]
    required: conditional
  - id: user_behavior
    source: platform/user-behavior.md
    required: false
  - id: conversation_history
    source: memory_short
    required: true
  - id: current_request
    source: user_input
    required: true
```

## Token Budget (TBD)

Priority when truncating: current request > CRM context > agent prompt > conversation history > RAG.
