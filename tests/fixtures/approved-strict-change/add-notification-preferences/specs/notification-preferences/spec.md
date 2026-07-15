# notification-preferences Fixture Specification

## Requirements
### Requirement: Update notification preferences
The API SHALL expose bearer-authenticated `POST /notifications/preferences`
with required boolean `email` and `push` request/response fields.

#### Scenario: Valid preferences
- **WHEN** an authenticated user posts boolean `email` and `push`
- **THEN** the response returns both values

#### Scenario: Non-boolean preference
- **WHEN** either field is not boolean
- **THEN** the endpoint returns HTTP 400
