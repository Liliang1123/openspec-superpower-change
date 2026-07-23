## ADDED Requirements

### Requirement: Governed Caveman Lite output profile

The Router SHALL provide an opt-in `governed-caveman-lite` presentation profile
that can be activated with the canonical conversational phrase
`OpenSpec 精简模式`. The profile SHALL use concise professional full sentences,
SHALL remain active only for the current conversation until disabled with
`OpenSpec 正常模式`, and SHALL work without a separately installed Caveman
skill.

The profile SHALL NOT alter request routing, OpenSpec approval, Superpowers
selection, evidence profiles, Handoff state, Review, verification, completion,
Git authority, or publication authority. Protected governance artifacts and
safety-critical text SHALL remain structurally complete.

#### Scenario: User enables the profile with the task

- **WHEN** the user sends `OpenSpec 精简模式：<任务>`
- **THEN** the Router handles the task under its normal governance route
- **AND** ordinary chat uses concise professional full sentences
- **AND** no separate Caveman skill is required

#### Scenario: User enables the profile before the task

- **WHEN** the user sends `OpenSpec 精简模式` before a later task
- **THEN** the profile applies to later ordinary responses in the same conversation
- **AND** the mode creates no workflow state or evidence artifact

#### Scenario: User disables the profile

- **GIVEN** the profile is active
- **WHEN** the user sends `OpenSpec 正常模式`
- **THEN** later responses return to normal output style
- **AND** this latest explicit user instruction controls Router prose even if a
  Caveman-style instruction was previously active
- **AND** routing, approval, evidence, and task state remain unchanged

#### Scenario: Conversation ends

- **GIVEN** the profile is active
- **WHEN** a new conversation begins
- **THEN** the Router starts in normal output mode
- **AND** no account, repository, or runtime preference is inferred

#### Scenario: Protected governance content is produced

- **GIVEN** the profile is active
- **WHEN** the Router produces Gate 0, a mandatory governance-step or approval
  field, an OpenSpec artifact, implementation plan, Handoff contract, evidence
  artifact, state transition, final verification, final Review, critical
  command, rollback instruction, security warning, or destructive confirmation
- **THEN** every required field and ordering constraint remains present
- **AND** governance clarity and safety override output compression

#### Scenario: Default Router request omits the phrase

- **WHEN** a normal Router request does not explicitly enable the profile
- **THEN** the new profile is not forced on
- **AND** existing output behavior remains compatible
