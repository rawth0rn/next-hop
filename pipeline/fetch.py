"""Fetch stage: pull RSS/Atom feeds, filter to the window, dedupe via ledger."""

import hashlib
import html
import json
import re
import time
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

import feedparser
import requests
import yaml

from . import config

TRACKING_PARAMS = re.compile(r"^(utm_|fbclid|gclid|mc_cid|mc_eid|cmpid|ref$)")
TAG_RE = re.compile(r"<[^>]+>")


def normalize_link(url: str) -> str:
    parts = urlsplit(url.strip())
    query = [(k, v) for k, v in parse_qsl(parts.query)
             if not TRACKING_PARAMS.match(k.lower())]
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path,
                       urlencode(query), ""))


def _hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:20]


def clean_text(s: str, max_words: int = 70) -> str:
    s = html.unescape(TAG_RE.sub(" ", s or ""))
    words = s.split()
    return " ".join(words[:max_words])


def load_sources() -> dict:
    return yaml.safe_load(config.SOURCES_FILE.read_text())


def load_seen() -> set:
    seen = set()
    if config.SEEN_FILE.exists():
        for line in config.SEEN_FILE.read_text().splitlines():
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            seen.add(row.get("u"))
            seen.add(row.get("t"))
    seen.discard(None)
    return seen


def mark_seen(candidates: list) -> None:
    config.ensure_dirs()
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with config.SEEN_FILE.open("a") as f:
        for c in candidates:
            f.write(json.dumps({"u": c["url_hash"], "t": c["title_hash"],
                                "ts": ts}) + "\n")


def _load_health() -> dict:
    if config.FEED_HEALTH_FILE.exists():
        try:
            return json.loads(config.FEED_HEALTH_FILE.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def _save_health(health: dict) -> None:
    config.ensure_dirs()
    config.FEED_HEALTH_FILE.write_text(json.dumps(health, indent=1))


def _entry_time(entry):
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None) or entry.get(attr)
        if t:
            return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
    return None


def _matches_keywords(entry_text: str, keywords) -> bool:
    if not keywords:
        return True
    text = entry_text.lower()
    return any(k.lower() in text for k in keywords)


def fetch_all(days: int = 7) -> dict:
    """Return {"candidates": [...], "feed_errors": [...], "disabled": [...]}."""
    sources = load_sources()
    seen = load_seen()
    health = _load_health()
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    feed_specs = []
    for sector, block in (sources.get("sectors") or {}).items():
        for feed in block.get("feeds", []):
            feed_specs.append((sector, feed))
    for feed in sources.get("shared", []):
        feed_specs.append((None, feed))

    candidates, feed_errors, disabled, dedup = [], [], [], set()
    next_id = 1
    for sector, feed in feed_specs:
        url = feed["url"]
        h = health.get(url, {"fails": 0})
        if h.get("fails", 0) >= 2:
            disabled.append(feed.get("name", url))
            continue
        try:
            resp = requests.get(url, timeout=20,
                                headers={"User-Agent": config.USER_AGENT})
            resp.raise_for_status()
            parsed = feedparser.parse(resp.content)
            if parsed.bozo and not parsed.entries:
                raise ValueError(f"unparseable feed ({parsed.bozo_exception})")
            h = {"fails": 0}
        except Exception as e:
            h["fails"] = h.get("fails", 0) + 1
            h["last_error"] = str(e)[:160]
            health[url] = h
            feed_errors.append(f"{feed.get('name', url)}: {str(e)[:120]}")
            continue
        health[url] = h

        for entry in parsed.entries[:80]:
            link = entry.get("link")
            title = (entry.get("title") or "").strip()
            if not link or not title:
                continue
            when = _entry_time(entry)
            if when is not None and when < cutoff:
                continue
            summary = clean_text(entry.get("summary") or
                                 entry.get("description") or "")
            if not _matches_keywords(f"{title} {summary}",
                                     feed.get("keywords")):
                continue
            norm = normalize_link(link)
            uh, th = _hash(norm), _hash(title.lower())
            if uh in seen or th in seen or uh in dedup:
                continue
            dedup.add(uh)
            candidates.append({
                "id": next_id,
                "url": link,
                "norm_url": norm,
                "url_hash": uh,
                "title_hash": th,
                "title": title,
                "summary": summary,
                "published": when.isoformat(timespec="seconds") if when else None,
                "feed": feed.get("name", url),
                "source_class": feed.get("source_class", "press"),
                "sector_hint": sector,
            })
            next_id += 1

    _save_health(health)
    candidates.sort(key=lambda c: c["published"] or "", reverse=True)
    return {"candidates": candidates, "feed_errors": feed_errors,
            "disabled": disabled}
