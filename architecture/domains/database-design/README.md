# Database Design

## Scope

- Azure SQL schema for audit, memory, feedback, metrics
- Alignment with ServiceNow as CRM source of truth
- Tenant isolation and RLS design

## Key Questions

- What lives in Azure SQL vs. ServiceNow only?
- Long memory retention and GDPR deletion?
- Audit log immutability pattern?

## Related

- [specifications/data-spec.md](../../specifications/data-spec.md)
- [runtime/MEMORY_MODEL.md](../../runtime/MEMORY_MODEL.md)
- [platform/database.md](../../platform/database.md)

## Decisions Pending

- Schema namespaces (audit, memory, feedback, config)
- Retention policies per table
