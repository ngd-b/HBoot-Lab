# Roadmap

## Completed

- [x] 确定产品名 `HBoot贴纸表情包` 和仓库名 `sticker`
- [x] 确定微信小程序、Web 和服务端三端结构
- [x] 创建 pnpm workspace 和根目录项目骨架
- [x] 创建 Next.js 宣传页、用户工作台和管理控制台入口
- [x] 创建 Fastify 服务端、Prisma 数据模型和健康检查
- [x] 接入统一认证 Node.js SDK 骨架
- [x] 接入统一 AI 能力平台客户端骨架
- [x] 确定复用 `common-infra` 的 PostgreSQL、Redis 和 MinIO
- [x] 确定单一 Compose 配置和 Server、Web 独立发布规则
- [x] 建立版本发布日志规则和根目录 `CHANGELOG.md`
- [x] 通过 TypeScript 检查、服务端测试和完整构建

## Next

- [ ] 创建正式微信小程序 AppID，并导入微信开发者工具
- [ ] 在统一认证平台注册 `sticker` 产品及微信配置
- [ ] 为 `sticker` 开通 `common-infra` 的 PostgreSQL、Redis 和 MinIO 专属凭证
- [ ] 配置 PostgreSQL 数据库迁移、Redis 和对象存储
- [ ] 创建根目录 `compose.yml`，只定义 `server` 和 `web`
- [ ] 创建 Server 与 Web 各自的 GitHub Actions 部署工作流
- [ ] 打通小程序与 Web 登录、本地用户映射和会话
- [ ] 打通 `image.background-removal` 去背景任务
- [ ] 从原产品抽离并接入贴纸模板与布局能力
- [ ] 完成选图、去背景、生成、编辑和保存的 MVP 链路
- [ ] 完成作品、任务、积分和订单数据同步
- [ ] 完成管理端统计、日志和设置
- [ ] 补齐隐私指引、用户协议和审核材料

## Validation

- [ ] 记录“贴纸”“表情包”等搜索词的曝光和点击
- [ ] 对比名称、图标和介绍调整前后的点击变化
- [ ] 记录进入制作、完成生成和保存作品的转化漏斗
- [ ] 根据真实数据决定继续优化表达还是调整功能方向
