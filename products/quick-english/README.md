# 急用英语

面向真实场景的英语救急小程序。用户选择一个场景，用约 5 分钟练习 5 句马上能用的英语表达。

## Status

🟢 Online / Iterating

## Product Goal

帮助“学过英语，但在机场、酒店、医院或面试现场说不出来”的用户，在具体场景中快速找到并练习最需要的表达。

它不是完整课程、词典或自由聊天机器人。

## Current Features

- 6 类、100 个真实场景
- 关键词与自然语言语义搜索、分类浏览和场景收藏
- 每个场景默认提供 5 句核心对话
- 双角色英语原声播放与多档语速
- 微信录音跟读
- Whisper 语音识别与逐句发音评分
- DeepSeek“换一批”，重新生成当前场景的 5 句对话
- 今日场景、连续学习天数和学习热力图
- 同分类连续练习、结果复盘和薄弱句重练
- 练习历史、收藏和设置的服务端同步
- 微信静默登录
- Next.js 产品官网与 Web 学习台
- 微信搜一搜结构化页面推送
- 用户学习行为统计和运营看板

## Product Principles

- 每个场景只保留 5 句，降低开始练习的压力
- 默认内容预先准备，打开场景不等待 AI
- AI 生成是补充，不取代人工筛选的基础内容
- 第一版围绕“马上能说”验证，不扩张成完整课程系统

## Tech Stack

| Layer | Technology |
| --- | --- |
| Mini Program | 微信小程序原生框架 |
| API | Python + FastAPI |
| LLM | DeepSeek API |
| ASR | faster-whisper |
| TTS | Piper / Kokoro ONNX |
| Content | JSON 场景文件 |
| Database | PostgreSQL |
| Session / Cache | Redis |
| Audio Storage | MinIO |
| Website | Next.js 16 + React 19 + Tailwind CSS |
| Deployment | Docker + GitHub Actions + Nginx |

## Documents

- [Architecture](architecture.md)
- [Roadmap](roadmap.md)

## Assets

- [产品截图](assets/screenshots/)
- [小程序码](assets/qr.jpg)
