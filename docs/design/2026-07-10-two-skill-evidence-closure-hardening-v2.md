# 两个 Codex 全局 Skill 证据闭环强化设计（v2）

文档类型：架构 Review、Self-Evolution 设计与实施闭环
日志及版本：2026-07-10 v2.0

## 结论

两个 Skill 继续保持单一入口分工，不合并为重复流程：

- `openspec-superpower-change` 是文件/行为变更、Review-and-fix、OpenSpec
  准入、Superpowers 执行路由和整个任务最终完成的 owner。
- `codex-brief-antigravity-review` 只负责非状态改变的 prompt/Brief 文案、
  普通只读 Review，以及已有有效 Handoff 后的外部批次治理。

统一闭环为：

```text
合同/方案 -> 当前 revision Preflight Review
-> 实施 -> 验证 -> 实施 Review
-> finding 则修正、重新验证、重新 Review
-> 持久化 final verification -> final Review
-> OpenSpec tasks 对账/归档/严格验证 -> 完成
```

不需要用户每次重复强调该循环；只要进入状态改变型工作，Skill 应按风险与
证据 profile 自动执行。轻量、只读、非状态改变任务不进入重流程。

## Review 发现与修正

1. **触发重叠**：两个 Skill 曾同时覆盖 Review、Brief 和外部协作。
   已用 frontmatter 与正文双向排除 file edit、Review-and-fix、workflow
   template change 和 final completion。
2. **Direct Change 口径冲突**：局部恢复被一律降为 compact。
   现改为 profile-aware；只有低风险 Direct 默认 compact，批准合同下的
   public/API restoration 仍为 strict。
3. **Preflight 语义重复**：曾与设计审批、实施 Review 混淆。
   现只检查可执行性，结果仅 PASS/BLOCKED；任何 finding 都先修订再重审。
4. **证据可伪造或复用**：仅有状态字符串、路径或哈希不足以证明当前
   batch/attempt。Schema 3 的四个 artifact reference 现在指向内嵌 schema-1
   manifest 的文件，绑定 role、result、change、batch、attempt、来源
   canonical revision/SHA-256。
5. **状态机可绕过**：对抗 Review 曾复现无 Review promotion、替换被审
   Report、原子化 final gate、blocked tuple 跳变、旧 attempt 复用等路径。
   validator 与回归测试现逐项拒绝。
6. **单快照 complete 不可信**：`complete` runtime validation 现在强制
   `--previous-status`，核对真实 prior canonical revision/hash 与 transition。
7. **OpenSpec/Superpowers 重复**：OpenSpec 是唯一批准设计合同；
   Superpowers 负责 discovery/plan/TDD/debug/review/verification discipline，
   不再生成同一决策的第二份审批文档，也不自行授予 Git 权限。

## 最终路由

| 场景 | 主入口 | OpenSpec | Superpowers | Handoff |
|---|---|---:|---|---:|
| prompt/Brief 文案、普通只读 diff/Report Review | Brief standalone | 否 | 否 | 否 |
| Review 并修复、文件或行为变化 | Change Gate | 按合同边界 | 按变更类型 | 仅外部执行 |
| 低风险、合同已定义的内部恢复 | Direct Change | 否 | TDD/debug/verify 按需 | 外部时 compact |
| approved public/API 纯恢复 | Direct Change | 不新建 | strict review/verify | 外部时 strict |
| 新能力、API/schema/security/lifecycle/workflow | OpenSpec proposal | 是 | 批准后执行 | 外部时需要 |
| 已有有效 status 的 dispatch/resume/Report Review | Brief handed-off | 沿用 | 批次 Review 不重复 | 是 |
| whole-task final completion | Change Gate | 对账并归档 | verification-before-completion | 消费已有证据 |

## Evidence 与状态约束

- Schema 3 只适用于 Handoff-backed 外部执行；inline compact 不创建 Handoff。
- `ready-for-review` 的决策必须保留被 Review 的同一 Report reference。
- Preflight/timeout artifact 只能用于 batch BLOCKED，不能替代 batch PASS。
- final verification 先形成独立 revision，final Review 后才可 complete。
- final BLOCKED 恢复和 blocked self-transition 不得改写已接受证据。
- 引入新 artifact 的 proposed transition 应在项目外临时生成，并以当前唯一
  canonical status 作为 `--previous-status` 验证后再原子替换。
- generic inline Step Evidence template 不嵌入 Handoff manifest；外部 final
  verification 使用独立模板，避免轻量任务被重流程污染。

## 与全局规则协同

- 当前用户指令 > 项目 `AGENTS.md` > 用户级全局规则；更具体约束优先。
- `AGENTS.md` 提供仓库验证和 no-push-without-approval 边界。
- OpenSpec 管 what/why/acceptance/approval；Superpowers plan 管 how。
- TDD 微步骤不逐个走 Evidence Gate；完整 business slice 才签收。
- Plan/Brief 不产生 Git 权限。当前 `main` 使用与最终 commit/push 权限来自本次
  用户明确指令，并已在 implementation plan Preflight 中持久化。

## 验证与回滚

- 两仓 source unittest：OpenSpec `53/53`，Brief `48/48`。
- 两仓 source/runtime validator 与 `quick_validate.py`：PASS。
- 26 个 source/runtime 关键文件 byte-identical：PASS。
- OpenSpec change 已归档；归档后 `--all --strict`：`1/1 PASS`。
- 对抗用例覆盖 role/result、batch/attempt、source fingerprint、unsafe path、
  hash、symlink、blocked recovery 与 previous-status transition。
- 两仓实施提交 push/tracking 确认后，临时结构化回滚备份已移入系统废纸篓，
  runtime `.DS_Store`、测试副本和 Python cache 已清理。

## 已接受信任边界

`--previous-status` 机械证明当前 transition 的最后一跳，不递归证明全部历史。
流程信任替换前 canonical prior state 未被 governor 重写，并保留每一跳 validator
PASS 输出和仓库历史。若威胁模型包含能够同时伪造 prior state 与全部 artifacts
的恶意本地 actor，需要 append-only journal 或签名锚；这会显著加重流程，不在本次
轻量 Skill 优化范围内。

## 待办

- 无未决设计或实现项。OpenSpec 归档、Git publication 与临时备份清理属于
  本次执行 closeout，其结果记录在归档历史和最终用户报告中。
