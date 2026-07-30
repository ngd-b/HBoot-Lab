# 急用英语架构

## Overview

```text
微信小程序
    │
    ▼
FastAPI
    ├── JSON 场景内容
    ├── DeepSeek ─────── 换一批对话
    ├── Piper / Kokoro ─ 语音合成与缓存
    ├── faster-whisper ─ 录音识别
    ├── 文本比对 ─────── 发音评分
    ├── 内存 Session ─── 微信身份
    └── SQLite ───────── 使用统计

Next.js Website
    └── 静态产品官网，不依赖业务 API
```

## Mini Program

- 原生微信小程序，无前端构建步骤
- 首页、分类、搜索、练习、结果、收藏、历史、个人中心和设置等页面
- 收藏、练习历史及用户设置保存在本地
- 冷启动通过微信 `code2session` 静默获取会话

## Backend

FastAPI 提供六组 API：

- 微信认证
- 分类和场景查询
- 场景搜索
- DeepSeek 对话生成
- TTS 音频
- 录音识别与评分

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

用户点击“换一批”时才调用 DeepSeek，并一次替换全部 5 句。

## Data and Models

- 61 个场景保存在 JSON 文件中，分为面试、职场、日常消费、生活办事、休闲娱乐和旅行六类
- TTS 音频缓存在 Docker 持久化卷中，启动后会在后台预热默认句子
- Whisper、Piper 和 Kokoro 模型通过只读目录外挂，切换模型无需重建业务镜像
- Session 当前存于进程内存，服务重启后用户需要重新登录
- 使用统计写入 SQLite，包括登录、场景访问、播放、评分和 AI 生成事件

## Deployment

- API 和官网使用独立 Docker 容器
- API 与 Web 分别通过版本标签发布
- Nginx 将 `/api` 和 `/health` 转发到 FastAPI，其余请求转发到 Next.js
- 当前不依赖公共 PostgreSQL、Redis 或 MinIO
