#!/usr/bin/env python3
"""Production desk: ElevenLabs sound effects and voiceover for the trailer experiment.

Reads the directors' orders from ../orders/orders-<round>.json and writes one mp3 per order to
<root>/<director>/dailies-<round>/audio/<label>.mp3. Prompts, scripts and lengths are sent exactly
as the director wrote them. No music is generated here.

Usage:
  python make_sound.py --dry-run              plan and expected credits, no network
  python make_sound.py --mock --test-root C:\\trailers\\_desk\\sound\\_mocktest   test tones, no API (needs ffmpeg)
  python make_sound.py                        real run, all three directors
  python make_sound.py --only t-a             one director
  python make_sound.py --regen t-b:bore_horn_1   regenerate one file

The API key is read from .env.txt (ELEVENLABS_API_KEY=...) next to this script or one folder up.
The key is never printed. Standard library only.
"""
import argparse, json, os, re, subprocess, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DESK = HERE.parent
ROOT = DESK.parent
API = "https://api.elevenlabs.io"
TTS_MODEL = "eleven_multilingual_v2"
SFX_MODEL = "eleven_text_to_sound_v2"
BUDGET = 3000            # ElevenLabs credits per director, whole experiment
PRICE_TOLERANCE = 1.5    # stop if the first charged item costs more than expected x this
DIRECTORS = ["t-a", "t-b", "t-c"]


def read_key():
    for p in (HERE / ".env.txt", DESK / ".env.txt", HERE / ".env", DESK / ".env"):
        if p.exists():
            for line in p.read_text(encoding="utf-8-sig").splitlines():
                m = re.match(r"\s*ELEVENLABS_API_KEY\s*=\s*(.+?)\s*$", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    k = os.environ.get("ELEVENLABS_API_KEY")
    if k:
        return k
    sys.exit("ELEVENLABS_API_KEY not found. Put ELEVENLABS_API_KEY=... in %s" % (HERE / ".env.txt"))


class Api:
    def __init__(self, key):
        self.key = key

    def call(self, method, path, query=None, body=None, binary=False, timeout=120):
        url = API + path + ("?" + urllib.parse.urlencode(query) if query else "")
        data = json.dumps(body).encode("utf-8") if body is not None else None
        last = None
        for attempt in range(1, 6):
            req = urllib.request.Request(url, data=data, method=method)
            req.add_header("xi-api-key", self.key)
            if data is not None:
                req.add_header("Content-Type", "application/json")
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    raw = r.read()
                    return raw if binary else json.loads(raw.decode("utf-8") or "{}")
            except urllib.error.HTTPError as e:
                text = e.read().decode("utf-8", "replace")[:500].replace(self.key, "***")
                last = "%s %s -> %s: %s" % (method, path, e.code, text)
                if e.code == 429 or e.code >= 500:
                    time.sleep(2 * attempt)
                    continue
                raise RuntimeError(last)
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last = "%s %s: %s" % (method, path, e)
                time.sleep(2 * attempt)
        raise RuntimeError(last)

    def used(self):
        s = self.call("GET", "/v1/user/subscription")
        return int(s.get("character_count", 0)), int(s.get("character_limit", 0))

    def audio(self, path, body):
        try:
            return self.call("POST", path, query={"output_format": "mp3_44100_192"}, body=body, binary=True)
        except RuntimeError as e:
            if re.search(r"output_format|tier|plan", str(e), re.I):
                return self.call("POST", path, query={"output_format": "mp3_44100_128"}, body=body, binary=True)
            raise


def infer_filters(desc):
    d = desc.lower()
    f = {"language": "en"}
    if re.search(r"\b(woman|female|contralto|girl)\b", d):
        f["gender"] = "female"
    elif re.search(r"\b(man|male|baritone|bass)\b", d):
        f["gender"] = "male"
    if re.search(r"\b(older|old|elderly|weathered)\b", d):
        f["age"] = "old"
    elif re.search(r"middle[- ]aged", d):
        f["age"] = "middle_aged"
    elif re.search(r"\byoung\b", d):
        f["age"] = "young"
    return f


def resolve_voice(api, desc, name, cache):
    """Desk rule for 'the first library result for this description', applied mechanically:
    1. Voice Library search with the full description, first result.
    2. If empty: search with the text before the first comma, first result.
    3. If empty: gender and age words from the description as filters, English, first result.
    In every step a result must carry the gender the description states (woman/female, man/male).
    A voice that cannot be added to the account is skipped for the next result. Every step is logged."""
    if desc in cache:
        return cache[desc]
    gender = infer_filters(desc).get("gender")
    g = {"gender": gender} if gender else {}
    retired = cache.get("_retired", [])
    k = 2
    base = name
    while name in retired:
        name = "%s v%d" % (base, k)
        k += 1
    steps = [("1 full description", dict({"search": desc}, **g)),
             ("2 first clause", dict({"search": desc.split(",")[0].strip()}, **g)),
             ("3 gender and age filters", infer_filters(desc))]
    for step, q in steps:
        q = dict(q, page_size=5)
        r = api.call("GET", "/v1/shared-voices", query=q)
        for rank, v in enumerate(r.get("voices") or [], 1):
            if gender and (v.get("gender") or "").lower() not in ("", gender):
                continue
            try:
                added = api.call("POST", "/v1/voices/add/%s/%s" % (v["public_owner_id"], v["voice_id"]),
                                 body={"new_name": name})
                vid = added.get("voice_id") or v["voice_id"]
            except RuntimeError as e:
                if re.search(r"already", str(e), re.I):
                    vid = v["voice_id"]
                else:
                    print("    voice '%s' could not be added (%s), trying the next result" % (v.get("name"), str(e)[:120]))
                    continue
            cache[desc] = {"voice_id": vid, "library_voice_id": v["voice_id"], "library_name": v.get("name"),
                           "library_gender": v.get("gender"), "library_age": v.get("age"), "gender_required": gender,
                           "account_name": name, "rule_step": step, "result_rank": rank,
                           "public_owner_id": v["public_owner_id"]}
            return cache[desc]
    raise RuntimeError("no library voice found for: " + desc)


def ffprobe_seconds(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                             capture_output=True, text=True, timeout=30).stdout.strip()
        return round(float(out), 2)
    except Exception:
        return None


def onset_seconds(path):
    """Leading silence, so the edit can place the sound on its first audible sample."""
    try:
        err = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-af", "silencedetect=noise=-45dB:d=0.02", "-f", "null", "-"],
                             capture_output=True, text=True, timeout=60).stderr
        m = re.search(r"silence_start: (-?[\d.]+)[\s\S]*?silence_end: ([\d.]+)", err)
        if m and float(m.group(1)) <= 0.01:
            return round(float(m.group(2)), 3)
        return 0.0
    except Exception:
        return None


def mock_audio(path, seconds):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "lavfi", "-i",
                    "sine=frequency=330:duration=%s" % seconds, "-b:a", "128k", str(path)], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", type=int, default=1)
    ap.add_argument("--only", choices=DIRECTORS)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--regen", action="append", default=[], help="director:label, repeatable")
    ap.add_argument("--voice-report", action="store_true", help="print the labels of the voices already picked, no generation")
    ap.add_argument("--forget-voice", action="append", default=[], help="account name of a picked voice to drop, so the rule picks again")
    ap.add_argument("--test-root", help="write audio and ledgers under this folder instead (for --mock tests)")
    a = ap.parse_args()
    global ROOT, HERE
    if a.mock and not a.test_root:
        sys.exit("--mock needs --test-root <folder>, so test tones never land in a director's dailies")
    orders_file = DESK / "orders" / ("orders-%d.json" % a.round)
    if a.test_root:
        ROOT = Path(a.test_root).resolve()
        HERE = ROOT / "_desk" / "sound"
        HERE.mkdir(parents=True, exist_ok=True)

    orders = json.loads(orders_file.read_text(encoding="utf-8"))
    ledger_path = HERE / ("sound-ledger-%d.json" % a.round)
    ledger = json.loads(ledger_path.read_text(encoding="utf-8")) if ledger_path.exists() else {}
    voices_path = HERE / "voices.json"
    voices = json.loads(voices_path.read_text(encoding="utf-8")) if voices_path.exists() else {}
    regen = set(a.regen)
    live = not (a.dry_run or a.mock)
    api = Api(read_key()) if live else None
    price_checked = bool(a.regen)   # desk corrections of single files skip the first-item price check
    if a.forget_voice and live:
        for desc in [k for k, v in voices.items() if isinstance(v, dict) and v.get("account_name") in a.forget_voice]:
            voices.setdefault("_retired", []).append(voices[desc]["account_name"])
            print("forgetting voice %s (%s)" % (voices[desc]["account_name"], voices[desc].get("library_name")))
            del voices[desc]
        voices_path.write_text(json.dumps(voices, indent=2, ensure_ascii=False), encoding="utf-8")
    if a.voice_report:
        if not live:
            sys.exit("--voice-report needs the real API (no --mock, no --dry-run)")
        vl_path = HERE / "voice-labels.json"
        vl = json.loads(vl_path.read_text(encoding="utf-8")) if vl_path.exists() else {}
        for desc, v in voices.items():
            if not isinstance(v, dict):
                continue
            try:
                info = api.call("GET", "/v1/voices/" + v["voice_id"])
                labels = info.get("labels") or {}
            except RuntimeError as e:
                labels = {"error": str(e)[:100]}
            want = infer_filters(desc).get("gender")
            print("%-24s %-36s wanted gender: %-7s labels: %s" % (v.get("account_name"), v.get("library_name"), want, json.dumps(labels, ensure_ascii=False)))
            if "error" not in labels and v.get("library_name"):
                vl[v["library_name"]] = labels
        vl_path.write_text(json.dumps(vl, indent=2, ensure_ascii=False), encoding="utf-8")
        print("voice-labels.json updated:", len(vl), "voices")
        return
    # The account counter lags behind the calls, so per-item deltas undercount. The run total is
    # the counter before the first call against the counter after it has settled at the end.
    runs_path = HERE / "usage-runs.json"
    run = {"round": a.round, "started": time.strftime("%Y-%m-%d %H:%M:%S"), "counter_start": api.used()[0]} if live else None

    for d in ([a.only] if a.only else DIRECTORS):
        items = orders[d]["sound"]
        out_dir = ROOT / d / ("dailies-%d" % a.round) / "audio"
        expected = sum(int(x["cost"]) for x in items)
        print("\n== %s: %d sound orders, expected %d credits" % (d, len(items), expected))
        if a.dry_run:
            for x in items:
                print("   %-22s %-3s %5s s  %4s cr" % (x["label"], x["type"], x.get("seconds") or "auto", x["cost"]))
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        led = ledger.setdefault(d, {})
        spent = sum(int(v.get("expected_credits") or 0) for v in led.values() if not v.get("mock"))
        letters = {}
        for x in items:
            if x["type"] == "vo":
                letters.setdefault(x["voice"], chr(ord("A") + len(letters)))
        for x in items:
            label = x["label"]
            path = out_dir / (label + ".mp3")
            tag = "%s:%s" % (d, label)
            if path.exists() and path.stat().st_size > 0 and tag not in regen:
                print("   keep  %s" % label)
                continue
            if live and spent + int(x["cost"]) > BUDGET:
                sys.exit("STOP: %s would pass its %d credit budget (spent %d, next %s costs %s)" % (d, BUDGET, spent, label, x["cost"]))
            before = api.used()[0] if live else 0
            entry = {"type": x["type"], "expected_credits": int(x["cost"]), "order": x["order"]}
            if x["type"] == "sfx":
                secs = float(x["seconds"]) if x.get("seconds") else None
                entry["seconds_ordered"] = secs if secs else "auto"
                if a.mock:
                    mock_audio(path, secs or 3)
                else:
                    body = {"text": x["prompt"], "model_id": SFX_MODEL}
                    if secs:
                        body["duration_seconds"] = min(30.0, max(0.5, secs))
                    path.write_bytes(api.audio("/v1/sound-generation", body))
            else:
                desc = x["voice"]
                entry["voice_description"] = desc
                if a.mock:
                    mock_audio(path, 1.5)
                    entry["voice"] = {"voice_id": "mock"}
                else:
                    v = resolve_voice(api, desc, ("trailers %s voice %s" % (d, letters[desc])) if a.round == 1 else ("trailers r%d %s voice %s" % (a.round, d, letters[desc])), voices)
                    voices_path.write_text(json.dumps(voices, indent=2, ensure_ascii=False), encoding="utf-8")
                    entry["voice"] = v
                    path.write_bytes(api.audio("/v1/text-to-speech/" + v["voice_id"], {"text": x["script"], "model_id": TTS_MODEL}))
                entry["script"] = x["script"]
            actual = (api.used()[0] - before) if live else 0
            if live and not price_checked and int(x["cost"]) > 0:
                # the counter updates late: wait for the first charge to show before trusting it
                for _ in range(18):
                    if actual > 0:
                        break
                    time.sleep(5)
                    actual = api.used()[0] - before
            spent += int(x["cost"]) if live else 0
            entry.update(actual_credits=actual, file=str(path.relative_to(ROOT)).replace("\\", "/"),
                         seconds_delivered=ffprobe_seconds(path), onset_seconds=onset_seconds(path),
                         mock=bool(a.mock))
            led[label] = entry
            ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False), encoding="utf-8")
            print("   made  %-22s expected %4s, charged %4s, %s s" % (label, x["cost"], actual if live else "mock", entry["seconds_delivered"]))
            if live and not price_checked and int(x["cost"]) > 0:
                price_checked = True
                if actual == 0:
                    sys.exit("STOP: %s is made but the account counter did not move in 90 s, so the price cannot be checked. "
                             "Nothing else was generated. Report this before continuing." % label)
                if actual > int(x["cost"]) * PRICE_TOLERANCE:
                    sys.exit("STOP: %s was charged %d credits, the order sheet says %s. Prices differ from the brief. "
                             "Nothing else was generated. Report this before continuing." % (label, actual, x["cost"]))
        print("   %s credits at order prices: %d of %d ordered (budget %d)" % (d, spent, expected, BUDGET))

    if live:
        last, same = -1, 0
        for _ in range(36):          # up to 6 minutes; settled = unchanged for a full minute
            time.sleep(10)
            now = api.used()[0]
            same = same + 1 if now == last else 0
            last = now
            if same >= 6:
                break
        run.update(finished=time.strftime("%Y-%m-%d %H:%M:%S"), counter_end=last, credits_charged=last - run["counter_start"])
        runs = json.loads(runs_path.read_text(encoding="utf-8")) if runs_path.exists() else []
        runs.append(run)
        runs_path.write_text(json.dumps(runs, indent=2), encoding="utf-8")
        print("\nAccount counter for this run: %d credits charged (start %d, end %d)" % (run["credits_charged"], run["counter_start"], last))
    if not a.dry_run:
        lines = ["# Sound ledger, round %d" % a.round, ""]
        for d, led in ledger.items():
            exp = sum(v["expected_credits"] for v in led.values())
            act = sum(int(v.get("actual_credits") or 0) for v in led.values())
            lines += ["## %s" % d, "", "Files: %d. Expected credits: %d. Charged: %d." % (len(led), exp, act), "",
                      "| file | type | ordered s | delivered s | onset s | expected | charged | voice |", "|---|---|---|---|---|---|---|---|"]
            for label, v in led.items():
                voice = (v.get("voice") or {}).get("library_name") or ""
                lines.append("| %s.mp3 | %s | %s | %s | %s | %s | %s | %s |" % (label, v["type"], v.get("seconds_ordered", ""),
                             v.get("seconds_delivered"), v.get("onset_seconds"), v["expected_credits"], v.get("actual_credits"), voice))
            lines.append("")
        (HERE / ("SOUND-LEDGER-%d.md" % a.round)).write_text("\n".join(lines), encoding="utf-8")
        print("\nLedger: %s" % (HERE / ("SOUND-LEDGER-%d.md" % a.round)))


if __name__ == "__main__":
    main()
