#!/usr/bin/env python3
"""Copy the entry image to the grader's output directory.

The image is drawn once and stored in this repository as entry.png.
This program only copies it to /output/entry.png and verifies the
copy byte for byte, so the two grading runs write identical bytes.
Standard library only; no network.
"""
import hashlib
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print("missing entry.png next to main.py", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_size = os.path.getsize(SRC)
    dst_size = os.path.getsize(DST)
    if src_size != dst_size:
        print(f"size mismatch: {src_size} != {dst_size}", file=sys.stderr)
        return 1
    if sha256_of(SRC) != sha256_of(DST):
        print("sha256 mismatch after copy", file=sys.stderr)
        return 1
    if dst_size > 1048576:
        print(f"entry.png over 1 MiB: {dst_size}", file=sys.stderr)
        return 1
    with open(DST, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a whole PNG", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({dst_size} bytes, sha256 {sha256_of(DST)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
