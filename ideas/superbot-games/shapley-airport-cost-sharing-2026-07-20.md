# Shapley value of the airport cost-sharing game: for the cooperative COST game v(S)=max_{i∈S} c_i, the Shapley value splits the grand runway cost by sharing each sorted segment equally among the planes that still need it — φ_j = Σ_{k≤j}(c_(k)−c_(k−1))/(n−k+1) — which is exactly the average marginal contribution over uniformly random join-orders, and is NOT equal shares of the total

> **State:** sim-ready
> **Class:** game (cooperative game theory / cost allocation)
> **Target:** sim-lab (VERDICT 244, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding (primary):** https://en.wikipedia.org/w/index.php?title=Shapley_value&oldid=1364397219@c557fc821d4fab14d90c3f7434e1120e6e9cf020 · fetched 2026-07-20
> **Grounding (secondary):** https://en.wikipedia.org/w/index.php?title=Airport_problem&oldid=1312709389@cc179b50972d2bf70492e5099ad242273874258a · fetched 2026-07-20
> **Reference (external, reachable):** [Shapley value — Wikipedia](https://en.wikipedia.org/w/index.php?title=Shapley_value&oldid=1364397219) states the average-marginal-contribution definition `\varphi_i(v)= \frac{1}{|N|!}\sum_R [v(P_i^R \cup \{i\}) - v(P_i^R)]` and efficiency `\sum_i \varphi_i(v)=v(N)` literally; [Airport problem — Wikipedia](https://en.wikipedia.org/w/index.php?title=Airport_problem&oldid=1312709389) states the segment-equal-sharing rule and that "the resulting set of landing charges is the Shapley value for an appropriately defined game." Byte-pinned to the raw-wikitext sha1 of each cited revision.
> **Verifier (firsthand):** ideas/superbot-games/verify_shapley_airport.py · results-dict sha256 `9cbd3c4ec0026187cd64a20bbb79167209f071adbd9a21ecade0787b55d0f4f2`

## The phenomenon (one line)
An airport runway must be long enough for the most demanding plane; when several planes with different runway requirements share one runway, the *fair* way to split the total cost — the cooperative Shapley value — is NOT "everyone pays an equal share." Small planes pay only for the short segment they need, big planes pay a premium for the extra length only they use, and each sorted runway segment is shared equally among exactly the planes that still need it.

## Domain
Cooperative game theory / cost allocation — the Littlechild–Owen airport game, a concrete cost game with a max characteristic function v(S)=max_{i∈S} c_i whose Shapley value has a clean closed form. The Shapley value is defined as the average marginal contribution of a player over uniformly random join-orders; this card is a cost-game instance of that definition.

## The folk belief
The intuitive "fair" split of a shared cost is to divide the total equally: n planes share a runway costing C, so everybody pays C/n. This is wrong for a cost game with heterogeneous needs. A small plane that only needs a short runway should not subsidize the extra length that exists solely for a jumbo jet. The Shapley value formalizes exactly that intuition and produces an *unequal* allocation that still exhausts the total cost.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Model the runway as a cooperative COST game on players N={1,…,n}. Player i needs a runway of cost c_i; a coalition S can serve all its planes with the longest runway any of them needs, so its cost is the characteristic function

    v(S) = max_{i∈S} c_i,   v(∅) = 0.

1. **The Shapley value is the average marginal contribution over join-orders.** For a random permutation R of the players, player i's marginal contribution is v(P_i^R ∪ {i}) − v(P_i^R), where P_i^R are the players before i in R. The Shapley value φ_i is the average of this over all n! orders. For the max-cost game, i's marginal contribution in a given order is max(0, c_i − max_{j before i} c_j): i pays only for runway length beyond what the already-arrived planes have already funded.

2. **Closed form: equal sharing of each sorted segment.** Sort the costs ascending c_(1) ≤ … ≤ c_(n) (with c_(0)=0). The runway decomposes into segments [c_(k−1), c_(k)]; segment k is needed by exactly the n−k+1 planes with rank ≥ k, and the Shapley value shares its cost c_(k)−c_(k−1) equally among them. Hence the plane at rank j pays

    φ_j = Σ_{k=1}^{j} (c_(k) − c_(k−1)) / (n − k + 1).

   This is the Littlechild–Owen result: the landing charges are the Shapley value of the airport game.

3. **Efficiency and symmetry.** The values sum exactly to the grand cost: Σ_i φ_i = v(N) = max c_i (the segments telescope). Two planes with equal cost are symmetric players and receive exactly equal value.

4. **The naive equal split is a distinct, falsifiable allocation.** Dividing the grand cost equally gives each plane v(N)/n. For any non-degenerate cost profile this is NOT the Shapley value — it overcharges the small planes and undercharges the large ones. Sampling the top player's random-order marginal contribution and comparing to v(N)/n rejects the equal split decisively.

Fuller form, one sentence: *the fair cost allocation of the airport game v(S)=max c_i is the Shapley value φ_j = Σ_{k≤j}(c_(k)−c_(k−1))/(n−k+1) — each runway segment shared equally among the planes that need it, equivalently the average marginal cost over random join-orders — which is efficient, symmetric, and provably not the equal split v(N)/n.*

## The formal model / Pinned world (committed constants)
- Object: the cooperative cost game on N players with v(S) = max_{i∈S} c_i, v(∅)=0.
- Marginal contribution of i in order R: max(0, c_i − max_{j before i} c_j).
- SEED = 20260717; a single `random.Random(SEED)` is consumed once, in the Monte-Carlo pass over random join-orders; the SAME sample feeds both G2 (exact-model agreement) and G4 (equal-split rejection).
- Exact arithmetic via `fractions.Fraction`; the n! average via `itertools.permutations`; the closed form via the sorted-segment sum.
- Committed constants: MAIN_COSTS=(1,2,4,8), MAIN5_COSTS=(1,2,4,8,16), SYM_COSTS=(2,5,5,9); G2/G4 G2_TRIALS=200,000; G4_THRESHOLD=6.0.

## Pre-registered gates
- **G1 — EXACT closed form == n! average (Fraction, n∈{4,5}).** For MAIN_COSTS (n=4) and MAIN5_COSTS (n=5), the segment closed form `shapley_closed` equals the exact average over ALL n! orderings `shapley_enum` as `fractions.Fraction`, for every player. *Direction:* every player equal; a single mismatch fails.
- **G2 — Monte-Carlo agreement, top player (|z| < 3).** 200,000 seeded random join-orders; the sampled mean marginal contribution of the top (max-cost) player is compared to its exact Shapley value; z = (mean − φ_top)/se. *Direction:* two-sided consistency with the exact value; small |z| = agreement.
- **G3 — invariance (exact).** Efficiency — Σ_i φ_i equals v(N) = max c_i exactly (Fraction); and symmetry — on SYM_COSTS=(2,5,5,9) the two equal-cost players (indices 1,2) receive exactly equal value. *Direction:* both exact; any mismatch fails.
- **G4 — falsifiability (equal split REJECTED).** The naive equal split allocates v(N)/n to every plane. On the SAME MC sample the top player's mean marginal contribution is compared to v(N)/n; z_eq = (mean − v(N)/n)/se. *Direction:* PASS iff |z_eq| > 6, i.e. the equal split is decisively rejected while the exact model is accepted (G2).

## Determinism & digest
`SEED = 20260717`; one `random.Random(SEED)` consumed once (the MC pass is the sole RNG consumer). `compute()` is a pure function of the seed and fixed constants; `main()` runs it twice in-process and asserts byte-identical canonical JSON, and a separate re-invocation is byte-identical. Whole-dict sha256 over the compact canonical JSON (no self-field), printed as the full 64 hex on stdout:

`results_sha256 = 9cbd3c4ec0026187cd64a20bbb79167209f071adbd9a21ecade0787b55d0f4f2`

Observed gate results (this pinned world): **G1 PASS** (closed == enum, all players, n=4 and n=5; main φ = (1/4, 7/12, 19/12, 67/12)). **G2** z = −1.311312 (|z| < 3), top player rank 3 (cost 8), mean 5.57834 vs target 67/12 ≈ 5.5833333. **G3 PASS** (efficiency Σφ = 8/1 == grand cost 8; symmetry — on (2,5,5,9) the pair is 3/2 == 3/2). **G4** z_eq = 939.716932 (> 6), equal split v(N)/n = 8/4 = 2/1 REJECTED. `all_pass = true`.

## Grounding & scope
Two byte-pinned revisions, quoted vs derived scrupulously separated:

**On the pinned Shapley_value revision (oldid 1364397219, raw-wikitext sha1 `c557fc82…e9cf020`, 29,964 bytes; API-sha1 = self-computed-sha1 exact match) — QUOTED:**
- The average-marginal-contribution definition: `<math>\varphi_i(v)= \frac{1}{|N|!}\sum_R\left [ v(P_i^R \cup \{i\}) - v(P_i^R) \right ]</math>` (the value as the average over all |N|! orderings R of the marginal contribution).
- Efficiency: `<math>\sum_{i\in N}\varphi_i(v) = v(N)</math>` ("the sum of the Shapley values of all agents equals the value of the grand coalition"), and symmetry as one of the four characterizing properties.

**On the pinned Airport_problem revision (oldid 1312709389, raw-wikitext sha1 `cc179b50…3874258a`, 3,339 bytes; API-sha1 = self-computed-sha1 exact match) — QUOTED:**
- The segment-equal-sharing rule verbatim: "Divide the cost of providing the minimum level of required facility for the smallest type of aircraft equally among the number of landings of all aircraft" and "Divide the incremental cost … for the second smallest type … equally among … all but the smallest type … Continue thus until finally the incremental cost of the largest type of aircraft is divided equally among … the largest aircraft type."
- The identity "the resulting set of landing charges is the Shapley value for an appropriately defined game," and the Littlechild–Owen (1973) attribution.

**Derived here, NOT on either pinned revision:**
- The **specific Shapley vectors** for the committed cost profiles — (1/4, 7/12, 19/12, 67/12) for (1,2,4,8), (1/5, 9/20, 67/60, 187/60, 667/60) for (1,2,4,8,16), (1/2, 3/2, 3/2, 11/2) for (2,5,5,9) (the airport page tabulates a *different* worked example with costs 8,11,13,18).
- The **equal-split falsifier** v(N)/n and its rejection.
- Every **Monte-Carlo number** (z = −1.311312, z_eq = 939.716932, means) — firsthand from the verifier.
- The **results_sha256** digest.

Honest posture: the *core mathematical claims* (the Shapley value as the average marginal contribution over random orderings, efficiency, and the airport segment-equal-sharing closed form as the Shapley value of the max-cost game) are QUOTED essentially verbatim from the two pinned revisions; this proposal's firsthand contribution is the specific cost-profile allocations, the two-route exact reproduction (closed form vs n! enumeration), the seeded Monte-Carlo confirmation, and the pre-registered rejection of the equal split. Nothing is oversold as novel.

## Dedup — distinct from the Shapley–Shubik power index card
This is the cooperative Shapley **VALUE** of a **COST** game and is explicitly DISTINCT from the already-built Shapley–Shubik power index card (`ideas/superbot-games/voting-power-not-weight-2026-07-20.md`, PROPOSAL 203 → VERDICT 216), which lives in a **simple VOTING** game. The two differ in both inputs and outputs: (a) the characteristic function is the max-cost function v(S)=max_{i∈S} c_i here versus the pivotal-swing 0/1 winning-coalition function of a weighted voting game there; (b) the object produced is a **cost-allocation vector** (how much each plane pays, summing to the grand cost) here versus a **per-voter power number** (a normalized share of pivotal swings) there. A repo-wide grep for "cost-sharing / airport game / cooperative Shapley value" finds no prior card — the only Shapley hits are the Shapley–Shubik voting-power card (a different object) and dedup mentions. No prior airport / cooperative-cost Shapley-VALUE card exists in the ledger; this slice is new.

## Reproduce

```
python3 ideas/superbot-games/verify_shapley_airport.py
# exit 0; prints the results dict, then
# results_sha256: 9cbd3c4ec0026187cd64a20bbb79167209f071adbd9a21ecade0787b55d0f4f2
# all_gates_pass: True
```

## Probe report (v0, self-adversarial)

**1. Is the closed form exactly the Shapley value (not merely approximate)?** Yes. G1 computes the allocation two independent ways — the sorted-segment closed form vs the exact average over all n! orderings — as `fractions.Fraction` for n=4 and n=5 and asserts exact per-player equality (e.g. main φ = (1/4, 7/12, 19/12, 67/12) both ways). No floats, zero slack.

**2. Could the allocation be an artefact of the sampler?** No. The value is an exact counting/averaging identity proved in G1; the Monte-Carlo gate G2 only confirms the top player's finite-sample mean marginal agrees (|z| = 1.31), and efficiency (G3) is an exact Fraction identity.

**3. What is the most plausible wrong belief this could be confused with?** The equal split v(N)/n. G4 pre-registers it as the falsifier and rejects it at z_eq ≈ 940 on the same sample — the top player's true value 67/12 ≈ 5.583 is nowhere near the equal split 2.

**4. Is the verifier deterministic and self-checking?** Yes. Single seeded RNG consumed once in a fixed order; in-process double-run + separate re-invocation both byte-identical; whole-dict sha256 with no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** The average-marginal-contribution definition and efficiency are quoted verbatim from the pinned Shapley_value revision; the segment-equal-sharing rule and the "landing charges = Shapley value" identity are quoted verbatim from the pinned Airport_problem revision; the specific vectors, the falsifier, and the numerics are explicitly flagged derived. The citation is neither over- nor under-claimed.

**6. Does it scale / is it robust?** G1 covers n=4 and n=5 exactly; the closed form is O(n log n) and matches the O(n!) brute force where both are computed; efficiency and symmetry are structural (hold for all profiles).

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong equal-split allocation and rejects it at z ≈ 940; had the value equalled the equal split, G4 would fire.

**8. Any residual risk before ruling?** The exact gates cover n up to 5 by full enumeration; larger n rests on the closed form, which G1 certifies against brute force where feasible. No blocker.

**Recommendation: sim-ready**
