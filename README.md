# openspec-superpower-change

[English](README.md) | [简体中文](README_cn.md)

`openspec-superpower-change` is a Codex skill that acts as the change-control entry gate for AI-assisted engineering work. It connects project-local rules, OpenSpec change contracts, Superpowers execution practices, and evidence-based verification into one repeatable workflow.

The goal is simple: an AI agent should not move from a request directly to implementation when the work may affect runtime behavior, public contracts, security, persistence, workflow routing, or operator-visible behavior.

## Highlights

- Classifies every request before state-changing work begins.
- Separates review-only, discovery, proposal, approved implementation, direct change, and self-evolution modes.
- Decides when OpenSpec is required and blocks implementation before approval.
- Routes approved work into Superpowers planning, TDD, debugging, and verification flows.
- Requires Step Evidence Gate output before progress or completion claims.
- Requires current-revision Plan/Brief Preflight Review before execution.
- Uses schema-5 Handoff state plus schema-2 evidence to separate agent product,
  instance, role, capability profile, provenance, and Confirmation Lease.
- Routes stable High/Medium/Low capability profiles without hardcoding model
  names and keeps the bound Codex control-plane instance authoritative.
- Separates platform, workflow-scope, and business/production authorization;
  High Review audits actual wiring, mechanisms, and an independent probe.
- Provides allowlisted Codex/Antigravity/Grok runtime synchronization with a
  versioned managed governance block and sensitive-category denial.

## Why It Exists

AI coding agents can be effective, but in production-grade repositories they commonly fail in ways that are preventable:

- implementing before reading local project rules;
- treating a task checklist as an approved contract;
- using test-only evidence for runtime behavior claims;
- bypassing OpenSpec for API, persistence, security, or workflow changes;
- weakening governance rules while editing the governance skill itself;
- losing track of approval status across external-agent handoffs.

This skill turns those risks into explicit gates, references, and validation checkpoints.

## How It Fits

| Capability | Responsibility | Owned By |
|---|---|---|
| Local project rules | Repository-specific constraints, review artifacts, handoff rules, commit conventions | Project `AGENTS.md` / local docs |
| OpenSpec | Change contract, requirements, scenarios, approval state | `openspec/` |
| Superpowers | Implementation planning, TDD, debugging, verification discipline | Superpowers skills |
| Step Evidence Gate | Evidence required before advancing or claiming completion | `references/step-evidence-gate.md` |
| Prompt / external batch review | Standalone prompt/diff review and Handoff-backed Brief/Report/Review attempts | `codex-brief-antigravity-review` |
| openspec-superpower-change | Routing, risk classification, approval gate, self-evolution boundary | This skill |

## Core Workflow

```text
Read local rules
-> Gate 0 request classification
-> Discovery First if terms or boundaries are unclear
-> OpenSpec proposal if contracts or high-risk behavior change
-> stop until approval
-> Superpowers plan for approved implementation
-> Plan/Brief Preflight Review; revise and repeat until PASS
-> TDD / debugging / implementation discipline
-> Step Evidence Gate on complete business slices
-> verify -> Review -> fix and repeat until Review PASS
-> persist fresh final verification evidence, then final diff/scope Review
-> reconcile/archive OpenSpec and complete only after all gates pass
```

## Request Modes

| Mode | Use When | File Changes? |
|---|---|---:|
| Review-only | The user asks this change gate to review architecture, authorization, risk, or completion evidence. | No |
| Discovery First | Terms, actors, lifecycle, or boundaries are unclear. | Usually glossary / context only |
| OpenSpec proposal | New capability, behavior contract, architecture, security, persistence, API, or workflow changes are needed. | Proposal artifacts only |
| Approved implementation | An OpenSpec-backed proposal has been explicitly approved. | Yes, after plan |
| Direct Change | Low-risk restoration, typo, formatting, docs-only, config-only, or tests for existing behavior. | Yes, scoped |
| Self-Evolution | This skill, its references, validators, examples, or sync rules are being changed. | Yes, gated |

Standalone task-prompt/Brief/checklist writing and ordinary read-only diff or Report review belong to `codex-brief-antigravity-review`. “Review and fix” returns here because it is implementation.

## Gate 0

Before editing files, running state-changing commands, creating proposal artifacts, or starting implementation, the agent must state:

1. active request mode;
2. references read and why they are sufficient;
3. whether OpenSpec is required;
4. required Superpowers sub-skills;
5. risk level, next action, and whether user confirmation is required.

## OpenSpec Boundary

OpenSpec is required for:

- new functionality or public behavior changes;
- API, schema, data lifecycle, persistence, or migration changes;
- security, sandbox, permissions, cross-tenant behavior, or auth changes;
- runtime tool exposure, cache strategy, request routing, skill routing, or workflow lifecycle changes;
- broad refactors that alter system boundaries;
- skill workflow changes.

OpenSpec may be skipped only for narrow restoration of existing intended behavior, small config changes without contract impact, typo/comment/formatting changes, docs-only updates without behavior impact, or tests for already-defined behavior.

## Evidence Profiles

| Profile | Typical Use |
|---|---|
| compact | Low-risk docs, formatting, config, or localized direct changes. |
| standard | Default multi-step implementation, review, and verification. |
| strict | Security, auth, public API/schema, persistence, migration, deployment, rollback, or cross-tenant work. |

## Repository Structure

```text
.
├── SKILL.md
├── references/
│   ├── request-modes.md
│   ├── openspec-decision-rule.md
│   ├── proposal-workflow.md
│   ├── approved-implementation-workflow.md
│   ├── direct-change-rule.md
│   ├── step-evidence-gate.md
│   ├── superpowers-adapter.md
│   ├── self-evolution-rule.md
│   ├── sync-checklist.md
│   ├── cross-cli-sync.md
│   └── cross-cli-portable-manifest.json
├── scripts/
│   ├── validate_core_gates.py
│   └── validate_cross_cli_sync.py
├── tests/
│   ├── test_workflow_rules.py
│   └── test_cross_cli_sync.py
├── openspec/
│   ├── project.md
│   └── changes/
├── examples/
├── templates/
└── docs/
```

## Key References

- `references/request-modes.md`: operating modes and constraints.
- `references/openspec-decision-rule.md`: when OpenSpec is mandatory.
- `references/proposal-workflow.md`: proposal creation and validation flow.
- `references/approved-implementation-workflow.md`: approved implementation workflow.
- `references/direct-change-rule.md`: low-risk direct change requirements.
- `references/step-evidence-gate.md`: compact and full evidence templates.
- `references/superpowers-adapter.md`: OpenSpec-aware Superpowers artifact, permission, and Preflight mapping.
- `references/self-evolution-rule.md`: rules for changing this skill.
- `references/sync-checklist.md`: local runtime and open-source copy synchronization.
- `references/cross-cli-sync.md`: required runtime targets, managed-rule parity,
  discovery, rollback, and completion blocking.

## Installation

Copy or link this skill into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R openspec-superpower-change "${CODEX_HOME:-$HOME/.codex}/skills/openspec-superpower-change"
```

## Validation

Run validation after editing the skill:

```bash
"${PYTHON_BIN:-python3}" "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" /path/to/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 /path/to/openspec-superpower-change/scripts/validate_core_gates.py /path/to/openspec-superpower-change
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s /path/to/openspec-superpower-change/tests -v
```

For an actual schema-4 external status, also validate referenced evidence files:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /path/to/openspec-superpower-change/scripts/validate_core_gates.py \
  /path/to/openspec-superpower-change \
  --status /project/docs/agent-collab/<change-id>/status.md \
  --artifact-root /project
```

Each referenced artifact embeds a schema-1 manifest that binds role, result,
change, batch, attempt, and source canonical revision/SHA-256. Before a
transition introduces new evidence, validate a proposed status from outside the
project with `--previous-status /project/docs/agent-collab/<change-id>/status.md`;
this is mandatory for `complete`. Replace the one canonical status only after
PASS, and do not persist a second marker block in the project.

`quick_validate.py` requires PyYAML; set `PYTHON_BIN` accordingly. The project validator and tests exercise the dependency-free fallback.

Portable core-skill changes must additionally use
`scripts/validate_cross_cli_sync.py` to generate a path/hash-only plan, apply and
verify each explicitly authorized runtime target, verify discovery/parity, and
run the path/category-only sensitive audit. Runtime/global writes remain subject
to explicit user authorization.

## Example Prompts

```text
Use openspec-superpower-change review-only mode. Read local rules, inspect this implementation plan, and report whether it requires OpenSpec. Do not modify files.
```

```text
Use openspec-superpower-change as the entry gate. Decide whether this requires Discovery First or an OpenSpec proposal before implementation.
```

```text
Use Direct Change mode. Confirm this restores intended behavior, make the smallest fix, run verification, and report evidence before claiming completion.
```

## Maintenance Notes

- Do not weaken approval gates, evidence gates, or completion-claim rules.
- Do not let OpenSpec `tasks.md` replace a Superpowers implementation plan.
- Do not let `CONTEXT.md` replace OpenSpec proposal artifacts.
- Do not sync runtime and open-source copies with directory-level overwrites; use the sync checklist.
- Do not complete verified-but-unreviewed work; any Review finding restarts correction, verification, and Review.
- Do not call OpenSpec-backed work closed with unreconciled tasks or without the
  repository-appropriate archive and post-archive validation.

## License

MIT. See [LICENSE](LICENSE).
