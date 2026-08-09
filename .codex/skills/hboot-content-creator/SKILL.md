---
name: hboot-content-creator
description: Discover, evaluate, and create HBoot content from real repository activity. Use when Codex needs to determine what HBoot should publish next, review updates since the latest WeChat article, compare product-development and technical-blog topics, produce a weekly content brief, or draft a new HBoot WeChat Official Account article from verified work in the configured repositories.
---

# HBoot Content Creator

Turn repository activity into one evidence-based HBoot article idea or draft. Prefer a clear experience, decision, failure, or lesson over a changelog recap.

## Workflow

### 1. Establish the time boundary

Run:

```bash
python3 .codex/skills/hboot-content-creator/scripts/collect_updates.py
```

Treat the latest committed creation of a Markdown file under `content/wechat/` as the default boundary. The script uses the Git addition commit, not filesystem modification time. If the user provides a date or asks for a fixed period, pass `--since <ISO-date>`.

Report the selected boundary, article title, file, commit, and timestamp. Do not silently substitute another date.

### 2. Collect and classify activity

Use the repositories in `references/repositories.json`. Keep these source classes separate:

- `product`: primary evidence for product stories.
- `product-component`: merge into its named product when reasoning.
- `technical-content`: source for standalone technical articles or practical technical reflections.
- `infrastructure`: supporting context unless it contains a strong independent decision or failure.

Treat release-only, test-only, chore-only, and routine documentation commits as supporting activity. In a `technical-content` repository, documentation commits are primary material.

Do not treat uncommitted work as completed. Mention it separately only when the user explicitly asks.

### 3. Verify promising changes

Use the scan only for discovery. For every serious candidate:

1. Read the relevant changelog or release notes when present.
2. Inspect selected commits with `git show --stat` and, when needed, the focused diff.
3. Read the latest two or three WeChat articles to avoid repeating the same thesis and to match the established voice.
4. Read `CLAUDE.md` before drafting and follow its scope and writing principles.

Do not infer motivation, user feedback, business results, or emotion from commit messages. Ask one focused question or mark the fact as unknown when the missing detail materially affects the story.

### 4. Build themes, not repository summaries

Group updates by the user problem or decision they reveal. A theme may combine repositories only when one thesis genuinely connects them.

Good theme shapes include:

- A launched product moved from “works” to “feels reliable.”
- A retention experiment exposed a product decision.
- A small bug changed how trustworthy a product felt.
- A technical study became usable code in a real product.
- Removing or simplifying something produced more value than adding a feature.

Avoid “this week I made N commits across M repositories” as the article structure.

### 5. Score and decide

Score each candidate from 0–3 on five dimensions:

- Evidence: enough verified facts and concrete scenes exist.
- Reader value: the lesson transfers beyond the repository.
- Tension: there is a problem, tradeoff, surprise, failure, or change in judgment.
- Freshness: it does not repeat the latest articles.
- Cohesion: it supports one clear thesis without forced connections.

Use these thresholds:

- 11–15: recommend a full WeChat article.
- 8–10: recommend a short post, or identify the missing evidence needed for a full article.
- 0–7: do not force publication.

Choose one primary topic. Include at most two alternatives and explain the tradeoff briefly.

### 6. Produce the requested output

For “what can I write?” or “is there enough content?”, return:

1. Time boundary and its source.
2. Compact repository activity summary.
3. Ranked candidate themes with scores.
4. One recommendation, central thesis, working titles, and outline.
5. Missing facts that would materially improve the article.

For “write/create/draft the article,” perform the same research, then create a Markdown draft under `content/wechat/` unless the user gives another destination. Follow the recent article style, but do not mechanically copy sentence rhythm or structure. Use the next `HBoot-Lab #NNN` number only when the existing series makes that number unambiguous.

Before finishing a draft:

- Trace every factual claim to repository evidence or user-provided context.
- Remove raw commit hashes, implementation trivia, and release-number lists unless essential to the story.
- Do not invent usage metrics, feedback, intent, or outcomes.
- End with a concrete reflection rather than a generic slogan.
- Do not generate cover art unless requested.

## Script options

```bash
# Explicit period
python3 .codex/skills/hboot-content-creator/scripts/collect_updates.py \
  --since 2026-08-01 --until 2026-08-10

# Machine-readable output
python3 .codex/skills/hboot-content-creator/scripts/collect_updates.py \
  --format json

# Show uncommitted work separately
python3 .codex/skills/hboot-content-creator/scripts/collect_updates.py \
  --include-working-tree
```

Pass `--lab-root` when running outside the HBoot-Lab working tree. Pass `--config` to use a different repository set.
