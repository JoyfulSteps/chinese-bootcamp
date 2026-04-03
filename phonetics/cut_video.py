"""
Cut local video into individual pinyin pronunciation clips.

Usage:
    python phonetics/cut_video.py                       # Cut all sounds
    python phonetics/cut_video.py --sounds "e,ü,zh"    # Cut specific sounds
    python phonetics/cut_video.py --include-practice     # Also cut practice sections
"""

import csv
import subprocess
import sys
import argparse
from pathlib import Path

BASE_DIR = Path(__file__).parent
VIDEO_FILE = BASE_DIR / "Học phát âm tiếng Trung.mp4"
CLIPS_DIR = BASE_DIR / "clips"
TIMESTAMPS_CSV = BASE_DIR / "timestamps.csv"


def time_to_seconds(t: str) -> float:
    parts = t.strip().split(":")
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    elif len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    return 0


def cut_clip(pinyin: str, start: str, end: str, clip_type: str):
    CLIPS_DIR.mkdir(exist_ok=True)
    safe_name = pinyin.replace("ü", "v")
    filename = f"{clip_type}_{safe_name}.mp4"
    output_path = CLIPS_DIR / filename

    if output_path.exists():
        print(f"  [SKIP] {filename} already exists")
        return output_path

    start_sec = time_to_seconds(start)
    end_sec = time_to_seconds(end)
    duration = end_sec - start_sec

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start_sec),
        "-i", str(VIDEO_FILE),
        "-t", str(duration),
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "128k",
        "-preset", "fast",
        "-crf", "23",
        "-vf", "scale=-2:480",
        "-loglevel", "error",
        str(output_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ERR] Failed: {filename}: {result.stderr[:200]}")
        return None

    size_kb = output_path.stat().st_size / 1024
    print(f"  [OK] {filename} ({duration}s, {size_kb:.0f}KB)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Cut pinyin video clips")
    parser.add_argument("--sounds", help="Comma-separated sounds to cut")
    parser.add_argument("--include-practice", action="store_true")
    args = parser.parse_args()

    print("=" * 50)
    print("  Pinyin Video Clip Cutter")
    print("=" * 50)

    if not VIDEO_FILE.exists():
        print(f"  [ERR] Video not found: {VIDEO_FILE}")
        print(f"  Place 'Học phát âm tiếng Trung.mp4' in phonetics/ folder")
        sys.exit(1)

    print(f"  Video: {VIDEO_FILE.name}")

    sounds_filter = None
    if args.sounds:
        sounds_filter = set(s.strip().lower() for s in args.sounds.split(","))

    rows = []
    with open(TIMESTAMPS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"  Found {len(rows)} entries in timestamps.csv")
    cut_count = 0
    skip_count = 0

    for row in rows:
        clip_type = row["type"].strip()
        pinyin = row["pinyin"].strip()
        start = row["start"].strip()
        end = row["end"].strip()

        if clip_type == "luyen_tap" and not args.include_practice:
            skip_count += 1
            continue

        if sounds_filter and pinyin.lower() not in sounds_filter:
            skip_count += 1
            continue

        result = cut_clip(pinyin, start, end, clip_type)
        if result:
            cut_count += 1

    print(f"\n{'=' * 50}")
    print(f"  Done! Cut {cut_count} clips, skipped {skip_count}")
    print(f"  Clips: {CLIPS_DIR}")


if __name__ == "__main__":
    main()
