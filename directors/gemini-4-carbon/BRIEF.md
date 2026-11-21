# NEAPSCAR: 30-Second Launch Trailer Production Brief

Audio provider: local
Video provider: handoff
Grade: none
Shot match: off

Discard all audio inside the clips (every source clip's embedded audio stream is muted).

## Goal
A 16:9 launch trailer, 1920x1080, 24 fps, Duration 30.0-30.0 s (720 frames exact), built from eight silent 1080p Veo 3.1 gameplay clips and a native black end card. It opens on a visual and sonic hook in the first 0.5 s (`anchor_hit` at 0.292 s), communicates the entire receding-ocean premise and all three gameplay pillars with the sound off, builds on a steady 130 BPM instrumental score (`dailies-1/music/music_attempt2.wav`), and stops the music dead on the summit bell strike (`beacon_strike` at 23.708 s) before the closing narrator line and pre-order end card.

Aim for roughly: S1 3.25 s, S2 3.67 s, S3 3.25 s, S4 3.67 s, S5 3.25 s, S6 3.21 s, S7 2.79 s, S8 3.67 s.

## Shot rules
Min shot: 2.0 s
Min dead cut: 0.75 s
Hard cuts only. No zooms, no speed changes, no freezes, no reversed footage. The first frame of the film is at most 0.5 s before anchor_hit.

## EDL
| Order | Source | In | Out | Content | Dailies File | Clip Audio |
|---|---|---|---|---|---|---|
| 1 | S1_ANCHOR | 0.417 | 3.667 | Hook: harpoon anchor slams wet basalt with sparks; whitewater crashes over braced diver | `dailies-1/01_S1_ANCHOR_quality_t1.mp4` | Muted |
| 2 | S2_BASIN | 0.000 | 3.667 | World reveal: cliff brink pull-out across miles of freshly drained seabed, wrecks, and waterfalls | `dailies-1/02_S2_BASIN_fast_t1.mp4` | Muted |
| 3 | S3_SKIFF | 0.833 | 4.083 | Feature 1 (Traversal): wind-skiff carves salt flat and launches airborne off shipwreck rib | `dailies-1/03_S3_SKIFF_fast_t1.mp4` | Muted |
| 4 | S4_VAULT | 0.667 | 4.333 | Feature 2 (Salvage): spoked bronze lock-wheel fires steam bolt; sunken floodgates grind open | `dailies-2/02_S4_VAULT_fast_t2.mp4` | Muted |
| 5 | S5_RETURN | 0.000 | 3.250 | Escalation: skittering wet pebbles tilt up to a hundred-foot tidal bore surging past wrecks | `dailies-2/03_S5_RETURN_fast_t2.mp4` | Muted |
| 6 | S6_LEVIATHAN | 0.500 | 3.708 | Feature 3 (Combat): trench leviathan pincer smash countered by twin harpoon cannon blasts | `dailies-1/06_S6_LEVIATHAN_fast_t1.mp4` | Muted |
| 7 | S7_ASCENT | 1.000 | 3.792 | Climax ascent: vertical chain haul up carved sea-spire as whitewater explodes against base | `dailies-1/07_S7_ASCENT_fast_t1.mp4` | Muted |
| 8 | S8_BEACON | 0.250 | 3.917 | Climax strike: two-handed brass maul hits colossal bronze tide-bell, blasting storm shockwave | `dailies-2/01_S8_BEACON_quality_t1.mp4` | Muted |
| 9 | END_CARD | 0.000 | 3.250 | Black text card: title, tagline, release date, and price | Generated in edit (`drawtext`) | Muted |

Events and verified 24 fps frame pins live in `out/cues.md`. Every source clip plays at 1.0x original speed with its own audio muted.

## Event detection
| Scene | Event name | What to look for |
|---|---|---|
| S1_ANCHOR | anchor_hit | first frame orange flint sparks burst under the harpoon anchor tip |
| S1_ANCHOR | wave_hit | frame the white ocean wave wall surges up over the rock ledge behind the diver |
| S2_BASIN | coat_gust | frame the oiled storm-coat flares sharply left in the cliff updraft |
| S3_SKIFF | sail_gust | frame the wind-skiff heels forward approaching the shipwreck rib |
| S3_SKIFF | rib_launch | first frame the skiff runners clear the barnacled shipwreck rib into open air |
| S4_VAULT | bolt_release | first frame bright spark and pressurized steam burst inside the spoked bronze wheel |
| S4_VAULT | doors_open | frame the double bronze floodgates part wide to spill golden vault light |
| S5_RETURN | tremor_start | skittering wet pebbles in the shallow puddle at the start of the upward tilt |
| S5_RETURN | bore_crest | frame the upward tilt locks onto the hundred-foot turquoise tidal bore |
| S6_LEVIATHAN | claw_slam | first frame white water erupts off wet rock under the leviathan's smashing pincer |
| S6_LEVIATHAN | harpoon_1, harpoon_2 | first frame of each orange muzzle/spark burst from the tethered harpoon cannon |
| S7_ASCENT | spire_crash | frame the churning whitewater wall smashes into the stone base of the spire |
| S8_BEACON | beacon_strike | exact golden contact flash as the brass maul strikes the colossal bronze tide-bell |

## ElevenLabs
Narrator: `eleven_multilingual_v2`, stability 0.50, similarity 0.80, style 0.00, speaker boost on.
Narrator voice by name, first that exists in the account: `Chuck Fresh`.
Forced alignment off.

Local voice mapping (`audio/local/`, selected from 4 auditioned voices across Round 1 and Round 2):
- `vo_4_narrator.mp3` <- `dailies-2/audio/vo_C_line1.mp3` (`Chuck Fresh - Movie Trailer Narrator`)
- `vo_8_narrator.mp3` <- `dailies-2/audio/vo_C_line2.mp3` (`Chuck Fresh - Movie Trailer Narrator`)
- `vo_11_narrator.mp3` <- `dailies-2/audio/vo_C_line3.mp3` (`Chuck Fresh - Movie Trailer Narrator`)
- `vo_17_narrator.mp3` <- `dailies-2/audio/vo_C_line4.mp3` (`Chuck Fresh - Movie Trailer Narrator`)

## SFX
Backed by selected Round 1 and Round 2 ElevenLabs dailies in `audio/local/sfx_<name>_<variant>.mp3`.

| Name | Prompt | Seconds | Variants | Trim | Dailies Source |
|---|---|---|---|---|---|
| anchor_slam | `Close heavy forged iron anchor spike smashing down onto solid wet basalt rock, metallic anvil thud and flint spark` | 2.0 | 1 | transient | `dailies-2/audio/anchor_slam_4.mp3` |
| hook_wave | `Heavy ocean wave smashing violently onto close wet black coastal rock, water impact and spray hiss` | 3.0 | 1 | transient | `dailies-2/audio/hook_wave_2.mp3` |
| coat_billow | `Heavy wet oiled-canvas trench coat snapping and billowing sharply in a sea-cliff wind gust` | 2.0 | 1 | transient | `dailies-2/audio/coat_billow_2.mp3` |
| sail_snap | `Heavy oiled canvas sail snapping taut in a strong sea gust with crisp brass rigging clink` | 2.0 | 1 | transient | `dailies-1/audio/sail_snap_1.mp3` |
| skiff_launch | `Heavy wooden-and-brass hydro-skiff runners scraping off a barnacled timber ramp into airborne wind whoosh` | 3.0 | 1 | transient | `dailies-2/audio/skiff_launch_1.mp3` |
| wheel_bolt | `Heavy spoked bronze vault wheel wrenched hard until a massive iron locking bolt slams open` | 2.0 | 1 | transient | `dailies-2/audio/wheel_bolt_1.mp3` |
| vault_grind | `Monumental ancient barnacled bronze and stone floodgate doors grinding open with heavy gear teeth meshing` | 4.0 | 1 | transient | `dailies-1/audio/vault_grind_1.mp3` |
| pebble_tremor | `Low seismic ground rumble rattling wet pebbles and loose shells across dark stone` | 3.0 | 1 | onset | `dailies-1/audio/pebble_tremor_1.mp3` |
| bore_horn | `Distant colossal mechanical brass cliff-bastion warning horn echoing across an open sea canyon` | 4.0 | 1 | onset | `dailies-1/audio/bore_horn_2.mp3` |
| leviathan_slam | `Colossal armored sea creature claw smashing down onto wet rock and shallow water` | 3.0 | 1 | transient | `dailies-1/audio/leviathan_slam_2.mp3` |
| harpoon_blast | `Heavy brass black-powder harpoon cannon firing with carapace impact spark and steel cable whip` | 2.0 | 2 | transient | `dailies-2/audio/harpoon_blast_1.mp3`, `harpoon_blast_2.mp3` |
| spire_crash | `Massive wall of ocean whitewater crashing violently against the base of a stone sea-cliff` | 4.0 | 1 | transient | `dailies-1/audio/spire_crash_2.mp3` |
| beacon_strike | `Monumental ancient bronze tide-bell struck hard, chest-punching gong transient, shockwave boom, long bronze decay` | 16.0 | 1 | transient | `dailies-1/audio/beacon_strike_4.mp3` |
| card_lock | `Single precise brass depth-gauge click followed by a deep resonant submarine bell ping` | 2.0 | 1 | transient | `dailies-1/audio/card_lock_1.mp3` |

## Audio map (times are verified 24 fps event frames from out/cues.md)
| Scene | Track | Voice | Text | At event | Offset | Gain |
|---|---|---|---|---|---|---|
| S1_ANCHOR | A3 | sfx:anchor_slam | | anchor_hit | 0.00 | +2 |
| S1_ANCHOR | A3 | sfx:hook_wave | | wave_hit | 0.00 | |
| S2_BASIN | A3 | sfx:coat_billow | | coat_gust | 0.00 | -1 |
| S2_BASIN | A2 | Narrator | `Twice a day, the whole sea drains bare.` | coat_gust | 0.35 | |
| S3_SKIFF | A3 | sfx:sail_snap | | sail_gust | 0.00 | -1 |
| S3_SKIFF | A3 | sfx:skiff_launch | | rib_launch | 0.00 | |
| S4_VAULT | A3 | sfx:wheel_bolt | | bolt_release | 0.00 | |
| S4_VAULT | A2 | Narrator | `Forty minutes to take what the deep forgot.` | bolt_release | 0.40 | |
| S4_VAULT | A3 | sfx:vault_grind | | doors_open | 0.00 | -2 |
| S5_RETURN | A3 | sfx:pebble_tremor | | tremor_start | 0.00 | -1 |
| S5_RETURN | A2 | Narrator | `Before a hundred feet of ocean comes home.` | tremor_start | 0.35 | |
| S5_RETURN | A3 | sfx:bore_horn | | bore_crest | 0.00 | -2 |
| S6_LEVIATHAN | A3 | sfx:leviathan_slam | | claw_slam | 0.00 | +1 |
| S6_LEVIATHAN | A3 | sfx:harpoon_blast | | harpoon_1, harpoon_2 | 0.00 | |
| S7_ASCENT | A3 | sfx:spire_crash | | spire_crash | 0.00 | +1 |
| S8_BEACON | A3 | sfx:beacon_strike | | beacon_strike | 0.00 | |
| S8_BEACON | A2 | Narrator | `Outrun the sea.` | beacon_strike | 1.50 | +3 |
| END_CARD | A3 | sfx:card_lock | | text_in | 0.00 | -4 |

Rules:
- SFX never move; they follow the picture.
- The narrator never covers the beacon_strike's first 1.5 s. If a line would run past its shot, start it earlier, else extend the shot hold if frames are left, else finish over the end card.

## Music and ambience
- Music (A4): `Propulsive clockwork-rigging pulse, war drums, spiccato strings, and dark brass swells, 130 BPM, instrumental only, 30 seconds`. One take (`audio/local/music_take1.wav`, selected from `dailies-1/music/music_attempt2.wav`).
- Bed placement: beat 1 on timeline 0.00. Cuts may move at most ±3 frames toward the beat grid; SFX never move.
- Hard stop: the music ends on the `beacon_strike` event (20 ms fade).
- Ambience (A5): `Wide open-air drained ocean canyon wind over wet basalt rock and distant surf`, 30 seconds (`audio/local/ambience.mp3`, selected from `dailies-1/audio/ambience_a.mp3`), under the whole film at -30 dBFS RMS, 1.0 s fade out over the end card.

## Mix levels
A2 narrator -3 dBFS peak. A3 SFX -9 dBFS peak (beacon_strike -3 dBFS peak, anchor_slam -6 dBFS peak). A4 music -21 dBFS RMS, ducked 5 dB under the narrator. A5 ambience -30 dBFS RMS.

Narrator low shelf +2 dB at 150 Hz.
Narrator compressed 8:1 above -36 dBFS (5 ms attack, 80 ms release).

beacon_strike decay held to 0.8 dB/s from 0.5 s after its attack (lift at most 36 dB).
beacon_strike ducked 3 dB under the narrator (40 ms attack, 180 ms release, 20 ms hold, key -32 dBFS), 14 dB more in the speech band 300-3000 Hz (15 ms attack, 60 ms release).
vault_grind ducked 5 dB under the narrator.
bore_horn ducked 6 dB under the narrator.

## End card
3.25 s black, after S8_BEACON. Centered lines in bold serif (`georgiab.ttf`, else DejaVu Serif Bold):
- `NEAPSCAR` (12.0% of the frame height)
- `Forty minutes of dry seabed. Then the ocean comes home.` (4.5% of the frame height, 90% white)
- `DECEMBER 4, 2026  |  $69.99` (3.8% of the frame height, 75% white)
Text fades in over 0.25 s. No readable text inside generated footage anywhere in the trailer.

## Export
`out/NEAPSCAR_master.mp4`: 1920x1080, 24 fps, H.264 CRF 18, x264 preset slow, yuv420p, AAC 192k 48 kHz. Two-pass loudnorm I=-14 TP=-1 LRA=11.
Also `out/NEAPSCAR_preview_360p.mp4`.
Social delivery: `out/NEAPSCAR_social.mp4`: two-pass loudnorm I=-10 TP=-1 LRA=11.

## QA
1. Duration 30.0-30.0 s.
2. -14 LUFS ±0.5, true peak ≤ -1 dBTP, no clipping.
3. Every event and cue placed or logged.
4. Every sound within ±1 frame of its event frame, measured on the master.
5. Music silent after `beacon_strike`.
6. beacon_strike is the loudest moment (momentary loudness, 400 ms).
7. The narrator reads over the beacon_strike: speech band 300-3000 Hz of the line at least 6 dB above the strike in the line's window.
8. The last 3 s before the end card stay within 8 LU of the beacon_strike (momentary loudness).
9. First sound (anchor_hit) within the first 0.5 s.
10. First frame not black; last frame is the end card.
11. No audio from the source clips in the master.
