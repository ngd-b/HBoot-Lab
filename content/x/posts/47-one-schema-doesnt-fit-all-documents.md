# 47｜One schema doesn't fit all documents

- 日期：2026-09-17
- 状态：待发布

## English

> A receipt, an invoice, and a payment screenshot share almost no fields, so one extraction schema either invents fields that don't exist or drops the ones that matter.
>
> My bookkeeping app detects the document type first and keeps each type's own field boundary—tax and invoice numbers stay on invoices, not on lunch receipts.
>
> Extracted fields now match what each document actually contains.

## 中文校对

> 小票、发票和支付截图几乎没有共同的字段，用同一套提取结构要么凭空造出不存在的字段，要么丢掉真正重要的字段。
>
> 我的记账工具先判断票据类型，再保持每类票据的字段边界——税额和发票号码只出现在发票上，不会跑到餐饮小票里。
>
> 提取出来的字段现在和每张票据实际包含的内容一致。

## 配图

纯文字发布。类型识别与字段边界是后台逻辑，静态截图无法证明不同票据类型使用了不同字段结构。

## 发布依据

- [小票智能分类记账产品说明](../../../products/ai-invoice/README.md)：PaddleOCR 识别发票、餐饮 / 超市小票、支付记录和交通票据；自动判断票据类型并保持发票专属字段边界。
- [小票智能分类记账路线图](../../../products/ai-invoice/roadmap.md)：已记录“发票、小票、支付记录和交通票据的类型识别”完成。
- 正文只描述已完成的产品行为，没有声称识别准确率或分类准确率提升。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
