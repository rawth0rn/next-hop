"""OpenRouter chat client with retries, usage capture, and cost logging."""

import json
import time

import requests

from . import config, costs

ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"


def chat(model: str, messages: list, *, run_id: str, stage: str,
         max_tokens: int = 4096, temperature: float = 0.4,
         timeout: int = 240, retries: int = 3) -> str:
    """One chat completion. Logs cost, enforces the monthly guardrail."""
    costs.check_monthly_budget()
    headers = {
        "Authorization": f"Bearer {config.openrouter_api_key()}",
        "Content-Type": "application/json",
        "HTTP-Referer": config.SITE_BASE_URL,
        "X-Title": "Next Hop pipeline",
    }
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "usage": {"include": True},
    }
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            resp = requests.post(ENDPOINT, headers=headers, json=payload,
                                 timeout=timeout)
            if resp.status_code in (429, 500, 502, 503, 504):
                last_err = f"HTTP {resp.status_code}"
                time.sleep(8 * attempt)
                continue
            resp.raise_for_status()
            data = resp.json()
            if "error" in data:
                last_err = str(data["error"])[:200]
                time.sleep(8 * attempt)
                continue
            choice = data["choices"][0]
            content = choice["message"].get("content") or ""
            finish = choice.get("finish_reason")
            usage = data.get("usage") or {}
            pt = int(usage.get("prompt_tokens") or 0)
            ct = int(usage.get("completion_tokens") or 0)
            cost = usage.get("cost")
            if cost is None:
                pin, pout = config.PRICE_TABLE.get(model, (1.0, 4.0))
                cost = (pt * pin + ct * pout) / 1_000_000
            costs.record(run_id, stage, model, pt, ct, float(cost))
            if not content.strip():
                # Reasoning models can burn the whole budget thinking and
                # return empty content with finish_reason "length".
                if finish == "length":
                    payload["max_tokens"] = min(payload["max_tokens"] * 2, 16000)
                last_err = f"empty completion (finish_reason={finish})"
                time.sleep(4 * attempt)
                continue
            return content
        except requests.RequestException as e:
            last_err = repr(e)[:200]
            time.sleep(8 * attempt)
    raise RuntimeError(f"LLM call failed after {retries} attempts "
                       f"(model={model}, stage={stage}): {last_err}")


def extract_json(text: str):
    """Parse the first JSON object found in a model response."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.rstrip().endswith("```"):
            text = text.rstrip()[:-3]
    start = text.find("{")
    if start == -1:
        raise ValueError("no JSON object in response")
    decoder = json.JSONDecoder()
    obj, _ = decoder.raw_decode(text[start:])
    return obj
