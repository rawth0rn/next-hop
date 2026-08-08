"""Publish stage: write post files, commit as the bot identity, push."""

import json
import re
import subprocess
from datetime import datetime

from . import config


def slugify(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:60].rstrip("-") or "post"


def write_post_file(sector: str, post: dict) -> str:
    now = datetime.now().astimezone()
    day = now.strftime("%Y-%m-%d")
    base = slugify(post["title"])
    d = config.CONTENT_DIR / sector
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{day}-{base}.md"
    n = 2
    while path.exists():
        path = d / f"{day}-{base}-{n}.md"
        n += 1
    fm = {
        "title": post["title"].strip(),
        "date": now.isoformat(timespec="seconds"),
        "summary": post["summary"].strip(),
        "tags": [str(t).strip().lower() for t in post.get("tags", [])][:4],
        "source_type": post.get("source_type", "press"),
        "sources": post.get("sources", []),
    }
    lines = ["---"]
    lines.append(f"title: {json.dumps(fm['title'])}")
    lines.append(f"date: {fm['date']}")
    lines.append(f"summary: {json.dumps(fm['summary'])}")
    lines.append("tags: [" + ", ".join(json.dumps(t) for t in fm["tags"]) + "]")
    lines.append(f"source_type: {fm['source_type']}")
    lines.append("sources:")
    for s in fm["sources"]:
        lines.append(f"  - {json.dumps(s)}")
    lines.append("---")
    lines.append("")
    lines.append(post["body_markdown"].strip())
    lines.append("")
    path.write_text("\n".join(lines))
    return str(path.relative_to(config.ROOT))


def _git(*args, check=True):
    return subprocess.run(["git", "-C", str(config.ROOT), *args],
                          capture_output=True, text=True, check=check)


def commit_and_push(message: str, push: bool = True) -> str:
    """Stage pipeline outputs, commit as the bot, push with one rebase retry."""
    _git("add", "content", "state", "costs", "DIGEST.md")
    status = _git("status", "--porcelain", "--", "content", "state", "costs",
                  "DIGEST.md").stdout.strip()
    if not status:
        return "nothing to commit"
    _git("-c", f"user.name={config.BOT_NAME}",
         "-c", f"user.email={config.BOT_EMAIL}",
         "commit", "-m", message)
    if not push:
        return "committed (push skipped)"
    try:
        _git("push", "origin", "main")
    except subprocess.CalledProcessError:
        _git("pull", "--rebase", "origin", "main")
        _git("push", "origin", "main")
    return "pushed"
