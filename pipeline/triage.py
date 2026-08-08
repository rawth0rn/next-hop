"""Triage stage: score candidates per sector with the cheap model, select
standalone picks (score >= PICK_SCORE, max 3) or a thin-week roundup."""

import re

from . import config, llm

SYSTEM = (
    "You curate stories for Next Hop, an expert blog strictly about the "
    "networking industry: connectivity, interconnect, and the infrastructure "
    "that carries traffic. Readers are practitioners. You score how well "
    "each candidate item fits one sector of the blog. High scores (7-10) go "
    "to items announcing something specific and significant: a product or "
    "technology launch, a standard ratified or adopted, a funded infrastructure "
    "build, a deployment milestone, a notable research result or measurement "
    "study, a meaningful open source release. Low scores (0-3) go to opinion "
    "pieces, listicles, vendor fluff without substance, minor personnel or "
    "earnings news, and anything off-sector. Score 4-6 for real but modest "
    "developments. Critically: an item about compute, chips, AI models, "
    "storage, or company business is off-scope no matter how big the news, "
    "unless networking, interconnect, or connectivity infrastructure is the "
    "core of the story rather than the backdrop. When the networking angle "
    "is peripheral, score 3 or lower. Never invent items. Respond with JSON "
    "only."
)


def recent_titles(sector: str, limit: int = 15) -> list:
    titles = []
    d = config.CONTENT_DIR / sector
    if not d.exists():
        return titles
    files = sorted((p for p in d.glob("*.md") if p.name != "_index.md"),
                   reverse=True)
    for p in files[:limit]:
        for line in p.read_text().splitlines()[:6]:
            m = re.match(r'^title:\s*"?(.+?)"?\s*$', line)
            if m:
                titles.append(m.group(1))
                break
    return titles


def triage_sector(sector: str, candidates: list, run_id: str,
                  pick_floor: int = None, roundup_floor: int = None) -> dict:
    """Return {"picks": [...], "roundup": [...], "considered": n}."""
    pick_floor = pick_floor if pick_floor is not None else config.PICK_SCORE
    roundup_floor = (roundup_floor if roundup_floor is not None
                     else config.ROUNDUP_SCORE)
    pool = [c for c in candidates
            if c["sector_hint"] in (sector, None)][:config.MAX_TRIAGE_ITEMS]
    if not pool:
        return {"picks": [], "roundup": [], "considered": 0,
                "considered_ids": []}

    lines = []
    for c in pool:
        lines.append(f'{c["id"]}. [{c["feed"]} | {c["source_class"]}] '
                     f'{c["title"]} :: {c["summary"][:400]}')
    recent = recent_titles(sector)
    recent_block = ("Recently published on this sector page. A candidate "
                    "that covers the same story as any of these, from any "
                    "outlet, scores 0:\n- " +
                    "\n- ".join(recent)) if recent else ""

    user = f"""Sector: {config.SECTORS[sector]['name']}
Sector scope: {config.SECTORS[sector]['scope']}

{recent_block}

Candidate items (id. [feed | class] title :: summary):
{chr(10).join(lines)}

Score the candidates for THIS sector only. If several candidates cover the
same underlying story, give a high score only to the single best telling and
score the rest 3 or lower. Return the 10 best as JSON:
{{"scored": [{{"id": <int>, "score": <0-10>, "angle": "<one sentence: the specific innovation and why it matters>"}}]}}
Only include items that genuinely belong to this sector. JSON only."""

    raw = llm.chat(config.TRIAGE_MODEL,
                   [{"role": "system", "content": SYSTEM},
                    {"role": "user", "content": user}],
                   run_id=run_id, stage=f"triage:{sector}",
                   max_tokens=4096, temperature=0.2)
    data = llm.extract_json(raw)
    by_id = {c["id"]: c for c in pool}
    scored = []
    for row in data.get("scored", []):
        c = by_id.get(row.get("id"))
        if not c:
            continue
        try:
            score = int(row.get("score", 0))
        except (TypeError, ValueError):
            continue
        scored.append({**c, "score": score,
                       "angle": str(row.get("angle", ""))[:400]})
    scored.sort(key=lambda x: x["score"], reverse=True)

    picks = [s for s in scored if s["score"] >= pick_floor][:config.MAX_PER_SECTOR]
    roundup = []
    if not picks:
        roundup = [s for s in scored if s["score"] >= roundup_floor][:3]
    return {"picks": picks, "roundup": roundup, "considered": len(pool),
            "considered_ids": [c["id"] for c in pool]}


def dedupe_across_sectors(results: dict) -> dict:
    """If two sectors picked the same URL, keep the higher-scored pick."""
    best = {}
    for sector, res in results.items():
        for p in res["picks"]:
            key = p["url_hash"]
            if key not in best or p["score"] > best[key][1]["score"]:
                best[key] = (sector, p)
    for sector, res in results.items():
        res["picks"] = [p for p in res["picks"]
                        if best.get(p["url_hash"], (sector,))[0] == sector]
    return results
