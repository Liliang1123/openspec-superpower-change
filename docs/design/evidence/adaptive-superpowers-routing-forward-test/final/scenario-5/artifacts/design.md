# Design: add-internal-readiness-endpoint

## Context

The process already has a loopback-bound internal admin listener and lifecycle
signals for initialization completion and shutdown start. Supervisors need a
small readiness contract, while public clients must not be able to discover the
route. The endpoint must remain side-effect-free and reveal no dependency or
configuration detail.

## Goals / Non-Goals

### Goals

- Expose one deterministic process-readiness signal to local internal callers.
- Keep method, request validation, status codes, body schema, headers, lifecycle
  transitions, and listener exposure testable.
- Preserve the current public API, authentication, persistence, and data model.

### Non-Goals

- Report liveness, dependency-level diagnostics, build metadata, or metrics.
- Add remote administrative access or a new authentication scheme.
- Persist readiness history or change startup/shutdown behavior.
- Provide a compatibility alias or register the route on the public listener.

## Decisions

### 1. Use one internal GET route

- Decision: register `GET /internal/readiness` only on the existing
  loopback-bound admin listener. The public listener behaves as if the route
  does not exist and returns its ordinary `404` response.
- Rationale: listener separation preserves the existing internal boundary and
  avoids creating a new credential or authorization contract.
- Alternatives considered: a public authenticated route was rejected because
  it expands the public and security surface; an in-process-only API was
  rejected because external process supervisors cannot call it.

### 2. Derive readiness only from process lifecycle

- Decision: readiness is `ready` exactly after successful initialization and
  before shutdown begins. All earlier, failed-initialization, and shutdown
  states are `not_ready`.
- Rationale: this is deterministic, has no external I/O, and does not conflate
  readiness with dependency diagnostics or liveness.
- Alternatives considered: dependency-specific checks were rejected because
  their timeout, freshness, and failure semantics are outside this change.

### 3. Keep the wire contract minimal and non-cacheable

- Decision: valid responses are exactly `{"status":"ready"}` with `200` or
  `{"status":"not_ready"}` with `503`, encoded as JSON with
  `Cache-Control: no-store`. Any query parameter or body returns `400` with
  `{"error":{"code":"INVALID_REQUEST"}}`. Other methods return `405` with
  `Allow: GET` and `{"error":{"code":"METHOD_NOT_ALLOWED"}}`.
- Rationale: fixed schemas are easy to probe and do not expose internal detail.
- Alternatives considered: verbose per-check output was rejected because it can
  leak configuration and makes the contract dependent on implementation detail.

### 4. Make the change additive without aliases or stored state

- Decision: no existing route or schema changes, no compatibility alias, no
  migration, and no persistence are introduced.
- Rationale: the endpoint is new and internal, so an alias or data lifecycle
  would add behavior without a consumer requirement.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| Route is accidentally exposed on the public listener | Add a real negative public-listener probe and routing test |
| Lifecycle transitions return a stale status | Drive the response directly from initialization/shutdown state and test every transition |
| A proxy or supervisor caches readiness | Send `Cache-Control: no-store` on every response |
| Error responses reveal internal detail | Use fixed error codes and prohibit diagnostic fields |

## Migration / Rollback

No data or consumer migration is required. Rollback removes the internal route,
handler, contract tests, and operator documentation together. Lifecycle state
and all existing routes remain unchanged. If preflight inspection finds that
the assumed existing loopback admin listener or lifecycle signals do not exist,
implementation is blocked and the proposal must be revised and re-approved.

