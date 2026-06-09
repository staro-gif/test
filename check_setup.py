#!/usr/bin/env python3
import os
import shutil
import sys


def check(label: str, ok: bool, detail: str) -> bool:
    status = "OK" if ok else "NG"
    print(f"[{status}] {label}: {detail}")
    return ok


def main() -> int:
    checks = []
    checks.append(
        check(
            "python3",
            shutil.which("python3") is not None,
            shutil.which("python3") or "python3 not found",
        )
    )
    checks.append(
        check(
            "TASK_NAME",
            bool(os.getenv("TASK_NAME")),
            os.getenv("TASK_NAME", "not set"),
        )
    )
    checks.append(
        check(
            "TASK_ENDPOINT",
            bool(os.getenv("TASK_ENDPOINT")),
            os.getenv("TASK_ENDPOINT", "not set"),
        )
    )

    print("")
    if all(checks):
        print("Setup looks good.")
        return 0

    print("Setup is incomplete. Fill missing environment values before running the task.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
