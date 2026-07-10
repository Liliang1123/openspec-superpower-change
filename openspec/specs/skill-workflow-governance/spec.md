# skill-workflow-governance Specification

## Purpose
Define deterministic ownership, approval, evidence, review, correction, and
completion rules for the `openspec-superpower-change` and
`codex-brief-antigravity-review` skill pair.
## Requirements
### Requirement: Deterministic skill routing
The skill pair SHALL route state-changing development work, review-and-fix,
workflow/template edits, OpenSpec authorization, and final completion decisions
through `openspec-superpower-change`. It SHALL reserve standalone
`codex-brief-antigravity-review` use for non-state-changing prompt/brief/checklist
generation and ordinary read-only artifact review, plus Handoff-backed external
batch governance after a valid handoff.

#### Scenario: Ambiguous review-and-fix wording
- **WHEN** a request includes both Review language and file modification or fixing
- **THEN** `openspec-superpower-change` is the primary skill
- **AND** the request is not handled as standalone lightweight Review

#### Scenario: Final completion evidence
- **WHEN** the user asks whether the whole implementation is complete
- **THEN** `openspec-superpower-change` owns the decision
- **AND** the brief skill may provide batch evidence but cannot authorize completion

### Requirement: Non-duplicated OpenSpec and Superpowers ownership
The workflow SHALL use OpenSpec as the single approved design contract and SHALL
map applicable Superpowers discovery, planning, TDD, Review, and verification
discipline onto that contract without creating a duplicate design approval or
granting Git permission.

#### Scenario: OpenSpec-backed brainstorming
- **WHEN** brainstorming applies to an OpenSpec-required change
- **THEN** its decisions are recorded in the OpenSpec proposal/design
- **AND** the same decision does not require a second `docs/superpowers/specs/`
  artifact or approval

#### Scenario: Plan contains Git steps
- **GIVEN** the current user has not explicitly authorized Git mutation
- **WHEN** a Superpowers plan is prepared for execution
- **THEN** `git add`, `git commit`, and `git push` steps are removed or blocked
- **AND** the plan itself does not count as authorization

### Requirement: Mandatory review correction loop
Every implementation path SHALL complete a current-revision Preflight Review,
verification, and post-implementation Review before completion. Every actionable
finding SHALL restart the corresponding correction and Review loop.

#### Scenario: Preflight finding
- **WHEN** a Plan or external Brief has an executable gap, placeholder, scope
  conflict, missing command, or unauthorized Git step
- **THEN** implementation or dispatch does not start
- **AND** the artifact is revised and reviewed again

#### Scenario: Non-actionable observation
- **WHEN** Review records an observation that requires no change
- **THEN** it is explicitly classified as an accepted residual risk with an owner
  or decision
- **AND** it is not represented as an unresolved actionable finding

### Requirement: Canonical auditable handoff state
Handoff-backed external execution SHALL use schema version 3 with exactly one
canonical state block, non-empty critical checks, safe evidence references,
sequential final-gate persistence, and attempt history.

#### Scenario: Empty verification contract
- **WHEN** any external Handoff has an empty or blank `step_critical` or
  `final_critical` entry
- **THEN** both validators reject the contract

#### Scenario: Final verification passes before final Review
- **WHEN** final verification passes with non-empty evidence artifacts
- **THEN** canonical status persists that PASS while final Review remains pending
- **AND** completion is still forbidden

#### Scenario: Complete without evidence
- **WHEN** lifecycle claims `complete` without attempt Report, batch Review, final
  verification, and final Review hashed artifact references
- **THEN** both validators reject the contract

#### Scenario: Stale or mislabeled evidence
- **WHEN** an artifact manifest has the wrong role, result, batch, attempt, or
  source revision for the claimed state
- **THEN** runtime validation rejects it
- **AND** Preflight/timeout evidence cannot substitute for batch Review PASS

#### Scenario: Complete without previous canonical state
- **WHEN** runtime validation receives a `complete` snapshot without the actual
  immediately preceding canonical status
- **THEN** it rejects the completion claim
- **AND** the project still keeps exactly one canonical marker block

#### Scenario: Blank blocker or unsafe artifact
- **WHEN** blocker details are blank or an artifact path is absolute or traverses
  outside the project
- **THEN** both validators reject the contract

### Requirement: Executable validation without optional YAML dependency
Project validators SHALL enforce schema-3 semantics with and without PyYAML,
reject Python booleans as positive integers, and keep single-repository tests
independent of an absent sibling clone.

#### Scenario: Standalone repository clone
- **GIVEN** the companion repository is not checked out beside the project
- **WHEN** the default unittest suite runs
- **THEN** local workflow tests still execute and pass
- **AND** only explicit cross-repository parity checks are skipped

### Requirement: OpenSpec completion reconciliation
An OpenSpec-backed task SHALL reconcile contract tasks and repository closeout
state before it is called closed.

#### Scenario: Repository implementation is complete
- **WHEN** all implementation, verification, and Review gates pass
- **THEN** `tasks.md` is reconciled with no unexplained open task
- **AND** required design/closeout documentation is updated
- **AND** the change is archived when repository completion semantics allow it
- **AND** strict validation passes after archive

#### Scenario: Deployment or release remains
- **WHEN** repository policy requires deployment or release before archival
- **THEN** the change remains active with an explicit owner and resume condition
- **AND** the workflow does not claim the contract is closed
