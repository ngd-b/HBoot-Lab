# 53｜Audit logs can store secrets

- 日期：2026-09-22
- 状态：已发布

## English

> Audit logs can become a second secret store.
>
> Before logging config changes, check whether URLs or runtime values can carry credentials.
>
> I now store field names + “updated” flags. It costs debugging detail but keeps secret values out.
>
> Would you keep masked values instead?

## 中文校对

> 审计日志也可能变成第二个秘密存储库。
>
> 记录配置变更前，先检查 URL 或运行参数值里是否可能带有凭据。
>
> 我现在只保存字段名和“已更新”标记。这会损失排查细节，但能避免把秘密值写进日志。
>
> 你会改为保留脱敏后的值吗？

## 配图

纯文字发布。这个改动发生在审计记录的数据边界，配置页面截图不能证明敏感值未被保存。

## 发布依据

- unified-ai 提交 `1305ee5`（2026-09-22）修改服务商与能力服务更新审计：不再记录完整 `base_url` 和运行配置值，改为记录 `baseUrlUpdated`、`runtimeConfigFields`、`credentialsUpdated` 等变更标记或字段名。
- `server/tests/test_audit_logs.py` 新增回归测试，用包含查询参数令牌的 URL 和私有运行参数值更新服务商，并断言这些值不出现在审计日志中，同时保留名称、字段名和更新标记。
- 正文描述的是已修复的数据记录行为；“损失排查细节”是删除旧值和新值后的直接取舍。结尾的脱敏值方案仍是待讨论选项，不声称已经实现或验证。正文不声称真实密钥已经泄露，也不扩展为所有日志字段均已完成敏感信息审查。

## 发布后记录

- X 链接：
- 实际时间：2026-09-22 11:01:23（Asia/Shanghai）
- Impressions：
- Likes：
- Replies：
- Reposts：
- Bookmarks：
- 观察：
