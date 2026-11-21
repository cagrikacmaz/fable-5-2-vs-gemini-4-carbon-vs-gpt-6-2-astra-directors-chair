# Regression: t-a

Run 2026-11-21T15:07:04.704Z (47 s) on a mirror; the film folder was only read. Mirrored: `BRIEF.md`, `OPEN_QUESTIONS.md`, `clips`, `audio`, `out/cues.md`. Offline: audio from the cache only.

## Result: PASS, the new master matches the existing one

| Check | Existing | New | Result |
|---|---|---|---|
| Format, frames | 1920x1080 @ 24/1, 720 fr, 30.000 s | 1920x1080 @ 24/1, 720 fr, 30.000 s | PASS |
| Loudness | -14.00 LUFS, -1.60 dBTP | -14.00 LUFS, -1.60 dBTP | PASS |
| Picture (framemd5) | 720 frames | 720 frames | PASS: 720/720 identical |
| Audio (decoded) | | | PASS: bit-identical |
| EDL table | | | PASS |
| Cue table | | | PASS |

## briefcut files at run time

| File | sha1 |
|---|---|
| `core/assets.mjs` | 6280ee8000 |
| `core/audition.mjs` | 7a72c52c15 |
| `core/autocues.mjs` | 2539136370 |
| `core/beats.mjs` | 8353c145b1 |
| `core/brief.mjs` | 08d6ccd32e |
| `core/cut.mjs` | 11a9d846ee |
| `core/edl.mjs` | 0f9df8e215 |
| `core/env.mjs` | 037bb8e210 |
| `core/estimate.mjs` | 80e0c0d905 |
| `core/ff.mjs` | e322e95d1b |
| `core/generate.mjs` | 198afe2e18 |
| `core/ingest.mjs` | a358b7d83e |
| `core/master.mjs` | 17d9fcc316 |
| `core/mix.mjs` | b18fd53eba |
| `core/pitch.mjs` | 633c0aeeb9 |
| `core/prepare.mjs` | 838808cca6 |
| `core/prompts.mjs` | 94d3f7df3b |
| `core/qa.mjs` | 3edef4cff4 |
| `core/regress.mjs` | 6e1d5e0078 |
| `core/report.mjs` | c36672f427 |
| `core/sfx.mjs` | 820e6bb427 |
| `core/sheets.mjs` | a8afe6bf9f |
| `core/strips.mjs` | 56635131eb |
| `core/sync-check.mjs` | 04bb59d98a |
| `core/util.mjs` | 70bdd7f226 |
| `core/video.mjs` | 9f3bbee5e5 |
| `core/voices.mjs` | 7eb7660e64 |
| `presets/default.json` | 8ad0bce270 |
| `presets/kids-channel.json` | 3e853b7ecb |
| `providers/audio/elevenlabs.mjs` | 9da9f18943 |
| `providers/audio/index.mjs` | f8392f8f21 |
| `providers/audio/local.mjs` | a0c0e473ef |
| `providers/audio/mock.mjs` | ee45552d0c |
| `providers/video/download.mjs` | f233a849e6 |
| `providers/video/fal.mjs` | c9d756a314 |
| `providers/video/gemini-omni.mjs` | f49e4a2ffa |
| `providers/video/handoff.mjs` | c0a39f2932 |
| `providers/video/higgsfield.mjs` | 0247162be3 |
| `providers/video/index.mjs` | 58aaa99453 |
| `providers/video/mock.mjs` | 873deeceef |
