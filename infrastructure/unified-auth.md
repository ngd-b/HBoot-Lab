# Unified Auth

HBoot 统一用户平台，目标是让多个产品共享一套账号、登录、安全和产品关系能力。

## Status

🧪 Core Flow Implemented / Not Fully Tested / Not Integrated

当前仓库已经完成核心账号链路、Web 授权码流程和生产部署骨架，但尚未完成完整测试，也没有任何现有产品依赖它。以下“已实现”表示代码已经具备，不代表现有产品已接入或能力已经过生产验证。

## Why

智能去背景、急用英语和 AI 发票助手分别实现了自己的微信登录、Token、用户身份和 Web 登录流程。产品增加后会带来：

- 相同认证链路重复开发
- Token 生命周期和刷新策略不一致
- 每个产品分别维护微信 AppSecret
- Web、小程序和产品后端身份难以统一
- 用户无法查看跨产品账号、安全记录和授权关系

Unified Auth 希望把这些重复能力收敛成公共平台。

## Implemented in Code

- Web 邮箱验证码登录
- Google 和 GitHub OAuth
- 微信小程序静默登录
- 微信小程序确认 Web 扫码登录
- RS256 Access Token 和 Refresh Token
- Refresh Token Rotation 与重放检测
- JWKS 公钥分发，产品后端本地验签
- 同一开放平台下基于 UnionID 统一多个小程序微信身份
- 邮箱绑定、登录设备、Session 和安全日志管理
- 产品注册、API Key 和微信配置管理
- Web Authorization Code + PKCE 登录
- 阿里云 DirectMail / Resend 邮件 Provider 切换
- 中英文界面与语言偏好
- 存活 / 就绪健康检查、部署后冒烟检查和标签发布工作流

## Current Architecture

```text
Web / 微信小程序 / 产品后端
              │
              ▼
     Next.js Unified Auth
        ├── Better Auth
        ├── WeChat Login API
        ├── JWT / JWKS
        ├── Product Registry
        ├── Security / Admin UI
        ├── Prisma ───── Shared PostgreSQL
        ├── ioredis ──── Shared Redis
        └── Email ────── Aliyun DirectMail / Resend
```

## Technology

| Layer | Technology |
| --- | --- |
| Application | Next.js 16 + React 19 |
| Auth Framework | Better Auth |
| Database | Prisma + PostgreSQL |
| Cache / Token State | Redis |
| JWT | jose + RS256 |
| Email | Resend |
| UI | Tailwind CSS |
| Deployment | Docker Compose |

统一用户通过全局用户 ID 与各产品本地用户建立映射；统一平台只管理身份、登录设备和产品注册关系，不保存产品业务数据。

## Planned Integration

```text
Unified Auth 自身测试
        ↓
急用英语试点
        ↓
AI 发票助手
        ↓
智能去背景
```

Web 产品的授权码 + PKCE 流程已经实现；小程序最小身份桥接仍是下一步。目标接入方式：

- 小程序把 `wx.login()` 的 code 发送到统一平台
- 产品后端使用各自 API Key 调用统一平台的微信身份解析接口
- 统一平台根据产品配置调用微信 `code2session`，返回全局用户 ID 和当前产品 OpenID
- 产品查找或创建本地用户并登记映射，继续签发原有 Token / Session
- Web 产品没有 Session 时通过 Authorization Code + PKCE 跳转统一登录页并换取身份
- 最小接入不迁移业务数据，也不要求小程序前端和鉴权中间件一次性重构

## Current Gaps

- [ ] 完成统一平台自身的功能测试
- [ ] 建立单元测试、集成测试和端到端测试
- [ ] 验证邮箱、Google、GitHub 和微信登录链路
- [ ] 验证 RS256 密钥生成、JWKS 缓存和安全轮换
- [ ] 实现并验证小程序最小身份桥接接口
- [ ] 实现 Node.js 产品接入 SDK
- [ ] 实现 Python 产品接入 SDK
- [ ] 验证旧用户与统一用户的映射和迁移
- [ ] 验证 Access Token / Refresh Token 升级兼容
- [ ] 选择一个低风险产品完成首次接入
- [ ] 为每个产品准备独立回滚方案
- [ ] 完成首次生产部署和部署后冒烟验证

## Important Boundary

在完成测试和首个产品接入之前：

- 三个产品继续使用各自现有认证体系
- Unified Auth 故障不会影响现有产品
- 不对外宣称已经实现“一号通行所有产品”
- 接入方案属于设计和开发素材，不是已上线能力
