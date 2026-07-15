## ADDED Requirements

### Requirement: Conditional project context discovery

The workflow SHALL run a Domain Context Check before material-choice and
implementation routing whenever affected domain terms, actors, boundaries,
states, or lifecycle may change. It SHALL invoke `grill-with-docs` only when
repository inspection leaves domain language unclear or conflicting, and SHALL
use equivalent built-in Discovery First rules when that skill is unavailable.

#### Scenario: Clear localized task

- **GIVEN** repository context defines the affected language and boundaries
- **AND** the task introduces no new or conflicting domain concept
- **WHEN** Gate 0 classifies the request
- **THEN** the workflow records the scoped context result
- **AND** does not invoke `grill-with-docs` solely because files will change

#### Scenario: Domain language remains ambiguous

- **GIVEN** repository inspection cannot resolve a term, actor, boundary, state,
  or lifecycle meaning that affects the contract
- **WHEN** the workflow reaches the Domain Context Check
- **THEN** it invokes `grill-with-docs` when installed
- **AND** otherwise follows the complete portable Discovery First procedure
- **AND** stabilizes domain language before choosing material solution behavior

#### Scenario: Canonical context is intentionally ignored

- **GIVEN** a Git repository designates `CONTEXT.md` as shared project knowledge
- **WHEN** ignore rules exclude that file from the repository change surface
- **THEN** the context checkpoint reports a project-knowledge finding
- **AND** the ignored local copy cannot by itself satisfy durable promotion
- **AND** no staging, commit, or push occurs without separate user authorization

### Requirement: Governed project-local learning promotion

Corrections and Review findings SHALL enter a project learning audit. The
workflow SHALL require project-local promotion after two independent
correction/Review signals establish the same generalized invariant, or after one
high-severity security, integrity, data-loss, or false-PASS event establishes
it. A user request to archive and distill the session SHALL always run Project
Learning Closeout and SHALL promote every confirmed project-local key point.

#### Scenario: Repeated correction and independent Review find a foundation issue

- **GIVEN** one or more human corrections expose an agent's wrong assumption
- **AND** a distinct Review observation independently confirms the same
  foundational, easy-to-miss project invariant
- **WHEN** the Candidate Card classifies the evidence
- **THEN** the project-local promotion threshold is met
- **AND** final completion remains blocked until promotion and enforcement pass

#### Scenario: One high-severity event occurs

- **WHEN** a single correction or Review finding establishes a security,
  integrity, data-loss, or false-PASS invariant
- **THEN** project-local promotion is mandatory without waiting for recurrence
- **AND** the high-severity evidence does not automatically authorize a global
  Skill change

#### Scenario: One low-risk task-local correction occurs

- **WHEN** a single low-risk correction affects only the current task and does
  not establish a project-local invariant
- **THEN** it remains in the current Plan, Review, or session summary
- **AND** it does not force permanent project documentation or block completion

#### Scenario: User requests session archive and distillation

- **GIVEN** implementation and Review have produced correction history
- **WHEN** the user asks the current session to archive and distill its bug-fix
  experience
- **THEN** the workflow runs Project Learning Closeout before final completion
- **AND** promotes every confirmed project-local key point through the project's
  normal change path even if the automatic threshold was not reached
- **AND** a chat-only archive summary cannot substitute for repository promotion

### Requirement: Layered durable knowledge and executable enforcement

The workflow SHALL classify promoted knowledge by responsibility. It SHALL keep
domain semantics in `CONTEXT.md`, engineering or agent-operating invariants in
project guidance, qualifying hard-to-reverse trade-offs in ADRs, and
mechanically enforceable behavior in deterministic regression tests or
validators. Candidate evidence SHALL be summarized without persisting sensitive
conversation content.

#### Scenario: One lesson contains semantic and implementation knowledge

- **GIVEN** a corrected bug reveals both a project-specific semantic truth and
  an easy-to-miss implementation mechanism
- **WHEN** the lesson is promoted
- **THEN** `CONTEXT.md` receives only the term, meaning, relationship, or resolved
  ambiguity
- **AND** engineering guidance receives the generalized implementation invariant
- **AND** neither artifact duplicates the full incident chronology

#### Scenario: The invariant is mechanically enforceable

- **WHEN** a prior wrong assumption can be represented by a deterministic input,
  state transition, schema, or validator condition
- **THEN** promotion includes a regression test or validator that rejects it
- **AND** prose-only documentation cannot satisfy the completion gate

#### Scenario: Mechanical enforcement is impossible

- **WHEN** the Candidate Card demonstrates that deterministic enforcement is not
  practical
- **THEN** it records a non-empty reason and an explicit adversarial Review
  scenario
- **AND** the promotion still requires focused verification and Review PASS

### Requirement: Learning-aware completion and archive order

The workflow SHALL complete required Project Learning Closeout before fresh
final verification, final Review, OpenSpec task reconciliation/archive, and the
session archive summary. Learning artifacts added during closeout SHALL enter
the changed-file inventory and ordinary verification/Review loop.

#### Scenario: Required learning remains only in conversation

- **GIVEN** a mandatory or explicitly requested project-local promotion exists
- **WHEN** the generalized invariant remains only in chat, Report, or Review
  output
- **THEN** final completion is `BLOCKED`
- **AND** the workflow does not reconcile/archive the change as complete

#### Scenario: Learning closeout adds project artifacts

- **WHEN** Project Learning Closeout updates context, engineering guidance,
  Candidate Cards, tests, or validators
- **THEN** focused verification and Review cover those changes
- **AND** fresh final verification and final Review occur after that PASS
- **AND** the final session summary references the durable result rather than
  becoming its only storage location

#### Scenario: External reviewer identifies the candidate

- **WHEN** an external reviewer reports a potential project-local invariant
- **THEN** its finding remains an evidence input
- **AND** the Codex control plane classifies, promotes, and verifies the candidate
- **AND** the reviewer cannot self-authorize promotion or completion
