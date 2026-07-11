# Cross-CLI Skill Governance Design Closeout

文档类型：Major Self-Evolution Design / Closeout Record
日志及版本：2026-07-11 v5（archived；Final Review PASS；local closeout complete）

## Contract

- OpenSpec change：`align-cross-cli-skill-governance`
- Source of truth：本仓库与 `codex-brief-antigravity-review`
- Evidence profile：`standard`
- Decision owner：Codex
- Required runtime targets：Codex、Antigravity CLI、Grok CLI

## Implemented design

- Handoff schema 4 绑定 `executor_agent`、`independent_reviewer_agent` 与
  `decision_owner: codex`；schema-1 evidence manifest 绑定 producing agent
  identity/role。
- Standard/strict 外部执行禁止 executor 自审；辅助 CLI 的 PASS 仅作为建议
  证据，不能推进 canonical state 或声明完成。
- `references/cross-cli-portable-manifest.json` 只声明便携 allowlist；同步拒绝
  credential、token、session、history、log、cache、model/settings、hook、MCP、
  binary、private-key 等类别。
- `scripts/validate_cross_cli_sync.py` 提供 `plan`、`apply`、`verify`、
  `verify-all`、`verify-discovery`、`audit`；支持路径/哈希计划、防篡改绑定、
  首次安装、0600 rule backup、原子替换与失败回滚。
- 三端全局规则仅安装/替换一个 versioned managed block；`CCG-001` 至
  `CCG-008` 保持语义一致，marker 外原生字节不被覆盖。

## Current evidence

- 五个修正后的 forward-test ID 可独立执行。
- 新增首次 Skill 安装、零 marker managed block、事务回滚、CLI round-trip
  与 plan tamper rejection 测试。
- 隔离 runtime 已完成 `plan -> apply/verify -> verify-all` 回环。
- 三端均同步 31 个 portable files，`verify-all` PASS；12 条 installed
  validators 全部 PASS。
- Grok `inspect --json` discovery PASS；mode `0600` inspect artifact 已消费。
- 三份 managed governance block 均只有一个 version-1 marker pair，body
  SHA-256 为 `407364aa62eba67c962e7ace22d6a834593a9c5a330907bf8617ea93b03e32ca`，
  原生规则前缀字节保持。
- Antigravity attempt 1 因 stale `agents/openai.yaml` 暴露 manifest target
  缺口；该 target 已按 secure backup 完整回滚。TDD 修正 metadata target 后，
  attempt 2 的 parity、installed validators 全部 PASS。
- 4 个 discoverable Antigravity 历史 backup 目录经 containment/non-symlink
  dry-run 和用户明确授权后，已移出 Skill discovery root。
- Pre-archive Review 发现 manifest 自身未触发 sync gate；新增 RED 后修复
  `classify_sync_trigger()`，三端使用独立 correction backup root 重新同步，
  installed validators、Grok discovery 与 `verify-all` 再次 PASS。
- Archive 前完整两仓 diff/scope/sensitive Review PASS；真正 Final Review 仍在
  archive 后执行。

## Pending gates

- 无本次 Change 阻塞项。
- 用户明确选择本地闭环；`git add`、commit、push 均未执行，未来如需发布，
  作为独立 Git 任务重新授权。

## Rollback

- 临时结构化备份曾位于：
  `/private/tmp/cross-cli-skill-sync-major-20260711`。
- 任一 target apply 失败时只恢复该 target 已替换文件，并移除本事务新建的
  文件和空目录；后续 target 不执行。
- Final Review PASS 后，用户明确授权本地闭环和清理；临时目录已删除并确认
  原路径不存在。长期回滚来源为后续 Git 历史或重新生成的受控 source diff。

## Final closeout evidence

- Archived change：
  `openspec/changes/archive/2026-07-11-align-cross-cli-skill-governance`
- Archive 后 strict validation：1 passed、0 failed。
- Final source/runtime matrix：主仓库 97 tests、Companion 55 tests、三端
  `verify-all` 与 installed validators PASS。
- Final sensitive audit：`0 sensitive categories found`；两仓
  `git diff --check` PASS；Final Review PASS。
- Publication decision：user-approved local closeout；未执行任何 Git staging、
  commit 或 push；temporary backup root cleanup PASS。
