# Design: add-notification-preferences-endpoint

## Context

The requested change is a narrow authenticated HTTP API addition. Bearer
authentication already exists and remains authoritative. The new operation has
two request fields, `email` and `push`; both use JSON Boolean values. A successful
response echoes those values, while a non-Boolean value for either field is a
client error with HTTP `400`.

The repository root contains no existing OpenSpec capability or active change
for this endpoint. This design therefore limits itself to the supplied public
contract and does not infer persistence, response-status, missing-field, or
additional-field behavior that the request did not define.

## Goals / Non-Goals

### Goals

- Define the exact `POST /notifications/preferences` API operation.
- Reuse the existing bearer-authentication boundary.
- Preserve the two Boolean values exactly in the successful response.
- Reject non-Boolean `email` or `push` values with HTTP `400`.
- Make implementation and verification work traceable to the API contract.

### Non-Goals

- Introduce or change authentication schemes, token semantics, or authorization
  policy.
- Add another endpoint path, deprecated route, or compatibility alias.
- Add a database, schema, or data migration.
- Define persistence or other request-shape behavior not supplied by this
  change, including missing or additional fields.

## Decisions

### 1. Reuse the existing bearer-authentication mechanism

- Decision: Protect the new endpoint with the service's existing bearer-auth
  middleware or equivalent boundary.
- Rationale: Authentication is an existing capability and the requested change
  does not authorize a new security mechanism.
- Alternatives considered: endpoint-specific authentication or anonymous
  access. Both are rejected because they would change the security boundary.

### 2. Validate types without coercion

- Decision: Treat `email` and `push` as JSON Booleans and return HTTP `400` if
  either supplied value is not a Boolean.
- Rationale: Direct type validation makes the contract deterministic and avoids
  accepting strings, numbers, or null as aliases for Boolean values.
- Alternatives considered: truthy/falsy coercion. Rejected because it conflicts
  with the explicit non-Boolean rejection requirement.

### 3. Echo the accepted representation

- Decision: The successful response contains `email` and `push` with the same
  Boolean values accepted from the request.
- Rationale: This is the complete response behavior requested and does not
  expose implementation-specific state.
- Alternatives considered: adding metadata, renaming fields, or returning an
  empty response. Rejected because those shapes are outside the requested
  contract.

### 4. Add one exact route with no migration

- Decision: Add only `POST /notifications/preferences`; add no alias and perform
  no data or schema migration.
- Rationale: The user explicitly excluded compatibility aliases and migration.
- Alternatives considered: a versioned or legacy alias and a migration step.
  Both are outside scope.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| Auth is accidentally bypassed on the new route | Exercise the existing bearer-auth boundary in endpoint tests and include it in High Review |
| Validator coerces strings, numbers, or null | Add negative tests for each field using representative non-Boolean JSON values |
| Response values or field names drift from the request | Assert exact `email` and `push` values in successful-response tests |
| Implementation adds an undocumented alias or migration | Review route registration and migration changes against the explicit non-goals |
| Unspecified API behavior is accidentally standardized | Keep success status, persistence, missing-field, and extra-field semantics outside this delta |

## Migration / Rollback

No data or schema migration is required. Before release, rollback consists of
removing the exact route registration and its new endpoint-specific code and
tests while leaving the existing bearer-authentication mechanism unchanged.

