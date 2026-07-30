# AI 发票助手

拍照或上传发票后，自动完成 OCR 识别、AI 分类、台账管理和报销数据导出。

## Status

🚧 Iterating

## Product Goal

减少个人和报销用户重复录入发票字段的时间，只聚焦“OCR 识别 + AI 自动归类”，不从第一版开始建设完整 OA、审批或财务系统。

## Current Features

- 微信小程序拍照或从相册选择文件
- 支持 JPG、PNG 和 PDF，一次最多上传 9 张
- PaddleOCR 识别发票、小票和支付截图
- 提取发票号码、交易方、金额、税额、日期和明细
- DeepSeek 自动归入 9 类报销类别并提取小类
- 文件哈希和发票字段双重判重
- 失败任务重试、重新识别和重新分类
- Web 发票台账、搜索、筛选和字段编辑
- Excel / CSV 导出
- 微信扫码登录 Web 管理台
- 用户、任务和系统指标管理页面

## Product Principles

- 小程序负责“拍和传”，Web 负责“看、改和导出”
- OCR 成功后再执行 AI 提取和分类
- 重复票不进入报销导出
- 技术方案围绕最小可用报销整理流程，不扩张成企业审批平台

## Tech Stack

| Layer | Technology |
| --- | --- |
| Mini Program | 微信小程序原生框架 |
| API | Python + FastAPI |
| Database | PostgreSQL + SQLAlchemy 2.0 + Alembic |
| Queue | Redis |
| Worker | Python 独立任务进程 |
| Storage | MinIO |
| OCR | PaddleOCR PP-OCRv5 |
| AI | DeepSeek OpenAI-compatible API |
| Web | Next.js 16 + React 19 + Tailwind CSS |
| Deployment | Docker + GitHub Actions + Nginx |

## Documents

- [Architecture](architecture.md)
- [Roadmap](roadmap.md)
