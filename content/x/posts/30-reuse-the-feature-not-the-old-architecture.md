# 30｜Reuse the feature, not the old architecture

- 日期：2026-09-08
- 状态：已发布
- 字符数：244

## English

> I’m turning one feature into its own app, and the easiest mistake would be copying the whole old stack with it.
>
> My rule: reuse the sticker logic, not the product architecture. The new app owns its data; identity and AI stay behind shared APIs.

## 中文校对

> 我正在把一个功能拆成独立应用，最容易犯的错，就是顺手把旧项目整套架构也搬过去。
>
> 我的原则是：只复用贴纸逻辑，不复用旧产品架构。新应用自己管理数据，身份认证和 AI 能力继续走公共接口。

## 配图

纯文字发布。现有架构图包含中文平台名和内部组件，全球受众需要额外理解成本；正文已经能独立讲清复用边界。

## 发布依据

- 新的贴纸产品从现有抠图产品中拆分，架构文档明确只复用贴纸模板、布局与领域逻辑。
- 新产品不沿用旧产品的认证、数据库和 AI 接入方式，而是对接统一认证平台与统一能力平台。
- 产品自身的数据仍由新产品服务管理，公共平台只承载身份认证和 AI 能力。
- 当前项目仍处于开发阶段，因此正文描述的是已确定的架构原则，不宣称产品已经上线。

## 发布后记录

- X 链接：
- 实际时间：2026-09-08 11:38
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
