# Proposal Review: streamline-workflow-prompt-contracts

- **文档类型**：OpenSpec Proposal Independent Review
- **日志及版本**：2026-07-17 / proposal-only independent review
- **结论**：通过
- **change-id**：`streamline-workflow-prompt-contracts`
- **验证范围**：
  - `openspec/changes/streamline-workflow-prompt-contracts/{proposal,design,tasks}.md`
  - `openspec/changes/streamline-workflow-prompt-contracts/specs/skill-workflow-governance/spec.md`
  - `docs/review/2026-07-17-streamline-workflow-prompt-contracts-review-draft.md`
  - `CONTEXT.md`
  - 对照既有 `openspec/specs/skill-workflow-governance/spec.md` 完成/路由相关条款
  - 复跑：`openspec validate streamline-workflow-prompt-contracts --strict` PASS
  - 复跑：`python3 scripts/validate_core_gates.py .` PASS
  - 复跑：`python3 -m unittest discover -s tests -v` → 128 tests PASS

## 问题与风险

未发现阻塞问题。

### 非阻塞残余风险（实施期跟踪，不挡批准）

1. **Superpowers 修正落点**：`finishing-a-development-branch` 属于 installed/source-managed 依赖；实施时必须固定修正路径、hash 与回归 fixture，防止上游覆盖回写矛盾文案。
2. **Companion 结构仍受测量门控**：薄 reference 与拆 Skill 二选一依赖运行时加载证据；不可观察目标记 `UNKNOWN`，不得用 bytes 冒充 token 事实或强行 split。
3. **既有基线 spec 历史表述**（如 handoff schema 版本措辞）不在本 change 范围；实施时勿借机扩大为全量 schema 重写。

## 事实偏差 / 遗漏

未发现相对已接受五项范围的偏差。

已确认覆盖：

| 已接受项 | Proposal 覆盖 |
|---|---|
| Option 2 worktree 矛盾 | Decision 1 + ADDED Requirement 1 |
| 唯一 Completion Contract | Decision 2 + ADDED Requirement 2 |
| Companion 薄入口 / 证据门控结构 | Decision 3 + ADDED Requirement 3 |
| prompt-collision forward tests | Decision 4 + ADDED Requirement 4 |
| 实测 prompt-load / tokenizer | Decision 5 + ADDED Requirement 4 |

已确认 **Non-Goals** 正确排除：Project Learning 重设计、CONTEXT/grill/caveman 语义重写、削弱证据/Review/Git 权限、Handoff schema 5 变更、第三治理器、按模型名路由。

已确认治理不变量保留：batch PASS ≠ task complete；Gate 0 相位选择；未授权 Git 阻塞；HARD-GATE 一旦选中不得削弱。

## 摘要

该 Major Self-Evolution proposal 范围与先前独立架构 Review 的**修正后**处置一致：定向精简提示词契约与冲突面，而非推倒治理。规格场景可测，设计决策与 tasks 的 RED→GREEN→sync→closeout 顺序合理。验证门禁复跑通过。

**实施批准条件**：以本 change-id 与当前 scoped contract 为准；实施中任何扩大 non-goal 范围或削弱 Non-negotiables 的改动需重新 Review。

## 后续建议 / 待办

1. 记录用户/控制平面对本 change-id 的实施批准（tasks 1.5）。
2. 从 tasks 2.x RED 证据开始实施；勿跳过 Option 2 矛盾 RED fixture。
3. Companion 结构选择必须绑定 task 2.4 证据后再做 3.3。
4. 临时备份 `/tmp/streamline-workflow-prompt-contracts-backup.kmSVEu` 保留至最终 Review PASS 后再清理。

## 批准声明

**批准实施 streamline-workflow-prompt-contracts**

批准含义：允许按 proposal/design/tasks/spec 实施五项定向改动；不批准范围外重构；不授权 git commit/push（除非用户另行明确命令）。
