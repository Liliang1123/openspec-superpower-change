## ADDED Requirements

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
