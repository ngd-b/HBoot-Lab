# 63｜Revoke a key while queued

- 日期：2026-09-26
- 状态：待发布
- 字符数：266

## English

> Does revoking an API key stop queued AI jobs?
>
> 1. Queue a request.
> 2. Revoke its key before it runs.
> 3. Check whether it still reaches the provider.
>
> I added a credential check before dispatch, so requests waiting in the queue can't rely on an earlier authorization.

## 中文校对

> 撤销 API 密钥，能阻止正在排队的 AI 任务吗？
>
> 1. 让一个请求进入队列。
> 2. 在它执行前撤销密钥。
> 3. 检查它是否仍然调用了服务商。
>
> 我在实际调用前加了凭证检查，让排队中的请求不能仅凭入队时的授权继续执行。

## 配图

纯文字。操作顺序本身就是可复用的检查方法，无需模拟后台截图。

## 选题门槛

- 读者：有排队、重试或限流等待的 AI 服务开发者，关心停用密钥后等待中的请求是否继续调用上游。
- 可带走的方法：按“入队、撤销、检查上游调用”复现一个权限变化边界，并在执行前重新读取凭证状态。
- 可回应的内容：读者可以分享队列授权的处理办法，以及如何区分尚未执行的请求与已经发给服务商的请求。开头问题对应后面的实际检查，不附加泛泛互动提问。

## 发布依据

- `../unified-ai` 提交 `3530ad1b309d53f0be8ac98a53a73fcdff0431ed`，2026-09-26。
- `server/app/api/routes/invocations.py` 新增 `_refresh_execution_authorization`，刷新凭证等实体，检查停用与过期状态；在实际 `adapter.invoke` 前调用。
- `server/tests/test_idempotency.py` 的 `test_sync_rechecks_credential_after_wait` 在排队等待期间停用凭证或将其设为过期，断言 401、相应错误码、上游未调用且队列已释放。
- 本次只阅读实现与已有测试，未执行产品测试。正文描述已提交的实现及读者可采用的检查，不声称发生过生产事故或能够撤回已经发到上游的请求。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
