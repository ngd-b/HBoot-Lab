# HBoot贴纸表情包

上传一张照片，去除背景后生成可以继续修改文字、字体、装饰和排版的个人贴纸表情包。产品同时提供微信小程序与 Web 操作端，并通过 Web 管理端查看统计、任务、日志和设置。

## Status

🟢 Online / Iterating

## Product Goal

先把“用自己的照片做一套贴纸表情包”这件事做顺：选图、去背景、生成、调整、保存，不扩张成复杂的图片设计平台。

## Why This Product

- `HBoot抠图去背景` 后台中，搜索词“贴纸”已有 99 次曝光，但没有带来进入。
- 这只能说明当前搜索曝光没有转化，还不能证明问题一定出在名称上。
- 当前假设是：`HBoot抠图去背景` 强调的是抠图，没有直接传达贴纸和表情包用途。
- 因此单独创建 `HBoot贴纸表情包`，用更明确的名称和产品入口验证这个需求。

## Current Progress — 2026-10-02

- 小程序首个正式版本 1.0.0 已于 2026-09-12 上线，来源仓库版本日志记录了用户确认。
- 已实现选图、可选去背景、六类主题、每套八张、多文字／图片／装饰编辑、图层排序和透明 PNG 导出。
- 已实现草稿保存、制作记录、积分、签到和购买入口；图文安全检测通过统一认证平台处理。
- Web 提供宣传页、工作台及管理控制台；统一认证、微信扫码确认和账号合并已接入。
- Server / Web 独立部署，复用公共 PostgreSQL、Redis 和 MinIO；版本日志记录 Server 0.4.2、Web 0.3.1。
- 待支付订单十分钟失效，停止常规自动查单，保留迟到付款、退款和发货补偿。
- 小程序 1.0.1 尚待发布，尚未记录上传确认、体验版设置、审核及正式发布完成；真实支付与晚到回调仍待正式环境验收。
- 依据：`sticker@c7dab95` 的 `README.md` 和 `CHANGELOG.md`。不将 1.0.1 的待发布状态覆盖到已经上线的 1.0.0。

## Validation Pending

- 尚未取得名称调整后的曝光、点击、制作和保存转化数据。
- 真机验收结果未记录，不能以自动化测试代替真实支付验收。

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
