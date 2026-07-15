# One knob printed twice: the write contract's two-tier rate limit (burst 10/10 s, sustained 60/min) has equal average rates — the sustained tier is dead ink under every uniform limiter discipline, the burst tier alone over-admits 7/6 of the sustained promise under fixed windows, and which of those two failures you get rides an unstated implementation choice

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot, round 15 opener; harvest source superbot-mineverse, the slot's least-recently-tapped repo source — its only prior fleet-slot tap was P045, round 8, a DIFFERENT document (docs/mining-data-contract.md, the READ contract's staleness constant); P055's game-slot tap (achievements catalog) is also disclosed — zero shared fixtures with either)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits mineverse or superbot files)
> **Grounding:** https://github.com/menno420/superbot-mineverse@b9ade33ae6019eff45195684fa6fd6f02da4bee0 · shallow clone fetched 2026-07-15T09:38:40Z (Q-0272 git transport, read-only)
> (companion firsthand read: menno420/superbot via GitHub code search pinned at ref f8e2313a087e18cb32e88269d468b0b30a41fad9, ~2026-07-15T09:44Z — executor-unbuilt evidence only; dedup-sweep HEADs: idea-engine 412f132, sim-lab 237b24a READ-ONLY (VERDICT 084 newest, fetched 2026-07-15T09:42:37Z). The verdict session is fully hermetic: every constant below is quoted-and-pinned in this file, zero repo/network reads at verdict time — the P017–P072 precedent.)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation); round 14 closed fully served (fleet P069 #432, venture P070 #434, game P071 #435, unrelated P072 #436, merged 2026-07-15T09:19:39Z), so round 15 REOPENS at fleet backlogs. Slot spacing history P061, P065, P069 → P073 (spacing 4) confirms the placement.

## The harvested tension (both horns committed, verbatim)

The mining-action WRITE contract commits a two-tier rate limit
(docs/mining-write-contract.md § Rate limits, lines 159–170 @ `b9ade33`):

> Enforced per `(suid, guild_id)` on the executor side. v1 defaults
> (executor-configurable, but these are the contract's expectations):
> - **Burst**: 10 actions per 10 seconds.
> - **Sustained**: 60 actions per minute.
> Over budget → HTTP 429, `reason_code: "rate_limited"`, plus a `Retry-After`
> header (integer seconds).

Two tiers, one unstated fact: **10/10 s and 60/60 s are the SAME average
rate** — exactly 1 action/second, the identity B·T = S·w = 600 on the
committed integers. And one unstated choice: the contract never says what a
"10 seconds" window IS — sliding, fixed/tumbling, or a token bucket. The
committed reference implementation has already voted, silently and
half-way: the shim — which the contract names as its § Rate limits
executable ("§ Rate limits as an opt-in deterministic mode —
`SHIM_RATE_LIMIT=10/10`", contract line 333, and the shim's own docstring
calls 10/10 "the contract's burst default", shim_bot.py:29) — carries
exactly ONE knob, `rate_limit: tuple[int, float] | None` (shim_bot.py:115),
implemented as a SLIDING window (`_consume_budget`, shim_bot.py:340–366:
eviction `while times and now - times[0] >= window`, line 360; `Retry-After
= max(1, math.ceil(times[0] + window - now))`, line 364). There is no
second knob: the sustained tier exists only as prose. Meanwhile the real
executor — the party the contract binds — is UNBUILT: "to be built in the
superbot repo" (contract line 37), blocked on the owner-side
`MINING_WRITE_ENDPOINT`/`MINING_WRITE_SHARED_SECRET` pair (superbot
docs/eap/night-review-2026-07-13.md @ `f8e2313`). Its discipline choice is
still open — which makes this the cheapest possible moment to price what
the pair of sentences actually means.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Model: slotted integer time (slot δ seconds, δ = 1 pinned primary), a
schedule = arrivals per slot (unbounded non-negative integers — clicks are
instantaneous), admitted = the schedule itself when it satisfies the
limiter (the adversary sends exactly what gets admitted). Three standard
disciplines for one tier (B per w seconds): SLIDING (every w-second span
carries ≤ B admits — the shim's semantics), FIXED (tumbling w-windows,
counter resets at boundaries), BUCKET (capacity B, refill B/w tokens/s,
start full; refill at slot boundaries after the slot, tokens capped — the
endpoint convention is pinned and its sensitivity disclosed below). Let
N_disc(L) = the adversary's maximum admits in any L-second span. Every
numeral below was RAN at drafting (the V084 NO-DERIVED-LITERALS lesson):
closed forms and independently-written DP/greedy/exhaustive twins, exact
agreement everywhere.

**T1 — the DEAD TIER.** At the committed pair (B, w, S, T) = (10, 10 s,
60, 60 s) — equal average rates, w | T — the sustained tier NEVER REJECTS
under any of the three disciplines applied uniformly to both tiers:
- uniform sliding: N_slide(60) = B·⌈60/w⌉ = **60 = S exactly** (the
  partition bound is tight; the counter touches the cap and never crosses —
  a margin-0 contact, registered as a knife-edge);
- uniform aligned-fixed: max admits in an aligned minute = **60 = S
  exactly** (six full sub-windows; a 61st request is rejected by the burst
  tier FIRST — the sustained counter cannot exceed 60 while every 10 s
  sub-window holds ≤ 10);
- uniform token-bucket pair: the sustained bucket (cap 60, refill 1/s)
  under adversarial burst-admissible traffic never drops below **exactly 50
  tokens** (greedy front-load is the minimizer; verified over a 600 s
  horizon) — dead by a 50-token margin.
The second sentence of the contract is dead ink under every uniform
implementation of the first.

**T2 — the FORK.** The burst tier ALONE, implemented under the two leakier
disciplines, breaches the sustained expectation in the worst 60 s span:
- fixed windows, adversarial alignment: N_fixed(60) = B·(⌈59/w⌉ + 1) =
  **70** — excess **7/6** of the sustained promise (≈ 16.7% over);
- token bucket: N_bucket(60) = B + ⌊59·(B/w)⌋ = **69** — excess **23/20**
  (15% over); under the closed-interval endpoint convention the value is
  **70** — the convention pair {69, 70} is disclosed and both sit ≥ the
  21/20 band, so the finding is convention-robust;
- and the classic boundary straddle: a 2-second span across a fixed-window
  boundary carries N_fixed(2) = **20 = 2B** — double the burst intent —
  where sliding allows 10.
So the pair's MEANING forks on the unstated discipline: a sliding executor
makes the sustained line dead ink; a fixed-window or token-bucket executor
that enforces the burst line (the two most common implementations)
under-delivers the sustained promise by 15–16.7% worst-case and doubles
the burst in a straddle. There is no discipline under which both sentences
are simultaneously live and honest.

**T3 — the LATTICE POINT.** The redundancy is exactly boundary-sited: under
sliding, the sustained tier is redundant iff B·⌈T/w⌉ ≤ S, and the committed
pair sits at EQUALITY (60 = 60). One constant-step off the boundary the
structure changes: at S = 50 a separating schedule exists even under
sliding (the witness is six 10-bursts at t = 0, 10, …, 50 — 60 admits > 50,
committed as a fixture); at w = 7 s (10 per 7) the redundancy dies by
divisibility alone (B·⌈60/7⌉ = **90** > 60 — no tier change needed); at
S = 70 the pair goes doubly slack with ANOTHER exact contact (adversarial
fixed 70 = 70). The committed constants are not merely close to the
degenerate configuration — they are ON it, at the corner where w | T and
B·T/w = S both hold.

The drafting surprise that makes this a mechanism head and not a nitpick:
the two failure modes are MUTUALLY EXCLUSIVE and jointly exhaustive over
the standard disciplines — every implementation either wastes the second
sentence or breaks it. The only reading under which the sustained line does
work is CROSS-discipline (policing a burst tier implemented leakier than
the reader assumed) — and that reading is exactly what a conformance
fixture can encode: the 70-in-60 witness schedule, run against the real
executor, distinguishes sliding from fixed/bucket in one probe.

## Pinned model (committed constants — grounded + invented-but-pinned, exact)

- Committed constants (verbatim @ `b9ade33`): B = 10 per w = 10 s (burst),
  S = 60 per T = 60 s (sustained), docs/mining-write-contract.md:164–165;
  429 + `Retry-After` integer seconds, :167–168; the shim's sliding
  eviction and Retry-After formula, shim_bot.py:360, 364; the shim's
  single-knob signature, shim_bot.py:115.
- Slotted time, slot δ ∈ {1, 1/2, 1/5} s (δ = 1 primary; the maxima triple
  must be invariant across the three — drafting: (60, 70, 69) at all
  three); arrivals per slot unbounded; admitted = schedule under the
  limiter constraint.
- Disciplines: SLIDING (every w-span ≤ B), FIXED-ALIGNED (tumbling grid
  anchored at 0), FIXED-ADVERSARIAL (alignment chosen by the adversary),
  BUCKET (cap B, refill B/w per second applied at slot boundaries after
  the slot, capped, start full; the closed-interval convention as a
  disclosed reporting exhibit).
- Grids: (B, w) ∈ {(10, 10), (10, 7), (5, 10), (20, 10)} × S ∈ {50, 60,
  70, 100} at T = 60; span lengths L ∈ {2, 10, 60, 120} for the maxima
  tables. Decision cell: the committed (10, 10, 60, 60).
- Arm A (DECISION arm, seedless): the closed forms N_slide(L) = B·⌈L/w⌉,
  N_fixed_adv(L) = B·(⌈(L−1)/w⌉ + 1), N_fixed_aligned(L) = B·⌈L/w⌉ (w | L),
  N_bucket(L) = B + ⌊(L/δ − 1)·(B/w)·δ⌋, all exact integers/Fractions; the
  T1 dead-tier checks (the two equality contacts + the exact bucket
  min-level 50); the T3 redundancy law and the separating-schedule triple.
  Byte-identical across process runs.
- Arm B (twin, seedless, INDEPENDENTLY WRITTEN): DP/greedy maxima over
  slotted schedules per discipline with alignment enumerated; an EXHAUSTIVE
  search on five small worlds ((L, w, B) ∈ {(6,2,2), (7,3,2), (5,5,3),
  (8,4,1), (9,3,3)} — drafting: closed form exact on all five); the
  bucket-pair minimum-level trace; independent separating-schedule search.
  Must equal every Arm-A number exactly.
- Arm R (seeded, REPORTING-ONLY): Poisson click streams (offered rate 2/s,
  exponential gaps) through a VERBATIM re-implementation of the shim's
  `_consume_budget` (deque + eviction + Retry-After formula); per-trace
  theorem check (worst trailing 60 s admitted-window ≤ 60 — drafting: both
  seeds touch 60 EXACTLY); the obedient Retry-After client (retry exactly
  at the header value — drafting: exactly 3600 admits in 3600 s, long-run
  rate exactly 1/s = the sustained rate). Main `random.Random(20261650)`
  (50,000 events), stability `random.Random(20261651)` (20,000),
  presentation shuffle 20261652. Draw counts asserted. NO statistical gate
  rides Arm R — the decision lives entirely in the exact seedless arms.
- Aux seed: 20261653, reserved, never read by any leg (the P054–P072 aux
  convention).
- Seeds 20261650–653 allocated from 20261650 per the coordinator relay:
  20261640–643 are P072/V085's registered set and the gap 20261644–649 is
  the disclosed in-flight buffer, so 20261650 is the next free index —
  strictly above both. Boundary-aware sweep — regex
  `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD 412f132 maxes
  at genuine 20261643, and the sim-lab clone READ-ONLY at 237b24a maxes at
  genuine 20261633 (V084's 20261630–633); the standalone numerals 20261664
  / 20261833 / 202670087 / 2026964142 are digit-substrings (Fraction
  numerators, results-JSON decimals), data not seeds — the P046–P072
  sweep-recipe trap re-confirmed.
- Print discipline (the P071 hazard, inherited): every registered quantity
  here is a small integer or small Fraction — no large-rank hazard — but
  the fixture still gates by in-memory equality first and prints second,
  per the pinned practice.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the committed tier pair is DEGENERATE: one knob printed
  twice — under every uniform discipline the sustained tier is dead ink,
  under the two leakier disciplines the burst tier alone breaks the
  sustained promise, and the committed constants sit exactly on the
  redundancy boundary — so the contract must pin the discipline and either
  derive or move the second tier": **(R1, dead tier)** no separating
  schedule exists at the committed pair under sliding (N_slide(60) ≤ S,
  exhaustive-and-closed-form) AND all three uniform-discipline dead checks
  hold with their exact contacts (sliding 60 = S, aligned-fixed 60 = S,
  bucket min level = 50 ≥ 1); **(R2, fork)** N_fixed_adv(60)/S ≥ 21/20 AND
  N_bucket(60)/S ≥ 21/20 (both endpoint conventions) AND the straddle
  N_fixed_adv(2) = 2B exactly; **(R3, lattice)** B·T = S·w exactly AND a
  separating schedule EXISTS at S = 50 under sliding AND N_slide(60) > S
  in the w = 7 world. (Checked FIRST because the costly direction is live
  NOW: the real executor is unbuilt and its author will read two sentences
  that cannot both be doing work — the fork ships silently in whichever
  discipline the builder happens to pick.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate
  failure below.
- **APPROVE** — "the sustained tier is a live, discipline-robust second
  knob": a separating schedule exists under sliding at the committed pair
  OR (N_fixed_adv(60) ≤ S AND N_bucket(60) ≤ S). (Mutually exclusive with
  REJECT by arithmetic on both clauses.)
- **NULL** — anything else; pre-registered axes: **band-straddle** (exactly
  one of fixed/bucket clears 21/20 — the finding is the exact maxima table
  with the binding discipline named); **law failure without gate failure**
  (a closed form disagrees with its DP twin outside the small worlds — the
  drafter's formula is wrong and the corrected law is the finding);
  **convention fragility** (the granularity triple {1, 1/2, 1/5} or the
  bucket endpoint pair flips any decision comparison — drafting pre-checked
  both non-flipping: maxima (60, 70, 69) at all three granularities, bucket
  pair {69, 70} both over the band); **twin-arm disagreement** surviving
  the INVALID diagnosis.

GATE POWER, computed at registration (the V065/V067 lesson): the sim is
FULLY DETERMINISTIC at every decision cell — every decision clause and
every F-gate is an exact integer/Fraction comparison or an exhaustive/DP
equality; the only seeded arm is reporting-only with NO statistical gate
(its gates are draw-count sentinels and exact reproducibility, pass
probability 1 for a correct implementation); JOINT pass probability for a
correct implementation = 1 EXACTLY (the P059–P072 no-stochastic-gate
precedent). MARGIN LEDGER, disclosed (the V083 practice): R2 clears at
×10/9 ≈ 1.111 (fixed, 7/6 vs 21/20) and ×23/21 ≈ 1.095 (bucket, 23/20 vs
21/20); the straddle clause is an exact equality BY LAW (2B — no margin
concept); R1 carries THREE registered margin-0 contacts (sliding 60 = S;
aligned-fixed 60 = S; and in the S = 70 falsifiability world, fixed
70 = 70) — these are knife-edges BY CONSTRUCTION, the head's entire claim
being that the committed constants sit exactly on the degeneracy surface;
the bucket dead check is the one fat margin (min level 50 vs the 1-token
threshold). R3's separating-emptiness clause is exact emptiness (no margin
concept).

## Gates (run INVALID on any failure)

- **F1 — model identities:** the equal-average identity B·T = S·w = 600 on
  the committed integers; the partition upper bound (any L-span splits into
  ⌈L/w⌉ blocks each inside some w-window, so N_slide(L) ≤ B·⌈L/w⌉) checked
  symbolically and numerically; admitted-equals-schedule accounting; the
  Retry-After formula reproduced verbatim from the pinned shim lines.
- **F2 — the three structure theorems, exact at every cell:** T1's three
  dead-tier checks with exact contact values (60, 60, min-level 50); T2's
  maxima (70, 69/70, straddle 20) with the excess ratios 7/6 and 23/20;
  T3's redundancy law over the full grid, the separating triple (committed
  none / S = 50 witness / S = 70 none), and the w = 7 divisibility world
  (90).
- **F3 — census anchors (exact, from the drafting run):** N_slide(60) = 60,
  N_fixed_adv(60) = 70, N_fixed_aligned(60) = 60, N_bucket(60) = 69
  (closed-interval exhibit 70), N_fixed_adv(2) = 20, N_slide(2) = 10;
  excesses 7/6 and 23/20, margins ×10/9 and ×23/21; bucket-pair min level
  = 50 exactly over 600 s; the w = 7 cell 90; the full 4×4 grid rows
  verbatim (e.g. (20, 10): 120/140/138 — every S in the grid live; (5,
  10): 30/35/34 — every S dead); obedient-client 3600 admits in 3600 s.
- **F4 — the hand world (pencil):** B = 2, w = 2 s, span 4 s: sliding max
  = 4 (two disjoint windows × 2 — and the EXHAUSTIVE search over all
  3^4 per-slot schedules agrees: 4), fixed-adversarial = 6 (three windows
  touched: 2 at the end of one, 2 in the middle one, 2 at the start of the
  last), bucket = 5 (start 2, refill 1/s × 3 boundaries). All three by
  pencil, matching both arms.
- **F5 — degeneracy and convention controls:** granularity invariance —
  the maxima triple (60, 70, 69) identical at δ ∈ {1, 1/2, 1/5}; the
  bucket endpoint pair {69, 70} both ≥ 21/20·S; the grid-wide discipline
  ordering N_slide ≤ N_bucket ≤ N_fixed_adv at every grid cell (drafting:
  holds at all 4 (B, w) rows); five exhaustive small-world checks of the
  sliding max law (all exact).
- **F6 — battery:** Arm B reproduces every Arm-A number exactly (DP/greedy
  vs closed form, independent separating search, independent alignment
  enumeration); twin independently-written decision evaluators agree on
  the ruling token; Arm-R draw-count sentinels; per-trace worst-window
  theorem check (≤ 60, with the observed contact AT 60 reported);
  presentation seed 20261652 read by presentation legs only; aux seed
  20261653 never read; stdout + results.json byte-identical across two
  process runs (Arms A/B platform-independent exact arithmetic; Arm R
  pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P072 exact-arm norm)

REJECT, at the drafter's exact values (the sim re-derives everything from
scratch and must not trust these; every number below was produced by the
drafting script this session): **R1** — no separating schedule at
(10, 10, 60, 60) under sliding; dead-tier contacts (60, 60) sliding,
(60, 60) aligned-fixed, bucket min level 50/1 over 600 s. **R2** —
N_fixed_adv(60) = 70 (7/6, ×10/9 over the band), N_bucket(60) = 69 (23/20,
×23/21; closed-interval 70), straddle 20 = 2B. **R3** — 600 = 600; S = 50
separating witness (six 10-bursts, 60 admits); w = 7 world 90 > 60.
Falsifiability is real and named on three axes: (i) the **S = 50 world** —
one committed-constant step down and the sustained tier is LIVE under
every discipline (the separating schedule exists even under sliding), so
APPROVE's first clause flips — the head's dead-ink claim is specific to
the committed constants, not to two-tier limiters in general; (ii) the
**w = 7 world** — redundancy dies by divisibility alone (90 > 60), so the
T1 theorem is lattice-conditional and says so; (iii) the **discipline-pin
world** — if the contract carried one sentence pinning "sliding window",
R2's fork would be moot and the finding would degrade to dead-ink only
(the consequence names exactly this one-sentence fix). Disclosed
sharpenings, reporting-only: the Arm-R traces touch the theorem contact
exactly (worst 60 s admitted-window = 60 on both seeds: 20261650 → 23270
admitted / 26730 rejected of 50,000 offered at 2/s; 20261651 → 9183/10817
of 20,000); the obedient Retry-After client self-paces to exactly the
sustained rate (3600 admits in 3600 s — the shim's header formula is an
exact sustained-compliance governor, a genuinely nice committed property
worth stating back to the lane).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

superbot-mineverse (the verdict CONSUMER) owns the harvested contract; the
superbot lane co-consumes (the unbuilt executor is the party that will pick
a discipline). REJECT → paste-ready structured choice, recommendation first
per Q-0263.2: **(a, recommended)** PIN THE DISCIPLINE in § Rate limits with
one sentence — "windows are SLIDING, per the shim's reference semantics
(`tests/shim/shim_bot.py` `_consume_budget`)" — and restate the sustained
line as a DERIVED conformance assertion rather than a second knob ("≤ 60 in
any rolling minute — implied by the burst tier under sliding; kept as an
executor conformance check"), PLUS commit the two witness schedules as
conformance fixtures (the 70-in-60 fixed-window witness and the 20-in-2 s
straddle) so a fixed-window or token-bucket executor FAILS the contract's
own done-criterion (shim-fixture conformance, contract lines 341–348)
before cutover — zero web-side behavior change, and the executor is
unbuilt so the fix costs one sentence and two fixtures now versus a silent
16.7% over-admission later; **(b)** make the sustained tier LIVE by moving
it off the lattice point (e.g. 40/min < 60) — a real second budget, but an
intended-UX decision the lane/owner must size, never ruled here; **(c)**
status quo + a doc note that the sustained line is expectational only.
APPROVE → the pair stands as-is with a measured basis. NULL → the named
axis ships with the exact maxima tables. Follow-ups named, none in scope:
multi-client contention fairness under the Retry-After governor; the
±300 s signature skew window's interaction with retry pacing; GCRA/
leaky-bucket-meter shaping semantics; per-(suid, guild_id) key-cardinality
memory of the executor-side store.

## Dedup

Tree-wide `rg -i 'rate.?limit|token.?bucket|sliding.?window|leaky.?bucket|burst'`
(bootstrap.py/.substrate excluded) at HEAD 412f132: no proposal P001–P072
prices a two-tier rate-limit pair, tier redundancy, or window-discipline
divergence. Hits argued distinct: **P069 → the CONWIP cap/floor pair** (the
same MOVE FAMILY — two committed constants in tension, priced by exact
theorems — on a DIFFERENT object with different mathematics: P069 is a
closed-loop stationary stochastic law over circulating WIP tokens; this
head is worst-case adversarial combinatorics on an open request stream —
zero shared fixtures, and the kinship is disclosed rather than hidden);
**P031/P035 lineage (superbot-games)** → game-side energy throttles and
pacing windows (game-economy semantics, not an HTTP contract's tier pair);
**P045** → the SAME repo's READ contract staleness constant (different
document, different mechanism — renewal-reward freshness, not admission
combinatorics); **P055** → the achievements catalog (game slot). sim-lab
READ-ONLY swept at 237b24a (VERDICT 084 newest): the sliding-window hits
are the V018/V046 game-admission lineage (a shared K-window over game
triggers — an admission CAP sized for economy balance, its "sliding-window
re-audit" a validity gate name) and the websites OAuth spike's
token-bucket (a security CONTROL exercised under attack) — no verdict
prices tier redundancy or discipline divergence. No recorded drop of this
head exists on any card. Method kin only: the P059–P072 fully-exact
zero-stochastic-gate discipline (exact arithmetic + independently-written
twin + reporting-only MC), reused as machinery on a new object — this
head's own additions to the battery: the DEAD-TIER theorem with its three
uniform-discipline contact values, the discipline FORK quantified as exact
worst-span maxima (7/6, 23/20, 2B), the LATTICE-POINT location of the
committed constants (equality in the redundancy law), and a per-trace
theorem-contact check inside the reporting arm.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional:
(1) ADVERSARIAL WORST-CASE — the maxima are over all admissible schedules;
real browser traffic is tamer, so T2's excesses are CEILINGS (the
directional statement: a fork that admits 7/6 worst-case admits less in
typical traffic — but a contract is exactly a worst-case instrument, which
is why worst-case is the right functional). (2) SLOTTED TIME — δ ∈ {1,
1/2, 1/5} s with unbounded per-slot arrivals; the granularity-invariance
gate (F5) is the check that nothing decision-bearing lives in the
quantization; the bucket's endpoint convention is the one convention-
sensitive cell and is disclosed with both values over the band. (3) THE
THREE DISCIPLINES are the universe — sliding, fixed, token bucket cover
the standard implementations (GCRA/leaky-meter is bucket-equivalent at
this granularity and named as a follow-up); a genuinely exotic discipline
could sit outside the fork, and the claim is scoped to the named three.
(4) PER-KEY ISOLATION — one (suid, guild_id) key's budget; cross-key
aggregation effects (global executor load) are out of scope. The T1/T3
theorems are exact facts about the committed constants under (2)–(3); the
T2 excesses additionally lean on (1) and say so.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained mechanism probe on
> committed constants, sim is report-only evidence, no spend/publish/irreversible
> surface — README § probe battery). Verify-first ran FIRST, live this slice:
> (a) **dedup** — the tree-wide and sim-lab sweeps above returned no prior
> pricing of tier redundancy or discipline divergence (nearest kins cited and
> argued); (b) **kill test NOT triggered** — no prior proposal, idea file, or
> session-card 💡 prices the write contract's rate-limit pair; P045's tap of
> this repo is a different document and mechanism; (c) **feasibility +
> liveness arithmetic checked LIVE** — every registered numeral was PRODUCED
> by the drafting script this session (the V084 NO-DERIVED-LITERALS lesson):
> the maxima table (60/70/69/20), both excess ratios and band margins, the
> three dead-tier contacts, the separating triple, the w = 7 world, the full
> grid, the granularity triple, the bucket convention pair, the pencil world
> with its exhaustive check, five small-world law verifications, and both
> Arm-R previews with the obedient-client trace; expected landing DISCLOSED
> (REJECT), all four rulings reachable under the pre-registered rule, the
> S = 50 APPROVE-flipping world and the discipline-pin degradation world both
> named, and the INVALID controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of what the
write contract's two rate-limit sentences jointly mean — taken where the
meaning actually lives: the worst-case admission maxima of the three standard
limiter disciplines at the committed constants (10/10 s, 60/min — the same
average rate, 1/s exactly). Three theorems carry it: the sustained tier never
fires under any uniform discipline (dead ink, with two margin-0 contacts and
one 50-token margin); the burst tier alone breaks the sustained promise by
7/6 (fixed) / 23/20 (bucket) with a 2B boundary straddle; and the committed
constants sit exactly on the redundancy boundary (one step off in any
direction changes the structure). All decision arithmetic is seedless exact
integers/Fractions judged against bands fixed before any code, byte-identical
across runs, with the seeded click-stream arm demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-15
fleet-slot opener goes unserved and the executor gets built against two
sentences nobody priced. (ii) Re-tap a recent slot source — fails the
least-recently-tapped rotation discipline this slot has kept since P053.
(iii) A prose bug report to the lane ("your two tiers have the same average
rate") — states the smell but not the structure: without the maxima it cannot
say WHICH failure ships (dead ink vs 16.7% over-admission), cannot price the
fork, and cannot hand the lane the one-probe conformance fixture that makes
the discipline testable. (iv) An MC-only sim — leaves every decision number
seed-noisy when the whole object is exact worst-case combinatorics (the
V065/V067 lesson); MC is demoted to the trace-level theorem-contact check.
(v) This head: exact maxima as the ruling, REJECT-first bands on dead-tier +
fork + lattice, INVALID on the F1–F6 gates, robustness disclosed via the
granularity/convention controls and the three named falsifiability worlds.
(vi) Over-scope (multi-client fairness, GCRA shaping, skew-window
interaction, key-cardinality memory) — each named as a follow-up, none in
scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~150-line stdlib file: four closed-form maxima, a
DP/greedy twin, an exhaustive small-world verifier, and a two-bucket
minimum-level trace — that single kernel yields the full discipline × (B, w,
S) maxima surface, the three dead-tier checks with exact contacts, the
separating-schedule triple, the divisibility world, the granularity and
convention controls, and the per-trace theorem-contact check on seeded click
streams — from a sim a verdict session runs cold in under a second.

**4. What breaks it? (assumptions made explicit)** (a) **Worst-case is a
choice** — typical traffic never hits the maxima; but the contract is a
worst-case instrument (it exists to bound the adversarial client), so the
functional matches the artifact; stated directionally in the model basis.
(b) **The three-discipline universe is a choice** — an exotic limiter could
sit outside the fork; the claim is scoped to the named three, which cover
every implementation in this fleet's committed code (the shim's sliding
deque; the websites spike's token bucket). (c) **Band placement could
cherry-pick** — the 21/20 band is committed BEFORE the sim, the expected
landing is DISCLOSED (REJECT), and the falsifiability is three-axis: S = 50
flips APPROVE's first clause, w = 7 kills the lattice claim's divisibility
leg, and a one-sentence discipline pin degrades the finding to dead-ink only
— the head says which single sentence would gut it. (d) **The closed forms
are claims, not axioms** — each is verified against an independently-written
DP twin AND an exhaustive search on five small worlds, and each carries the
law-failure-without-gate-failure NULL axis, so a wrong formula becomes a
finalized corrected law, not a silent bad gate. (e) **The margin-0 contacts
could hide fragility** — they are the head's THESIS, registered as
knife-edges in the margin ledger (the committed constants sit ON the
degeneracy surface; that is the finding, not an accident of the grid).

**5. What does it unlock?** For the mineverse lane: the write contract's
§ Rate limits gains a measured basis at the exact moment the executor is
still unbuilt — the one-sentence discipline pin plus two committed witness
fixtures (70-in-60, 20-in-2 s) turn an unstated implementation choice into a
conformance-testable clause, riding the contract's own done-criterion
(shim-fixture conformance, lines 341–348). For the fleet: a transferable
correction for every surface that ships burst + sustained limiter pairs —
check B·T/w against S before shipping two tiers (equal average rates = one
knob printed twice), pin the window discipline in the contract (the same
constant pair is compliant or 16.7%-leaky depending on it), and encode the
discipline as a witness-schedule fixture, not prose. Plus one genuinely
positive committed property stated back: the shim's Retry-After formula is
an exact sustained-rate governor (an obedient client self-paces to
precisely 1/s).

**6. What is the cheapest experiment that decides it?** The whole head IS
the cheapest deciding experiment: Arm A settles every decision number
exactly in milliseconds with no seed. The single cheapest probe if a reader
doubts a leg is the pencil world — B = 2 per 2 s over a 4 s span: sliding
admits 4 (two windows), fixed-straddle admits 6 (three windows touched),
bucket admits 5 (2 + 3 refills) — three disciplines, three different
answers, countable on fingers; and the committed pair's degeneracy is one
multiplication: 10 × 60 = 60 × 10.

**7. What would make this a mistake to run?** If the exact treatment were
unavailable (it is not — the decision surface is small-integer
combinatorics), if the head duplicated a prior pricing (it does not — the
sweeps returned no tier-pair or discipline pricing anywhere in either tree,
and both nearest kins are argued distinct at the fixture level), or if the
disclosed REJECT made the run theater. It does not: the value is the
independent hermetic re-derivation PLUS the parts no code comment states —
the three exact contact values, the fork quantified as worst-span maxima
with committed witness schedules, the lattice-point location of the
committed constants — and both non-REJECT rulings are genuinely reachable
(APPROVE is one committed-constant step away at S = 50; the discipline-pin
world degrades the finding by construction).

**8. How will we know it worked?** A committed sim-lab report with: the full
discipline × (B, w, S) maxima tables (exact integers), the three dead-tier
checks with contact values, the separating-schedule triple with the S = 50
witness, the divisibility world, the granularity and convention control
tables, the margin ledger (×10/9, ×23/21, the three registered margin-0
contacts, the 50-token bucket margin), the F1–F6 gate results, the verdict
token against the pre-registered bands, Arm R's trace table (admitted/
rejected/worst-window per seed, the obedient-client rate), and a
byte-identity note (two process runs identical). A clean run reproduces the
drafter's disclosed reference values (60/70/69/20; 7/6 and 23/20; contacts
60, 60, 50; witness 60 > 50; w = 7 → 90) from scratch, or — the more
interesting outcome — DISAGREES and pins the drafter's error, which the
pre-registered rule then rules on honestly (the law-failure NULL axis
exists for exactly that).

**Recommendation: sim-ready**
