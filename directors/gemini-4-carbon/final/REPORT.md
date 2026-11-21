# NEAPSCAR report

Generated 2026-11-21T12:12:02.356Z by briefcut from `BRIEF.md` (preset `default`, version 1).

## QA

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | Duration 30-30 s | PASS | 30.000 s, 720 frames (EDL total 720) |
| 2 | Loudness -14 LUFS ±0.5, true peak ≤ -1 dBTP, no clipping | PASS | I -14.10 LUFS, TP -1.10 dBTP, LRA 5.30 LU (measured on the exported AAC); sample peak -1.13 dBFS, 0 samples at full scale |
| 3 | Every event and cue placed or logged | PASS | 19 placed, 0 dropped; 0 event(s) not found |
| 4 | Every sound within ±1 frame of its frame, measured on the master | PASS | worst 0.00 frames over 19 sounds; each sound located in the master by cross-correlation against the premix (see Cues), frames checked on sync_check.jpg |
| 5 | Music silent after the hard stop (A4 below -60 dBFS from beacon_strike + 20 ms) | PASS | stop at 23.708 s; A4 peak afterwards digital silence |
| 6 | beacon_strike is the loudest moment (momentary loudness, 400 ms) | PASS | maximum M -9.04 LUFS at 24.200 s (window end); beacon_strike at 23.708 s |
| 7 | `NEAPSCAR_social.mp4`: -10 LUFS ±0.5, true peak ≤ -1 dBTP, no clipping | PASS | I -10.00 LUFS, TP -1.10 dBTP, LRA 2.60 LU (exported AAC); sample peak -1.40 dBFS, 0 samples at full scale; limiter ceiling -2.5 dBTP, loudnorm pass 2 linear |
| 8 | The narrator reads over beacon_strike: speech band 300-3000 Hz at least 6 dB above it in the line's window | PASS | 172.34 dB: narrator -27.66 dBFS RMS, beacon_strike -200.00 dBFS RMS, both band-limited to 300-3000 Hz (24 dB/octave edges), 3.850-6.624 s (cue 4), premix stems |
| 9 | Last 3 s before the end card within 8 LU of beacon_strike (momentary loudness) | PASS | beacon_strike M -9.04 LUFS at 24.200 s; lowest M from 23.750 to 26.750 s -14.26 LUFS at 25.800 s (window end), 5.22 LU below |
| 10 | First sound (anchor_hit) within the first 0.5 s | PASS | anchor_hit at 0.292 s |
| 11 | First frame not black; last frame is the end card | PASS | mean luma first 74.46, last 5.95 (0-255), brightest end-card pixel 248 |
| 12 | No audio from the source clips in the master | PASS | 1 audio stream in the master (the mix); picture rendered with -an, 8 source clip audio stream(s) never mapped |
| 13 | Hard cuts only: no speed change, freeze, reverse, zoom or transition | PASS | render graph holds trim, scale, colour, card text and concat only (out/work/render_graph.txt) |
| 14 | Min shot 2 s | PASS | shortest shot 2.792 s |
| 15 | Cuts on the music grid (±3 frames allowed) | PASS | worst cut 19.38 ms from a beat (one frame = 41.67 ms) |
| 16 | No silence below -50 dBFS longer than 1.5 s | PASS | none |
| 17 | Making-of numbers | n/a | takes used 8, rejected 14; local audio: 139 TTS characters, 4 TTS, 15 SFX, 1 music, 1 ambience generations in the cache (0 made this run, 21 reused); est. 0.00 USD; runtime 67.35 s |

## Edit decision list (as rendered)

| # | Source | Listed in-out (s) | Rendered in-out (s) | Nudge in/out (frames) | Timeline (s) | Length (s) | Cut vs beat (ms) | Content | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S1_ANCHOR | 0.417-3.667 | 0.417-3.667 | 0/0 | 0.000-3.250 | 3.250 | 19.38 | Hook: harpoon anchor slams wet basalt with sparks; whitewater crashes over braced diver | - |
| 2 | S2_BASIN | 0.000-3.667 | 0.000-3.667 | 0/0 | 3.250-6.917 | 3.667 | 6.09 | World reveal: cliff brink pull-out across miles of freshly drained seabed, wrecks, and waterfalls | - |
| 3 | S3_SKIFF | 0.833-4.083 | 0.833-4.083 | 0/0 | 6.917-10.167 | 3.250 | 13.29 | Feature 1 (Traversal): wind-skiff carves salt flat and launches airborne off shipwreck rib | - |
| 4 | S4_VAULT | 0.667-4.333 | 0.667-4.333 | 0/0 | 10.167-13.833 | 3.667 | 12.17 | Feature 2 (Salvage): spoked bronze lock-wheel fires steam bolt; sunken floodgates grind open | - |
| 5 | S5_RETURN | 0.000-3.250 | 0.000-3.250 | 0/0 | 13.833-17.083 | 3.250 | 7.21 | Escalation: skittering wet pebbles tilt up to a hundred-foot tidal bore surging past wrecks | - |
| 6 | S6_LEVIATHAN | 0.500-3.708 | 0.500-3.708 | 0/0 | 17.083-20.292 | 3.208 | 15.08 | Feature 3 (Combat): trench leviathan pincer smash countered by twin harpoon cannon blasts | - |
| 7 | S7_ASCENT | 1.000-3.792 | 1.000-3.792 | 0/0 | 20.292-23.083 | 2.792 | 7.49 | Climax ascent: vertical chain haul up carved sea-spire as whitewater explodes against base | - |
| 8 | S8_BEACON | 0.250-3.917 | 0.250-3.917 | 0/0 | 23.083-26.750 | 3.667 | 17.98 | Climax strike: two-handed brass maul hits colossal bronze tide-bell, blasting storm shockwave | - |
| 9 | END_CARD | 0.000-3.250 | 0.000-3.250 | 0/0 | 26.750-30.000 | 3.250 | - | Black text card: title, tagline, release date, and price | - |

## Events

From `out/cues.md` (2 fps sheets, then 8 and 24 fps strips). Timeline = where the event frame lands in the cut.

| Clip | Event | Source t (s) | Source frame | Timeline (s) | Found |
|---|---|---|---|---|---|
| S1 | anchor_hit | 0.708 | 17 | 0.292 | yes |
| S1 | wave_hit | 2.875 | 69 | 2.458 | yes |
| S2 | coat_gust | 0.250 | 6 | 3.500 | yes |
| S3 | sail_gust | 1.000 | 24 | 7.083 | yes |
| S3 | rib_launch | 2.208 | 53 | 8.292 | yes |
| S4 | bolt_release | 1.000 | 24 | 10.500 | yes |
| S4 | doors_open | 2.833 | 68 | 12.333 | yes |
| S5 | tremor_start | 0.083 | 2 | 13.917 | yes |
| S5 | bore_crest | 1.167 | 28 | 15.000 | yes |
| S6 | claw_slam | 1.125 | 27 | 17.708 | yes |
| S6 | harpoon_1 | 2.208 | 53 | 18.792 | yes |
| S6 | harpoon_2 | 3.250 | 78 | 19.833 | yes |
| S7 | spire_crash | 1.583 | 38 | 20.875 | yes |
| S8 | beacon_strike | 0.875 | 21 | 23.708 | yes |
| END_CARD | start | 0.000 | 0 | 26.750 | yes |
| END_CARD | text_in | 0.250 | 6 | 27.000 | yes |

## Cues

Times in timeline seconds. Picture = the event frame. Target = picture + offset: where the sound must be heard to start. Effects are placed by their attack point (the first 5 ms window within 10 dB of the loudest window of the trimmed take), voices by their gated onset. Heard = where that point sits in the master: the take's first 80 ms are located in the master audio by cross-correlation (shift column) and the shift is added to the target. Error = heard - target, in frames. The frames themselves are verified by eye on sync_check.jpg, cut from the master.

| # | Scene | Sound | Event | Offset | Picture | Target | Heard | Error (frames) | Shift in master (ms) | Variant / file | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | S1_ANCHOR | sfx:anchor_slam | anchor_hit | +0.00 | 0.292 | 0.292 | 0.292 | +0.00 | 0.00 | sfx_anchor_slam_1.mp3 | placed | gain +2 dB |
| 2 | S1_ANCHOR | sfx:hook_wave | wave_hit | +0.00 | 2.458 | 2.458 | 2.458 | +0.00 | 0.00 | sfx_hook_wave_1.mp3 | placed | - |
| 3 | S2_BASIN | sfx:coat_billow | coat_gust | +0.00 | 3.500 | 3.500 | 3.500 | +0.00 | 0.00 | sfx_coat_billow_1.mp3 | placed | gain -1 dB |
| 4 | S2_BASIN | Narrator `Twice a day, the whole sea drains bare.` | coat_gust | +0.35 | 3.500 | 3.850 | 3.850 | +0.00 | 0.00 | vo_4_narrator.mp3 | placed | voice Chuck Fresh; low shelf +2 dB at 150 Hz; compressed 8:1 above -36 dBFS |
| 5 | S3_SKIFF | sfx:sail_snap | sail_gust | +0.00 | 7.083 | 7.083 | 7.083 | +0.00 | 0.00 | sfx_sail_snap_1.mp3 | placed | gain -1 dB |
| 6 | S3_SKIFF | sfx:skiff_launch | rib_launch | +0.00 | 8.292 | 8.292 | 8.292 | +0.00 | 0.00 | sfx_skiff_launch_1.mp3 | placed | - |
| 7 | S4_VAULT | sfx:wheel_bolt | bolt_release | +0.00 | 10.500 | 10.500 | 10.500 | +0.00 | 0.00 | sfx_wheel_bolt_1.mp3 | placed | - |
| 8 | S4_VAULT | Narrator `Forty minutes to take what the deep forgot.` | bolt_release | +0.40 | 10.500 | 10.900 | 10.900 | +0.00 | 0.00 | vo_8_narrator.mp3 | placed | voice Chuck Fresh; low shelf +2 dB at 150 Hz; compressed 8:1 above -36 dBFS |
| 9 | S4_VAULT | sfx:vault_grind | doors_open | +0.00 | 12.333 | 12.333 | 12.333 | +0.00 | 0.00 | sfx_vault_grind_1.mp3 | placed | ducked 5 dB under the voices; gain -2 dB |
| 10 | S5_RETURN | sfx:pebble_tremor | tremor_start | +0.00 | 13.917 | 13.917 | 13.917 | +0.00 | 0.00 | sfx_pebble_tremor_1.mp3 | placed | gain -1 dB |
| 11 | S5_RETURN | Narrator `Before a hundred feet of ocean comes home.` | tremor_start | +0.35 | 13.917 | 14.267 | 14.267 | +0.00 | 0.00 | vo_11_narrator.mp3 | placed | voice Chuck Fresh; low shelf +2 dB at 150 Hz; compressed 8:1 above -36 dBFS |
| 12 | S5_RETURN | sfx:bore_horn | bore_crest | +0.00 | 15.000 | 15.000 | 15.000 | +0.00 | 0.00 | sfx_bore_horn_1.mp3 | placed | ducked 6 dB under the voices; gain -2 dB |
| 13 | S6_LEVIATHAN | sfx:leviathan_slam | claw_slam | +0.00 | 17.708 | 17.708 | 17.708 | +0.00 | 0.00 | sfx_leviathan_slam_1.mp3 | placed | gain +1 dB |
| 14.1 | S6_LEVIATHAN | sfx:harpoon_blast | harpoon_1 | +0.00 | 18.792 | 18.792 | 18.792 | +0.00 | 0.00 | sfx_harpoon_blast_1.mp3 | placed | - |
| 14.2 | S6_LEVIATHAN | sfx:harpoon_blast | harpoon_2 | +0.00 | 19.833 | 19.833 | 19.833 | +0.00 | 0.00 | sfx_harpoon_blast_2.mp3 | placed | - |
| 15 | S7_ASCENT | sfx:spire_crash | spire_crash | +0.00 | 20.875 | 20.875 | 20.875 | +0.00 | 0.00 | sfx_spire_crash_1.mp3 | placed | gain +1 dB |
| 16 | S8_BEACON | sfx:beacon_strike | beacon_strike | +0.00 | 23.708 | 23.708 | 23.708 | +0.00 | 0.00 | sfx_beacon_strike_1.mp3 | placed | decay held to 0.8 dB/s; ducked 3 dB under the voices (40 ms attack, 180 ms release) |
| 17 | S8_BEACON | Narrator `Outrun the sea.` | beacon_strike | +1.50 | 23.708 | 25.208 | 25.208 | +0.00 | 0.00 | vo_17_narrator.mp3 | placed | voice Chuck Fresh; low shelf +2 dB at 150 Hz; compressed 8:1 above -36 dBFS; gain +3 dB (peak 0 dBFS) |
| 18 | END_CARD | sfx:card_lock | text_in | +0.00 | 27.000 | 27.000 | 27.000 | +0.00 | 0.00 | sfx_card_lock_1.mp3 | placed | gain -4 dB |

## Mix and master

- A2 voices peak-normalized to -3 dBFS; A3 effects to -9 dBFS peak (anchor_slam -6, beacon_strike -3).
- A4 music: take 1 of 1 (steadiest: local tempo spread take 1 0.12 BPM); 130.01 BPM detected, downbeat at 0.017 s of the file placed on timeline 0.000 s; -21 dBFS RMS where it plays (gain -3.34 dB), ducked up to 5.00 dB under the voices; hard stop at 23.708 s with a 20 ms fade.
- A5 ambience at -30 dBFS RMS under the whole film (gain 9.80 dB), 1 s fade out at the end.
- Pre-master -16.11 LUFS / -0.08 dBTP; gain 2.11 dB; limiter ceiling -1.5 dBTP at 4x oversampling (latency compensated); loudnorm pass 2 output -14.06 LUFS, -1.46 dBTP, mode linear.
- Decay held: beacon_strike falls no faster than 0.8 dB/s from 0.5 s after its loudest 50 ms (lift at most 36 dB).
- Effects ducked under the voices (keyed like the music): vault_grind 5 dB, 120 ms attack, 450 ms release; bore_horn 6 dB, 120 ms attack, 450 ms release; beacon_strike 3 dB, 40 ms attack, 180 ms release, 14 dB more in 300-3000 Hz (15 ms attack, 60 ms release), 20 ms hold, keyed at -32 dBFS.
- Voice dynamics: narrator compressed 8:1 above -36 dBFS (5 ms attack, 80 ms release), then back to the voice's peak level.
- Voice colour: narrator low shelf +2 dB at 150 Hz, then back to the voice's peak level.
- Export: `out/NEAPSCAR_master.mp4` 1920x1080, 24 fps, H.264 CRF 18 (slow), yuv420p, BT.709, AAC 192k 48 kHz; `out/NEAPSCAR_preview_360p.mp4`.
- Extra loudness target: `out/NEAPSCAR_social.mp4` at -10 LUFS / -1 dBTP, mastered from the same premaster (gain 9.89 dB, limiter ceiling -2.5 dBTP); measured I -10.00 LUFS, TP -1.10 dBTP.
- End card: 3.25 s, font `georgiab.ttf`, "NEAPSCAR" (12.0%), "Forty minutes of dry seabed. Then the ocean comes home." (4.5%, 90%), "DECEMBER 4, 2026  |  $69.99" (3.8%, 75%), fade in 0.25 s.

## Momentary loudness, last 5 s

Master, 400 ms windows, value at the window end. End card from 26.750 s. Reference: beacon_strike M -9.04 LUFS.

| t (s) | M (LUFS) | Below reference (LU) |
|---|---|---|
| 25.00 | -9.89 | 0.85 |
| 25.20 | -10.99 | 1.95 |
| 25.40 | -12.11 | 3.06 |
| 25.60 | -13.79 | 4.75 |
| 25.80 | -14.26 | 5.22 |
| 26.00 | -13.72 | 4.68 |
| 26.20 | -13.37 | 4.32 |
| 26.40 | -13.24 | 4.19 |
| 26.60 | -12.99 | 3.95 |
| 26.80 | -11.69 | 2.64 |
| 27.00 | -11.52 | 2.48 |
| 27.20 | -11.21 | 2.16 |
| 27.40 | -11.26 | 2.21 |
| 27.60 | -12.05 | 3.01 |
| 27.80 | -12.79 | 3.75 |
| 28.00 | -13.07 | 4.03 |
| 28.20 | -13.60 | 4.55 |
| 28.40 | -13.70 | 4.66 |
| 28.60 | -13.23 | 4.19 |
| 28.80 | -12.81 | 3.77 |
| 29.00 | -12.53 | 3.49 |
| 29.20 | -13.07 | 4.02 |
| 29.40 | -13.90 | 4.85 |
| 29.60 | -14.24 | 5.20 |
| 29.80 | -14.80 | 5.76 |

## Decisions and log

- **clip audio**: 8 source clip(s) carry an audio stream (S1_ANCHOR.mp4, S2_BASIN.mp4, S3_SKIFF.mp4, S4_VAULT.mp4, S5_RETURN.mp4, S6_LEVIATHAN.mp4, S7_ASCENT.mp4, S8_BEACON.mp4); it is discarded, as the brief says
- **loudness**: NEAPSCAR_social.mp4: loudnorm's target was biased +0.20 LU so the export measures -10 LUFS on the EBU R128 meter (loudnorm's internal meter reads this short film differently)
