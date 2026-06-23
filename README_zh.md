# openspec-superpower-change

[English](README.md) | [简体中文](README_zh.md)

`openspec-superpower-change` 是一个项目级的 AI 开发变更准入控制（Change Gate）与治理编排器。它不是一个普通的软件设计文档（SDD）工作流，不是 OpenSpec 的别名，也不是 Superpowers 的简单包装。

相反，它将领域澄清（`grill-with-docs`）、变更合同审批（`OpenSpec`）、执行规范（`Superpowers`）以及渐进式证据验证（`Step Evidence Gate`）有机结合，形成了一个统一的、规范化的治理框架。

---

## 为什么这不同于普通的 SDD

普通的软件设计文档（SDD）工作流通常遵循一种线性的、无准入控制的开发过程：

```text
spec -> plan -> tasks -> implement
```

而 `openspec-superpower-change` 强制进行主动分类、风险评估和持续验证：

```text
读取本地规则 (read local rules)
-> 对请求模式进行分类 (Gate 0)
-> 澄清领域语言（必要时）
-> 评估是否需要 OpenSpec 审批（当合同/风险发生变更时）
-> 在审批通过后使用 Superpowers（规划、TDD、调试、实现、验证）
-> 在每一个控制步骤留存证据 (Step Evidence Gate)
-> 仅在验证证据齐备后才声明完成 (claim completion)
```

这种结构化治理能够确保 AI 辅助开发过程保持可预测、可审计和安全——特别是在处理复杂的、生产级的历史代码库时。

---

## 关系矩阵

| 能力 | 核心职责 | 何时调用 |
|---|---|---|
| **OpenSpec** | 定义 **“改动什么”**、**“为什么改”** 以及 **“验收合同”**（Acceptance Contract）。 | 当 API、Schema、持久化、安全性、工作流或公共行为发生变更时。 |
| **Superpowers** | 定义 **“如何实现”** 已批准的开发工作，包括规划、实现、测试、调试、评审和验证。 | 任何非平凡（Non-trivial）的代码实现阶段。 |
| **grill-with-docs** | 澄清领域术语、边界、参与者、生命周期状态和设计决策。 | 在编写规范之前，当领域逻辑存在歧义或不明确时。 |
| **openspec-superpower-change** | 编排所有能力，定义请求模式，并验证证据控制门（Evidence Gates）。 | 作为所有 AI 辅助工程任务的默认入口。 |

---

## Gate 0：强制准入控制

在修改任何项目文件、运行会改变状态的命令或提出设计规范之前，Agent **必须** 完成 **Gate 0**。

Gate 0 要求声明：
1. **当前请求模式 (Active request mode)**：Review-only（仅评审）/ Discovery First（探索优先）/ OpenSpec proposal（OpenSpec 提案）/ Approved implementation（批准后实现）/ Direct Change（直接变更）/ Self-Evolution（自我进化）。
2. **已读参考资料 (References read)**：阅读了 `references/` 目录下的哪些文件，以及为什么它们是足够的。
3. **OpenSpec 必要性 (OpenSpec necessity)**：评估是否需要 OpenSpec 审批（`yes` / `no` / `uncertain`），并给出简短理由。
4. **所需 Superpowers (Superpowers required)**：映射本次任务所需的执行规范（如：TDD、writing-plans、systematic-debugging）。
5. **风险与确认 (Risk and confirmation)**：评估风险级别，以及在状态迁移前是否需要用户确认。

*如果任务涉及运行期工具、安全边界、沙箱、缓存策略或核心工作流，严禁使用 Direct Change。*

---

## 变更路径 (Change Paths)

该框架根据风险和范围定义了三种不同的开发路径：

### 1. 轻量路径 (Lightweight Path)
* **适用场景**：低风险的直接修改（拼写错误、注释、格式化、无合同影响的文档更新、对现有行为补充测试、定位明确的 bug 修复）。
* **控制要求**：本地指令检查、针对性验证和简短的最终报告。不需要创建 OpenSpec 构件。

### 2. 标准路径 (Standard Path)
* **适用场景**：多步骤的 bug 修复、不改变外部行为的重构，或实现已经批准的合同。
* **控制要求**：Superpowers 实现计划（针对多步骤工作）、TDD/调试、Step Evidence Gate 检查点，以及完成前的验证（verification-before-completion）。

### 3. 严格路径 (Strict Path)
* **适用场景**：涉及合同变更或高风险的工作（新功能、架构/生命周期修改、API/Schema 变更、安全边界变更、Skill 工作流变更）。
* **控制要求**：领域澄清（`grill-with-docs`）、OpenSpec 提案与审批、Superpowers 实现计划、Step Evidence Gate 验证，以及正式的验证证据。

---

## 硬性约束 (Non-Negotiables)

* **严禁绕过**：`CONTEXT.md` 绝对不能替代 OpenSpec 提案。`tasks.md` 绝对不能替代 Superpowers 计划。Superpowers 计划不能绕过 OpenSpec 审批。
* **步骤顺序**：在当前步骤的 Step Evidence Gate 通过之前，不得进入下一阶段。
* **基于证据**：没有明确的验证证据，严禁声明任务已完成。
* **演进红线**：本 Skill 的自我进化（Self-Evolution）不得削弱验证门、审批要求或用户控制边界。

---

## 推荐的项目结构

对于由本 Skill 治理的物理工作空间项目，推荐使用以下目录结构：

```text
├── README.md               # 项目概览与语言切换
├── README_zh.md            # 中文版 README
├── SKILL.md                # 核心 Skill 说明（Gate 0, 阅读矩阵）
├── openspec/               # OpenSpec 已批准合同
│   └── changes/
│       └── <change-id>/    # proposal.md, tasks.md, design.md
├── docs/
│   └── superpowers/
│       └── plans/          # YYYY-MM-DD-<change-id>.md
├── references/             # 详细指南模块与规则
└── scripts/                # 验证与辅助工具脚本
```

---

## 参考指南 (Reference Guide)

`references/` 目录包含了模块化的规则和检查清单。在 Gate 0 准入阶段，Agent 必须根据任务类型参考特定的指南：

* **[workflow-overview.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/workflow-overview.md)**：全局工作流导览。定义了整体工作流的路由机制、各角色职责、产出物以及治理边界，编排了何时进行提案、设计、实现和验证。
* **[local-instruction-checkpoint.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/local-instruction-checkpoint.md)**：本地指令检查点。规定了在开始任何修改前，必须读取和核对的本地指令（如项目根目录 `AGENTS.md` 和 `CONTEXT.md` 规则检查），确保改动符合项目规范。
* **[request-modes.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/request-modes.md)**：请求模式详解。详细定义了 6 种请求模式（Review-only, Discovery First, OpenSpec proposal, Approved implementation, Direct Change, Self-Evolution）的判定标准与行为约束。
* **[openspec-decision-rule.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/openspec-decision-rule.md)**：OpenSpec 决策规则。明确给出了必须引入 OpenSpec 变更合同的 11 类技术场景（如 API 变更、架构调整、沙箱边界等），以及可以直接进行轻量修改的例外场景。
* **[proposal-workflow.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/proposal-workflow.md)**：提案工作流规范。规定了 OpenSpec 提案包的创建、组织、验证（通过 `openspec validate`）以及等待用户批准的详细控制步骤。
* **[approved-implementation-workflow.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/approved-implementation-workflow.md)**：批准后实现工作流。指导在提案获批后，如何通过 `superpowers:writing-plans` 建立实施计划（存储在 `docs/superpowers/plans/`），并把任务分解为包含具体文件、测试命令和证据控制门的执行步骤。
* **[direct-change-rule.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/direct-change-rule.md)**：直接变更规则。规定了无须 OpenSpec 审批的低风险修改（如格式化、本地 bug 修复、拼写错误纠正等）的执行标准，强调依然需要进行针对性验证和最终报告。
* **[step-evidence-gate.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/step-evidence-gate.md)**：步骤证据门参考。提供了不同风险等级下实施步骤的证据校验模板（包括 Gate 0 到 Gate 2 等）。详细描述了在执行具体代码修改时输出的校验信息以确保可审计性。
* **[response-patterns.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/response-patterns.md)**：响应模式模板。定义了 Agent 在处于不同请求模式（评审、探索、实现、直接变更）时，与用户交互时必须遵循的回复结构、前置免责声明和输出模板。
* **[sdd-comparison.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/sdd-comparison.md)**：与普通 SDD 的对比。深度解析了本治理框架相比于传统的软件设计文档流程，在领域澄清、控制门拦截、基于证据的完成声明等方面的增强与优化。
* **[self-evolution-rule.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/self-evolution-rule.md)**：Skill 自我进化规则。规定了本 Skill 自身优化、重构或升级时的规范。强调自我进化不得削弱任何验证门、证据校验或用户控制边界，并需要对 Skill 进行回归验证。
* **[sync-checklist.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/sync-checklist.md)**：同步检查清单。当本 Skill 在本地运行期拷贝或开源项目副本发生更新时，用于规范双向同步和兼容性验证的步骤。
* **[fablecodex-caveman-review.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/fablecodex-caveman-review.md)**：方法论边界。界定了本门控工作流与其它方法论（如 FableCodex）和输出风格（Caveman 风格压缩）之间的集成边界，明确指出正式的工程文档绝对不能被过度压缩。
* **[obsidian-knowledge-base.md](file:///Users/elvis/file/develop/opensource/openspec-superpower-change/references/obsidian-knowledge-base.md)**：Obsidian 知识库集成规范。指导如何将任务执行中的经验沉淀、技术复盘记录到本地 Obsidian 知识库中，作为长期知识的汇聚地。

---

## 风险模型与 FableCodex 边界

本 Skill 刻意引入了一定的流程开销，以防代码回归和失控。

* **FableCodex**：仅作为可选的参考清单，而非平行的执行层。其审查概念可以启发 Code Review，但不能取代 OpenSpec 任务或 Step Evidence Gate。
* **Caveman 风格输出**：可用于压缩聊天消息、进度更新或 git commit 提交信息。但 **绝对禁止** 压缩正式的工程构件（如 OpenSpec 提案、Superpowers 计划、验证记录、风险/回滚说明）。

---

## 安装说明

在 Codex 环境中全局安装此 Skill：

```bash
cp -R openspec-superpower-change "${CODEX_HOME:-$HOME/.codex}/skills/openspec-superpower-change"
```

---

## 示例 Prompt

* **仅评审模式 (Review-Only Mode)**:
  ```text
  Use openspec-superpower-change review-only mode. Read local rules, inspect the design, and report whether implementation would require OpenSpec. Do not modify files.
  ```
* **提案优先模式 (Proposal First Mode)**:
  ```text
  Use openspec-superpower-change as the only entry gate. First determine whether this requires Discovery First or OpenSpec. If OpenSpec is required, create proposal artifacts and stop for approval before implementation.
  ```
* **直接变更模式 (Direct Change Mode)**:
  ```text
  Use Direct Change mode. Confirm this restores intended behavior, reproduce the bug, make the smallest fix, add or update a regression test, run verification, and report root cause, changes, verification, and residual risk.
  ```
