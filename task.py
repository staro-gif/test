#!/usr/bin/env python3
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone


def log(message: str) -> None:
    print(message, flush=True)


def build_payload() -> dict:
    return {
        "taskName": os.getenv("TASK_NAME", "travel-marketing-task"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "github-actions",
    }


def run() -> int:
    endpoint = os.getenv("TASK_ENDPOINT", "").strip()
    api_key = os.getenv("TASK_API_KEY", "").strip()
    payload = build_payload()

    log(f"Starting task: {payload['taskName']}")
    log(f"Payload: {json.dumps(payload, ensure_ascii=True)}")

    if not endpoint:
        log("TASK_ENDPOINT is not set. Scaffold is working, but no remote job target is configured yet.")
        return 0

    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=body,
        headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {api_key}"} if api_key else {}),
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            response_body = response.read().decode("utf-8", errors="replace")
            log(f"Request succeeded with status {response.status}")
            log(response_body[:1000])
            return 0
    except urllib.error.HTTPError as error:
        log(f"HTTP error: {error.code}")
        log(error.read().decode("utf-8", errors="replace")[:1000])
        return 1
    except urllib.error.URLError as error:
        log(f"Network error: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(run())
