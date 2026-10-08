# NOX v1.0 — Agent Architecture

## Core agents
- Supervisor: coordinates execution and delegates work.
- Planner: converts objectives into explicit execution plans.
- Reviewer: evaluates outputs and determines whether revision is required.

## Workforce
Specialist agents belong under `backend/app/workforce` and must expose explicit capabilities,
cost/complexity metadata, safety constraints, and observable execution outcomes.

## Production rule
An agent is not considered production-ready until routing, permissions, failure handling,
observability, persistence, and tests are implemented together.
