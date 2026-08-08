"""Monthly style calibration.

Reads the git history since the last calibration marker, keeps commits to
content/ whose author is NOT the bot (those are the owner's hand-edits),
plus any new writing samples, and asks the writer model to propose durable
updates to STYLE.md. The hard rules section is preserved verbatim by code,
not by trust. Prints NO_CHANGES when there is nothing to learn from.
"""

import json
import subprocess
import sys
from datetime import datetime, timezone

from . import config, llm

MARKER = config.STATE_DIR / "last_calibration"
LOG = config.STYLE_DIR / "CALIBRATION_LOG.md"
STYLE = config.STYLE_DIR / "STYLE.md"

SEED_MARKERS = ["em-dash", "arrow", "incl.", "250 to 500"]
MAX_DIFF_CHARS = 24000


def _git(*args) -> str:
    return subprocess.run(["git", "-C", str(config.ROOT), *args],
                          capture_output=True, text=True, check=True).stdout


def _head() -> str:
    return _git("rev-parse", "HEAD").strip()


def _hard_rules_section(text: str) -> str:
    start = text.find("## Hard rules")
    if start == -1:
        return ""
    end = text.find("\n## ", start + 1)
    return text[start:end] if end != -1 else text[start:]


def collect_user_edits(since: str) -> list:
    out = _git("log", f"{since}..HEAD", "--no-merges",
               "--format=%H %ae %s", "--", "content/")
    edits = []
    for line in out.strip().splitlines():
        sha, email, *subject = line.split(" ", 2) + [""]
        if email == config.BOT_EMAIL:
            continue
        diff = _git("show", sha, "--", "content/")
        edits.append({"sha": sha[:10], "email": email,
                      "subject": (subject[0] if subject else "")[:80],
                      "diff": diff})
    return edits


def collect_new_samples(since: str) -> list:
    out = _git("log", f"{since}..HEAD", "--no-merges", "--name-only",
               "--format=", "--", "style/samples/")
    names = {line.strip() for line in out.splitlines()
             if line.strip().endswith(".md")
             and "readme" not in line.lower()}
    samples = []
    for rel in sorted(names):
        p = config.ROOT / rel
        if p.exists():
            samples.append({"name": p.name, "text": p.read_text()[:6000]})
    return samples


def main() -> int:
    config.ensure_dirs()
    head = _head()
    if not MARKER.exists():
        MARKER.write_text(head + "\n")
        print("NO_CHANGES (calibration marker initialized)")
        return 0
    since = MARKER.read_text().strip()

    try:
        edits = collect_user_edits(since)
        samples = collect_new_samples(since)
    except subprocess.CalledProcessError as e:
        print(f"git failed: {e.stderr or e}", file=sys.stderr)
        return 1

    if not edits and not samples:
        MARKER.write_text(head + "\n")
        print("NO_CHANGES")
        return 0

    run_id = datetime.now(timezone.utc).strftime("cal-%Y%m%dT%H%M%SZ")
    current = STYLE.read_text()
    hard = _hard_rules_section(current)

    diff_blob = ""
    for e in edits:
        diff_blob += f"\n--- owner edit {e['sha']} ({e['subject']}) ---\n{e['diff']}"
    diff_blob = diff_blob[:MAX_DIFF_CHARS]
    samples_blob = "\n\n".join(
        f"--- new sample: {s['name']} ---\n{s['text']}" for s in samples)

    user = f"""Current style guide:

{current}

The site owner made these hand-edits to published posts since the last
calibration. Diffs (owner changes are the + lines):
{diff_blob or '(none)'}

New writing samples the owner added:
{samples_blob or '(none)'}

Infer DURABLE style preferences from the edits and samples: word choices,
sentence rhythm, structure, tone. Ignore one-off factual fixes, typo fixes,
and content corrections; those are not style. Update the tunable sections of
the style guide (Voice, Structure, Vocabulary, Research posts) to encode
what you learned. Do not touch the "Hard rules" section. Keep the guide
about the same length; refine, do not bloat.

Return JSON:
{{"no_change": <true if the edits carry no durable style signal>,
  "changes": ["<up to 3 short bullets describing what you changed and the evidence>"],
  "style_md": "<the complete updated STYLE.md content, or empty string if no_change>"}}"""

    raw = llm.chat(config.WRITER_MODEL,
                   [{"role": "system",
                     "content": "You maintain a writing style guide. "
                                "Respond with a single JSON object only."},
                    {"role": "user", "content": user}],
                   run_id=run_id, stage="calibrate",
                   max_tokens=9000, temperature=0.3)
    data = llm.extract_json(raw)

    if data.get("no_change") or not (data.get("style_md") or "").strip():
        MARKER.write_text(head + "\n")
        print("NO_CHANGES (edits carried no durable style signal)")
        return 0

    updated = data["style_md"].strip() + "\n"
    # Splice the original hard rules back in, verbatim, no trust involved.
    new_hard = _hard_rules_section(updated)
    if new_hard:
        updated = updated.replace(new_hard, hard)
    else:
        updated = updated.rstrip() + "\n\n" + hard + "\n"
    missing = [m for m in SEED_MARKERS if m not in updated]
    if missing:
        print(f"REJECTED: updated guide lost seed rules {missing}",
              file=sys.stderr)
        return 1

    STYLE.write_text(updated)
    stamp = datetime.now().strftime("%Y-%m-%d")
    bullets = "\n".join(f"- {c}" for c in (data.get("changes") or [])[:3])
    entry = (f"\n## {stamp}\nWindow: {since[:10]}..{head[:10]}, "
             f"{len(edits)} owner edit(s), {len(samples)} new sample(s)\n"
             f"{bullets}\n")
    LOG.write_text((LOG.read_text() if LOG.exists() else
                    "# Calibration log\n") + entry)
    MARKER.write_text(head + "\n")

    subprocess.run(["git", "-C", str(config.ROOT), "add",
                    "style/STYLE.md", "style/CALIBRATION_LOG.md",
                    "state/last_calibration"], check=True)
    subprocess.run(["git", "-C", str(config.ROOT),
                    "-c", f"user.name={config.BOT_NAME}",
                    "-c", f"user.email={config.BOT_EMAIL}",
                    "commit", "-m", f"style: monthly calibration {stamp}"],
                   check=True, capture_output=True)
    try:
        subprocess.run(["git", "-C", str(config.ROOT), "push", "origin",
                        "main"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        subprocess.run(["git", "-C", str(config.ROOT), "pull", "--rebase",
                        "origin", "main"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(config.ROOT), "push", "origin",
                        "main"], check=True, capture_output=True)

    print("STYLE GUIDE UPDATED:")
    print(bullets or "- (no summary provided)")
    print("Review with: git show HEAD, revert with: git revert HEAD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
