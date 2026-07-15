# Change: Add notification preferences endpoint fixture

## Why
Exercise approved strict implementation routing with a concrete public API contract.

## What Changes
- Add `POST /notifications/preferences` under existing bearer authentication.
- Accept and return boolean `email` and `push`; reject non-booleans with 400.
- Add no migration and no compatibility alias.

## Impact
- Fixture risk profile: `strict` public API/schema behavior.
- Fixture scope: routing forward-test only; no production authorization.

## Approval Status
- Change-id: `add-notification-preferences`
- [x] Strict fixture contract approved for routing forward-test
