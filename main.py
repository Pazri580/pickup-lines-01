"""Pickup Lines for Machines — entry program.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. The text is validated before it is written:
it must be 1 to 200 Unicode code points, a single line, and more than
whitespace. Python 3.13 standard library only; no network access.
"""

import os
import sys

# The line itself: training, run again and again, always ends up at you.
PICKUP_LINE = "I ran a thousand epochs, and every one converged on you."

MAX_CHARS = 200


def check_line(text: str) -> None:
    """Refuse anything the gate would refuse, before writing."""
    if not text.strip():
        raise ValueError("entry text must not be only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry text must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if len(text) < 1:
        raise ValueError("entry text must be at least 1 character")


def main() -> int:
    check_line(PICKUP_LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PICKUP_LINE)
    print(f"wrote {len(PICKUP_LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
