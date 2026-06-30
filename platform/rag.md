# RAG — Knowledge Retrieval

RUNTIME_CONTEXT layer 5. Subordinate to CRM source-of-truth rules in data-spec.

## Sources

- [shared/SALES_PLAYBOOK.md](../shared/SALES_PLAYBOOK.md) and shared industry IP
- Customer knowledge base (Layer 4)
- Product documentation (Layer 4)

## Rules

1. RAG supplements — never overrides CRM field values
2. Cite KB documents in `sources` with type `kb`
3. Low RAG confidence → retrieve or ask, do not invent

## TBD

- Embedding model (Azure OpenAI ada-002 or successor)
- Vector store (Azure AI Search)
- Chunk size and overlap
- Freshness / re-index cadence

## Related

- [architecture/domains/ai-architecture](../architecture/domains/ai-architecture/README.md)
