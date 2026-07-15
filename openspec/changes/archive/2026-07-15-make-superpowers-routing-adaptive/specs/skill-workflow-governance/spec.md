## ADDED Requirements

### Requirement: Phase-aware Superpowers activation

The workflow SHALL select Superpowers sub-skills from the current task phase,
unresolved material decisions, and implementation risk. Generic creation or
modification wording alone SHALL NOT activate a sub-skill.

#### Scenario: Broad skill metadata also matches

- **GIVEN** a state-changing request matches both the change gate and broad Superpowers metadata
- **WHEN** skill routing begins
- **THEN** the shared managed governance rule routes the request through change-gate phase classification first
- **AND** only the Superpowers sub-skills selected by that classification apply to the current phase
- **AND** a selected sub-skill retains its complete rules and HARD-GATE behavior

#### Scenario: Fully specified proposal-only change

- **GIVEN** the user requests only OpenSpec proposal/spec/design/tasks artifacts
- **AND** repository facts plus the request define a testable contract without a material unresolved decision
- **WHEN** Gate 0 classifies the current phase
- **THEN** it records no implementation Superpowers sub-skill for proposal drafting
- **AND** the workflow creates and strictly validates the OpenSpec artifacts
- **AND** it stops for approval of the exact change-id before implementation

#### Scenario: Material proposal ambiguity remains

- **GIVEN** repository inspection cannot resolve a choice that changes scope, security, compatibility, data lifecycle, production authority, or testable acceptance
- **WHEN** the proposal contract would otherwise choose that behavior for the user
- **THEN** the workflow invokes `superpowers:brainstorming`
- **AND** preserves its HARD-GATE after invocation
- **AND** records the accepted decision in the single OpenSpec design/spec contract

#### Scenario: Bounded proposal assumption

- **GIVEN** a missing proposal detail is reversible at approval time
- **AND** it is visible in the proposal/design
- **AND** it does not decide security, compatibility, destructive migration, data lifecycle, production authority, or testable acceptance
- **WHEN** the proposal is drafted
- **THEN** the workflow MAY record that detail as an explicit bounded assumption
- **AND** SHALL NOT invoke brainstorming solely because that assumption exists

#### Scenario: Approved implementation begins

- **GIVEN** the user has approved the exact OpenSpec change-id and scoped contract
- **WHEN** the task transitions from proposal-only to implementation
- **THEN** Gate 0 is refreshed for the implementation phase
- **AND** multi-slice, strict, or external work retains its required planning, TDD, Preflight, Review, evidence, and verification discipline

### Requirement: Model-independent workflow weight

The workflow SHALL NOT use a concrete model, vendor, or version name as a reason
to bypass or require approval, evidence, Review, verification, or a Superpowers
sub-skill. Workflow weight SHALL follow task facts and stable capability/risk
profiles.

#### Scenario: Strong model is selected

- **WHEN** a stronger or newer model executes a proposal-only or implementation task
- **THEN** phase-aware routing applies without adding ceremony solely because the model changed
- **AND** the model identity does not remove any gate required by the task's contract or risk

### Requirement: Request-scoped brief OpenSpec Review

Standalone `codex-brief-antigravity-review` SHALL run only for the current
explicit wording or read-only Review request. It SHALL default to a concise,
findings-first OpenSpec artifact Review and SHALL NOT auto-chain after change
generation.

#### Scenario: Change generated without a Review request

- **GIVEN** OpenSpec artifacts have been produced and validated
- **WHEN** the current user request does not ask for standalone Review
- **THEN** the companion skill is not invoked automatically
- **AND** no duplicate Review ceremony or Handoff artifact is created

#### Scenario: Explicit standalone OpenSpec Review

- **WHEN** the user explicitly requests a read-only Review of proposal, spec, design, and tasks
- **THEN** the companion inspects proposal scope, spec scenarios, design decisions and risks, task traceability, and cross-artifact consistency
- **AND** reports scope/evidence, actionable findings, verdict, and next action in brief form
- **AND** omits governance narration that does not change the result or next action
- **AND** creates no Handoff and makes no implementation or final-completion decision

#### Scenario: Valid Handoff exists

- **GIVEN** a valid canonical Handoff Contract exists
- **WHEN** the request dispatches, audits, retries, recovers, or promotes that external batch
- **THEN** the complete handed-off lifecycle remains in force
- **AND** standalone brevity does not remove required artifacts, evidence, or state transitions
