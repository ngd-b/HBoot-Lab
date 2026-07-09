# 🧪 HBoot-Lab

> Build in Public. Learn by Building. Grow by Sharing.

HBoot-Lab is my public laboratory.

This repository documents the complete journey of building software—from an idea to a real product.

Unlike a traditional technical blog, this repository focuses on **real projects**, **real decisions**, **real failures**, and **real lessons learned**.

Every product deserves a story, not just source code.

---

## 🎯 Mission

This repository exists to record the entire lifecycle of a product.

Including:

- 💡 Product ideas
- 🏗 Architecture design
- 🤖 AI experiments
- 🔬 Technology selection
- 📝 Development journals
- 🐞 Bugs and debugging
- 🚀 Product launches
- 📊 User feedback
- 📈 Product iterations
- 💰 Monetization attempts
- 🎉 Successes and failures

The goal is to leave a complete record of every project.

---

## 📂 Repository Structure

```text
.
├── projects/          # Product development logs
├── experiments/       # AI & technical experiments
├── journals/          # Development journals
├── reviews/           # Weekly / Monthly reviews
├── ideas/             # Product ideas
├── marketing/         # SEO, growth, promotion
├── assets/            # Images, diagrams, screenshots
└── templates/         # Writing templates
```

---

## 🚀 Current Projects

| Project                    | Status       |
| -------------------------- | ------------ |
| AI Background Remover      | ✅ Online    |
| Quick English Mini Program | ✅ Online    |
| Personal Website           | ✅ Online    |
| Tool Website               | 🚧 Iterating |

---

## ✍️ What You Will Find Here

Instead of writing only about technologies, I write about the process of building products.

Examples:

- Why I built this product.
- Why I chose one technology over another.
- Problems I encountered.
- How I solved them.
- What I learned.
- What I would do differently next time.

The focus is on **building**, not just coding.

---

## 📚 Difference from Learning-Blog

This repository is **NOT** a technical knowledge base.

| Learning-Blog       | HBoot-Lab            |
| ------------------- | -------------------- |
| Learn technologies  | Build products       |
| Tutorials           | Development journals |
| Technical notes     | Product stories      |
| Framework knowledge | Real-world practice  |
| Concepts            | Decisions & lessons  |

Learning-Blog answers:

> **"What did I learn?"**

HBoot-Lab answers:

> **"What did I build?"**

---

## 🌱 Principles

- Build first.
- Share honestly.
- Document everything.
- Learn continuously.
- Focus on solving real problems.
- Ship small and iterate fast.

No fake stories.

No exaggerated achievements.

Only real experience.

---

## 📝 Writing Workflow

```text
Idea
    ↓
Design
    ↓
Development
    ↓
Experiment
    ↓
Reflection
    ↓
Article
    ↓
Publish
```

Every meaningful step should leave a record.

---

## 🎯 Long-term Goal

I hope that years later, this repository will become a complete archive of my journey as an independent developer.

Not just successful projects, but also unfinished ideas, failed experiments, lessons learned, and everything in between.

Because every product is worth remembering.

---

## 🛠 Local Setup

After cloning this repository, run these two commands once (per machine):

```bash
git lfs install                       # fetch large files (images/videos) via Git LFS
git config core.hooksPath .githooks   # enable the pre-commit secret scanner
```

> Both are **local** settings that `git clone` does **not** carry over —
> run them again on every new machine.

### Git hooks

`core.hooksPath` activates the pre-commit secret scanner, which blocks
commits that look like they contain API keys, tokens, or private keys.

To bypass the scanner on a false positive:

```bash
git commit --no-verify
```

### Large files (Git LFS)

Images, videos, and other binaries (`*.png`, `*.jpg`, `*.webp`, `*.pdf`,
`*.mp4`, …) are stored via **Git LFS** so the repo history stays lightweight.
See [.gitattributes](.gitattributes) for the tracked patterns. Just `git add`
them as usual — LFS handles the rest. If you clone without `git lfs install`,
image files will appear as small text pointers instead of real content.

### Private content

Keep private content (revenue details, raw interviews, secrets) out of the
public history by placing it in `drafts/` or naming files `*.private.md` —
both are ignored via `.gitignore`.

---

## 👋 About Me

I'm HBoot, a frontend developer exploring AI, indie hacking, automation, and product development.

Building products, learning every day, and sharing the journey.

If any article or project is helpful to you, I'm glad this lab has fulfilled its purpose.
