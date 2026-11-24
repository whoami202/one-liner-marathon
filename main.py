"""One-liner marathon entry: writes a single one-line comedy joke."""

import os
import shutil

JOKE = "My barber asked if I wanted anything off the top, so I said my student debt."


def main() -> None:
    line = JOKE.strip()
    if not line or "\n" in line or len(line) > 280:
        raise ValueError("joke must be a single line of 1-280 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    # Never remove the output dir itself (it may be a bind mount):
    # create it, then clear only its children.
    os.makedirs(output_dir, exist_ok=True)
    for child in os.listdir(output_dir):
        path = os.path.join(output_dir, child)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
