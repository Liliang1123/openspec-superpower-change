# Cross-CLI Skill Synchronization

Use this reference after a validated change to portable runtime content in
`openspec-superpower-change`, `codex-brief-antigravity-review`, or the shared
global governance block.

## Authority and roles

- Codex owns routing, approval, canonical state, evidence acceptance, final
  verification, and completion.
- Antigravity CLI and Grok CLI may act as assigned executor or independent
  reviewer. Their result is advisory until Codex validates it.
- Standard/strict external work uses different executor and reviewer identities.
  If the second auxiliary CLI is unavailable, Codex performs the distinct Review;
  if no distinct reviewer is available, the batch is `BLOCKED`.

## Trigger boundary

Run this gate when a path declared in
`references/cross-cli-portable-manifest.json` or the managed body in
`references/shared-global-governance.md` changes. A README, changelog, test,
design-history, or archived OpenSpec-only change does not trigger runtime sync.

## Runtime surfaces

Defaults may be overridden by environment variables, but all resolved paths must
remain inside their declared roots:

| Target | Skill root | Global rule file |
|---|---|---|
| Codex | `${CODEX_HOME:-$HOME/.codex}/skills` | `${CODEX_HOME:-$HOME/.codex}/AGENTS.md` |
| Antigravity CLI | `${ANTIGRAVITY_CLI_HOME:-$HOME/.gemini/antigravity-cli}/skills` | `$HOME/.gemini/GEMINI.md` |
| Grok CLI | `${GROK_HOME:-$HOME/.grok}/skills` | `${GROK_HOME:-$HOME/.grok}/AGENTS.md` |

Installed targets selected by the user are `required`. `not-applicable` is valid
only for an uninstalled, unsupported, or explicitly excluded target and requires
Codex owner, evidence, reason, and resume condition. Failure, staleness, or
discovery failure is `BLOCKED`, never `not-applicable`.

## Managed global rule block

`references/shared-global-governance.md` is the canonical managed body. Each
global rule file contains exactly one matching versioned begin/end marker block.
Only bytes inside that block may change; native CLI rules outside it must remain
byte-identical. Parity requires all stable `CCG-*` invariant IDs and the canonical
body SHA-256.

## Safe sequence

```text
validated source + Review PASS
-> generate path/hash-only sync plan
-> Review plan and target snapshots
-> apply one target atomically
-> validate target manifest, managed block, skill validators, and discovery
-> repeat next target
-> verify all required targets
-> final Review
```

Failure restores the current target from its secure backup, verifies restoration,
and stops before later targets. Rule backups are mode `0600`, remain outside any
skill discovery root, never have their contents logged, and are removed after
successful closeout.

## Portable and forbidden content

Only manifest-declared `SKILL.md`, linked `references/`, required `scripts/`,
`templates/`, and supported metadata are portable. Reject absolute/traversal or
URL paths, backslashes, symlink escapes, and non-regular files.

Never synchronize credentials, auth/token files, sessions, history, logs,
caches, model/settings files, hooks, MCP secrets, CLI binaries, or `.env`/private
key material. Diagnostics report only path and category, never matching values.

## Verification

- All targets: portable path/SHA-256 parity, managed-block parity, quick validator,
  and repository-specific validator.
- Antigravity CLI: deterministic root, linked-file closure, and validators;
  an optional non-mutating prompt cannot replace these checks.
- Grok CLI: deterministic checks plus `grok inspect --json` path verification.
  Inspect output is mode `0600`, read only for required skill paths, not echoed,
  and removed after verification.

Do not claim global skill optimization complete until every required target and
the final Codex Review pass.
