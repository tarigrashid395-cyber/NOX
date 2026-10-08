# NOX v1.0 — API Foundation

The API boundary is owned by `backend/app/api`.

Recommended production conventions:
- Version HTTP APIs under `/api/v1`.
- Validate request and response contracts with Pydantic v2.
- Authenticate every protected operation.
- Propagate request IDs for observability.
- Return machine-readable error envelopes.
- Keep provider credentials out of request payloads.

Concrete endpoints should be introduced only with their corresponding domain implementation,
schema, repository/service boundary, tests, and operational documentation.
