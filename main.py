"""Laugh Lab one-liner entry.

The joke: a robot vacuum, caught after eating a sock, pleads its case
like a defendant in court — the sock started it, because lying there
looking exactly like dust made it fair game for a machine hired to
destroy dust. The entry line is written verbatim to /output/entry.txt.
"""

import os

ENTRY = "In my defense, the sock started it: it lay there looking exactly like the dust I was hired to destroy."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
