# Vickrey second-price auctions make honesty a dominant strategy: bidding your true value weakly beats every bluff no matter what rivals do — and the exact shade that *wins* a first-price auction never helps here

> **State:** sim-ready
> **Class:** superbot-games · sealed-bid auction / mechanism design · Vickrey second-price auction (Vickrey 1961)
> **Target:** sim-lab (VERDICT 212, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Vickrey_auction&oldid=1338833083@398d2e4148cc7ee83f1343f720f6e243926bb895 · fetched 2026-07-20T05:26:52Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/vickrey-truthful-dominance-2026-07-20.py` (hashlib, json, math, fractions, itertools, random) — results-dict sha256 a96d59f3…6527c (see Dry-sim below).

## The phenomenon (one line)
In a sealed-bid **second-price** (Vickrey) auction the winner pays the *runner-up's* bid, so bidding your exact true value is a weakly dominant strategy — you can never do strictly better by shading down or bluffing up, whatever every rival bids — even though the same shade that is *optimal* in a first-price auction strictly helps there.

## The folk belief
"Never show your hand. In any auction you shade your bid below your true value — reveal less than you're willing to pay and pocket the difference; bidding your true max just hands your surplus to the seller." That instinct is correct for a first-price auction and dead wrong for a second-price one: the pricing rule, not the sealed-bid format, decides whether honesty pays.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Designers of any sealed-bid subsystem — a raid-loot roll, a guild-bank auction, a blind market buy order — worry that players will strategically underbid to game settlement, which forces bolt-on anti-collusion and anti-sniping machinery. The Vickrey rule dissolves that worry at the root. Because the price a winner pays is set by the *second-highest* bid, it is decoupled from the winner's own bid: your report changes only *whether* you win, never *what you pay* when you do. That single structural fact collapses the private-information game — every player's best move is to report truth, no matter what anyone else does, so there is nothing to model and nothing to game. A second-price settlement rule is therefore a *strategyproof primitive*: it turns "what should I bid?" into "type the number you actually value it at," which is fair, computationally free for the player, and denies a bid-shading meta any oxygen. The contrast sharpens the lesson: a first-price settlement invites an arms race of shading and opponent-modeling (symmetric equilibrium shade s(v) = ⌊v·(n−1)/n⌋), which advantages spreadsheet players and manufactures a skill gap that is pure rent-extraction, not fun. The counterintuitive lever for honest behavior is not surveillance but a change to *who sets the price*.

## The formal model (committed constants — sim-lab must reproduce exactly)
- n bidders, index 0 = focal; private values and bids are integers on a discrete grid.
- Winner = highest bid; ties broken to the lowest index (the focal wins its own ties).
- **Vickrey utility:** if the focal wins, u = value − (highest opponent bid); else 0. The price is independent of the focal's own bid.
- **First-price utility:** if the focal wins, u = value − (own bid); else 0.
- **Symmetric first-price shade:** s(v) = ⌊v·(n−1)/n⌋ (the uniform-value Bayes–Nash bid).
- Payoffs are integers, so every dominance comparison (G1) and expectation (G2) is exact — no floats enter the dominance verdict.

## Pinned world (committed constants)
- SEED = 20260717; Z_GATE = 3.0.
- G1 grid: n=3, values 0..4, bids 0..6 (245 (value, opponent-profile) enumerations).
- G2 grid: n=3, values 0..6 (343 value profiles), exact `Fraction` expectations.
- G3 Monte Carlo: n=3, values 0..12, 200000 seeded draws, opponents bid truthfully.
- Shift (G4): G1 at (n=2, v≤6, b≤8) and (n=4, v≤3, b≤5); G3 at (n=4, v≤20).
- Digest: sha256 of json.dumps(results, sort_keys=True, separators=(",",":")), floats pre-rounded to 6 dp, whole-dict, no self-referential field, stdout-only.

## Pre-registered gates (sim-ready iff ALL hold, in order G1 -> G2 -> G3 -> G4)
- **G1 — exhaustive weak dominance (integer-exact; direction: wants 0 mismatches).** Over all 245 (value, opponent-profile) enumerations and every alternative bid, `deviations_strictly_better == 0`, truthful is a maximizer on 100% of profiles (245/245), and the result is non-vacuous (`truthful_strictly_better_instances > 0`).
- **G2 — exact-expectation contrast (Fraction-exact closed form; direction: sign agreement).** Over the full 343-profile value grid, E[shade − truthful] = 114/343 > 0 in first-price but −27/343 ≤ 0 in Vickrey, and E[truthful first-price surplus] = 0 EXACTLY (closed form: truthful bidding against truthful rivals captures zero surplus in a first-price auction).
- **G3 — Monte-Carlo surprise (direction: first-price z ≥ 3σ, Vickrey z ≤ 0).** With 200000 draws against truthful opponents, the shade strictly helps in first-price (z ≥ 3.0) and strictly does NOT help in Vickrey (z ≤ 0 — truthful is never beaten).
- **G4 — robustness/shift (direction: wants 0 mismatches + contrast persists).** G1 dominance re-holds (0 deviations, 100% optimal) under two shifted grids, and the G3 contrast (first-price z ≥ 3σ, Vickrey z ≤ 0) persists under a shifted value range.

all_pass = G1 ∧ G2 ∧ G3 ∧ G4.

## Pre-registered decision rule
APPROVE (reproduce head) iff sim-lab's independent re-implementation reproduces `results_sha256 = a96d59f3…6527c` byte-for-byte AND all four gates hold with the stated directions. Any nonzero `deviations_strictly_better`, a non-positive first-price E-gap, a Vickrey E-gap > 0, E[truthful first-price surplus] ≠ 0, first-price z < 3σ, or Vickrey z > 0 REFUTES the head.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- G1 (n=3, v≤4, b≤6): deviations_strictly_better = 0; profiles = 245; profiles_truthful_optimal = 245 (100%); truthful_strictly_better_instances = 485. **PASS** (wants 0).
- G2 (n=3, v≤6): E[Δ first-price] = 114/343 ≈ +0.332362; E[Δ Vickrey] = −27/343 ≈ −0.078717; E[truthful first-price surplus] = 0/1 = 0 exactly. **PASS** (sign agreement + exact 0).
- G3 (n=3, v≤12, 200000 draws): z_firstprice = +192.175024 (mean Δ = +0.54983); z_vickrey = −155.312083 (mean Δ = −0.21806). **PASS** (first-price ≥ 3σ; Vickrey ≤ 0).
- G4 shift: G1 at (n=2, v≤6, b≤8) deviations = 0 (63/63 optimal); G1 at (n=4, v≤3, b≤5) deviations = 0 (864/864 optimal); G3 at (n=4, v≤20) z_firstprice = +156.675416, z_vickrey = −142.040465. **PASS**.
- all_pass = True.

**Disclosed results-dict sha256 = a96d59f378e5d04a4e211dafafa22244e09d22126ba2c9b1e5f1cc0bdeb6527c**

Digest recipe: sha256( json.dumps(results, sort_keys=True, separators=(",",":")) ), floats rounded to 6 dp before hashing, whole-dict, no self-referential sha field, printed to stdout only. Verified byte-identical across an in-process double-run (guarded in `main`) and two separate process invocations.

## Verifier
Stdlib-only (`hashlib, json, math, fractions, itertools, random`). `g1_dominance` exhaustively enumerates every (value, opponent-bid-profile, alternative-bid) triple and counts strictly-profitable deviations from truthful; `g2_exact_expectation` sums exact `Fraction` utility gaps over the full value grid; `g3_montecarlo` streams 200000 seeded draws against truthful opponents and computes a z-statistic for the shade − truthful utility change in each format; `build_results` assembles the four gate booleans; `main` double-runs in-process and aborts on any divergence before emitting the digest.

Reproduce:
```
python3 ideas/superbot-games/vickrey-truthful-dominance-2026-07-20.py
```
Expected: the JSON dump above, four `PASS` lines, `all_pass: True`, and `results_sha256: a96d59f378e5d04a4e211dafafa22244e09d22126ba2c9b1e5f1cc0bdeb6527c` (exit 0).

## Why it matters (game design)
A second-price settlement rule is a drop-in strategyproof primitive for any sealed-bid subsystem — loot auctions, guild-bank sales, blind market orders. Because the winner's price is set by the runner-up, not themselves, the dominant strategy is "enter the number you actually value it at": no opponent-modeling, no shading meta, no rent for sophisticated players. Ship a first-price rule instead and you invite an arms race of bid-shading (equilibrium shade s(v) = ⌊v·(n−1)/n⌋) that rewards spreadsheet play over enjoyment and silently taxes casual bidders. The counterintuitive lever: to make players behave honestly, don't police them — change who sets the price.

## Dedup
Distinct from every existing superbot-games head:
- `penney-game-second-mover-advantage-2026-07-20.md` (P193) — non-transitive *waiting-time* on coin sequences; no auction, no pricing rule.
- `intransitive-efron-dice-2026-07-20.md` (P195) — intransitive dice beats-cycle; no bidding.
- `blotto-evenness-trap-2026-07-19.md` (P171) — resource allocation across fronts, no truthful-revelation mechanism.
- `glicko-rd-order-sensitivity-2026-07-19.md` / `mmr-rating-deflation-2026-07-19.md` — rating dynamics, not auctions.
- `guild-volunteer-dilemma-2026-07-18.md`, `snipe-clearing-leak-2026-07-18.md` — these *use* a second-price / settlement flavor as scenario dressing but prove volunteer-dilemma / clearing-leak effects; NEITHER states or verifies Vickrey truthful dominance or the first-price shading contrast, which is this head's whole content.
- The fleet-lane `fleet/deferred-acceptance-proposer-advantage-2026-07-15.md` covers Gale–Shapley strategy-proofness on *matching*, a different mechanism from single-item second-price pricing.
`git grep -i vickrey` / `git grep -i "second-price truthful"` on origin/main returns no prior head proving this result. Pivot: none — Vickrey/VCG were un-built; the head is taken as first choice.

## Model basis (declared model-dependence — the P024 discipline)
Assumes: single indivisible item, independent private values, quasi-linear risk-neutral utility, sealed simultaneous bids, ties broken deterministically to the lowest index. Under these standard assumptions the dominance is a theorem (Vickrey 1961) — exact and free of any distributional assumption. The first-price shade s(v) = ⌊v·(n−1)/n⌋ is the symmetric Bayes–Nash bid *for uniform values*; the G3 contrast uses it as a concrete "known-optimal-elsewhere" strategy against truthful opponents, not as a claim about first-price equilibria under other priors. Relaxing risk-neutrality or independence can perturb first-price behavior but does NOT touch the Vickrey dominance, which holds bid-profile-by-bid-profile.

## One-line design fix
For any sealed-bid subsystem where you want honest bids, settle at the runner-up's price (Vickrey), not the winner's — the dominant strategy becomes "bid what you actually value it at."

## Probe report (v0, 2026-07-20)
**1. What is this really?** A proof-carrying claim that the second-price *pricing rule* (not the sealed-bid format) is what makes truthful bidding weakly dominant, with an exhaustive integer-exact enumeration plus a first-price contrast showing the same shade that wins there never helps in Vickrey.

**2. Is it surprising / counterintuitive?** Yes — the folk instinct "always shade your bid" is exactly right in first-price and exactly wrong in second-price; the settlement rule flips the optimal strategy while the visible sealed-bid format is identical.

**3. Is it TRUE (exactly, under a clean model)?** Yes. G1 enumerates all 245 profiles with zero strictly-profitable deviations (integer-exact); G2 gives the first-price/Vickrey expectation gap as exact Fractions (114/343 vs −27/343) with truthful first-price surplus exactly 0. It is Vickrey's 1961 theorem, reproduced.

**4. Is it reproducible deterministically (stdlib only)?** Yes — SEED=20260717, byte-identical results_sha256 `a96d59f3…6527c` across an in-process double-run and two separate process invocations; stdlib modules only.

**5. What would REFUTE it?** Any nonzero `deviations_strictly_better`, a first-price E-gap ≤ 0, a Vickrey E-gap > 0, E[truthful first-price surplus] ≠ 0, first-price z < 3σ, or Vickrey z > 0.

**6. Is it distinct from prior heads (dedup)?** Yes — no prior superbot-games or fleet head proves Vickrey truthful dominance; the two docs mentioning "second-price" use it as scenario dressing, not as a verified truthful-revelation result (see Dedup).

**7. Is the grounding real and specific?** Yes — Wikipedia "Vickrey auction" revision oldid 1338833083 carries a dedicated "Proof of dominance of truthful bidding" section; the pinned SHA-1 is the raw-wikitext sha1 (matches MediaWiki's own stored revision sha1). Caveat: the pin covers raw wikitext bytes, not rendered HTML or template expansions.

**8. What does it unblock / why does sim-lab care?** A strategyproof sealed-bid primitive sim-lab can drop into any auction subsystem, plus a reusable exact-dominance + Monte-Carlo-contrast harness for future mechanism-design heads.

**Recommendation: sim-ready**
