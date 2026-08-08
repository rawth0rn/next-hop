"""Central configuration for the Next Hop pipeline."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
STYLE_DIR = ROOT / "style"
SAMPLES_DIR = STYLE_DIR / "samples"
STATE_DIR = ROOT / "state"
COSTS_DIR = ROOT / "costs"
LOGS_DIR = ROOT / "logs"
SOURCES_FILE = Path(__file__).resolve().parent / "sources.yaml"

SEEN_FILE = STATE_DIR / "seen.jsonl"
FEED_HEALTH_FILE = STATE_DIR / "feed_health.json"
COSTS_FILE = COSTS_DIR / "costs.jsonl"
DIGEST_FILE = ROOT / "DIGEST.md"
LAST_RUN_FILE = LOGS_DIR / "last_run.json"

HERMES_ENV = Path.home() / ".hermes" / ".env"

SITE_BASE_URL = "https://rawth0rn.github.io/next-hop"
SITE_NAME = "Next Hop"

BOT_NAME = "Next Hop Bot"
BOT_EMAIL = "nexthop-bot@users.noreply.github.com"

WRITER_MODEL = "moonshotai/kimi-k2-thinking"
TRIAGE_MODEL = "deepseek/deepseek-v4-flash"

# USD per million tokens (input, output). The usage block OpenRouter returns
# wins when present; this table is the fallback and the sanity cross-check.
PRICE_TABLE = {
    "moonshotai/kimi-k2-thinking": (0.60, 2.50),
    "deepseek/deepseek-v4-flash": (0.068, 0.137),
}

# Budget guardrails in USD. Requirement is 15-25/month; abort well under it.
MONTHLY_ABORT_USD = 20.0
RUN_SOFT_CAP_USD = 2.0

# Triage selection thresholds (0-10 significance score).
PICK_SCORE = 7      # minimum for a standalone post
ROUNDUP_SCORE = 4   # minimum for inclusion in a thin-week roundup
MAX_PER_SECTOR = 3
MAX_TRIAGE_ITEMS = 120  # per-sector cap on items sent to triage

WORD_MIN = 250
WORD_MAX = 500

# Domains that answer 403 to non-browser clients but serve fine to readers.
WAF_TOLERATED_DOMAINS = {
    "www.sdxcentral.com",
    "www.datacenterdynamics.com",
    "www.telecompetitor.com",
    "www.iotworldtoday.com",
    "blogs.juniper.net",
    "www.reuters.com",
    "www.bloomberg.com",
}

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

SECTORS = {
    "iot-edge": {
        "name": "IoT & Edge",
        "scope": (
            "Connectivity for devices and the edge: LPWAN, LoRa, NB-IoT, Matter, "
            "Thread, industrial IoT networking, edge compute and edge networking "
            "platforms, device-to-cloud connectivity."
        ),
    },
    "data-center": {
        "name": "Data Center",
        "scope": (
            "Data center network hardware and fabrics: AI cluster fabrics, Ultra "
            "Ethernet, NVLink, UALink, InfiniBand, 800G and 1.6T optics, co-packaged "
            "optics, switching and routing silicon, SmartNIC and DPU hardware."
        ),
    },
    "cloud-native": {
        "name": "Cloud Native Networking",
        "scope": (
            "The software layer of networking: eBPF, Cilium, service mesh, "
            "Kubernetes networking, CNI, gateway API, load balancing software, "
            "DPU and IPU software stacks, network observability software."
        ),
    },
    "telecom": {
        "name": "Telecom",
        "scope": (
            "Carrier and service provider networks: 5G-Advanced, 6G research, Open "
            "RAN, fixed wireless access, fiber broadband, subsea cables, carrier "
            "routing and transport, telecom standards."
        ),
    },
    "physical-infrastructure": {
        "name": "Physical Infrastructure",
        "scope": (
            "What networks are built on: fiber builds and routes, data center "
            "construction, power and cooling for AI data centers, colocation and "
            "interconnect, structured cabling, grid and energy for networks."
        ),
    },
    "satellite-space": {
        "name": "Satellite & Space",
        "scope": (
            "Networking beyond the ground: LEO broadband constellations, Starlink, "
            "Kuiper, direct-to-cell, non-terrestrial networks, optical inter-satellite "
            "links, ground stations, space-to-ground connectivity."
        ),
    },
}


class BudgetExceeded(Exception):
    """Raised when the monthly spend guardrail trips."""


def openrouter_api_key() -> str:
    """Read the OpenRouter key from the environment or the Hermes .env file.

    The key value must never be printed or logged.
    """
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key:
        return key
    if HERMES_ENV.exists():
        for line in HERMES_ENV.read_text().splitlines():
            line = line.strip()
            if line.startswith("OPENROUTER_API_KEY="):
                value = line.split("=", 1)[1].strip().strip('"').strip("'")
                if value:
                    return value
    raise RuntimeError(
        "OPENROUTER_API_KEY not found in environment or ~/.hermes/.env"
    )


def ensure_dirs() -> None:
    for d in (STATE_DIR, COSTS_DIR, LOGS_DIR, SAMPLES_DIR):
        d.mkdir(parents=True, exist_ok=True)
