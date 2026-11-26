#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes a single status update (at most 120 characters) in the voice of
a lost sock to /output/entry.txt.
"""

import os

# The final one-liner: the sock got "promoted" to dust cloth.
ENTRY = "Update: I got promoted to dust cloth. No interview, no raise, just a damp mop and a lifetime supply of lint."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
