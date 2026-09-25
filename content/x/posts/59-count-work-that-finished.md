# 59｜Count the work that finished

- 日期：2026-09-25
- 状态：已发布
- 字符数：268

## English

> OCR can finish even when categorization fails.
>
> If quota accounting treats the whole job as failed, completed recognition work disappears from usage.
>
> I changed settlement to count successful OCR pages even when the later AI step fails, and backfilled earlier records.

## 中文校对

> 即使后续分类失败，OCR 也可能已经完成。
>
> 如果额度系统把整项任务都算作失败，已经完成的识别工作就不会计入用量。
>
> 我调整了结算逻辑：即使后续 AI 步骤失败，也单独统计成功完成 OCR 的页数，并补录了早期记录。

## 配图

纯文字。没有真实用量前后对比数据；不制作示意图代替产品结果。

## 发布依据

- `ai-invoice` 提交 `543bab7d` 调整额度对账：OCR 成功的页面会计入识别用量，不再要求后续 AI 分类也成功。
- 同一提交新增迁移，为早期记录补回已经完成的 OCR 用量。帖子没有声称发生过少扣费或具体影响规模。

## 发布后记录

- X 链接：
- 实际时间：2026-09-25 10:53（北京时间）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
