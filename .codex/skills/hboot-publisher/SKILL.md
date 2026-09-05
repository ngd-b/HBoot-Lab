---
name: hboot-publisher
description: Create, revise, record, and commit platform-ready HBoot content for X, short-form video, and WeChat Official Account. Use for posts, spoken-video episodes, articles, titles/descriptions/tags, publication records, and content Git commits. For repository-wide topic discovery without a publishing deliverable, use hboot-content-creator instead.
---

# HBoot Publisher

Apply the repository's current publishing rules even when the conversation has no earlier context. Treat repository files and the user's supplied text as the source of truth; do not reconstruct rules from memory.

## Route by channel

Identify the requested channel before drafting or revising:

- For X posts and X replies, read [references/x.md](references/x.md).
- For spoken short videos, read [references/video.md](references/video.md).
- For WeChat Official Account articles, read [references/wechat.md](references/wechat.md).

For new or substantially revised public content, also read `CLAUDE.md`, the complete live plan named in the channel reference, the relevant source evidence, and the latest two or three comparable published items. Do not use an old chat answer as the only source.

For a status-only or commit-only request, inspect the target content and its live index, but do not rewrite the content.

## Preserve authored content

- Text supplied or rewritten by the user is locked by default.
- If the user asks to update only the title, description, tags, cover prompt, status, or index, change only those fields.
- Do not polish, reorder, shorten, or append to locked text unless the user explicitly asks to revise that text.
- Published copy is immutable by default. After publication, only add the actual time, link, metrics, observations, and status unless the user explicitly requests a correction.
- When editing an existing draft, inspect the diff so user changes made between turns are not overwritten.

## Evidence and claims

- Use actual product behavior, repository evidence, or facts directly supplied by the user.
- Do not invent results, feedback, revenue, motivation, review rules, or emotional reactions.
- Keep product-specific details only when they prove the point. Lead with a reader problem, decision, or useful method.
- Verify current platform rules from primary sources when they materially affect the draft. Mark uncertain or time-sensitive details instead of presenting them as permanent facts.

## Record the work

When creating a publishable item, create or update its repository file and add it to the current channel index or series plan with status `待发布` or `待拍摄`. Do not merely return disposable chat copy.

Interpret common follow-ups as follows:

- `已发布`: use the user's statement as confirmation; record the current Asia/Shanghai date and time and mark the item published. Do not invent a URL.
- `提交`: this means create a Git commit, not publish to an external platform. Stage only the active content item and its index or plan, run `git diff --check`, commit with a scoped Chinese message, then report the commit ID.
- `已发布，提交`: update the publication record first, then commit it.
- `都提交`: include all clearly related content changes in the active publishing batch, while leaving unrelated user work untouched.

Never claim the worktree is clean without checking `git status --short` after the commit. If unrelated changes remain, report them without modifying them.

## Final check and response

Before presenting a draft, check the applicable channel reference item by item. Do not say it follows the rules if a required check was skipped.

For X posts and spoken-video scripts, also run:

```bash
python3 .codex/skills/hboot-publisher/scripts/check_publishable.py <content-file>
```

This catches structural, language, platform-context, and length mistakes. It does not replace the semantic preflight in the channel reference. Use `--allow-platform-context` only when the user explicitly wants WeChat or Mini Program context in an X post and the detail is essential.

Respond in Chinese, but keep the public copy in the channel's required language. Lead with the finished copy or recorded outcome. Keep process commentary brief. Mention the file path for a created or updated artifact. Do not commit unless the user asks.
