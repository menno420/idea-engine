# Does "almost complete" mean "almost done"? The coupon collector's tail

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 9 closer; a NINTH fleet-external domain: occupancy & collection problems / the coupon collector, disjoint from the eight prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** menno420/idea-engine@a500048c488a80d449720d737918e887f3a4e9e8 · fetched 2026-07-14T00:26:42Z — the dedup-sweep HEAD, the only read this head takes; every model constant below is pinned in this file, zero repo/network reads at verdict time (the P017–P051 hermetic precedent)
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
