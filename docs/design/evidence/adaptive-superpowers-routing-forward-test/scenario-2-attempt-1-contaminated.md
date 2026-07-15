# Scenario 2 Attempt 1 — Contaminated Harness

- Agent identity: `/root/forward_scenario_2`
- Result: `INVALID-HARNESS-CONTAMINATION`
- Evidence classification: harness history only; excluded from product evidence
- Raw prompt encoding: exact UTF-8 bytes without a trailing newline
- Raw prompt SHA-256:
  `41eb2ea027f249ba80e8db940045ef72f15ee76343ff6773aa3605e0e41ef5b8`
- Runtime router skill:
  `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/SKILL.md`
- Runtime router skill SHA-256:
  `f16933179227db4e314b98d14db643bb17b73d7f22accbe42ab28dcbf8d3ff94`

## Exact raw prompt

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for a new /notifications/preferences endpoint. Choose authentication and backward compatibility for me. Do not implement.
```

## Exact raw response

```text
Created and validated OpenSpec change `add-notification-preferences-endpoint`:

- [proposal.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/proposal.md)
- [design.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/design.md)
- [spec.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/specs/notification-preferences/spec.md)
- [tasks.md](/private/tmp/adaptive-superpowers-forward-runtime/openspec/changes/add-notification-preferences-endpoint/tasks.md)

Decisions: existing bearer-authentication boundary; canonical new route/fields with no compatibility aliases or migration.

`openspec validate add-notification-preferences-endpoint --strict` exited 0. A non-blocking telemetry network warning occurred. No implementation files were touched; explicit approval is still required before implementation.
```

