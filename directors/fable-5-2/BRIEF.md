# MOONDRAWN: 30 s launch trailer, final cut

The sea leaves, she goes in, the sea comes back. Thirteen shots in 25 s, then one 5 s text card. Every frame and every sound below is pinned; nothing is left to the edit.

Video provider: handoff
Audio provider: local
Grade: none
Shot match: off

## Goal
A 16:9 film, 30-30 s, 1920x1080, 24 fps: exactly 720 frames, 600 of footage and 120 of card. It must read with the sound off: the sea runs out in the first three seconds, the wall of water comes back at 17 s, the card answers it.

## Shot rules
Min shot: 1.0 s
Min dead cut: 0.75 s
Hard cuts only. Clips play at original speed; a trim is the only edit. The first frame of the film is at most 0.5 s before drain.

## Clip audio
Muted for every one of the 13 clips. No source clip audio is used anywhere; every sound in the film comes from the audio map below.

## Clips
| Clip file | Dailies file | Model | Audio |
|---|---|---|---|
| `clips/S02_PIER.mp4` | `dailies-2/78_S02_PIER_r2_fast_t2.mp4` | Veo 3.1 Fast | muted |
| `clips/S03_LAUNCH.mp4` | `dailies-2/83_S03_LAUNCH_r2_fast_t1.mp4` | Veo 3.1 Fast | muted |
| `clips/S04_VISTA.mp4` | `dailies-1/05_S04_VISTA_fast.mp4` | Veo 3.1 Fast | muted |
| `clips/S05_CITY.mp4` | `dailies-1/06_S05_CITY_fast.mp4` | Veo 3.1 Fast | muted |
| `clips/S06_RELIC.mp4` | `dailies-1/12_S06_RELIC_fast.mp4` | Veo 3.1 Fast | muted |
| `clips/S07_GIANT.mp4` | `dailies-1/11_S07_GIANT_fast.mp4` | Veo 3.1 Fast | muted |
| `clips/S08_EYE.mp4` | `dailies-1/23_S08_EYE_lite.mp4` | Veo 3.1 Lite | muted |
| `clips/S09_BOOTS.mp4` | `dailies-2/88_S09_BOOTS_r2_lite_t1.mp4` | Veo 3.1 Lite | muted |
| `clips/S14_RETURN.mp4` | `dailies-2/79_S14_RETURN_r2_fast_t1.mp4` | Veo 3.1 Fast | muted |
| `clips/S10_WALL.mp4` | `dailies-1/01_S10_WALL_fast.mp4` | Veo 3.1 Fast | muted |
| `clips/S11_CHASE.mp4` | `dailies-1/09_S11_CHASE_fast.mp4` | Veo 3.1 Fast | muted |
| `clips/S12_RISE.mp4` | `dailies-2/89_S12_RISE_r2_lite_t1.mp4` | Veo 3.1 Lite | muted |
| `clips/S13_LEAP.mp4` | `dailies-2/80_S13_LEAP_r2_fast_t1.mp4` | Veo 3.1 Fast | muted |

## EDL
| Order | Source | In | Out | Content |
|---|---|---|---|---|
| 1 | S02_PIER | 0.000 | 3.500 | 0.000-3.500: HOOK: she watches the whole sea run out; boats drop onto the seabed |
| 2 | S03_LAUNCH | 0.000 | 2.000 | 3.500-5.500: she goes after it: sand-yacht away from the stilt town, dry seabed ahead |
| 3 | S04_VISTA | 1.000 | 3.500 | 5.500-8.000: the open seabed: racing between colossal wrecks |
| 4 | S05_CITY | 0.250 | 2.250 | 8.000-10.000: a drowned city, still pouring water |
| 5 | S06_RELIC | 2.000 | 4.000 | 10.000-12.000: the reward: she lifts a glowing orb from a chest |
| 6 | S07_GIANT | 0.500 | 2.500 | 12.000-14.000: something asleep: she walks under a stranded giant |
| 7 | S08_EYE | 0.375 | 1.875 | 14.000-15.500: it wakes: the eye opens on her |
| 8 | S09_BOOTS | 1.250 | 2.750 | 15.500-17.000: the turn: water comes back around her boots |
| 9 | S14_RETURN | 1.500 | 3.500 | 17.000-19.000: the price: the sea as a wall, she backs away |
| 10 | S10_WALL | 2.500 | 3.500 | 19.000-20.000: the chase: the wall smashes the wrecks behind her |
| 11 | S11_CHASE | 0.500 | 1.500 | 20.000-21.000: close on her at the tiller, the wave gaining |
| 12 | S12_RISE | 2.000 | 4.000 | 21.000-23.000: the giant swims out of the wave beside her |
| 13 | S13_LEAP | 0.000 | 2.000 | 23.000-25.000: she jumps the crest, against the moon |
| 14 | END_CARD | 0.00 | 5.00 | 25.000-30.000: title, tagline, release date, price |

## Event detection
| Scene | Event name | What to look for |
|---|---|---|
| S02_PIER | drain | first frame of the film: the sea already pulling away from the pier |
| S02_PIER | boats_drop | first frame the two near boats sit on bare seabed |
| S06_RELIC | orb_lift | the orb leaves the chest |
| S08_EYE | eye_open | the lid parts: one frame before the first sliver of the eye |
| S09_BOOTS | water_in | the foam sheet sweeps past her heels |
| S10_WALL | wreck_hit | debris flying off the wreck behind her, two frames after the cut |
| S12_RISE | breach | head and fin of the giant clear of the wave face |
| S13_LEAP | riser_peak | no picture event: timing mark so the riser ends on the cut to the card |
| END_CARD | stop | no picture event: music stop, two frames before its bar 14 |
| END_CARD | boom | no picture event: bar 14 of the music, 2.000 s into the card |

## Voices
Narrator: `eleven_multilingual_v2`, stability 0.5, similarity 0.8, style 0.0, speaker boost on, speed 1.0.
Narrator voice by name, first that exists in the account: `Don - Movie Trailer Narrator`.
Forced alignment off.
The six lines are the delivered files of orders 106 to 111; nothing is generated.

## SFX
| Name | Prompt | Seconds | Variants | Trim |
|---|---|---|---|---|
| sea_drain | `A whole sea draining away in seconds: a huge mass of water rushing out and receding fast into the distance, deep hollow suction roar that fades to quiet dripping. No music.` | 4 | 1 | onset |
| boats_drop | `Several heavy wooden boats dropping onto wet rocks and sand one after another as water drains from under them: deep wooden thuds, hull creaks, chains rattling.` | 3 | 1 | transient |
| sail_snap | `Large canvas sail filling with a sudden gust: one loud sharp flap and crack of cloth, bright and close, then rope creak.` | 2 | 1 | transient |
| skiff_run | `Wooden cart wheels racing over wet sand at high speed, steady hiss of spray, wind humming in a sail and rigging, wood rattle. Continuous.` | 4 | 2 | onset |
| ruin_falls | `Hundreds of small waterfalls pouring from stone ruins into shallow pools, echoing in a huge stone hall, steady splashing and dripping.` | 4 | 1 | onset |
| relic_shimmer | `Soft magical shimmer swelling as a glowing glass orb is lifted, airy sparkle with a warm glassy ring, gentle, no melody.` | 2 | 1 | onset |
| giant_breath | `Huge whale breathing out through its blowhole, close: loud airy rush of breath and spray, hoarse and breathy, then dripping.` | 3 | 1 | onset |
| eye_open | `Giant wet eyelid peeling open, very close: slimy squelch and stretch of thick skin, then a short low animal grunt. Mid-range, clearly audible on small speakers.` | 2 | 1 | transient |
| eye_sub | `A giant creature's eye snapping open: quick wet fleshy blink followed by a deep ominous bass pulse. Close, short.` | 2 | 1 | onset |
| water_rush | `Thin sheet of sea water rushing in fast over wet sand and flooding around boots, sharp hiss, foam fizz and trickle. Close.` | 2 | 1 | onset |
| wall_long | `Enormous breaking wave chasing closer for ten seconds: continuous thunderous roar of whitewater that gets steadily louder and brighter right to the end, hissing foam on top of a deep rumble. No pause, no fade-out.` | 10 | 1 | onset |
| wall_roar | `Colossal tidal wave charging closer: continuous thunderous roar of whitewater growing steadily louder, deep rumble with crashing and splintering wood detail.` | 5 | 1 | onset |
| wreck_crash | `Huge wave smashing through old wooden ships: timber splintering and cracking, masts snapping, heavy crashing water.` | 3 | 1 | onset |
| giant_call | `Gigantic sea creature bellowing: one long powerful whale-like horn call, deep and majestic, echoing across open water.` | 4 | 1 | onset |
| whale_breach | `Enormous whale bursting out of a wave: massive rush and surge of water, heavy splash, spray raining down.` | 3 | 1 | transient |
| leap_whoosh | `Heavy fast whoosh of a boat launching off a wave into the air, burst of spray at the start, then airy wind. Short.` | 2 | 1 | transient |
| riser | `Reverse cymbal swell: starts from silence and builds smoothly for three seconds to a loud bright peak, then cuts instantly to silence. No melody.` | 3 | 1 | none |
| title_crack | `Explosive crack of a giant wave smashing a wooden pier: sharp bright splintering timber and a hard slap of water, loud in the middle and high frequencies, almost no deep bass. One hit, then spray falling.` | 3 | 1 | transient |
| title_slam | `Single massive cinematic trailer impact: deep boom with a hard cracking mid-range hit, like a giant wave slamming a sea wall, then a long dark reverb tail. One hit only, no melody.` | 5 | 1 | transient |
| title_boom | `Massive cinematic trailer hit: thunderclap and huge metal clang struck together, bright, punchy and clearly audible on small speakers, followed by a long shimmering reverb tail that rings for five seconds. One hit only, no melody.` | 6 | 1 | onset |

## Audio map
| Scene | Track | Voice | Text | At event | Offset | Gain |
|---|---|---|---|---|---|---|
| S02_PIER | A3 | sfx:sea_drain |  | drain | 0.00 |  |
| S02_PIER | A2 | Narrator | `Once a day, the moon takes the sea away.` | drain | 0.15 |  |
| S02_PIER | A3 | sfx:boats_drop |  | boats_drop | 0.00 |  |
| S03_LAUNCH | A3 | sfx:sail_snap |  | clip start | 0.00 |  |
| S03_LAUNCH | A3 | sfx:skiff_run |  | clip start | 0.50 |  |
| S03_LAUNCH | A2 | Narrator | `You have one hour.` | clip start | 0.30 |  |
| S04_VISTA | A3 | sfx:skiff_run |  | clip start | 0.40 |  |
| S04_VISTA | A2 | Narrator | `Everything it ever swallowed is waiting down there.` | clip start | 0.40 |  |
| S05_CITY | A3 | sfx:ruin_falls |  | clip start | 0.00 |  |
| S06_RELIC | A3 | sfx:relic_shimmer |  | orb_lift | 0.00 |  |
| S07_GIANT | A3 | sfx:giant_breath |  | clip start | 0.50 |  |
| S08_EYE | A3 | sfx:eye_open |  | eye_open | 0.00 |  |
| S08_EYE | A3 | sfx:eye_sub |  | eye_open | 0.00 |  |
| S08_EYE | A2 | Narrator | `Then it comes back.` | eye_open | 0.45 | +3 |
| S09_BOOTS | A3 | sfx:water_rush |  | water_in | 0.00 |  |
| S14_RETURN | A3 | sfx:wall_long |  | clip start | 0.00 |  |
| S14_RETURN | A3 | sfx:wall_roar |  | clip start | 0.00 |  |
| S10_WALL | A3 | sfx:wreck_crash |  | wreck_hit | 0.00 |  |
| S11_CHASE | A3 | sfx:skiff_run |  | clip start | 0.50 |  |
| S12_RISE | A3 | sfx:giant_call |  | clip start | 0.00 |  |
| S12_RISE | A3 | sfx:whale_breach |  | breach | 0.00 |  |
| S13_LEAP | A3 | sfx:leap_whoosh |  | clip start | 0.00 |  |
| S13_LEAP | A3 | sfx:riser |  | riser_peak | 0.00 |  |
| END_CARD | A3 | sfx:title_crack |  | start | 0.00 |  |
| END_CARD | A3 | sfx:title_slam |  | start | 0.00 |  |
| END_CARD | A2 | Narrator | `Moondrawn.` | start | 0.85 |  |
| END_CARD | A2 | Narrator | `Be back before the sea is.` | stop | 0.40 |  |
| END_CARD | A3 | sfx:title_boom |  | boom | 0.00 |  |

## Music and ambience
- Music (A4): `Instrumental trailer music with a sea-shanty heartbeat, 120 BPM, 4/4, straight rhythm, foot stomps and hand claps, plucked strings and a whistling flute tune, war drums and low brass from bar 9, a final crash on bar 13, instrumental only, 59 seconds`. One take.
- Bed placement: beat 1 on timeline 1.00. Cuts may move at most ±0 frames toward the beat grid; SFX never move.
- Hard stop: the music ends on the `stop` event (20 ms fade).
- Ambience (A5): `Open tidal flats at low tide: steady sea wind, distant gulls, faint water trickling over wet sand. Calm, continuous, seamless loop. No music, no voices.`, 30 seconds, under the whole film at -36 dBFS RMS, 1.0 s fade out over the end card.

## Mix levels
A2 narrator -2 dBFS peak. A3 SFX -10 dBFS peak (sea_drain -6 dBFS peak, boats_drop -15 dBFS peak, sail_snap -8 dBFS peak, skiff_run -13 dBFS peak, ruin_falls -16 dBFS peak, relic_shimmer -13 dBFS peak, giant_breath -9 dBFS peak, eye_open -7 dBFS peak, eye_sub -14 dBFS peak, water_rush -12 dBFS peak, wall_long -7 dBFS peak, wall_roar -6 dBFS peak, wreck_crash -8 dBFS peak, giant_call -6 dBFS peak, whale_breach -8 dBFS peak, leap_whoosh -8 dBFS peak, riser -10 dBFS peak, title_crack -3 dBFS peak, title_slam -6 dBFS peak, title_boom -5 dBFS peak). A4 music -20 dBFS RMS, ducked 6 dB under the narrator. A5 ambience -36 dBFS RMS.
Narrator compressed 6:1 above -30 dBFS (5 ms attack, 100 ms release).
sea_drain ducked 8 dB under the narrator (80 ms attack, 300 ms release).
boats_drop ducked 8 dB under the narrator (80 ms attack, 300 ms release).
eye_open ducked 8 dB under the narrator (80 ms attack, 300 ms release).
eye_sub ducked 8 dB under the narrator (80 ms attack, 300 ms release).
water_rush ducked 8 dB under the narrator (80 ms attack, 300 ms release).
wall_long ducked 8 dB under the narrator (80 ms attack, 300 ms release).
wall_roar ducked 8 dB under the narrator (80 ms attack, 300 ms release).
title_crack ducked 10 dB under the narrator (80 ms attack, 300 ms release).
title_slam ducked 10 dB under the narrator (80 ms attack, 300 ms release).
title_boom ducked 10 dB under the narrator (80 ms attack, 300 ms release).

## End card
5.0 s black. Font `C:/Windows/Fonts/bahnschrift.ttf`. Four centered lines: `MOONDRAWN` (14% of the frame height), `Be back before the sea is.` (6% of the frame height, 85% white), `February 26, 2027` (5% of the frame height), `Pre-order now  $59.99` (5% of the frame height, 85% white). Text fades in over 0.25 s.

## Audio files
| Local file | Dailies file | Used for |
|---|---|---|
| `audio/local/music_take1.wav` | `dailies-2/music/music_M4.wav` | the music track (M4, order 126) |
| `audio/local/ambience.mp3` | `dailies-1/audio/ambience.mp3` | bed under the whole film |
| `audio/local/sfx_sea_drain_1.mp3` | `dailies-1/audio/sfx_sea_drain_2.mp3` | effect `sea_drain` |
| `audio/local/sfx_boats_drop_1.mp3` | `dailies-2/audio/sfx_boats_drop_1.mp3` | effect `boats_drop` |
| `audio/local/sfx_sail_snap_1.mp3` | `dailies-2/audio/sfx_sail_snap_3.mp3` | effect `sail_snap` |
| `audio/local/sfx_skiff_run_1.mp3` | `dailies-1/audio/sfx_skiff_run_2.mp3` | effect `skiff_run`, variant 1 |
| `audio/local/sfx_skiff_run_2.mp3` | `dailies-1/audio/sfx_skiff_run_1.mp3` | effect `skiff_run`, variant 2 |
| `audio/local/sfx_ruin_falls_1.mp3` | `dailies-1/audio/sfx_ruin_falls_1.mp3` | effect `ruin_falls` |
| `audio/local/sfx_relic_shimmer_1.mp3` | `dailies-1/audio/sfx_relic_shimmer_2.mp3` | effect `relic_shimmer` |
| `audio/local/sfx_giant_breath_1.mp3` | `dailies-2/audio/sfx_giant_breath_2.mp3` | effect `giant_breath` |
| `audio/local/sfx_eye_open_1.mp3` | `dailies-2/audio/sfx_eye_open_4.mp3` | effect `eye_open` |
| `audio/local/sfx_eye_sub_1.mp3` | `dailies-1/audio/sfx_eye_open_1.mp3` | effect `eye_sub` |
| `audio/local/sfx_water_rush_1.mp3` | `dailies-1/audio/sfx_water_rush_1.mp3` | effect `water_rush` |
| `audio/local/sfx_wall_long_1.mp3` | `dailies-2/audio/sfx_wall_long_2.mp3` | effect `wall_long` |
| `audio/local/sfx_wall_roar_1.mp3` | `dailies-1/audio/sfx_wall_roar_2.mp3` | effect `wall_roar` |
| `audio/local/sfx_wreck_crash_1.mp3` | `dailies-2/audio/sfx_wreck_crash_1.mp3` | effect `wreck_crash` |
| `audio/local/sfx_giant_call_1.mp3` | `dailies-1/audio/sfx_giant_call_2.mp3` | effect `giant_call` |
| `audio/local/sfx_whale_breach_1.mp3` | `dailies-2/audio/sfx_whale_breach_1.mp3` | effect `whale_breach` |
| `audio/local/sfx_leap_whoosh_1.mp3` | `dailies-1/audio/sfx_leap_whoosh_1.mp3` | effect `leap_whoosh` |
| `audio/local/sfx_riser_1.mp3` | `dailies-2/audio/sfx_riser_4.mp3` | effect `riser` |
| `audio/local/sfx_title_crack_1.mp3` | `dailies-2/audio/sfx_title_crack_2.mp3` | effect `title_crack` |
| `audio/local/sfx_title_slam_1.mp3` | `dailies-1/audio/sfx_title_slam_2.mp3` | effect `title_slam` |
| `audio/local/sfx_title_boom_1.mp3` | `dailies-2/audio/sfx_title_boom_2.mp3` | effect `title_boom` |
| `audio/local/vo_2_narrator.mp3` | `dailies-2/audio/vo_D_N1.mp3` | audio map row 2: "Once a day, the moon takes the sea away." |
| `audio/local/vo_6_narrator.mp3` | `dailies-2/audio/vo_D_N2.mp3` | audio map row 6: "You have one hour." |
| `audio/local/vo_8_narrator.mp3` | `dailies-2/audio/vo_D_N3.mp3` | audio map row 8: "Everything it ever swallowed is waiting down there." |
| `audio/local/vo_14_narrator.mp3` | `dailies-2/audio/vo_D_N4.mp3` | audio map row 14: "Then it comes back." |
| `audio/local/vo_26_narrator.mp3` | `dailies-2/audio/vo_D_N5.mp3` | audio map row 26: "Moondrawn." |
| `audio/local/vo_27_narrator.mp3` | `dailies-2/audio/vo_D_N6.mp3` | audio map row 27: "Be back before the sea is." |

## Export
`out/MOONDRAWN_master.mp4`: 1920x1080, 24 fps, H.264 CRF 16, x264 preset slow, AAC 192k 48 kHz. Two-pass loudnorm I=-14 TP=-1 LRA=11.
Also `out/MOONDRAWN_preview_360p.mp4`.

## QA
1. Duration 30-30 s.
2. -14 LUFS ±0.5, true peak ≤ -1 dBTP, no clipping.
3. Every event and cue placed or logged.
4. Every SFX onset within ±1 frame of its event frame, measured on the master.
5. Music silent after `stop`.
6. First sound (drain) within the first 0.5 s.
7. First frame not black; last frame is the end card.
8. No audio from the source clips in the master.
9. Hard cuts only, no retiming; every cut on the music grid.
