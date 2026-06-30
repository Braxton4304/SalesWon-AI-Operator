# AI Architecture

## Scope

- LLM selection and routing (Azure OpenAI, failover)
- RAG architecture and grounding strategy
- Agent orchestration (single vs. multi-agent)
- Prompt assembly (see [runtime/RUNTIME_CONTEXT.md](../../runtime/RUNTIME_CONTEXT.md))

## Key Questions

- When to spawn sub-agents vs. single-agent with tools?
- Embedding model and chunk strategy for sales knowledge?
- How does BUSINESS_REASONING influence model routing?

## Related

- [specifications/runtime-spec.md](../../specifications/runtime-spec.md)
- [platform/rag.md](../../platform/rag.md)
- [runtime/BUSINESS_REASONING.md](../../runtime/BUSINESS_REASONING.md)

## Decisions Pending

- Primary model and fallback chain
- RAG vs. CRM-only grounding boundaries
