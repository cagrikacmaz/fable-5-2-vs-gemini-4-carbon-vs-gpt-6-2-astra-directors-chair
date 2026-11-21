# MOONDRAWN report

Generated 2026-11-21T12:01:33.272Z by briefcut from `BRIEF.md` (preset `default`, version 1).

## QA

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Duration 30-30 s | PASS | 30.000 s, 720 frames (EDL total 720) |
| 2 | Loudness -14 LUFS ±0.5, true peak ≤ -1 dBTP, no clipping | PASS | I -14.00 LUFS, TP -1.60 dBTP, LRA 6.80 LU (measured on the exported AAC); sample peak -1.67 dBFS, 0 samples at full scale |
| 3 | Every event and cue placed or logged | PASS | 28 placed, 0 dropped; 0 event(s) not found |
| 4 | Every sound within ±1 frame of its frame, measured on the master | PASS | worst 0.00 frames over 28 sounds; each sound located in the master by cross-correlation against the premix (see Cues), frames checked on sync_check.jpg |
| 5 | Music silent after the hard stop (A4 below -60 dBFS from stop + 20 ms) | PASS | stop at 26.917 s; A4 peak afterwards digital silence |
| 6 | First sound (drain) within the first 0.5 s | PASS | drain at 0.000 s |
| 7 | First frame not black; last frame is the end card | PASS | mean luma first 110.50, last 6.96 (0-255), brightest end-card pixel 225 |
| 8 | No audio from the source clips in the master | PASS | 1 audio stream in the master (the mix); picture rendered with -an, 13 source clip audio stream(s) never mapped |
| 9 | Hard cuts only: no speed change, freeze, reverse, zoom or transition | PASS | render graph holds trim, scale, colour, card text and concat only (out/work/render_graph.txt) |
| 10 | Min shot 1 s | PASS | shortest shot 1.000 s |
| 11 | Cuts on the music grid (±0 frames allowed) | PASS | worst cut 0.09 ms from a beat (one frame = 41.67 ms) |
| 12 | No silence below -50 dBFS longer than 1.5 s | PASS | none |
| 13 | Making-of numbers | n/a | takes used 13, rejected 0; local audio: 200 TTS characters, 8 TTS, 21 SFX, 1 music, 1 ambience generations in the cache (0 made this run, 29 reused); est. 0.00 USD; runtime 32.36 s |

## Edit decision list (as rendered)

| # | Source | Listed in-out (s) | Rendered in-out (s) | Nudge in/out (frames) | Timeline (s) | Length (s) | Cut vs beat (ms) | Content | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S02_PIER | 0.000-3.500 | 0.000-3.500 | 0/0 | 0.000-3.500 | 3.500 | 0.01 | 0.000-3.500: HOOK: she watches the whole sea run out; boats drop onto the seabed | - |
| 2 | S03_LAUNCH | 0.000-2.000 | 0.000-2.000 | 0/0 | 3.500-5.500 | 2.000 | 0.02 | 3.500-5.500: she goes after it: sand-yacht away from the stilt town, dry seabed ahead | - |
| 3 | S04_VISTA | 1.000-3.500 | 1.000-3.500 | 0/0 | 5.500-8.000 | 2.500 | 0.02 | 5.500-8.000: the open seabed: racing between colossal wrecks | - |
| 4 | S05_CITY | 0.250-2.250 | 0.250-2.250 | 0/0 | 8.000-10.000 | 2.000 | 0.03 | 8.000-10.000: a drowned city, still pouring water | - |
| 5 | S06_RELIC | 2.000-4.000 | 2.000-4.000 | 0/0 | 10.000-12.000 | 2.000 | 0.04 | 10.000-12.000: the reward: she lifts a glowing orb from a chest | - |
| 6 | S07_GIANT | 0.500-2.500 | 0.500-2.500 | 0/0 | 12.000-14.000 | 2.000 | 0.05 | 12.000-14.000: something asleep: she walks under a stranded giant | - |
| 7 | S08_EYE | 0.375-1.875 | 0.375-1.875 | 0/0 | 14.000-15.500 | 1.500 | 0.05 | 14.000-15.500: it wakes: the eye opens on her | - |
| 8 | S09_BOOTS | 1.250-2.750 | 1.250-2.750 | 0/0 | 15.500-17.000 | 1.500 | 0.06 | 15.500-17.000: the turn: water comes back around her boots | - |
| 9 | S14_RETURN | 1.500-3.500 | 1.500-3.500 | 0/0 | 17.000-19.000 | 2.000 | 0.06 | 17.000-19.000: the price: the sea as a wall, she backs away | - |
| 10 | S10_WALL | 2.500-3.500 | 2.500-3.500 | 0/0 | 19.000-20.000 | 1.000 | 0.07 | 19.000-20.000: the chase: the wall smashes the wrecks behind her | - |
| 11 | S11_CHASE | 0.500-1.500 | 0.500-1.500 | 0/0 | 20.000-21.000 | 1.000 | 0.07 | 20.000-21.000: close on her at the tiller, the wave gaining | - |
| 12 | S12_RISE | 2.000-4.000 | 2.000-4.000 | 0/0 | 21.000-23.000 | 2.000 | 0.08 | 21.000-23.000: the giant swims out of the wave beside her | - |
| 13 | S13_LEAP | 0.000-2.000 | 0.000-2.000 | 0/0 | 23.000-25.000 | 2.000 | 0.09 | 23.000-25.000: she jumps the crest, against the moon | - |
| 14 | END_CARD | 0.000-5.000 | 0.000-5.000 | 0/0 | 25.000-30.000 | 5.000 | - | 25.000-30.000: title, tagline, release date, price | - |

## Events

From `out/cues.md` (2 fps sheets, then 8 and 24 fps strips). Timeline = where the event frame lands in the cut.

| Clip | Event | Source t (s) | Source frame | Timeline (s) | Found |
|---|---|---|---|---|---|
| S02 | drain | 0.000 | 0 | 0.000 | yes |
| S02 | boats_drop | 1.833 | 44 | 1.833 | yes |
| S06 | orb_lift | 2.542 | 61 | 10.542 | yes |
| S08 | eye_open | 0.875 | 21 | 14.500 | yes |
| S09 | water_in | 1.542 | 37 | 15.792 | yes |
| S10 | wreck_hit | 2.583 | 62 | 19.083 | yes |
| S12 | breach | 2.833 | 68 | 21.833 | yes |
| S13 | riser_peak | 1.208 | 29 | 24.208 | yes |
| END_CARD | start | 0.000 | 0 | 25.000 | yes |
| END_CARD | text_in | 0.250 | 6 | 25.250 | yes |
| END_CARD | stop | 1.917 | 46 | 26.917 | yes |
| END_CARD | boom | 2.000 | 48 | 27.000 | yes |

## Cues

Times in timeline seconds. Picture = the event frame. Target = picture + offset: where the sound must be heard to start. Effects are placed by their attack point (the first 5 ms window within 10 dB of the loudest window of the trimmed take), voices by their gated onset. Heard = where that point sits in the master: the take's first 80 ms are located in the master audio by cross-correlation (shift column) and the shift is added to the target. Error = heard - target, in frames. The frames themselves are verified by eye on sync_check.jpg, cut from the master.

| # | Scene | Sound | Event | Offset | Picture | Target | Heard | Error (frames) | Shift in master (ms) | Variant / file | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S02_PIER | sfx:sea_drain | drain | +0.00 | 0.000 | 0.000 | 0.000 | +0.00 | 0.00 | sfx_sea_drain_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 2 | S02_PIER | Narrator `Once a day, the moon takes the sea away.` | drain | +0.15 | 0.000 | 0.150 | 0.150 | +0.00 | 0.00 | vo_2_narrator.mp3 | placed | voice Don - Movie Trailer Narrator; compressed 6:1 above -30 dBFS |
| 3 | S02_PIER | sfx:boats_drop | boats_drop | +0.00 | 1.833 | 1.833 | 1.833 | +0.00 | 0.00 | sfx_boats_drop_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 4 | S03_LAUNCH | sfx:sail_snap | start | +0.00 | 3.500 | 3.500 | 3.500 | +0.00 | 0.00 | sfx_sail_snap_1.mp3 | placed | - |
| 6 | S03_LAUNCH | Narrator `You have one hour.` | start | +0.30 | 3.500 | 3.800 | 3.800 | +0.00 | 0.00 | vo_6_narrator.mp3 | placed | voice Don - Movie Trailer Narrator; compressed 6:1 above -30 dBFS |
| 5 | S03_LAUNCH | sfx:skiff_run | start | +0.50 | 3.500 | 4.000 | 4.000 | +0.00 | 0.00 | sfx_skiff_run_1.mp3 | placed | - |
| 7 | S04_VISTA | sfx:skiff_run | start | +0.40 | 5.500 | 5.900 | 5.900 | +0.00 | 0.00 | sfx_skiff_run_2.mp3 | placed | - |
| 8 | S04_VISTA | Narrator `Everything it ever swallowed is waiting down there.` | start | +0.40 | 5.500 | 5.900 | 5.900 | +0.00 | 0.00 | vo_8_narrator.mp3 | placed | voice Don - Movie Trailer Narrator; compressed 6:1 above -30 dBFS |
| 9 | S05_CITY | sfx:ruin_falls | start | +0.00 | 8.000 | 8.000 | 8.000 | +0.00 | 0.00 | sfx_ruin_falls_1.mp3 | placed | - |
| 10 | S06_RELIC | sfx:relic_shimmer | orb_lift | +0.00 | 10.542 | 10.542 | 10.542 | +0.00 | 0.00 | sfx_relic_shimmer_1.mp3 | placed | - |
| 11 | S07_GIANT | sfx:giant_breath | start | +0.50 | 12.000 | 12.500 | 12.500 | +0.00 | 0.00 | sfx_giant_breath_1.mp3 | placed | - |
| 12 | S08_EYE | sfx:eye_open | eye_open | +0.00 | 14.500 | 14.500 | 14.500 | +0.00 | 0.00 | sfx_eye_open_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 13 | S08_EYE | sfx:eye_sub | eye_open | +0.00 | 14.500 | 14.500 | 14.500 | +0.00 | 0.00 | sfx_eye_sub_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 14 | S08_EYE | Narrator `Then it comes back.` | eye_open | +0.45 | 14.500 | 14.950 | 14.950 | +0.00 | 0.00 | vo_14_narrator.mp3 | placed | voice Don - Movie Trailer Narrator; compressed 6:1 above -30 dBFS; gain +3 dB (peak 1 dBFS) |
| 15 | S09_BOOTS | sfx:water_rush | water_in | +0.00 | 15.792 | 15.792 | 15.792 | +0.00 | 0.00 | sfx_water_rush_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 16 | S14_RETURN | sfx:wall_long | start | +0.00 | 17.000 | 17.000 | 17.000 | +0.00 | 0.00 | sfx_wall_long_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 17 | S14_RETURN | sfx:wall_roar | start | +0.00 | 17.000 | 17.000 | 17.000 | +0.00 | 0.00 | sfx_wall_roar_1.mp3 | placed | ducked 8 dB under the voices (80 ms attack, 300 ms release) |
| 18 | S10_WALL | sfx:wreck_crash | wreck_hit | +0.00 | 19.083 | 19.083 | 19.083 | +0.00 | 0.00 | sfx_wreck_crash_1.mp3 | placed | - |
| 19 | S11_CHASE | sfx:skiff_run | start | +0.50 | 20.000 | 20.500 | 20.500 | +0.00 | 0.00 | sfx_skiff_run_1.mp3 | placed | - |
| 20 | S12_RISE | sfx:giant_call | start | +0.00 | 21.000 | 21.000 | 21.000 | +0.00 | 0.00 | sfx_giant_call_1.mp3 | placed | - |
| 21 | S12_RISE | sfx:whale_breach | breach | +0.00 | 21.833 | 21.833 | 21.833 | +0.00 | 0.00 | sfx_whale_breach_1.mp3 | placed | - |
| 22 | S13_LEAP | sfx:leap_whoosh | start | +0.00 | 23.000 | 23.000 | 23.000 | +0.00 | 0.00 | sfx_leap_whoosh_1.mp3 | placed | - |
| 23 | S13_LEAP | sfx:riser | riser_peak | +0.00 | 24.208 | 24.208 | 24.208 | +0.00 | 0.00 | sfx_riser_1.mp3 | placed | - |
| 24 | END_CARD | sfx:title_crack | start | +0.00 | 25.000 | 25.000 | 25.000 | +0.00 | 0.00 | sfx_title_crack_1.mp3 | placed | ducked 10 dB under the voices (80 ms attack, 300 ms release) |
| 25 | END_CARD | sfx:title_slam | start | +0.00 | 25.000 | 25.000 | 25.000 | +0.00 | 0.00 | sfx_title_slam_1.mp3 | placed | ducked 10 dB under the voices (80 ms attack, 300 ms release) |
| 26 | END_CARD | Narrator `Moondrawn.` | start | +0.85 | 25.000 | 25.850 | 25.850 | +0.00 | 0.00 | vo_26_narrator_v2.mp3 | placed | voice Don - Movie Trailer Narrator; compressed 6:1 above -30 dBFS |
| 28 | END_CARD | sfx:title_boom | boom | +0.00 | 27.000 | 27.000 | 27.000 | +0.00 | 0.00 | sfx_title_boom_1.mp3 | placed | ducked 10 dB under the voices (80 ms attack, 300 ms release) |
| 27 | END_CARD | Narrator `Be back before the sea is.` | stop | +0.40 | 26.917 | 27.317 | 27.317 | +0.00 | 0.00 | vo_27_narrator.mp3 | placed | voice Don - Movie Trailer Narrator; compressed 6:1 above -30 dBFS |

## Mix and master

- A2 voices peak-normalized to -2 dBFS; A3 effects to -10 dBFS peak (sea_drain -6, boats_drop -15, sail_snap -8, skiff_run -13, ruin_falls -16, relic_shimmer -13, giant_breath -9, eye_open -7, eye_sub -14, water_rush -12, wall_long -7, wall_roar -6, wreck_crash -8, giant_call -6, whale_breach -8, leap_whoosh -8, riser -10, title_crack -3, title_slam -6, title_boom -5).
- A4 music: take 1 of 1 (steadiest: local tempo spread take 1 0.08 BPM); 120.00 BPM detected, downbeat at 0.047 s of the file placed on timeline 1.000 s; -20 dBFS RMS where it plays (gain -3.80 dB), ducked up to 6.00 dB under the voices; hard stop at 26.917 s with a 20 ms fade.
- A5 ambience at -36 dBFS RMS under the whole film (gain 2.90 dB), 1 s fade out at the end.
- Pre-master -13.53 LUFS / 1.81 dBTP; gain -0.51 dB; limiter ceiling -2 dBTP at 4x oversampling (latency compensated); loudnorm pass 2 output -13.92 LUFS, -1.98 dBTP, mode linear.
- Effects ducked under the voices (keyed like the music): sea_drain 8 dB, 80 ms attack, 300 ms release; boats_drop 8 dB, 80 ms attack, 300 ms release; eye_open 8 dB, 80 ms attack, 300 ms release; eye_sub 8 dB, 80 ms attack, 300 ms release; water_rush 8 dB, 80 ms attack, 300 ms release; wall_long 8 dB, 80 ms attack, 300 ms release; wall_roar 8 dB, 80 ms attack, 300 ms release; title_crack 10 dB, 80 ms attack, 300 ms release; title_slam 10 dB, 80 ms attack, 300 ms release; title_boom 10 dB, 80 ms attack, 300 ms release.
- Voice dynamics: narrator compressed 6:1 above -30 dBFS (5 ms attack, 100 ms release), then back to the voice's peak level.
- Export: `out/MOONDRAWN_master.mp4` 1920x1080, 24 fps, H.264 CRF 16 (slow), yuv420p, BT.709, AAC 192k 48 kHz; `out/MOONDRAWN_preview_360p.mp4`.
- End card: 5 s, font `bahnschrift.ttf`, "MOONDRAWN" (14%), "Be back before the sea is." (6%, 85%), "February 26, 2027" (5%), "Pre-order now  $59.99" (5%, 85%), fade in 0.25 s.

## Momentary loudness, last 5 s

Master, 400 ms windows, value at the window end. End card from 25.000 s.

| t (s) | M (LUFS) |
|---|---|
| 25.00 | -9.73 |
| 25.20 | -10.88 |
| 25.40 | -10.77 |
| 25.60 | -12.06 |
| 25.80 | -12.43 |
| 26.00 | -13.49 |
| 26.20 | -15.23 |
| 26.40 | -15.92 |
| 26.60 | -16.52 |
| 26.80 | -18.83 |
| 27.00 | -21.73 |
| 27.20 | -15.31 |
| 27.40 | -14.15 |
| 27.60 | -17.20 |
| 27.80 | -20.20 |
| 28.00 | -21.46 |
| 28.20 | -21.01 |
| 28.40 | -19.28 |
| 28.60 | -19.71 |
| 28.80 | -17.64 |
| 29.00 | -16.77 |
| 29.20 | -19.66 |
| 29.40 | -21.71 |
| 29.60 | -18.49 |
| 29.80 | -19.57 |

## Decisions and log

- **clip audio**: 13 source clip(s) carry an audio stream (S02_PIER.mp4, S03_LAUNCH.mp4, S04_VISTA.mp4, S05_CITY.mp4, S06_RELIC.mp4, S07_GIANT.mp4, S08_EYE.mp4, S09_BOOTS.mp4, S14_RETURN.mp4, S10_WALL.mp4, S11_CHASE.mp4, S12_RISE.mp4, S13_LEAP.mp4); it is discarded, as the brief says
- **loudness**: MOONDRAWN_master.mp4: loudnorm's target was biased -0.20 LU so the export measures -14 LUFS on the EBU R128 meter (loudnorm's internal meter reads this short film differently)
