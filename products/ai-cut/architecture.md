# 智能去背景架构

## Overview

```text
微信小程序
    │
    ├── 登录、积分、任务和历史
    ▼
Koa Business API ─────────────── PostgreSQL
    │                              用户 / 积分 / 任务 / RBAC
    │
    ├── 头像文件 ──────────────── Shared MinIO
    │
    └── 上传 / 触发 / 查询 / 图片代理
            ▼
      FastAPI Cutout API
            ├── Shared Redis
            │     任务队列 / 状态 / TTL / API Key
            ├── Shared MinIO
            │     input/{jobId}.jpg
            │     output/{jobId}.png
            └── HTTP Task API
                    ▼
              Inference Worker
                    └── Provider Router
                          ├── rembg + ONNX Runtime
                          │     isnet-general-use
                          ├── Volcengine AI MediaKit
                          ├── Aliyun ImageSeg
                          └── remove.bg

Next.js Website / Admin ──────── Koa Business API
```

## Frontend

- `miniprogram/` 是原生微信小程序
- 支持单张、批量、证件照、结果编辑和历史记录
- 用户通过微信静默登录，不需要额外注册
- 图片编辑器采用参数化处理管线，支持撤销和重做
- `web/` 是 Next.js 产品官网和管理后台

## Business API

- Node.js、Koa 和 TypeScript
- Prisma 管理 PostgreSQL 数据
- 负责微信登录、JWT、用户、积分、任务记录和管理后台
- 上传前调用微信图片安全检查
- 将图片和处理请求转发给独立抠图服务
- 根据 Standard / Plus 和任务类型选择去背景后端，并保存任务等级快照
- 每 5 秒轮询处理中任务，完成后更新状态，失败或超时则退款
- 图片输出通过业务 API 代理，避免向客户端暴露内部服务凭据
- 高清编辑导出在服务端基于原始结果重放裁剪、旋转、翻转和调色步骤，并使用短时令牌、像素上限与串行队列保护资源

## AI Service

AI 推理位于独立的 `bg-remove` 仓库，不在 Koa 业务 API 进程中运行。业务服务通过 `CUTOUT_SERVICE_URL` 调用 FastAPI：

- 上传图片并获得 `jobId`
- 触发异步处理
- 查询任务状态
- 下载输入图和透明结果图

FastAPI 将任务和所选 Provider 压入 Redis。Worker 直接消费队列、从 MinIO 下载输入图，调用本地 ONNX 或配置的第三方去背景 Provider，再将透明 PNG 写回 MinIO，并回调 API。

本地推理当前使用 `isnet-general-use` 模型；服务也支持按通用、人像和商品场景路由到火山引擎，并保留阿里云与 remove.bg Provider。Worker 运行在 3 GB 内存限制下，只使用一个 ONNX 线程，并在每次本地推理后主动释放图片和张量内存。

### Reliability

- Worker 单个任务最多重试 3 次，并使用指数退避
- 当前任务 ID 写入本地锁文件，Worker 崩溃重启后会把孤儿任务标记为失败
- Redis 和 MinIO 操作带瞬时断线重试
- 每个任务拥有 TTL，过期后自动清理 Redis 状态和 MinIO 输入、输出文件
- Koa 业务服务发现任务失败、丢失或超时后，将任务标记为失败并退还积分
- Koa 与 FastAPI 之间使用 API Key + Token 双请求头认证
- 大图展示使用轻量 WebP 预览，保存和编辑导出仍基于完整分辨率结果

## Data

PostgreSQL 主要保存：

- 用户与微信 OpenID
- 积分余额和积分流水
- 抠图任务及处理状态
- 管理员、角色、权限和操作日志
- 可动态调整的系统设置

## Deployment

- Koa API、Next.js Web、产品 PostgreSQL、FastAPI Cutout API 和 Worker 通过 Docker 部署
- GitHub Actions 按 API、Web 标签分别发布
- Nginx 负责 HTTPS、反向代理和请求限流
- Koa 与 `bg-remove` 都加入公共 `infra-net`
- Koa 使用公共 MinIO 保存头像
- `bg-remove` 使用公共 Redis 保存队列和状态，使用公共 MinIO 保存抠图输入与结果
- PostgreSQL 当前仍由产品自己的容器提供
- Koa 自身已预留 Redis 配置，但应用层限流尚未接入；产品的 AI 推理链路已经通过 `bg-remove` 使用 Redis
