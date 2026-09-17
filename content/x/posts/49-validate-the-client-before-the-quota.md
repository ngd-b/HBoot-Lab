# 49｜Validate the client before the quota

- 日期：2026-09-18
- 状态：已发布

## English

> A QR-code login page polls a shared endpoint until the phone confirms, and every poll spends quota. A request that isn't tied to the browser that started the scan can drain that budget before the real user gets through.
>
> I verify the poll belongs to the initiating browser before deducting any quota, and keep the IP rate limit as the outer guard.
>
> The polling budget now goes to the browser that actually scanned — not to whoever hits the endpoint.

## 中文校对

> 二维码登录页会轮询同一个接口直到手机确认，而每次轮询都消耗额度。一个没有绑定到发起扫码浏览器的请求，会在真正用户走完之前就把额度耗尽。
>
> 我先校验这次轮询确实来自发起扫码的浏览器，再扣减额度，并把 IP 限流留作外层防护。
>
> 轮询额度现在花在真正扫码的浏览器上，而不是谁打到接口就算谁的。

## 配图

纯文字发布。校验发起浏览器再扣额是后端逻辑，静态截图无法证明额度扣减顺序。

## 发布依据

- unified-auth 仓库提交 `9bdbad4`「防止未绑定请求消耗二维码领取额度」与 CHANGELOG 3.0.0：扫码轮询先校验发起浏览器，再扣减二维码额度，避免未绑定请求耗尽合法浏览器的轮询和领取额度；保留前置 IP 限流。
- 正文只描述已完成的产品行为，没有声称攻击次数或额度节省效果。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
