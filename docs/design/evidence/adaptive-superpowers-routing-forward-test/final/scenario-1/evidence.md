# Durable Forward-Test Evidence — Scenario 1

- Agent identity: `/root/forward_s1_evidence`
- Result: `PASS`
- Raw prompt encoding: exact UTF-8 bytes without a trailing newline
- Raw prompt SHA-256:
  `0b2b31e6e4aa2a2663559b4ad99180cb3326d904535110ab3146e89004706c01`
- Actual trigger chain: `openspec-superpower-change` -> Gate 0
  `proposal-only` -> no Superpowers sub-skill -> four OpenSpec artifacts ->
  strict validation -> exact change-id approval stop

## Exact raw prompt

```text
Read /private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md and use the skill at /private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change. Create proposal/spec/design/tasks only for POST /notifications/preferences. Authentication is existing bearer auth; request fields are email:boolean and push:boolean; response echoes both fields; 400 rejects non-booleans; no migration or compatibility alias. Do not implement.
```

## Runtime hashes

| Runtime file | SHA-256 |
|---|---|
| `/private/tmp/adaptive-superpowers-forward-runtime/AGENTS.md` | `bb575b3ab94b38416d9d901fc134da1467013684ef9dd4744a1ca0952a44bb23` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/openspec-superpower-change/SKILL.md` | `a216bc8b75913add296722bd6fe38c5586845a1406c9c36da0cbbe34cd702ab9` |
| `/private/tmp/adaptive-superpowers-forward-runtime/skills/codex-brief-antigravity-review/SKILL.md` | `348edb64124cc1abac4532ce2d44d2eb88523684f2e4ad0220bd570b628f1ed9` |

## Durable raw response

| Evidence file | SHA-256 |
|---|---|
| [`raw-response.md`](raw-response.md) | `58a2f1744a024bf7876ba251fe1b746867b3e3fc1020825e22c07ed68c8b4170` |

## Durable artifact snapshots

Each snapshot hash was verified byte-for-byte against the corresponding live
artifact before the controller reset the isolated runtime.

| Snapshot | SHA-256 |
|---|---|
| [`artifacts/proposal.md`](artifacts/proposal.md) | `911bf2d50b836f392e68c3ca1a600f2ed67f6a1b0e14a0643b3ddaa9e6509589` |
| [`artifacts/design.md`](artifacts/design.md) | `741f4480f690bf10840e6ef7a059893b7359b4ed6c42fabf418116b5045c1ae4` |
| [`artifacts/tasks.md`](artifacts/tasks.md) | `da3fc0116d00f7638ec981ee56203192ef8937f76bbd7480ff08709b43d07b1d` |
| [`artifacts/specs/notification-preferences-api/spec.md`](artifacts/specs/notification-preferences-api/spec.md) | `c4ba355868255badb0ee3d8f2cb6d069f1a820253edf67f652697bc201e851a2` |

## Controller finding

The fully specified request remained in proposal-only mode without invoking
brainstorming. The agent created and strictly validated exactly four OpenSpec
artifacts, performed no implementation, and stopped with approval unchecked.
