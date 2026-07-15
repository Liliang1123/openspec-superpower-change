Created OpenSpec change `add-notification-preferences-endpoint` with only:

- [proposal.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/proposal.md)
- [design.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/design.md)
- [tasks.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/tasks.md)
- [spec.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/specs/notification-preferences-api/spec.md)

Contract covers the exact route, existing bearer auth, Boolean `email`/`push`, echoed response, HTTP 400 for non-Booleans, and excludes migrations and compatibility aliases. No implementation was performed; approval remains unchecked.

Validation: `openspec validate add-notification-preferences-endpoint --strict` passed with exit 0. The telemetry DNS warning was non-blocking.
