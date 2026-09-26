# 60｜Payments during account merges

- 日期：2026-09-26
- 状态：已发布
- 字符数：240

## English

> A successful payment can reach an account that's just been merged.
>
> I changed fulfillment to detect that handoff and request a retry against the surviving account, so an account merge doesn't turn a valid payment into a permanent rejection.

## 中文校对

> 支付成功的通知到达时，原账号可能刚刚被合并。
>
> 我调整了发放逻辑：识别这次账号切换，并要求向合并后保留的账号重试，避免账号合并让一笔有效支付被永久拒绝。

## 配图

纯文字。没有真实支付事故或用户损失数据，不制作交易截图。

## 发布依据

- 本轮扫描起点为公众号 #031《记一句英语，把使用场景也带上》的新增提交 `f9578ef`，时间为 2026-09-26 01:44:01（北京时间）。
- `ai-invoice` 提交 `a47cdd8`（2026-09-26）调整 `billing_fulfillment_service.py`：获取用户锁后重新读取状态，若原账号已不可用且身份解析指向另一个账号，返回可重试的 503 / ACCOUNT_MAPPING_CHANGED。
- 同一提交中的 `test_payment_racing_with_merge_is_retryable` 覆盖首次返回可重试错误、再次处理后积分记入保留账号的场景。本次只阅读实现和测试代码，未执行测试。
- 正文描述已提交的处理逻辑，不声称已部署、发生过真实支付事故或追回了用户资金。

## 发布后记录

- X 链接：
- 实际时间：2026-09-26 18:59（北京时间）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
