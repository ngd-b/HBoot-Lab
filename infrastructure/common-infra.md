# Common Infrastructure

三个产品逐渐增多后，重复部署 PostgreSQL、Redis 和 MinIO 带来了配置不一致、资源浪费和维护成本。`common-infra` 将这些基础服务统一部署，再按业务进行隔离。

## Status

🟢 Running / Iterating

## Services

| Service | Version | Purpose |
| --- | --- | --- |
| PostgreSQL | 16 | 业务关系型数据 |
| Redis | 7 | 缓存、限流和异步任务队列 |
| MinIO | 固定发布版本 | 图片、发票和导出文件 |

可选管理工具包括 pgAdmin 和 RedisInsight，默认不在生产环境启动。

## Isolation Model

每个业务通过 `provision.sh <service-name>` 获得独立凭据：

- PostgreSQL：独立数据库和账号，不能访问其他业务数据库
- Redis：独立 ACL 用户，只能访问业务前缀下的 Key，并禁用高风险管理和复制命令
- MinIO：独立桶、服务账号和桶级访问策略

生成的凭据保存在不提交 Git 的 `.credentials/<service-name>.env`。

## Network

公共服务创建外部 Docker 网络 `infra-net`。同一服务器上的业务容器加入网络后，通过以下容器名访问：

- `infra-postgres`
- `infra-redis`
- `infra-minio`

基础服务端口只绑定宿主机回环地址，不直接暴露到公网。

## Operations

- Docker Compose 健康检查
- Redis AOF 持久化
- PostgreSQL、Redis 和 MinIO 旧数据迁移工具
- 业务一键开通和带确认的拆除脚本
- GitHub Actions 自动部署
- 部署失败自动恢复上一版文件和容器配置
- PostgreSQL、Redis 和 MinIO 备份说明

## Current Product Adoption

| Product / Service | PostgreSQL | Redis | MinIO |
| --- | --- | --- | --- |
| AI 发票助手 | ✅ Shared | ✅ Shared queue | ✅ Shared |
| 智能去背景业务服务 | ⏳ Product container | ⏳ Config only | ✅ Shared avatars |
| 智能去背景推理服务 | — | ✅ Shared queue / status | ✅ Shared input / output |
| 急用英语 | — | — | — |
| Unified Auth | 🧪 Planned | 🧪 Planned | — |

急用英语当前使用 JSON、内存 Session、SQLite 和本地持久化卷，保持轻量单机架构。

智能去背景分为两个仓库：Koa 业务服务的 PostgreSQL 仍由自己的 Compose 管理，Redis 仅有预留配置；独立 `bg-remove` 推理服务已经使用公共 Redis 和 MinIO 完成任务排队、状态管理及图片存储。

Unified Auth 的 Compose 已配置接入 `infra-net`，计划使用公共 PostgreSQL 和 Redis，但平台尚未测试完成，也没有接入现有产品，因此不计入已运行的产品依赖。

## Why It Matters

公共基础设施不会直接产生用户可见功能，但能减少新产品反复搭建相同服务的时间，让第五个、第六个产品在一致的底层能力上开始。
