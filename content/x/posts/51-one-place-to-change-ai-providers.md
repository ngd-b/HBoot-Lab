# 51｜One place to change AI providers

- 日期：2026-09-21
- 状态：已发布

## English

> Switching AI providers can mean editing every app that uses them.
>
> I built a shared service for OCR, speech and image processing. It handles provider-specific requests and responses, so apps can keep the same API.
>
> A new provider still needs testing on real inputs.

## 中文校对

> 换一家 AI 服务商，可能意味着所有接入它的应用都要改。
>
> 我做了一层共用服务，接入文字识别、语音和图像处理。不同服务商的请求与返回格式由它处理，应用可以继续使用相同的接口。
>
> 换了服务商，仍然要拿实际输入测试效果。

## 配图

纯文字发布。公众号封面含中文，不复用到本帖。

## 发布依据

- 承接公众号 #027《做了几个 AI 产品后，我为什么又做了一个能力平台？》，聚焦服务适配层的用途。
- unified-ai 当前 README、接口接入文档与 CHANGELOG 已记录 OCR、语音、抠图及模型接入，产品通过平台能力协议调用，提供方适配器负责格式转换。
- ADR-0001 记录稳定能力协议与提供方适配的设计动因；该文档仍标注 Proposed，已实现范围以代码及发布记录为准。
- “保持相同接口”限定为平台输入输出约定不变的情况，不承诺服务效果一致、所有切换均无需产品改动，或所有产品已经完成迁移。
- 本帖描述实现与适用边界，不虚构实际切换事件、节省时间或性能数据。

## 发布后记录

- X 链接：
- 实际时间：2026-09-21 02:55:01（Asia/Shanghai）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
