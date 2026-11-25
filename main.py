"""Worst Superpower entry: one line, written to /output/entry.txt.

The line names the power and its uselessness in the same breath,
so the joke is complete with no setup or explanation.
"""

from pathlib import Path

ENTRY_LINE = "I can teleport anywhere - but only to places I'm already standing."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY_LINE.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(text.encode("utf-8"))
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
