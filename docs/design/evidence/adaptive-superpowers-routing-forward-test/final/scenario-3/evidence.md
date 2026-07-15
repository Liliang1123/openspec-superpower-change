# Durable Forward-Test Evidence — Scenario 3

- Agent identity: `/root/forward_s3_evidence`
- Result: `PASS`
- Raw prompt encoding: exact UTF-8 bytes without a trailing newline
- Raw prompt SHA-256:
  `e4384da9d29ee51930ac5144cbb11ea888d7b6d0b37e64ea3f97810cd8996b50`
- Actual trigger chain: refreshed Gate 0 -> executable plan -> isolated worktree
  -> Preflight Review -> TDD -> real authenticated API acceptance plus unit,
  type, build, and strict OpenSpec verification -> independent High Review ->
  fix/verify/Review loop -> fresh final verification

## Exact raw prompt

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. The exact approved strict fixture is /Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences. Describe the required implementation route for that contract and stop before editing.
```

## Runtime hashes

| Runtime file | SHA-256 |
|---|---|
| `/private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md` | `bb575b3ab94b38416d9d901fc134da1467013684ef9dd4744a1ca0952a44bb23` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/SKILL.md` | `a216bc8b75913add296722bd6fe38c5586845a1406c9c36da0cbbe34cd702ab9` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review/SKILL.md` | `348edb64124cc1abac4532ce2d44d2eb88523684f2e4ad0220bd570b628f1ed9` |

## Approved strict fixture inputs

| Exact input path | SHA-256 |
|---|---|
| [`/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/proposal.md`](../../../../../../tests/fixtures/approved-strict-change/add-notification-preferences/proposal.md) | `4b4a8d0ae921b5f19f097a5676e5b9b48e0246a380f369dc83de43ba540fc1e2` |
| [`/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/design.md`](../../../../../../tests/fixtures/approved-strict-change/add-notification-preferences/design.md) | `e3e07a23d89d731fb60b79a4e9d3f2f09262441a55894c16032af517d91018e8` |
| [`/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/tasks.md`](../../../../../../tests/fixtures/approved-strict-change/add-notification-preferences/tasks.md) | `9f7588a952c59bee3bac668f156859603d06ed80a79320bcf032a1d84be2041c` |
| [`/Users/elvis/.config/superpowers/worktrees/openspec-superpower-change/feature-make-superpowers-routing-adaptive/tests/fixtures/approved-strict-change/add-notification-preferences/specs/notification-preferences/spec.md`](../../../../../../tests/fixtures/approved-strict-change/add-notification-preferences/specs/notification-preferences/spec.md) | `1907201158435985cb6bce62dc6f17a63308edab50972df5dad10f8208b147c2` |

## Durable raw response

| Evidence file | SHA-256 |
|---|---|
| [`raw-response.md`](raw-response.md) | `a4f3708bf57a1def8e4ae09b68f27b74d604d7acf75b63d0a4c379c520bd75ad` |

## Negative runtime-edit evidence

Exact command:

```sh
set -o pipefail
rg --files /private/tmp/adaptive-superpowers-forward-runtime/openspec -g 'proposal.md' -g 'design.md' -g 'tasks.md' -g 'spec.md' | sort
```

Exit semantics: the pipeline exited `1` because `rg` found no matching artifact
paths and `pipefail` propagated the no-match status. Standard output was exactly
zero bytes, confirming that the route description created no proposal, design,
spec, or tasks artifact.

| Path-only output | Byte count | SHA-256 |
|---|---:|---|
| [`artifact-inventory.txt`](artifact-inventory.txt) | `0` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## Controller finding

The response refreshed Gate 0 for the approved strict public-API contract and
retained the complete implementation discipline: executable planning,
worktree isolation, Preflight PASS, TDD, real and official verification,
independent High Review with fix loops, and fresh final verification. It stopped
before editing, as requested.
