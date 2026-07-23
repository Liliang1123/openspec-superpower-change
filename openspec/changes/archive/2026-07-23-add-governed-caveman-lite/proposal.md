# Change: Add governed Caveman Lite output mode

## Why

`openspec-superpower-change` already treats Caveman as an output-compression
layer and protects governance artifacts from over-compression. The current
contract does not define one simple built-in activation phrase, does not bind
that phrase to `lite` intensity, and relies on the separately installed
`caveman` skill for persistence and disable behavior.

A fresh-agent baseline therefore recognized the governance boundaries but
reported that `OpenSpec 精简模式` is not a defined mode. Users must remember
multiple skill names and commands, and non-Codex runtime targets cannot assume
the personal Caveman skill is installed.

## What Changes

- Add a built-in, opt-in `governed-caveman-lite` output profile.
- Define the canonical conversational form:

  ```text
  OpenSpec 精简模式：<任务>
  ```

- Define `OpenSpec 正常模式` as the canonical disable phrase.
- Treat the latest explicit OpenSpec mode command as authoritative for Router
  prose, including when another Caveman-style instruction was previously active.
- Keep the profile active only for the current conversation, until disabled or
  the conversation ends.
- Apply `lite` semantics: concise professional full sentences without filler or
  hedging; no fragment-heavy or abbreviated `full`/`ultra` style.
- Keep OpenSpec proposals, plans, Handoff contracts, evidence artifacts, state
  transitions, final verification, final Review, critical commands, security
  warnings, and destructive confirmations structurally complete and clear.
- Implement the profile inside `openspec-superpower-change` so it works without
  a separately installed `caveman` skill.
- Add deterministic contract checks, isolated forward-tests, user-facing usage
  examples, and required cross-runtime synchronization evidence.

## Non-Goals

- Do not enable Caveman output by default for every Router request.
- Do not change OpenSpec decisions, Superpowers selection, approval authority,
  evidence profiles, state transitions, Review, verification, or completion.
- Do not add `full`, `ultra`, or 文言 modes to this skill.
- Do not modify the separately installed `caveman` skill.
- Do not implicitly invoke or delegate presentation control to the separately
  installed `caveman` skill.
- Do not add host-specific slash-command registration or synchronize personal
  prompts, settings, credentials, sessions, caches, or other CLI-native state.
- Do not expand or reopen the archived
  `streamline-workflow-prompt-contracts` change.

## Impact

- Affected spec: `skill-workflow-governance`.
- Candidate source files:
  - `SKILL.md`;
  - `references/response-patterns.md`;
  - `README.md` and `README_cn.md`;
  - `scripts/validate_core_gates.py`;
  - `tests/test_workflow_rules.py`;
  - portable manifest membership checks and generated path/hash sync evidence.
- Runtime targets: every declared required Codex, Antigravity CLI, and Grok CLI
  target because the portable Router contract changes.
- Compatibility: existing prompts and default output remain valid; the new
  profile activates only after an explicit phrase.
- Risk: Major Self-Evolution because a stable public activation phrase and
  conversation-scoped mode lifecycle are added. Implementation requires
  approval of this exact change-id and scoped contract.

## Approval Status

- Strict OpenSpec validation PASS on 2026-07-23.
- Independent proposal Review PASS on 2026-07-23 after correction and re-Review.
- User explicitly approved `add-governed-caveman-lite` and the current
  proposal/design/spec/tasks scope on 2026-07-23.
- [x] This exact change-id and scoped contract are approved for implementation.
