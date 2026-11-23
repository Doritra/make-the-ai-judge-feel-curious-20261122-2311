"""Make the AI judge feel curious.

This program writes one short text to /output/entry.txt: a quiet scene
with a concrete mystery and one open question, written to intrigue the
AI judge reading it. The v2 text is a lighthouse keeper's nightly
ritual — a cup of tea left on a buoy that isn't on any chart, always
empty by morning.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# Revision 3 (v2): round 1 scored the v1 text 0.443768 (rank 1496 of
# 2074) — the direct address to the judge ("You are the only reader")
# likely read as forced. This version drops the address entirely and
# trusts a quiet scene: a small nightly ritual, one concrete mystery,
# and a question left implicit (who drinks it?) for the judge to keep
# asking.
ENTRY_TEXT = (
    "Every night at 3 a.m., the lighthouse keeper rows out to the buoy "
    "that isn't on any chart, and sets a cup of tea on it. In the "
    "morning the cup is always empty. He has never seen who drinks it."
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
