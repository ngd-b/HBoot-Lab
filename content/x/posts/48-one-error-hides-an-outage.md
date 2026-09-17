# 48｜One error hides an outage

- 日期：2026-09-18
- 状态：已发布

## English

> A failed session check usually means one of two things: the token is invalid, or my own auth service is down. Most code returns the same generic error for both.
>
> I split them at the verification layer — a revoked credential returns 401, an unreachable auth service returns 503 — and tag each with the product and the verification stage that failed.
>
> During an outage, valid users no longer get told they've been logged out.

## 中文校对

> 会话校验失败通常是两种之一：token 失效，或者我的认证服务自己挂了。大多数代码对这两种情况返回同一个笼统错误。
>
> 我在验签层把它们分开——凭证失效返回 401，认证服务不可达返回 503——并各自带上产品和失败的验签阶段。
>
> 服务故障时，正常用户不再被当成已登出。

## 配图

纯文字发布。401/503 的区分发生在后端验签层，静态截图无法证明错误码分支和诊断字段。

## 发布依据

- unified-auth 仓库提交 `07f23c0`「区分会话凭证失效与认证服务异常」与 CHANGELOG 3.0.2：会话验签限定 RS256，区分凭证失效（401）与认证服务内部异常（503），补充产品标识和验签阶段诊断。
- 正文只描述已完成的产品行为，没有声称降低了登录投诉或提升了可用性数字。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
