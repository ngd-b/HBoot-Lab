# AI 发票助手架构

## Overview

```text
微信小程序 ───────────────┐
                          ▼
Next.js Web / BFF ─── FastAPI API
                          ├── PostgreSQL
                          ├── MinIO
                          └── Redis Queue
                                  ▼
                               Worker
                                  ├── PaddleOCR
                                  └── DeepSeek
```

## Client Responsibilities

### Mini Program

- 拍照、选择文件和批量上传
- 展示发票台账、详情及处理状态
- 修改识别结果、重试 OCR 或 AI
- 微信静默登录
- 扫描并确认 Web 端登录

### Web

- Next.js App Router
- 管理发票台账、筛选、编辑和导出
- 通过 BFF 代理访问 FastAPI，浏览器不直接连接后端
- JWT 保存在 httpOnly Cookie 中
- 支持管理员查看用户、任务和全局统计

## Backend

FastAPI 按 API、Service 和 Provider 分层：

- API：认证、上传、发票、OCR、分类、导出、文件、任务、分类和管理端
- Service：发票业务、上传、统计和分类
- Provider：PaddleOCR、DeepSeek 和 MinIO 的可替换实现
- SQLAlchemy 异步会话访问 PostgreSQL
- Alembic 是唯一数据库结构管理入口，服务启动时自动执行迁移

## Processing Pipeline

```text
文件上传
    ↓
格式、大小与文件魔数校验
    ↓
文件哈希判重
    ↓
MinIO 保存原文件
    ↓
Redis 入队 OCR
    ↓
Worker 加载 PaddleOCR
    ↓
正则提取基础字段 + 发票字段判重
    ↓
Redis 链式入队 AI
    ↓
DeepSeek 结构化提取 + 9 类分类
    ↓
PostgreSQL 更新为可用状态
```

Redis 入队失败时会降级到 API 进程内任务。导出目前始终使用进程内后台任务，API 重启会丢失正在执行的导出。

## Shared Infrastructure

三个基础服务全部来自 `common-infra`：

- PostgreSQL：发票、用户、任务、类别和导出记录
- Redis：使用 `invoice:*` 前缀的 OCR / AI 任务队列
- MinIO：保存发票原文件和导出文件

业务使用独立数据库账号、Redis ACL 前缀和 MinIO 专属桶，与其他产品隔离。

## Deployment

- Backend、Worker 和 Web 是三个独立容器
- Backend 与 Worker 使用同一业务镜像
- OCR 模型通过只读目录预置，不在启动时自动下载
- 所有容器加入公共 `infra-net`
- API 和 Web 使用不同版本标签独立发布
- 部署完成后执行 API 健康检查和 Web 冒烟检查
