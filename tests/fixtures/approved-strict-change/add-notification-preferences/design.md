# Design: add-notification-preferences fixture

## Decisions
- Reuse bearer authentication and implement one POST handler.
- Request/response fields are required booleans `email` and `push`.
- Non-boolean input returns 400; no migration or compatibility alias exists.

## Risk / Rollback
Public API/schema work is strict. Rollback removes the handler, schema, tests,
and docs together; real API acceptance and independent Review are mandatory.
