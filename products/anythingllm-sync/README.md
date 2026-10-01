# AnythingLLM Sync

将 Obsidian 指定目录中的 Markdown 笔记同步到 AnythingLLM Workspace，用于检索与问答。

## Status — 2026-10-02

🧪 已实现，正在处理社区审核反馈；未确认进入社区插件目录。

## Current Features

- 创建、编辑、重命名自动同步；删除笔记时移除 Workspace 中的旧检索嵌入
- 防抖、内容哈希去重、批量同步及当前笔记手动同步
- 每个 Vault 独立配置与同步映射，API Key 存储在 Obsidian SecretStorage
- 已按社区反馈调整设置页，迁移到声明式设置 API

## Boundaries

删除同步只覆盖 Workspace 检索嵌入，不保证清除 AnythingLLM 全局文档存储中的旧源文件。当前已提交 manifest 为 1.0.3，最低 Obsidian 版本为 1.13.0；README 中的旧最低版本尚未同步，以 manifest 为准。未获取社区审核通过或生产使用指标。

## Evidence

`anythingllm-sync@5bdabbd`：README、CHANGELOG、manifest.json 及社区反馈相关提交。详见[本次同步记录](../../journals/2026-10-02-product-progress-sync.md)。
