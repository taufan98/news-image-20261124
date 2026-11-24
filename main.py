"""news-image-20261124 entry program.

Copies the pre-built newspaper front page (entry.png, 1024x1024 PNG
summing up the world news of Tuesday 24 November 2026) to the output
directory as entry.png. Standard library only, no network, deterministic:
every run writes the same bytes.
"""

import hashlib
import os
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")

    with open(SOURCE, "rb") as f:
        data = f.read()

    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print("entry.png exceeds the 1 MiB limit", file=sys.stderr)
        return 1

    with open(dest, "wb") as f:
        f.write(data)

    # Post-copy audit: re-read what was written and confirm it matches.
    with open(dest, "rb") as f:
        written = f.read()
    if hashlib.sha256(written).digest() != hashlib.sha256(data).digest():
        print("written entry.png does not match the source", file=sys.stderr)
        return 1

    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {dest} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
