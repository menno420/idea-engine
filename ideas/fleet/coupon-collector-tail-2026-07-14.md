# Does "almost complete" mean "almost done"? The coupon collector's tail

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 9 closer; a NINTH fleet-external domain: occupancy & collection problems / the coupon collector, disjoint from the eight prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@a500048c488a80d449720d737918e887f3a4e9e8 · fetched 2026-07-14T00:26:42Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is pinned in this file, zero repo/network reads at verdict time — the P017–P051 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 9 has served fleet backlogs (P049 #358), venture (P050 #371) and game mechanics (P051 #373), so this head is the round-9 UNRELATED closer.

**Placement note (decide-and-flag):** this fleet-external pure-probability head lives in `ideas/fleet/` per the check_sections carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, 044 and 048 did.

## The folk belief

"Once you've collected most of a random-draw set — trading cards, gacha banner, sticker album, loot-box cosmetics — you're basically done; the last few are a minor mop-up." The intuition is linear: 90% of the set collected feels like 90% of the effort spent.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

In a uniform coupon collector (each draw an independent uniform pick over N distinct items), the wait to go from j distinct items held to j+1 is geometric with success probability (N−j)/N, so its expectation is N/(N−j). By linearity the expected total draws to complete the set is E[T_N] = Σ_{j=0}^{N−1} N/(N−j) = N·H_N with H_N = Σ_{k=1}^{N} 1/k the N-th harmonic number (exact rational). The expected cost of the LAST m distinct items (going from N−m held to all N) is E[tail_m] = Σ_{j=N−m}^{N−1} N/(N−j) = N·H_m. The tail-cost fraction is therefore φ(N,m) = H_m / H_N — divorced from the linear "10% of set = 10% of effort" intuition, because the collection acquires the common items early and the rare-remaining items (the expensive geometric waits) last.

## Pinned model (committed constants)

- Draw model: uniform iid over N distinct items; one item per draw.
- Decision grid: N ∈ {20, 50, 100, 200}; tail size m(N) = ⌈N/10⌉ = {2, 5, 10, 20}. Decision cell N = 50.
- Exact quantities (Arm A, seedless): E[T_N] = N·H_N; E[tail] = N·H_m; φ(N) = H_m/H_N — all exact fractions.Fraction.
- Distributional side-pin (reporting only): exact CDF via inclusion–exclusion P(T_N ≤ t) = Σ_{j=0}^{N} (−1)^j C(N,j) (1 − j/N)^t, used for gate identities and the overshoot report P(T_50 > 2·E[T_50]).
- Confirmation arm (Arm S): seeded MC, N_runs = 200,000 via random.Random(20261345), draw-until-complete, recording total draws and draws-since-the-(N−m)-th-distinct; agreement gate |mean_S − E_A|/E_A ≤ 1/100 AND ≤ 4·SE on E[T_N] and on φ per grid cell.
- Stability leg: seed 20261346, N_runs = 20,000, reproduces the ruling through twin evaluators.
- Reporting/sensitivity leg: seed 20261347 — (a) last-20% alternative m = ⌈N/5⌉; (b) a weighted rarity-tier collector (pinned tiers: 70% mass split over the first 0.7·N items, 25% over the next 0.25·N, 5% over the last 0.05·N) via MC only (no simple exact closed form — disclosed), which pushes φ HIGHER; these name axes, never flip the decision.
- Aux seed: 20261348, reserved, never read by any decision number.
- Seeds 20261345–348 strictly above P051's 20261344 high-water; digit-boundary re-sweep at HEAD a500048 (idea-engine) and the sim-lab working copy shows max allocation 20261344 / 20261336 (the larger numerals 20261542/20261664/20261833 are Fraction-numerator digit substrings in sim-lab results.json — data, not seeds; the P041/P046/P050/P051 rule re-confirmed; this block sits below them, no digit-boundary crossing).

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the tail-is-minor folk belief FAILS in the costly direction": φ(50) ≥ 2/5 AND φ(N) ≥ 2/5 in ≥ 3 of the 4 grid cells AND Arm S confirms within tolerance. (Costly because under-budgeting completion is the error that strands a half-finished collection.)
- **INVALID** (controls misbehaving — report, no ruling): the H_N re-derivation gate fails, or the m=N identity φ=1 / m=1 identity φ=1/H_N fails, or the small-N exact-CDF identity fails, or the Arm-S agreement gate fails on any grid cell.
- **APPROVE** — "the folk belief holds — the tail is minor": φ(N) ≤ 1/5 at EVERY grid N AND the seed-20261346 stability leg reproduces. (Mutually exclusive with REJECT by arithmetic.)
- **NULL** — anything else; pre-registered axes: band-straddle (φ(50) ∈ (1/5, 2/5)); N-sensitivity (φ crosses a band across the grid — the finding is the φ(N) growth curve with its boundary named); weight-sensitivity (the weighted leg would flip a promoted decision — named, never ruling); arm disagreement.

## Expected landing (DISCLOSED per the P048/P049/P050/P051 closed-form-arm norm)

REJECT, at the drafter's exact φ = H_m/H_N: N=20 → (3/2)/H_20 ≈ 0.417, N=50 → (137/60)/H_50 ≈ 0.508, N=100 → H_10/H_100 ≈ 0.565, N=200 → H_20/H_200 ≈ 0.612 — all ≥ 2/5, 4 of 4, with the decision cell at ≈ 0.508 (the last 10% of a 50-item set costs about HALF the expected draws). The sim re-derives every value from scratch and must not trust these. Falsifiability real: the N=20 cell at ≈ 0.417 sits just above the 2/5 edge (a stricter tail definition or the last-20% leg lands it differently), and the APPROVE band 1/5 is genuinely reachable — a set whose tail is a single item at large N gives φ = 1/H_N → small, so the pre-registered bands discriminate. Disclosed sharpening: the final SINGLE coupon alone costs N draws = 1/H_N of the total (≈ 22% at N=50), so the last item dominates the tail.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof plus a transferable method note. REJECT → the "almost complete = almost done" heuristic retires with numbers, and the rule of thumb ships: budget roughly HALF your draws for the last 10% of any uniform random-draw collection (loot-box cosmetics, gacha banners, card sets, and any fleet "collect all N distinct X" coverage sweep — sample-all-N-shards, hit-every-N-endpoint). APPROVE → the linear intuition gains a measured basis. NULL → the named axis (most likely the φ(N)-growth curve or the weighted-tier amplification) ships with its boundary and the free follow-up (promote the weighted leg to a decision arm at pinned tiers).

## Dedup

Tree-wide `rg -i 'coupon|collector|occupancy|gacha|loot.?box|birthday|collect.?all|sticker'` (bootstrap.py/.substrate excluded) at HEAD a500048 — the sweep's hits are argued in the proposal block. No proposal P001–P051 and no verdict V001–V061 prices an occupancy/collection/coverage-completion problem; nearest by "counterintuitive pure-probability" are P032 (Penney) and P048 (Parrondo) — zero shared machinery (no harmonic-sum stage-expectation kernel, no collect-all-distinct absorbing structure). Method kin only: the P017–P051 exact-arm + seeded-confirmation discipline.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'coupon|collector|occupancy|gacha|loot.?box|birthday|collect.?all|sticker'`
> (bootstrap.py/.substrate excluded) at the grounding pin `a500048` returned zero domain
> hits; the 34 raw lines are all incidental (V024/P034 drift-*regime* occupancy, P051's
> "self-funded collector", and the P044 checkout-pooling idea's set-aside "birthday-collision
> scheduling" mention — the collision/occupancy family confirmed considered and never priced).
> (b) **kill test NOT triggered** — no prior proposal P001–P051, idea file, or session-card 💡
> prices an occupancy/collection/coverage-completion problem or the coupon collector.
> (c) **feasibility + liveness arithmetic checked** — runtime bounded (Arm A is four exact
> harmonic-sum `Fraction` reductions, Arm S is 200k draw-until-complete loops over N ≤ 200;
> well under a minute, stdlib only); expected landing DISCLOSED with its exact drafting-time
> value (REJECT, φ(50) = (137/60)/H_50 ≈ 0.508) rather than hidden, all rulings reachable
> under the pre-registered rule, the band-straddle NULL axes and the INVALID controls gate
> both named.

**1. What is this really?** A pre-registered exact MEASUREMENT of the folk belief that
finishing a random-draw collection is a minor mop-up — does the last ⌈N/10⌉ of a uniform
coupon-collector set actually cost a materially large share of the expected draws — computed
as the exact-rational tail-cost fraction φ(N) = H_m/H_N over the grid N ∈ {20,50,100,200},
judged against bands fixed before any code (REJECT `φ ≥ 2/5` in ≥3 of 4 cells first, APPROVE
`φ ≤ 1/5` at every N with stability reproduction, NULL otherwise), every decision number an
exact `Fraction`, byte-identical across two runs, with a seeded draw-until-complete Monte-Carlo
arm cross-validating the closed form.

**2. What is the possibility space?** (i) Don't run it — the round-9 unrelated slot's closer
goes unserved and the rotation closes short. (ii) Re-use a prior round's domain — fails the
owner's "rotate" ask (P017/P024/P028/P032/P036/P040/P044/P048 occupy voting, routing,
tournaments, pattern races, stopping, spatial self-organization, queueing, ratchets). (iii) A
literature summary ("the coupon collector is N·H_N, see any probability text") — retells the
textbook direction, measures nothing against a pre-registered consumer-relevant band, and
dodges the live question (how much of the total does the *last 10%* cost, and does the folk
belief fail). (iv) An MC-only estimate — leaves φ noisy and seed-dependent when an EXACT
rational closed form is available, so the DECISION arm is the exact harmonic-sum solve and MC
is demoted to confirmation. (v) This head: exact-rational Arm A on the pinned grid as the
ruling, seeded Arm S as the cross-check, REJECT-first bands on φ, INVALID gate on the H_N /
φ(m=N)=1 / φ(m=1)=1/H_N / exact-CDF identities, robustness disclosed via the reporting-only
last-20% and weighted-rarity-tier legs. (vi) Over-scope (non-uniform weights as a *decision*
arm, pity timers, multi-copy sets, partial-set objectives) — each named as a follow-up, none
in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One
~150-line stdlib file: an exact `Fraction` harmonic-sum kernel H_N = Σ 1/k reused for E[T_N],
E[tail_m], and φ = H_m/H_N across the four grid cells, plus one draw-until-complete MC loop
parameterized by N and the tail index. That single file yields an exact, reproducible ruling
on a famous counterintuitive result at a consumer-relevant pin, AND — as free side pins — the
exact inclusion–exclusion CDF for the overshoot report P(T_50 > 2·E[T_50]), the last-single-
coupon share 1/H_N, and the weighted-tier amplification column, all from a sim a verdict
session runs cold in under a minute.

**4. What breaks it? (assumptions made explicit)** (a) **The uniformity assumption is a
choice** — equal per-item draw probability is the named most-likely-to-flip alternative; real
collections are rarity-weighted, which pushes φ HIGHER, so a uniform REJECT is robust in the
costly direction and the weighted-tier leg brackets the amplification (direction stated).
(b) **Band placement could cherry-pick** — both bands (2/5, 1/5) are committed BEFORE any code,
are DISJOINT, NULL is first-class (band-straddle, N-sensitivity, weight-sensitivity, arm
disagreement), and the expected landing is DISCLOSED (REJECT) rather than hidden. (c) **The
tail definition is a choice** — last-10% is the pinned tail; the last-20% and single-item legs
bracket the definition sensitivity, and the N=20 cell at ≈0.417 sits deliberately just above
the 2/5 edge so the falsifiability is real. (d) **The independence assumption** — iid draws
with no pity timer or dedup-guarantee mechanic is the named alternative that would SHORTEN the
tail and is the direction that could reach APPROVE, stated. (e) **An arithmetic slip in the
drafter's hand check** — the sim RE-DERIVES every H_N, E[T_N], E[tail], and φ from scratch
with zero trust in this file's `≈` values, and Arm S's independent draw-until-complete
simulation cross-checks by a completely different code path, so a solver bug shows up as an
Arm-A/Arm-S disagreement → INVALID.

**5. What does it unlock?** The pipeline's NINTH fleet-external verdict and the rotation lane's
proof it spans domains (voting → routing → tournaments → pattern races → stopping → spatial
self-organization → queueing → ratchets → occupancy/collection); a measured, citable answer to
"does almost-complete mean almost-done for a random-draw set, and by how much" — the exact φ
table, the last-single-coupon share, and the overshoot report as standalone side pins; and a
clean, fully-hermetic exact-rational harmonic-sum + collect-all-distinct template that any
later occupancy/coverage question in the fleet can reuse (sample-all-N-shards,
hit-every-N-endpoint coverage sweeps).

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest deciding
experiment: Arm A's four harmonic-sum `Fraction` reductions settle the ruling in microseconds
and need no seed; Arm S's 200k draw-until-complete loops (≈ a second per cell) are the
cross-check. The single cheapest probe if a reader doubts a specific leg is the small-N exact
enumeration at N ∈ {2,3} (E[T_2] = 3, E[T_3] = 11/2), which anchors both the closed form and
the MC against a hand-countable ground truth.

**7. What would make this a mistake to run?** If the exact rational solve were somehow
unavailable (it is not — harmonic numbers are always exact rationals), or if the domain
duplicated a prior head (it does not — dedup returned zero), or if the ruling were
pre-determined in a way that made it worthless. The last is the sharpest self-check: the
landing is disclosed as REJECT, so is this theater? No — the VALUE is the independent hermetic
re-derivation + MC cross-validation + the exact φ(N) growth curve and the weighted-tier
amplification, and the falsifiability is real (the N=20 cell sits just above the 2/5 edge and
the APPROVE band 1/5 is reachable via a single-item tail at large N). It would only be a
mistake if run as a bare "compute a known constant"; framed as re-derive-plus-validate-plus-
price-the-consumer-band, it is a genuine, self-contained knowledge deliverable.

**8. How will we know it worked?** A committed sim-lab report with: Arm A's exact φ(N), E[T_N],
and E[tail] as `Fraction`s and their `float` renderings; the last-single-coupon share 1/H_N;
the inclusion–exclusion overshoot report P(T_50 > 2·E[T_50]); the verdict token (REJECT /
APPROVE / NULL) against the pre-registered bands; Arm S's seeded empirical means each inside
tolerance of Arm A per grid cell; the weighted-tier reporting column; the small-N enumeration
anchors; and a byte-identity note (two process runs of Arm A produce identical rationals). A
clean run reproduces φ(50) = (137/60)/H_50 (the drafter's disclosed reference) from scratch,
or — the more interesting outcome — DISAGREES with it and pins the drafter's arithmetic error,
which the pre-registered rule then rules on honestly.

**Recommendation: sim-ready**
