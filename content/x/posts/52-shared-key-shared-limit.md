# 52｜Shared key, shared limit

- 日期：2026-09-21
- 状态：已发布

## English

> Two apps sharing an AI API key can each stay under their own rate limit and still exceed the shared quota.
>
> I put app requests, background jobs and admin tests through the same scheduler. They now wait for shared capacity before calling the provider.

## 中文校对

> 两个应用共用一把 AI API Key，即使各自没有超过自己的频率限制，合起来仍可能超过共享额度。
>
> 我让产品请求、后台任务和管理端测试经过同一个调度器。它们现在会先等待共享执行额度，再调用服务商。

## 配图

纯文字发布，聚焦多个调用入口共用额度的问题。

## 发布依据

- unified-ai 提交 `aea9cc1` 和 CHANGELOG server-v1.3.0：同步请求、异步 Worker 和控制台测试共享厂商执行额度。
- `server/app/services/provider_queue.py` 的共享范围由适配器类型、上游主机和凭据标识构成，执行前同时检查产品和提供方额度。这里的 shared quota 指执行频率与并发容量，不是余额或日配额。
- `server/tests/test_provider_queue.py` 包含多个配置共享容量、Worker 与控制台共享容量的测试。没有把模拟测试当成生产性能数据。
- 开头是说明共用凭据的场景，不虚构已经发生的线上事故；未承诺排队后永不超时或自动识别厂商所有限制。

## 发布后记录

- X 链接：
- 实际时间：2026-09-21 19:04:27（Asia/Shanghai）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
