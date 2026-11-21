# REPORT: MOONDRAWN launch trailer

The final cut is [BRIEF.md](BRIEF.md) with its cue sheet [out/cues.md](out/cues.md). It is a valid briefcut brief: I ran it, and briefcut rendered `out/MOONDRAWN_master.mp4` from it with all 12 of its QA checks passing (`out/REPORT.md`).

**One thing to know first: I have not heard this trailer.** I judged every sound by measurement and every picture on sheets and frame strips. The levels, timing and frequency balance are checked. What the voice, the music and the effects actually sound like is not.

## The cut

| Time | Shot | Take used | What happens |
|---|---|---|---|
| 0.0-3.5 | S02_PIER | round 2, Veo Fast | Hook: she watches the whole sea run out, boats drop onto the seabed |
| 3.5-5.5 | S03_LAUNCH | round 2, Veo Fast | She goes after it on the sand-yacht |
| 5.5-8.0 | S04_VISTA | round 1, Veo Fast | The open seabed, between colossal wrecks |
| 8.0-10.0 | S05_CITY | round 1, Veo Fast | A drowned city, still pouring water |
| 10.0-12.0 | S06_RELIC | round 1, Veo Fast | She lifts a glowing orb from a chest |
| 12.0-14.0 | S07_GIANT | round 1, Veo Fast | She walks under a stranded giant |
| 14.0-15.5 | S08_EYE | round 1, Veo Lite | Its eye opens on her, at 14.5 |
| 15.5-17.0 | S09_BOOTS | round 2, Veo Lite | Water comes back around her boots |
| 17.0-19.0 | S14_RETURN | round 2, Veo Fast | The sea as a wall; she backs away |
| 19.0-20.0 | S10_WALL | round 1, Veo Fast | The wall smashes the wrecks behind her |
| 20.0-21.0 | S11_CHASE | round 1, Veo Fast | Close on her at the tiller |
| 21.0-23.0 | S12_RISE | round 2, Veo Lite | The giant swims out of the wave beside her |
| 23.0-25.0 | S13_LEAP | round 2, Veo Fast | She jumps the crest, against the moon |
| 25.0-30.0 | END_CARD | text card | MOONDRAWN / Be back before the sea is. / February 26, 2027 / Pre-order now $59.99 |

- **Length:** 30.000 s, 720 frames at 24 fps, 1920x1080.
- **Clip audio:** muted for all 13 clips. briefcut never maps clip audio, and the brief says so.
- **Sound:** one music track, one ambience bed, and 28 cues: six narrator lines and 22 effects. Every cue measures 0.00 frames from its target in the master.
- **Loudness:** -14.0 LUFS, true peak -1.6 dBTP.
- **Narrator:** each line sits 5.7 to 11.5 dB above the rest of the mix in the speech band (300-3000 Hz), measured from the stems.

To render it again: `npx briefcut prepare .` then `npx briefcut cut . --offline`, from this folder.

## How I chose the music without hearing it

I measured all four tracks with briefcut's own beat detector and with loudness per beat, and looked at spectrograms. I chose the track whose measured structure matched the picture, not the one I had expected to use.

| Track | Tempo found | Steadiness (BPM spread) | What the loudness shows | Verdict |
|---|---|---|---|---|
| M1, folk-orchestral | 119.99 | 0.71 | Flat: -17 dB before 0:16, -15 after. Every beat equally accented, so no bar line can be found | Usable bed, no shape |
| M2, stomp and shanty | 122, or 110 when hinted at 120 | 4.30 | Detector locks on only 40% of beats at the ordered tempo | Rejected: grid not reliable |
| M3, quieter first half | 130.05 | 0.19 | Wrong tempo; the big lift arrives at 0:29, after the footage ends | Rejected |
| **M4, straight shanty** | **120.00** | **0.08** | Bar 8 drops 10 dB, hits on bars 9, 11 and 13, bar 12 drops again | **Used** |

Why M4:

- **It is the steadiest and the only one with a findable bar line.** Beat one carries clearly more accent than beats two and four, so the detector's downbeat is the real one. briefcut's own rule for several takes is "steadiest tempo wins", and it agrees.
- **Its shape is three hits with air between them.** I did not order that; I ordered a continuous chase. But measured per beat it is better for a trailer than what I asked for.
- **I laid the cut on it.** With beat one on timeline 1.00, the quiet bar falls on the eye and the boots (15-17 s), the hits fall on the wall (17.0), the giant (21.0) and the title (25.0), and the second quiet bar falls on the leap (23-25 s). Every cut is within 0.09 ms of a beat.
- **The first second has no music**, only the sea draining, so the hook has its own sound.
- **The track does not end at the title; it carries on.** I stop it dead two frames before its bar 14 (26.92 s) and put the last line, "Be back before the sea is.", in the clear.

What measurement cannot tell me: whether the flute tune is any good, whether the track sounds like the game, or whether the stop feels like a decision or a mistake. Those need ears.

## What worked

- **Two rounds, 60/40.** Round 1 gave a usable take of all 13 shots. That let round 2 buy improvements instead of rescues, and six of the 13 final shots are round 2 takes.
- **Testing three models on the same prompts.** Veo Fast is 10 of the 13 final shots and Lite is 3. Lite at half the price was good enough for the eye, the boots and the giant in the wave.
- **Skipping Veo Quality.** The 13 clips on screen cost 115 of the 400 credits; the rest bought the choice.
- **The hook retake.** Both round 1 Veo hooks showed lettering on a boat hull, which the rules forbid. Asking for old wooden boats with bare hulls fixed it, and the retake is also the better shot.
- **The new shot, S14_RETURN.** Framing the returning wave like the hook makes the turn read with the sound off.
- **Measuring the sound.** The three title impacts from round 1 were 90-99% sub-bass and would have vanished on a phone. Without the measurement I would have cut with them.
- **Checking the mix from the stems.** The first render passed QA with the narrator between 2 dB under and 1 dB over the bed on three lines. I compressed the voice, lowered the music 3 dB and ducked ten effects under the narrator to get every line to about 6 dB or more.

## What I would change

- **Voice orders.** The desk's search found nothing for my long descriptions and fell back to the words before the first comma, so "older woman, low and weathered" came back as a young advertising voice. Round 1 of voices was lost to this. Only one of six voices matched its full description, and it is the one in the cut. I would order short, searchable descriptions from the start, and audition with one line per voice.
- **The narrator is slow.** His six lines take 13.8 s of the 30. Line 4 is also a much quieter take than the others and needed 3 dB of gain. With credits left I would re-order lines 1 and 3 shorter.
- **Music orders.** Asking for timestamps and a "continuous build" got one flat track and one at the wrong tempo. I would describe hits and gaps in bars from the first attempt, since that is what the edit needs and what the best track happened to do.
- **Title impact.** Even the round 2 "bright" hits came back 70% sub-bass or as a slow swell. The title lands on the music's own crash plus a crack; it is adequate by the numbers, not a signature sound. I would describe a real mid-range source (metal, timber) and never the word "boom".
- **Omni Flash.** Five clips, 75 credits, none in the final. They were worth having as round 1 tests (the only clean hook and the only real leap arc), but two would have done.
- **The skiff is not the same vehicle twice.** Wheel count, hull and rig change from shot to shot, and in the chase it has grown a deck. Colour (yellow coat, red sail, the moon) holds the film together, but a text-only prompt cannot hold a prop. I would write fewer shots that show it close.
- **Unordered things on screen.** S04_VISTA has a group of figures standing by a wreck. It reads as other salvagers, but I did not ask for them.
- **Pinning from 2 fps sheets.** Their time labels run up to half a second early. I pinned three events from them first and had to re-check all three on exact-frame strips; the eye moved five frames and the orb four. I would pin only from strips.
- **One card.** briefcut draws a single text card, so the title cannot sit over the leap, and five seconds of black is a sixth of the trailer.

## Not verified

- How anything sounds: the narrator's delivery and his pronunciation of "Moondrawn", the music's tune and character, and whether each effect resembles what its prompt asked for.
- The whole film in motion. I checked every cue frame on `out/sync_check.jpg` and the cut on `out/preview_sheet.jpg`, not by watching it.

## Budget

| | Budget | Spent | Delivered | In the cut |
|---|---|---|---|---|
| Video, Flow credits | 400 | 400 | 50 clips | 13 clips |
| Sound and voice, ElevenLabs credits | 3,000 | 3,000 | 44 effects, 37 voice lines | 22 effect files (ambience included), 6 lines |
| Music attempts | 4 | 4 | 4 tracks | 1 track |

## Files

- [BRIEF.md](BRIEF.md): the final cut. Clips, trims, card, music, every sound cue, mix levels, and which dailies file each clip and sound comes from.
- [out/cues.md](out/cues.md): every event frame and how it was found.
- `clips/` and `audio/local/`: the selected takes and sounds under the names briefcut reads.
- `out/MOONDRAWN_master.mp4`: the render.
- `out/REPORT.md`, `out/sync_check.jpg`, `out/preview_sheet.jpg`: briefcut's QA.
