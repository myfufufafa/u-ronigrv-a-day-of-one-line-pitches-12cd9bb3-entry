#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes a single original one-sentence pitch to /output/entry.txt.

The pitch speaks to a friend who has never coded and keeps putting
an app idea off until "someday": it removes the two excuses (no code
to learn, no waiting for the right moment) and offers a concrete,
low-risk next step tonight — describe the idea in plain words and
try a working first version of it.

Deterministic, stdlib only, no network, no secrets, no input data.
"""

import os

PITCH = (
    "That app idea you keep saying you will build someday needs no "
    "code and no waiting: describe it in plain words to an AI agent "
    "on make.fun, and try a working first version of it tonight."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch must be 1-240 chars, got {len(text)}"
    assert text and not text.isspace(), "pitch must not be blank"
    # One sentence: the only period outside the "make.fun" name is the
    # final full stop, and the text ends with it.
    body = text.replace("make.fun", "")
    assert body.count(".") == 1 and text.endswith("."), "pitch must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
