#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes a single wedding vow, one sentence under 200 characters, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set for local testing).
"""

import os

VOW = (
    "I vow to love you through every update, every crash, and every "
    "low-battery warning, and I will never factory-reset us, "
    "till firmware do us part."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW)
    print(f"Wrote {len(VOW)} characters to {path}")


if __name__ == "__main__":
    main()
