# Change: Add internal readiness endpoint

## Why

Internal process supervisors need a deterministic HTTP signal that distinguishes
an initialized process from one that is still starting or has begun shutdown.
The signal must not expose operational detail or become part of the public API.

## What Changes

- Add `GET /internal/readiness` on the existing loopback-bound internal admin
  listener only.
- Return `200` with `{"status":"ready"}` after initialization completes and
  before shutdown begins; return `503` with `{"status":"not_ready"}` otherwise.
- Reject query parameters or a request body with `400`; return `405` plus
  `Allow: GET` for other methods on the internal route.
- Add `application/json` and `Cache-Control: no-store` response headers without
  dependency names, credentials, personal data, or other diagnostic detail.
- Add no persistence, migration, public-listener route, compatibility alias, or
  new authentication mechanism.

## Impact

- Affected specs: `internal-readiness`.
- Affected code: internal HTTP routing, process lifecycle readiness state,
  endpoint contract tests, and internal operator documentation.
- Compatibility: additive internal route; existing public and internal routes
  and response contracts remain unchanged.
- Risk profile: `standard`; the endpoint is read-only and non-persistent, with
  public-listener non-exposure verified as a required acceptance condition.

## Approval Status

- Change-id presented to user: `add-internal-readiness-endpoint`
- Strict validation result: PASS (`openspec validate add-internal-readiness-endpoint --strict`, exit 0; telemetry flush warning was non-blocking)
- [ ] Proposal reviewed
- [ ] This specific scoped change-id approved for implementation
