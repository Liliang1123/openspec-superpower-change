# Change: Add a project learning gate

## Why

The workflow already defines Discovery First and governed learning candidates,
but their project-level lifecycle is incomplete. Domain context checks are not
explicit in the phase-aware top-level route, and a correction or independent
Review finding can fix the current bug without becoming durable knowledge that
future agents load and executable tests enforce.

The failure is observable in `qagent_service`: `CONTEXT.md` was removed from Git
and ignored by commit `0c0c5ab`; a local copy survived but stopped evolving with
the project. The user also routinely ends a completed task by asking the current
session to archive and distill its bug-fix experience. A chat-only summary does
not protect later agents from repeating the same foundational assumption.

## What Changes

- Add a conditional Domain Context Check before discovery/design routing.
  Clear tasks skip `grill-with-docs`; unclear or conflicting domain language
  uses it when installed and uses the existing Discovery First procedure as the
  cross-CLI fallback.
- Add a project-local learning-promotion threshold: two independent
  correction/Review signals for the same generalized invariant, or one
  high-severity security, integrity, data-loss, or false-PASS event.
- Add an explicit Project Learning Closeout trigger whenever the user requests
  session archive and experience distillation. It audits the task's corrections
  and Review findings and promotes every confirmed project-local key point.
- Route each promoted lesson to the correct durable layer: domain semantics to
  `CONTEXT.md`, agent-facing implementation traps to engineering-invariant
  guidance, qualifying trade-offs to ADRs, and mechanical behavior to regression
  tests or validators.
- Block final completion when required promotion or enforceable regression
  coverage is missing. Verify and Review learning artifacts before OpenSpec
  reconciliation/archive and before generating the final session summary.
- Require canonical shared context to remain non-ignored and included in the
  change inventory without treating staging, commit, or push as implicitly
  authorized.
- Add contract tests, validator coverage, a qagent-shaped sanitized fixture,
  forward-tests, public workflow documentation, and cross-CLI synchronization
  for changed portable rules.

## Impact

- Affected spec: `skill-workflow-governance`.
- Affected project: `openspec-superpower-change` and its declared Codex,
  Antigravity CLI, and Grok CLI runtime copies.
- Expected source: router `SKILL.md`, discovery/local-instruction/learning and
  closeout references, a Candidate Card template, managed governance rules,
  portable manifest/sync validation, tests, examples, README, and changelog.
- The companion Handoff schema and lifecycle do not change. External reviewer
  findings are evidence inputs; Codex remains the promotion/completion owner.
- Existing project `CONTEXT.md` files are not bulk-rewritten. Affected projects
  are checked lazily when a task touches domain language or reaches learning
  closeout. The qagent repository itself is evidence and a fixture source, not a
  modification target of this change.
- Risk: `standard` Major Self-Evolution because request routing, required
  knowledge artifacts, and final-completion blocking behavior change.

## Approval Status

- Change-id presented to user: `add-project-learning-gate`
- Strict validation result: PASS (`openspec validate add-project-learning-gate --strict --no-interactive`, exit 0)
- [x] Proposal reviewed
- [x] This specific scoped change-id approved for implementation
- Approval record: user replied `同意` on 2026-07-15 immediately after the
  exact `add-project-learning-gate` change-id, validated proposal scope, and
  required approval response were presented; provenance is
  `ai-proposed/user-approved`.
