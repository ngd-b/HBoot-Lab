# 15｜Build prepares, runtime stays restricted

- 日期：2026-08-29
- 状态：待发布
- 实际时间：

## English

> My migration image used `npm ci --ignore-scripts`.
>
> That also skipped Prisma’s engine setup—the runtime files needed when migrations run.
>
> I changed the image to prepare Prisma during build, then drop to a non-root user for execution.
>
> Build prepares. Runtime stays restricted.

## 中文

> 我的数据库迁移镜像使用了 `npm ci --ignore-scripts`。
>
> 但这也跳过了 Prisma 引擎准备，执行迁移时缺少真正需要的运行文件。
>
> 我把 Prisma 的准备放回镜像构建阶段，再让迁移继续以非 root 用户运行。
>
> 构建负责准备，运行时继续受限。

## 配图

纯文字发布。代码差异很小，截图不能比正文更清楚地解释问题。

## 发布依据

- 统一用户平台提交 `85c6a663`：迁移镜像从 `npm ci --ignore-scripts` 改为在构建阶段执行完整的 `npm ci`。
- 镜像仍在依赖准备完成后切换为非 root 用户执行迁移。
- 新增测试，固定依赖安装必须发生在切换用户之前，并防止重新加入 `--ignore-scripts`。
- 修复已包含在统一用户平台 `v2.3.1` 发布提交中。

## 发布后记录

- X 链接：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
