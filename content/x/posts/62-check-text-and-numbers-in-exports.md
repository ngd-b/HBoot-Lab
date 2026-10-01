# 62｜Check text and numbers in exports

- 日期：2026-09-26
- 状态：待发布
- 字符数：261

## English

> Exporting user text to Excel? Try a note containing =1+1.
>
> If it becomes 2, your export changed data into a formula.
>
> I fixed my receipt app's XLSX export by marking strings as text. Check a negative amount too: -25.50 should stay numeric, so totals still work.

## 中文校对

> 要把用户填写的文字导出到 Excel？试试填一条内容为 =1+1 的备注。
>
> 如果它变成了 2，你的导出把原始数据变成了公式。
>
> 我在小票应用的 XLSX 导出里把字符串明确标记为文本，修复了这个问题。再检查一个负数金额：-25.50 应当仍是数字，这样才能继续参与求和。

## 配图

纯文字。两个具体输入已足以说明检查方法，没有本次实测的 Excel 截图，不制作模拟结果冒充实测。

## 选题门槛

- 读者：提供表格下载功能的独立开发者，尤其是把用户输入或识别结果导出为表格的产品。
- 可带走的方法：用文字 =1+1 和数字 -25.50 分别检查导出，既检查文字是否被解释成公式，也检查数值是否仍可参与计算。
- 可回应的内容：读者可以补充自己的导出边界样例、单元格类型处理办法，或遇到过的兼容性问题；无需附加空泛提问。

## 发布依据

- `../ai-invoice` 提交 `a47cdd898ece64f54af5f6fc67ee4f4b9a780a89`，2026-09-26。
- `backend/app/api/endpoints/exports.py` 的 XLSX 导出创建单元格后，对字符串明确设置 `cell.data_type = "s"`；数值保持原类型。
- 同一提交的 `backend/tests/test_export_filters.py` 中，`test_excel_external_text_is_never_serialized_as_formula` 使用备注 `=1+1` 和金额 `Decimal("-25.50")`，检查导出文件对应单元格的值与类型。
- 本次阅读了实现和测试代码，未运行产品测试或打开 Excel 实测。不声称已部署、发生过攻击、造成过损失或所有表格软件行为相同。正文的两个值用于建议读者自行检查；修复描述仅限已提交的 XLSX 处理逻辑。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
