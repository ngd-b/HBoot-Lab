# X publishing rules

## Source of truth

Read `content/x/X滚动发布计划.md` completely before creating or substantially revising an X post. Read the latest two or three relevant files under `content/x/posts/` and the source content or product evidence for the new post.

## Audience and language

- Public posts are English only. Chinese is allowed only as an internal translation in the repository file.
- Write for global indie developers, AI builders, and people shipping products.
- Do not assume the reader uses WeChat or knows what a Mini Program is.
- Do not put `Mini Program`, WeChat-specific dashboard fields, or Chinese ecosystem terminology in the public copy unless that detail is essential to a transferable point. Default to universal terms such as `app`, `app review`, `payment`, `privacy form`, or `order dashboard`.
- The real Mini Program may remain in the internal evidence section.

## Post standard

- One post, one problem.
- The first two lines must show a concrete problem, surprise, or contrast that a new reader can understand.
- Then state what was actually done and the concrete result. Stop there; do not append a slogan or generic lesson.
- Use short, natural developer language. Avoid translated Chinese syntax, article summaries, release logs, and forced engagement questions.
- Mention AI only when its real action is known. Say what AI scanned, drafted, compared, generated, or changed, plus any human check that actually happened.
- Do not invent user reactions or performance data.
- Keep a normal single post within 280 characters unless the user explicitly asks for a thread or has specified a different account limit.
- Do not add hashtags by default.
- Add an image only when it supplies evidence, shows a result, or explains a relationship. A Chinese screenshot that requires lengthy context is usually not useful for the global audience.

## Repository record

For a new main post:

1. Use the next number after the highest indexed post.
2. Create `content/x/posts/NN-short-english-slug.md`.
3. Include: title, date, status, `English`, `中文校对`, image decision, publication evidence, and post-publication fields.
4. Add the post to `content/x/X滚动发布计划.md` as `待发布`.

For an X reply, normally return one concise English reply that acknowledges the comment and adds one useful point. Do not create a new numbered post unless the user asks to record it.

When the user says the post is published, change both the post file and index to `已发布` and record the current time in the post. Leave the link blank if none was supplied.

## Preflight

- English public copy only.
- Understandable without WeChat context.
- First two lines contain a real hook.
- One problem, one actual action, one result.
- AI involvement is specific and factual when included.
- Within the intended post length.
- Draft file and index agree.
