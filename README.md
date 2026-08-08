# Next Hop

An autonomous, AI-generated blog tracking innovation across the networking
industry. Live at https://rawth0rn.github.io/next-hop/

Six sectors: IoT & Edge, Data Center, Cloud Native Networking, Telecom,
Physical Infrastructure, Satellite & Space. Every post covers one specific
announced innovation in 250 to 500 words with the primary source cited.

## How it works

A Python pipeline (`pipeline/`) runs weekly:

1. **fetch**: pulls ~30 RSS/Atom feeds (industry press, company engineering
   blogs, research feeds like arXiv cs.NI and the IETF blog), 7-day window,
   deduped against `state/seen.jsonl`
2. **triage**: DeepSeek v4 Flash scores candidates per sector; items scoring
   7+ become standalone posts (max 3 per sector), thin weeks fall back to a
   single roundup, dead-quiet sectors skip honestly
3. **extract**: trafilatura pulls readable article text
4. **write**: Kimi K2 Thinking writes the post following `style/STYLE.md`
   plus rotating samples from `style/samples/`
5. **qa**: deterministic checks (word count, live links, banned style
   patterns, duplicate titles); one regeneration, then drop
6. **publish**: commits as Next Hop Bot, pushes; GitHub Actions builds Hugo
   and deploys to Pages
7. **digest**: `DIGEST.md`, `logs/last_run.json`, macOS notification

A monthly calibration pass (`pipeline/calibrate.py`) learns durable style
preferences from the owner's hand-edits to published posts and updates the
tunable sections of `style/STYLE.md` (the hard rules are spliced back in by
code and cannot drift).

Every model call is logged to `costs/costs.jsonl`; the pipeline aborts if
month-to-date spend reaches $20 (typical spend is around $1/month).

Scheduling is handled by a Hermes agent cron job on the owner's machine; see
`AGENTS.md` for the operating contract.

## Site

Hugo + PaperMod (pinned submodule). Build locally with `hugo server`.
