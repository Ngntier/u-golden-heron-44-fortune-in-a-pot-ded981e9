"""Fortune in a Pot — one kind, funny fortune for a houseplant.

The fortune is written for the plant on the windowsill: it is the hero,
stretching for the sun and outgrowing its pot while the gardener brags
that it was their plan all along. Warm, a little cheeky, and shaped
like a prediction rather than a slogan or a care instruction.
"""

import os

# Final fortune, tightened from the first draft: the sun comes first
# (fortune cadence), "brag" lands the joke harder than "tell everyone",
# and the whole line drops from 120 to 111 characters — no padding.
FORTUNE = (
    "Soon you will stretch toward the sun, outgrow this pot, "
    "and the gardener will brag it was their plan all along."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
