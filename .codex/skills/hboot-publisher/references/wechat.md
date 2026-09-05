# WeChat Official Account publishing rules

## Source of truth

Read `CLAUDE.md`, the latest two or three comparable files under `content/wechat/`, and any active series plan in that directory. Read the real product evidence behind the proposed article.

## Article standard

- Write for a broad Chinese audience. Explain the user problem before technical implementation.
- One article answers one clear question. Separate other directions into later articles instead of building a long all-in-one draft.
- The product is evidence, not the headline merely because a feature was added.
- Prefer a concrete scene, conflict, failure, cost, or decision. Avoid changelog prose, generic AI claims, and long technical tutorials.
- Describe AI's role only when it materially changed the work, and state the action precisely.
- Use natural Chinese with varied sentence openings. Remove AI-like summaries, inflated transitions, and slogans.
- Follow an active series plan's length and scope. For the virtual-payment series, keep each article focused and normally within its recorded 350–600 Chinese-character range.
- Verify time-sensitive platform rules before publication and use primary sources where available.

## Repository record

Create the Markdown draft under `content/wechat/` and update an active series plan when one exists. Preserve user-authored passages unless the user explicitly asks for body editing.

Generate a cover prompt only when requested. If the user asks to generate the cover text together with the image, include the exact Chinese headline, layout, style, aspect ratio, and legibility constraints in the prompt.

When the user says the article is published, update the active series plan or article status record that already exists. Do not add invented readership data or links.

## Preflight

- One question only.
- Broad reader can understand it without code knowledge.
- Real problem appears before the product feature.
- Technical details are limited to what changes the reader's understanding.
- Claims trace to user context, repository evidence, or current primary sources.
- User-written text remains unchanged unless revision was requested.
