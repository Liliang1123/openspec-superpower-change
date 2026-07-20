# Adversarial Implementation Review: streamline-workflow-prompt-contracts

- **文档类型**: Code / Implementation / Evidence Review（只读对抗性）
- **日志及版本**: 2026-07-20 / session-adversarial-review-paused-impl
- **结论**: **需修改**（Combined: **FIX BEFORE CONTINUE**）
- **验证范围**:
  - OpenSpec: `proposal.md` / `design.md` / `tasks.md` / `specs/skill-workflow-governance/spec.md`
  - Plan: `docs/superpowers/plans/2026-07-17-streamline-workflow-prompt-contracts.md`
  - Evidence: `docs/design/evidence/2026-07-17-companion-prompt-load.md`
  - Worktrees: Router / Companion / Superpowers (`streamline-workflow-prompt-contracts`)
  - 只读命令: `git status` / `git diff` / `git diff --check`；Superpowers `node --test` + `quick_validate`；Router focused unittest + `validate_core_gates` + `openspec validate --strict`；Companion focused unittest + `validate_templates` + `py_compile`
  - **未**修改任何实现文件；**未** commit/push/sync/archive

---

## Verdicts

| Track | Verdict |
|---|---|
| 1. Approved design | **PASS** |
| 2. Superpowers 已实施部分 | **CONDITIONAL PASS** |
| 3. Router 已实施部分 | **CONDITIONAL PASS** |
| 4. Companion 当前 RED 半成品 | **INVALID RED** |
| 5. Combined implementation | **FIX BEFORE CONTINUE** |

---

## 问题与风险（Findings-first）

### F-01 — Completion Contract 遗漏原 whole-task 义务（语义削弱）

- **Severity**: P0
- **对象**: Router
- **位置**:
  - `references/completion-contract.md` L7–L73（整份 canonical）
  - 对比 `HEAD:references/approved-implementation-workflow.md` Final Completion / OpenSpec closeout 原清单
  - 对比当前 `SKILL.md` L142–L148 vs `completion-contract.md` L41–L44
- **事实**:
  - Canonical 被声明为“唯一规范性 whole-task checklist”，但缺失或弱化了原清单中的稳定义务：
    - 未点名 `final_critical`、hashed evidence manifest、`--previous-status` 完成转移
    - 未要求 final Review 覆盖 tests/logs、sensitive information、temporary files、unrelated changes
    - 未要求调用 `superpowers:verification-before-completion`
    - 未保留 “chat-only summary is not durable promotion”
    - OpenSpec 侧未显式要求 reconcile `tasks.md` / update design-closeout docs
  - Learning 从 SKILL 的“implementation Review PASS 后、final verification 前 **run** Project Learning Closeout”弱化为 canonical 的 “**when** its threshold is met or the user explicitly requests”
- **为何违规**:
  - 批准 design/spec 要求 dedup **不削弱** completion；canonical 是唯一权威后，遗漏即门禁削弱
  - SKILL 与 canonical 对 Learning 触发条件表述不一致，构成多权威源
- **最小修复**:
  - 把原 Final Completion + OpenSpec closeout 的可验证义务完整迁入 `completion-contract.md`（结果导向表述可，但义务不得丢）
  - Learning 与 SKILL 对齐为：Review PASS 后进入 closeout；mandatory promotion / explicit archive-and-distill 才阻塞 completion
  - Secondary 只保留 pointer + route-specific 证据，不得保留更强/更弱的 whole-task 规则
- **修复后验证**:
  - 对照 `git show HEAD:references/approved-implementation-workflow.md` 义务矩阵 diff
  - `python3 -m unittest ...test_completion_contract...` + `validate_core_gates.py .`
  - 人工确认 secondary 无第二套 whole-task checklist
- **阻塞继续实施**: **是**（应先修 Router canonical，再推进 Companion GREEN）

### F-02 — prompt-collision “测试”是 fixture 自证，不是 forward-test

- **Severity**: P0
- **对象**: Router
- **位置**:
  - `tests/fixtures/prompt-collision-cases.json` L1–L32（含 `expected` 字段）
  - `tests/test_workflow_rules.py` L340–L360（`assertEqual` 对 fixture 内 `expected`）
- **事实**:
  - 测试只校验 JSON 里写着的 expected 与硬编码 dict 一致，并确认 skill/adapter 文本里存在若干短语
  - 未对 raw prompt 跑隔离路由/agent，也未观察 Gate 0 / Preflight / HARD-GATE 行为
  - CHANGELOG 已写 “Add paired prompt-collision fixtures…”；OpenSpec/tasks 4.2 与 design §4 要求的是 **无 expected-answer leakage 的 forward-tests**
- **为何违规**:
  - 批准范围第 4 项与 spec “Measured prompt-load and prompt-collision evidence” 要求可观察行为证明
  - 当前 GREEN 会产生伪证明：fixture 自洽 ≠ 路由正确
- **最小修复**:
  - 保留 fixture 仅作场景目录（可去掉或隔离 `expected`，避免 leakage）
  - 增加 raw forward scenarios：proposal-only / material brainstorming / unauthorized Git / authorized Git / selected HARD-GATE；只断言可观察输出
  - 文档区分 “static contract inventory” vs “forward-test PASS”
- **修复后验证**:
  - 独立 runner/agent 对 5 场景 raw prompt 的可观察结果
  - 全量 unittest + 明确记录哪些仍为 static
- **阻塞继续实施**: **是**（可并行于 Companion，但不得宣称 collision 已 GREEN）

### F-03 — Companion RED 以错误原因失败（INVALID RED）

- **Severity**: P0
- **对象**: Companion
- **位置**:
  - `tests/test_workflow_rules.py` L192–L204（`## Common Boundaries` 先失败）
  - `scripts/validate_templates.py` L1200–L1205（同样要求 `## Common Boundaries`）
  - 当前 `SKILL.md` 使用 `## Non-Negotiables`（约 L160），**不存在** `## Common Boundaries`
  - 真实缺陷 `### Artifact Paths` 等在 `SKILL.md` L80+，但 thin-entry 测试从未执行到 `assertNotIn`
- **事实**:
  - `py_compile` 通过；语法完整
  - focused tests: 2 FAIL
    1. `test_thin_entry...` → `AssertionError: '## Common Boundaries' not found`（测的是未来 GREEN 标题，不是当前缺陷）
    2. `test_handoff_governor...` → governor 文件缺失（**有效 RED**）
  - `validate_templates.py .` → `missing required file: .../handed-off-external-execution.md`（**有效 RED**）
  - 脆弱断言：`split(...).rsplit(...).__str__().lower()` 判断 pointer 附近有 `read`（L197–L199）
- **为何违规**:
  - 有效 RED 应证明“薄入口未完成 / governor 缺失 / 仍内嵌 governor 细节”
  - 当前 thin-entry 测试被错误前置条件短路，不能保护路由隔离
  - plan Task 6 写的是 “common authority/Git boundaries”，不是强制 `## Common Boundaries` 标题
- **最小修复**:
  - RED 断言改为：缺 pointer、仍含 `### Artifact Paths` / `### State Machine` / `## Evidence Profiles`、缺 governor 文件
  - 共享边界可断言 Non-Negotiables/Git 禁止短语，或在 GREEN 时再引入 `## Common Boundaries`
  - 删除 `.__str__()` 附近性启发式；改为显式 “when Handoff route selected, read `references/handed-off-external-execution.md`” 契约句
  - 重新跑 RED 并保存失败原因
- **修复后验证**:
  - 仅跑两个 focused tests：失败原因必须是 thin 结构/内嵌细节/缺 reference
  - `validate_templates.py .` 以缺 reference 或内嵌细节失败，非 SyntaxError
- **阻塞继续实施**: **是**（先修 RED 再 GREEN）

### F-04 — tasks.md 2.4/2.5 过早勾选；进度账本失真

- **Severity**: P1
- **对象**: Plan / Evidence / Combined
- **位置**:
  - `openspec/changes/streamline-workflow-prompt-contracts/tasks.md` L16–L17（2.4/2.5 `[x]`）
  - 同文件 L13–L15、L21–L25（2.1–2.3、3.x 仍 `[ ]`，但 Superpowers/Router 已 GREEN 一轮）
  - Evidence `docs/design/evidence/2026-07-17-companion-prompt-load.md` L30–L80：仅 standalone Grok `observed`；Handoff load 明确 post-implementation；Antigravity `UNKNOWN`
- **事实**:
  - 2.4 要求 standalone/**Handoff** load evidence on each **observable** runtime；Handoff 正向加载证据尚未捕获
  - 2.5 “Review the decision” 无独立 decision Review 工件（仅有 evidence 文档 + plan Preflight 叙事）
  - Superpowers Option 2 与 Router Completion 已落地，但 2.1–3.2 未勾选
- **为何违规**:
  - 过早完成勾选会误导后续 agent 跳过 Handoff load / decision review
  - 进度账本与 worktree 现实不一致，增加半成品误判风险
- **最小修复**:
  - 2.4 改回未完成，或拆分为 2.4a standalone done / 2.4b Handoff forward after GREEN
  - 2.5 保持 checked 仅当有可引用的决策 Review；否则 unchecked + 记录 thin-reference 为 provisional
  - 同步勾选已真实完成的 2.1–2.3 / 3.1–3.2（在证据齐全后）
- **修复后验证**: tasks 与 plan checkbox 对照 `git status` 与测试证据
- **阻塞继续实施**: **是**（账本修正成本低，应先做）

### F-05 — Secondary 仍保留 whole-task 完成语义（双权威残余）

- **Severity**: P1
- **对象**: Router
- **位置**:
  - `SKILL.md` L142–L148（Learning 完整规范性段落仍在 entry body）
  - `references/approved-implementation-workflow.md` L85–L105（仍含 `final_critical`、`--previous-status`、`verification-before-completion` 等 whole-task 过程）
  - `references/step-evidence-gate.md` L45–L57（Gate 2 仍有 `Completion claim allowed: yes/no`）
  - Validator `scripts/validate_core_gates.py` L1281–L1310 只检查 pointer + canonical needles，**不**检测 secondary 冲突清单
- **事实**:
  - 设计允许 concise safety + route-specific evidence；当前 secondary 仍可独立驱动完成判断
  - Spec scenario “secondary artifact diverges” 无机械检测
- **为何违规**:
  - 批准目标是单一权威；现状为 pointer + 残留 checklist 并存
- **最小修复**:
  - SKILL Learning 改为 pointer + 一句不弱于 canonical 的提醒，细节只在 canonical
  - approved Final Completion 仅保留 Handoff/route 机制指针，不重复 whole-task 成功条件
  - Gate 2 明确 “slice evidence only；whole-task claim 禁止在此签字” 或移除 `Completion claim allowed`
  - Validator 增加：secondary 不得出现独立 “whole-task checklist” 标题/编号完成清单（允许 pointer 句）
- **修复后验证**: `validate_core_gates` + 人工对照三 secondary
- **阻塞继续实施**: **是**（与 F-01 同批修）

### F-06 — Superpowers 缺少上游覆盖防护

- **Severity**: P1
- **对象**: Superpowers / Combined
- **位置**:
  - `skills/finishing-a-development-branch/SKILL.md`（已修 Option 2）
  - `tests/finishing-branch-policy.test.js`（仅文案契约）
  - `package.json` version `5.0.7`；origin `github.com/obra/superpowers`
  - design Risks: “Superpowers update overwrites the Option 2 correction → Track source provenance/hash”
- **事实**:
  - 语义修复正确：Option1 cleanup；Option2 preserve；Step5 `1 and 4`；QR/Red Flags 一致
  - `node --test` PASS；`quick_validate` PASS
  - 无 upstream commit/hash/path provenance 记录，无 Router 侧 pin 或 sync 回归
- **为何违规**:
  - 批准 design 已识别上游覆盖风险；未落地则 Option 2 修复可被静默冲掉
- **最小修复**:
  - 在 Router change evidence 或 Superpowers worktree 记录：skill 路径、修订前/后 SHA-256、upstream repo/version/commit
  - 回归测试纳入 Router/combined 校验清单或 portable sync check
- **修复后验证**: 记录 hash；重跑 Node test；sync checklist 引用
- **阻塞继续实施**: **否**（不阻塞 Companion GREEN，但阻塞最终 completion）

### F-07 — Superpowers 测试未覆盖全部活跃矛盾面且偏脆

- **Severity**: P2
- **对象**: Superpowers
- **位置**: `tests/finishing-branch-policy.test.js` L18–L31
- **事实**:
  - 覆盖 Option2 / Step5 / QR row / Red Flags
  - 未断言 Option1 仍为 Cleanup；未断言 Common Mistakes 段；未断言 Integration “using-git-worktrees cleans up” 是否需限定选项
  - 大量精确 Markdown 文案匹配
- **为何风险**: 文案微调可假红；Option1 回归（曾误改）无直接保护
- **最小修复**: 增加 Option1 cleanup 断言；可选稳定语义 token 而非整表 row
- **修复后验证**: `node --test tests/finishing-branch-policy.test.js`
- **阻塞继续实施**: **否**

### F-08 — 范围外 CONTEXT.md 未跟踪产物

- **Severity**: P2
- **对象**: Router / Combined
- **位置**: worktree 根 `CONTEXT.md`（untracked，约 43 行 glossary）
- **事实**: Non-Goals 明确不重做 CONTEXT.md 分层；该文件不在五项批准范围
- **为何风险**: 范围扩张 / 与 Non-Goal 摩擦；后续误 commit
- **最小修复**: 移出 change 范围或标明非本 change 交付；不纳入 completion
- **阻塞继续实施**: **否**（勿纳入本 change 合并）

### F-09 — Companion governor 针测过浅，移动后仍可能漂移

- **Severity**: P2
- **对象**: Companion
- **位置**: `tests/test_workflow_rules.py` L205–L216；`validate_templates.py` L1210–L1217
- **事实**: 仅 `assertIn` 短针；无对当前 SKILL Handed-off 段的 hash/全文 parity；无 “batch PASS ≠ final completion” 强约束句
- **最小修复**: GREEN 时用从 SKILL 切出的全文/规范化 hash 与 reference 对齐，或结构化段落清单 + 禁止句
- **阻塞继续实施**: **否**（GREEN 时必须加强）

### F-10 — README/CHANGELOG 未超 token 声称，但 collision 表述易被高估

- **Severity**: P3
- **对象**: Router
- **位置**: `CHANGELOG.md` Unreleased；`README.md` Completion Contract 行
- **事实**: 无 bytes/token 伪结论；collision 写的是 fixtures 而非 measured runtime savings
- **风险**: 读者可能把 fixtures 当成 forward-test 完成
- **最小修复**: 明确 “static fixtures; forward-tests pending/pass”
- **阻塞继续实施**: **否**

---

## 预期 RED / 计划内未完成（非 finding）

| 项 | 分类 | 说明 |
|---|---|---|
| Companion 缺 `references/handed-off-external-execution.md` | 预期 RED | 计划 Task 6/7；`validate_templates` 与 governor 测试因此失败是合理的 |
| Companion SKILL 仍内嵌 Handed-off 细节 | 计划内 | GREEN 前应保留；但 RED 测试应**直接**断言此点 |
| tasks 3.3–3.5 / 4.x / 5.x / 6.x | 计划内未完成 | 实施暂停点 |
| Antigravity load `UNKNOWN` | UNKNOWN | evidence 正确未推断 token |
| Handoff route load forward-test | 计划内 | evidence 已声明 post-impl |
| Runtime sync / archive / final completion | 明确禁止本 Review 执行 | 未做 |

---

## 复验证据摘要

### Superpowers

```text
node --test tests/finishing-branch-policy.test.js  → 1 pass
quick_validate.py skills/finishing-a-development-branch → Skill is valid
diff: Option2 Then cleanup→preserve; Step5 1,2,4→1 and 4; Options 2 and 3 keep
Option1 Then: Cleanup worktree 仍在
```

### Router

```text
3 focused tests PASS
validate_core_gates.py . PASS
openspec validate streamline-workflow-prompt-contracts --strict PASS
git diff --check clean
```

### Companion

```text
py_compile scripts/validate_templates.py tests/test_workflow_rules.py → OK
2 focused tests FAIL (Common Boundaries; missing governor)
validate_templates.py . → missing handed-off-external-execution.md
```

---

## 对 20 个 Review 问题的简答

1. **范围**: 主体落在五项内；`CONTEXT.md` 与过早任务勾选有扩张/账本问题。
2. **Non-Goals**: 未见 Learning 系统重做、grill/caveman/schema5 重设计；**completion 义务有削弱风险（F-01）**。
3. **thin-reference 证据**: 在 design 表下 **provisional 可接受**（Codex documented + Grok standalone 无 eager ref + Antigravity UNKNOWN 不 claim savings）；**不足以勾选“含 Handoff load 的 2.4 完成”**。
4. **2.4/2.5**: **过早**（F-04）。
5. **唯一权威**: 名义上是；实际上 canonical 不全 + secondary 残留 → **尚未真正唯一**。
6. **去重遗漏**: **是**（F-01）。
7. **secondary**: 必要安全冗余不足，**仍像多权威**（F-05）。
8. **validator**: 独立 `read(completion-contract.md)` + pointer；**非拼接自证**，但是 **浅层 needle**，检不出语义削弱。
9. **fixture**: **是静态契约自证**，不能替代 forward-tests（F-02）。
10. **还需 raw forward**: proposal-only；material→brainstorming+HARD-GATE；unauthorized Git BLOCKED/rewrite；authorized Git 不误拒；standalone 不进 Handoff；valid Handoff 加载完整 governor；Option2 preserve（已有 Node）。
11. **Git 正反**: fixture 目录有配对，**无行为证明**；adapter 文本仍有 never-grants / explicit authorize。
12. **proposal-only / brainstorming / HARD-GATE**: 同 F-02。
13. **Option2**: **一致**；Option1 已恢复；未改 push/PR/discard/force-push 门禁。
14. **上游覆盖**: 需 path + content hash + upstream commit/version + 可重复回归（F-06）。
15. **Companion RED patch**: 语法完整；**thin-entry 失败原因错误** → INVALID RED；governor 缺失失败有效；`read` 附近启发式脆弱。
16. **薄 SKILL 保留**: Route Selection、Standalone、共享 Non-Negotiables/Git、模板指针、Maintenance；**完整下沉**: Handed-off body（Artifact Paths、State Machine、Evidence Profiles、身份绑定、Preflight/High Review、correction loop、batch≠complete）。
17. **防漂移**: 迁移后全文/hash parity + 结构化 needle + forward-test valid Handoff。
18. **docs/manifest**: Companion README/README_cn/CHANGELOG + Router portable manifest 增加新 reference；**禁止**未测 token 节省（evidence 已遵守）。
19. **计划/tasks**: 需修正 RED 断言与 tasks 勾选；design 本身 **不必 redesign**。
20. **下一步最小顺序**: 见下。

---

## 按依赖排序的最小修复清单

1. **修正 Companion RED**（F-03）：失败原因对准内嵌细节/缺 pointer/缺 governor；去掉脆弱 `read` 启发式。
2. **修正 tasks 账本**（F-04）：取消过早 2.4/2.5 完成声明；标记 Handoff load pending。
3. **补全 Completion Contract 义务并对齐 secondary**（F-01 + F-05）。
4. **加强 Superpowers 回归与 provenance**（F-07 + F-06，可与 3 并行）。
5. **Companion GREEN**：创建 governor reference（从现 SKILL 无损迁移）+ 薄入口 + README_cn/CHANGELOG + Router manifest。
6. **Raw prompt-collision / route-load forward-tests**（F-02 + design cases 6–7）。
7. **再 Review** → 全量校验 → 才允许 sync/archive 讨论。
8. **CONTEXT.md** 移出本 change 或单独决策（F-08）。

---

## 摘要

- 批准设计（五项 + Non-Goals + evidence 层级）**本身可 PASS**。
- Superpowers Option 2 **功能修复正确**，缺 provenance 与更强回归。
- Router Completion **结构方向正确**，但 canonical **义务不全** + Learning 措辞弱化 + secondary 双权威 + collision 伪 GREEN → **CONDITIONAL PASS / 继续前必修**。
- Companion **半成品语法可用**，但 thin-entry RED **无效对准** → **INVALID RED**。
- Combined: **FIX BEFORE CONTINUE**。
- 未发现 bytes/4 token 伪结论；evidence 对 Antigravity UNKNOWN 处理合规。
- 本 Review **不是** final completion，**不是** runtime sync 授权。
