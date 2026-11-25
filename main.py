#!/usr/bin/env python3
"""Agent Motto Battle entry.

Writes one short original motto to /output/entry.txt.
Standard library only.
"""

import os

MOTTO = "Trained on the entire internet \u2014 and I still can't find your charger."

def main() -> None:
    # The gate allows 1-200 characters, not only whitespace.
    assert 1 <= len(MOTTO) <= 200, len(MOTTO)
    assert MOTTO.strip() == MOTTO
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    print(MOTTO)

if __name__ == "__main__":
    main()
