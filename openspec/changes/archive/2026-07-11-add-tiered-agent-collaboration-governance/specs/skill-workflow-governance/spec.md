## ADDED Requirements

### Requirement: Capability-profile routing and bounded authority

The workflow SHALL route agent work using stable capability profiles rather
than concrete model names and SHALL enforce each profile's decision-authority
ceiling.

#### Scenario: Low executor encounters ambiguity
- **GIVEN** a `mechanical-low` executor receives a bounded task
- **WHEN** it encounters an unexpected failure, contract ambiguity, security
  field, forbidden file, or required design decision
- **THEN** it returns `BLOCKED` to the control plane
- **AND** it does not expand scope or choose an architecture

#### Scenario: Medium executor reaches an authority boundary
- **GIVEN** a `cohesive-medium` executor implements an approved slice
- **WHEN** the work would change OpenSpec scope, risk, acceptance, production
  authority, or completion state
- **THEN** it stops and escalates to `control-plane-high`
- **AND** the existing approval is not silently broadened

#### Scenario: Model metadata changes
- **WHEN** the concrete model or vendor used for a profile changes
- **THEN** authorization and evidence identity remain unchanged
- **AND** model metadata does not grant decision authority

### Requirement: Schema-5 product, instance, and role identity

New governed external contracts SHALL use schema 5 to separate agent product,
instance, role, capability profile, and control-plane ownership.

#### Scenario: Same product uses separate instances
- **GIVEN** two Codex instances serve as executor and independent reviewer
- **WHEN** schema-5 evidence is validated
- **THEN** their `agent_instance_id` values differ and match their assigned roles
- **AND** product equality does not permit executor self-review

#### Scenario: Instance or role impersonation
- **WHEN** Report or Review evidence has the wrong product, instance, role, or
  capability profile for the canonical assignment
- **THEN** validation rejects the evidence
- **AND** canonical state does not advance

#### Scenario: Active schema-4 contract exists
- **WHEN** deployment inventory finds an active schema-4 Handoff
- **THEN** schema-5 deployment is `BLOCKED` until that contract reaches its
  existing terminal state
- **AND** the v4 contract is not rewritten, ignored, or silently migrated

### Requirement: Layered authorization and Confirmation Leases

The workflow SHALL distinguish tool/platform, scope/workflow, and
business/production authorization and SHALL reuse only a valid scope-bound
Confirmation Lease.

#### Scenario: Platform command permission already exists
- **GIVEN** the platform already permits a safe test command
- **WHEN** the same approved artifact revision and scope reruns that command
- **THEN** the workflow does not request a duplicate chat confirmation
- **AND** it still records the verification result

#### Scenario: Platform permission meets production deletion
- **GIVEN** a shell prefix can execute a deletion command
- **WHEN** the task would delete production data or perform another human-only
  business action
- **THEN** the workflow requires explicit business/production authorization
- **AND** platform permission cannot satisfy that gate

#### Scenario: Confirmation Lease remains valid
- **WHEN** read-only checks, tests, diff review, or the same finding's
  fix/verify/Review loop stay within the bound revision, scope, and risk
- **THEN** the lease is reused without repeated confirmation

#### Scenario: Confirmation Lease is invalidated
- **WHEN** scope, acceptance, risk, production impact, credentials, external
  side effects, destructive Git, evidence assumptions, or the user's decision changes
- **THEN** the lease expires
- **AND** the affected higher-level authorization is requested again

### Requirement: Decision provenance and governed learning candidates

Material decisions SHALL retain an allowed provenance value, and corrections
SHALL enter a Learning Candidate Pipeline before any global Skill evolution.

#### Scenario: User accepts an AI recommendation
- **WHEN** the control plane proposes an option and the user approves it
- **THEN** provenance is `ai-proposed/user-approved`
- **AND** it is not recorded as `user-originated`

#### Scenario: One low-risk correction occurs
- **WHEN** the user corrects task-local wording once
- **THEN** the workflow creates or updates a task-local Candidate Card
- **AND** it does not automatically modify a global Skill

#### Scenario: Global candidate meets evidence threshold
- **WHEN** an invariant has two independent reproductions or one high-severity
  security, integrity, or false-PASS event
- **THEN** the workflow may create a Self-Evolution proposal candidate
- **AND** implementation still requires explicit OpenSpec approval, TDD,
  forward-tests, Review, and runtime synchronization

#### Scenario: Decision is deferred or revoked
- **WHEN** the user defers or revokes a prior decision
- **THEN** provenance and lease status record that transition
- **AND** stale approval cannot authorize later work

### Requirement: Governed manual external execution

State-changing standard or strict work SHALL use the governed Handoff lifecycle
even when a Brief is manually copied to another CLI.

#### Scenario: User manually copies a standard Brief
- **WHEN** an external agent receives the Brief through copy/paste rather than a
  dispatch tool
- **THEN** the Brief still binds canonical status, instance, profile, allowed
  files, abort conditions, evidence, and Report path
- **AND** the work is not downgraded to standalone mode

#### Scenario: Executor reports DONE or PASS
- **WHEN** an executor claims its batch or the whole task is complete
- **THEN** the claim remains non-authoritative Report evidence
- **AND** only the control plane may record promotion or final completion after Review

### Requirement: High independent Review and claim-to-mechanism evidence

For standard and strict work, the control plane SHALL perform or consume a
distinct High Review that examines actual implementation mechanisms rather than
only replaying executor commands.

#### Scenario: Executor tests pass but a copied field is lost
- **WHEN** the executor Report says PASS and focused tests pass
- **THEN** High Review traces the copy/transform/wiring chain
- **AND** it returns `FAIL` if the actual diff loses a required field

#### Scenario: Unit tests miss an adversarial input
- **WHEN** existing tests pass but an independent bounded-input probe reproduces
  a crash or contract violation
- **THEN** High Review blocks promotion
- **AND** correction, verification, and a fresh Review are required

#### Scenario: Metadata claim lacks a mechanism
- **WHEN** a Report claims concurrency, restart, recovery, or another behavior
  based only on labels or metadata
- **THEN** Review traces the claim to the runner or production mechanism
- **AND** unsupported claims cannot pass

### Requirement: Profile-weighted workflow remains proportionate

The workflow SHALL preserve compact, standard, and strict evidence weight while
enforcing the same approval and completion invariants.

#### Scenario: Compact mechanical task
- **WHEN** a low-risk deterministic task has no open architecture, security,
  persistence, production, or public-contract decision
- **THEN** it may remain inline with focused verification and concise Review
- **AND** no unnecessary canonical lease artifact is created

#### Scenario: Strict authorization-sensitive task
- **WHEN** work affects real credentials, authorization, production, migration,
  deletion, release, rollback, or recovery
- **THEN** strict real evidence and explicit human business gates apply
- **AND** mocks or platform permissions cannot replace them
