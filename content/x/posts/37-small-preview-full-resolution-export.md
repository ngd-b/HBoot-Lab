# 37｜Small preview, full-resolution export

- 日期：2026-09-13
- 状态：已发布

## English

> A smaller preview shouldn't mean a smaller download.
>
> My image editor displays a lightweight WebP preview. On export, the server replays crops, rotations, flips, and color edits on the full-resolution result.
>
> The saved PNG keeps the original detail.

## 中文校对

> 预览图缩小了，下载的图片不该跟着缩水。
>
> 我的图片编辑器展示轻量 WebP 预览。导出时，服务端在完整分辨率的处理结果上重新执行裁剪、旋转、翻转和调色。
>
> 保存的 PNG 保留原图细节。

## 配图

纯文字。本文说明预览与导出的处理方式，没有现成的同素材分辨率对比图，不用示意图充当实际结果。

## 发布依据

- [抠图服务架构](../../../products/ai-cut/architecture.md) Reliability：大图展示使用轻量 WebP 预览，保存和编辑导出仍基于完整分辨率结果。
- 同一架构的 Business API：高清编辑导出在服务端基于原始结果重放裁剪、旋转、翻转和调色步骤。
- [已完成事项](../../../products/ai-cut/roadmap.md)：大图轻量预览与服务端高清编辑导出已完成。
- 正文的 original detail 指导出基于完整分辨率结果，不使用压小的预览作为导出源；不表示裁剪后像素尺寸不变，也不承诺无损还原输入图或提升清晰度。没有声称具体性能收益。

## 发布后记录

- X 链接：
- 实际时间：2026-09-13 01:33（北京时间）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
