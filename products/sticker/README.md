# HBoot贴纸表情包

上传一张照片，去除背景后生成可以继续修改文字、字体、装饰和排版的个人贴纸表情包。产品计划同时提供微信小程序与 Web 操作端，并通过 Web 管理端查看统计、任务、日志和设置。

## Status

🟡 In Development / Scaffolded

## Product Goal

先把“用自己的照片做一套贴纸表情包”这件事做顺：选图、去背景、生成、调整、保存，不扩张成复杂的图片设计平台。

## Why This Product

- `HBoot抠图去背景` 后台中，搜索词“贴纸”已有 99 次曝光，但没有带来进入。
- 这只能说明当前搜索曝光没有转化，还不能证明问题一定出在名称上。
- 当前假设是：`HBoot抠图去背景` 强调的是抠图，没有直接传达贴纸和表情包用途。
- 因此单独创建 `HBoot贴纸表情包`，用更明确的名称和产品入口验证这个需求。

## Current Progress

- 已创建独立仓库 `sticker`
- 已按根目录拆分 `miniapp/`、`web/`、`server/` 和共享包
- Web 已预留宣传首页、用户工作台和管理控制台
- 服务端已搭好统一认证 SDK 和统一 AI 能力平台客户端
- 已确定复用 `common-infra` 的 PostgreSQL、Redis 和 MinIO，不在产品内重复部署
- 已确定一份 Compose 配置、Server 与 Web 分开发布的规则
- 已建立根目录 `CHANGELOG.md`，正式版本发布前必须记录日志
- TypeScript 检查、服务端测试和完整构建已通过
- 正式小程序 AppID 尚未创建，暂时使用 `touristappid`，还未导入微信开发者工具

## Planned MVP

- 从相册或相机选择一张照片
- 调用统一 AI 能力平台去除背景
- 根据透明主体生成一组贴纸表情包
- 修改文案、字体、装饰和排版
- 保存单张贴纸或整套作品
- 小程序与 Web 共用用户、作品、任务和积分数据
- 管理端查看统计、任务、日志和产品设置

## Product Principles

- 产品名和首页第一屏直接表达“贴纸表情包”用途
- 第一版只完成一条核心制作链路
- 复用原有贴纸能力，不复用旧产品的认证和 AI 接入方式
- 客户端只访问产品服务端，不直接持有平台凭证
- 用曝光、点击和实际制作数据验证名称与产品表达

## Tech Stack

| Layer | Technology |
| --- | --- |
| Mini Program | 微信小程序原生框架 + TypeScript |
| Website / Workspace / Admin | Next.js 16 + React 19 |
| Business API | Node.js + Fastify + TypeScript |
| Shared Infrastructure | `common-infra`：PostgreSQL + Redis + MinIO |
| Database | PostgreSQL + Prisma |
| Image Composition | Sharp |
| Authentication | HBoot 统一认证平台 |
| Background Removal | HBoot 统一 AI 能力平台 `image.background-removal` |
| Deployment | Docker Compose + GitHub Actions |
| Repository | pnpm workspace |

## Documents

- [Architecture](architecture.md)
- [Roadmap](roadmap.md)
