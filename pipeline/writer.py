"""Write stage: generate posts with the writer model, guided by STYLE.md."""

from datetime import date

from . import config, llm


def _style_guide() -> str:
    p = config.STYLE_DIR / "STYLE.md"
    return p.read_text() if p.exists() else ""


def _samples() -> str:
    """Up to two writing samples, rotated by ISO week."""
    files = sorted(p for p in config.SAMPLES_DIR.glob("*.md")
                   if p.name.lower() != "readme.md")
    if not files:
        return ""
    week = date.today().isocalendar()[1]
    picked = [files[week % len(files)]]
    if len(files) > 1:
        picked.append(files[(week + 1) % len(files)])
    parts = []
    for f in dict.fromkeys(picked):
        parts.append(f"--- sample: {f.name} ---\n{f.read_text().strip()}")
    return "\n\n".join(parts)


def _system() -> str:
    samples = _samples()
    samples_block = (
        f"\n\nWriting samples from the site owner. Match their voice:\n{samples}"
        if samples else ""
    )
    return (
        "You write posts for Next Hop, a blog covering innovation in the "
        "networking industry, read by practitioners. Follow the style guide "
        "exactly; it wins over any habit you have."
        f"\n\n{_style_guide()}{samples_block}"
        "\n\nAlways respond with a single JSON object, nothing else."
    )


_CONTRACT = f"""Format contract, all items mandatory:
- Body is {config.WORD_MIN} to {config.WORD_MAX} words of markdown prose (word count excludes link URLs).
- Cover ONE specific innovation only. Open with the concrete thing that happened.
- Cite the primary source with an inline markdown link on first mention.
- Include a grounded "why it matters" for practitioners; no invented numbers, no claims beyond the source.
- Copy proper nouns, product names, company names, numbers, and units exactly as the source material spells them. If a name or number is not in the source material, leave it out.
- If the source material is marked THIN, stay strictly within what is given and keep claims minimal.
- For research items, name the paper or draft and its stage (preprint, working group draft, published RFC, conference).
- Never use em-dashes, en-dashes, or arrows of any kind. Write "including", never "incl."
- Title: specific and plain, under 80 characters, no colon-heavy clickbait.
- summary: one plain sentence under 160 characters.
- tags: 2-4 short lowercase topic tags (not the sector name).

Return JSON: {{"title": "...", "summary": "...", "tags": ["..."], "body_markdown": "..."}}"""


def write_post(sector: str, item: dict, material: dict, run_id: str,
               feedback: str = "") -> dict:
    fb = (f"\n\nYour previous attempt failed these checks, fix them:\n{feedback}"
          if feedback else "")
    thin = " (THIN: extraction failed, only feed summary available)" if material["thin"] else ""
    body_text = material["text"] or item["summary"]
    user = f"""Sector: {config.SECTORS[sector]['name']}
Source type: {item['source_class']}
Editor's angle: {item['angle']}

Source material{thin}:
Title: {item['title']}
Outlet: {item['feed']}
Published: {item.get('published') or 'this week'}
URL: {item['url']}

{body_text}

Write the post. {_CONTRACT}{fb}"""
    raw = llm.chat(config.WRITER_MODEL,
                   [{"role": "system", "content": _system()},
                    {"role": "user", "content": user}],
                   run_id=run_id, stage=f"write:{sector}",
                   max_tokens=7000, temperature=0.6)
    post = llm.extract_json(raw)
    post["sources"] = [item["url"]]
    post["source_type"] = item["source_class"]
    return post


def write_roundup(sector: str, items: list, materials: list, run_id: str,
                  feedback: str = "") -> dict:
    fb = (f"\n\nYour previous attempt failed these checks, fix them:\n{feedback}"
          if feedback else "")
    blocks = []
    for item, material in zip(items, materials):
        text = (material["text"] or item["summary"])[:3000]
        blocks.append(f"""Item: {item['title']}
Outlet: {item['feed']} ({item['source_class']})
URL: {item['url']}
Angle: {item['angle']}
{text}""")
    user = f"""Sector: {config.SECTORS[sector]['name']}

This was a quiet week for the sector, so write ONE short roundup post
covering the {len(items)} smaller developments below. A sentence or two of
sector context is fine, then each item gets a short paragraph with its own
inline source link. The roundup is the one exception to the single-innovation
rule, but every other rule in the contract holds.

{chr(10).join(blocks)}

Write the post. {_CONTRACT}{fb}"""
    raw = llm.chat(config.WRITER_MODEL,
                   [{"role": "system", "content": _system()},
                    {"role": "user", "content": user}],
                   run_id=run_id, stage=f"write-roundup:{sector}",
                   max_tokens=7000, temperature=0.6)
    post = llm.extract_json(raw)
    post["sources"] = [i["url"] for i in items]
    post["source_type"] = "roundup"
    return post
