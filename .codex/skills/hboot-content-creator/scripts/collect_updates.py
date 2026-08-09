#!/usr/bin/env python3
"""Collect repository activity since the latest committed WeChat article."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


RECORD_SEPARATOR = "\x1e"
FIELD_SEPARATOR = "\x1f"
PRIMARY_PREFIXES = {"feat", "fix", "refactor", "perf", "security", "privacy"}
SUPPORTING_PREFIXES = {"build", "chore", "ci", "docs", "release", "style", "test"}


def run_git(repo: Path, args: list[str], *, check: bool = True) -> str:
    command = ["git", "--no-optional-locks", "-C", str(repo), *args]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown git error"
        raise RuntimeError(f"git failed in {repo}: {detail}")
    return result.stdout


def first_heading(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.startswith("# "):
                    return line[2:].strip()
    except OSError:
        pass
    return path.stem


def latest_content_creation(lab_root: Path) -> dict[str, str]:
    content_root = lab_root / "content" / "wechat"
    candidates: list[dict[str, str]] = []
    for path in sorted(content_root.glob("*.md")):
        relative = path.relative_to(lab_root).as_posix()
        output = run_git(
            lab_root,
            [
                "log",
                "--diff-filter=A",
                "--follow",
                "-1",
                f"--format=%cI{FIELD_SEPARATOR}%H{FIELD_SEPARATOR}%s",
                "--",
                relative,
            ],
        ).strip()
        if not output:
            continue
        created_at, commit, subject = output.split(FIELD_SEPARATOR, 2)
        candidates.append(
            {
                "created_at": created_at,
                "commit": commit,
                "subject": subject,
                "file": relative,
                "title": first_heading(path),
            }
        )
    if not candidates:
        raise RuntimeError(
            "No committed Markdown article was found under content/wechat; pass --since explicitly."
        )
    return max(candidates, key=lambda item: datetime.fromisoformat(item["created_at"]))


def commit_prefix(subject: str) -> str:
    head = subject.split(":", 1)[0].strip().lower().lstrip("@!# ")
    if "(" in head:
        head = head.split("(", 1)[0]
    return head if head else "other"


def is_material(kind: str, prefix: str) -> bool:
    if kind == "technical-content":
        return prefix not in {"build", "chore", "ci", "release", "test"}
    if prefix in PRIMARY_PREFIXES:
        return True
    if prefix in SUPPORTING_PREFIXES:
        return False
    return True


def parse_commits(output: str, kind: str) -> list[dict[str, Any]]:
    commits: list[dict[str, Any]] = []
    for record in output.split(RECORD_SEPARATOR):
        record = record.strip("\n")
        if not record:
            continue
        fields = record.split(FIELD_SEPARATOR, 3)
        if len(fields) != 4:
            continue
        commit, committed_at, subject, body = fields
        prefix = commit_prefix(subject)
        commits.append(
            {
                "commit": commit,
                "short_commit": commit[:8],
                "committed_at": committed_at,
                "subject": subject,
                "body": body.strip(),
                "category": prefix,
                "material": is_material(kind, prefix),
            }
        )
    return commits


def resolve_repo_path(lab_root: Path, configured_path: str) -> Path:
    path = Path(configured_path).expanduser()
    if not path.is_absolute():
        path = lab_root / path
    return path.resolve()


def scan_repository(
    lab_root: Path,
    entry: dict[str, str],
    since: str,
    until: str,
    include_working_tree: bool,
) -> dict[str, Any]:
    repo = resolve_repo_path(lab_root, entry["path"])
    result: dict[str, Any] = {**entry, "resolved_path": str(repo)}
    if not repo.is_dir() or not (repo / ".git").exists():
        result.update({"available": False, "error": "repository not found", "commits": []})
        return result

    try:
        output = run_git(
            repo,
            [
                "log",
                f"--since={since}",
                f"--until={until}",
                "--no-merges",
                "--date=iso-strict",
                f"--pretty=format:%H{FIELD_SEPARATOR}%cI{FIELD_SEPARATOR}%s{FIELD_SEPARATOR}%b{RECORD_SEPARATOR}",
            ],
        )
        commits = parse_commits(output, entry["kind"])
        categories = Counter(item["category"] for item in commits)
        result.update(
            {
                "available": True,
                "head": run_git(repo, ["rev-parse", "--short", "HEAD"]).strip(),
                "branch": run_git(repo, ["branch", "--show-current"]).strip() or "detached",
                "total_commits": len(commits),
                "material_commits": sum(1 for item in commits if item["material"]),
                "categories": dict(sorted(categories.items())),
                "commits": commits,
            }
        )
        if include_working_tree:
            status = run_git(repo, ["status", "--short"], check=False).splitlines()
            result["working_tree"] = status
    except RuntimeError as error:
        result.update({"available": False, "error": str(error), "commits": []})
    return result


def load_config(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    repositories = data.get("repositories")
    if not isinstance(repositories, list) or not repositories:
        raise RuntimeError(f"No repositories configured in {path}")
    required = {"name", "path", "kind", "group"}
    for index, entry in enumerate(repositories):
        if not isinstance(entry, dict) or not required.issubset(entry):
            raise RuntimeError(f"Invalid repository entry #{index + 1} in {path}")
    return repositories


def markdown_report(report: dict[str, Any]) -> str:
    boundary = report.get("boundary")
    lines = ["# HBoot content update scan", ""]
    lines.append(f"- Since: `{report['since']}`")
    lines.append(f"- Until: `{report['until']}`")
    if boundary:
        lines.extend(
            [
                f"- Boundary source: {boundary['title']}",
                f"- Boundary file: `{boundary['file']}`",
                f"- Boundary commit: `{boundary['commit'][:8]}`",
            ]
        )
    else:
        lines.append("- Boundary source: explicit `--since`")

    lines.extend(
        [
            "",
            "## Summary",
            "",
            "| Source | Kind | Group | Commits | Material | Categories |",
            "| --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for repo in report["repositories"]:
        if not repo.get("available"):
            lines.append(
                f"| {repo['name']} | {repo['kind']} | {repo['group']} | — | — | unavailable |"
            )
            continue
        categories = ", ".join(f"{key}:{value}" for key, value in repo["categories"].items()) or "—"
        lines.append(
            f"| {repo['name']} | {repo['kind']} | {repo['group']} | "
            f"{repo['total_commits']} | {repo['material_commits']} | {categories} |"
        )

    for repo in report["repositories"]:
        lines.extend(["", f"## {repo['name']}", ""])
        lines.append(f"- Path: `{repo['resolved_path']}`")
        if not repo.get("available"):
            lines.append(f"- Error: {repo.get('error', 'unavailable')}")
            continue
        lines.append(f"- Branch / head: `{repo['branch']}` / `{repo['head']}`")
        if not repo["commits"]:
            lines.append("- No commits in this period.")
        for commit in repo["commits"]:
            support = "" if commit["material"] else " — supporting"
            date = commit["committed_at"][:10]
            lines.append(
                f"- {date} `{commit['short_commit']}` [{commit['category']}] "
                f"{commit['subject']}{support}"
            )
        if "working_tree" in repo:
            lines.append("- Uncommitted work:")
            if repo["working_tree"]:
                lines.extend(f"  - `{line}`" for line in repo["working_tree"])
            else:
                lines.append("  - clean")
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    skill_root = Path(__file__).resolve().parents[1]
    default_lab_root = skill_root.parents[2]
    parser = argparse.ArgumentParser(
        description="Collect HBoot repository activity since the latest WeChat article."
    )
    parser.add_argument("--lab-root", type=Path, default=default_lab_root)
    parser.add_argument("--config", type=Path, default=skill_root / "references" / "repositories.json")
    parser.add_argument("--since", help="Git-compatible date or ISO timestamp")
    parser.add_argument("--until", help="Git-compatible date or ISO timestamp")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--include-working-tree", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    lab_root = args.lab_root.expanduser().resolve()
    config_path = args.config.expanduser().resolve()
    try:
        if not (lab_root / ".git").exists():
            raise RuntimeError(f"HBoot-Lab Git repository not found at {lab_root}")
        boundary = None if args.since else latest_content_creation(lab_root)
        since = args.since or boundary["created_at"]
        until = args.until or datetime.now().astimezone().isoformat(timespec="seconds")
        repositories = load_config(config_path)
        scans = [
            scan_repository(
                lab_root,
                entry,
                since,
                until,
                args.include_working_tree,
            )
            for entry in repositories
        ]
        report = {
            "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "lab_root": str(lab_root),
            "since": since,
            "until": until,
            "boundary": boundary,
            "repositories": scans,
        }
        if args.format == "json":
            json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
            sys.stdout.write("\n")
        else:
            sys.stdout.write(markdown_report(report))
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
