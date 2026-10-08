# NOX v1.0 — Autonomous Execution

Execution is organized around:
- Tasks
- Missions
- Workspaces
- Artifacts

Task lifecycle should be explicit and durable, with cancellation, retries, recovery,
timeouts, idempotency, and auditability.

Long-running missions must persist state independently from the request lifecycle.
