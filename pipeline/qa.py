"""QA stage: deterministic checks on generated posts. No LLM involved."""

import re
from urllib.parse import urlsplit

import requests

from . import config

BANNED = [
    (re.compile(r"—"), "em-dash"),
    (re.compile(r"–"), "en-dash"),
    (re.compile(r"→|⇒|←|⟶"), "arrow character"),
    (re.compile(r"(?<![-<])->(?!>)"), "ascii arrow ->"),
    (re.compile(r"=>"), "ascii arrow =>"),
    (re.compile(r"\bincl\.", re.IGNORECASE), '"incl."'),
]

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")

STOPWORDS = {"a", "an", "the", "for", "as", "of", "to", "in", "on", "and",
             "with", "by", "at", "its", "is", "new", "from", "into"}


def _sig_words(title: str) -> set:
    return {w for w in re.findall(r"[a-z0-9]+", title.lower())
            if w not in STOPWORDS}


def similar_title_exists(title: str, titles: set) -> str:
    """Return the matching existing title when the new one covers the same
    story (70 percent of its significant words already used), else ""."""
    new = _sig_words(title)
    if not new:
        return ""
    for t in titles:
        if len(new & _sig_words(t)) / len(new) >= 0.7:
            return t
    return ""


def word_count(body: str) -> int:
    no_links = LINK_RE.sub(r"\1", body)
    no_urls = re.sub(r"https?://\S+", "", no_links)
    return len(no_urls.split())


def existing_titles() -> set:
    titles = set()
    for p in config.CONTENT_DIR.rglob("*.md"):
        if p.name == "_index.md":
            continue
        for line in p.read_text().splitlines()[:6]:
            m = re.match(r'^title:\s*"?(.+?)"?\s*$', line)
            if m:
                titles.add(m.group(1).strip().lower())
                break
    return titles


def source_already_cited(url: str) -> bool:
    needle = url.split("://", 1)[-1].rstrip("/")
    for p in config.CONTENT_DIR.rglob("*.md"):
        if p.name == "_index.md":
            continue
        if needle in p.read_text():
            return True
    return False


def _url_ok(url: str) -> bool:
    host = urlsplit(url).netloc
    try:
        resp = requests.head(url, timeout=15, allow_redirects=True,
                             headers={"User-Agent": config.USER_AGENT})
        if resp.status_code in (405, 501):
            resp = requests.get(url, timeout=20, stream=True,
                                headers={"User-Agent": config.USER_AGENT})
        if resp.status_code < 400:
            return True
        if resp.status_code in (403, 429):
            return True  # WAF or rate limit; the link itself is real
        return host in config.WAF_TOLERATED_DOMAINS
    except requests.RequestException:
        return False


def check_post(post: dict, *, skip_link_check: bool = False,
               known_titles: set = None) -> list:
    """Return a list of human-readable failures; empty means pass."""
    failures = []
    title = (post.get("title") or "").strip()
    summary = (post.get("summary") or "").strip()
    body = (post.get("body_markdown") or "").strip()

    if not title:
        failures.append("missing title")
    if len(title) > 90:
        failures.append(f"title too long ({len(title)} chars, max 90)")
    if not summary:
        failures.append("missing summary")
    if len(summary) > 180:
        failures.append(f"summary too long ({len(summary)} chars, max 180)")
    if not isinstance(post.get("tags"), list) or not post.get("tags"):
        failures.append("tags must be a non-empty list")

    wc = word_count(body)
    if wc < config.WORD_MIN:
        failures.append(f"body too short ({wc} words, need {config.WORD_MIN}-{config.WORD_MAX})")
    if wc > config.WORD_MAX:
        failures.append(f"body too long ({wc} words, need {config.WORD_MIN}-{config.WORD_MAX})")

    check_zone = f"{title}\n{summary}\n{body}"
    for pattern, label in BANNED:
        if pattern.search(check_zone):
            failures.append(f"banned style: contains {label}")

    body_links = [u for _, u in LINK_RE.findall(body)]
    if not body_links:
        failures.append("body has no inline markdown source link")
    else:
        cited_hosts = {urlsplit(u).netloc for u in body_links}
        source_hosts = {urlsplit(u).netloc for u in post.get("sources", [])}
        if source_hosts and not (cited_hosts & source_hosts):
            failures.append("body links do not include the primary source")

    titles = known_titles if known_titles is not None else existing_titles()
    if title.lower() in titles:
        failures.append("duplicate title already published")
    else:
        match = similar_title_exists(title, titles)
        if match:
            failures.append(
                f'covers the same story as published post "{match}"')

    if not skip_link_check:
        for u in dict.fromkeys(body_links + list(post.get("sources", []))):
            if not _url_ok(u):
                failures.append(f"link check failed: {u}")

    return failures
