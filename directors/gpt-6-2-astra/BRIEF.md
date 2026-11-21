# Morrow Under Tow

Video provider: handoff
Audio provider: local
Grade: none
Shot match: off

## Goal

1920x1080, 16:9, 24 fps, exactly 720 frames. Open on a tug with the sun on its line. Show what the player does at the wheel, where that takes the light, and who was waiting for it.

## Shot rules

Hard cuts only. Min shot: 2.0 s. Play every source at original speed. Discard all source clip audio. All lettering belongs to the end card. In and Out are local source seconds, first frame included and Out excluded. Master frame numbers start at zero.

## EDL

| Order | Source | In | Out | Content | Master frames [in, out) | Clip audio | Original file |
|---|---|---|---|---|---|---|---|
| 1 | S1_TOW | 0.000000 | 2.791667 | Start with the line already stretched across the bright disk. Give the eye time to follow it down to the tug. | 0–67 | Mute | dailies-1/01_S1_TOW_quality_t1.mp4 |
| 2 | S2_HELM | 0.500000 | 3.333333 | Cut inside. The skipper turns the wooden wheel. The trees and the blue bridge share the window. | 67–135 | Mute | dailies-2/32_S2_HELM_fast_t2.mp4 |
| 3 | S3_FORK | 2.166667 | 5.458333 | See the result from above. The white wake curls past the orchard and the bow points into the arch. | 135–214 | Mute | dailies-2/28_S2_STARBOARD_fast_t1.mp4 |
| 4 | S4_WINCH | 0.208333 | 2.541667 | Her plum sleeve crosses the black drum. Stay for the downstroke and the return. | 214–270 | Mute | dailies-1/03_S3_WINCH_fast_t1.mp4 |
| 5 | S5_ARCH | 0.000000 | 3.750000 | Look aft. The brick ceiling glows above a single sun. Blue masonry recedes around both sides of the deck. | 270–360 | Mute | dailies-2/30_S4_CLEARANCE_fast_t2.mp4 |
| 6 | S6_THAW | 0.333333 | 5.458333 | An ice plate slips off a harbour step. Hold until gold water spills down the exposed treads. | 360–483 | Mute | dailies-2/31_S5_LOWEST_STEP_fast_t1.mp4 |
| 7 | S7_BREAD | 0.875000 | 5.583333 | From the sill, the baker offers warm bread. The skipper takes its weight. Let the floury hand withdraw. | 483–596 | Mute | dailies-1/06_S6_HEEL_fast_t2.mp4 |
| 8 | END_CARD | 0.000000 | 5.166667 | Black card. Give the release and pre-order information the same screen time as the name. | 596–720 | Card | Built in the edit |

## Voices

Voices by name: `Baker`
Forced alignment off.

Use the two delivered readings for the sister. She speaks offscreen across the wheelhouse shot, then at arm's length over the bakery sill.

## SFX

Each name resolves to one delivered recording. The Prompt column identifies the sound in that recording.

| Name | Prompt | Seconds | Variants | Trim | Original file |
|---|---|---|---|---|---|
| rope_catch | Loaded towrope against the post | 1 | 1 | transient | dailies-1/audio/rope_catch.mp3 |
| wheel_grip | Cuff and hand on the wooden rim | 2 | 1 | transient | dailies-2/audio/wheel_grip.mp3 |
| hull_wash | Rush of water along the bow | 12 | 1 | onset | dailies-1/audio/hull_wash.mp3 |
| drum_turn | Loaded winding drum | 5 | 1 | onset | dailies-1/audio/drum_turn.mp3 |
| arch_tail | Slap of water reflected off brick | 8 | 1 | onset | dailies-2/audio/arch_tail.mp3 |
| ice_release | Flex and release of sheet ice | 2 | 1 | transient | dailies-1/audio/ice_release.mp3 |
| stair_wash | Thin wave on stone | 2 | 1 | onset | dailies-2/audio/stair_wash.mp3 |
| loaf_lift | Crust lifting from a floured board | 2 | 1 | transient | dailies-2/audio/loaf_lift.mp3 |

## Audio map

At event gives numeric **source seconds** within the named clip. Master frame gives the corresponding point in the trailer. For effects, the number pins the audible attack. Each effect plays out its trimmed tail. Gains are dB relative to the track level.

| Scene | Track | Voice | Text | At event | Offset | Gain | Master frame | Picture cue |
|---|---|---|---|---|---|---|---|---|
| S1_TOW | A3 | sfx:rope_catch | | 0.125000 | 0 | 0 | 3 | Establish the strain on the visible line. |
| S2_HELM | A3 | sfx:wheel_grip | | 0.500000 | 0 | -5 | 67 | Cut from the tow to a hand already on the spoke. |
| S2_HELM | A2 | Baker | `Mind the bridge. You lost a morning there once.` | 0.583333 | 0 | 0 | 69 | Begin the warning as the hand carries the spoke upward. |
| S3_FORK | A3 | sfx:hull_wash | | 3.000000 | 0 | -9 | 155 | Let the wake come forward as its curve becomes clear. |
| S4_WINCH | A3 | sfx:drum_turn | | 0.833333 | 0 | -4 | 229 | Weight on the downward handle. |
| S5_ARCH | A3 | sfx:arch_tail | | 0.666667 | 0 | -6 | 286 | Wet brick overhead, with the echo carrying into open air. |
| S6_THAW | A3 | sfx:ice_release | | 0.875000 | 0 | -2 | 373 | The upper sheet starts sliding off the tread. |
| S6_THAW | A3 | sfx:stair_wash | | 3.958333 | 0 | -3 | 447 | A gold runnel spills over the exposed lip. |
| S7_BREAD | A2 | Baker | `Still like the heel?` | 1.375000 | 0 | 0 | 495 | The baker's fingers open over the loaf, before the skipper takes it. |
| S7_BREAD | A3 | sfx:loaf_lift | | 4.500000 | 0 | -5 | 570 | The baker's hand draws clear. Leave this small sound exposed. |

## Music and ambience

- Music (A4): `M2, instrumental clay cups and bowed bass, 120 BPM requested, 30 seconds`. One take. Use `dailies-1/music/music_M2.wav`. Use its first detected downbeat, approximately 1.289544 s into the file. Play one continuous 30-second passage, through the end card, with the standard 0.30 s end fade.
- Bed placement: beat 1 on timeline 0.00. Cuts may move at most ±0 frames toward the beat grid.
- Ambience (A5): `sheltered water at the bakery threshold`, 30 seconds, under the whole film at -31 dBFS RMS, 1.0 s fade out over the end card. Use `dailies-2/audio/quay_perspective.mp3`. Harbour water connects the first wake to the last hand on the sill.

## Mix levels

A2 narrator -6 dBFS peak. A3 SFX -10 dBFS peak. A4 music -22 dBFS RMS, ducked 5 dB under the narrator. A5 ambience -31 dBFS RMS.

## End card

5.166667 s on solid black. Centre all four lines as one block. Use `segoeuib.ttf`. Text fades in over 0.001 s and stays still to the last frame.

- `MORROW UNDER TOW` (9% of the frame height, 100% white)
- `Who gets the morning?` (5% of the frame height, 90% white)
- `17 SEPTEMBER 2027` (5% of the frame height, 100% white)
- `PRE-ORDER · US$34.99` (5% of the frame height, 100% white)

## Local asset layout

The staged files are linked to the original dailies. Picture lives in `clips/<EDL source>.mp4`. In `audio/local/`, effects use `sfx_<name>_1.mp3`, the score uses `music_take1.wav` and the ambience uses `ambience.mp3`. The two A2 files are `vo_3_baker.mp3` from `dailies-1/audio/sister_bridge.mp3` and `vo_9_baker.mp3` from `dailies-1/audio/sister_heel.mp3`. All cue positions are in this brief.

## Export

`out/MORROW_master.mp4`, 1920x1080, 24 fps, H.264 CRF 18, x264 preset slow, AAC 192k 48 kHz. Two-pass loudnorm I=-14 TP=-1 LRA=11.
Preview `out/MORROW_preview_360p.mp4`.

## QA

Duration 30-30 s. Verify 720 frames, all ten cue placements within ±1 frame, -14 LUFS ±0.5 and true peak ≤ -1 dBTP. Check the original-speed picture and the five-second reading hold with playback muted. The first frame must show the tow. The last frame must show the title, tagline, date and price.
