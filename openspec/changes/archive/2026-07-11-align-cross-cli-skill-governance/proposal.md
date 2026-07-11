# Change: Align cross-CLI skill governance and synchronization

## Why

`openspec-superpower-change` and `codex-brief-antigravity-review` currently
govern Codex correctly, but their post-optimization sync checklist covers only
the open-source repositories and Codex runtime. Antigravity CLI already carries
older copies, Grok CLI does not carry the two core skills, and the three global
rule files have overlapping but drifting governance language. This makes the
auxiliary agents less predictable and can let a source change be called complete
before every intended runtime sees it.

## What Changes

- Make Codex the single primary orchestrator and final completion owner.
- Allow Antigravity CLI and Grok CLI to act as batch-scoped executors or
  independent reviewers, while keeping their output advisory until Codex audits
  the required evidence and records the authoritative decision.
- Upgrade external collaboration to schema version 4 so canonical status and
  evidence bind concrete executor/reviewer CLI identities and reject same-agent
  self-review where independent Review is required.
- Add a required post-optimization synchronization gate for the two core skills:
  validated source -> Codex runtime -> Antigravity CLI runtime -> Grok CLI
  runtime -> discovery/parity verification -> final Review.
- Define a versioned, marker-bounded shared-rule core for all three CLIs while
  preserving tool-specific overlays, permission models, paths, and native
  configuration outside the managed block.
- Add an allowlisted cross-CLI sync reference and validator/forward-tests that
  never copy credentials, sessions, auth files, model settings, or caches.
- Treat a missing required runtime, failed discovery, parity drift, or unresolved
  auxiliary Review finding as `BLOCKED`, not as a completed global skill update.

## Impact

- Affected spec: `skill-workflow-governance`.
- Affected projects: both open-source skill repositories.
- Affected runtime surfaces: Codex, Antigravity CLI, and Grok CLI personal
  skills/global rules.
- Compatibility: skill bodies remain Agent Skills-compatible; active schema-3
  contracts must finish under schema 3, and schema 4 applies only to contracts
  created after deployment; each CLI retains its native global-rule filename and
  CLI-specific overlay.
- Risk profile: `standard` Major Self-Evolution because this changes runtime
  synchronization, collaboration ownership, and completion semantics.

## Approval Record

On 2026-07-11 the user explicitly approved the exact change-id and scoped
contract with: “批准实施 align-cross-cli-skill-governance”. Any expansion beyond
this contract requires a new approval decision.
