# Morrow Under Tow · trailer plan

The first image should make someone point at the rope. The last should make them hungry. Between the two, the viewer sees a skipper choose a destination, work the winch and bring a frozen quay back into use. The sister has two lines, both dispensable to understanding the trip. Her second is the only one she says face to face.

## The thirty seconds

Target master is 1920×1080, 16:9, 24 fps. The intervals below are timeline seconds, including their start and excluding their end. Source in/out frames will come from the dailies. Each picture row uses one continuous original-speed trim with a hard cut at each boundary.

| Timeline | Frames | Picture to earn | Sound to earn |
|---|---:|---|---|
| 0–3 | 72 | **S1_TOW.** Open with the whole absurd arrangement in profile. The line taking the load and the sun bobbing behind the boat must read by second two. | Put the rope catch on the load. Let the water and the opening note stand alone before anybody speaks. |
| 3–7 | 96 | **S2_FORK.** Hold long enough to see both routes and the wake bend toward the chimney. | The baker comes in over the turn. “Mind the bridge. You lost a morning there once.” |
| 7–11 | 96 | **S3_WINCH.** Sleeve, crank, falling sun. Stay for the moment it locks low. | The drum has a wooden chatter. Give the last tooth one iron click. |
| 11–15 | 96 | **S4_BRIDGE.** The brickwork catches the moving light first. The sun squeezes out under the lip. | Water echoes off the arch. Lose the echo as the orb clears stone. |
| 15–20 | 120 | **S5_THAW.** Keep the white bank and bakery steps in frame as the ice parts. Cut when light on open water reaches the bottom step. | Start the ice resonance on the first visible break. Let the fine melt replace it as the gap widens. |
| 20–25 | 120 | **S6_HEEL.** From the skipper's eyes, a sun-round bread heel comes across the sill. Stay through the touch and release. | “Still like the heel?” on the offer. Leave enough quiet to hear the crust give under the skipper's fingers. |
| 25–30 | 120 | **END_CARD.** Hard cut to black with the four centred lines below. Hold the purchase information for the full five seconds. | One score plays through. Its last answer and the harbour water carry the card. |

End-card copy, in reading order. Set in plain white type. Use heights of 9%, 5%, 5% and 5% of the frame respectively. Make the text settle within the first frame.

1. **MORROW UNDER TOW**
2. Who gets the morning?
3. 17 SEPTEMBER 2027
4. PRE-ORDER · US$34.99

## Two calls on the budget

| Account | Round 1 order | Round 2 allocation | Reason |
|---|---:|---:|---|
| Video | 280 | 120 | Buy a Quality take for the two pieces of difficult physics, the tethered sun and the thaw. Two Fast takes apiece cover the fork, winch, arch and handoff. The reserve buys one more 8-second Quality take and two Fast takes once we can see what broke. |
| Effects and voice | 1,687 | 1,313 | Buy both lines, the continuous harbour air and isolated sounds for each visible action. Keep the rest for sounds whose attack, distance or duration depends on the selected pictures. |
| Music | 3 attempts | 1 attempt | Hear three ways of making this boat move. Spend the last attempt on a revised arrangement timed to the two actual moments of release, under the bridge and at the sill. One complete take supplies the score. |

## Dailies and retakes

Watch each contact sheet in silence first. At thumbnail size the boat, rope and sun must read together before the tug climbs the swell. Reject any trim containing legible marks. Check the opening and the thaw for weight and direction, then find the intervals in the remaining takes that show the right turn, the winch lowering the light, the passage under stone and the hands exchanging bread. For the handoff, favour a take where the baker leaves a little flour on the plum sleeve.

Round 2 priority for the Quality take is a missing opening, then a missing thaw. If both read cleanly, spend it on a close waterline angle of the thaw, with the first piece of ice nudging the lowest bakery step. Put the two Fast orders against the first two missing actions in story order. If all four are present, use them for a sightline from the helm through the fork and a closer handoff where the sister's flour leaves a print on the plum sleeve. The director will write the exact prompts in the second call.

For the sound reserve, budget four auto-length attacks at 100 each and 83 fixed seconds at 11 each. The working split for the fixed material is a 30-second sheltered harbour bed, 25 seconds of under-deck propulsion, 20 seconds of ice resonance and 8 seconds of close bakery room tone. Use the reserve first for any line that misses its picture window, rebalancing those lengths or variants against the returned ledger. Audition the music against rope load, ice release and bread offer. Prefer the take with the clearest contrast between open water and the quiet window. Break a tie by the cleanest ending under the card, then by earlier attempt number.

## Final assembly after delivery

Use the installed briefcut 0.1.0 command `.\.briefcut\cli\briefcut.cmd` from this folder. The checkout includes the [brief format](.briefcut/docs/BRIEF_FORMAT.md) and [edit rules](.briefcut/docs/RULES.md). Use `Video provider: handoff` and `Audio provider: local` in the final `BRIEF.md`. Put one selected take per scene in `clips/`, named by its full scene ID. Put the chosen score in `audio/local/music_take1.*`, the chosen bed in `audio/local/ambience.*`, effects in `sfx_<name>_1.*` in that same directory, and the two voice files in `vo_<audio-map row>_baker.*`. Preserve their actual extensions. Declare one music take in the brief.

Use the 2 fps sheets to locate actions, then 8 and 24 fps strips to pin the audible contacts in `out/cues.md`. Record the selected source In/Out in the EDL and use `END_CARD | 0.00 | 5.00` for the last source and range. Use briefcut's `## End card` section for all four lines. Set beat nudging to `at most ±0 frames`, grade to `none` and shot matching off. Mute the embedded track of every selected clip, including any retake. Mix from the delivered stems, targeting −14 LUFS integrated and at most −1 dBTP.

The final desk pass uses local audio preparation and `cut . --offline`. Check the resulting master for 720 frames, original-speed motion, a legible opening on mute and a readable card on the last frame. Check each attack against its pictured action on the master sync sheet. Source trims, take numbers and the score choice belong to the final cut after both rounds of dailies.
