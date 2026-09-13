# 38｜Natural-language search without sharing receipts

- 日期：2026-09-13
- 状态：已发布

## English

> "How much did I spend on food last month?"
>
> In my receipt app, AI turns the question into filters. The database checks them against the user's records and returns matching receipts and a total.
>
> For this search, the model never sees the receipts or calculates the total.

## 中文校对

> “上个月吃饭花了多少钱？”
>
> 在我的小票工具里，AI 把问题解析成筛选条件。数据库根据这些条件查询当前用户的记录，返回匹配的票据和总金额。
>
> 这条查询链路中，模型不接收票据内容，也不负责计算总额。

## 配图

纯文字发布。正文已能说明查询过程，不需要额外配图。

## 发布依据

- [小票工具架构](../../../products/ai-invoice/architecture.md) Natural-language Search：规则解析与 DeepSeek 意图补充生成查询条件，经确定性校验后，由 PostgreSQL 在当前用户范围内筛选和汇总，返回匹配票据、数量和消费总额。
- 同一架构记录明确：模型只接收查询文本和允许的分类信息，不接收用户票据内容。
- [已完成事项](../../../products/ai-invoice/roadmap.md)：自然语言查账、金额汇总和最近 / 最高 / 最低消费查询已完成。
- [开发日志](../../../journals/2026-08.md) 2026-08-17：自然语言查账已上线，可按时间、商家、类别、票据类型和金额筛选并汇总。
- 开头是能力范围内的查询示例，不冒充用户原话或实际查询截图；未编造金额或查询准确率。模型不接收票据的边界仅指自然语言查账，不指 OCR 后的 AI 提取与分类链路。

## 发布后记录

- X 链接：
- 实际时间：2026-09-13 11:15（北京时间）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
