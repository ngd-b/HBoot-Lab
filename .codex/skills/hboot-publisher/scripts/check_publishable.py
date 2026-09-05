#!/usr/bin/env python3
"""Check deterministic HBoot publishing invariants without external packages."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SECTION_RE = r"(?ms)^## {heading}\s*\n(.*?)(?=^## |\Z)"
CJK_RE = re.compile(r"[\u3400-\u9fff]")


def get_section(text: str, heading: str) -> str | None:
    match = re.search(SECTION_RE.format(heading=re.escape(heading)), text)
    return match.group(1).strip() if match else None


def get_quote(section: str) -> str:
    lines: list[str] = []
    for line in section.splitlines():
        if line.startswith(">"):
            lines.append(line[1:].lstrip())
    return "\n".join(lines).strip()


def check_x(text: str, allow_platform_context: bool) -> tuple[list[str], str]:
    errors: list[str] = []
    for heading in ("English", "中文校对", "配图", "发布依据", "发布后记录"):
        if get_section(text, heading) is None:
            errors.append(f"missing section: {heading}")

    english_section = get_section(text, "English") or ""
    post = get_quote(english_section)
    if not post:
        errors.append("English section has no blockquoted public copy")
    if CJK_RE.search(post):
        errors.append("English public copy contains Chinese characters")
    if len(post) > 280:
        errors.append(f"English public copy is {len(post)} characters; limit is 280")

    if not allow_platform_context:
        banned = ("mini program", "wechat", "微信", "小程序")
        lowered = post.lower()
        found = [term for term in banned if term in lowered or term in post]
        if found:
            errors.append("public copy contains platform-specific context: " + ", ".join(found))

    if not re.search(r"(?m)^- 状态：(待发布|已发布)", text):
        errors.append("missing or invalid publication status")
    return errors, f"X public copy: {len(post)} characters"


def check_video(text: str) -> tuple[list[str], str]:
    errors: list[str] = []
    required = ("口播母版", "平台标题", "发布描述", "标签", "画面与来源")
    for heading in required:
        if get_section(text, heading) is None:
            errors.append(f"missing section: {heading}")

    spoken = get_section(text, "口播母版") or ""
    first_line = next((line.strip() for line in spoken.splitlines() if line.strip()), "")
    if not first_line:
        errors.append("spoken master has no opening line")
    if not re.search(r"(?m)^- 状态：(待拍摄|已发布)", text):
        errors.append("missing or invalid episode status")
    return errors, f"Video opening: {first_line}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("content_file", type=Path)
    parser.add_argument("--allow-platform-context", action="store_true")
    args = parser.parse_args()

    path = args.content_file
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    normalized = path.as_posix()
    if "/content/x/posts/" in f"/{normalized}":
        errors, summary = check_x(text, args.allow_platform_context)
    elif "/content/video/scripts/" in f"/{normalized}":
        errors, summary = check_video(text)
    else:
        print("ERROR: expected a file under content/x/posts or content/video/scripts", file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
