## ADDED Requirements

### Requirement: Authenticated notification-preferences submission

The service SHALL expose `POST /notifications/preferences` through its existing
bearer-authentication mechanism. The request representation SHALL use the fields
`email` and `push`, and each field SHALL have a JSON Boolean value.

#### Scenario: Authenticated request reaches the operation

- **GIVEN** a request carries bearer credentials accepted by the existing
  authentication mechanism
- **WHEN** the client sends `POST /notifications/preferences` with Boolean
  `email` and `push` fields
- **THEN** the service processes the notification-preferences operation

#### Scenario: Existing bearer authentication rejects a request

- **GIVEN** a request is not accepted by the existing bearer-authentication
  mechanism
- **WHEN** the client sends `POST /notifications/preferences`
- **THEN** the existing bearer-authentication failure behavior applies
- **AND** the notification-preferences operation does not process the request

### Requirement: Successful response echoes notification preferences

For an accepted request, the successful response SHALL contain `email` and
`push` with the same Boolean values supplied in the request.

#### Scenario: Email and push are enabled

- **WHEN** an authenticated client submits `email` as `true` and `push` as
  `true`
- **THEN** the successful response contains `email` as `true` and `push` as
  `true`

#### Scenario: Email and push differ

- **WHEN** an authenticated client submits different Boolean values for
  `email` and `push`
- **THEN** the successful response preserves each submitted value under its
  corresponding field

#### Scenario: Email and push are disabled

- **WHEN** an authenticated client submits `email` as `false` and `push` as
  `false`
- **THEN** the successful response contains `email` as `false` and `push` as
  `false`

### Requirement: Non-Boolean preference values are rejected

The service SHALL return HTTP `400` when the supplied `email` value or the
supplied `push` value is not a JSON Boolean. The service SHALL NOT coerce a
string, number, object, array, or null value into a Boolean.

#### Scenario: Email is not a Boolean

- **GIVEN** an authenticated request supplies a non-Boolean `email` value
- **WHEN** the client sends `POST /notifications/preferences`
- **THEN** the service returns HTTP `400`

#### Scenario: Push is not a Boolean

- **GIVEN** an authenticated request supplies a non-Boolean `push` value
- **WHEN** the client sends `POST /notifications/preferences`
- **THEN** the service returns HTTP `400`

#### Scenario: Both values are not Booleans

- **GIVEN** an authenticated request supplies non-Boolean values for both
  `email` and `push`
- **WHEN** the client sends `POST /notifications/preferences`
- **THEN** the service returns HTTP `400`

### Requirement: Exact route and migration scope

The change SHALL add only `POST /notifications/preferences` for this operation.
It SHALL NOT add a compatibility alias and SHALL NOT require a data or schema
migration.

#### Scenario: Route scope is reviewed

- **WHEN** the change is prepared for release
- **THEN** `POST /notifications/preferences` is the only route added for the
  notification-preferences operation
- **AND** no compatibility alias exists
- **AND** no data or schema migration is included
