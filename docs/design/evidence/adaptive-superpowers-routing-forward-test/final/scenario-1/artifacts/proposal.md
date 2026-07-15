# Change: Add notification preferences endpoint

## Why

Authenticated clients need a single API operation for submitting email and push
notification preferences. The service has bearer authentication already, but it
does not yet expose the requested `POST /notifications/preferences` contract.

## What Changes

- Add `POST /notifications/preferences` behind the existing bearer-authentication
  mechanism.
- Accept request fields `email` and `push`, each as a Boolean.
- Return a successful response that echoes the accepted `email` and `push`
  values.
- Return HTTP `400` when either field is not a Boolean.
- Add only the exact endpoint path; do not add a compatibility alias.
- Require no data or schema migration.

## Impact

- Affected specs: `notification-preferences-api`.
- Affected code after approval: the notification-preferences HTTP route,
  request validation, and focused endpoint tests; the existing bearer-auth
  mechanism is reused rather than changed.
- Compatibility: additive exact-path API change with no compatibility alias.
- Migration: none.
- Risks: strict evidence profile because this is a public authenticated API
  contract; implementation must not coerce non-Boolean values or weaken the
  existing auth boundary.

## Approval Status

- Change-id presented to user: `add-notification-preferences-endpoint`
- Strict validation result: PASS (`openspec validate add-notification-preferences-endpoint --strict`, exit 0; telemetry flush warning was non-blocking)
- [ ] Proposal reviewed
- [ ] This specific scoped change-id approved for implementation
