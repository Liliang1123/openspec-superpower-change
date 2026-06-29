# Handoff Contract

The Handoff Contract is the single machine-readable state shared by
`openspec-superpower-change` and `codex-brief-antigravity-review`.

## Marker Block

Use exactly one block in `status.md`, Gate output, or the active execution
artifact:

````markdown
<!-- COOP_HANDOFF_CONTRACT_START -->
```yaml
schema_version: 1
change_id: add-example-change
mode: approved-implementation
approval_status: approved
risk_profile: standard
batch_profile: cohesive
current_batch: 1
planned_batches: 2
executor: external-agent
governor: codex-brief-antigravity-review
next_owner: codex-brief-antigravity-review
step_critical:
  - focused test command
final_critical:
  - full test matrix
business_acceptance:
  unit: required
  pipeline: optional
  api: required
  real_business: required
stop_conditions:
  - scope expansion
  - contract ambiguity
verification_strategy:
  step: run step_critical for each batch; review reruns critical plus one independent check
  final: run final_critical once on the final batch
readonly_fields:
  - mode
  - approval_status
  - risk_profile
```
<!-- COOP_HANDOFF_CONTRACT_END -->
````

## Schema

Required fields: `schema_version`, `change_id`, `mode`, `approval_status`,
`risk_profile`, `batch_profile`, `current_batch`, `planned_batches`,
`executor`, `governor`, `next_owner`, `step_critical`, `final_critical`,
`business_acceptance`, `stop_conditions`, and `verification_strategy`.

Allowed profiles:

- `risk_profile`: `compact`, `standard`, `strict`.
- `batch_profile`: `single`, `cohesive`, `staged`.

Rules:

- The block must appear exactly once.
- `current_batch` must be between `1` and `planned_batches`.
- `business_acceptance` must define `unit`, `pipeline`, `api`, and
  `real_business` as `required`, `optional`, or `not-applicable`.
- `standard` and `strict` work require non-empty `step_critical` and
  `final_critical` lists.
- `codex-brief-antigravity-review` must not overwrite `mode`,
  `approval_status`, or `risk_profile`.
- Missing, contradictory, stale, duplicated, or unparsable contracts are
  `BLOCKED` and must return to `openspec-superpower-change` or the user.

## Ownership

`openspec-superpower-change` creates the contract and owns final verification.
`codex-brief-antigravity-review` consumes it for Brief, Report, Review, and
batch promotion. The governor may advance `current_batch` and `next_owner`
only after `PASS`; it may not re-decide OpenSpec approval or risk profile.
