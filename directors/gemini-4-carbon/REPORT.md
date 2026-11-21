# Director's Post-Production Report (`NEAPSCAR`)

## 1. What Worked

- **Two-round `65% / 35%` budget split (`260 / 140` Flow, `2,006 / 994` ElevenLabs, `3 / 1` Flow Music):** Securing full two-take coverage across all eight trailer scenes in Round 1—plus an immediate `100`-credit `Veo 3.1 Quality` hero render on the opening `0–3.25 s` hook (`S1_ANCHOR`)—guaranteed an editable assembly while keeping `140` Flow credits and `994` ElevenLabs credits in reserve for Round 2. Every Round 2 order targeted a measured Round 1 defect, bringing final unspent budget to `0` across video, sound/voice, and music.
- **Repeatable non-facial protagonist silhouette:** Defining the Tether-Diver through consistent outerwear and silhouette markers (dark oiled-canvas storm coat, weathered brass diving goggles over a cloth face-wrap, glowing warm-amber hip lantern, shoulder harpoon-winch) maintained strong visual continuity across eight independent text-to-video prompts without image references or facial uncanny-valley drift, while pairing warm amber highlights against deep teal basalt and sea mist.
- **Single-action physical mechanics engineered for `briefcut` frame sync and silent viewing:** Designing every shot around one high-contrast physical state change—harpoon anchor sparking on wet basalt (`f17` of `S1_ANCHOR`), storm-coat flaring at the cliff brink over a drained sea (`f6` of `S2_BASIN`), wind-skiff launching airborne off a shipwreck rib (`f53` of `S3_SKIFF`), spoked bronze lock-wheel firing a steam bolt before floodgates grind open (`f24` and `f68` of `S4_VAULT`), skittering pebbles tilting up to a hundred-foot tidal bore (`f2` and `f28` of `S5_RETURN`), leviathan pincer smash answered by twin harpoon cannon blasts (`f27`, `f53`, `f78` of `S6_LEVIATHAN`), surf exploding at the base of the sea-spire (`f38` of `S7_ASCENT`), and a two-handed brass maul striking the summit tide-bell (`f21` of `S8_BEACON`)—made the open-world loop legible with the sound off and gave `briefcut` crisp `24 fps` contact frames.
- **Voice auditioning & spectral `150–400 Hz` SFX diagnostics between rounds:** Inspecting Round 1's ledger and waveforms caught two fatal voice issues—Candidate A (`Dom`) peaked below `-21 dBFS` with a young conversational timbre, and Candidate B (`Dain`) turned out to be a Korean-language voice model (`language: ko`)—while revealing the desk's exact Voice Library lookup rule (first-comma clause + gender/age filter). Formatting Round 2's description as `Trailer narrator, male middle aged deep gravelly cinematic baritone` locked onto `Chuck Fresh - Movie Trailer Narrator` (`109.5 Hz` median fundamental, `61.8%` `80–300 Hz` chest power share, clean `-6.9 to -8.8 dBFS` peaks, and `2.77 / 2.19 / 2.53 / 1.29 s` voiced durations that fit every shot window cleanly). Measuring Round 1 SFX in the `150–400 Hz` punch band similarly flagged thin generations (`skiff_carve_1` at `-63.0 dB`, `harpoon_shot_1` at `-53.2 dB`, `foam_surge_1` at `-51.4 dB`); Round 2 re-prompts boosted midrange impact by `+20` to `+36.7 dB` (`skiff_launch_1` `-26.3 dB`, `harpoon_blast_1` `-30.5 dB`, `hook_wave_2` `-31.0 dB`, `anchor_slam_4` `-31.0 dB`).
- **Pre-computing beat-locked `24 fps` cut frames for exact `30.000 s` (`720 frames`) runtime:** Because `briefcut`'s `snapCutsToBeats` can nudge cut points by `±3 frames` (which would otherwise shift total frame count away from `720`), we placed all eight clip trims on the nearest integer `24 fps` frames to `music_attempt2.wav`'s `130.01 BPM` beat grid (`frames 78, 166, 244, 332, 410, 487, 554, 642`, followed by a `78`-frame `END_CARD` to `720`), achieving `< 20 ms` beat alignment with `0/0` frame drift.

---

## 2. What I Would Change

- **Never chain two separate prop interactions in one 8-second text-to-video prompt:** Round 1's `S4_VAULT` prompt asked the salvager to *"slam a glowing cylinder into a socket and pull a heavy lever,"* causing `Veo 3.1 Fast` to toss the glowing cylinder erratically across the frame in both takes. Round 1's `S8_BEACON` prompt (`"slam a blazing core into the cradle of a bell"`) similarly hallucinated a floating fireball and a static sky ring. Starting Round 1 directly with single-body mechanical prompts (wrenching a mounted bronze wheel; swinging a solid two-handed brass maul into the side of a bell) would have freed `40` Flow credits for an additional `Veo 3.1 Quality` upgrade on `S2_BASIN` or `S6_LEVIATHAN`.
- **Write Voice Library descriptions for the first-comma + age-enum rule in Round 1:** Using prose adjectives (`"Deep, weathered..."`) in Round 1 caused the fallback search to query the single word `"Deep"` without a recognized age enum (`young`, `middle_aged`, `old`), spending `278` ElevenLabs credits on two unsuitable Round 1 voices. Leading with `<library archetype>, <gender> <age enum>` from the start would have redirected those `278` credits into additional foley layers.
- **Prefer explicit `8–12 s` durations over `Automatic` length on percussive SFX:** While Round 1's `Automatic` `beacon_strike_4` delivered an exceptional `16.0 s` natural bronze bell decay (`100` credits, used in the final master), Round 2's `Automatic` `beacon_ram_auto` truncated at `1.0 s` (`100` credits for `1 s` of audio). Explicit integer durations (`11` credits/s) eliminate length lottery on resonant hits.
- **Include `full-frame edge-to-edge 16:9 widescreen with no black letterbox bars` in every Round 1 prompt:** Adding that constraint in Round 2 completely prevented the `116 px` top/bottom cinema bars (`crop=1920:848:0:116`) that `ffmpeg cropdetect` caught on `dailies-1/05_S5_RETURN_fast_t1.mp4`, as well as the static `< 1.0` motion tail caught by per-second motion profiling on `dailies-1/05_S5_RETURN_fast_t2.mp4`.

---

## 3. How I Chose the Music Without Hearing It

To select one winning score out of the four generated Flow Music WAV files (`music_attempt1.wav`–`music_attempt4.wav`) without listening to any audio, each file was decoded to `48 kHz` stereo float PCM and evaluated across **six deterministic signal-processing metrics** (using `briefcut`'s `detectBeats`, `tempoSteadiness`, and zero-phase `bandPass` filters):

1. **Detected BPM & Beat Hit Ratio:** Autocorrelation + comb-filter onset locking around the `120 BPM` target to verify a clear rhythmic pulse for cut snapping.
2. **Local Tempo Steadiness (`bpmStdDev`):** Standard deviation of local BPM across sliding `6 s` windows—essential so a frozen beat grid stays locked to percussive transients from `0.0 s` to the `23.708 s` hard stop.
3. **Downbeat Latency (`downbeat`):** Timestamp of the first true musical downbeat (`< 0.05 s` means immediate beat-one energy at frame 0 without trimming past a sluggish intro).
4. **Macro Crescendo Trajectory (`5-second` RMS windows from `downbeat`, `0–25 s`):** A 30-second launch trailer that cuts music dead at `23.708 s` requires a continuous upward energy climb peaking in the `20–25 s` window—never a mid-trailer breakdown dip.
5. **Spectral Vocal Pocket (`45–180 Hz` low drive vs. `300–3000 Hz` speech band relative to broadband RMS):** Measuring how much midrange energy competes with the narrator in the `300–3000 Hz` band before keyed ducking, while retaining low-end weight (`45–180 Hz`).
6. **Dynamic Crest Factor (`Peak - RMS` over `0–23 s`):** Verifying crisp percussive transients (`16–18 dB` crest) rather than over-compressed wash.

### Quantitative Comparison of All Four Flow Music Attempts

| Metric | Attempt 1 (`dailies-1`) | **Attempt 2 (`dailies-1`) — SELECTED** | Attempt 3 (`dailies-1`) | Attempt 4 (`dailies-2`) |
|---|---:|---:|---:|---:|
| **Delivered Duration** | `62.4 s` | **`68.6 s`** | `66.8 s` | `181.2 s` |
| **Detected BPM** | `121.05 BPM` | **`130.01 BPM`** | `120.00 BPM` | `128.00 BPM` |
| **Beat Hit Ratio** | `1.00` | **`0.98`** | `1.00` | `1.00` |
| **Full-Track `bpmStdDev`** | `0.278 BPM` | **`0.122 BPM` (steadiest)** | `1.026 BPM` (drifts) | `0.388 BPM` (`0.074` in 0–35s) |
| **First Downbeat** | `1.072 s` | **`0.017 s` (immediate)** | `0.025 s` | `0.021 s` |
| **Crest Factor (`0–23 s`)** | `16.7 dB` | **`17.4 dB`** | `20.7 dB` | `16.5 dB` |
| **Low Band (`45–180 Hz` rel.)** | `-4.4 dB` | **`-4.4 dB`** | `-5.3 dB` | `-4.0 dB` |
| **Speech Band (`300–3000 Hz` rel.)** | `-7.1 dB` | **`-8.7 dB` (cleaner VO pocket)** | `-7.4 dB` | `-10.4 dB` |
| **5s RMS Arc (`0–5` → `20–25 s`)** | `-20.7 → -16.8 → -16.8 → -15.9 → -14.8 dB` (`+5.9 dB`) | **`-22.4 → -19.6 → -18.8 → -16.7 → -14.0 dB` (`+8.4 dB` strictly monotonic)** | `-19.4 → -21.0 → -22.5 → -20.3 → -18.8 dB` (dips `-3.1 dB` mid-cut) | `-20.3 → -21.5 → -21.1 → -17.9 → -19.1 dB` (3-min slow intro, dips at 20–25s) |

### Elimination & Selection Decision

- **Attempt 3 rejected:** Despite matching `120.00 BPM` globally, its local tempo drifted by `1.026 BPM` (`8×` worse than Attempt 2) and its RMS energy sagged by `-3.1 dB` across `5–15 s` (`-19.4 → -22.5 dB`), creating a hollow midsection right during skiff traversal and vault opening.
- **Attempt 4 rejected:** Flow Music generated a `181.2 s` (`3-minute`) arrangement; consequently, its first `15 s` stayed flat in low-energy intro mode (`-20.3 → -21.5 → -21.1 dB`) and its `20–25 s` window actually dropped `-1.2 dB` (`-17.9 → -19.1 dB`) right where our spire ascent and summit climax needed peak intensity.
- **Attempt 1 vs. Attempt 2 (`Attempt 2` selected):** Both climbed without dipping, but **`dailies-1/music/music_attempt2.wav`** won decisively on four objective counts:
  1. **Steadiest full-track clock (`0.122 BPM` spread vs. `0.278 BPM`)**, locking every 6-second window tightly between `130.0` and `130.4 BPM`.
  2. **Zero intro dead-air (`downbeat = 0.017 s` vs. `1.072 s`)**, hitting frame 0 immediately alongside the `0.292 s` harpoon anchor hook.
  3. **Largest, strictly monotonic crescendo (`+8.4 dB` vs. `+5.9 dB`)**, rising in every single 5-second step from `-22.4 dB` (`0–5 s`) to its `-14.0 dB` peak (`20–25 s`) immediately before the `23.708 s` hard stop on `beacon_strike`, maximizing the dramatic contrast when the music cuts to digital silence.
  4. **Deeper natural vocal pocket (`-8.7 dB` vs. `-7.1 dB` in `300–3000 Hz`)**, giving the baritone narrator `+1.6 dB` of extra midrange separation while matching Attempt 1's `-4.4 dB` low-frequency drive.

---

## 4. Rendered Master Verification (`briefcut` QA)

Assembled and mastered via `briefcut` from `BRIEF.md` + `out/cues.md` (`out/REPORT.md` and `out/SUMMARY.md`):

- **Master export:** `out/NEAPSCAR_master.mp4` (`1920×1080`, `16:9`, `24 fps`, `30.000 s` / `720` frames exact, `-14.10 LUFS`, `-1.10 dBTP`, `0` clipped samples) + `out/NEAPSCAR_social.mp4` (`-10.00 LUFS`, `-1.10 dBTP`) + `out/NEAPSCAR_preview_360p.mp4`.
- **Edit & clip audio:** Hard cuts only (`0/0` frame nudges across all 9 entries, worst cut `19.38 ms` from the `130.01 BPM` beat grid, shortest shot `2.792 s`); all 8 source clip audio streams muted (`-an`).
- **Frame sync & QA:** **16 / 16 QA checks PASS** — `19` cues placed (`0` dropped, `0` events missing), **`0.00` frames worst sync error** measured on the exported master (`out/sync_check.jpg`), first hook hit at `0.292 s`, music digital silence after the `23.708 s` hard stop on `beacon_strike`, and `beacon_strike` verified as the loudest `400 ms` momentary peak.
