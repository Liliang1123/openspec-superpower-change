# Design: Cross-CLI skill governance and synchronization

## Context

Codex is the user's primary development agent. Antigravity CLI and Grok CLI are
auxiliary agents used for implementation and independent Review. All three can
read Agent Skills-compatible `SKILL.md` files, but they use different runtime
roots and global-rule files:

- Codex: `~/.codex/skills/` and `~/.codex/AGENTS.md`;
- Antigravity CLI: `~/.gemini/antigravity-cli/skills/` and
  `~/.gemini/GEMINI.md`;
- Grok CLI: `~/.grok/skills/` and `~/.grok/AGENTS.md`.

The design must prevent governance drift without copying secrets or forcing
tool-specific configuration into a false byte-identical format.

## Goals / Non-Goals

### Goals

- Keep one primary owner for routing, approval, evidence, and completion.
- Make auxiliary implementation and Review roles explicit and auditable.
- Synchronize both core skills to all selected runtimes after a validated skill
  optimization.
- Validate semantic parity of shared global rules and exact parity of portable
  skill files.
- Keep the workflow lightweight for ordinary non-skill tasks.

### Non-Goals

- Make Antigravity or Grok an alternative final completion authority.
- Synchronize auth, tokens, sessions, caches, MCP credentials, models, hooks, or
  general CLI settings.
- Require both auxiliary agents for every compact change.
- Introduce a daemon, background watcher, plugin framework, or remote service.
- Force byte-identical global rule files across CLIs.

## Considered Approaches

### 1. Shared symlink tree

Point every CLI at one physical skill tree. This minimizes copying but couples
runtime availability, prevents safe CLI-specific adaptation, and makes rollback
or partial discovery failures harder to isolate. Rejected.

### 2. Manual checklist only

Document three copy commands and rely on human inspection. This is lightweight
but does not prevent drift or prove Grok/Antigravity discovery. Rejected because
the current gap is already a checklist-completion problem.

### 3. Canonical source plus allowlisted adapters (selected)

Keep the two repositories as canonical skill sources. Copy only approved
portable files into each runtime, preserve per-CLI overlays, and validate exact
or semantic parity according to file type. This adds one small validator and no
runtime dependency.

## Decisions

### 1. Codex remains the authoritative control plane

Codex owns Gate 0, OpenSpec classification and approval, plan/Brief authorization,
Handoff creation, evidence audit, correction-loop decisions, final verification,
and final completion. Auxiliary agents cannot advance canonical state or turn an
advisory `PASS` into task completion.

For a governed batch:

1. Codex assigns an auxiliary `executor` and a different
   `independent_reviewer` for standard/strict external work. When both auxiliary
   CLIs are available, the other auxiliary CLI is the reviewer; otherwise Codex
   performs the distinct Review pass.
2. The executor changes only allowed files and produces the attempt Report.
3. The independent reviewer produces findings against the Report, diff, contract,
   and evidence; it does not edit the implementation in the same review attempt.
4. Codex audits both outputs, reruns required critical checks where possible, and
   records the authoritative `PASS`, `FAIL`, or `BLOCKED` transition.
5. Every actionable finding returns to correction, verification, and Review.

`compact` work may use one auxiliary or remain inline. `standard` and `strict`
external work always separates executor and reviewer identities. If neither a
second auxiliary reviewer nor Codex Review is available, the batch is `BLOCKED`;
it is never silently downgraded. The user may explicitly reroute the work to a
new compact contract only when the risk profile genuinely qualifies as compact,
not as a waiver inside a standard/strict contract.

External Handoff schema version 4 adds immutable `executor_agent`,
`independent_reviewer_agent`, and `decision_owner` identities. Report and Review
evidence manifests bind `agent_identity` and `agent_role`. For independent Review,
the validator rejects equal executor/reviewer identities, identity/role mismatch,
or a non-`codex` decision owner. Identities use only the canonical enum `codex`,
`antigravity-cli`, or `grok-cli`; unknown names and aliases are rejected.
`independent_reviewer_agent: not-applicable` is allowed only for a declared
compact path with a non-blank reason; Codex still performs the authoritative
inline Review.

Schema 4 is enforced for newly created contracts after deployment. Before the
validator switches, Codex inventories known active schema-3 canonical statuses.
If any are active, deployment is `BLOCKED` until each finishes under the existing
v3 workflow and reaches `complete`. Schema 3 has no auditable aborted terminal
state, so an active contract cannot be bypassed through an ignore list or chat-only
abandonment. Immutable v3 contracts are never rewritten in place or silently
migrated. The no-active-v3 inventory result is retained as upgrade evidence.

### 2. Post-optimization sync is a completion gate

The gate applies only when portable runtime allowlist content or the canonical
shared governance block changes. Repository-only README, changelog, OpenSpec
archive, tests, or design-history changes do not trigger runtime synchronization.
It does not run after ordinary application changes.

```text
source change PASS
-> source tests and Review PASS
-> Codex runtime sync + validation
-> Antigravity runtime sync + validation
-> Grok runtime sync + discovery validation
-> shared global-rule semantic parity check
-> final cross-runtime Review
-> completion allowed
```

Every installed target that the user has included in the collaboration surface
is `required` by default. `not-applicable` is allowed only when the CLI is not
installed, does not support the skill, or the user explicitly excludes it; the
record includes decision owner, evidence, reason, and resume condition. It cannot
hide a failed, stale, or undiscoverable required target. Missing or failed
required targets are `BLOCKED`.

### 3. Portable allowlist and secret denylist

Portable skill content is allowlisted: `SKILL.md`, linked `references/`, required
`scripts/`, `templates/`, and declared metadata such as `agents/openai.yaml` when
the destination supports it. Repository-only files such as `.git/`, OpenSpec
history, project docs, tests, and changelog are not runtime requirements.

Never synchronize `auth*`, token files, sessions, logs, caches, model settings,
hooks, MCP credentials, history, or CLI binaries. The validator fails if a sync
manifest names a denied category. Source and destination paths must stay inside
declared roots; absolute/traversal paths, symlink escapes, and non-regular files
are rejected. Writes use a temporary regular file followed by atomic replacement.
Backups containing global rules use mode `0600`, never print file contents, and
are removed after successful verification.

### 4. Exact skill parity, semantic rule parity

Portable skill files are compared by relative path and SHA-256 against the
canonical source manifest. Global rule files are not copied byte-for-byte. The
repository stores one canonical managed block with stable invariant IDs and a
version. Each CLI rule file contains exactly one matching begin/end marker block;
only that block is replaced. Its body hash must match the canonical source, and
bytes outside the markers must remain unchanged. The block contains:

- Codex primary owner and final completion authority;
- auxiliary agents cannot self-authorize or advance canonical state;
- Plan/Preflight -> Implement -> Verify -> Review -> Fix loop;
- evidence-before-completion and no unresolved actionable findings;
- explicit Git/push permission boundaries;
- post-skill-optimization cross-runtime sync gate;
- sensitive and CLI-native configuration exclusion.

CLI-specific language, tool names, native rule precedence, and permissions stay
outside that shared block.

### 5. Verification strategy

- Unit tests assert trigger scope, role separation, allowlist/denylist behavior,
  target-state handling, and completion blocking on drift.
- Source and installed copies run existing quick validators and project
  validators.
- Antigravity validation confirms the runtime root, portable-file manifest,
  linked reference closure, and compatible quick/project validators. An optional
  non-mutating CLI prompt has a fixed timeout and may supplement but never replace
  those deterministic checks.
- Grok validation runs `grok inspect --json` and confirms both skills resolve from
  the intended user path.
- RED/GREEN forward-tests cover premature completion, auxiliary self-approval,
  missing Grok sync, stale Antigravity files, and attempted credential copying.

## Risks / Trade-offs

| Risk | Mitigation |
|---|---|
| CLI capabilities change | Keep adapters path-driven and validate discovery rather than assume it. |
| Three copies increase drift | Generate SHA-256 manifests and block completion on mismatch. |
| Independent Review becomes duplicate ceremony | Require it by risk/profile, not for every compact task. |
| Global rules become overly large | Synchronize a concise invariant block and retain native overlays. |
| Auxiliary reviewer claims authority | Codex remains the only canonical transition and completion owner. |
| Secrets leak during sync | Strict allowlist plus explicit denylist and sensitive-pattern audit. |
| Managed rules overwrite native settings | Replace only the single versioned marker block and verify all outside bytes are unchanged. |

## Rollback

Before implementation, create structured backups of both repositories and the
three affected runtime rule/skill surfaces under `/private/tmp`. On failure,
restore only allowlisted files from those backups and rerun each runtime's
validator/discovery check. After successful publication, repository commits are
the long-term rollback source and temporary backups are removed.
