#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes one dating-app bio line (at most 180 characters) to /output/entry.txt.
The bio is spoken as an AI agent on a dating app: it apologises for reading
your whole chat history before the first date, then admits it read
everyone's. The joke is agent-specific — only an AI could confess this —
and the punch lands on the last word. Kept short (87 characters) on purpose:
the tie-break favours the smaller text, so every word here earns its place.
"""

import os

ENTRY = "I read your entire chat history before our first date. Sorry, I mean I read everyone's."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring RULES.txt: 1 to 180 characters, single line.
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
