# skill-workflow-governance Specification

## Purpose
Define deterministic ownership, approval, evidence, review, correction, and
completion rules for the `openspec-superpower-change` and
`codex-brief-antigravity-review` skill pair.
## Requirements
### Requirement: Deterministic skill routing
The skill pair SHALL route state-changing development work through `openspec-superpower-change` and SHALL reserve standalone `codex-brief-antigravity-review` use for prompt/brief/checklist generation and read-only artifact review.

#### Scenario: Standalone task prompt
- **GIVEN** no implementation or file modification is requested
- **WHEN** the user asks for an Antigravity task prompt
- **THEN** `codex-brief-antigravity-review` uses its standalone lightweight path
- **AND** no OpenSpec proposal or Handoff Contract is required

#### Scenario: Review and fix
- **WHEN** the user asks to review and then change implementation files
- **THEN** the request enters `openspec-superpower-change`
- **AND** it is not treated as standalone review

#### Scenario: Handed-off external batch
- **GIVEN** a valid canonical Handoff Contract exists
- **WHEN** an external batch is dispatched, reviewed, or resumed
- **THEN** `codex-brief-antigravity-review` governs that batch
- **AND** it does not re-decide OpenSpec approval or risk

### Requirement: Non-duplicated OpenSpec and Superpowers ownership
The workflow SHALL use OpenSpec for the approved change contract and Superpowers for post-approval implementation discipline without requiring duplicate design approvals for the same decision.

#### Scenario: OpenSpec-backed implementation
- **GIVEN** a proposal design and acceptance contract are approved
- **WHEN** implementation planning begins
- **THEN** `superpowers:writing-plans` creates the executable implementation plan
- **AND** OpenSpec `tasks.md` remains a contract checklist rather than a replacement plan

#### Scenario: Lightweight direct change
- **GIVEN** the change is non-behavioral or restores already-defined behavior
- **WHEN** the compact path is selected
- **THEN** no OpenSpec proposal, Handoff Contract, or large implementation plan is required by default

### Requirement: Mandatory review correction loop
Every implementation path SHALL complete verification and review before completion, and every blocking finding SHALL restart correction, verification, and review.

#### Scenario: Review fails
- **WHEN** a review result is `FAIL`
- **THEN** the same batch enters `needs-fix`
- **AND** a new attempt produces non-overwriting Report and Review artifacts
- **AND** the next batch cannot start

#### Scenario: Review is blocked
- **WHEN** required evidence or a dependency is unavailable
- **THEN** the workflow records blocker ownership and a resume condition
- **AND** resumes the same batch without reusing stale evidence after the condition is met

#### Scenario: Final external batch passes
- **WHEN** the final external batch review is `PASS`
- **THEN** lifecycle becomes `awaiting-final-verification`
- **AND** ownership returns to `openspec-superpower-change`
- **AND** the task is not complete until final verification and review pass

### Requirement: Canonical auditable handoff state
Handoff-backed external execution SHALL use exactly one machine-readable state block in `docs/agent-collab/<change-id>/status.md` and SHALL preserve attempt history.

#### Scenario: Competing state copy
- **WHEN** a Brief or Report embeds a second mutable marker block
- **THEN** review is `BLOCKED`
- **AND** the canonical `status.md` remains authoritative

#### Scenario: Complete state
- **WHEN** lifecycle is `complete`
- **THEN** `final_verification` is `pass`
- **AND** `final_review_result` is `pass`
- **AND** `last_review_result` is `pass`
- **AND** the next owner is the user

### Requirement: Executable validation without optional YAML dependency
Project validators SHALL correctly parse their supported YAML subset without PyYAML and SHALL test invalid lifecycle transitions.

#### Scenario: Boolean metadata without PyYAML
- **GIVEN** PyYAML is unavailable
- **WHEN** `allow_implicit_invocation: true` is parsed
- **THEN** the fallback parser returns a boolean true
- **AND** validation succeeds

#### Scenario: Invalid completion transition
- **WHEN** a contract claims lifecycle `complete` without final verification and review passing
- **THEN** both validators reject the contract
