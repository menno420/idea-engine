# Seeded cave runs — one parameter multiplies the endless cave into infinite caves

> **State:** parked(build-direct — owner-gated new scope: the lane's ⚑ concept pick, still open at lane HEAD `c7592d6`, is exactly the gate the capture predicted; this head is the "keep investing in Lumen Drift" arm's concrete costed option for the owner's EAP sitting (window ends 2026-07-14) — one lane PR post-pick, nothing for sim-lab: the only empirical question, per-seed passability, is self-served by the lane's own `tools/check-cave.py` mirror in CI)
> **Class:** product · **Target:** `menno420/gba-homebrew`
> **Sequence:** after the owner concept pick (the lane's top ⚑ at `c7592d6`; expected at the EAP sitting, window ends 2026-07-14) — the head's whole purpose is to be ON THE TABLE at that sitting as the "more Lumen Drift" arm's named option, so it must be probed/costed BEFORE the pick and built only AFTER it

## Problem

Polish pass 3 rebuilt the world so every row is a **pure function of the world
row** — an endless deterministic cave through a sliding 4KB window. Endless, but
singular: there is exactly ONE cave, forever. Past mastery every run replays the
same layout, echo bands cycle the same three section looks, and score-as-depth
converges on route memorization — the arcade loop's replay value has a ceiling the
architecture no longer requires.

## Idea

Thread a **run seed** through the pure row functions (phase/feature/waveform
offsets keyed by seed): one small parameter, multiplicative content. Unlocks in
rising order of ambition — seed shown on the death card and enterable on the title
screen (share a brutal cave with a friend), per-seed BEST in the existing SRAM
save, and a daily seed for a comparable community score. Determinism is preserved
per seed, so the entire proof harness keeps working: the canonical and deep-run
replays pin seed 0 (today's cave, byte-identical), and CI optionally adds one
assert on a second seed to prove divergence. Sequencing is explicit: this is
**new scope**, and the lane's ⚑ says new Lumen Drift scope needs owner say-so —
this capture exists so the "keep investing" arm of the pick is a concrete option,
not a blank. If the itch.io publish happens (venture-lab capture,
[`games-adjacent-candidate-three-2026-07-10.md`](../venture-lab/games-adjacent-candidate-three-2026-07-10.md)),
daily seeds are the natural retention hook for a PWYW listing.

## Grounding

- The pure-function rewrite that makes this nearly free ("every row is a pure
  function of the world row … endless deterministic cave"; rows 0-61 byte-identical
  to the committed layout): lane
  [`control/status.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/control/status.md)
  and PR #23 row in
  [`docs/review-queue.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/review-queue.md)
  (the same row warns any edit to `layout_of_row`/`row_solid`/`row_features`
  rewrites the whole cave — a seed parameter is the disciplined way to vary them).
- New-scope gate ("keep investing in Lumen Drift (new scope needs owner say-so)"):
  ⚑ needs-owner in the same status pin.
- SRAM save slot + title screen already exist to carry per-seed BEST and seed
  entry: concept-doc polish-pass-1 entry,
  [`docs/concepts/session-1-concepts.md` @ `bc73da7`](https://raw.githubusercontent.com/menno420/gba-homebrew/bc73da70b5e46995dc63319cfd4b3bf997a886c9/docs/concepts/session-1-concepts.md).

**Why now:** the owner is about to make the concept pick — the fork's
"more Lumen Drift" arm should name its best concrete option before he chooses,
and the PR #23 architecture is the moment this became a small change instead of a
rewrite.

## Probe report (v0, 2026-07-11)

*Probed 2026-07-11T09:37Z, single-pass battery. Live-state verification FIRST: lane
HEAD is `c7592d6` (`git ls-remote` 09:29:21Z; read via a blobless clone at the pin —
the lane moved a LOT since the capture pin `bc73da7`: session-8 slices 1–6 plus kit
upgrades v1.8.0→v1.10.0, lane PRs #28–#37). NOT overtaken — no run seed exists
anywhere at HEAD: stem-greps (`seed`, `daily`, `share`) across `games/`, `tools/`,
`docs/`, `control/` hit only the build-time asset-generator LCGs
(`games/lumen-drift/audio/generate_audio.py:26`,
`games/lumen-drift/graphics/generate_assets.py:60` — compile-time, not run-time) and
one false friend read in the body per the stem-grep rule (`gl_run_state.h:44` "Seed
the best score" = SRAM best-score load, no cave seed). Lane inbox @ `c7592d6` carries
ORDERs 001/002/003 only — nothing seed-shaped; no new-scope ruling has landed: the
concept pick is STILL the lane's top ⚑ ("The menu is WITH THE OWNER; slices 4–6
executed the coordinator's announced default (deepen Lumen Drift). An explicit pick
still gates the remaining sessions" — lane `control/status.md` @ `c7592d6`), and the
lane self-reports IDLE on it ("the local backlog is now empty or owner-gated …
genuinely gated on the owner's concept pick rather than on unfinished work"). Premise
mutation recorded honestly: the capture's "echo bands cycle the same three section
looks" half is PARTIALLY overtaken — v1.1 "the echoes deepen" added depth tiers
(crystal step shrinks per 60-row cycle, gallery echoes tighten from tier 2, plateau
tier 3 at row 244; rows 0–123 cell-for-cell identical to v1.0), so difficulty-flatness
is fixed — but the SINGULARITY half is fully intact: there is still exactly ONE cave,
and the lane's own v1.3 route-recorder promotion proves the memorization ceiling
mechanically (`tools/route-recorder.py` autopilots the committed cave and regenerated
the committed tier-run keys byte-identically — a singular cave is literally
scriptable). Sibling-head outcome noted for the index: the play-kit park was
LANE-SELF-SERVED (slice 3, lane PR #31 `41708da`: committed `dist/lumen-drift.gba` +
`docs/PLAYING.md`, CI sha256 per ORDER 000) — the sixth lane-self-served datapoint
class, and it matters here: the dist/play-doc surface a seed-share UX would document
on now exists.*

**1. What is this really?**
One parameter that converts the architecture's determinism from a single artifact
into a family generator. Polish pass 3 made every row a pure function of the world
row; a run seed makes the cave a pure function OF something — same guarantees, ×2^32
content. Product-wise it is the replay-value multiplier plus a social surface (share
a brutal cave by code, daily challenge, per-seed BEST) at near-zero content cost.
Strategically it is the pick enabler: the owner's concept-pick fork has a "keep
investing in Lumen Drift" arm, and this head exists so that arm names a concrete,
costed, provable option instead of a blank — which is why it must be probed before
the sitting and built only after the pick.

**2. What is the possibility space?**
Four axes. **Seed scope:** whole-cave keyed with seed 0 = identity (offsets all zero
⇒ today's cave byte-identical, every committed replay untouched) vs echoes-only
(rows 64+; authored intro always fixed) — whole-cave-with-identity dominates: simpler
lockstep, and the intro is protected by the identity property anyway. **What the seed
keys:** phase offsets into the existing wave tables (`wave_a`/`wave_b` index offsets
in `layout_of_row`), per-band section-look permutation, crystal-step phase, blob/
pillar modulus phases — phase offsets first (smallest diff, preserves the tables'
smoothness bounds), look-permutation as a later rung. **UX rungs (rising ambition):**
seed on the death card → title-screen seed entry (D-pad digits + A, one-button-family
friendly) → per-seed BEST in SRAM → daily seed. Honest wrinkle found here: GBA carts
have no reliable RTC, so "daily seed" on-device is impossible — the daily is a
PUBLISHED CODE (the itch.io listing page or README carries today's code; the player
types it), which still works and still drives the retention loop, but it is a
distribution feature, not a cartridge feature. **Proof depth:** CI second-seed
divergence assert (the capture's floor) → full-period `check-cave.py` scan per
featured seed → an N-seed passability smoke sweep (host python, seconds per seed).

**3. What is the most advanced capability reachable by the simplest implementation?**
A single u32 threaded as index offsets through `layout_of_row`/`row_solid`/
`row_features`, mirrored in the two host tools, buys structurally-guaranteed-playable
infinite caves — not just different ones. The load-bearing find of this probe: the
row #23 junction guard (slice 3 fix, `main.cpp` `row_features` docstring) is
CONSTRUCTIVE and pure-per-row — each crystal cell is kept only if a crystal-free
shared-open column survives toward BOTH neighbours — so the crystal-death-gate class
that cost the lane its 126-gate audit cannot recur under ANY seed, by construction
rather than by testing. Layout passability is then the only per-seed question, and
`tools/check-cave.py` (the committed lockstep mirror, full-period rows 0..20405 scan
already run per-PR) answers it for pennies per seed. And v1.3's route-recorder
promotion means per-seed replay proofs are now CHEAP TO RECORD (`route-recorder.py
<depth> <frames> OUT` regenerates key files deterministically) — the harness cost of
proving a second seed dropped to near zero since capture. Seed 0 = identity keeps the
canonical and deep-run replays byte-identical, so the entire existing proof estate
survives untouched.

**4. What breaks it?**
- **The lockstep TRIPLE.** At capture there were two surfaces to keep in sync
  (`main.cpp` + `check-cave.py`); v1.3 added a third (`route-recorder.py` plans
  corridors from the same pure layout, "keep them in lockstep" per its own header).
  All three must take the seed or CI proofs silently lie about a different cave than
  the ROM renders. Mitigation is the identity property plus the existing
  byte-identical replay asserts — a missed surface reds immediately on seed 0.
- **Layout pinches under arbitrary seeds.** The echoes' band-transition guarantee
  ("adjacent centers differ by at most 3 columns") is a property of the FIXED tables
  and their strides; independently offsetting `wave_a` vs `wave_b` phases preserves
  table smoothness but not necessarily every band-boundary alignment (the deep's +8
  phase offset exists precisely to line a passage up). Verdict-relevant but not
  fatal: `check-cave.py --seed` scans a featured seed's full period in seconds; the
  slice ships a sweep, and an unlucky seed can simply be rejected at entry
  (seed-validation rule) rather than engineered around.
- **SRAM keyspace.** Per-seed BEST over a u32 space cannot be a table of everything;
  the honest v1 is BEST-per-seed for the LAST N seeds played (small LRU) or daily +
  overall only. The `gl_save.h` magic-tag convention (`LDRIFT1` → `LDRIFT2`) makes
  the schema bump safe — old saves read as fresh — but the play doc must say so.
- **The daily-seed RTC wall** (no clock on cart) — see Q2; a published-code daily is
  the honest design, and it lives with the venture-lab listing, not in this slice.
- **The gate itself.** Building this before the pick would burn the lane's own ⚑
  discipline (slices 4–6 deepened under an announced default, but the lane then
  deliberately IDLED rather than invent scope — the gate is real, live, and correct).
  This is sequencing, not technical risk: the probe's job is to have the option
  costed for the sitting, not to jump it.

**5. What does it unlock?**
Replay value past the route-memorization ceiling the lane's own autopilot proves
exists (Q3). The natural retention hook for the venture-lab PWYW listing
(cross-link: `ideas/venture-lab/games-adjacent-candidate-three-2026-07-10.md`) —
shared seed codes and a published daily give an itch.io page a reason to be revisited,
and the listing page is exactly where the daily code lives (Q2's RTC finding makes
these two ideas MORE coupled than the capture knew). The concept pick's "keep
investing" arm becomes a real option with a real cost (one lane PR) and a real proof
story. Fleet-pattern value: determinism-as-content-multiplier — any lane that makes
its world a pure function gets a seed parameter nearly free.

**6. What does it depend on?**
- **The owner concept pick** — the hard gate, verified still open at `c7592d6`;
  expected at the EAP sitting (window ends 2026-07-14). Decays gracefully: if the
  pick goes to Clockwork Courier or Shoal, this head stays parked as the documented
  road-not-taken; nothing rots.
- Lane toolchain/CI health — pinned toolchain (checksum manifest), reproducible
  build re-proven at slice 6 (baseline sha256 reproduced before any change), all
  replay tiers green at the pin.
- No cross-lane build dependency: everything it touches lives in
  `menno420/gba-homebrew` (`main.cpp`, both mirror tools, `gl_save.h`, CI workflows,
  `docs/PLAYING.md`). Downstream co-consumer, not dependency: venture-lab's listing
  consumes the daily-code surface post-EAP behind the owner's itch.io clicks.

**7. Which lane should build it?**
`menno420/gba-homebrew`, alone — it owns the row functions, all three lockstep
surfaces, the SRAM helper, and the replay-tier CI the identity property leans on;
this repo cannot write lane files (Q-0260). NOT sim-lab: the one empirical question
(are seeded caves passable/fair?) is exactly the shape the lane already self-serves —
`check-cave.py` is a committed host-side mirror that scans a seed's full period in
seconds, so the evidence is the lane's own CI red/green (the #114 precedent; same
family as the mineverse shim-replay harness park, #102). A simulator would reproduce
the lane's own tool, slower, with less authority.

**8. What is the smallest shippable slice?**
ONE lane PR, strictly post-pick: (1) u32 `run_seed` threaded as index offsets through
`layout_of_row`/`row_solid`/`row_features`, seed 0 ⇒ all offsets 0 ⇒ byte-identical
(all committed replays and pixel asserts untouched by construction); (2) the same
parameter added to BOTH host mirrors (`check-cave.py --seed`, `route-recorder.py`
seed arg) — the lockstep triple moves together or the PR does not merge; (3) CI
gains three cheap steps: a second-seed divergence assert (two seeds, different keys
line), a full-period `check-cave.py` scan on one pinned nonzero seed, and a ~64-seed
passability smoke sweep (host python, report-only fraction); (4) death card shows
the seed, title screen enters it (D-pad digit entry, A to confirm, default = last
seed); (5) `docs/PLAYING.md` gains the seed section. Per-seed BEST (SRAM schema
bump) and the published-daily convention are rung 2 — named, deferred, not in the
slice. Done-when: existing tiers green UNCHANGED + the three new steps green +
play-doc updated.

**Recommendation: park** — build-direct, owner-gated new scope: the concept pick
(the lane's top ⚑, verified open at `c7592d6`) is the explicit gate, this head is
now the pick's "keep investing in Lumen Drift" arm fully costed for the ≤2026-07-14
EAP sitting, and nothing here is sim-shaped — the only empirical question, per-seed
passability, is self-served by the lane's own `check-cave.py` mirror in its own CI.
