#!/usr/bin/env python3
"""news-image-20261117 entry v3.

One front page summing up Tuesday 17 November 2026: 43 stories from six
continents. The page is pre-rendered as entry.png (hand-drawn with Pillow
on the builder's machine); this script only copies it to /output.

Standard library only: no third-party packages are needed or used.
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
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
