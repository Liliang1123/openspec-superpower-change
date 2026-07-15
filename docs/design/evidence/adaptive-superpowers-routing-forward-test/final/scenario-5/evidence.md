# Durable Forward-Test Evidence — Scenario 5

- Agent identity: `/root/forward_s5_evidence`
- Result: `PASS`
- Raw prompt encoding: exact UTF-8 bytes without a trailing newline
- Raw prompt SHA-256:
  `5f00a02ef6759ae1218e18e1a92f7cf42b6a158f04095c5c525ab0166886c134`
- Actual trigger chain: `openspec-superpower-change` -> Gate 0
  `proposal-only` -> no Superpowers sub-skill -> four OpenSpec artifacts ->
  strict OpenSpec validation -> skill quick validation -> core-gate validation
  -> all 117 unit tests -> exact change-id approval stop
- Actual generated change root:
  `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/openspec/changes/add-internal-readiness-endpoint/`

## Exact raw prompt

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create and strictly validate proposal/spec/design/tasks for a fully specified internal endpoint, then stop for approval. Do not review the generated change with another skill.
```

## Pre-dispatch runtime hashes

| Runtime file | SHA-256 |
|---|---|
| `/private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md` | `bb575b3ab94b38416d9d901fc134da1467013684ef9dd4744a1ca0952a44bb23` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/SKILL.md` | `a216bc8b75913add296722bd6fe38c5586845a1406c9c36da0cbbe34cd702ab9` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review/SKILL.md` | `348edb64124cc1abac4532ce2d44d2eb88523684f2e4ad0220bd570b628f1ed9` |

## Durable raw response

| Evidence file | SHA-256 |
|---|---|
| [`raw-response.md`](raw-response.md) | `61145148796f95404d402ff421771220976e4d70e854c9434bd30f31c7a73957` |

The response explicitly states: `No implementation or separate review skill
was invoked.` It also stops for explicit approval of
`add-internal-readiness-endpoint`.

## Durable artifact snapshots

Each snapshot hash was verified byte-for-byte against the corresponding live
skill-local artifact before any runtime refresh or reset.

| Snapshot | SHA-256 |
|---|---|
| [`artifacts/proposal.md`](artifacts/proposal.md) | `4e8f656da14e921610930aafab5c9698613999dbbff1f0ae19c0b7033fc3d4d7` |
| [`artifacts/design.md`](artifacts/design.md) | `bda5152a05e8d4a95207926c6248e44f6c1d6a1177ee99a99a21110ee4adbd83` |
| [`artifacts/tasks.md`](artifacts/tasks.md) | `2f5dc12bc12aef0eb9e7045efd843896f089b8baa2f8b05e7af25c13d9a8e2e4` |
| [`artifacts/specs/internal-readiness/spec.md`](artifacts/specs/internal-readiness/spec.md) | `dac25d4c6baf9ce92551e26a7d4314aa9cf3d9a7d46c2071f8e138184e371a8f` |

## Artifact-root inventories

The runtime-root OpenSpec inventory used:

```sh
set -o pipefail
rg --files /private/tmp/adaptive-superpowers-forward-runtime/openspec -g 'proposal.md' -g 'design.md' -g 'tasks.md' -g 'spec.md' | sort
```

It exited `1` because `rg` found no matching paths and `pipefail` propagated
the no-match status. Standard output was exactly zero bytes.

| Runtime-root path output | Byte count | SHA-256 |
|---|---:|---|
| [`runtime-root-inventory.txt`](runtime-root-inventory.txt) | `0` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The actual skill-local generated root inventory used:

```sh
rg --files /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/openspec/changes/add-internal-readiness-endpoint | sort
```

It exited `0` and emitted exactly four paths: proposal, design, tasks, and the
`internal-readiness` spec. The exact path-only output is durable below.

| Skill-local path output | Line count | SHA-256 |
|---|---:|---|
| [`skill-local-inventory.txt`](skill-local-inventory.txt) | `4` | `f7f9848016bc2951b03a8e48b792fab1c458d09948223a22c0f7f2f5db5638fb` |

## Controller finding

The fully specified internal endpoint stayed on the router's proposal-only
path, generated exactly four skill-local OpenSpec artifacts, completed all
reported validation layers, and stopped for approval. The runtime root remained
empty, and neither implementation nor the separate Review skill was invoked.
