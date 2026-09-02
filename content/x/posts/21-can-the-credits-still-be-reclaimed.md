# 21｜Can the credits still be reclaimed?

- 日期：2026-09-02
- 状态：待发布，计划稍晚发布

## English

> Say someone buys 100 credits, spends 30, but still has 120. Should the refund be blocked?
>
> I changed the check: don't ask if purchased credits were used. Ask if all 100 can still be reclaimed.
>
> Enough balance: recommend a refund. Shortfall: recommend blocking and show the gap.

## 中文

> 假设有人买了 100 积分，用掉 30，但账户里还剩 120。这个退款要不要拦？
>
> 我刚改了退款判断：不再看“买来的积分有没有用过”，而是看退款时能不能完整收回这 100 积分。
>
> 余额够，就建议退款；余额不够，才建议拦截并说明还差多少。

## 配图

纯文字发布。具体数字已经能说明退款判断中的冲突，后台订单截图不能增加有效信息。

## 发布依据

- 《智能去背景》已实现 iOS 退款询问判断，并根据需要撤回的积分与账户当前可用积分给出建议。
- 判断逻辑不再因为购买积分曾被使用就直接建议拦截；当前余额足以完整撤回本次购买权益时建议退款。
- 当前余额不足以撤回剩余权益时才建议拦截，并记录需要撤回的积分、可用积分与缺口。
- “购买 100、使用 30、余额 120”的数字是已提交测试中的示例场景，不代表真实用户订单。

## 发布后记录

- X 链接：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
