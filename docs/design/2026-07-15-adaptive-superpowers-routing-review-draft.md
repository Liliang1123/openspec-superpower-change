# 自适应 Superpowers 路由 Self-Evolution Review Draft

文档类型：Major Self-Evolution 审查草案  
拟议 change-id：`make-superpowers-routing-adaptive`  
状态：仅用于 OpenSpec 提案；未获准实施

## 观察到的问题

当前工作流已经避免了两类明显重复：OpenSpec 是唯一设计合同，
`codex-brief-antigravity-review` 的 standalone 路径也不创建 Handoff 或
Superpowers plan。现行 RED 基线仍暴露一个比例失衡点：

1. 对“创建 proposal/spec/design/tasks”的 proposal-only 请求，通用的“创建/修改”
   语义会让 `superpowers:brainstorming` 提前介入。
2. 示例 endpoint 没有给出 method、鉴权、payload、默认值、错误与兼容策略时，
   当前路径会逐项提问、比较 2–3 个方案并等待确认；这些步骤有设计价值，但在
   OpenSpec 本身仍是待审批草案时，全部采用 HARD-GATE 交互会产生明显 ceremony。
3. 风险 profile、任务阶段和 Superpowers 激活条件没有被充分分离。公共 API 使
   后续实现保持 `strict`，不等于 proposal 草拟阶段必须自动进入完整执行纪律。
4. Companion skill 的 standalone review 已经较轻；它的问题不是强制触发，而是
   还可以更明确地禁止在 change 产出后自动串联 Review，并固定默认 brief 结构。

上述判断不依赖具体模型名称。更强的模型可以减少澄清成本，但不能替代 OpenSpec
批准、真实验证、Review 或用户控制边界；用 `GPT-5.x` 等名称直接分支也会造成
脆弱且不可审计的授权规则。

## 期望行为

- 用任务阶段、未决决策和风险决定 Superpowers 子技能，而不是用通用“创建/修改”
  词或具体模型版本决定。
- proposal-only 请求先读取仓库事实；已充分定义时直接生成 OpenSpec 草案并 strict
  validate，不触发 brainstorming、writing-plans、TDD 或 implementation Review。
- 对可逆且会在 OpenSpec 审批中显式呈现的缺省项，允许记录有界假设；只有影响
  scope、安全、兼容、数据生命周期或可验收性的实质未决问题才进入 brainstorming。
- 一旦 brainstorming 确实适用，保留其 HARD-GATE，并把结论写入同一 OpenSpec
  design/spec delta；不创建第二份设计合同或第二次设计审批。
- 获批后的多 slice、strict 或外部实现继续使用现有 plan、TDD、Preflight、Review、
  evidence 和 verification 门禁；本变更不以“模型更强”为理由削弱完成条件。
- `codex-brief-antigravity-review` 只在用户明确请求 standalone wording/read-only
  Review，或已有有效 Handoff 时触发。Standalone 默认只输出 scope/evidence、
  actionable findings、verdict/next action，不复述整套治理流程。

## 方案比较

### A. 全局禁用 Superpowers

开销最低，但会同时移除高风险实现中的 TDD、Review 和完成前验证，不满足项目
Non-negotiables，拒绝采用。

### B. 按模型版本启停

能直接回应 GPT-5.6 的体验，但模型名称不等于风险或授权能力，升级后还会再次漂移，
并与 capability-profile 规则冲突，拒绝采用。

### C. 按阶段、歧义和风险自适应激活（推荐）

proposal 草拟、已批准实现、standalone review 和 handed-off execution 分开判定；
只在存在具体未决设计或执行风险时加载对应 Superpowers 子技能。这样保留治理价值，
同时去掉由宽泛触发词造成的 ceremony。

## 拟修改文件与精确规则方向

### `openspec-superpower-change`

- `SKILL.md`
  - 在 Superpowers Mapping 前增加 phase-aware activation 规则。
  - 明确“列出 `none` 的子技能不得仅因通用创建/修改语义再次触发”。
- `references/proposal-workflow.md`
  - 增加 proposal-only 快路径、仓库事实优先和有界假设条件。
- `references/superpowers-adapter.md`
  - 明确 selective invocation；被选择后仍完整遵循对应 skill。
- `references/request-modes.md`
  - 将 OpenSpec proposal 与 approved implementation 的子技能边界写成可判定规则。
- `references/shared-global-governance.md`
  - 增加稳定 invariant：governed work 先由 change gate 完成 phase classification，
    再选择 Superpowers 子技能；通用创建/修改语义不得抢先触发。
- `references/cross-cli-portable-manifest.json`
  - 提升 managed-rule version 并声明新 invariant ID，确保三端规则先于 skill 正文生效。
- `scripts/validate_cross_cli_sync.py`
  - 允许 managed-rule version 3 精确绑定 CCG-001..CCG-014，同时保留历史版本。
- `tests/test_workflow_rules.py`
  - 先写 RED 断言，再加入最小规则文本；覆盖 proposal-only、material ambiguity、
    no model-name routing、implementation gates preserved。
- `examples/openspec-change.md`、`README.md`、`README_cn.md`
  - 对齐用户可见示例与说明。

建议核心规则片段：

```text
Generic create/modify wording SHALL NOT activate a Superpowers sub-skill by
itself. Gate 0 selects sub-skills from the current phase, unresolved material
decisions, and implementation risk.

For proposal-only work, inspect repository facts first. If the contract can be
drafted with explicit bounded assumptions, create and validate the OpenSpec
artifacts without brainstorming. Invoke brainstorming only for a material
unresolved choice that changes scope, security, compatibility, data lifecycle,
or testable acceptance. Once invoked, keep its HARD-GATE intact.
```

### `codex-brief-antigravity-review`

- `SKILL.md`
  - 明确 standalone Review 不因 change 产出自动串联；必须有当前请求。
  - 增加 OpenSpec artifact 的 brief checklist：proposal scope、spec scenarios、
    design decisions/risks、tasks traceability、跨 artifact 一致性。
- `tests/test_workflow_rules.py`
  - 覆盖 request-scoped trigger、brief 默认输出和 handed-off path 不变。
- `README.md`、`README_cn.md`
  - 对齐公开说明。

建议核心规则片段：

```text
Do not auto-chain Standalone Lightweight Review after producing a change.
Use it only for the current explicit wording/read-only-review request. Keep the
default response findings-first and omit governance narration unless it changes
the result or next action.
```

### 合同与同步文件

- `openspec/changes/make-superpowers-routing-adaptive/{proposal.md,design.md,tasks.md}`
- `openspec/changes/make-superpowers-routing-adaptive/specs/skill-workflow-governance/spec.md`
- `references/cross-cli-portable-manifest.json` 不增加 portable path，但会提升 managed-rule
  version 并加入新的稳定 invariant ID。
- 获批并验证 source 后，同步两个 source repo、Codex runtime、Antigravity CLI 和
  Grok CLI 的 manifest-declared portable 文件。

## Validation 与 forward-test

实施必须按 writing-skills/TDD 走 RED -> GREEN：

1. 在两个仓库先加入失败的文本/路由契约测试并观察预期 FAIL。
2. 最小修改 skill/reference 使 focused tests GREEN。
3. 运行：

```bash
"${PYTHON_BIN:-python3}" "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" .
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_core_gates.py .
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

4. 在 companion repo 运行其 `quick_validate.py`、`validate_templates.py` 和 unittest。
5. 用隔离 fresh-agent 场景执行 GREEN forward-test：
   - fully specified proposal-only endpoint：不触发 brainstorming；
   - materially ambiguous endpoint：触发 brainstorming 且保留 HARD-GATE；
   - approved strict implementation：plan/TDD/Review/verification 不被跳过；
   - explicit standalone OpenSpec review：brief findings-first，无 Handoff；
   - change 产出后未请求 Review：不自动触发 brief skill。
6. 运行 cross-CLI plan/apply/verify-all；任一 required target stale/failed 即
   `BLOCKED`，不得声称全局优化完成。

## 备份与回滚

结构化临时备份：
`/private/tmp/adaptive-superpowers-self-evolution-20260715-103712/`。

实施或同步失败时，从该目录按相对路径恢复受影响 source/runtime；先验证恢复结果，
再决定是否继续。只有 source、runtime、forward-test、Review 和 cross-CLI 验证全部
通过后才清理备份。未得到用户明确命令时不执行 `git add`、commit、push 或破坏性 Git。
