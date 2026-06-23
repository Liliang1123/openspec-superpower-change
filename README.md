# openspec-superpower-change

[English](README.md) | [简体中文](README_zh.md)

`openspec-superpower-change` is a project-level AI development change gate and governance orchestrator. It is not a generic Software Design Document (SDD) workflow, not an OpenSpec alias, and not a Superpowers wrapper. 

Instead, it orchestrates domain clarification (`grill-with-docs`), change contract approval (`OpenSpec`), execution discipline (`Superpowers`), and progressive evidence validation (`Step Evidence Gate`) into a single, cohesive governance framework.

---

## Why this is not ordinary SDD

Ordinary Software Design Document (SDD) workflows typically follow a linear, un-gated process:

```text
spec -> plan -> tasks -> implement
```

`openspec-superpower-change` enforces active classification, risk assessment, and continuous verification:

```text
read local rules
-> classify request mode (Gate 0)
-> clarify domain language (when needed)
-> require OpenSpec approval (when contract/risk changes)
-> use Superpowers after approval (planning, TDD, debugging, implementation, verification)
-> keep evidence at every gated step (Step Evidence Gate)
-> claim completion only after verification evidence exists
```

This structural governance ensures AI-assisted development remains predictable, auditable, and safe—especially when working with complex, production-grade legacy codebases.

---

## Relationship matrix

| Capability | Core Responsibility | When to Invoke |
|---|---|---|
| **OpenSpec** | Defines *what* changes, *why* it changes, and the *acceptance contract*. | When API, schema, persistence, security, workflow, or public behavior changes. |
| **Superpowers** | Defines *how* approved work is planned, implemented, tested, debugged, reviewed, and verified. | For any non-trivial implementation phase. |
| **grill-with-docs** | Clarifies domain terms, boundaries, actors, lifecycle states, and design decisions. | Prior to writing specifications when domain logic is ambiguous. |
| **openspec-superpower-change** | Orchestrates all capabilities, defines request modes, and validates evidence gates. | Default entry point for all AI-assisted engineering tasks. |

---

## Gate 0: Mandatory Entry Gate

Before modifying any project files, running state-altering commands, or proposing specifications, the agent **MUST** complete **Gate 0**. 

Gate 0 requires stating:
1. **Active request mode**: Review-only / Discovery First / OpenSpec proposal / Approved implementation / Direct Change / Self-Evolution.
2. **References read**: Which files from `references/` were read and why they are sufficient.
3. **OpenSpec necessity**: Whether OpenSpec is required (`yes` / `no` / `uncertain`) with a brief reason.
4. **Superpowers required**: Mapping of required execution disciplines (e.g., TDD, writing-plans, systematic-debugging).
5. **Risk and confirmation**: Risk level assessment and whether user approval is required before state transition.

*Direct Change is strictly forbidden if the task touches runtime tools, security boundaries, sandboxes, cache strategies, or core workflows.*

---

## Change Paths

This framework defines three distinct paths based on risk and scope:

### 1. Lightweight Path
* **Usage**: Low-risk direct changes (typos, comments, formatting, non-contract documentation, tests for existing behavior, localized bug fixes).
* **Gated Requirements**: Local instructions check, targeted verification, and a concise final report. No OpenSpec artifacts required.

### 2. Standard Path
* **Usage**: Multi-step bug fixes, refactoring without behavior modification, or implementing already-approved contracts.
* **Gated Requirements**: Superpowers implementation plan (for multi-step work), TDD/debugging, Step Evidence Gate checkpoints, and verification-before-completion.

### 3. Strict Path
* **Usage**: Contract-changing or high-risk work (new capabilities, architectural/lifecycle modifications, API/schema shifts, security boundaries, skill workflow changes).
* **Gated Requirements**: Domain clarification (`grill-with-docs`), OpenSpec proposal & approval, Superpowers implementation plan, Step Evidence Gate validation, and formal verification evidence.

---

## Non-Negotiables

* **No Bypasses**: `CONTEXT.md` cannot replace OpenSpec proposals. `tasks.md` cannot replace a Superpowers plan. Superpowers planning cannot bypass OpenSpec approval.
* **Gate Sequence**: You cannot move to the next phase until the current Step Evidence Gate passes.
* **Evidence-Based**: No completion claims can be made without explicit verification evidence.
* **Evolution Guardrails**: Self-evolution of this skill cannot weaken validation gates, approval requirements, or user-control boundaries.

---

## Recommended Project Layout

For physical workspace projects governed by this skill, the following layout is recommended:

```text
├── README.md               # Project overview & language switch
├── README_zh.md            # Chinese translation of README
├── SKILL.md                # Main skill instructions (Gate 0, read matrix)
├── openspec/               # OpenSpec approved contracts
│   └── changes/
│       └── <change-id>/    # proposal.md, tasks.md, design.md
├── docs/
│   └── superpowers/
│       └── plans/          # YYYY-MM-DD-<change-id>.md
├── references/             # Detailed guide modules & rules
└── scripts/                # Verification & helper utilities
```

---

## Reference Guide

The `references/` directory contains modular rules and checklists. Under Gate 0, agents must refer to specific modules based on task type:

* **[workflow-overview.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/workflow-overview.md)**: Overall workflow routing, responsibilities, artifacts, and governance boundaries. It orchestrates when to proposal, design, implement, and verify.
* **[local-instruction-checkpoint.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/local-instruction-checkpoint.md)**: Rules for reading project-specific instructions (e.g., `AGENTS.md` and `CONTEXT.md` checks) before beginning any changes.
* **[request-modes.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/request-modes.md)**: Detailed criteria and constraints for the 6 request modes (Review-only, Discovery First, OpenSpec proposal, Approved implementation, Direct Change, Self-Evolution).
* **[openspec-decision-rule.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/openspec-decision-rule.md)**: Concrete rules for when an OpenSpec change is mandatory (e.g., API/schema shifts, security boundaries, skill workflow changes) and when it can be skipped.
* **[proposal-workflow.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/proposal-workflow.md)**: Step-by-step pipeline for drafting, structuring, validating (via `openspec validate`), and seeking approval for OpenSpec change contracts.
* **[approved-implementation-workflow.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/approved-implementation-workflow.md)**: Guidelines for writing Superpowers execution plans (`docs/superpowers/plans/`) containing small, testable steps with explicit verification.
* **[direct-change-rule.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/direct-change-rule.md)**: Workflow and validation rules for low-risk, non-contract modifications like formatting, localized bug fixes, and comment updates.
* **[step-evidence-gate.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/step-evidence-gate.md)**: Compact and full templates for the Step Evidence Gate. Defines mandatory evidence requirements at each execution checkpoint.
* **[response-patterns.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/response-patterns.md)**: Standardized response structures and templates for each request mode to ensure consistent and informative communication.
* **[sdd-comparison.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/sdd-comparison.md)**: High-level comparison between ordinary Software Design Document (SDD) flows and the `openspec-superpower-change` gated governance model.
* **[self-evolution-rule.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/self-evolution-rule.md)**: Strict rules for modifying this skill itself. Requires backwards compatibility, regression testing, and prevents weakening validation gates.
* **[sync-checklist.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/sync-checklist.md)**: A synchronization checklist for merging patches, minor updates, or major updates between local runtime copies and open-source repositories.
* **[fablecodex-caveman-review.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/fablecodex-caveman-review.md)**: Boundaries between the core gate model, optional FableCodex checklists, and caveman-style output compression.
* **[obsidian-knowledge-base.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/obsidian-knowledge-base.md)**: Standards for organizing long-term technical knowledge, task templates, and post-mortems in an Obsidian knowledge sink.

---

## Risk Model & FableCodex Boundaries

This skill adds process overhead intentionally to prevent regressions. 

* **FableCodex**: Treated as an optional reference checklist, not a parallel execution layer. Its inspection concepts may inspire reviews but cannot replace OpenSpec tasks or Step Evidence Gates.
* **Caveman-Style Output**: May compress chat messages, progress updates, or git commit messages. It **must not** compress official engineering artifacts (e.g., OpenSpec proposals, Superpowers plans, verification records, risk/rollback notes).

---

## Installation

To install this skill globally in your Codex environment:

```bash
cp -R openspec-superpower-change "${CODEX_HOME:-$HOME/.codex}/skills/openspec-superpower-change"
```

---

## Example Prompts

* **Review-Only Mode**:
  ```text
  Use openspec-superpower-change review-only mode. Read local rules, inspect the design, and report whether implementation would require OpenSpec. Do not modify files.
  ```
* **Proposal First Mode**:
  ```text
  Use openspec-superpower-change as the only entry gate. First determine whether this requires Discovery First or OpenSpec. If OpenSpec is required, create proposal artifacts and stop for approval before implementation.
  ```
* **Direct Change Mode**:
  ```text
  Use Direct Change mode. Confirm this restores intended behavior, reproduce the bug, make the smallest fix, add or update a regression test, run verification, and report root cause, changes, verification, and residual risk.
  ```
