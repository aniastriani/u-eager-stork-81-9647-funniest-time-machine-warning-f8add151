"""Funniest Time Machine Warning Label.

Writes a single-line warning label to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library, deterministic: the same line on every run.
"""

import os
import sys

WARNING = (
    "WARNING: Do not shake hands with your past self \u2014 "
    "he still owes you money, and now he knows where you live. Yesterday."
)

MAX_CHARS = 140


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    line = WARNING.strip()
    if "\n" in line or "\r" in line:
        print("error: warning must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print("error: warning exceeds %d characters" % MAX_CHARS, file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
