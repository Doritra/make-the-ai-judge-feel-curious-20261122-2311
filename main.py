"""Make the AI judge feel curious.

This program writes one short text to /output/entry.txt: a quiet scene
with a concrete mystery and one open question, written to intrigue the
AI judge reading it.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# Revision 2: "farther" for the tide's physical distance; the rest of
# the scene is unchanged — three concrete lost things, one reader awake,
# one open question (piano key or door key) left for the judge to keep
# asking.
ENTRY_TEXT = (
    "The tide went out farther than the charts allow tonight, and the "
    "beach gave back a bicycle, a front door, and a piano with its lid "
    "still closed. You are the only reader awake to see it \u2014 which "
    "key do you try first?"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY_TEXT
    assert 1 <= len(text) <= 280, f"entry is {len(text)} code points"
    assert text.strip(), "entry is only white space"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
