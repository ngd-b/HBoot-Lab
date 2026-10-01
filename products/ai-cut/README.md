# HBoot抠图去背景

基于 AI 的微信小程序抠图工具。用户上传图片后，可以获得透明背景图片，并继续完成裁剪、变换、调色、背景替换和证件照制作。

## Status

🟢 Online / Iterating

## Product Goal

让用户在不被强制注册、广告或下载付费阻挡的情况下，快速完成一次图片背景移除。

## Progress Sync — 2026-10-02

- 已接入统一认证、Web 邮箱／微信登录、账号合并和统一支付；后台授权改为平台管理员，原本地角色不再授予管理权限。
- 版本日志记录擦除画笔、撤销重做、原始分辨率擦除导出及保守的透明残留清理；主体不明确时保留原结果。
- 已提交独立智能消除页面，支持矩形位置、文字和 Logo 参考图，可继续消除或衔接去背景；任务恢复、扣费与失败退款复用既有流程。
- 智能消除仍需目标环境迁移、标准版服务授权和真实样张验收；源码完成不等于已启用。画笔 RLE、自动 OCR 和 Pro 自动消除暂未开放。
- 依据：`cutout@0faf332`、`CHANGELOG.md`、`docs/smart-erase-integration.md`；详见[本次同步记录](../../journals/2026-10-02-product-progress-sync.md)。

## Latest Milestone

- 2026-08-15：产品 UV 达到 500
- 2026-08-15：开始广告变现，前三日收入分别为 0.3 元、0.4 元和 0.4 元，累计 1.1 元
- 积分策略取消普通分享奖励，用户可以通过完整观看激励视频获得积分

## Current Features

- 单张图片上传、拍照和 AI 去背景
- 一次最多 9 张图片的批量抠图
- 透明背景图、商品白底图和批量抠图的场景化入口
- 原图与结果对比
- 图片编辑：裁剪、旋转、缩放、调色和背景替换
- 基于原始结果重放编辑步骤的高清 PNG 导出
- 证件照尺寸与底色处理
- 透明 PNG 保存、成品图分享和批量顺序保存
- Standard / Plus 处理等级及单次增强重跑
- 长任务完成后的微信订阅消息提醒
- 微信静默登录、头像和昵称管理
- 积分获取、消耗、退款、连续签到和激励视频奖励；普通分享不再直接发放积分
- 抠图历史记录、作品有效期和快捷再处理
- Next.js 产品官网
- 管理后台：用户、积分、平台管理员授权、操作日志和系统设置

## Product Principles

- 用户打开工具后可以直接完成任务
- 不在处理完成后阻止用户拿到结果
- 功能围绕图片处理，不扩张成复杂设计平台
- 失败或超时任务自动退还积分

## Tech Stack

| Layer | Technology |
| --- | --- |
| Mini Program | 微信小程序原生框架 |
| Business API | Node.js + Koa + TypeScript |
| Cutout API | Python + FastAPI |
| Inference Worker | rembg + ONNX Runtime |
| Database | PostgreSQL + Prisma |
| Website / Admin | Next.js 16 + React 19 + Tailwind CSS |
| Queue / Status | Redis |
| Object Storage | MinIO |
| Deployment | Docker + GitHub Actions + Nginx |
| Cutout Providers | 本地 ONNX，以及可配置的火山引擎、阿里云和 remove.bg |
| Local Model | BiRefNet（早期）、isnet-general-use（当前） |

业务 API 负责微信身份、积分、任务记录、高清编辑导出和结果代理；独立的 `bg-remove` 服务负责文件保存、任务排队和按任务等级选择去背景 Provider。

## Documents

- [Why AI Cut](idea.md)
- [Architecture](architecture.md)
- [Roadmap](roadmap.md)
- [上线第一周复盘](launch/first-week-review.md)
- [上线两个月复盘](launch/two-month-review.md)
- [500 UV 与首次广告收入](launch/500-uv-and-first-ad-revenue.md)

## Assets

- [产品截图](assets/screenshots/)
- [演示图片](assets/demo/)
- [小程序码](assets/qr.jpg)
