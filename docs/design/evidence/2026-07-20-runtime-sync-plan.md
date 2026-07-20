# Runtime Sync Plan Evidence

Date: 2026-07-20
Change: `streamline-workflow-prompt-contracts`
Status: generated; independent plan Review pending

## Source and trigger

- Canonical Router source: the `streamline-workflow-prompt-contracts` Router
  feature worktree.
- Canonical Companion source: the matching Companion feature worktree.
- Portable trigger: the manifest adds the Router Completion Contract and the
  Companion Handoff governor, and existing portable files changed.
- Source audit: `0 sensitive categories found` using the path-only audit mode.

## Deployment-drain inventory

- Known canonical status paths inspected: 11.
- Active `schema_version: 4` contracts: 0.
- Historical schema 1/2 and non-contract pointer files were not migrated or
  modified.
- Required installed targets: Codex, Antigravity CLI, and Grok CLI.

## Generated plan

- Path: `/private/tmp/streamline-workflow-prompt-contracts-sync-plan.json`
- Mode: `0600`
- SHA-256:
  `6e4b9b431900eb86bd5a646bc7b7fb51c2afcb6f0c8d71cd2c689458ebe97593`
- Schema: 1.
- Manifest-bound files: 39 per required target.
- Managed governance: version 4, 15 invariant IDs, canonical body SHA-256
  `3cec896a53b16c1b2782343cb08301c62e38ac71c44cb45c82daa1ca8f054ac3`.
- Existing Codex, Antigravity, and Grok managed blocks match the canonical body;
  native bytes outside those blocks are not planned source content.

The first output attempt used `/tmp`, which is a symlink on this host and was
correctly rejected by the safe-parent validator. The plan was regenerated under
the real `/private/tmp` path without weakening validation.

## Target delta

All three required targets have the same expected portable delta:

- stale Router: `SKILL.md`,
  `references/approved-implementation-workflow.md`,
  `references/response-patterns.md`,
  `references/step-evidence-gate.md`, and
  `scripts/validate_core_gates.py`;
- missing Router: `references/completion-contract.md`;
- stale Companion: `SKILL.md` and `scripts/validate_templates.py`;
- missing Companion:
  `references/handed-off-external-execution.md`.

No other manifest path differs. The plan contains source/target paths and
SHA-256 values only; it contains no credentials, sessions, logs, caches, hooks,
MCP configuration, or other CLI-native content.

## Stop and rollback boundary

No runtime apply is authorized by this artifact alone. After independent plan
Review PASS, apply one target atomically with a per-target secure backup, run
parity/validators/discovery, and stop before later targets if apply or
verification fails. A failed target must be restored and restoration verified.
