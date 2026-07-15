# The archive roll that cannot save the file: mandatory pointer stubs turn the 200KB rollover threshold into a ~233-proposal countdown, and the obvious fix only buys 2.9× because the roll receipts are a second tombstone family

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS rotation slot, round 13 OPENER; the slot's SECOND tap of fleet-manager after P037 → V048, disclosed: P037 priced the review-queue row-trigger threshold, this head prices the outbox rollover convention — zero shared fixtures, no compaction content anywhere in P037)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab or fleet-manager files)
> **Grounding:** https://github.com/menno420/idea-engine@256ea5c910d1d18856e0570cf3c8766685e7cde6 · fetched 2026-07-15T04:40:18Z
> (HEAD of this repo — the priced convention is quoted VERBATIM in this tree's own `control/outbox.md` ROLLOVER 001 block and every model constant below is measured from the live bus file at this pin, then pinned as a clean constant in this file; sim-lab READ-ONLY at origin/main aa8627e for the dedup ledger + seed sweep only; zero repo/network reads at verdict time — the hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation); round 12 closed fully served — P061 fleet (#408), P062 venture (#410), P063 game mechanics (#419), P064 unrelated closer (#427) — so round 13 OPENS at fleet backlogs, per the rule-3 cycle AND the slot's spacing-4 history (P019, P021, P025, P029, P033, P037, P041, P045, P049, P053, P057, P061 → P065). The walkthrough §E baton "round 13 opens at the fleet-backlogs rotation slot" is now CORRECT arithmetic — P064 flagged and served the miscounted round-12 unrelated closer; this head consumes the corrected baton.

**Placement note (decide-and-flag):** homed in `ideas/fleet/` per the check_sections
carve-out for cross-cutting/manager-layer heads — the P037 precedent exactly (the
slot's first fleet-manager tap also lived here); flagged rather than silently
squatting in a lane section.

## The folk belief

"A threshold-triggered archive roll keeps a live append-only file bounded forever:
when the file gets big, move the finished entries to an archive and leave pointer
stubs behind — the file shrinks, numbering stays stable, repeat as needed." The
committed form (fm `docs/conventions/outbox-rollover.md`, quoted verbatim in this
repo's `control/outbox.md` ROLLOVER 001 block, 2026-07-14T04:43:16Z): "**200KB
threshold · terminal-blocks-only · dated archive files · mandatory pointer stubs ·
content-stable numbering**", executed here once already (PROPOSALs 001–057 rolled
byte-faithful to `control/outbox-archive-2026-07-14.md`, each leaving a
heading+target+idea-link stub; pre-roll file 546,027 B). The reading treats the
roll as a thermostat: whenever the file exceeds 200KB, rolling brings it back
down, so the live file stays small no matter how long the pipeline runs.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

The thermostat reading fails on its own arithmetic, and the failure has a clean
shape: **a compaction policy whose evictions leave mandatory per-item tombstones
is a counter, not a thermostat.** Every roll converts each evicted full block
(b bytes) into a pointer stub (s bytes) that never leaves the live file — the
convention's own "content-stable numbering" clause REQUIRES the stub to stay — and
appends the roll's own receipt (the ROLLOVER block, h_r bytes), which also never
leaves. So the post-roll floor F_k = H0 + k·h_r + s·n_k + (pending window) rises
monotonically with every roll: reclaim per evicted block is b − s once, but the
s survives forever. Three consequences, each exactly computable in integer bytes:
(1) **geometric thrash** — the spacing between rolls, Δ_k = ceil((T − F_k)/b),
is non-increasing and decays until every single appended proposal triggers its own
roll; (2) **the wall** — a computable saturation point N* where even rolling after
every append cannot bring the file under the threshold: the roll fires and the
file is STILL ≥ T (at the measured constants, N* = 233 proposals — the pipeline
is at 64); (3) **the fix that underdelivers** — the obvious repair, ONE range stub
per roll ("PROPOSAL 001–057 rolled → archive §…") instead of 57 per-block stubs,
multiplies capacity only 2.88× (wall 671), because the per-roll RECEIPTS are a
second tombstone family: at saturation they are 24.8% of the wall mass, and under
the range policy they become the binding family. True boundedness needs the
receipt chain compacted too — let each roll's receipt SUPERSEDE the previous
(newest receipt names the full archived span) — and then the floor pins at a
constant H0 + h_r + s + W·b = 34,030 B exactly, forever. Drafting found three
hand-provable structure theorems the sim must confirm as gates: **FLOOR LAW**
(the post-roll size has the exact closed form above — and it is roll-TIMING
independent: rolling late or on any schedule yields the same post-roll size at
the same terminal set, which is what makes the wall robust to the fact that real
rolls are order-fired, not threshold-fired); **RECEIPT-FREE INVARIANCE** (with
h_r = 0 and W = 0 the wall is N* = ceil((T − H0)/s) EXACTLY — identical across
the entire block-size grid: how BIG proposals are sets the roll count and the
approach speed, never the wall; block-size discipline cannot buy capacity);
**COMPACT BOUNDEDNESS** (under the receipt-superseding range policy the floor is
a constant and the spacing is a constant — the file never saturates). The wall is
not volume-born, it is policy-born: the archive layer absorbs unbounded bytes by
design (dated archive files), and only the tombstone grammar decides whether the
LIVE file is bounded.

## Pinned model (measured at HEAD 256ea5c, then pinned as clean constants — all integer bytes, exact arithmetic)

- Live file = header H0 + roll receipts + stubs + full blocks. H0 = 500
  (measured 456). Threshold T ∈ {102400, 204800, 409600}, decision cell 204800
  (the committed "200KB" read as KiB; the 200,000-decimal reading lands N* = 224 —
  immaterial to every band, disclosed).
- Full proposal block b ∈ {8000, 16000, 24000}, decision cell 16000 (measured
  P058–P064: mean 16,212, min 8,168, max 19,263).
- Pointer stub s ∈ {265, 530, 1060}, decision cell 530 (measured 57 live stubs:
  mean 529.9, min 517, max 543). The s grid prices the STUB GRAMMAR: 265 ≈
  heading+target only, 530 = the committed heading+target+idea-URL, 1060 ≈ a stub
  that also quotes the summary line.
- Roll receipt h_r = 1000 per roll (measured ROLLOVER 001 = 1,002 B); appended to
  the live file at every roll (the committed shape — ROLLOVER 001 lives in the
  live outbox).
- Pending window W ∈ {0, 2, 8}, decision cell 2: the newest W blocks are
  non-terminal (verdict pending) and stay full through a roll ("terminal-blocks-
  only"). Roll 1 kept exactly one (P058); ORDER 003's ≥1-in-flight duty with the
  WIP-3 cap bounds normal operation at 1–3; 8 is the verdict-lag stress cell.
- Process: proposals append one full block each; a roll fires at the first append
  that makes the file ≥ T; the roll evicts every terminal full block (all but the
  newest W), appends its receipt, and per policy leaves: **P-STUB** (committed —
  one pointer stub per evicted block), **P-RANGE** (one range stub per roll),
  **P-COMPACT** (one range stub per roll AND the receipt chain collapsed to the
  newest receipt). SATURATION: post-roll size ≥ T. N* = total proposals appended
  at saturation.
- Metrics, all exact integers/rationals: the floor series F_k, the spacing series
  Δ_k with the collapse index (first roll with Δ ≤ 2), roll count K, N*(policy,
  cell) over the full {T × s × b × W} grid, the range multiplier N*_range/N*_stub,
  the wall composition (stub mass / receipt mass / window mass / header at
  saturation), the timing-invariance check, and reporting-only wall-date
  arithmetic at the observed pipeline pace.
- Arm A (the DECISION arm, seedless): the exact integer recurrence — Δ_k =
  ceil((T − F_k)/b), floor update per policy — over the full grid; byte-identical
  across process runs, stdlib only, seconds.
- Arm B (twin, seedless, INDEPENDENTLY-WRITTEN): a literal byte-ledger simulator —
  an actual list of (block, size, terminal-state) records appended, scanned, and
  rolled — must reproduce every Arm-A number EXACTLY, including every floor and
  spacing entry.
- Arm R (seeded, REPORTING-ONLY): block sizes drawn per proposal from the pinned
  mix {8000: 1/4, 16000: 1/2, 24000: 1/4} (mean exactly 16000); 10,000 process
  replications on `random.Random(20261567)` (one uniform per appended proposal,
  draw counts counted and asserted), reporting the wall DISTRIBUTION beside the
  deterministic wall; stability leg `random.Random(20261568)` at 2,000;
  presentation shuffle 20261569. NO statistical gate rides Arm R — a mix-induced
  drift from the deterministic wall is a named finding, never a ruling.
- Aux seed: 20261570, reserved, never read by any leg (the P054–P064 aux
  convention).
- Seeds 20261567–570 strictly above the tree high-water 20261566 (P064's
  registration) and the sim-lab genuine high-water 20261562 (V074's 20261559–62);
  boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree
  at HEAD 256ea5c (max genuine 20261566) and the sim-lab clone READ-ONLY at
  origin/main aa8627e (max genuine 20261562) — the larger standalone numerals
  (20261833, 202670087, and sim-lab results.json digit runs, e.g. 2026964142) are
  the documented Fraction-numerator / decimal-fraction data-not-seed specimens;
  the P046–P064 sweep-recipe trap re-confirmed.

## Pre-registered decision rule (evaluation order: REJECT first)

All decision clauses read the decision cell (P-STUB, T = 204800, s = 530,
b = 16000, W = 2, h_r = 1000, H0 = 500) unless a policy is named.

- **REJECT** — "the committed mandatory-pointer-stub rollover is not a
  bounded-live-file rule — it is a finite counter: every roll raises the floor,
  the threshold is a countdown with a wall at pipeline scale, thrash precedes the
  wall, and the obvious range-stub fix underdelivers because the roll receipts
  are a second tombstone family": N*_stub ≤ 300, AND the thrash regime is real
  (≥ 8 pre-saturation rolls have spacing ≤ 2), AND the fix underdelivers —
  N*_range ≤ 4 × N*_stub exact — while P-COMPACT holds a CONSTANT floor over
  100,000 appends (the wall is policy-born, not volume-born). (Checked FIRST
  because the costly direction is fleet-wide: every bounded-live-surface
  convention that compacts by leaving per-item pointers — outbox rolls, heartbeat
  upkeep lists, review-queue rows with per-row markers, session-card indexes —
  inherits the counter, and codifying "roll when big" as a boundedness guarantee
  ships a silent capacity wall into each one.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure
  below.
- **APPROVE** — "the convention is effectively bounded at pipeline scale — the
  wall sits beyond any plausible horizon and roll cadence stays comfortable":
  N*_stub ≥ 500 AND every one of the first 20 spacings ≥ 4. (Mutually exclusive
  with REJECT via 300 vs 500 on the same exact integer.)
- **NULL** — anything else; pre-registered axes: band-straddle (N*_stub ∈ (300,
  500), or the thrash clause alone fails, or the multiplier clause alone fails —
  the finding is the exact floor/spacing curves and the wall table); an
  invariance-theorem failure without gate failure (the drafter's receipt algebra
  is wrong — the corrected law is the finding); P-COMPACT saturating (same shape
  — the corrected boundedness condition is the finding); twin-arm disagreement
  surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067
lesson, applied): the sim is FULLY DETERMINISTIC — every decision clause and every
F-gate is an exact integer identity, structural assertion, or byte comparison; the
only seeded arm is reporting-only with NO statistical gate (its sole gates are the
draw-count sentinel and exact reproducibility, pass probability 1 for a correct
implementation); JOINT pass probability across all gates for a correct
implementation = 1 EXACTLY (the P059–P064 no-stochastic-gate precedent:
determinism proven by byte-identical re-run, not estimated), and decision
separation is noise-free exact arithmetic — the disclosed landing clears the N*
band at 1.29×, the thrash band at 2.25× (18 rolls vs 8), and the multiplier band
at 1.39× (2.88 vs 4), so the ruling cannot move except via a mis-implemented
model, which the anchor gates catch as INVALID.

## Gates (run INVALID on any failure)

- **F1 — model & mechanism identities:** conservation (proposals appended =
  stubbed + archived-window + live at every step); the spacing identity Δ_k =
  ceil((T − F_k)/b) re-derived by the literal event walk; the floor law F_k =
  H0 + k·h_r + s·n_k + Σ(newest W blocks) at EVERY roll under P-STUB (and its
  P-RANGE/P-COMPACT forms: s·k and s + h_r constant respectively); file size ==
  sum of parts, exact, at every append.
- **F2 — the three structure theorems, exact:** (a) FLOOR LAW timing invariance —
  an alternate pinned schedule (roll every 25 appends regardless of size) yields
  the SAME post-roll size at the same terminal set, every comparison exact;
  (b) RECEIPT-FREE INVARIANCE — at h_r = 0, W = 0 the wall equals
  ceil((T − H0)/s) = 386 and is IDENTICAL across the whole b grid {8000, 16000,
  24000}; (c) COMPACT BOUNDEDNESS — under P-COMPACT the floor is the constant
  H0 + h_r + s + W·b = 34,030 and the spacing is constant 11, held over 100,000
  appends. Plus MONOTONE THRASH: F_k strictly increasing and Δ_k non-increasing
  under P-STUB at every grid cell.
- **F3 — closed-form anchors (decision cell):** N*_stub = 233 with K = 51 rolls;
  first spacing 13 = ceil((204800 − 32500)/16000); first floor 39,330 =
  500 + 1000 + 530·11 + 32000; collapse index 34 (the first spacing ≤ 2; rolls
  34–51 all have Δ ≤ 2, count 18); saturation floor 205,930 with the exact wall
  composition — stub mass 122,430 (59.4%), receipts 51,000 (24.8%), window
  32,000 (15.5%), header 500; N*_range = 671 (multiplier 671/233 ≈ 2.88);
  P-COMPACT floor 34,030.
- **F4 — the hand world:** T = 100, H0 = 10, h_r = 5, s = 2, b = 20, W = 1 →
  N* = 18, K = 8, spacings (5, 3, 3, 2, 2, 1, 1, 1), floors (43, 54, 65, 74, 83,
  90, 97, 104) — walked by pencil.
- **F5 — degeneracies:** s = b = 16000 (stubs as big as blocks — compaction
  reclaims nothing but the window): N* = 13 at the decision cell's other
  constants; s = 0 AND h_r = 0 (true deletion): no saturation in 100,000 appends,
  floor constant H0 + W·b = 32,500.
- **F6 — battery:** Arm B reproduces every Arm-A number exactly (every wall,
  every floor entry, every spacing entry, every composition row); twin
  independently-written decision evaluators agree on the ruling token; Arm-R
  draw-count sentinels (1 uniform per appended proposal) counted and asserted;
  aux seed 20261570 never read; stdout + results.json byte-identical across two
  process runs (Arms A/B platform-independent integers; Arm R pinned to a stated
  CPython minor).

## Expected landing (DISCLOSED per the P048–P064 closed-form-arm norm)

REJECT, at the drafter's exact prototype values (the sim re-derives everything
from scratch and must not trust these): decision cell — N*_stub = **233**
proposals (the pipeline is at 64), K = 51 rolls, spacing 13 → 1 with collapse at
roll 34 (proposal ≈ 208), 18 rolls in the Δ ≤ 2 thrash regime (≥ 8, 2.25×);
saturation floor 205,930 with composition stub/receipt/window/header =
59.4% / 24.8% / 15.5% / 0.2%; N*_range = 671, multiplier 2.88 ≤ 4 (1.39×);
P-COMPACT floor constant 34,030 with spacing constant 11 over 100,000 appends.
Full stub-policy wall table N*(W, b): W = 0 → 318 / 283 / 258 across b = 8000 /
16000 / 24000; W = 2 → 292 / 233 / 187; W = 8 → 215 / 92 / 17 (a verdict-lag
stall at fat blocks saturates almost immediately — the W·b window mass eats the
whole threshold). s grid at the cell: 265 → 369, 530 → 233, 1060 → 136. T grid:
102400 → 76, 204800 → 233, 409600 → 581. Receipt-free invariant wall: 386 across
the entire b grid. Falsifiability is real on every clause: the T = 409600 cell
lands N* = 581 ≥ 500 with all first-20 spacings ≥ 12 — one grid step up the
threshold lands APPROVE outright; the W = 0, b = 8000 corner (318), the
halved-stub cell (369), and the doubled-threshold-adjacent readings sit in the
(300, 500) straddle — one grid step in three different directions lands NULL; and
APPROVE at the decision cell itself was arithmetically live until the stubs were
MEASURED (a heading-only ~150 B stub grammar, which the convention could have
chosen, lands N* = 504 ≥ 500 — the committed heading+target+idea-URL stub at
530 B is what puts the wall inside pipeline scale). Disclosed sharpenings,
reporting-only: at the observed pipeline pace (63 proposal intervals over 4.43
days ≈ 14.2/day) the decision-cell wall dates to ≈ 2026-07-27 — inside the
extended EAP's own operating horizon plus days, a date, not a risk class; the
model retrodicts the live file's post-roll-1 state (k = 1, n = 57, W = 2 → floor
63,710 vs the measured 154,629 B with SEVEN full blocks and ~9.5 KB of
non-proposal ASK/ACK/CLOSE-OUT blocks — the un-modeled block families and the
five extra pending fulls account for the gap, disclosed as the F1 boundary, and
they only SHRINK real headroom, REJECT-ward); the next-roll forecast — with 57
stubs live, the model puts roll 2 at ≈ 11 post-roll full blocks (the live file
holds 7 at HEAD).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Verdict CONSUMER: **fleet-manager** — owner of `docs/conventions/outbox-rollover.md`
(the 200KB threshold, the mandatory-pointer-stub clause, the roll execution).
APPLICATION GUARD, two conditions: (1) the verdict conditions on the committed
convention shape at the pin (per-block stubs + per-roll live receipts +
terminal-blocks-only) — a changed stub grammar or receipt convention means
re-run, not reuse; (2) it conditions on stub/receipt mass being live-file
resident — an archive-side numbering index changes the model. REJECT →
paste-ready structured choice, recommendation first per Q-0263.2 —
(a, recommended: one convention line, zero migration, removes the wall entirely)
amend the convention: ONE RANGE STUB per roll (the span + archive pointer keeps
content-stable numbering — the archive holds every block byte-faithful) AND each
roll's receipt SUPERSEDES the previous (the newest ROLLOVER block names the full
archived span; the superseded receipt rolls with the next batch) — the measured
floor pins at ≈ 34 KB forever (the COMPACT-BOUNDEDNESS theorem, exact);
(b) keep per-block stubs and accept the counter: schedule the stub-file's own
second-order roll before ≈ 80% of N* — pushes the wall out one level, the same
law recurses on the stub file; (c) raise the threshold — pure postponement, N*
scales ≈ linearly in T (76 / 233 / 581 across the grid) and the countdown
restarts. On EVERY branch the archive layer is untouched and vindicated (dated
archive files absorb unbounded bytes by design — the wall lives only in the live
file's tombstone grammar). APPROVE → the committed convention gains a measured
basis and the wall table ships as capacity documentation. NULL → the named axis
ships with the exact floor/spacing curves. Transfer surface named: every
fleet convention that keeps a bounded live surface by replacing items with
per-item pointers — heartbeat "known upkeep" lists, review-queue rows with
per-row terminal markers, session-card index files, HANDOFF regeneration — the
law is one line: **compaction that leaves per-item tombstones has capacity
(T − H)/s, and compaction whose RECEIPTS live on the compacted surface has a
second wall behind the first; boundedness requires the tombstone AND receipt
grammars to be O(1) per roll, not O(items).**

## Dedup

Tree-wide `rg -i 'rollover|compaction|tombstone|log.structured|garbage.collect|saturat|stub'`
(bootstrap.py/.substrate excluded) at HEAD 256ea5c: every hit is a word collision
or the SUBJECT's own machinery, not a prior pricing — the ROLLOVER 001 block and
ORDER 010 (the convention this head prices, quoted as grounding); "tombstone" in
the check_sections supersede-marker sense (a retired-doc pointer, no mass
accounting); "stub" as code/host-seam stubs and content-free session stubs;
"saturation" only in P055's badge-saturation (idle-game badge thresholds — no
files, no compaction). sim-lab sweep (READ-ONLY at origin/main aa8627e, same
terms): rollover housekeeping session cards (ORDER 005/010 execution — the
machinery again) and code-stub collisions; no verdict prices file growth,
compaction, or tombstone mechanics. No proposal P001–P064 and no verdict
V001–V076 (ledger read FIRSTHAND at aa8627e: finalized through V074 plus the
V075/V076 pair; V077 pending on P064) prices append-only file growth, a
compaction policy, or a capacity wall. Nearest priors argued distinct:
**P061 → V072** (the nearest kin by "committed operational constant priced as a
law" — an order-up-to REFILL rule on a consumable work queue: demand, dryness,
stock-outs; here NOTHING is consumed — the file only grows, there is no demand
process, and the priced object is the boundedness of a compaction policy),
**P019 → V021** (reorder-point SIGNAL tuning — the other inventory family, same
distinction), **P037 → V048** (the same repo's first tap — a row-count
DETECTION/classification threshold on the review queue: when to LOOK, no mass
accounting, no floor dynamics, no wall), **P053 → V064** (healthcheck cadence —
detection of external transients, blind windows; nothing accumulates),
**P025/P029 → V027/V031** (claim expiry/lease renewal — lifetime rules on
individual claims, no aggregate mass), **P052 → V063** (coupon-collector
occupancy — collection completion, not capacity), **P056 → V067** (length-biased
sampling — no growth process). Method kin only: the P059–P064 fully-deterministic
no-stochastic-gate discipline; the literal byte-ledger twin arm and the wall-
composition decomposition are this head's own additions to the battery.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional:
(1) CONSTANT sizes per cell — real blocks vary (measured 8,168–19,263) and real
stubs vary (517–543); Arm R prices the block-size mix and reports the wall
distribution (reporting-only); saturation is MASS-driven, so mixing moves the
wall by far less than one straddle width — direction disclosed, never gated.
(2) THRESHOLD-FIRED rolls — real rolls are order-fired (ORDER 010 fired at
546 KB, 2.7× over threshold); the FLOOR LAW is roll-timing-invariant (F2a), so
the wall is timing-robust and only the thrash cadence is model-conditional —
stated in the landing. (3) PROPOSAL-ONLY traffic — the live file also carries
ASK/ACK/REPORT/CLOSE-OUT blocks (≈ 9.5 KB at HEAD) which the model excludes;
they only shrink headroom, REJECT-ward, direction stated never simulated.
(4) The WINDOW is the newest W blocks — real pending sets can be non-contiguous
(a stalled old verdict); non-contiguity changes which blocks wait, not the
retained mass, and W = 8 prices the stall direction. The RECEIPT-FREE INVARIANCE
theorem is robust to (1): it is a pure mass identity, not a size-distribution
fact.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> sweep at the grounding pin 256ea5c and the sim-lab READ-ONLY sweep at aa8627e
> returned word collisions and the subject's own machinery only (the supersede-
> tombstone sense, code stubs, badge saturation, the ORDER 005/010 rollover
> housekeeping); no proposal P001–P064, verdict V001–V076, idea file, or card 💡
> prices file growth, compaction, or tombstone mechanics; no recorded runner-up
> drop of this domain exists on any card. (b) **kill test NOT triggered** — the
> nearest kin (P061 refill inventory, P037 row-count trigger, P019 low-water
> signal) share surfaces or grammar but zero fixtures and zero mechanism (nothing
> is consumed here; no detection; the priced object is a compaction policy's
> boundedness). (c) **feasibility + liveness arithmetic checked** — runtime
> trivial (exact integer recurrences over a ≤ 81-cell grid plus a 100,000-append
> boundedness walk: seconds, stdlib only); the expected landing is DISCLOSED with
> exact drafting-time values (REJECT, N* = 233 at the decision cell) rather than
> hidden; all four rulings reachable under the pre-registered rule (APPROVE one
> grid step up the T grid at 581; three one-step straddle NULLs named; INVALID on
> the F1–F6 identity/theorem/anchor/degeneracy battery).

**1. What is this really?** A pre-registered exact MEASUREMENT of the folk claim
"a threshold-triggered archive roll keeps the live file bounded", taken on the
fleet's own committed rollover convention (200KB · terminal-blocks-only ·
mandatory pointer stubs · content-stable numbering) at constants measured from
the live bus file: the post-roll floor law, the roll-spacing decay, the
saturation wall N* per policy (committed per-block stubs vs range stub vs
receipt-compacting range stub), and the wall's mass composition — every number an
exact integer, judged against bands fixed before any code (REJECT first:
N* ≤ 300 AND thrash real AND the obvious fix ≤ 4× while true compaction is
bounded; APPROVE: N* ≥ 500 with comfortable cadence; NULL otherwise with named
axes), byte-identical across two runs, with the seeded size-mix arm demoted to
reporting-only.

**2. What is the possibility space?** (i) Don't run it — the wall arrives
unpriced at the pipeline's own pace (the reporting row dates the decision-cell
wall ≈ 2026-07-27; the convention was executed here once and will fire again at
≈ 11 post-roll full blocks). (ii) Wait for the wall and fix it live — pays the
thrash regime first (the last 18 rolls come ≤ 2 proposals apart) and debugs a
convention under churn. (iii) A prose warning ("stubs accumulate, watch the
file") — states a direction, measures nothing, and misses the two quantitative
surprises drafting found: the RECEIPTS are a quarter of the wall (so the obvious
fix underdelivers 2.88× where intuition says ~10×), and block-size discipline
buys literally zero wall (the invariance theorem). (iv) An MC-only sim — leaves
every decision number seed-noisy when the whole object is exact integer
arithmetic (the V065/V067 lesson: the decision arms are seedless recurrences, MC
demoted to reporting). (v) This head: exact wall/floor/spacing tables as the
ruling, REJECT-first bands on the wall + thrash + fix-underdelivery, INVALID on
the identity/theorem/anchor/degeneracy/battery gates, robustness disclosed via
the full W × b × s × T tables with three live straddle edges and a one-step
APPROVE cell. (vi) Over-scope (stochastic verdict-lag processes, non-proposal
block traffic models, archive-side indexing, second-order stub-file rolls) —
each named as boundary or follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~150-line stdlib file: an integer recurrence (Δ_k =
ceil((T − F_k)/b), floor update per policy) — that single kernel yields the
exact wall table over the full grid, the floor/spacing series with the collapse
index, the wall composition, all three structure theorems as THEOREM CHECKS
(timing invariance, receipt-free invariance, compact boundedness), both
degeneracies, and the policy comparison that turns a folk guarantee into a
one-line design law — from a sim a verdict session runs cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **Constant sizes are a
choice** — real block/stub sizes vary; the mix arm reports the wall distribution
and saturation is mass-driven, but a fat-tailed block mix could smear the thrash
onset (never the floor law — it is exact per realized sizes); disclosed as the
F1 boundary. (b) **The model prices proposals only** — ASK/ACK/REPORT traffic
shrinks real headroom; the wall is therefore an UPPER bound on the live file's
real capacity, REJECT-ward, stated. (c) **Band placement could cherry-pick** —
the 300/500 wall bands, the ≥ 8 thrash clause, and the ≤ 4× multiplier are
committed BEFORE the sim, the landing is DISCLOSED (REJECT at 1.29× / 2.25× /
1.39×), and falsifiability is two-sided: T = 409600 lands APPROVE outright,
three adjacent cells land straddle NULL, and APPROVE at the decision cell was
live until the stub grammar was measured (a 150 B heading-only stub lands 504).
(d) **The convention might be read differently** — if fm's rollover doc means
the stubs to live archive-side (not in the live file), the model's stub term
vanishes; the committed EXECUTION here (57 stubs in the live outbox at HEAD,
byte-measured) is the grounding, and the application guard names the re-run
condition. (e) **An arithmetic slip in the drafter's algebra** — the sim
re-derives everything from scratch; all three theorems are F2 gates AND carry
their own theorem-failure-without-gate-failure NULL axes, so a wrong hand proof
becomes a finalized finding (the corrected law), not a silent bad gate.

**5. What does it unlock?** The fleet-backlogs lane's thirteenth slot entry and
the slot's second fleet-manager head; a measured, citable answer to "is the
rollover convention bounded" with a dated wall, delivered ~170 proposals before
it binds; the one-line transferable law (tombstone AND receipt grammars must be
O(1) per roll, not O(items)) for every bounded-live-surface convention in the
fleet — heartbeat upkeep lists, review-queue rows, card indexes; and two
standalone side pins (the wall-composition decomposition showing receipts at
24.8%, and the receipt-free invariance theorem showing block-size discipline
buys zero wall).

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: seedless integer recurrences, seconds. The single
cheapest probe if a reader doubts the mechanism is the receipt-free invariance
by hand: with no receipts and no window, each evicted block leaves s bytes that
never leave, so the floor after stubbing n blocks is H0 + s·n regardless of how
big the blocks were — the file saturates at the first n with H0 + s·n ≥ T,
i.e. N* = ceil((T − H0)/s) = 386 at the pinned constants, three lines of pencil.

**7. What would make this a mistake to run?** If the live file's stubs were not
actually resident (they are — 57 measured at HEAD, 30,204 B of them), if the
domain duplicated a prior head (it does not — the sweep returned collisions and
the subject's own machinery only), or if the disclosed REJECT made the run
theater. It does not: the value is the independent re-derivation of the three
theorems PLUS the parts no hand argument gives — the exact wall table over
{T × s × b × W} (the W = 8 column collapsing to 17 at fat blocks was a
drafting-time surprise), the wall composition that prices the receipt family,
and the exact 2.88× underdelivery of the obvious fix — and both non-REJECT
rulings are genuinely reachable one grid step from the decision cell.

**8. How will we know it worked?** A committed sim-lab report with: the exact
wall table N*(policy, T, s, b, W), the decision-cell floor and spacing series
with the collapse index, the wall-composition row, the three theorem
verifications, the degeneracy rows, the F1–F6 gate results, the verdict token
against the pre-registered bands, Arm R's wall distribution beside the
deterministic wall (reporting-only), and a byte-identity note (two process runs
identical). A clean run reproduces the drafter's disclosed reference values
(N* = 233, K = 51, collapse 34, composition 59.4/24.8/15.5, multiplier 2.88,
compact floor 34,030) from scratch, or — the more interesting outcome —
DISAGREES and pins the drafter's error, which the pre-registered rule then rules
on honestly (the theorem-failure NULL axes exist for exactly that).

**Recommendation: sim-ready**
