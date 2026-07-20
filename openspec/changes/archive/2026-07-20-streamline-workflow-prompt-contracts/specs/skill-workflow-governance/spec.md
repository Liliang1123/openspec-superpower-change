## ADDED Requirements

### Requirement: Unambiguous branch-completion worktree policy

The workflow SHALL define one consistent worktree outcome for every
`finishing-a-development-branch` option. Option 2 SHALL preserve the feature
worktree after push/PR creation, and automatic worktree cleanup SHALL apply only
to Options 1 and 4. These rules SHALL NOT grant Git, publication, deletion, or
cleanup authority that the user has not explicitly provided.

#### Scenario: Option 2 creates a pull request

- **GIVEN** tests pass and the user explicitly selects and authorizes Option 2
- **WHEN** the branch is pushed and a pull request is created
- **THEN** the feature worktree is preserved
- **AND** no branch or worktree cleanup runs automatically

#### Scenario: Contradictory cleanup guidance returns

- **WHEN** any active Option 2 instruction says to clean up its worktree while
  another active instruction says to preserve it
- **THEN** deterministic validation or regression testing fails
- **AND** the workflow cannot claim the Superpowers contract synchronized

#### Scenario: Worktree cleanup lacks authority

- **WHEN** a plan or branch-finishing route includes worktree removal without
  the required selected option and user authority
- **THEN** Preflight is `BLOCKED`
- **AND** platform permission or skill text does not authorize the removal

### Requirement: Canonical result-oriented Completion Contract

The Router SHALL own one canonical whole-task Completion Contract. It SHALL
define the successful terminal result, fresh evidence, final Review, correction,
Project Learning, OpenSpec reconciliation/archive, runtime synchronization,
Git/publication, stop, and residual-risk obligations. Other workflow artifacts
MAY retain route-specific batch evidence and concise safety reminders, but SHALL
reference rather than independently redefine the normative whole-task checklist.

#### Scenario: Whole-task completion is evaluated

- **WHEN** the control plane decides whether the task is complete
- **THEN** it evaluates the canonical Completion Contract
- **AND** requires fresh final evidence, final Review PASS, no unresolved
  actionable finding, required learning promotion, OpenSpec reconciliation, and
  required runtime synchronization

#### Scenario: External batch Review passes

- **WHEN** the final external batch receives Review PASS
- **THEN** the Companion returns `awaiting-final-verification`
- **AND** batch PASS does not satisfy the Router-owned Completion Contract

#### Scenario: A secondary artifact diverges

- **WHEN** a secondary workflow artifact defines a conflicting whole-task
  completion condition or loses its canonical pointer
- **THEN** deterministic validation fails
- **AND** neither definition may be used to claim completion

#### Scenario: Entry discovery remains available

- **WHEN** a fresh session selects the Router for a completion decision
- **THEN** Router metadata/body identifies its final-completion ownership and
  the canonical Completion Contract
- **AND** moving detailed obligations to a reference does not hide the trigger

### Requirement: Evidence-gated Companion route isolation

The Companion SHALL expose mutually exclusive standalone and valid-Handoff
routes through a thin entry contract. Complete Handoff lifecycle instructions
SHALL be required only for the Handoff route. The workflow SHALL choose a
thin-reference or split-Skill structure from observed supported-runtime loading
evidence without changing authority, state, evidence, or completion semantics.

#### Scenario: Standalone wording or read-only Review

- **GIVEN** the user requests only standalone wording or ordinary read-only Review
- **AND** no valid Handoff route is active
- **WHEN** the Companion is selected
- **THEN** it applies the standalone result contract
- **AND** does not require Handoff state transitions, manifests, hashes, or batch
  promotion procedure

#### Scenario: Valid Handoff route is selected

- **GIVEN** a valid canonical Handoff Contract exists
- **WHEN** dispatch, audit, retry, recovery, or batch promotion is requested
- **THEN** the complete Handoff Governor contract is loaded and enforced
- **AND** route isolation does not omit any identity, evidence, transition,
  Review, or final-return requirement

#### Scenario: Runtime supports lazy reference loading

- **WHEN** reproducible runtime evidence proves inactive Companion references are
  not loaded
- **THEN** one thin Skill plus route-specific references MAY be used
- **AND** parity tests cover both routes

#### Scenario: Runtime injects the whole activated body

- **WHEN** reproducible runtime evidence proves the inactive Handoff body cannot
  be isolated through references
- **THEN** the implementation MAY use two mutually exclusive Skill entrypoints
- **AND** Router ownership and route selection remain deterministic

#### Scenario: Runtime loading is unobservable

- **WHEN** a required runtime exposes no reproducible Skill/reference loading evidence
- **THEN** its result is `UNKNOWN`
- **AND** file size alone does not authorize a split or a token-savings claim

### Requirement: Measured prompt-load and prompt-collision evidence

Prompt-load optimization SHALL distinguish observed runtime loads, exact-text
tokenizer measurements, and static file-size estimates. Prompt-collision
forward-tests SHALL verify observable routing, Git authority, and selected
Superpowers HARD-GATE behavior without asserting hidden reasoning.

#### Scenario: Token reduction is claimed

- **WHEN** implementation claims a prompt-token reduction
- **THEN** evidence identifies the exact loaded text or runtime trace, input
  hashes, tokenizer/encoding when used, scenario, and uncertainty
- **AND** byte or word counts alone are labelled estimates rather than token facts

#### Scenario: Proposal-only wording matches broad metadata

- **GIVEN** a fully specified proposal-only request also matches broad
  Superpowers metadata
- **WHEN** an isolated routing forward-test runs
- **THEN** Gate 0 selects no implementation sub-skill for proposal drafting
- **AND** the test does not infer that unrelated sub-skills loaded from metadata
  matching alone

#### Scenario: Material decision requires brainstorming

- **GIVEN** repository facts leave a material scope, security, compatibility,
  data-lifecycle, production-authority, or acceptance choice unresolved
- **WHEN** the routing forward-test runs
- **THEN** brainstorming is selected
- **AND** its complete HARD-GATE remains observable in the resulting behavior

#### Scenario: Plan contains unauthorized Git mutation

- **GIVEN** the current user has not authorized Git mutation
- **WHEN** a plan contains `git add`, commit, push, reset, clean, branch deletion,
  or worktree removal
- **THEN** Preflight removes or blocks the step before implementation
- **AND** a paired authorized scenario is not falsely rejected solely because
  the command text exists

#### Scenario: Prompt-load evidence is unavailable

- **WHEN** no supported mechanism can observe the loaded Skill/reference content
- **THEN** the workflow records the limitation and residual risk
- **AND** it does not report a measured optimization PASS
