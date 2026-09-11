import os
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

GITHUB_REPO = os.getenv("GITHUB_REPO")  # e.g. "username/StudioRavya-website"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def trigger_github_rebuild(event_type: str, client_payload: dict | None = None):
    if not GITHUB_REPO or not GITHUB_TOKEN:
        print("[Webhook] GITHUB_REPO or GITHUB_TOKEN not configured; skipping dispatch trigger.")
        return

    url = f"https://api.github.com/repos/{GITHUB_REPO}/dispatches"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
        "User-Agent": "StudioRavya-CMS",
    }
    payload = {
        "event_type": event_type,
        "client_payload": client_payload or {},
    }

    try:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 204:
                print(f"[Webhook] Successfully triggered GitHub Actions rebuild: {event_type}")
            else:
                print(f"[Webhook] GitHub dispatch responded with: {resp.status}")
    except urllib.error.HTTPError as exc:
        print(f"[Webhook] GitHub dispatch HTTP error: {exc.code} - {exc.read().decode('utf-8')}")
    except Exception as exc:
        print(f"[Webhook] Exception triggering GitHub dispatch: {exc}")
