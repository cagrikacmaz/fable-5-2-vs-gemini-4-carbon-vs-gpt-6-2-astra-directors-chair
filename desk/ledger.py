#!/usr/bin/env python3
"""Desk: write LEDGER.md for each director, cumulative over all rounds so far.
usage: ledger.py [last_round]       (default 2; same template and wording for all three directors)"""
import json, re, subprocess, sys
from pathlib import Path
DESK = Path(__file__).resolve().parent
ROOT = DESK.parent
last = int(sys.argv[1]) if len(sys.argv) > 1 else 2
ROUNDS = list(range(1, last + 1))
BUD = {"flow": 400, "el": 3000, "music": 4}

def load(p, default):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default

def dur(p):
    try:
        return round(float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                          capture_output=True, text=True).stdout.strip()), 2)
    except Exception:
        return None

ORD = {r: load(DESK / "orders" / ("orders-%d.json" % r), {}) for r in ROUNDS}
SND = {r: load(DESK / "sound" / ("sound-ledger-%d.json" % r), {}) for r in ROUNDS}
NOTES = {r: load(DESK / ("desk-notes-%d.json" % r), {}) for r in ROUNDS}
VL = load(DESK / "sound" / "voice-labels.json", {})

for d in ("t-a", "t-b", "t-c"):
    music_all = [m for r in ROUNDS for m in ORD[r][d]["music"]]
    per = {}
    for r in ROUNDS:
        o = ORD[r][d]
        real = {k: v for k, v in SND[r].get(d, {}).items() if not v.get("mock")}
        per[r] = {"flow": sum(int(v["cost"]) for v in o["video"]),
                  "el": sum(int(v["expected_credits"]) for v in real.values()),
                  "el_ordered": sum(int(x["cost"]) for x in o["sound"]),
                  "n_real": len(real), "n_sound": len(o["sound"]), "music": len(o["music"]), "real": real}
    def row(name, key, budget):
        cells = []
        for r in ROUNDS:
            p = per[r]
            if key == "el" and p["n_real"] < p["n_sound"]:
                cells.append("%d ordered, %d of %d files made" % (p["el_ordered"], p["n_real"], p["n_sound"]))
            else:
                cells.append(str(p[key]))
        used = sum(per[r]["el" if key == "el" and per[r]["n_real"] == per[r]["n_sound"] else ("el_ordered" if key == "el" else key)] for r in ROUNDS)
        return "| %s | %d | %s | %d | %d |" % (name, budget, " | ".join(cells), used, budget - used)
    L = ["# Ledger after round %d" % last, "",
         "Written by the production desk. Same template for every director. Production is closed after round %d." % last, "",
         "## Budget", "",
         "| | budget | " + " | ".join("round %d" % r for r in ROUNDS) + " | total | remaining |",
         "|---|---|" + "---|" * len(ROUNDS) + "---|---|",
         row("Flow credits (video)", "flow", BUD["flow"]),
         row("ElevenLabs credits (sound effects, voice)", "el", BUD["el"]),
         row("Flow Music attempts", "music", BUD["music"]), ""]
    for r in reversed(ROUNDS):
        o = ORD[r][d]; dl = ROOT / d / ("dailies-%d" % r)
        clips = load(dl / "clips.json", {})
        vorders = {int(v["order"]): v for v in o["video"]}
        L += ["# Round %d" % r, "",
              "## Video: dailies-%d/" % r, "",
              "Every clip was generated from your prompt as written, at the model, length and count you ordered, then downloaded with Flow's 1080p upscale. "
              "A 2 fps contact sheet of each clip is in dailies-%d/sheets/ under the same name. Clip audio is not used in the edit." % r, "",
              "| file | order | label | model | ordered s | delivered s | size | credits |", "|---|---|---|---|---|---|---|---|"]
        by_o = {}
        for name in sorted(clips):
            by_o.setdefault(int(name.split("_")[0]), []).append(name)
        for k in sorted(vorders):
            v = vorders[k]; names = by_o.get(k, [])
            each = int(v["cost"]) / max(1, int(v["outputs"]))
            if not names:
                L.append("| (not delivered) | %d | %s | %s | %s | | | %s |" % (k, v["label"], v["model"], v["duration"], v["cost"]))
            for n in names:
                c = clips[n]
                L.append("| %s | %d | %s | %s | %s | %s | %sx%s | %g |" % (n, k, v["label"], v["model"], v["duration"], c["seconds"], c["width"], c["height"], each))
        L += ["", "Delivered %d of %d ordered clips. Flow credits charged: %d." % (len(clips), sum(int(v["outputs"]) for v in o["video"]), per[r]["flow"]), "",
              "## Music: dailies-%d/music/" % r, "",
              "Each description was given to Flow Music as written, instrumental mode on. Flow Music has no length setting and returns tracks of its own length. Nothing was trimmed.", "",
              "| file | order | your label | delivered s |", "|---|---|---|---|"]
        for f in sorted((dl / "music").glob("*.wav")) if (dl / "music").exists() else []:
            m = re.search(r"(\d)", f.stem); idx = int(m.group(1)) - 1 if m else 0
            mo = music_all[idx] if idx < len(music_all) else {"order": "", "label": ""}
            L.append("| %s | %s | %s | %s |" % (f.name, mo["order"], mo["label"], dur(f)))
        L += ["", "## Sound effects and voice: dailies-%d/audio/" % r, ""]
        real = per[r]["real"]
        if real:
            L += ["Each prompt and script line was sent as written. A length was set only where you gave one. Credits are counted at the brief's rates: 11 per second, 100 for an automatic length, 1 per character of voice.", "",
                  "| file | order | type | ordered s | delivered s | leading silence s | credits | voice used |", "|---|---|---|---|---|---|---|---|"]
            for label, v in real.items():
                L.append("| %s.mp3 | %s | %s | %s | %s | %s | %s | %s |" % (label, v.get("order"), v["type"], v.get("seconds_ordered", "as spoken"), v.get("seconds_delivered"),
                         v.get("onset_seconds"), v["expected_credits"], (v.get("voice") or {}).get("library_name") or ""))
            L += ["", "Delivered %d of %d ordered files. ElevenLabs credits: %d." % (len(real), per[r]["n_sound"], per[r]["el"])]
            vs = {}
            for v in real.values():
                if v.get("voice"): vs[v["voice_description"]] = v["voice"]
            if vs:
                L += ["", "Voices. Rule applied to every director: Voice Library search with your description, first result; if the search is empty, the text before the first comma; if still empty, the gender and age words as filters. A result must carry the gender your description states. The library's own labels for each voice are listed so you can see what you got.", ""]
                for desc, v in vs.items():
                    lab = VL.get(v.get("library_name"), {})
                    labs = ", ".join("%s: %s" % (k, lab[k]) for k in ("gender", "age", "language", "accent", "descriptive", "use_case") if lab.get(k))
                    L.append("- \"%s\" -> %s (rule step %s, result %s). Library labels: %s" % (desc, v.get("library_name"), v.get("rule_step"), v.get("result_rank"), labs or "not listed"))
        else:
            L.append("Not generated yet.")
        nt = NOTES[r]
        if nt.get(d) or nt.get("all"):
            L += ["", "## Desk notes, round %d" % r, ""] + ["- " + n for n in nt.get("all", []) + nt.get(d, [])]
        L.append("")
    (ROOT / d / "LEDGER.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(d, "LEDGER.md:", {r: (per[r]["flow"], per[r]["el"], per[r]["music"]) for r in ROUNDS})
