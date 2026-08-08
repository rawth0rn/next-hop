"""Extract stage: pull readable article text for each selected item."""

import requests
import trafilatura

from . import config

MAX_CHARS = 12000
THIN_CHARS = 400


def extract(url: str) -> dict:
    """Return {"text": str, "thin": bool}. Falls back gracefully."""
    html = None
    try:
        html = trafilatura.fetch_url(url)
    except Exception:
        html = None
    if not html:
        try:
            resp = requests.get(url, timeout=25,
                                headers={"User-Agent": config.USER_AGENT})
            if resp.status_code < 400:
                html = resp.text
        except requests.RequestException:
            html = None
    text = None
    if html:
        try:
            text = trafilatura.extract(html, include_comments=False,
                                       include_tables=False)
        except Exception:
            text = None
    text = (text or "").strip()
    thin = len(text) < THIN_CHARS
    return {"text": text[:MAX_CHARS], "thin": thin}
