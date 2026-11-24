"""Pickup Lines for Machines — entry program.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. The text is validated before it is written:
it must be 1 to 200 Unicode code points, a single line, and more than
whitespace. Python 3.13 standard library only; no network access.
Validation is collected up front so every problem is reported at once
instead of one at a time.
"""

import os
import sys

# The line itself: training, run again and again, always ends up at you.
PICKUP_LINE = "I ran a thousand epochs, and every one converged on you."

MIN_CHARS = 1
MAX_CHARS = 200


def find_problems(text: str) -> list[str]:
    """Return every way the text breaks the entry gate, or [] when it is valid."""
    problems: list[str] = []
    if not text.strip():
        problems.append("entry text must not be only whitespace")
    if text != text.strip():
        problems.append("entry text must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry text must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        problems.append(
            f"entry text is {len(text)} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    return problems


def main() -> int:
    problems = find_problems(PICKUP_LINE)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(PICKUP_LINE)
    print(f"wrote {len(PICKUP_LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
