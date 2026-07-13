# Gloamline plateau survival ceiling — does the committed night ramp ever cap a moving player, or is the best-nights record a patience meter?

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003
> GAME-MECHANICS slot, round 6; rounds 1–5 were P020 casino odds → V022 reject,
> P023 entry fee → V025 reject, P027 comp/stipend → V029 null, P031 explore
> pacing → V033 null, P035 mining booster throttle seal) ·
> **Target:** `menno420/gba-homebrew` (the Game Lab lane — owns the Gloamline
> constants, the difficulty backlog, and the best-nights record system this
> verdict prices; routing is the manager's per Q-0260, this repo never edits
> gba-homebrew files); verification target `menno420/sim-lab` per the Q-0264
> pipeline
> **Grounding:** https://github.com/menno420/gba-homebrew@d87f9ad7d283465c5bc8d26ea47b8cbffb307cc1 · fetched 2026-07-13T16:27:16Z
> (shallow clone at drafting; every constant below quoted from
> `games/gloamline-nds/source/gl_sim.h`, `games/gloamline-nds/source/main.c`,
> and the committed pure mirror `tools/check-gloam.py` — sha256
> `c86d950723b6fff1159a9c6cddb32822f6c8651e65376f2001a86f7372492892` — all at
> that pin; subject sourced via superbot `docs/fleet-reading-path.md`,
> raw-fetched this slice; pokemon-mod-lab DARK, skipped per the path's rule)

**Origin:** drafted under standing owner ORDER 003 ("continue coming up with new
ideas, that is your main purpose") in the ORDER 004 rule-3 rotation — round 6:
P037 served fleet-backlogs, P038 served venture, so this head is the round's
GAME-MECHANICS slot. It is the first game-mechanics head sourced from the Game
Lab repo (all five prior rounds drew on superbot/superbot-games), and the first
whose entire engine is a sibling lane's own committed pure-Python proof mirror.

## The idea

Gloamline (gba-homebrew's owner-picked NDS horde-defense arc, 11 slices shipped)
scores runs in **nights survived**, and the lane has now built two whole slices
of infrastructure on that score: the slice-9 battery best-nights record
(EEPROM-wear-disciplined, strictly-better-only writes) and the slice-11 rematch
verb (SELECT replays the recorded best seed spawn-for-spawn). The difficulty
curve under the score is committed and pinned: waves ramp `2·night − 1` to a
**cap of 24 at night 13** (`gl_wave_count`), all of a night's dead spawn inside
the first 2,400 frames of a 3,600-frame night on the fence perimeter, and the
player is strictly faster than every Shambler (384 vs 192 subpx/frame — 2:1,
effectively 2.67:1 against the 1/4 stagger expectation).

The lane's 28 host proofs (517 asserts) verify the mechanics exhaustively — but
every survival-shaped proof is about an **idle** player (proof 2: from every
spawn, an idle player is contacted within 400 frames) or about
survivability-in-principle of single mechanisms. **No committed artifact
measures whether the night-13 plateau actually pressures a MOVING player.**
That is the load-bearing unknown under the record system: if a clean bounded
kiting policy survives the 24-crowd plateau indefinitely, the nights-survived
record is unbounded and measures patience (or execution stamina), not skill —
and the concept doc's own later-lever ("dark edges spawn faster") is what the
difficulty backlog needs next, before more record chrome. If the ramp corners
every bounded policy at a computable night, the record is a real skill score
with a measurable ceiling. Neither direction is pre-computable: the speed
advantage argues kiter immortality, but spawns land ON the fence all through
the first 2,400 frames and the safe radius guards only the **lamppost**
(night-start position, `gl_spawn_of_night`) — a fresh spawn may land 14 px from
a perimeter-kiting player's path, and a closed loop laps its own slow pursuers
into a wall, while an interior evader faces encirclement instead. Which effect
wins at 24-crowd density is exactly the open number.

## The model (every constant committed in-tree @ `d87f9ad`)

**Engine = the lane's own mirror, byte-reused.** The sim imports the `gl_*`
function block byte-copied from `tools/check-gloam.py` @ `d87f9ad` (full-file
sha256 pinned above, re-verified before import — the V042/V043 byte-reuse
precedent applied to a sibling lane's proof mirror): `gl_hash`,
`gl_spawn_of_night`, `gl_player_step`, `gl_shambler_staggers`,
`gl_shambler_stride`, `gl_shambler_step`, `gl_chebyshev`, `gl_contact`,
`gl_wave_count`, `gl_spawn_frame`, `gl_shove`, `gl_dark_press`,
`gl_light_radius`. Constants (quoted): arena 16..239 × 32..175 px at
`GL_ONE=256` subpixels; lamppost (128, 104); player 384/271 straight/diag;
Shambler 192/135; stagger `(gl_hash(id, frame) & 3) == 0` (rate 1/4); contact
Chebyshev < 10 px; safe radius 64 px from the lamppost; `GL_ZOMBIE_CAP` 24;
`GL_WAVE_SPAWN_SPAN` 2,400; `GL_NIGHT_FRAMES` 3,600; shove nearest-only, range
24 px, push 40 px per axis, stun 45, cooldown 90 (an attempt arms the cooldown
hit or whiff — `main.c do_shove_verb`); dark press `oil < GL_OIL_LOW ∧ dist >
gl_light_radius(oil)` cancels the stagger (at oil 0 the radius is
`GL_LIGHT_R_MIN` = 24 px). Per-frame loop order quoted at drafting from
`main.c` @ `d87f9ad` and pinned in the fixture: spawn due indices
(`gl_spawn_frame`) → player step (keys → `gl_player_step`) → shove verb →
the dead's step (`step_the_dead`, main.c:737 — stun decrement → stagger unless
pressed → stride; barricades carry no decision role here) → contact check ends
the run. Each night starts fresh — player at the lamppost, crowd empty
(`start_night`, main.c:521) — so the per-night cell is the game's own
semantics, not a simplification.

**Policy family (pre-registered, deterministic, keys-only — exactly the input
surface the ROM accepts, one key-set per frame):**

- **IDLE** — the regression leg (must reproduce proof 2's bound exactly).
- **KITE-PERIM** — clockwise waypoint loop on the rectangle inset 24 px from
  the fence (waypoints (40,56), (215,56), (215,151), (40,151) px); per-axis
  signed move toward the current waypoint (deadzone GL_ONE/2); waypoint
  advances at Chebyshev ≤ 2 px. Zero crowd awareness — the CHEAPEST policy.
- **KITE-GRAD** — myopic evader: each frame score all 9 key-sets (8 directions
  + none) through `gl_player_step`; score = min over live Shamblers of
  Chebyshev to the moved point; pick the max, ties by pinned order (N, NE, E,
  SE, S, SW, W, NW, stay). The one-frame-lookahead skill bracket.
- **SHOVE-PERIM / SHOVE-GRAD** — the same two plus A whenever the cooldown is
  0 and the nearest Shambler is within `GL_SHOVE_RANGE`.

Barricades/planks/scavenge are OUT of decision scope by design (no B presses;
proof 7 already settled the no-trap/eventual-pressure art; a camper family is
the named follow-up head if NULL binds on it).

**Oil legs (the second decision axis — the lantern's survival value):**
**LIT** (`oil_for_press = GL_OIL_MAX`: press identically 0, stagger active —
the pre-slice-7 chase) vs **DARK** (`oil_for_press = 0`: any Shambler farther
than 24 px from the player never staggers). The LIT−DARK ceiling delta prices
slice 7's whole pressure mechanic in nights, for the first time.

**Arm D — deterministic census (zero RNG; game seeds are enumerated fixture
inputs, NOT registry seeds — stated):** decision cells = {KITE-PERIM,
SHOVE-PERIM} × {LIT, DARK} × nights {13, 16, 20, 24} × game seeds 0..127, and
{KITE-GRAD, SHOVE-GRAD} × {LIT, DARK} × nights {13, 24} × game seeds 0..31
(the 9-move scan is 9× the work); ramp leg nights 1..12 × seeds 0..127 ×
KITE-PERIM × LIT reporting-only (the curve under the record). Metrics per
cell: SURV (fraction of seeds surviving the full 3,600 frames), median death
frame among deaths, min-gap quartiles, shove connects.

**Arm S — seeded execution noise (the human-hands bracket):** each frame
w.p. ε ∈ {1/16, 1/4} the policy's chosen key-set is replaced by a uniform draw
over the 9 key-sets (the A press is not perturbed); {KITE-PERIM, KITE-GRAD} ×
{LIT, DARK} × nights {13, 24} × ε, M = 32 replications × game seeds 0..31.
Seeds: **20261293 main / 20261294 stability (M = 16, must reproduce the
ruling) / 20261295 reporting / 20261296 aux (never read by any decision
number)** — allocated strictly above the P038 registry high-water 20261292
(re-checked across all prior outbox blocks at drafting; nothing higher).
Pinned loop order (policy, oil, night, ε, seed, replication); one
`random.random()` per frame.

**Gates (run invalid on any failure):** mirror sha256 re-verified before
import; IDLE regression — from every spawn of seeds 0..63 × nights 1..4,
monotone non-increasing Chebyshev and contact within 400 frames (proof 2's own
bound and range, reproduced exactly); spawn identities on every census spawn —
on the fence perimeter, ≥ 64 px from the lamppost (proof 1's predicate),
`gl_wave_count ≡ min(2n−1, 24)` exact, spawn frames non-decreasing and
< 2,400; stagger-rate identity (mean over a pinned (id, frame) grid within 3σ
of 1/4) and DARK-leg zero staggers among steps with dist > 24 px, measured on
every leg; press-dominance spot gate (the pressed chase never reaches contact
later than the lit chase from the same spawn — proof 11's own property,
sampled on its committed range); per-leg frame/draw-count sentinels; twin
independently-written decision evaluators; stdout + results.json byte-identical
across two process runs; CPython minor pinned.

## Decision rule (pre-registered; evaluated in this order, REJECT first)

- **REJECT** ("the plateau carries no pressure for clean bounded play — the
  nights-survived record is a patience meter"): KITE-PERIM at LIT survives in
  ≥ 99% of census seeds at EVERY decision night {13, 16, 20, 24} AND the
  ε = 1/16 noisy KITE-PERIM at night 24 LIT survives ≥ 90% of replications.
  Checked FIRST — the costly error is the lane spending further slices
  polishing an unbounded score (two record-chrome slices already shipped)
  when the concept doc's own named-later lever ("dark edges spawn faster")
  is what the evidence demands next. Consequence: the difficulty backlog gets
  the quantified reason, routed lane-side via the manager sweep (Q-0260).
- **APPROVE** ("the committed ramp has a real ceiling — the record is a skill
  score"): EVERY swept policy (including SHOVE-GRAD, the strongest) posts
  SURV < 50% at some decision night in BOTH oil legs, stability-reproduced;
  the per-policy ceiling table is the pin. Consequence: the best-nights
  record system is ratified as a bounded skill score with the measured
  ceiling attached; no difficulty lever demanded.
- **NULL** (anything else — a legitimate and here plausible outcome): the
  conditional finding is the citable pin — e.g. the noiseless kiter immortal
  while ε-noise kills within the plateau (difficulty lives in execution
  consistency, a legitimate arcade shape, quantified as the measured
  noise→survival curve); or the LIT/DARK fork flips a band (the lantern's
  survival value in nights — slice 7's pressure measured); or KITE-PERIM dies
  to lapped-crowd pileups while KITE-GRAD walks free (the skill axis is
  routing, not speed). Flip axes named via per-axis survival shares. Cheapest
  live probe named: the lane's own committed route files and the battery's
  EARNED best-nights record (proof 20: best = 1, seed 118 — the emulated
  chip's own dawn write) locate real play on the measured curve at zero new
  tooling.

**Boundaries (stated in the verdict):** the policy family brackets BOUNDED
play, not optimal play — every SURV is a lower bound on the best player's, so
REJECT (immortality shown by one bounded policy) is robust in its direction
while APPROVE rules on this family only (stated); KITE-GRAD is myopic by
design (one-frame lookahead); the plank/oil/scavenge ECONOMY is out of
decision scope (nights are independent by `start_night`'s own reset; oil
enters as the two pinned legs, not a trajectory — the dynamic oil-skip
sustainability head is the named runner-up below); policies emit exactly the
key-sets the ROM accepts. **Liveness, disclosed:** no closed form decides any
band — the 2:1 speed ratio argues REJECT, the fence-spawn stream measured from
the lamppost (not the player) plus the lap-your-own-pursuers geometry argue
APPROVE/NULL; the drafting session pins no expected landing beyond naming
NULL's conditional shapes as plausible.

## Dedup (swept at drafting, HEAD `8e588f0`)

Tree-wide `rg -i "gloamline|shambler|horde|kiting|lamplighter|survival.ceiling"`
(bootstrap.py/.substrate excluded): zero hits outside this head's own files. No
outbox proposal P001–P038 cites gba-homebrew at all; the section's four
2026-07-10 heads are all parked(build-direct), none sim-shaped. Nearest by
SLOT: P031 → V033 and P035 (superbot-games pacing/economy — different repo,
different machinery, zero shared fixture/metric/consumer). Nearest by SHAPE:
the casino family P020/P023/P027 → V022/V025/V029 (bankroll-ruin grids — the
player risks chips there, position here; zero shared model). Nearest by
METHOD: V042/V043 (committed-engine byte-reuse) and P031 → V033 (policy census
over composed committed machinery) — method precedent only. P031's own
alternatives line passed a browser-game difficulty pin because it had "no
committed in-tree baseline to chain to tonight" — Gloamline's mirror IS the
committed baseline that head lacked, which is why this head exists now.

**Alternatives passed on merit:** the Gloamline oil-economy multi-night
sustainability head (proof 12's static one-interlude margin made dynamic) —
real but smaller stakes: the static margin is 2× and proofs 10/12 already show
every pickup fits the dawn walk, so the dynamic question reduces to a
skip-policy tax table; the Brineward arc (sibling game, concept tree mid-build,
no committed score surface yet); Lumen Drift seeded-cave difficulty (the
lane's own `check-cave.py` self-serves per-seed passability in CI — "nothing
sim-shaped" per the section's 2026-07-11 probe); a mineverse browser-game
difficulty pin (no committed pure mirror there; V042's family already prices
that lane's economy shape).

## Probe report (v0, 2026-07-13)

**1. What is this really?** A pre-registered survival-ceiling census for a
shipped game's committed difficulty curve: does the night ramp (2n−1, cap 24)
ever cap a moving bounded player, measured by driving the lane's own
byte-reused pure mirror under a pinned policy family — pricing the score
system two shipped slices already build on.

**2. What is the possibility space?** Trust the ramp by vibes (the status
quo — record chrome ships on an unmeasured score); hand-tune difficulty
lane-side without evidence; wait for real owner playtests to reveal the
ceiling (slow, n=1, unrecorded); or this head: enumerate the game's own seed
space under bounded policies and pre-register what each landing means for the
lane's next slice.

**3. Most advanced capability from the simplest implementation?** One stdlib
sim + fixture JSON: the mirror block byte-copied (sha256-gated), five
deterministic policies, two oil legs, a seeded noise bracket — producing a
per-policy per-night survival table, a noise→survival curve, and the
lantern's survival value in nights, all byte-reproducible.

**4. What breaks it?** The policy family is the disclosed weakest joint —
bounded policies bracket real play from below, so APPROVE rules on the family
only (stated in-band); KITE-GRAD's one-frame myopia may under-read the skill
ceiling (the noise arm brackets the other side); the per-night cell excludes
the cross-night economy by design (the game's own `start_night` reset makes
that exact, not approximate, for position/crowd — only oil/planks carry, and
oil is swept as its two extreme legs).

**5. What does it unlock?** The lane's next-slice fork, decided on evidence:
late-ramp difficulty lever vs record-system ratification vs the conditional
rule (noise curve / lantern delta); plus reusable art — a
policy-census-over-committed-mirror kernel any shipped game with a pure proof
layer can inherit (Brineward is next in line as its arc completes).

**6. What does it depend on?** Nothing at verdict time — fully hermetic:
every constant quoted into the fixture at drafting @ `d87f9ad`, the mirror
byte-copied and sha256-gated, zero repo/network reads in the verdict session.
Consumers: gba-homebrew owns the constants and the difficulty backlog
(routing is the manager's per Q-0260); sim-lab owns the method precedent.

**7. Which lane should build it?** sim-lab (the hermetic pre-registered
discipline is the P017–P038 committed precedent; the byte-reuse move is
V042/V043's). The verdict consumer is the gba-homebrew lane via the manager
sweep. Dedup argued line-by-line above — no prior proposal or verdict touches
this repo's games, survival ceilings, or horde-defense mechanics.

**8. What is the smallest shippable slice?** The committed sim + fixture
reproducing the census, noise legs, and gates byte-identically per the
done-when in the outbox block — one PR in sim-lab, no lane build.

**Recommendation: sim-ready**
