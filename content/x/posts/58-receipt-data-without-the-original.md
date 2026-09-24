# 58｜Keep receipt data, reclaim the original

- 日期：2026-09-25
- 状态：已发布
- 字符数：279

## English

> Keeping every uploaded receipt forever can quietly turn into a storage cost.
>
> I added a cleanup flow that previews the files you’ll remove, then deletes selected originals while keeping the extracted receipt data.
>
> The trade-off is clear: no original means no restore or re-scan.

## 中文校对

> 永久保留每一张上传的收据，会悄悄变成存储成本。
>
> 我加了一个清理流程：先预览将要删除的文件，再删除选中的原件，同时保留已经提取的收据信息。
>
> 取舍很明确：没有原件，就无法恢复或重新识别。

## 配图

纯文字。没有已记录的真实界面对比图；不制作示意图代替产品结果。

## 发布依据

- `ai-invoice` 提交 `4aef72de` 新增附件管理流程：可预览待清理原件，确认后删除对象存储中的原件，并将凭证记录的 `file_url` 置空，保留提取出的凭证数据。
- 产品界面明确说明原件删除后无法恢复或重新 OCR；帖子保留这一限制，不声称降低了多少成本或存储占用。

## 发布后记录

- X 链接：
- 实际时间：2026-09-25 01:18（北京时间）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
