# 50｜The status a product reads

- 日期：2026-09-18
- 状态：待发布

## English

> A payment order in my database is just a snapshot of what WeChat knows. Return that cached value on a status query and a user keeps seeing "pending" while WeChat already said "paid."
>
> Now a query re-syncs the order with WeChat before answering — rate-limited, with a short lease so concurrent polls don't double-hit the endpoint. An old unpaid order past its sync window stays out of the polling loop instead of being silently revived.
>
> The status a product reads is now the payment provider's truth, not my last write.

## 中文校对

> 数据库里的支付订单，只是微信状态的一个快照。状态查询时直接返回这个缓存值，用户就会一直看到「待支付」，而微信那边其实早已显示「已支付」。
>
> 现在查询会先向微信重新同步这笔订单再返回——带限流、带短租约，避免并发轮询重复打到接口。已经过了同步窗口的旧未支付订单，会留在轮询循环之外，而不是被悄悄重新拉回来。
>
> 产品读到的状态，现在是支付服务商的真实结果，而不是我上一次写入的值。

## 配图

纯文字发布。查询时重新同步是后端逻辑，静态截图无法证明「查询返回的是微信最新状态而非本地缓存」。

## 发布依据

- unified-auth 仓库提交 `1ba5445`「查询支付订单时同步微信状态并兼容超时订单」（2026-09-15，位于 v3.0.2 之后的未发布改动）：产品查询支付订单时，先调用微信 `query_order` 重新同步并核对账本，再返回状态；用固定窗口限流（每单 30 秒 1 次）与 120 秒租约避免并发重复查单；已过 10 分钟同步窗口的旧未支付订单不会重启自动轮询，查单期间到达的回调 / 退款唤醒仍被保留。
- 正文只描述已完成的产品行为，没有声称同步成功率、到账速度或用户投诉下降。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
