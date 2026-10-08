# NOX v1.0 — Memory

Memory combines durable application state with semantic retrieval.

## Storage boundaries
- Supabase/PostgreSQL: authoritative structured state.
- Qdrant: vector index and semantic retrieval.
- Redis: transient coordination, caching, queues, and short-lived state.

## Retrieval requirements
Memory retrieval must be scoped by user, workspace, project, and permissions before
semantic results are exposed to an agent or user.
