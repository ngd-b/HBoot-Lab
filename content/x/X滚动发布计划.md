# X 滚动发布计划

账号：[X @bhboot42633](https://x.com/bhboot42633)

## 发布规则

- 账号定位：面向全球独立开发者、AI Builder 和正在把产品做上线的人，不以获取微信小程序终端用户为主要目标。
- 发布语言：只发英文；中文只用于内部校对，以及复用到公众号、视频号、小红书等中文平台。
- 同一条帖子不做中英双语，不在英文内容之间穿插中文测试，避免受众和账号语言信号反复变化。
- 每天一条主帖；当天项目进展有明确用户价值时，可在两小时后再发一条进度帖。
- 主帖暂定北京时间 21:30，进度帖暂定 23:30。
- 每条只解决一个问题，不写产品更新流水账。
- 只有图片能解释关系、形成对比或提供证据时才配图。
- 每天完成 3–5 条有内容的回复或引用回复。

## 内容偏向

X 上可以把微信小程序作为真实案例，但不能把帖子写成只对微信生态内用户有意义的功能通知。选题必须先找到全球开发者都能理解的问题，再用实际完成的小程序功能作为证据。

优先发布：

1. AI 参与真实产品开发的过程：AI 做了什么、哪里不够、人工如何判断和收尾。
2. 独立开发者上线产品时遇到的具体问题：支付、订单、数据一致性、审核、获客、转化和运营。
3. 从“功能能运行”到“产品可以放心使用”的改进：失败恢复、后台管理、状态确认、异常处理和体验细节。
4. 一个具体产品决策及其取舍：为什么这样设计，放弃了什么，实际解决了什么问题。
5. 可迁移的开发经验：即使读者不使用微信，也能把这条经验用到自己的产品里。

降低优先级或不单独发布：

- 只有“新增了某功能”的更新通知。
- 需要先了解微信规则、中文界面或产品历史才能看懂的内容。
- 只罗列开发步骤、版本号、技术名词或功能清单的流水账。
- 没有真实依据的用户反馈、收入、增长效果和情绪化故事。
- 与独立开发、AI 产品和产品上线无关的零散主题。

### 小程序内容的转换方式

不要把“微信小程序”本身当成吸引点。先讲普遍问题，再交代这个问题是在小程序里解决的。

- 弱：`I added virtual payments to my WeChat Mini Program.`
- 强：`A successful payment doesn't always mean the user received their credits. I built order recovery before calling the payment flow done.`
- 弱：`I built an admin page for my Mini Program.`
- 强：`Once real payments are involved, I need to answer three questions quickly: Did the payment succeed? Were the credits delivered? Can the order be recovered?`

涉及微信特有规则时，只有它能带出一个更普遍的产品或开发判断才发；纯微信教程留给中文平台。

## 创作说明

X 帖不是文章摘要，也不是版本更新日志。它首先要让尚未了解 HBoot 产品的读者看懂场景，并产生“我也遇到过”的感觉，然后再说明这次实际做了什么。

### 内容结构

1. 用一个具体场景、麻烦或错误开头，让陌生读者不需要了解产品背景也能看懂。
2. 直接说明这次做了什么，以及用户现在能得到什么具体结果。
3. 能用真实结果证明时，附界面截图、前后对比或短视频；视觉素材必须与正文描述的是同一件事。
4. 写到结果即可，不强行补一段抽象道理、口号或“产品启示”。

例如，不要从“我给某产品增加了某功能”开始；可以先写“一张张制作和保存表情很麻烦”，再写“现在上传一张照片就能生成并保存 8 张表情”。

### 表达要求

- 使用自然、口语化的表达，像向同行或用户讲刚刚完成的一件事。
- 前两行必须出现具体问题、意外结果或明确反差，不能先介绍产品背景。
- 使用开发者日常会说的短句和常用词，不直译中文长句，不写演讲式金句。
- 多写真实动作、具体对象、数字和结果，少写“可靠性很重要”“产品应该如何”这类脱离场景的结论。
- 产品名不能承担开头的吸引力；即使读者第一次看到这个名字，也应能独立理解整条帖子。
- 不编造用户反馈、情绪、效果数据或开发动机。没有证据时，只写已经完成并验证的事实。
- 不为了互动生硬提问。只有确实存在可讨论的选择、经验或分歧时，才邀请读者回应。

### 选题连续性

- 一个发布周期集中在同一类读者关心的主题，避免连续帖子在图片工具、底层架构、英语学习和视频制作之间无关联跳转。
- 不同产品可以出现，但要由同一个读者问题连接，例如“独立开发者怎样把一个真实需求做成可用产品”。
- 功能进展只有在能说明具体使用场景、变化或结果时才单独发布；纯版本号、常规修复和功能清单只做内部记录。

### 发布前检查

- 第一行是否能让不了解产品的人看懂？
- 不使用微信的海外开发者，是否也能从中获得一个具体经验？
- 内容是在讲一个普遍问题，还是只在播报小程序功能？
- AI 的参与是真实且具体的，还是为了蹭话题临时加上的？
- 是否有一个具体场景，而不是只有概念或结论？
- 是否清楚说明做了什么和得到什么结果？
- 是否删除了文章腔、总结腔和抽象口号？
- 如果功能适合展示，是否准备了真实结果图或短视频？
- 所有事实是否都有仓库记录、实际产品或用户提供的信息支撑？

## 帖子索引

| 编号 | 日期 | 主题 | 状态 |
| --- | --- | --- | --- |
| 01 | 2026-08-25 | [Build for the task, not the demo](posts/01-build-for-the-task-not-the-demo.md) | 已发布 |
| 03 | 2026-08-26 | [Same identity does not mean same account data](posts/03-same-identity-does-not-mean-same-account-data.md) | 已发布 |
| 04 | 2026-08-26 | [Three rules for ads in utility products](posts/04-three-rules-for-ads-in-utility-products.md) | 已发布 |
| 05 | 2026-08-25 | [Reliability is part of the product](posts/05-reliability-is-part-of-the-product.md) | 已发布 |
| 06 | 2026-08-25 | [Reuse existing outputs](posts/06-reuse-existing-outputs.md) | 已发布 |
| 10 | 2026-08-28 | [Less choice can create more practice](posts/10-less-choice-can-create-more-practice.md) | 已发布 |
| 11 | 2026-08-27 | [The second video has a starting point](posts/11-the-second-video-has-a-starting-point.md) | 已发布 |
| 12 | 2026-08-28 | [Know when not to fill a field](posts/12-know-when-not-to-fill-a-field.md) | 已发布 |
| 13 | 2026-08-28 | [The preview is a promise](posts/13-the-preview-is-a-promise.md) | 已发布 |
| 14 | 2026-08-28 | [Shared AI capabilities, separate product data](posts/14-shared-ai-capabilities-separate-product-data.md) | 已发布 |
| 15 | 2026-08-29 | [Build prepares, runtime stays restricted](posts/15-build-prepares-runtime-stays-restricted.md) | 待发布 |
| 16 | 2026-08-30 | [Low revenue, high UX cost](posts/16-low-revenue-high-ux-cost.md) | 已发布 |
| 17 | 2026-09-02 | [The product is the pack](posts/17-the-product-is-the-pack.md) | 已发布 |
| 18 | 2026-09-02 | [Placement changes the trade-off](posts/18-placement-changes-the-tradeoff.md) | 已发布 |
| 19 | 2026-09-02 | [One photo, eight stickers](posts/19-one-photo-eight-stickers.md) | 已发布 |
| 20 | 2026-09-02 | [Credit packs are live](posts/20-credit-packs-are-live.md) | 已发布 |
| 21 | 2026-09-04 | [Can the credits still be reclaimed?](posts/21-can-the-credits-still-be-reclaimed.md) | 暂缓：需解释过多前提 |
| 22 | 2026-09-04 | [AI can’t make users pay](posts/22-ai-cant-make-users-pay.md) | 已发布 |
| 23 | 2026-09-04 | [No more guessing about payment orders](posts/23-no-more-guessing-about-payment-orders.md) | 已发布（中文） |

## 每日进度帖

进度帖不提前硬填。每天从最新项目活动中选择，只有能形成“问题—选择—用户收益”的内容才新建单独文件，并补入上方索引。纯版本发布、常规修复、测试补充和无法解释用户价值的更新只留在开发记录中。

## 发布复盘

每连续发布 7 天复盘一次：比较曝光、回复、转发、收藏、纯文字与配图表现，以及长期主帖和当天进度帖的差异。若某个主题回应明显更好，继续深入同一个用户问题，不重复原句。

语言不再作为日常变量反复测试。至少连续发布 20 条英文帖后再复盘内容表现；重点看精准关注、主页访问、回复和收藏，曝光只作为辅助指标。

### 2026-09-04 语言方向调整

- 前几周英文帖的单条曝光曾达到约 100–200。
- 切换中文后的数日，单条曝光降至个位数。
- 从下一条开始恢复并持续发布英文，不删除已经发布的中文帖。
- 这次数据只能支持“当前账号继续英文发布”，不能证明所有中文内容在 X 上都没有受众。

### 2026-09-02 表现基线

- 当前已发布帖子的单条曝光最高约为 100–200。
- 暂未记录具体是哪一条帖子达到最高曝光，也没有各帖的完整互动数据。
- 现阶段先把 100–200 作为账号的初始曝光基线，不据此判断哪类主题更有效；复盘前需补齐各帖的 Impressions、Likes、Replies、Reposts 和 Bookmarks。

最近一次素材扫描时间：`2026-09-04T06:30:29+08:00`
