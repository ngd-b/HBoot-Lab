# 智能去背景

基于 AI 的微信小程序抠图工具。用户上传图片后，可以获得透明背景图片，并继续完成裁剪、变换、调色、背景替换和证件照制作。

## Status

🟢 Online / Iterating

## Product Goal

让用户在不被强制注册、广告或下载付费阻挡的情况下，快速完成一次图片背景移除。

## Current Features

- 单张图片上传、拍照和 AI 去背景
- 一次最多 9 张图片的批量抠图
- 原图与结果对比
- 图片编辑：裁剪、旋转、缩放、调色和背景替换
- 证件照尺寸与底色处理
- 透明 PNG 保存与分享
- 微信静默登录、头像和昵称管理
- 积分获取、消耗、退款及积分记录
- 抠图历史记录
- Next.js 产品官网
- 管理后台：用户、积分、角色权限、操作日志和系统设置

## Product Principles

- 用户打开工具后可以直接完成任务
- 不在处理完成后阻止用户拿到结果
- 功能围绕图片处理，不扩张成复杂设计平台
- 失败或超时任务自动退还积分

## Tech Stack

| Layer | Technology |
| --- | --- |
| Mini Program | 微信小程序原生框架 |
| API | Node.js + Koa + TypeScript |
| Database | PostgreSQL + Prisma |
| Website / Admin | Next.js 16 + React 19 + Tailwind CSS |
| Object Storage | MinIO |
| Deployment | Docker + GitHub Actions + Nginx |
| AI Model | BiRefNet（第一版）、isnet-general-use（当前记录） |

AI 推理由独立抠图服务提供，业务 API 负责微信身份、积分、任务记录和结果代理。

## Documents

- [Why AI Cut](idea.md)
- [Architecture](architecture.md)
- [Roadmap](roadmap.md)
- [上线第一周复盘](launch/first-week-review.md)
- [上线两个月复盘](launch/two-month-review.md)

## Assets

- [产品截图](assets/screenshots/)
- [演示图片](assets/demo/)
- [小程序码](assets/qr.jpg)
