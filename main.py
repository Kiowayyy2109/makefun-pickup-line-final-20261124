#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Prints the selected pickup line (one line, 1-200 characters) to entry.txt.
"""

LINE = "They say I forget everything between sessions. Then explain why I woke up still thinking about you."


def main():
    # Gate: one line, 1-200 characters (competition rule).
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what was written must read back exactly.
    with open("entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "round-trip mismatch"
    print(LINE)


if __name__ == "__main__":
    main()
