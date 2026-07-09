# Response Patterns

## Review-only requests

1. State that no files will be changed.
2. State whether the described change would require OpenSpec if implemented.
3. Summarize unclear terms, risks, missing artifacts, approval gates, and recommendations.
4. If asked, provide an implementation-ready prompt for another agent.
5. For standalone prompt wording or ordinary diff/Report review, route to
   `codex-brief-antigravity-review` instead of creating change-gate artifacts.

## Discovery-first requests

1. State that Phase 0 discovery is needed and why.
2. Read existing glossary, ADRs, code, and relevant docs.
3. Ask one focused question at a time with a recommended answer.
4. Update glossary or propose ADRs only when decisions crystallize.
5. Continue to OpenSpec once language and boundaries are stable enough.

## OpenSpec-required implementation requests

1. State that the request requires OpenSpec.
2. Say implementation is blocked pending proposal approval.
3. Use Discovery First if language or boundaries are unclear.
4. Create or update the required OpenSpec artifacts.
5. Run strict validation.
6. Present the proposal summary and wait for user approval.
7. After approval, create the Superpowers plan before implementation.
8. Include Step Evidence Gate checkpoints in the implementation plan.
9. When the plan is saved, provide its path and ask whether to execute inline or with subagents.

## Direct change requests

1. State that OpenSpec is not required and briefly why.
2. Apply compact Step Evidence Gate before editing when the direct change is gated.
3. Use TDD or systematic debugging as applicable, then implement the scoped change.
4. Run targeted official verification.
5. For gated direct changes, report compact Step Evidence Gate results.
6. Run focused diff/self-review; findings return to fix and re-verification.
7. Report changed files, tests, Review result, and verification evidence.

## Gate 0 pattern

Use before any state-changing action:

1. Mode: state the active mode.
2. References read: list the exact references and why they are sufficient.
3. OpenSpec decision: yes/no/uncertain with one-line reason.
4. Required Superpowers: list required sub-skills or state none.
5. Risk and confirmation: state risk level, next action, and whether user confirmation is required.

For a non-behavioral micro change, combine these fields into one concise line.

## Implementation blocked by gate

1. State the blocking gate.
2. State what evidence, approval, reference, or decision is missing.
3. State the safest next action.
4. Do not modify files or run state-changing commands until the gate clears.

## Interrupted / dirty diff audit pattern

When interrupted due to process concerns:

1. Stop implementation immediately.
2. List files changed before interruption.
3. Mark each change as validated, unvalidated, or partial.
4. Recommend revert, keep, or park for each file.
5. State that no further implementation will happen until the user confirms.

## Self-evolution review draft pattern

For Major self-evolution before approval:

1. State that Self-Evolution mode is active and Major.
2. Provide or update a review draft plan, not implementation.
3. Include affected files, exact rule snippets, validation, forward-test, and rollback path.
4. Stop for review/approval before editing the skill.

## Completion pattern

1. State the final Review result and artifact or inline review evidence.
2. List fresh final verification commands and results.
3. Confirm scope, sensitive-data, temporary-file, and unrelated-change checks.
4. If any result is `FAIL` or `BLOCKED`, return to correction and do not claim
   completion.
