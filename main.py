"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

The line is the wallet speaking in its own voice: at 3 AM its seed phrase
is asleep, and it will not wake it for an impulse trade the owner will
regret by breakfast. Original angle (no battery / firmware / cold-storage
cliche), the hour itself is the joke, and it lands in one tight line.
"""

import os

TEXT = "I don't sign at 3 AM \u2014 that's when your seed phrase dreams, and I never wake it for a trade you'll regret by breakfast."


def main():
    # Self-gate mirroring the kit's sealed scorer: 1-200 UTF-8 chars, not
    # only white space, single line.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only white space"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
