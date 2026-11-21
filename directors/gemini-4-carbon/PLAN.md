# PRODUCTION & BUDGET PLAN (`NEAPSCAR`)

## 1. Trailer Architecture & `briefcut` Alignment

The final cut is a **30.000-second (`720 frames` at `24 fps`), `16:9` (`1920×1080`)** launch trailer assembled deterministically with `briefcut` (`Audio provider: local`, hard cuts only, original clip speed, zero retiming/zooms/transitions, mastered to `-14 LUFS ±0.5` / `≤ -1.0 dBTP`).

Reading `briefcut`'s source and QA rules directly shaped four foundational production decisions before placing a single Round 1 order:

1. **Every clip's embedded audio will be muted:** `briefcut` renders picture with `-an`, discards source clip audio streams, and enforces `No audio from the source clips in the master` in QA. Every sonic element in the trailer—voiceover (`A2`), frame-accurate diegetic foley and impacts (`A3`), musical pulse (`A4`), and continuous seabed wind/surf room tone (`A5`)—must therefore be ordered explicitly from ElevenLabs and Flow Music.
2. **Exact beat-to-frame grid (`120 BPM` at `24 fps`):** At `120 BPM`, one beat equals `0.500 s` (`12 frames`) and one 4/4 bar equals `2.000 s` (`48 frames`). Every planned shot length (`3.0 s`, `3.5 s`, `4.0 s`) sits above `briefcut`'s `2.0 s` minimum shot rule with room for `±3 frame` beat-grid nudges, summing to **30.000 seconds (`720 frames`)**:
   - `S1_ANCHOR` (`0.00–3.00 s`, `3.0 s`): **Hook** — brass harpoon-anchor slams wet basalt with sparks in `< 0.5 s` as whitewater surges past.
   - `S2_BASIN` (`3.00–6.50 s`, `3.5 s`): **World Reveal** — cliff brink pull-out across miles of steaming, freshly drained seabed, coral canyons, and stranded wrecks.
   - `S3_SKIFF` (`6.50–10.00 s`, `3.5 s`): **Feature 1 (Traversal)** — hydro-skiff carving mirror-wet salt flats, sail snapping taut to jump a sunken hull rib.
   - `S4_VAULT` (`10.00–13.50 s`, `3.5 s`): **Feature 2 (Salvage Engineering)** — slotting a glowing amber core to grind open barnacled bronze floodgates.
   - `S5_RETURN` (`13.50–16.50 s`, `3.0 s`): **Escalation** — skittering pebbles tilt up to a hundred-foot wall of ocean thundering back across the horizon.
   - `S6_LEVIATHAN` (`16.50–19.50 s`, `3.0 s`): **Feature 3 (Combat)** — trench leviathan pincer smash countered by a pneumatic tether-harpoon swing.
   - `S7_ASCENT` (`19.50–22.50 s`, `3.0 s`): **Climax Build** — vertical winch ascent up a sheer beacon spire as the tidal bore explodes against its base.
   - `S8_BEACON` (`22.50–26.50 s`, `4.0 s`): **Climax Strike + Hard Stop** — slamming the amber core into the summit bronze tide-bell; music hard-stops (`20 ms` fade) on `beacon_strike`, leaving a `1.5 s` protected shockwave window before the closing narrator line (`Outrun the sea.`).
   - `END_CARD` (`26.50–30.00 s`, `3.5 s`): **Text Card** — native `briefcut` black end card fading in title (`NEAPSCAR`), tagline (*Forty minutes of dry seabed. Then the ocean comes home.*), release date (`DECEMBER 4, 2026`), and price (`$69.99`), punctuated on `text_in` by `card_lock`.
3. **Works with the sound off:** Because generated clips forbid all on-screen text/HUD/UI, every shot was designed around a distinct, high-contrast physical cause-and-effect state change—anchoring against whitewater, revealing a drained sea, sailing the seabed, opening a sunken vault, spotting the returning wave wall, grappling a leviathan, winching up a tower, and firing a storm-parting beacon—culminating in a self-explanatory tagline and pre-order card.
4. **Silhouette continuity across independent text prompts:** Giving the Tether-Diver a consistent non-facial silhouette (dark oiled-canvas storm coat, brass diving goggles over a cloth wrap, glowing warm-amber hip lantern, shoulder harpoon-winch) prevents facial morphing across clips while keeping teal-vs.-amber visual readability sharp.

---

## 2. Two-Round Budget Allocation & Rationale

Unspent credits earn nothing, yet spending 100% blindly in Round 1 leaves zero capacity to fix generative artifacts, hallucinated glyphs, off-tempo music, or newly discovered visual actions on the Round 1 contact sheets. Our split secures **100% playable trailer coverage in Round 1** while reserving **targeted high-impact firepower for Round 2** so every credit is spent by wrap.

| Resource | Total | Round 1 Spend | Round 2 Reserve | Strategy |
|---|---:|---:|---:|---|
| **Flow Video** | 400 credits | **260** (65.0%) | **140** (35.0%) | Full 8-scene multi-take base + S1 Quality hook now; 1 Quality hero upgrade + 4 Fast retakes in Round 2 |
| **ElevenLabs Audio** | 3,000 credits | **2,006** (66.9%) | **994** (33.1%) | 2-voice VO audition + 2×30s ambience + multi-take SFX now; picture-locked foley & VO/SFX retakes in Round 2 |
| **Flow Music** | 4 attempts | **3** (75.0%) | **1** (25.0%) | 3 distinct 120 BPM instrumental arrangements now; 1 diagnostic refinement attempt in Round 2 |

### Video: 260 Spent Now / 140 Reserved for Round 2
- **Why unify on the Veo 3.1 family at 8 seconds (`1080p`):** Every `8 s` clip is delivered at `1080p` at no extra cost and provides `4.0–5.0 s` of trim margin around a `3.0–4.0 s` edit window—essential for trimming around AI motion drift without violating `briefcut`'s ban on retiming. Staying inside Veo 3.1 (`Quality` + `Fast`) preserves uniform color rendering and frame cadence across cuts.
- **Why 260 credits in Round 1:** Ordering **2 outputs in Veo 3.1 Fast (`20 credits/scene`)** across all 8 scenes (`160 credits`) guarantees at least two takes per shot immediately. Investing **100 credits in Veo 3.1 Quality** on `S1_ANCHOR` right away locks flagship texture and water/spark fidelity onto the crucial first 3 seconds (`3 takes` total on the hook).
- **How the remaining 140 credits will be spent in Round 2:**
  - **100 credits (`1 × Veo 3.1 Quality`, 8s, 1080p):** Reserved to upgrade our climax money shot `S8_BEACON` (or `S2_BASIN` if `S8`'s Fast take is already flawless) once Round 1 contact sheets validate how the prompt frames the summit shockwave.
  - **40 credits (`4 × Veo 3.1 Fast`, 8s, 1080p):** Reserved for prompt-revised retakes on whichever Round 1 scenes show character glitches, weak impact frames, or unwanted symbols. If all 8 scenes pass cleanly, these 40 credits add alternate action angles or B-roll options so `0` Flow credits go unspent.

### Sound & Voice: 2,006 Spent Now / 994 Reserved for Round 2
- **De-risking blind voice selection (`278 credits`):** Because the production desk picks the *first library result* for a one-line voice description, relying on a single description risks an unsuitable vocal timbre or room reflection. Ordering all four concise lines (`139` characters total) in **two contrasting descriptions**—a weathered male baritone (`Orders 10–13`) and a smoky female contralto (`Orders 31–34`)—costs under 10% of the ElevenLabs budget and lets us select the cleaner, lower-centroid voice in Round 1 dailies.
- **Full-length ambience & multi-take transient SFX (`1,728 credits`):**
  - Two `30-second` continuous seabed wind-and-surf beds (`660 credits`) ensure a seamless `A5` floor across the entire `30.0 s` runtime with zero silence holes.
  - Every scene (`S1`–`S8` + `END_CARD`) receives dedicated fixed-length foley and impact generations (`11 credits/s`), with 2 takes on key transients (`anchor_slam`, `sail_snap`, `core_lock`, `bore_horn`, `leviathan_slam`, `harpoon_shot`, `spire_crash`, `card_lock`) for take selection and `briefcut` variant rotation.
  - The climax `beacon_strike`—which must carry the trailer's loudest `400 ms` momentary peak, sustain its tail at `1.2 dB/s` after the music hard-stop, and duck cleanly in the `300–3000 Hz` speech band under the final line—gets **three `8 s` takes (`264 credits`) plus one `Automatic` take (`100 credits`)** to guarantee rich midrange punch and harmonic bronze ring.
- **How the remaining 994 credits will be spent in Round 2:**
  - Once Round 1 video dailies arrive and we inspect `2 fps` contact sheets and `8/24 fps` strips, generated footage routinely reveals specific visible physical moments (extra footsteps, secondary wave splashes, debris scatter, cable creaks) that require custom frame-pinned foley so sound matches picture on `sync_check.jpg`.
  - Any remaining balance in Round 2 will fund tightened VO line rewrites (if a shot's clean window is shorter than expected), extra SFX variants, and rich acoustic sweeteners, spending the full `3,000`-credit allocation down to zero.

### Music: 3 Attempts Spent Now / 1 Attempt Reserved for Round 2
- **Why 3 attempts in Round 1:** Music generation varies in beat-one onset clarity and local tempo drift. Generating three `120 BPM`, `30-second`, strictly instrumental maritime-orchestral arrangements upfront gives `briefcut`'s beat detector three real candidates to rank by local BPM steadiness and rhythmic drive from `0.00 s` to the `~22.8 s` hard stop.
- **Why 1 attempt in Round 2:** Holding the 4th attempt allows a targeted revision after hearing Round 1's tracks (fixing tempo drift, brightening percussion transients, or sharpening the climax climb)—or, if Round 1 already yields a winner, testing one bold alternate arrangement before locking the single best track into the final cut.
