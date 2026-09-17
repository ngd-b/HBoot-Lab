# 46｜Offline practice still counts

- 日期：2026-09-17
- 状态：已发布

## English

> A practice can finish while the phone has no connection, and the event just disappears.
>
> My English app writes learning events to a local queue first, keeps them through a dropped connection, and syncs them in batches once it's back—deduplicating by event ID.
>
> Offline practice still gets recorded, and never twice.

## 中文校对

> 练习可能在手机断网时完成，事件就这样丢失。
>
> 我的英语应用先把学习事件写进本地队列，断网时保留，恢复后分批同步，并按事件 ID 去重。
>
> 离线练习依然会被记录，而且不会重复记录。

## 配图

纯文字发布。本地队列与幂等去重是后台行为，静态截图无法证明断网保留和去重结果。

## 发布依据

- [场景外语学习架构](../../../products/quick-english/architecture.md) 记录学习事件进入本地可靠队列，断网时保留，恢复后分批补传并按事件 ID 去重。
- [场景外语学习路线图](../../../products/quick-english/roadmap.md) 已记录“离线学习事件队列、批量补传和幂等去重”完成。
- 正文只描述已完成的产品行为，没有声称留存或学习效果提升。

## 发布后记录

- X 链接：
- 实际时间：
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
