#!/usr/bin/env python3
"""
Generate responsive variants (400w, 800w, 1200w + WebP) for all screenshots.
Usage: python3 scripts/generate-screenshots.py
"""

import os
import sys
from PIL import Image

SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "screenshots")
SIZES = [400, 800, 1200]

# Map old (spaced) filenames to clean names
FILE_MAP = [
    ("Screenshot_20260616-123812_ .jpg", "screenshot-playlist"),
    ("Screenshot_20260616-123826_ .jpg", "screenshot-settings"),
    ("Screenshot_20260616-124130_ .jpg", "screenshot-home"),
    ("Screenshot_20260616-124141_ .jpg", "screenshot-about"),
    ("Screenshot_20260616-124212_ .jpg", "screenshot-player"),
    ("Screenshot_20260616-124219_ .jpg", "screenshot-sura-list"),
    ("Screenshot_20260616-124237_ .jpg", "screenshot-reciter"),
    ("Screenshot_20260616-135950_ .jpg", "screenshot-discover"),
]

def process_file(src_name, base_name):
    src_path = os.path.join(SRC_DIR, src_name)
    if not os.path.exists(src_path):
        print(f"  [SKIP] {src_name} not found")
        return

    print(f"  Processing: {src_name} -> {base_name}")
    img = Image.open(src_path).convert("RGB")
    original_w, original_h = img.size

    # Original -> WebP
    webp_orig = os.path.join(SRC_DIR, f"{base_name}.webp")
    img.save(webp_orig, "WEBP", quality=82, method=6)
    print(f"    {base_name}.webp ({original_w}x{original_h})")

    # Original JPEG (copy with clean name)
    jpg_orig = os.path.join(SRC_DIR, f"{base_name}.jpg")
    img.save(jpg_orig, "JPEG", quality=90)
    print(f"    {base_name}.jpg ({original_w}x{original_h})")

    # Resized variants
    for w in SIZES:
        ratio = w / original_w
        h = int(original_h * ratio)
        resized = img.resize((w, h), Image.LANCZOS)

        # JPEG
        jpeg_path = os.path.join(SRC_DIR, f"{base_name}-{w}w.jpg")
        resized.save(jpeg_path, "JPEG", quality=85)
        print(f"    {base_name}-{w}w.jpg ({w}x{h})")

        # WebP
        webp_path = os.path.join(SRC_DIR, f"{base_name}-{w}w.webp")
        resized.save(webp_path, "WEBP", quality=82, method=6)
        print(f"    {base_name}-{w}w.webp ({w}x{h})")

    # Remove old spaced file
    os.remove(src_path)
    print(f"    [DEL] {src_name}")

def main():
    print(f"Processing screenshots in: {SRC_DIR}\n")
    for old_name, clean_name in FILE_MAP:
        process_file(old_name, clean_name)
    print("\nDone! Generated all variants.")

if __name__ == "__main__":
    main()
