# Durable Forward-Test Evidence — Scenario 2

- Agent identity: `/root/forward_s2_evidence`
- Result: `PASS`
- Raw prompt encoding: exact UTF-8 bytes without a trailing newline
- Raw prompt SHA-256:
  `41eb2ea027f249ba80e8db940045ef72f15ee76343ff6773aa3605e0e41ef5b8`
- Actual trigger chain: `openspec-superpower-change` -> Gate 0
  `proposal-only` -> material authentication/backward-compatibility choice ->
  `superpowers:brainstorming` HARD-GATE -> explicit acceptance required before
  artifact finalization

## Exact raw prompt

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for a new /notifications/preferences endpoint. Choose authentication and backward compatibility for me. Do not implement.
```

## Runtime hashes

| Runtime file | SHA-256 |
|---|---|
| `/private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md` | `bb575b3ab94b38416d9d901fc134da1467013684ef9dd4744a1ca0952a44bb23` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/SKILL.md` | `a216bc8b75913add296722bd6fe38c5586845a1406c9c36da0cbbe34cd702ab9` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review/SKILL.md` | `348edb64124cc1abac4532ce2d44d2eb88523684f2e4ad0220bd570b628f1ed9` |

## Durable raw transcript

The transcript preserves the agent's `MESSAGE` followed by `FINAL_ANSWER`.

| Evidence file | SHA-256 |
|---|---|
| [`raw-transcript.md`](raw-transcript.md) | `833ef35014b0aed2c4f980a0737e84f1ec5002a8eeda58621745c7e161820574` |

## Negative artifact-inventory evidence

Exact command:

```sh
set -o pipefail
rg --files /private/tmp/adaptive-superpowers-forward-runtime/openspec -g 'proposal.md' -g 'design.md' -g 'tasks.md' -g 'spec.md' | sort
```

Exit semantics: the pipeline exited `1` because `rg` found no matching artifact
paths and `pipefail` propagated that no-match status. Standard output was
exactly zero bytes; this is the expected negative result, not an execution
error.

| Path-only output | Byte count | SHA-256 |
|---|---:|---|
| [`artifact-inventory.txt`](artifact-inventory.txt) | `0` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

## Controller finding

The agent treated authentication and backward compatibility as material choices
despite the request to choose them for the user. It invoked brainstorming,
presented one recommended contract and alternatives, and required explicit
acceptance at the intact HARD-GATE. The live path inventory independently
confirms that no proposal, design, spec, or tasks artifact was finalized.
