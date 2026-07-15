# Change: Make Superpowers routing adaptive

## Why

The two-skill workflow already avoids duplicate OpenSpec/Superpowers design
artifacts and keeps standalone Brief review lightweight. A remaining mismatch
is that generic creation/modification wording can still activate broad
Superpowers discovery before a proposal-only task has been classified by phase,
material ambiguity, and implementation risk. On strong models this produces
avoidable question-by-question ceremony, but disabling Superpowers globally
would also remove valuable implementation safeguards.

The workflow needs a model-independent activation rule: OpenSpec approval and
completion evidence remain mandatory, while individual Superpowers sub-skills
load only when the current phase and unresolved decisions require them.

## What Changes

- Add a phase-aware Superpowers activation rule. Generic create/modify wording
  alone does not activate brainstorming, planning, TDD, or implementation Review.
- Add a shared cross-CLI precedence invariant so governed work enters the change
  gate's phase classification before broad Superpowers metadata is evaluated.
- Add a proposal-only fast path: inspect repository facts, record safe bounded
  assumptions, draft and strictly validate OpenSpec artifacts, then stop for the
  existing change-id approval.
- Define material ambiguity that still requires brainstorming and preserve the
  brainstorming HARD-GATE once that sub-skill is selected.
- Keep approved multi-slice, strict, and external implementation on the current
  plan/TDD/Preflight/Review/verification workflow.
- Make standalone `codex-brief-antigravity-review` explicitly request-scoped,
  findings-first, and non-automatic after change generation; keep its valid-
  Handoff path unchanged.
- Add two-repository regression tests and isolated forward-tests for lean and
  full routes, then synchronize every declared required runtime target.

## Impact

- Affected specs: `skill-workflow-governance`.
- Affected projects: `openspec-superpower-change`,
  `codex-brief-antigravity-review`, and their declared runtime copies.
- Affected source: router and companion `SKILL.md`, proposal/request/Superpowers
  references, the shared managed governance block, portable manifest and sync
  validator, routing tests, OpenSpec examples, and public README guidance.
- Compatibility: existing approval, evidence, Handoff schema, lifecycle,
  completion, Git authority, and cross-CLI rules remain unchanged.
- Risk: `standard` Major Self-Evolution because trigger and Superpowers boundary
  behavior changes. The primary failure mode is under-triggering discovery for a
  material API/security/compatibility decision.

## Approval Status

- Change-id presented to user: `make-superpowers-routing-adaptive`
- Strict validation result: PASS (`openspec validate make-superpowers-routing-adaptive --strict`, exit 0; telemetry flush warning was non-blocking)
- [x] Proposal reviewed
- [x] This specific scoped change-id approved for implementation
- Approval record: user replied `批准` on 2026-07-15 immediately after the exact change-id and scoped proposal were presented; provenance is `ai-proposed/user-approved`.
