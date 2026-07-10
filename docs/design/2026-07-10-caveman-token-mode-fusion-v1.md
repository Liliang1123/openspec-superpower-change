# Caveman 与两个全局 Skill 的融合方案 v1

文档类型：架构融合设计与实施闭环
日志及版本：2026-07-10 v1.0

## 结论

`caveman` 应仅作为**输出压缩器**，不承接治理职责；两个 skill 的闭环不变。

- `openspec-superpower-change`：状态变化、OpenSpec 需/否判定、Superpowers 规划、最终验收与任务完成 gate 的唯一入口。
- `codex-brief-antigravity-review`：轻量 standalone 写作/只读 Review 与已有有效 Handoff 的外部批次治理。
- `caveman`：在以上两个 skill 的非治理输出层被显式要求时压缩表达（不省略证据字段）。

## 触发与场景分流

```text
非状态变更、非治理路径（prompt/brief/evidence-only）
  -> codex-brief-antigravity-review
  -> 需要更短说明则可启用 caveman 风格压缩

状态变更/Review-and-fix/Final completion
  -> openspec-superpower-change
  -> 按现有 Gate 0、Preflight、Verify->Review 闭环
  -> 若用户要求，最终给定用户可读摘要可压缩，但不能省略关键字段

已有有效 Handoff 执行批次
  -> codex-brief-antigravity-review 按 schema-3 管理
  -> 仅可输出压缩版解释，不得改写 evidence/状态字段
```

## 与现有闭环的对齐

- 现有 `方案 -> 自我 Review -> 实施 -> 验证 -> 再 Review -> 修正` 仍完整保留。
- `FAIL`/`BLOCKED` 仍必须修正/恢复后再次 Review。
- 最终 `PASS` 仍由 `openspec-superpower-change` 做 final verification 与 final review 的闭环门禁。
- `caveman` 只影响用户可读文字，不影响 `status.md`、artifact path/hash 或 evidence role/result。

## 约束统一口径

1. 任何治理 artifact（schema-1/3 manifest、handoff contract、status、review 模板）不可压缩。
2. 不允许用 caveman 省略：
   - `review result`（PASS/FAIL/BLOCKED）
   - 风险与阻塞原因
   - required critical commands / stop conditions
   - artifact path 与 sha256
3. 遇到安全、状态迁移、生产级验证与完整闭环时不应默认 caveman；若用户要求，可仅将叙述压缩，不改变实质内容。

## 本次融合优化结果（落地项）

- 在 `openspec-superpower-change/SKILL.md` 与 `codex-brief-antigravity-review/SKILL.md` 增加 caveman 角色边界：
  - caveman 是输出压缩层；
  - 明确 governance artifact 不可压缩、不可替代。
- 在 `openspec-superpower-change/references/request-modes.md`、`references/response-patterns.md` 增加 token 预算/输出压缩边界。
- 形成单一设计文档记录：本页。

## 后续验证

- 仅文档与边界约束变更，无新增运行时代码。
- 需执行两个仓库自检：`quick_validate.py`、验证脚本、`unittest`，确认变更不破坏既有规则。
