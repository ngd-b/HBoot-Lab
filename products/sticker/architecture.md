# HBoot贴纸表情包架构

## Overview

```text
微信小程序 ─┐
            ├──> Sticker Server ──> HBoot 统一认证平台
Web ────────┘          ├──────────> HBoot 统一 AI 能力平台
                       └──────────> common-infra
                                      ├── PostgreSQL
                                      ├── Redis
                                      └── MinIO
```

项目不使用 `apps/` 目录，三个发布端直接放在仓库根目录：

- `miniapp/`：微信小程序，负责选图、生成、编辑和保存
- `web/`：Next.js，包含宣传官网、用户工作台和管理控制台
- `server/`：Fastify 产品服务端，承载业务接口和平台集成
- `packages/`：接口契约、API 客户端、贴纸核心能力和认证 SDK

## Client Boundary

浏览器和小程序只访问 Sticker Server。统一认证 API Key、统一 AI 凭证和第三方 Provider 信息都留在服务端，不能下发到客户端。

Web 计划包含三类页面：

- `/`：产品介绍和搜索落地页
- `/app`：用户制作贴纸的工作台
- `/console`：统计、任务、日志和设置

生产环境计划使用 `sticker.hboot.fun`。入口层将 `/api/*` 转发到 Fastify，其余路径转发到 Next.js。

## Product Server

产品服务端负责：

- 将统一身份映射为本地业务用户
- 管理贴纸草稿、模板、作品和导出产物
- 管理去背景与高清导出任务
- 保存积分、订单、设置、统计和审计记录
- 调用统一 AI 能力平台的 `image.background-removal`
- 保存平台 `request_id` 和业务任务状态，支持问题排查

统一认证平台只负责全局身份和产品会话；统一 AI 能力平台负责能力授权、Provider 路由、平台凭证、配额与能力调用日志。产品自己的用户作品和运营数据仍由 Sticker Server 管理。

## Shared Infrastructure

PostgreSQL、Redis 和 MinIO 全部由 `common-infra` 提供。Sticker Server 通过外部 Docker 网络 `infra-net` 使用专属数据库账号、Redis ACL、MinIO Access Key 和 Bucket，不使用 root 凭证，也不在产品 Compose 中启动重复实例。

- PostgreSQL：本地用户、作品、任务、积分、订单、设置、统计和审计数据
- Redis：短期任务状态、缓存、幂等键和跨实例临时数据
- MinIO：原图、透明主体、贴纸成品和导出文件

## Reuse Strategy

从 `HBoot抠图去背景` 复用贴纸模板和布局等纯业务能力，但不直接复用它现有的登录、积分、数据库和 AI 服务接入。可复用逻辑收敛到 `packages/sticker-core/`，避免绑定微信 API、HTTP 框架或数据库。

## Deployment

- 根目录只保留一份 `compose.yml`，包含 `server` 和 `web` 两个服务，并接入 `infra-net`。
- Compose 配置不包含 PostgreSQL、Redis 和 MinIO。
- Server 和 Web 使用独立镜像、版本和健康检查，可以分别更新，发布其中一个不能重建另一个。
- `.github/workflows/deploy-server.yml` 监听 `server-v*`，只部署 Server。
- `.github/workflows/deploy-web.yml` 监听 `web-v*`，只部署 Web。
- 两个 GitHub Actions 工作流共用根目录的 `compose.yml`。
- 不创建 `deploy/`、`ops/` 或多套 Compose 目录；环境差异通过服务器变量和镜像标签表达。

每次打版本标签前必须更新根目录 `CHANGELOG.md`。发布日志需要写明版本改动、配置或数据影响、验证结果和必要的回滚说明；日志版本、Git 标签和镜像标签保持一致。

## Current Limitation

正式小程序 AppID 尚未创建，`project.config.json` 当前使用 `touristappid`。获得 AppID 后，还需要在统一认证平台登记 `orgId=sticker`、服务地址和微信配置，才能完成正式登录、预览和审核链路。
