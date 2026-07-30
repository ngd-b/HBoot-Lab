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
    ├── 头像文件 ──────────────── MinIO
    │
    └── 上传 / 触发 / 查询
            ▼
      AI Cutout Service
            │
            ├── 任务队列与文件存储
            └── AI Inference Model
                  BiRefNet → isnet-general-use

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
- 每 5 秒轮询处理中任务，完成后更新状态，失败或超时则退款
- 图片输出通过业务 API 代理，避免向客户端暴露内部服务凭据

## AI Service

AI 推理不在业务 API 进程中运行。业务服务通过 `CUTOUT_SERVICE_URL` 调用独立抠图服务：

- 上传图片并获得 `jobId`
- 触发异步处理
- 查询任务状态
- 下载输入图和透明结果图

早期使用 BiRefNet，当前产品档案记录为 `isnet-general-use`。模型服务源码不在当前产品业务仓库中。

## Data

PostgreSQL 主要保存：

- 用户与微信 OpenID
- 积分余额和积分流水
- 抠图任务及处理状态
- 管理员、角色、权限和操作日志
- 可动态调整的系统设置

## Deployment

- Koa API、Next.js Web 和 PostgreSQL 通过 Docker 部署
- GitHub Actions 按 API、Web 标签分别发布
- Nginx 负责 HTTPS、反向代理和请求限流
- 已加入 `infra-net`，头像使用公共 MinIO
- PostgreSQL 当前仍由产品自己的容器提供
- Redis 已预留配置，但运行时限流和任务逻辑尚未接入 Redis
