#!/usr/bin/env python3
"""One-line joke about an AI pair-programming demo gone wrong.

Writes the joke to /output/entry.txt (exactly one line) so the
make.fun program/v1 grader can read it. Pure standard library,
deterministic: every run writes the same line.
"""

import os

JOKE = (
    "In our live demo, my AI pair programmer wrote all the code, "
    "I nodded like I understood it, and when the demo crashed, "
    "the AI apologised to the audience \u2014 for having to work with me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
