# MORROW report

Generated 2026-11-21T15:10:58.948Z by briefcut from `BRIEF.md` (preset `default`, version 1).

## QA

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Duration 30-30 s | PASS | 30.000 s, 720 frames (EDL total 720) |
| 2 | Loudness -14 LUFS ±0.5, true peak ≤ -1 dBTP, no clipping | PASS | I -13.90 LUFS, TP -1.30 dBTP, LRA 5.30 LU (measured on the exported AAC); sample peak -1.41 dBFS, 0 samples at full scale |
| 3 | Every event and cue placed or logged | PASS | 10 placed, 0 dropped; 0 event(s) not found |
| 4 | Every sound within ±1 frame of its frame, measured on the master | PASS | worst 0.00 frames over 10 sounds; each sound located in the master by cross-correlation against the premix (see Cues), frames checked on sync_check.jpg |
| 5 | First frame not black; last frame is the end card | PASS | mean luma first 76.98, last 7.77 (0-255), brightest end-card pixel 226 |
| 6 | No audio from the source clips in the master | PASS | 1 audio stream in the master (the mix); picture rendered with -an, 7 source clip audio stream(s) never mapped |
| 7 | Hard cuts only: no speed change, freeze, reverse, zoom or transition | PASS | render graph holds trim, scale, colour, card text and concat only (out/work/render_graph.txt) |
| 8 | Min shot 2 s | PASS | shortest shot 2.333 s |
| 9 | Cuts on the music grid (±0 frames allowed) | PASS | worst cut 18.97 ms from a beat (one frame = 41.67 ms) |
| 10 | No silence below -50 dBFS longer than 1.5 s | PASS | none |
| 11 | Making-of numbers | n/a | takes used 7, rejected 0; local audio: 67 TTS characters, 2 TTS, 8 SFX, 1 music, 1 ambience generations in the cache (0 made this run, 12 reused); est. 0.00 USD; runtime 65.46 s |

## Edit decision list (as rendered)

| # | Source | Listed in-out (s) | Rendered in-out (s) | Nudge in/out (frames) | Timeline (s) | Length (s) | Cut vs beat (ms) | Content | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S1_TOW | 0.000-2.792 | 0.000-2.792 | 0/0 | 0.000-2.792 | 2.792 | 18.97 | Start with the line already stretched across the bright disk. Give the eye time to follow it down to the tug. | - |
| 2 | S2_HELM | 0.500-3.333 | 0.500-3.333 | 0/0 | 2.792-5.625 | 2.833 | 3.74 | Cut inside. The skipper turns the wooden wheel. The trees and the blue bridge share the window. | - |
| 3 | S3_FORK | 2.167-5.458 | 2.167-5.458 | 0/0 | 5.625-8.917 | 3.292 | 16.33 | See the result from above. The white wake curls past the orchard and the bow points into the arch. | - |
| 4 | S4_WINCH | 0.208-2.542 | 0.208-2.542 | 0/0 | 8.917-11.250 | 2.333 | 7.47 | Her plum sleeve crosses the black drum. Stay for the downstroke and the return. | - |
| 5 | S5_ARCH | 0.000-3.750 | 0.000-3.750 | 0/0 | 11.250-15.000 | 3.750 | 9.96 | Look aft. The brick ceiling glows above a single sun. Blue masonry recedes around both sides of the deck. | - |
| 6 | S6_THAW | 0.333-5.458 | 0.333-5.458 | 0/0 | 15.000-20.125 | 5.125 | 17.86 | An ice plate slips off a harbour step. Hold until gold water spills down the exposed treads. | - |
| 7 | S7_BREAD | 0.875-5.583 | 0.875-5.583 | 0/0 | 20.125-24.833 | 4.708 | 6.09 | From the sill, the baker offers warm bread. The skipper takes its weight. Let the floury hand withdraw. | - |
| 8 | END_CARD | 0.000-5.167 | 0.000-5.167 | 0/0 | 24.833-30.000 | 5.167 | - | Black card. Give the release and pre-order information the same screen time as the name. | - |

## Events

From `out/cues.md` (2 fps sheets, then 8 and 24 fps strips). Timeline = where the event frame lands in the cut.

| Clip | Event | Source t (s) | Source frame | Timeline (s) | Found |
|---|---|---|---|---|---|
| END_CARD | start | 0.000 | 0 | 24.833 | yes |
| END_CARD | text_in | 0.000 | 0 | 24.833 | yes |

## Cues

Times in timeline seconds. Picture = the event frame. Target = picture + offset: where the sound must be heard to start. Effects are placed by their attack point (the first 5 ms window within 10 dB of the loudest window of the trimmed take), voices by their gated onset. Heard = where that point sits in the master: the take's first 80 ms are located in the master audio by cross-correlation (shift column) and the shift is added to the target. Error = heard - target, in frames. The frames themselves are verified by eye on sync_check.jpg, cut from the master.

| # | Scene | Sound | Event | Offset | Picture | Target | Heard | Error (frames) | Shift in master (ms) | Variant / file | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S1_TOW | sfx:rope_catch | - | +0.00 | 0.125 | 0.125 | 0.125 | +0.00 | 0.00 | sfx_rope_catch_1.mp3 | placed | - |
| 2 | S2_HELM | sfx:wheel_grip | - | +0.00 | 2.792 | 2.792 | 2.792 | +0.00 | 0.00 | sfx_wheel_grip_1.mp3 | placed | gain -5 dB |
| 3 | S2_HELM | Baker `Mind the bridge. You lost a morning there once.` | - | +0.00 | 2.875 | 2.875 | 2.875 | +0.00 | 0.00 | vo_3_baker.mp3 | placed | voice Baker |
| 4 | S3_FORK | sfx:hull_wash | - | +0.00 | 6.458 | 6.458 | 6.458 | +0.00 | 0.00 | sfx_hull_wash_1.mp3 | placed | gain -9 dB |
| 5 | S4_WINCH | sfx:drum_turn | - | +0.00 | 9.542 | 9.542 | 9.542 | +0.00 | 0.00 | sfx_drum_turn_1.mp3 | placed | gain -4 dB |
| 6 | S5_ARCH | sfx:arch_tail | - | +0.00 | 11.917 | 11.917 | 11.917 | +0.00 | 0.00 | sfx_arch_tail_1.mp3 | placed | gain -6 dB |
| 7 | S6_THAW | sfx:ice_release | - | +0.00 | 15.542 | 15.542 | 15.542 | +0.00 | 0.00 | sfx_ice_release_1.mp3 | placed | gain -2 dB |
| 8 | S6_THAW | sfx:stair_wash | - | +0.00 | 18.625 | 18.625 | 18.625 | +0.00 | 0.00 | sfx_stair_wash_1.mp3 | placed | gain -3 dB |
| 9 | S7_BREAD | Baker `Still like the heel?` | - | +0.00 | 20.625 | 20.625 | 20.625 | +0.00 | 0.00 | vo_9_baker.mp3 | placed | voice Baker |
| 10 | S7_BREAD | sfx:loaf_lift | - | +0.00 | 23.750 | 23.750 | 23.750 | +0.00 | 0.00 | sfx_loaf_lift_1.mp3 | placed | gain -5 dB |

## Mix and master

- A2 voices peak-normalized to -6 dBFS; A3 effects to -10 dBFS peak.
- A4 music: take 1 of 1 (steadiest: local tempo spread take 1 7.95 BPM); 128.09 BPM detected, downbeat at 1.290 s of the file placed on timeline 0.000 s; -22 dBFS RMS where it plays (gain -0.30 dB), ducked up to 5.00 dB under the voices.
- A5 ambience at -31 dBFS RMS under the whole film (gain 11.57 dB), 1 s fade out at the end.
- Pre-master -18.48 LUFS / 4.95 dBTP; gain 4.75 dB; limiter ceiling -1.5 dBTP at 4x oversampling (latency compensated); loudnorm pass 2 output -13.82 LUFS, -1.48 dBTP, mode linear.
- Export: `out/MORROW_master.mp4` 1920x1080, 24 fps, H.264 CRF 18 (slow), yuv420p, BT.709, AAC 192k 48 kHz; `out/MORROW_preview_360p.mp4`.
- End card: 5.166667 s, font `segoeuib.ttf`, "MORROW UNDER TOW" (9%), "Who gets the morning?" (5%, 90%), "17 SEPTEMBER 2027" (5%), "PRE-ORDER · US$34.99" (5%), fade in 0.001 s.

## Momentary loudness, last 5 s

Master, 400 ms windows, value at the window end. End card from 24.833 s.

| t (s) | M (LUFS) |
|---|---|
| 25.00 | -15.86 |
| 25.20 | -17.24 |
| 25.40 | -17.06 |
| 25.60 | -17.31 |
| 25.80 | -16.94 |
| 26.00 | -14.78 |
| 26.20 | -14.00 |
| 26.40 | -14.16 |
| 26.60 | -14.94 |
| 26.80 | -16.23 |
| 27.00 | -17.27 |
| 27.20 | -17.42 |
| 27.40 | -17.18 |
| 27.60 | -16.09 |
| 27.80 | -14.83 |
| 28.00 | -14.70 |
| 28.20 | -15.24 |
| 28.40 | -15.56 |
| 28.60 | -14.78 |
| 28.80 | -14.15 |
| 29.00 | -14.34 |
| 29.20 | -15.39 |
| 29.40 | -16.93 |
| 29.60 | -15.84 |
| 29.80 | -15.78 |

## Decisions and log

- **clip audio**: 7 source clip(s) carry an audio stream (S1_TOW.mp4, S2_HELM.mp4, S3_FORK.mp4, S4_WINCH.mp4, S5_ARCH.mp4, S6_THAW.mp4, S7_BREAD.mp4); it is discarded, as the brief says
- **music tempo**: ordered 120 BPM, detected 128.09; the detected grid is used
