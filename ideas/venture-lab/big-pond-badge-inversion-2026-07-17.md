# Big-pond badge-starvation inversion: placing a title in the maximum-audience category is dominated by an interior pond size, because a rank-K category-bestseller badge — a large conversion multiplier — is unattainable in the biggest, most-competitive ponds

> **State:** sim-ready
> **Class:** venture-lab · self-publishing category placement · non-monotone selection under a threshold badge
> **Target:** sim-lab (VERDICT 103, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@6ec7cc8 · fetched 2026-07-17T02:45:45Z
> **Harvest source (firsthand):** ideas/venture-lab/ (the Ship-It / KDP self-publishing venture world; category placement is a live per-title decision object — priors read this session: series-readthrough-saturation-crossover, channel-concentration-vs-diversification, ku-exclusivity-fork, keyword-tiling-vs-independent-picks)

## The phenomenon (one line)
Choosing the browse category with the most traffic can yield FEWER sales than an interior-size category, because a rank-K "category bestseller" badge (a large organic-conversion multiplier) is only earned where your velocity clears the local competition — and competition rises faster than traffic across ponds, so the badge is lost exactly in the biggest ponds.

## The folk belief
"More eyeballs is better — place the title in the largest-audience category you qualify for." Sales are modeled as monotone increasing in category traffic; the badge is treated as a nice-to-have, not a decision variable. Under that model the answer is always the max-audience pond.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Organic sales in category c = baseline v0 (category-independent) + T_c · p0 · (1 + b·badge_c), where T_c is daily browse traffic, p0 the base browse→buy rate, and b the conversion lift from holding the category-bestseller badge. You earn the badge iff your pre-badge velocity u_c = v0 + T_c·p0 clears the category's rank-K competitor threshold g_c. The trap is a race between two increasing functions of pond size: traffic T_c (the upside) and competition g_c (which gates the badge). When g_c rises FASTER than u_c — the realistic case, since larger categories attract stronger, higher-velocity competitors — there is a crossover pond c* beyond which the badge is lost. Below c* you carry the (1+b) multiplier; at c* sales drop discontinuously by b·T_{c*}·p0 even though traffic went UP. If that badge-loss cliff exceeds the incremental traffic gain, the largest badged pond (interior) strictly dominates the max-audience pond. The optimum is interior, and the naive max-audience choice sits on the wrong side of a discontinuity it cannot see.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- Categories: C = 9, index 0..8.
- Traffic T = [800,1000,1200,1400,1600,1800,2000,2200,2400] browse/day (linear +200 — traffic gains across ponds are MODEST by construction).
- Base conversion p0 = 0.01. Baseline sales v0 = 5.0/day (category-independent).
- Badge lift b = 1.5 (effective conversion p0·(1 + b·badge)).
- Competition schedule (committed): g = [6,9,13,18,24,31,39,48,58] — rank-K competitor pre-badge velocity, rising STEEPLY with pond size.
- Badge rule: badge_c = 1 iff u_c = v0 + T_c·p0 ≥ g_c. → badge = [1,1,1,1,0,0,0,0,0]; crossover at index 4; last badged (interior optimum candidate) = index 3 (T=1400).
- Horizon H = 90 days. N_REPS = 400. SEED = 20260717 (SEEDLESS w.r.t. the shared seed block 20261730 — left untouched, P084/P085/P089 precedent; the sim pins its own SEED constant).
- Stochastics (exact Poisson thinning): buys_c ~ Poisson(H·T_c·p0·(1+b·badge_c)); baseline ~ Poisson(H·v0); total = buys + baseline. Integer/string-keyed deterministic streams (key "SEED|c|rep", sha512-routed) — no wall-clock, no global RNG, no PYTHONHASHSEED dependence.

## Pre-registered gates (evaluation order R1 → R2 → R3 → R4; APPROVE iff ALL hold)
- **R1 — interior dominance.** c_opt = argmax_c mean_sales_c must be INTERIOR (index ≠ 8, the max-audience pond), and mean[c_opt] − mean[c_maxaud=8] ≥ 3σ (combined SE). Dry-sim: c_opt=3, gap≈988.9 sales at combined_se≈3.88 → 255σ.
- **R2 — badge cliff is a real discontinuity.** The last badged pond (index 3) outsells the first unbadged pond (index 4) at ≥3σ, DESPITE index 4 carrying more traffic. Dry-sim: gap≈1712.5 at combined_se≈3.58 → 479σ; more-traffic-fewer-sales confirmed (1600>1400 browse, 1888<3600 sales).
- **R3 — the inversion is not a knife-edge.** Across the pinned b-grid [1.0,1.25,1.5,1.75,2.0] AND ±10% scalings of the competition schedule g, argmax stays INTERIOR (never index 8). Dry-sim: b-grid → [3,3,3,3,3]; g×0.9 → 3, g×1.1 → 2 (the optimum shifts WITHIN the interior as competition tightens, never to max-audience). DISCLOSED: the specific interior index is competition-scale-dependent; the invariant claim is "interior, not max-audience," not "index 3 exactly."
- **R4 — badge is the sole cause (control).** With b = 0 (badge lift removed), argmax must return to index 8 (max audience) at ≥3σ over index 7, restoring the folk monotone answer. Dry-sim: argmax=8, gap≈182.5 at combined_se≈3.52 → 52σ. Isolates the badge threshold as the sole driver of the inversion.

## Pre-registered decision rule
APPROVE iff R1 ∧ R2 ∧ R3 ∧ R4 all hold on the pinned world; else REJECT with the first failing gate named. Twin evaluators (an R1→R4 if-chain and a table-driven scan) MUST agree on the verdict token and the first-failing gate; disagreement → hard SystemExit (no verdict emitted).

## Disclosed verifier (the sim-lab spec)
One-command, stdlib-only, hermetic Python. Pinned-world constants at file top (T, p0, v0, b, g, H, N_REPS, SEED). Exact Poisson-thinning draws on integer/string-keyed random.Random streams; NO wall-clock/network/git/PYTHONHASHSEED. Emits results.json via json.dumps(sort_keys=True, indent=2) carrying verdict, first_failing_gate, per-category (T, badge, mean, se), the four gate blocks (gap, combined_se, margin_sigma, pass), the R3 argmax sweep vectors, twin agreement, and self_checks. fixtures.json pins the world + a first-rep anchor draw (written on first run, verified thereafter). Double-run must be byte-identical (results-dict sha256 stable). Self-checks (≥12) gate exit 0. Dry-sim reference: results-dict sha256 dc97a537634ebb853d4b6605619a2111d3d3f8f17501aafd5edbe3938bba15e4 (SEED=20260717, N_REPS=400, H=90).

## Why it matters (venture-ops)
Category/BISAC placement is a live, low-cost, high-leverage lever for every title the venture ships — and the default heuristic ("pick the biggest category you fit") is exactly the dominated choice when a badge threshold is in play. The model says: place for the badge, not for raw audience; the largest BADGEABLE pond, not the largest pond, is the target. It also predicts a diagnostic signature — a title that loses its badge should show a traffic-up/sales-down step — that the venture can watch for when a competitor surge pushes it off a category leaderboard.

## Dedup
Distinct decision-object from every venture prior. NOT series-readthrough-saturation-crossover (P086: quality budget across series DEPTH; this is single-title category SELECTION). NOT channel-concentration-vs-diversification (that splits a promo budget across channels; this picks ONE category under a threshold). NOT ku-exclusivity-fork / keyword-tiling / sample-window-toll / bundle-pwyw-lattice / impulse-price-blanket-series-collapse. The novel object: a NON-MONOTONE-in-audience sales function with a discontinuous rank-K badge threshold, yielding an interior optimum. No prior models a badge/leaderboard threshold or a big-pond/small-pond competition race.

## Model basis (declared model-dependence — the P024 discipline)
The badge lift b=1.5, the competition schedule g, and the traffic schedule T are COMMITTED ASSUMPTIONS, not empirically measured from a live storefront. The verdict tests the INTERNAL decision-logic under these committed constants — "does a badge threshold with competition rising faster than traffic produce an interior optimum that dominates the max-audience choice, and does removing the badge restore monotonicity" — not the empirical magnitude of b for any specific store. The world is calibrated (modest linear traffic, steep competition) to exhibit the mechanism cleanly; R3 shows the qualitative conclusion (interior, not max-audience) survives ±10% competition rescaling and a 2× b-range. What would falsify the DECISION claim, not just retune it: a competition schedule rising no faster than traffic (badge never lost → monotone, R4-like) or a badge lift small enough that the traffic gain always dominates the cliff.

## Probe report (v0, 2026-07-17)
> Single-pass battery (panel not escalated: dedup clears against all 28 venture-lab priors by decision-object; kill-test is the R4 control; feasibility/liveness confirmed by a run dry-sim; grounding reachable at idea-engine@6ec7cc8, fetched this session).

**1. What is this really?** A selection problem with a hidden discontinuity: expected sales are non-monotone in category size because a rank-K badge multiplier switches off where competition overtakes your velocity. The decision object is "which browse category," and the folk max-audience rule is dominated.

**2. Is it genuinely new?** Yes — see Dedup. No venture prior models a leaderboard/badge threshold or a traffic-vs-competition race; the closest (series read-through crossover) is about series depth, a different object and a different mechanism.

**3. What would kill it?** The R4 control (b=0) — if the inversion survived removing the badge, the phenomenon would be some other artifact and the idea is INVALID. Dry-sim: b=0 restores argmax=max-audience at 52σ, so the badge is the sole cause. Also killed if competition rose no faster than traffic (badge never lost).

**4. Is it feasible to simulate?** Yes — stdlib-only, exact Poisson thinning, ~2s runtime, 400 reps × 9 categories × 2 badge regimes. Fully specified pinned world; no external data.

**5. What did the dry-sim measure?** All four gates pass with enormous headroom: R1 255σ, R2 479σ, R4 52σ; R3 argmax interior across the entire b-grid and both g-scalings. Badge crossover interior at index 4 (last badged = index 3, T=1400), which is the global optimum. Twin evaluators agree APPROVE / first_failing=None; double-run byte-identical (sha dc97a53…).

**6. What correction was disclosed?** One modeling-mechanics fix, no threshold change: random.Random rejects tuple seeds, so streams are keyed by the string "SEED|c|rep" (sha512-routed, deterministic, PYTHONHASHSEED-independent) — the requested per-(category,rep) independence is preserved. No N_REPS/H bump was needed; margins are orders of magnitude over the 3σ floor. R3 additionally discloses that the interior optimum index (3 vs 2) depends on the competition scale — the invariant is "interior," not a fixed index.

**7. What are the stability bounds / sanity checks?** Sanity: badged expected sales E_c = H·(v0 + 2.5·T_c·p0) and unbadged E_c = H·(v0 + T_c·p0) match the Monte-Carlo means to <0.1% (e.g. index 3: E=3600 vs mean 3600.5; index 8: E=2610 vs mean 2611.6). The badge vector is deterministic and checkable by hand. Margins are σ-scaled against the Poisson SE, not asserted.

**8. How will we know it worked?** V103 reproduces the pinned world one-command, hits verdict=APPROVE / first_failing_gate=None with R1,R2,R4 ≥3σ and R3 argmax interior across all sweeps, twins agree, and the results-dict double-run is byte-identical — reported with the per-category table and the four margins.

## Gate power + margin ledger
| gate | claim | dry-sim margin | floor |
|---|---|---|---|
| R1 | interior optimum dominates max-audience | 255σ (gap 988.9 / se 3.88) | 3σ |
| R2 | badge cliff: traffic-up, sales-down | 479σ (gap 1712.5 / se 3.58) | 3σ |
| R3 | interior across b∈[1,2], g±10% | argmax [3,3,3,3,3]; g×0.9→3, g×1.1→2 | interior ≠ 8 |
| R4 | badge-off restores max-audience | 52σ (gap 182.5 / se 3.52) | 3σ |

**Recommendation: sim-ready**
