# Concentrating an N-book series' quality budget on the entry book beats spreading it — until the entry step hits the read-through ceiling r_max, where the optimal allocation FLIPS to spread: a saturation-driven crossover located exactly at the world's stability bound

> **State:** sim-ready
> **Class:** venture — round-18 venture slot (standing ORDER 003 · rotation slot per ORDER 004 rule 3). Adjudication: sim-lab VERDICT 099.
> **Target:** sim-lab
> **Grounding:** https://github.com/menno420/idea-engine@8c83fef66c5c8f97820e9d0593f00932a484a3b1 · fetched 2026-07-16T17:43:03Z
> **Harvest source (firsthand):** the venture-lab idea tree read FIRSTHAND @ 8c83fef — the series/read-through economics implicit in ideas/venture-lab/ (book-versioning, breadth-depth, KU-exclusivity heads all model single-title funnels; NONE models multi-book series read-through allocation). r_base/r_max/slope are stipulated pinned constants, disclosed as calibration-not-estimate per the TRUTH bar.

## The phenomenon (one line)

A KDP author with an N-book series and a fixed quality budget B faces a CROSSOVER: below a threshold B\* the entry-concentrated allocation earns more revenue, above it the evenly-spread allocation wins — and the reversal is caused by the entry step's read-through saturating at the ceiling r_max (the world's stability bound), past which extra budget on book 1 is wasted while downstream steps still have headroom.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

A series is a multiplicative funnel. The entry cohort of C readers all buy book 1. A reader reaches book k+1 only by having advanced every earlier transition, so with per-transition read-through r_1, r_2, r_3 the expected books bought per reader is

    E[books] = 1 + r_1 + r_1·r_2 + r_1·r_2·r_3,

and total revenue = C · E[books] (royalty = 1 unit/book). The **shadow value** (marginal revenue) of raising transition k is the sum of every downstream term that r_k multiplies:

    ∂E/∂r_1 = 1 + r_2 + r_2·r_3      (r_1 gates ALL three downstream books)
    ∂E/∂r_2 = r_1·(1 + r_3)          (r_2 gates only books 3–4, and only for readers past step 1)
    ∂E/∂r_3 = r_1·r_2                 (r_3 gates only book 4)

At the base world (all r=0.30) the reach ordering is strict: ∂E/∂r_1 = 1 + 0.30 + 0.09 = 1.39 > ∂E/∂r_2 = 0.30·1.30 = 0.39 > ∂E/∂r_3 = 0.09. A budget unit buys the most revenue at the EARLIEST transition, because a Δ read-through at step k multiplies through every downstream term. **This is the mechanism that favors CONCENTRATE** — pour the whole budget into r_1, the highest-reach step.

The reach argument holds ONLY while r_1 can still move. Under the linear map r_k = min(r_max, r_base + slope·b_k), the entry step saturates once b_1 reaches (r_max − r_base)/slope = (0.85 − 0.30)/0.05 = **11 budget units**. Past b_1 = 11 the entry step is clamped at r_max = 0.85: its marginal revenue per extra budget unit is exactly ZERO — concentrate's revenue goes FLAT. Meanwhile SPREAD keeps all three transitions unsaturated far longer (each gets only B/3), so every one of its budget units still buys nonzero reach. The two curves cross: below B\* concentrate's higher per-unit reach dominates; above B\* concentrate is stuck at its ceiling while spread's headroom compounds, and spread wins. **The reversal is LOCATED at the stability bound r_max** — this is the P085/V098 lesson embodied deliberately: the gate that flips the answer sits at the world's own saturation crossover, not above it.

## Pinned world (verbatim — sim-lab must reproduce exactly)

- **Series:** N = 4 books → 3 read-through transitions r_1, r_2, r_3 (r_1 = book1→2, r_2 = book2→3, r_3 = book3→4). Book 1 is always bought by every entry-cohort reader.
- **Entry cohort:** C = 2000 readers per seed. Seeds S = [1, 2, 3, 4, 5] (fresh cohort per seed; report per-seed + mean).
- **Royalty:** 1 unit per book bought. **Revenue = total books bought across the cohort.**
- **Base read-through:** r_base = 0.30 (every transition, no budget).
- **Ceiling (STABILITY BOUND):** r_max = 0.85, STRICTLY < 1 — read-through can never reach certainty; realized read-through clamps here.
- **Quality→read-through map (LINEAR up to the cap — a deliberate modeling choice that ISOLATES the saturation mechanism; disclosed):** `r_k = min(r_max, r_base + slope·b_k)`, slope = 0.05. So a single step saturates at b = (0.85 − 0.30)/0.05 = **11 budget units**.
- **Allocations tested at each budget B:** CONCENTRATE = (b_1 = B, b_2 = 0, b_3 = 0); SPREAD = (b_1 = B/3, b_2 = B/3, b_3 = B/3).
- **Stochastic advance:** each reader independently Bernoulli-advances transition k with probability r_k; a reader who fails transition k buys no further books.
- **Budget probe grid:** B ∈ {6, 11, 16, 22, 33}. (B_lo = 6 keeps CONCENTRATE unsaturated: r_1 = 0.60, margin 0.25 below r_max. B_hi = 33 saturates CONCENTRATE's entry step at b_1 = 33 ≫ 11 and wastes 22 units, while SPREAD's b = 11/step just reaches r_max.)
- **CRITICAL — shared randomness / fresh cohort per seed:** for each seed, draw each reader's per-transition uniforms u_1, u_2, u_3 ONCE and evaluate BOTH allocations on the SAME draws (common random numbers — a reader advances transition k iff u_k < r_k under each allocation's own rates). CONCENTRATE and SPREAD MUST see identical reader draws per seed (paired comparison; else NULL). A fresh cohort (fresh RNG stream) is drawn per seed.

## Pre-registered gates (ACCEPT iff ALL hold; else REJECT — order R1→R2→R3→R4)

Calibrated on a stdlib dry-sim over seeds [1..5], C = 2000, common random numbers (throwaway, NOT committed). Margins reported in σ = std-of-the-mean of the per-seed paired difference.

- **R1 (reach regime — concentrate wins unsaturated).** At B_lo = 6, mean revenue(CONCENTRATE) > mean revenue(SPREAD) for ALL 5 seeds, with the paired margin ≥ 3σ. **Calibrated:** CONC mean = 3641.8 books vs SPREAD 3225.0; per-seed CONC−SPREAD diffs = [454, 435, 388, 381, 426] (all > 0); mean margin = 416.8 books ≈ 0.208/reader; **29.8σ** (σ = std-of-mean of the paired diff; need ≥ 3σ). Hand-EV: conc = 1.834/reader vs spread = 1.624/reader.
- **R2 (saturation regime — the reversal, spread wins).** At B_hi = 33, mean revenue(SPREAD) > mean revenue(CONCENTRATE) for ALL 5 seeds, with the paired margin ≥ 3σ. **Calibrated:** SPREAD mean = 6344.4 books vs CONC 4336.6; per-seed SPREAD−CONC diffs = [1974, 2042, 2002, 1989, 2032] (all > 0); mean margin = 2007.8 books ≈ 1.004/reader; **156.7σ**. Hand-EV: spread = 3.187/reader vs conc = 2.182/reader.
- **R3 (well-posedness / stability sanity).** In EVERY run, every realized r_k ∈ [r_base, r_max] = [0.30, 0.85] (no read-through exceeds the ceiling — the V098 check), AND mean revenue is monotone non-decreasing in B for BOTH allocations. **Calibrated:** all rates clamp within [0.30, 0.85] by construction; CONC mean-rev sequence over B = {6,11,16,22,33} = [3641.8, 4336.6, 4336.6, 4336.6, 4336.6] (non-decreasing); SPREAD = [3225.0, 3651.6, 4129.4, 4804.8, 6344.4] (non-decreasing).
- **R4 (crossover located at the entry-step ceiling).** The crossover budget B\* (smallest grid B where mean revenue(SPREAD) ≥ mean revenue(CONCENTRATE)) lies strictly in (11, 22], AND across that range CONCENTRATE's mean revenue is FLAT (its entry step is clamped at r_max), so the reversal is mechanistically caused by the stability bound, not a downstream artifact. **Calibrated:** B\* = **22** ∈ (11, 22]; CONCENTRATE mean revenue at B ∈ {11, 16, 22, 33} = {4336.6, 4336.6, 4336.6, 4336.6} — flat to 0.0 books (r_1 clamped at r_max = 0.85 for all b_1 ≥ 11).

**Disclosed expected landing: ACCEPT** (the crossover exists and is bound-located). Falsifiability axes: if slope or r_max were mis-set so CONCENTRATE never saturates within the grid, R2/R4 fail → REJECT; that is the honest failure mode. If shared randomness is dropped so the allocations see different draws, the paired comparison is confounded → NULL.

## Disclosed verifier

Committed stdlib-only Python (`random` only), fixed seeds S = [1..5], implementing the pinned map and the Bernoulli funnel under common random numbers. It prints the {B × allocation} mean-revenue table (per-seed + mean), the crossover budget B\*, the R1/R2 paired margins in σ, the R3 stability + monotonicity checks, the R4 concentrate-flatness spread, and ONE ruling ACCEPT/REJECT under the pre-registered R1→R2→R3→R4 order. **Fixture** = the seed-1, B_lo = 6, per-reader books-bought for the first 50 readers under BOTH allocations (identical draws), committed alongside. **NULL condition:** the reader draw is under-specified such that CONCENTRATE and SPREAD see different uniforms (the shared-randomness requirement violated) — the comparison is then confounded by draw noise, not allocation.

## Why it matters (venture-ops)

A KDP series author hears two folk beliefs and this head prices exactly where each is right. Folk belief #1 — "make book 1 great, everything flows from the funnel entry" — is CORRECT while the entry step has headroom: a budget unit at the earliest transition multiplies through every downstream book (highest reach), so at small budgets concentrate genuinely wins (R1). Folk belief #2 — "even quality across the series" — is CORRECT once the entry step saturates: past B\* every extra unit on book 1 is wasted at the r_max ceiling while downstream transitions still convert, so spread wins (R2). The actionable rule: pour budget into book 1 UNTIL its read-through nears the ceiling (b_1 ≈ 11 here), then redirect the surplus downstream — "make book 1 great" is right only until its read-through saturates. The crossover B\* is the switch, and it sits at the world's stability bound, not above it.

## Dedup

Tree-wide `rg -g '!bootstrap.py' -g '!.substrate' -i 'read.?through|series funnel|saturation crossover' ideas/` at HEAD 8c83fef returns prior "read-through" usage in three shapes, NONE of which is a multi-book series budget-allocation head:
- **P038 (`ku-exclusivity-fork`, and the V049 pin):** "read-through rt" is a ROYALTY fraction / revenue constant, not a per-transition survival probability, and the decision is KU-vs-wide enrollment — no allocation across transitions.
- **`impulse-price-blanket-series-collapse` (2026-07-15):** uses geometric series read-through r as a DEMAND CHANNEL inside a PRICE-band decision (the m\* volume-ratio bar); the decision object is the price/scope of the boilerplate, read-through is a fixed swept parameter, and there is no quality budget and no saturation ceiling.
- **`sample-window-front-matter-toll` (2026-07-15):** within-artifact position survival for a SINGLE title (front-matter attrition), not a multi-book funnel.

Nearest venture priors, argued distinct: **book-versioning-breadth-depth-allocation** allocates a production budget across breadth/depth of ONE title (single funnel, no multiplicative series reach, no ceiling-located reversal); **adaptive-versioning-early-signal** sequences versioning on an early signal (a stopping/sequencing object, not a budget split); **channel-concentration-vs-diversification** is a concentrate-vs-spread head but across marketing CHANNELS with independent (additive) returns — this head's returns are MULTIPLICATIVE down a funnel and the reversal is caused by a per-step read-through CEILING. This is the pipeline's FIRST head to price a multi-book series read-through funnel as a BUDGET-ALLOCATION object with a stability-bound-located saturation crossover.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained venture-economics probe, the sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep confirmed no prior
> head prices a MULTI-book series read-through ALLOCATION; the read-through hits are a royalty
> constant (P038), a demand-channel leg in a price-band decision (impulse-price-blanket), and a
> single-title front-matter survival (sample-window), none a budget split across transitions with
> a ceiling-located reversal. (b) **kill test NOT triggered** — no recorded drop of a
> series-allocation head on any card. (c) **harvest source read FIRSTHAND** — the venture-lab idea
> tree @ 8c83fef; r_base/r_max/slope are DISCLOSED as stipulated pinned constants
> (calibration-not-estimate), since no committed read-through measurement pins them. (d) **grounding
> reachability** — HONEST: the phenomenon is a stdlib funnel-sim any verdict session runs cold; the
> venture tree grounds the WHY (series read-through is the tree's own recurring demand channel),
> not the map constants. All registered numerals were produced live this session by a throwaway
> stdlib dry-sim (seeds [1..5], C = 2000, common random numbers; NOT committed).

**1. What is this really?** A pre-registered head-to-head between two quality-budget allocations —
CONCENTRATE (all on the entry book) and SPREAD (even across the series) — over an N = 4 book
multiplicative read-through funnel, measured across a budget family B ∈ {6, 11, 16, 22, 33}. The
claim is a SATURATION-DRIVEN CROSSOVER: concentrate wins at small budgets (its entry-step reach is
highest) but the optimal allocation FLIPS to spread once the entry step saturates at the
read-through ceiling r_max — the reversal is located at the world's own stability bound.

**2. What is the possibility space?** (i) Don't run it — the round-18 venture slot goes unserved
and the pipeline stays thinner toward V099. (ii) A folklore retelling ("make book 1 great" vs
"even quality") — retells both beliefs without the exact crossover B\*, the ceiling-location of the
reversal, or the multiplicative reach expressions. (iii) A single-budget snapshot — misses that the
ranking FLIPS across B; one B decides nothing. (iv) This head: a seedful funnel-sim sharing each
reader's draws across both allocations, four pre-registered gates R1–R4, a disclosed fixture.
(v) Over-scope (N-book families, nonlinear/concave quality maps, per-step slopes, promo-degraded
downstream read-through) — each a named follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One ~120-line
stdlib file (`random` only): C readers × 3 shared uniforms, two allocations' rate vectors, a
Bernoulli funnel, run over 5 seeds × 5 budgets, printing the {B × allocation} revenue table, B\*,
and the four gate results — that single kernel yields the reach-regime win (R1), the saturation
reversal (R2), the stability + monotonicity sanity (R3), and the ceiling-location of the crossover
(R4) in well under a second per configuration.

**4. What breaks it? (assumptions made explicit)** (a) **Shared randomness is LOAD-BEARING** — if
the two allocations draw independent reader streams, the paired comparison is confounded by draw
noise, not allocation; the disclosed verifier NULLs if the draw is under-specified. (b) **The
linear quality→read-through map is a deliberate choice** — it ISOLATES the saturation mechanism; a
concave map would saturate more gently and move B\*, and that is a named follow-up, not a claim
about true author production functions. (c) **r_base/r_max/slope are stipulated, not fit** — the
head prices the phenomenon UNDER the pinned map, not a claim about a real series' read-through
rates. (d) **R4 is the mechanistic core** — if the crossover were NOT accompanied by
concentrate-flatness (i.e. the reversal came from a downstream artifact rather than the entry-step
ceiling), the "located at the stability bound" story is false and the head is REJECTED.

**5. What does it unlock?** A measured, citable answer to "concentrate the series quality budget on
book 1, or spread it?" — directly actionable because it corrects BOTH folk beliefs and hands the
author a switch: concentrate until the entry read-through nears r_max, then redirect the surplus
downstream. The crossover B\* is the operational trigger, and the ceiling-location result tells the
author WHY (the entry step is wasted past saturation) rather than just THAT.

**6. What is the cheapest experiment that decides it?** The head IS the cheapest deciding
experiment: the {B × allocation} table settles all four gates in one short run. The single cheapest
sanity probe is the seed-1 first-50-reader books-bought fixture: at B = 6 concentrate's readers
reach deeper on average, at B = 33 spread's do — visible by counting before any statistic.

**7. What would make this a mistake to run?** If the allocations saw different reader draws
(confounds allocation with noise — the pre-registered NULL guards exactly this), if the map
constants were presented as an ESTIMATE rather than a stipulated calibration (the TRUTH bar —
disclosed), or if the disclosed ACCEPT made the run theater. It does not: the value is the
independent hermetic re-derivation (the verdict session re-implements the funnel and must reproduce
the crossover B\* = 22, the R1/R2 margins, and the concentrate-flatness from scratch), and both
ACCEPT and REJECT are genuinely reachable (R2's reversal or R4's ceiling-location could miss under a
mis-set slope/r_max).

**8. How will we know it worked?** A committed sim-lab report with: the {B × allocation}
mean-revenue table per-seed and mean over S = [1..5]; the R1 margin at B = 6 and R2 margin at
B = 33 in σ; the R3 stability (all r_k ∈ [0.30, 0.85]) and monotonicity check; the R4 crossover
B\* with the concentrate-flatness spread; the seed-1 first-50-reader fixture matching the committed
values; and ONE ruling ACCEPT/REJECT under the pre-registered R1→R2→R3→R4 order.

## Gate power + margin ledger

Dry-sim margins in σ units (σ = std-of-the-mean of the per-seed paired difference, n = 5 seeds,
C = 2000, common random numbers; NOT committed — sim-lab re-derives):
- **R1 (B = 6, CONC > SPREAD):** margin = 416.8 books, σ (SEM of paired diff) = 13.98 books → **29.8σ** (need ≥ 3σ). All 5 per-seed diffs strictly positive.
- **R2 (B = 33, SPREAD > CONC):** margin = 2007.8 books, σ = 12.82 books → **156.7σ** (need ≥ 3σ). All 5 per-seed diffs strictly positive.
- **R3:** stability holds by construction (r_k = min(r_max, …) ⇒ r_k ∈ [0.30, 0.85] always); monotonicity holds for both allocations (sequences above).
- **R4:** B\* = 22 (single grid crossing in (11, 22]); CONCENTRATE mean revenue flat at 4336.6 books across B ∈ {11, 16, 22, 33} (0.0-book variation), confirming the reversal is entry-step-ceiling-caused.

Both R1 and R2 margins clear 3σ by ~10× and ~50× respectively at C = 2000, so no cohort increase is
needed. The direction is correct (concentrate wins low, spread wins high), so the disclosed ACCEPT
is reachable and REJECT remains live only via a mis-set map (R2/R4).

**Recommendation: sim-ready**
