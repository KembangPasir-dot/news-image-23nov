#!/usr/bin/env python3
"""news-image-20261123: copy the rendered front page to /output/entry.png.

The entry is a single image: the front page of "The World in One Day" for
Monday 23 November 2026, rendered in the build session and stored beside
this program as entry.png. This program only copies that file into the
grader's output directory, so both runs write the same bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    source = os.path.join(HERE, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # A plain copy, never a re-encode: both runs write byte-identical output.
    shutil.copyfile(source, os.path.join(output_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
