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

### Requirement: Codex-primary auxiliary-agent collaboration

The workflow SHALL keep Codex as the single owner of routing, approval,
canonical state transitions, evidence acceptance, final verification, and final
completion while allowing Antigravity CLI and Grok CLI to serve as explicitly
assigned batch executors or independent reviewers.

External collaboration SHALL use schema version 4 to bind immutable
`executor_agent`, `independent_reviewer_agent`, and `decision_owner` identities;
Report and Review evidence SHALL bind the producing agent identity and role.
Canonical agent identities SHALL be exactly `codex`, `antigravity-cli`, or
`grok-cli`, and `decision_owner` SHALL be `codex`.

#### Scenario: Auxiliary implementation and Review are separated
- **GIVEN** both auxiliary CLIs are available for a standard or strict external batch
- **WHEN** one auxiliary agent implements the batch
- **THEN** the other assigned auxiliary agent SHALL independently review its diff, Report,
  contract, and evidence
- **AND** Codex audits both outputs before recording the authoritative transition

#### Scenario: Second auxiliary reviewer is unavailable
- **GIVEN** a standard or strict external batch has an auxiliary executor
- **WHEN** the other auxiliary CLI cannot Review
- **THEN** Codex performs the distinct Review pass
- **AND** the batch is `BLOCKED` if no distinct reviewer is available
- **AND** the existing standard or strict contract is not downgraded by waiver

#### Scenario: Same auxiliary agent attempts independent self-review
- **WHEN** executor and independent reviewer identities are equal, or evidence
  identity/role does not match the canonical assignment
- **THEN** validation rejects the Report or Review
- **AND** the batch does not advance

#### Scenario: Unknown identity or non-Codex decision owner
- **WHEN** a contract uses an identity outside the canonical enum or sets
  `decision_owner` to a value other than `codex`
- **THEN** validation rejects the contract
- **AND** no evidence or state transition is accepted

#### Scenario: Auxiliary reviewer claims completion
- **WHEN** an auxiliary reviewer reports `PASS` or claims the whole task complete
- **THEN** its result remains advisory evidence
- **AND** canonical state and final completion do not advance until Codex runs the
  required verification and records its own Review decision

#### Scenario: Review finding requires correction
- **WHEN** either auxiliary Review or Codex Review contains an actionable finding
- **THEN** the same scope returns to correction and verification
- **AND** a fresh Review is required before promotion or completion

#### Scenario: Active schema-3 contract exists during upgrade
- **WHEN** pre-deployment inventory finds an active schema-3 canonical status
- **THEN** schema-4 deployment is `BLOCKED` until the v3 workflow reaches its
  existing `complete` terminal state
- **AND** immutable v3 state is not rewritten or silently migrated
- **AND** an ignore list or chat-only abandonment cannot bypass the block

### Requirement: Post-optimization cross-CLI synchronization gate

The workflow SHALL, after either core workflow skill or its shared governance
rules change, synchronize every declared required runtime target and verify
source parity or discovery before claiming the global skill optimization
complete.

#### Scenario: All three runtimes are required
- **GIVEN** Codex, Antigravity CLI, and Grok CLI are declared required targets
- **WHEN** source validation and Review pass
- **THEN** both core skills are synchronized to all three runtime roots
- **AND** each target passes its compatible validator or discovery check
- **AND** final completion remains blocked until cross-runtime parity passes

#### Scenario: A target is unavailable
- **WHEN** a required runtime is missing, stale, undiscoverable, or fails validation
- **THEN** synchronization status is `BLOCKED`
- **AND** the workflow records the target, reason, owner, and resume condition
- **AND** it does not claim global skill optimization complete

#### Scenario: Target is explicitly not applicable
- **WHEN** an uninstalled, unsupported, or user-excluded target is declared
  `not-applicable` before synchronization
- **THEN** the decision includes owner, evidence, non-blank reason, and resume condition
- **AND** completion may proceed without that target only if all remaining
  required targets pass

#### Scenario: Failure is mislabeled not applicable
- **WHEN** an installed required target is stale, undiscoverable, or fails validation
- **THEN** the target remains `BLOCKED` rather than `not-applicable`
- **AND** global skill optimization cannot be called complete

#### Scenario: Repository-only documentation changes
- **WHEN** only README, changelog, tests, design history, or archived OpenSpec files change
- **THEN** no runtime synchronization is required
- **AND** the ordinary repository validation and Review rules still apply

### Requirement: Safe semantic global-rule alignment

The workflow SHALL keep one versioned, stable-ID governance invariant block
aligned across Codex, Antigravity CLI, and Grok CLI while preserving native
overlays and excluding sensitive or runtime-owned configuration from synchronization.

#### Scenario: Global rule files use different native formats
- **WHEN** the three CLIs use different filenames, precedence rules, or tool syntax
- **THEN** the shared governance invariants remain equivalent
- **AND** only a single begin/end marker block is replaced
- **AND** CLI-specific bytes outside that block remain unchanged

#### Scenario: Portable skill parity
- **WHEN** a portable skill file is synchronized
- **THEN** its relative path and SHA-256 match the canonical source manifest
- **AND** drift blocks the sync gate

#### Scenario: Sensitive category enters a sync manifest
- **WHEN** a proposed sync includes credentials, auth/token files, sessions,
  history, logs, caches, model settings, hooks, MCP secrets, or CLI binaries
- **THEN** validation rejects the manifest
- **AND** no sensitive category is copied to another runtime

#### Scenario: Unsafe source or destination path
- **WHEN** a manifest path is absolute, traverses its declared root, resolves
  through a symlink outside that root, or is not a regular file
- **THEN** validation rejects the synchronization before any target replacement
- **AND** diagnostics identify only the path/category without printing sensitive content

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
