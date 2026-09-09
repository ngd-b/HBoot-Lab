# 32｜Keep AI jobs out of the client

- 日期：2026-09-09
- 状态：已发布
- 字符数：258

## English

> Closing the app shouldn’t erase an AI background-removal job.
>
> My sticker tool will run on mobile and web, so I’m keeping jobs on the server, not in either client. Both sides will read the same task status, credits, and files without syncing separate copies.

## 中文校对

> 关掉应用，不应该让一个 AI 去背景任务跟着消失。
>
> 我的贴纸工具会同时运行在移动端和 Web 端，所以任务统一放在服务端，而不是任何一个客户端里。两端读取同一份任务状态、积分和文件，不需要再同步两套副本。

## 配图

纯文字发布。当前只有内部架构图，没有能够证明跨端任务状态的完整产品界面；等任务链路完成后再用真实状态页或录屏展示。

## 发布依据

- 贴纸产品计划同时提供移动端与 Web 操作端，两端只访问同一个 Sticker Server。
- 去背景和高清导出被设计为服务端任务，由产品服务保存任务状态和平台请求编号。
- 用户、作品、任务、积分和文件由同一套产品数据与存储管理，不在两个客户端各自维护副本。
- 当前项目仍处于开发阶段，因此正文使用进行时和将来时描述正在落实的架构，不宣称跨端链路已经上线。

## 发布后记录

- X 链接：
- 实际时间：2026-09-09 15:47
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
