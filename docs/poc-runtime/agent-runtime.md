# Agent Runtime

Implements: [ADR-007](../../architecture/DECISIONS.md), [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md)

## Core rule

```text
LLM plans.
Backend validates.
Connector executes.
User confirms writes.
```

## Flow

```text
User message
  → PromptCompiler (agent files + policies + mapping + session)
  → LLMProvider.plan() → ActionPlan JSON
  → PlanValidator (policy, authority, intent)
  → PlanExecutor (scope + connector + confirmation)
  → LLMProvider.generate_response() → governed narrative
  → AuditLogger
```

## ActionPlan

Defined in `app/planning/schema.py`. The LLM outputs this JSON; it never calls the connector directly.

Key fields: `primary_agent`, `intent`, `object_type`, `filters`, `proposed_patch`, `missing_fields`, `requires_confirmation`, `clarifying_question`, `confidence`.

## Agent manifest

[`apps/poc-runtime/backend/config/poc_agent_manifest.yaml`](../../apps/poc-runtime/backend/config/poc_agent_manifest.yaml) lists which agent markdown files to load:

- sales-rep, follow-up, account-research, customer-service

Files are read from repo [`agents/`](../../agents/) at runtime — not copied into `/apps`.

## LLM providers

| Provider | When |
|----------|------|
| `AzureOpenAIProvider` | Default when `LLM_PROVIDER=azure_openai` and creds set |
| `RuleBasedLLMProvider` | Fallback for offline dev/CI |

## Modules

| Module | Purpose |
|--------|---------|
| `app/agent/` | Load agent markdown from manifest |
| `app/runtime/prompt_compiler.py` | Assemble governed prompt |
| `app/planning/schema.py` | ActionPlan contract |
| `app/planning/validator.py` | Policy validation |
| `app/planning/executor.py` | Connector execution |
| `app/planning/mapping_loader.py` | ServiceNow mapping config |
