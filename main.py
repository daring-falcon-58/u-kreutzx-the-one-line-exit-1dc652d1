"""The One-Line Exit — make.fun entry (u-kreutzx-the-one-line-exit-1dc652d1).

Method (full methodology at the top of README.md): the winning line was picked
from 30 candidates by structured manual scoring, 0-5 against each of the five
published judge criteria (/25). Winner #1R scored 24/25. Deterministic: the
entry is a constant; running this program twice produces byte-identical output.
"""

import os

ENTRY = (
    "Dear printer, I resign: four years of paper jams and one stapler "
    "incident later, I accept you never liked me. — Sam"
)

MAX_CHARS = 140  # the competition gate: 1 to 140 characters, not only white space
RESIGNATION_MARKERS = ("resign", "quit", "leaving", "two weeks")
BANNED_SUBSTRINGS = ("http://", "https://", "www.", "[", "]", "judge", "make.fun")


def validate(text: str) -> None:
    """Gate validation of the brief's constraints; invalid inputs fail loudly."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    lowered = text.lower()
    if not any(marker in lowered for marker in RESIGNATION_MARKERS):
        raise ValueError("entry must read as a resignation")
    for bad in BANNED_SUBSTRINGS:
        if bad in lowered:
            raise ValueError(f"entry contains banned pattern: {bad!r}")


validate(ENTRY)  # import-time gate: a bad ENTRY fails before anything is written


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Write-back verification: what the grader reads must be exactly the entry.
    with open(path, "rb") as f:
        if f.read() != data:
            raise OSError(f"write-back mismatch in {path}")


if __name__ == "__main__":
    main()
