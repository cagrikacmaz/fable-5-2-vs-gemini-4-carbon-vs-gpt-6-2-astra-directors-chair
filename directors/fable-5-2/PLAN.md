# PLAN: MOONDRAWN launch trailer

## The trailer

One idea, readable with the sound off: **the sea leaves, you go in, the sea comes back.** The hook is the sea itself pulling away from a harbour in the first three seconds. The middle is the reward (what is down there). The last third is the price (the wall of water). The end card answers the whole thing in six words: *Be back before the sea is.*

Planned cut, 30.000 s = 720 frames at 24 fps. Music is ordered at 120 BPM, so a beat is 12 frames and every cut below sits on a beat.

| Time | Shot | What a silent viewer reads | Sound (all added in the edit) |
|---|---|---|---|
| 0.0-3.0 | S02_PIER or S01_DRAIN | A girl in yellow watches the sea run away under a giant moon | `sea_drain` from frame 0, music enters at 1.0, line N1 |
| 3.0-5.0 | S03_LAUNCH | She goes after it on a sailing cart | `sail_snap`, `skiff_run`, line N2 |
| 5.0-7.5 | S04_VISTA | The seabed is a huge open world | `skiff_run`, line N3 |
| 7.5-10.0 | S05_CITY | There is a drowned city down here | `ruin_falls` |
| 10.0-12.0 | S06_RELIC | And things worth taking | `relic_shimmer` |
| 12.0-14.0 | S07_GIANT | And things asleep | `giant_breath` |
| 14.0-15.5 | S08_EYE | It wakes, she is reflected in its eye | `eye_open` |
| 15.5-17.0 | S09_BOOTS | Water is coming back around her boots | `water_rush`, line N4 |
| 17.0-19.5 | S10_WALL | The whole sea, as a wall | `wall_roar`, music changes gear on its bar 9 |
| 19.5-21.0 | S11_CHASE | She is not fast enough | `skiff_run`, `wall_roar` |
| 21.0-23.0 | S12_RISE | The giant swims in the wave beside her | `giant_call` |
| 23.0-25.0 | S13_LEAP | She jumps the crest, against the moon | `leap_whoosh`, `riser` |
| 25.0-30.0 | END_CARD | MOONDRAWN / Be back before the sea is. / February 26, 2027 / Pre-order now $59.99 | `title_slam`, music stops dead, lines N5 and N6 |

## What briefcut accepts, and what that decided

I installed briefcut 0.1.0 in this folder, read its docs and its parser, and parsed a draft of the final brief to confirm the format below is accepted.

- **Clip audio is never used.** briefcut renders the picture without audio and maps only its own mix, so in the final cut every clip is **muted**. I therefore asked the video models for no dialogue and no music, and every sound in the trailer is ordered separately.
- **Hard cuts only, no retiming.** That matches the rules here. Each shot is one trim of one clip.
- **One text card.** briefcut draws a single end card from text lines. Title, tagline, release date and price all go on it, 5 s long, and nothing readable is asked for inside footage.
- **Exactly 30 s.** The brief will say `Duration 30-30 s` and `Cuts may move at most ±0 frames`, so the frames I list are the frames rendered: 600 of footage plus 120 of card. Minimum shot is set to 1.0 s; the shortest planned shots are 1.5 s.
- **Cuts on the beat grid.** briefcut measures the music's real tempo and checks every cut against it. I order 120 BPM, then recompute the cut frames from the measured grid in the final. Music starts on timeline 1.00 so its bar 9 lands on the wave (17.0) and its bar 13 on the title (25.0).
- **Music ends on the title.** `Hard stop` cuts the music at the end card and `title_slam` is set as the loudest moment, with its tail held under the last two lines.
- **Own audio files.** With `Audio provider: local`, briefcut reads files named `sfx_<name>_<variant>`, `vo_<row>_<voice>`, `music_take1` and `ambience`. The sound-effect labels in ORDERS-1 already use those names.
- **Effects are placed by their attack on a pinned frame.** Each sound is tied to a frame I find on 8 and 24 fps strips of the chosen take, so which sounds I need depends on what the takes show. That is a reason to hold sound budget for round 2.

## Budget across the two rounds

| Budget | Round 1 | Round 2 | Total |
|---|---|---|---|
| Video, Flow credits | 240 | 160 | 400 |
| Sound and voice, ElevenLabs credits | 1,779 | 1,221 | 3,000 |
| Music attempts | 2 | 2 | 4 |

**Video, round 1 (240).** Thirteen shots, each as one Veo 3.1 Fast take (130) and one Veo 3.1 Lite take (65), plus Omni Flash 1.2 at 720p for 5 s on the three shots that depend most on water physics: the hook, the wall and the leap (45).

- Every shot gets two takes from two models, and the three that carry the trailer get three.
- All Veo clips are 8 s because the price is the same for 4, 6 or 8 and I only need 1 to 3 s of each: more frames to choose from at no cost.
- No Veo 3.1 Quality. One clip is a quarter of the budget and cannot be retaken; the same 100 credits buys ten Fast takes, and in a cut this fast the take matters more than the last step of fidelity.
- No 360p. Delivered at 1080p it would be the softest shot in the film.
- Round 1 is also the model test. Fast and Lite run the same thirteen prompts side by side, and Omni runs three of them.

**Video, round 2 (160).** Prompts in round 1 are written blind; round 2 is written after seeing what each model does with them, so 40% is held back. In order:

1. Any shot with no usable take: rewritten prompt, two takes on the model that did best.
2. More takes of the hook, the wall and the leap.
3. If Lite holds up next to Fast, the rest goes to Lite and buys twice as many takes. If Omni wins, its 3 s minimum makes the short inserts 9 credits each.
4. The last credits go to zero with Omni's per-second price.

**Sound, round 1 (1,779).** All effects use a set length at 11 credits per second, never the 100-credit automatic length: 28 generations for 1,287 credits, including a 30 s ambience bed, three variants of the title impact and two of every sound that carries a story beat. Voice is six short lines, 164 characters, read by three different voice descriptions (492), because the desk takes the first library result and I want a choice. Each line is its own file so it can be placed on its own frame.

**Sound, round 2 (1,221).** The six lines again in the winning voice, with any rewording the cut's timing asks for; effects for whatever the chosen takes show that I did not predict; replacements for sounds that measure wrong. What remains goes to extra variants of the title impact and the closing lines, and a final line sized to land on zero.

**Music, 2 + 2.** Round 1 tries two characters at the same tempo and structure: folk-orchestral (M1) and stomp-and-shanty (M2). Both ask for an instant start, 8 bars of wonder, 4 bars of chase and a final hit at 0:24. Round 2 spends the other two attempts refining whichever came back closer, using the measured tempo, length and shape.

## How I will judge the dailies

- **Picture:** the desk's contact sheets, then `briefcut sheets --takes` for 2 fps sheets with motion profiles, and `briefcut strip` at 8 and 24 fps for the frames I will cut and sync on. A take is rejected for readable text or glyphs, interface elements, a morphing hero or skiff, or action that starts too late to trim.
- **Sound:** by measurement, since I judge files, not a mix: briefcut's beat detection for tempo and steadiness of each music take, loudness curves for build and for the final hit, spectrograms for vocals and for where each effect's energy sits (an impact that is all sub-bass disappears on a phone), and attack position and length for every effect.

## Risks and fallbacks

- **The draining sea does not read in three seconds.** Open on S08_EYE (it acts in its first second) or on the wall, and let S01/S02 follow. Line N1 still states the premise.
- **Hero or skiff differ between clips.** Colour carries identity: mustard-yellow coat, rust-red sail, giant moon, in every prompt in the same words. The cut can lean on the wides, where both are small.
- **The giant in the wave fails.** Drop S12 and give its two seconds to the wall and the leap.
- **Music comes back at another tempo, with an intro, or with a voice.** The cut follows the measured grid, not the ordered one; two attempts are held for a retake.
- **A voice is wrong for the game.** Three were ordered; round 2 re-reads in the best one.
