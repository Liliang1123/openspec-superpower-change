# Runtime Sync Results

Date: 2026-07-20
Change: `streamline-workflow-prompt-contracts`
Status: all target verification passed; final cross-target Review pending

## Bound plan

- Plan: `/private/tmp/streamline-workflow-prompt-contracts-sync-plan.json`
- Mode: `0600`
- SHA-256:
  `6e4b9b431900eb86bd5a646bc7b7fb51c2afcb6f0c8d71cd2c689458ebe97593`
- The active schema-4 inventory was repeated immediately before the first
  apply and remained empty.

## Per-target application and verification

The unchanged reviewed plan was applied sequentially. Each apply reported
`pass` with 38 backups, followed by target parity, Router and Companion quick
validation, and both Python 3.11.7/PyYAML and Python 3.14.2 dependency-free
project validators.

| Target | Apply | Parity | Router validators | Companion validators |
|---|---|---|---|---|
| Codex | PASS | PASS | PASS | PASS |
| Antigravity CLI | PASS | PASS | PASS | PASS |
| Grok CLI | PASS | PASS | PASS | PASS |

Grok discovery used a mode-`0600` `grok inspect --json` artifact. The discovery
validator returned `PASS` and consumed the artifact; it no longer exists.

`verify-all` returned PASS for `antigravity-cli`, `codex`, and `grok-cli`.

## Backup evidence and Review correction

Backups remain outside every discovery root at
`/private/tmp/streamline-workflow-prompt-contracts-sync-backup` pending final
Review and cleanup authorization. Existing portable files preserve their live
modes in backup so rollback restores both bytes and permissions. The one
sensitive global-rule backup per target is mode `0600`, as required.

| Target | `0600` sensitive rule | `0644` portable | `0755` portable |
|---|---:|---:|---:|
| Codex | 1 | 36 | 1 |
| Antigravity CLI | 1 | 36 | 1 |
| Grok CLI | 1 | 37 | 0 |

The earlier sync-plan Review stated too broadly that backup files were mode
`0600`. The implementation, executable tests, and canonical sync contract
require `0600` for sensitive rule backups while ordinary portable backups
preserve their original `0644` or `0755` mode. This is an evidence-wording
finding, not a runtime safety failure. Task 5.2 is reopened until an independent
Reviewer corrects that statement and reaffirms the plan verdict.

## Boundaries

- No Git mutation, archive, release, or cleanup was performed.
- Raw forward-test debug logs and all sync backups remain temporary.
- Runtime parity PASS is not whole-task completion.
- Task 5.4 remains open until a final independent cross-target Review verifies
  current parity, discovery, validator evidence, backup/rollback semantics, and
  the corrected Review statement.
