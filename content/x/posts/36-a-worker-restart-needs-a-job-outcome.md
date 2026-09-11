# 36｜A worker restart needs a job outcome

- 日期：2026-09-12
- 状态：已发布
- 字符数：250

## English

> An AI worker can restart while its last job stays stuck on "processing".
>
> I persist the active job ID. On restart, the worker marks the abandoned job as failed. The billing service detects the failure and refunds the credits.
>
> The user can try again.

## 中文校对

> AI 处理进程重启了，之前的任务却可能还卡在“处理中”。
>
> 我把正在处理的任务 ID 保存下来。重启时，处理进程会把遗留任务标记为失败；负责积分的业务服务检测到失败后退还积分。
>
> 用户可以重新尝试。

## 配图

纯文字发布。任务恢复与积分处理的实现已由仓库记录支持，没有额外准备运行时截图，不虚构故障前后画面。

## 发布依据

- [抠图服务架构](../../../products/ai-cut/architecture.md) Reliability：当前任务 ID 写入本地锁文件，Worker 崩溃重启后将孤儿任务标记为失败。
- 同一架构记录：业务服务发现任务失败、丢失或超时后，将其标记为失败并退还积分。
- [已完成事项](../../../products/ai-cut/roadmap.md)：任务重试、崩溃恢复和过期文件清理已完成。
- 本帖讲已实现的故障处理路径，不宣称今天发生过线上故障，也不宣称原任务会自动恢复执行。最后一句指积分退回后用户可以重新尝试。

## 发布后记录

- X 链接：
- 实际时间：2026-09-12 07:06（北京时间）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
