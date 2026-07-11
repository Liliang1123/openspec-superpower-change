# 分层 Agent 协作治理设计与实施记录

- 文档类型：Major Self-Evolution Design / Implementation Record
- 日志及版本：2026-07-11 v1（source implementation；runtime/archive pending authorization）

## 背景与结论

本变更在不新增第三个总控 Skill、不绑定具体模型名的前提下，为现有两
Skill 协作增加稳定 capability profile、schema-5 实例身份、三层授权、
Confirmation Lease、Learning Candidate Pipeline 和 High Review。Router
仍是唯一控制面；executor/reviewer 结果仍是非权威证据。

## 核心设计

- `control-plane-high` 负责架构、批准、审计、promotion/archive/completion；
  `cohesive-medium` 和 `mechanical-low` 只执行封闭范围，遇歧义或越权即
  `BLOCKED`。
- schema 5 使用 `control_plane_owner`、`executor_assignment`、
  `independent_reviewer_assignment`，每个 assignment 分离 product、instance、
  role 和 profile；standard/strict 禁止同实例自审。
- schema-2 evidence 绑定 assignment 和 canonical revision/SHA-256；历史
  schema-4/schema-1 证据保持不可变。runtime 部署前 active-v4 必须为零。
- 工具/平台权限、scope/workflow 批准、business/production 批准互不替代。
  Lease 只在 revision/scope/risk/decision 均未变化时复用；`deferred/revoked`
  状态强制 `blocked`，旧 Lease 不可重新激活。
- 用户纠正先形成 Candidate Card；达到复现/高严重度阈值也只能提出
  Self-Evolution proposal，不能自动改全局 Skill。
- High Review 检查实际文件与完整 diff、copy/transform/production wiring、
  claim-to-mechanism、critical rerun 和独立 adversarial/business-chain probe。

## 实施与证据

- OpenSpec Change：`add-tiered-agent-collaboration-governance`，用户已明确批准。
- Plan：`docs/superpowers/plans/2026-07-11-tiered-agent-collaboration-governance.md` revision 2；Preflight PASS。
- 临时回滚根：`/private/tmp/tiered-agent-collaboration-major-20260711-134941`；
  全部门禁 PASS 后经用户明确授权删除，清理验证 PASS。
- RED：两仓库十个稳定场景各 `10 failures`；三项 hardening 各 `3 failures`。
- GREEN：router `113` tests PASS（显式 companion 路径下零跳过）；companion
  `69` tests PASS。项目 validators PASS。
- managed governance：version 2，`CCG-001` 至 `CCG-013`。

## 授权边界与待办

- runtime/global-rule write 已获授权并完成：Codex attempt-01 在 version-upgrade
  marker 处安全阻断并验证完整回滚；修复后 Codex attempt-02、Antigravity CLI、
  Grok CLI 均 apply/verify/installed-validation PASS，Grok discovery PASS。
- 三端 managed block 已从 version 1 升级到 version 2，原生块外字节保持不变；
  runtime sensitive audit 为 0。
- OpenSpec 已归档为
  `openspec/changes/archive/2026-07-11-add-tiered-agent-collaboration-governance`，
  主 spec 合并 7 项 Requirement，归档后 strict validation PASS。
- backup 已经明确授权并清理；`git add`、commit、push、merge 仍须分别明确授权。
- runtime apply 前必须重跑 schema-4 inventory；任何 active v4 都阻断部署。
