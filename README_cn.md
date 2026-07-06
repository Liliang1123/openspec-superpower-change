# openspec-superpower-change

[English](README.md) | [简体中文](README_cn.md)

`openspec-superpower-change` 是一个 Codex Skill，用作 AI 辅助工程任务的变更准入入口。它把项目本地规则、OpenSpec 变更合同、Superpowers 执行纪律和基于证据的验证门禁连接成一个可重复执行的工作流。

核心目标很简单：当工作可能影响运行时行为、公开合同、安全、持久化、工作流路由或运维可见行为时，AI Agent 不能从用户请求直接跳到代码实现。

## 亮点

- 在任何状态改变工作开始前先分类请求。
- 区分 Review-only、Discovery First、OpenSpec proposal、Approved implementation、Direct Change 和 Self-Evolution。
- 判断何时必须使用 OpenSpec，并在获批前阻止实现。
- 将已批准工作路由到 Superpowers 的计划、TDD、调试和验证流程。
- 要求在推进或声明完成前输出 Step Evidence Gate 证据。
- 提供受控的自我演进和本地/开源 Skill 同步规则。

## 为什么需要它

AI Coding Agent 很有用，但在生产级仓库里常见的失败模式也很明确：

- 未读取本地项目规则就开始实现；
- 把任务清单当成已批准合同；
- 用测试层证据声明运行时行为已经正确；
- 对 API、持久化、安全或工作流变更绕过 OpenSpec；
- 在修改治理 Skill 时削弱治理规则本身；
- 外部 Agent 交接后丢失审批状态和风险边界。

该 Skill 将这些风险转化为明确的门禁、参考文件和验证检查点。

## 体系定位

| 能力 | 职责 | 归属 |
|---|---|---|
| 本地项目规则 | 仓库约束、review 落盘、handoff、提交规范 | 项目 `AGENTS.md` / 本地文档 |
| OpenSpec | 变更合同、需求、场景、审批状态 | `openspec/` |
| Superpowers | 实施计划、TDD、调试、验证纪律 | Superpowers skills |
| Step Evidence Gate | 推进或声明完成前所需证据 | `references/step-evidence-gate.md` |
| openspec-superpower-change | 路由、风险分类、审批门禁、自我演进边界 | 本 Skill |

## 核心工作流

```text
读取本地规则
-> Gate 0 请求分类
-> 术语或边界不清时先 Discovery First
-> 合同或高风险行为变化时创建 OpenSpec proposal
-> 停下等待审批
-> 为已批准实现创建 Superpowers plan
-> 按 TDD / 调试 / 实施纪律执行
-> 通过 Step Evidence Gate 验证
-> 只有证据齐备后才允许声明完成
```

## 请求模式

| 模式 | 适用场景 | 是否改文件 |
|---|---|---:|
| Review-only | 用户要求评审、评估、批判、总结或生成提示词。 | 否 |
| Discovery First | 术语、参与者、生命周期或边界不清。 | 通常只改 glossary / context |
| OpenSpec proposal | 需要新增能力、行为合同、架构、安全、持久化、API 或工作流变更。 | 只改 proposal 产物 |
| Approved implementation | OpenSpec-backed proposal 已明确获批。 | 是，需先有计划 |
| Direct Change | 低风险恢复、拼写、格式、无行为影响文档、配置或既有行为测试。 | 是，范围受限 |
| Self-Evolution | 修改本 Skill、参考文件、校验器、示例或同步规则。 | 是，受门禁约束 |

## Gate 0

在编辑文件、运行状态改变命令、创建 proposal 产物或开始实现之前，Agent 必须说明：

1. 当前请求模式；
2. 已读取的参考文件，以及为什么足够；
3. 是否需要 OpenSpec；
4. 所需 Superpowers 子技能；
5. 风险级别、下一步动作，以及是否需要用户确认。

## OpenSpec 边界

以下场景必须使用 OpenSpec：

- 新功能或公开行为变化；
- API、schema、数据生命周期、持久化或迁移变化；
- 安全、沙箱、权限、跨租户行为或认证变化；
- Runtime 工具暴露、缓存策略、请求路由、Skill 路由或工作流生命周期变化；
- 改变系统边界的大范围重构；
- Skill 工作流变化。

只有在恢复既有预期行为、小型无合同影响配置变更、拼写/注释/格式修复、无行为影响文档更新，或为既有行为补测试时，才可以跳过 OpenSpec。

## 证据等级

| 等级 | 典型场景 |
|---|---|
| compact | 低风险文档、格式、配置或局部直接变更。 |
| standard | 默认的多步骤实现、评审和验证。 |
| strict | 安全、认证、公开 API/schema、持久化、迁移、部署、回滚或跨租户工作。 |

## 仓库结构

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
│   ├── self-evolution-rule.md
│   └── sync-checklist.md
├── scripts/
│   └── validate_core_gates.py
├── examples/
├── templates/
└── docs/
```

## 关键参考文件

- `references/request-modes.md`：工作模式与约束。
- `references/openspec-decision-rule.md`：何时必须使用 OpenSpec。
- `references/proposal-workflow.md`：proposal 创建与验证流程。
- `references/approved-implementation-workflow.md`：批准后的实施流程。
- `references/direct-change-rule.md`：低风险直接变更要求。
- `references/step-evidence-gate.md`：compact/full 证据模板。
- `references/self-evolution-rule.md`：修改本 Skill 的规则。
- `references/sync-checklist.md`：运行时副本与开源副本同步规则。

## 安装

复制或链接到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R openspec-superpower-change "${CODEX_HOME:-$HOME/.codex}/skills/openspec-superpower-change"
```

## 验证

修改 Skill 后运行：

```bash
python3 /Users/elvis/.codex/skills/.system/skill-creator/scripts/quick_validate.py /path/to/openspec-superpower-change
python3 /path/to/openspec-superpower-change/scripts/validate_core_gates.py /path/to/openspec-superpower-change
```

## 示例 Prompt

```text
Use openspec-superpower-change review-only mode. Read local rules, inspect this implementation plan, and report whether it requires OpenSpec. Do not modify files.
```

```text
Use openspec-superpower-change as the entry gate. Decide whether this requires Discovery First or an OpenSpec proposal before implementation.
```

```text
Use Direct Change mode. Confirm this restores intended behavior, make the smallest fix, run verification, and report evidence before claiming completion.
```

## 维护说明

- 不得削弱审批门禁、证据门禁或完成声明规则。
- 不得让 OpenSpec `tasks.md` 替代 Superpowers implementation plan。
- 不得让 `CONTEXT.md` 替代 OpenSpec proposal 产物。
- 不得用目录级覆盖同步运行时副本和开源副本；必须使用 sync checklist。

## License

MIT. See [LICENSE](LICENSE).
