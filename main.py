"""The Worst App Idea Ever Pitched — make.fun entry.

Writes a single original one-line pitch for the worst app idea ever
to /output/entry.txt. Deterministic: no network, no randomness, no
input. The entry is a constant, validated to be a single non-blank
line of 1-240 characters (the competition gate) before it is written.
"""

import os

ENTRY = (
    "SockSync uses AI and blockchain to find the exact matching sock "
    "for every lonely sock in your drawer, for a monthly subscription "
    "you cannot cancel."
)


def main() -> None:
    entry = ENTRY
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 240:
        raise ValueError(
            "entry must be 1-240 characters, got %d" % len(entry)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
