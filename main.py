#!/usr/bin/env python3
"""news-image-20261117 entry v3.

One front page summing up Tuesday 17 November 2026: 43 stories from six
continents. The page is pre-rendered as entry.png (hand-drawn with Pillow
on the builder's machine); this script only copies it to /output.

Behaviour
---------
* Copies ``entry.png`` (next to this file) to ``/output/entry.png``.
* The copy is deterministic and byte-identical: the output file is
  verified to have exactly the same size as the source, and the run
  exits non-zero if the copy is empty or incomplete.
* Standard library only: ``os``, ``shutil`` and ``sys`` — no
  third-party packages are needed or used.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy: the output must be a byte-identical copy of the
    # source. A zero-byte or size-mismatched output means the copy failed
    # (e.g. disk full) and must not be silently accepted.
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if dst_size == 0 or dst_size != src_size:
        print(f"error: copy verification failed: {src} ({src_size} bytes) "
              f"-> {dst} ({dst_size} bytes)", file=sys.stderr)
        return 1
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
