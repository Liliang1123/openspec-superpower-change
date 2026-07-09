# 两个 Codex 全局 Skill 工作流优化设计

文档类型：架构与工作流优化设计
日志及版本：2026-07-10 v1.0

## 结论

两个 Skill 保持独立，不合并、不并行争抢入口：

- `openspec-superpower-change` 是所有状态改变型开发工作的唯一准入与最终完成入口。
- `codex-brief-antigravity-review` 是 task prompt/Brief/diff/Report/evidence 的专项编写与复核 Skill；已有有效 Handoff 时兼任外部批次 governor。

## Review 发现的主要问题

1. 两个 frontmatter description 同时覆盖任务拆解、Review 和外部协作，隐式触发会抢路由。
2. Brief Skill 强制 Handoff，导致只写 prompt、普通 diff Review 等轻量场景被错误 `BLOCKED`。
3. OpenSpec 与 Superpowers brainstorming 可能重复设计、重复文档和重复审批。
4. Step Evidence Gate 被理解为覆盖每个 TDD 微步骤，执行过重。
5. `FAIL`/`BLOCKED` 没有同批次修正、恢复、重新验证和再次 Review 的强制回环。
6. 最终外部批次 PASS 没有回交 router 的可机读状态，可能被误当成任务完成。
7. Handoff marker 可复制到多个产物，缺少 canonical source、revision 和 attempt 历史。
8. validator 未校验关键状态迁移，且 Brief validator 的无 PyYAML fallback 与 target path 存在真实缺陷。
9. 两仓 Git 授权规则、Self-Evolution 强度和验证环境说明不一致。
10. 源码与全局 runtime skill 缺少可重复的同步与四份验证闭环。

## 最终路由

| 场景 | 入口 | OpenSpec | Superpowers | Handoff |
|---|---|---:|---|---:|
| 只写/优化 prompt、Brief、checklist | Brief standalone | 否 | 否 | 否 |
| 普通 diff/Report/evidence 只读 Review | Brief standalone | 否 | 否 | 否 |
| Review 并修复、任何文件修改 | Change Gate | 按边界判断 | 按变更类型 | 仅外部执行 |
| 局部恢复既有行为 | Change Gate / Direct Change | 否 | TDD/debugging/verification 按需 | 外部执行时 compact |
| 新能力、API/schema、安全、workflow lifecycle | Change Gate / OpenSpec | 是 | 批准后 plan/TDD/review/verification | 外部执行时需要 |
| 已有有效 Handoff 的 dispatch/resume/Report Review | Brief handed-off | 沿用既有决定 | 批次 Review 已承担 review gate | 是 |
| Skill trigger/routing/evidence/completion 变化 | Change Gate / Major Self-Evolution | 是 | writing-skills + RED/GREEN + review | 按执行方式 |

## OpenSpec / Superpowers / AGENTS.md 协同

- 项目 `AGENTS.md` 与当前用户直接指令优先；Git add/commit/push 只在本次明确授权时执行。
- OpenSpec 只负责 what/why/acceptance/approval，是唯一设计合同。
- `superpowers:brainstorming` 仅用于澄清设计选项，结论写入 OpenSpec design，不再生成同一决策的第二份设计审批。
- OpenSpec 批准后，`superpowers:writing-plans` 负责可执行步骤；OpenSpec `tasks.md` 不替代 plan。
- TDD 管理业务 slice 内 RED/GREEN；Step Evidence Gate 只签收完整 slice 或风险里程碑。
- inline standard/strict 使用独立 Review；外部批次 Review 已承担 code-review gate，避免重复。
- `verification-before-completion` 只在最终 Review PASS 且 fresh verification 完成后允许成功声明。

## 闭环状态

```text
ready-for-brief -> ready-for-execution -> ready-for-review
FAIL -> needs-fix -> 同 batch 新 attempt -> verify -> Review
BLOCKED -> blocked(owner/reason/resume_condition) -> 同 batch 新 attempt -> Review
PASS 非最终 -> 下一 batch
PASS 最终 -> awaiting-final-verification -> router final verification + final Review
两者 PASS -> complete（终态）
```

Canonical state 只存在于 `docs/agent-collab/<change-id>/status.md`。Schema v2 使用 `contract_revision`、`attempt`、`last_review_result`、`final_review_result`、`final_verification` 和 blocker 字段；attempt 产物不得覆盖历史。

## 证据与验证

- `compact`：聚焦验证 + inline diff/self-review；默认无大 plan/Handoff。
- `standard`：完整业务 slice、关键命令、独立 Review、最终矩阵一次。
- `strict`：真实 API/schema/迁移/安全/回滚/业务链证据，不得用 mock 或单测替代。
- 两仓使用标准库 `unittest` 固化路由、schema、transition、fallback 和 parity 负例。
- `quick_validate.py` 使用具备 PyYAML 的解释器；项目 validator 必须在无 PyYAML 默认 `python3` 下通过。

## 回滚

实施期结构化备份：`/private/tmp/two-codex-skills-self-evolution-20260710-064702/`。验证或同步失败时，按相对目录恢复 source/runtime；成功提交和 push 后删除临时备份。

## 待办

- 已完成两仓及两份 runtime skill 的 validator、`quick_validate.py`、38 个回归测试、parity 和三轮独立 Review。
- 剩余发布动作：分别 commit、push，并在成功后清理临时备份。
