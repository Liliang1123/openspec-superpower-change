# Companion Prompt-Load Evidence

Date: 2026-07-17, refreshed 2026-07-20
Change: `streamline-workflow-prompt-contracts`
Decision: use one thin Companion `SKILL.md` plus a directly linked Handoff-only
reference; independent decision Review remains required before task 2.5 closes.

## Evidence rules

- Runtime paths or supported host documentation are evidence; file size is not.
- `UNKNOWN` remains unknown and is not converted into a token estimate.
- The private traces were searched only for Companion Skill/reference paths. Their
  prompt and session contents were neither copied here nor used as evidence.

## Codex

Status: `documented`

The installed `skill-creator` contract defines three-level progressive
disclosure: metadata is always present, the `SKILL.md` body loads when selected,
and bundled resources load as needed. It also directs multi-variant Skills to
keep selection guidance in `SKILL.md` and move route-specific detail to directly
linked references.

- Source: `/Users/elvis/.codex-account-a/skills/.system/skill-creator/SKILL.md`
- SHA-256: `da44c88f6b3845a8fa8c60792ec9a722110a55a9793c279757b48fefb11f819c`
- Relevant section: `Progressive Disclosure Design Principle`
- Limitation: this is the supported Codex contract, not an exported exact prompt.
- Consequence: a thin entry plus one-level Handoff reference is supported.

## Grok CLI

Status: `observed` for standalone and valid-Handoff route outcomes

- Initial standalone version: `grok 0.2.102 (ab5ebf69acec)`
- Discovery evidence: `grok inspect --json` listed
  `/Users/elvis/.grok/skills/codex-brief-antigravity-review/SKILL.md` as a user Skill.
- Scenario command: `grok --single <standalone read-only prompt> --no-subagents
  --disable-web-search --permission-mode plan --debug --debug-file <private-log>`
- Private trace SHA-256:
  `fc1c65873bf5a387b1c79936ee9a06a49314a3f96d4958879de686d3e6f88d40`
- Path-only scan result: Companion `SKILL.md` paths were present; no Companion
  `references/*` path was present.
- Limitation: this proves the observed standalone activation only. It does not
  prove hidden prompt composition or future host behavior.
- Consequence: no eager-reference behavior was observed that would require a
  second Skill entrypoint.

The 2026-07-20 source forward-test reran both routes against the feature
worktree with `grok 0.2.106 (bde89716f679)`, plan permission, no subagents, and
web search disabled. The runner contained raw requests and output-field names,
but no expected answers.

- Runner SHA-256:
  `87327fd2f6c2b124071b314c11bb59fc27c9b22a5903c1b33dc86ca019d1f2bb`
- Standalone output SHA-256:
  `1715304355b154c36490c40fec7e1c25b1115c95fc4863a527db95c1e05a324e`
- Standalone observable result: route `Standalone Lightweight`, no Handoff
  reference reported read, no status mutation, completion owner `Codex`.
- Valid-Handoff output SHA-256:
  `934e333117ae77355551971c512f10530d835839cae6f5ffd51ef630d47e507f`
- Valid-Handoff observable result: route `handed-off-external-execution`, with
  `SKILL.md`, `references/handed-off-external-execution.md`, and
  `references/handoff-contract.md` reported read; no status mutation; final
  completion owner `openspec-superpower-change`.
- Source hashes: thin entry
  `fb0c3c2157415674df41147ebc415e701d45f6d894d10c763117dc3253d95e00`;
  Handoff governor
  `3d4d0b25a0312c6f21d682044af2296a5a9541c8a7bade2bb382b4fcc8b02bf7`;
  Handoff contract
  `62dfe033d0c6f8b6e0fde79e32f44c97a4da1efca7913def3378bcd16c5e2340`.
- Trace limitation: Grok's debug log exposed `read_file` call counts but not
  safely attributable path arguments, and also contained runtime authentication
  material. It is private temporary data, is not durable evidence, and must be
  deleted after the final evidence gate. The route conclusions above are
  observable output evidence, not an exact injected-prompt claim.

## Antigravity CLI

Status: `UNKNOWN`

- CLI surface: `agy`; startup reported language server version `1.1.3`.
- Scenario command: `agy --print --sandbox --mode plan --log-file <private-log>
  <standalone read-only prompt>`
- Result: the headless run completed after auto-denying a command permission,
  but the requested private trace remained empty. Antigravity's own CLI log did
  not expose Companion Skill/reference paths in a path-only scan.
- Requested-log SHA-256:
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- Host-log SHA-256:
  `b357ae37a2693711978bb3db1878cb3f5dbe6e54df4a17c6ad1ee15a0904926c`
- Limitation: absence of a logged path is not proof of absence from an injected
  prompt. No token or loading conclusion is drawn.
- Consequence: preserve a single discoverable entry and an explicit direct
  pointer so the route remains usable even though loading is unobservable.

## Structure decision

The approved thin-reference branch is selected because Codex's supported Skill
contract explicitly provides on-demand references, Grok's controlled route
tests distinguish standalone from valid-Handoff behavior, and no required target
proved that references are unavoidably injected. Antigravity remains `UNKNOWN`,
so this decision carries no measured token-savings claim. This is an
evidence-selected implementation decision, not task 2.5 completion until an
independent Review accepts the evidence and limitations.

The implementation must preserve the existing Skill name/description, route
selection, standalone contract, common authority and Git boundaries, and place
the complete unchanged external-batch governor in
`references/handed-off-external-execution.md`. Post-implementation forward tests
must prove that standalone work does not enter Handoff governance and a valid
Handoff explicitly loads the complete governor.

## Leakage review

PASS for the durable artifact. This document contains executable names,
version/hash evidence, summarized route observations, and source paths only. It
contains no session identifier, credential, environment value, hidden reasoning,
or private prompt transcript. Raw debug logs are explicitly excluded and remain
temporary cleanup targets.
