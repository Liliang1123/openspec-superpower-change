# Engineering Invariants

## Project learning must be entry-discoverable and artifact-bound

Scope: project workflow, skill routing, completion gates, and their validators.

Invariant:

- A mandatory closeout path must be discoverable from the skill frontmatter in
  a fresh session; instructions available only after loading the skill cannot
  establish an unconditional trigger.
- Each portable governance artifact must own and validate its own responsibility
  boundary. A validator must not concatenate unrelated files in a way that lets
  required rules move into the wrong artifact while validation still passes.
- An explicit request to archive and distill a session triggers project-learning
  audit and promotion before completion. A chat summary is a reference to the
  durable result, never its only storage.
- Mechanically enforceable workflow invariants require a deterministic negative
  regression that rejects the previous wrong assumption.

Counterexample: `project-learning-closeout.md` is replaced with a placeholder
while its text is appended to a Candidate Card template, and a concatenation-
based validator still returns PASS. This is a false PASS even though every
required phrase still exists somewhere in the portable file set.

Loading pointer: agents read this file through `AGENTS.md`; executable policy
and completion order remain canonical in `SKILL.md` and
`references/project-learning-closeout.md`.

## Validation fixtures must be valid in every supported parser mode

Scope: YAML-backed workflow contracts and tests for the dependency-free parser
fallback.

Invariant: a fixture used by both PyYAML and the fallback parser must be valid
standard YAML after contract-marker/fence extraction. Run the affected test
suite once with an interpreter that provides PyYAML and once with the supported
dependency-free interpreter. A fallback-only PASS cannot prove parser parity.

Counterexample: a fenced contract closes with four backticks. The fallback
scalar parser ignores the stray backtick, while PyYAML rejects it, so validation
passes in one worktree interpreter and fails after cherry-pick in another.

Loading pointer: the dual validation requirement is declared in `AGENTS.md`;
this invariant explains why both paths are mandatory.
