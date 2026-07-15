## ADDED Requirements

### Requirement: Internal-only readiness route

The service SHALL register `/internal/readiness` only on its existing
loopback-bound internal admin listener. It SHALL accept `GET` and SHALL NOT
register the route on the public listener.

#### Scenario: Internal GET reaches the endpoint

- **WHEN** a caller sends `GET /internal/readiness` through the internal admin listener
- **THEN** the service evaluates and returns the current process readiness state

#### Scenario: Public listener does not expose the route

- **WHEN** a caller sends `GET /internal/readiness` through the public listener
- **THEN** the service returns its ordinary HTTP `404` response
- **AND** the response does not reveal that an internal route exists

#### Scenario: Unsupported method

- **WHEN** a caller uses any method other than `GET` on the internal route
- **THEN** the endpoint returns HTTP `405`
- **AND** the `Allow` response header is exactly `GET`
- **AND** the JSON body is `{"error":{"code":"METHOD_NOT_ALLOWED"}}`

### Requirement: Exact request shape

The endpoint SHALL accept no query parameters and no request body.

#### Scenario: Empty GET request

- **WHEN** an internal caller sends `GET /internal/readiness` without query parameters or a body
- **THEN** the request is valid

#### Scenario: Query parameter is present

- **WHEN** an internal caller sends any query parameter
- **THEN** the endpoint returns HTTP `400`
- **AND** the JSON body is `{"error":{"code":"INVALID_REQUEST"}}`

#### Scenario: Request body is present

- **WHEN** an internal caller sends a request body, including an empty JSON object
- **THEN** the endpoint returns HTTP `400`
- **AND** the JSON body is `{"error":{"code":"INVALID_REQUEST"}}`

### Requirement: Lifecycle-derived readiness

The endpoint SHALL report `ready` exactly when process initialization has
completed successfully and shutdown has not begun. It SHALL report `not_ready`
before initialization succeeds, after initialization fails, and from the moment
shutdown begins.

#### Scenario: Initialization completed

- **GIVEN** process initialization completed successfully
- **AND** shutdown has not begun
- **WHEN** a valid readiness request is received
- **THEN** the endpoint returns HTTP `200`
- **AND** the JSON body is exactly `{"status":"ready"}`

#### Scenario: Initialization is incomplete

- **GIVEN** process initialization has not completed successfully
- **WHEN** a valid readiness request is received
- **THEN** the endpoint returns HTTP `503`
- **AND** the JSON body is exactly `{"status":"not_ready"}`

#### Scenario: Initialization failed

- **GIVEN** process initialization failed
- **WHEN** a valid readiness request is received
- **THEN** the endpoint returns HTTP `503`
- **AND** the JSON body is exactly `{"status":"not_ready"}`

#### Scenario: Shutdown began

- **GIVEN** shutdown has begun
- **WHEN** a valid readiness request is received
- **THEN** the endpoint returns HTTP `503`
- **AND** the JSON body is exactly `{"status":"not_ready"}`

### Requirement: Stable safe response contract

Every response from the internal endpoint SHALL use
`Content-Type: application/json` and `Cache-Control: no-store`. Responses SHALL
contain only the fields specified by this contract and SHALL NOT contain
dependency names, configuration values, credentials, personal data, stack
traces, or other diagnostic detail. Calling the endpoint SHALL NOT mutate
process state or persisted data and SHALL NOT perform external I/O.

#### Scenario: Successful response headers and fields

- **WHEN** the endpoint returns HTTP `200`
- **THEN** `Content-Type` is `application/json`
- **AND** `Cache-Control` is `no-store`
- **AND** the only response field is `status`

#### Scenario: Non-success response remains safe

- **WHEN** the endpoint returns HTTP `400`, `405`, or `503`
- **THEN** `Content-Type` is `application/json`
- **AND** `Cache-Control` is `no-store`
- **AND** the response contains no implementation or diagnostic detail

#### Scenario: Repeated probes have no side effects

- **WHEN** a caller invokes the endpoint repeatedly
- **THEN** no process lifecycle state or persisted data changes because of the calls
- **AND** no external I/O is initiated by the calls

### Requirement: Additive compatibility

The change SHALL add only `/internal/readiness`; it SHALL NOT add a compatibility
alias or modify existing public or internal route contracts.

#### Scenario: Existing routes remain unchanged

- **WHEN** the internal readiness endpoint is introduced
- **THEN** all pre-existing public and internal route paths and response schemas remain unchanged
- **AND** no alternate readiness path is registered
