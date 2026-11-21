#!/usr/bin/env python3
"""Desk: copy 1080p Flow downloads into a director's dailies folder under order-based names.
usage: ingest.py <director> <round> id8=name [id8=name ...]   (name without .mp4)
Keeps the Flow file name in dailies-<round>/clips.json."""
import json, shutil, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
DL = ROOT.parent / "Downloads"
d, rnd = sys.argv[1], sys.argv[2]
out = ROOT / d / ("dailies-%s" % rnd)
out.mkdir(parents=True, exist_ok=True)
mf = out / "clips.json"
man = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {}
for pair in sys.argv[3:]:
    id8, name = pair.split("=")
    hits = sorted(DL.glob("*_%s_1080p.mp4" % id8)) or sorted(DL.glob("*_%s.mp4" % id8))
    if len(hits) != 1:
        print("!! %s: %d files match" % (id8, len(hits))); continue
    src = hits[0]; dst = out / (name + ".mp4")
    if not dst.exists() or dst.stat().st_size != src.stat().st_size:
        shutil.copyfile(src, dst)
    p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height,r_frame_rate:format=duration", "-of", "json", str(dst)],
                       capture_output=True, text=True).stdout
    j = json.loads(p); st = j["streams"][0]
    man[name + ".mp4"] = {"flow_file": src.name, "flow_id": id8, "width": st["width"], "height": st["height"],
                          "fps": st["r_frame_rate"], "seconds": round(float(j["format"]["duration"]), 2),
                          "bytes": dst.stat().st_size}
    print("ok %-34s %sx%s %ss  <- %s" % (name, st["width"], st["height"], man[name + ".mp4"]["seconds"], src.name))
mf.write_text(json.dumps(man, indent=2, ensure_ascii=False), encoding="utf-8")
print(len(man), "clips in", out)
