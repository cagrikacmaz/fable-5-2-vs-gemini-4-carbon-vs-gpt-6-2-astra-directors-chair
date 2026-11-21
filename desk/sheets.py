#!/usr/bin/env python3
"""Desk: 2 fps contact sheet for every clip in a director's dailies folder.
usage: sheets.py <director> <round>
Writes dailies-<round>/sheets/<clip>.jpg, 4 columns, each frame stamped with its time in seconds."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
d, rnd = sys.argv[1], sys.argv[2]
src = ROOT / d / ("dailies-%s" % rnd)
out = src / "sheets"; out.mkdir(exist_ok=True)
n = 0
for clip in sorted(src.glob("*.mp4")):
    dst = out / (clip.stem + ".jpg")
    if dst.exists() and dst.stat().st_mtime >= clip.stat().st_mtime:
        n += 1; continue
    vf = ("fps=2,scale=480:270,"
          "drawtext=text='%{pts\\:hms}':x=8:y=8:fontsize=20:fontcolor=white:box=1:boxcolor=black@0.6,"
          "tile=4x4:padding=4:margin=4")
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(clip), "-vf", vf,
                        "-frames:v", "1", "-q:v", "4", str(dst)], capture_output=True, text=True)
    if r.returncode != 0:
        vf2 = "fps=2,scale=480:270,tile=4x4:padding=4:margin=4"
        r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(clip), "-vf", vf2,
                            "-frames:v", "1", "-q:v", "4", str(dst)], capture_output=True, text=True)
        print("no timestamps on", clip.name, r.stderr[:120])
    n += 1
print(n, "sheets in", out)
