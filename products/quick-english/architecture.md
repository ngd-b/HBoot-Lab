# 急用英语架构

## Overview

```text
微信小程序
    │
    ▼
FastAPI
    ├── JSON 场景内容
    ├── DeepSeek ─────── 换一批对话
    │                    语义搜索兜底
    ├── Piper / Kokoro ─ 双角色语音合成
    ├── faster-whisper ─ 本地录音识别
    ├── Aliyun NLS ───── 可选 ASR / TTS
    ├── 文本比对 ─────── 发音评分
    ├── PostgreSQL ───── 用户 / 收藏 / 练习 / 学习事件
    ├── Redis ────────── Session / 限流 / 搜索缓存
    └── MinIO ────────── 默认句子 TTS 音频

Next.js Website
    ├── 产品官网
    ├── Web 学习台 ───── FastAPI
    └── 运营看板 ─────── FastAPI Admin API
```

## Mini Program

- 原生微信小程序，无前端构建步骤
- 首页、分类、搜索、练习、结果、收藏、历史、个人中心和设置等页面
- 收藏、练习历史先本地写入，再异步同步到服务端
- 学习事件进入本地可靠队列，断网时保留，恢复后分批补传并按事件 ID 去重
- 冷启动通过微信 `code2session` 静默获取 Redis 会话
- 今日场景和场景目录采用缓存优先、后台刷新

## Backend

FastAPI 提供以下主要 API：

- 微信认证
- 分类和场景查询
- 关键词搜索、自然语言语义搜索和今日场景
- DeepSeek 对话生成
- TTS 音频
- 录音识别与评分
- 用户收藏、练习历史和学习统计
- 学习事件单条 / 批量上报
- 运营统计

统一响应格式为 `{code, message, data}`，付费或高消耗接口带有限流。

## Content Flow

```text
选择场景
    ↓
读取预先整理的 5 句默认对话
    ↓
播放 TTS / 用户录音
    ↓
Whisper 识别
    ↓
文本比对评分
```

用户点击“换一批”时，系统优先分配该用户未见过的共享生成批次；需要补充内容时才调用 DeepSeek，并一次替换全部 5 句。完成练习后会生成句子级报告，用户可以直接重练薄弱句或进入同分类下一个场景。

## Data and Models

- 100 个场景保存在 JSON 内容库中，分为面试、职场、日常消费、生活办事、休闲娱乐和旅行六类
- 默认场景 TTS 音频使用内存 LRU 和 MinIO 两级缓存，启动后在后台预热；临时生成句子的音频只进入内存缓存
- Whisper、Piper 和 Kokoro 模型通过只读目录外挂，切换模型无需重建业务镜像
- 生产环境会话与限流状态存入 Redis，本地开发可降级到内存
- PostgreSQL 保存用户、收藏、练习记录、生成内容池和学习事件；存量 SQLite 数据已提供自动迁移
- 原始跟读录音只用于当次识别，不写入 MinIO，识别完成后释放

## Deployment

- API 和 Web 使用独立 Docker 容器
- API 与 Web 分别通过版本标签发布
- Nginx 将 `/api` 和 `/health` 转发到 FastAPI，其余请求转发到 Next.js
- 生产 API 加入公共 `infra-net`，依赖共享 PostgreSQL、Redis 和 MinIO；任一依赖未就绪时拒绝带病启动
