# 72｜Checkout timeout isn't rejection

- 日期：2026-10-02
- 状态：已发布
- 字符数：256

## English

> Your checkout request timed out. The provider may still have created a transaction.
>
> My billing service keeps two states:
> Rejected: fix the cause, retry the same order and idempotency key.
> Unknown: block recreation and reconcile the original request first.

## 中文校对

> 创建支付的请求超时了，服务商仍可能已经创建了交易。
>
> 我的支付服务区分两种状态：
> 明确拒绝：修正原因，沿用原订单和幂等键重试。
> 结果未知：阻止重新创建，先核对原请求的结果。

## 配图

纯文字。没有真实重复付款事故或对应数据，不制作虚构订单截图。

## 选题门槛

- 读者：接入外部支付服务、需要处理超时和重试的独立开发者。
- 具体问题：请求超时无法证明渠道没有创建交易，直接重新创建会带来额外交易的风险。
- 可带走的做法：把明确拒绝与结果未知分开处理；拒绝后修正原因并保留订单及幂等键，未知时先核查再决定下一步。
- 讨论空间：开发者如何设计重试入口、保存原请求标识、核查渠道结果及处理无法立即确认的订单。本帖陈述已实现的处理方式，不虚构未决决策或强行追加问题。

## 发布依据

- 用户明确选择素材方向 2：支付请求超时后，重试按钮该做什么。
- `unified-billing` 提交 `a88f97f8bcb076acccfe5dcf053546bfa103e4f0` 实现创建支付失败分类、保留首次原因、原订单重试限制及核查流程；`tests/checkout-failure.test.ts` 包含对应模拟验证。本次未运行该仓库测试。
- 核对 HEAD `4ee1c7d` 的 `docs/API.md`“异常交易与恢复”：渠道标准拒绝允许管理员修正配置后重试原任务，保留原订单和幂等键；超时、网络异常、响应或入库异常保留 UNKNOWN，普通任务重试不能重新创建。
- 已知并验证归属的交易编号可用于只读渠道查询；否则等待已配置渠道事件、扫描或管理员核实。英文 reconcile 不表示所有结果未知的订单都能自动立即查清。
- `ai-invoice` 的 `607ea4ff` 同步消费这一失败契约，不通过替换订单掩盖未知结果。
- 开头是假设的超时场景，不是作者真实被重复扣款或用户投诉。只描述创建交易，不把请求超时说成已经付款成功。
- 不声称本次已经避免多少重复付款、提升转化或完成真实生产端到端验收；这不是支付平台通用错误码或当前政策介绍。

## 发布后记录

- X 链接：
- 实际时间：2026-10-02 07:55（北京时间，按确认时间记录）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 24 小时记录：
- 72 小时记录：
- 观察：
