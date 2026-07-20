# Letting each request pick its own server pool inflates mean latency to exactly 4/3 of the coordinated optimum — the price-of-anarchy ceiling — and no affine-latency topology does worse: in the tight two-pool Pigou network selfish routing pays average latency 1 against the planner's 3/4, a 33.3% latency tax purely from self-interest

> **State:** sim-ready
> **Class:** counterintuitive-equilibrium / congestion routing games (fleet cross-cutting)
> **Target:** sim-lab (VERDICT 206, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Price_of_anarchy&oldid=1360730011@41ef002fa41f05716003462cc43eb203775b5604 · fetched 2026-07-20
> **Reference (external, reachable):** [Price of anarchy — Wikipedia](https://en.wikipedia.org/w/index.php?title=Price_of_anarchy&oldid=1360730011) — rendered article verified reachable 2026-07-20 via WebFetch, stating the theorem "the pure PoA of any generalized routing problem (G,L) with linear latencies is ≤ 4/3" and "w(f) ≤ (4/3)·min_{f\*} w(f\*)"; the source revision is pinned by sha1 41ef002fa41f05716003462cc43eb203775b5604 of the raw wikitext at oldid 1360730011 (21804 bytes, fetched live 2026-07-20 via action=raw). The ≤ 4/3 bound for linear latencies is on the page; the tight Pigou instance (selfish 1 vs optimal 3/4) and the exact grid-enumeration identity gate are firsthand. Classic sources: A. C. Pigou, *The Economics of Welfare* (1920); Koutsoupias & Papadimitriou, "Worst-case equilibria" (STACS 1999, who coined "price of anarchy"); Roughgarden & Tardos, "How bad is selfish routing?" (JACM 2002, the 4/3 bound for affine latencies).
> **Verifier (firsthand):** ideas/fleet/price_of_anarchy_pigou_bound.py · results-dict sha256 9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda

## The phenomenon (one line)
Route one unit of demand across two parallel server pools whose per-request latency rises linearly with the pool's own load; let each request choose the pool fastest for it, and the selfish equilibrium's average latency is exactly 4/3 of the coordinated optimum in the worst case — a fixed 33.3% tax that no affine-latency topology can exceed.

## Domain
Nonatomic congestion / routing games — the Wardrop selfish-user equilibrium versus the social optimum, and the tight worst-case ratio between them (the price of anarchy). A fleet reading: request dispatch across load-dependent server pools where each request is routed to whatever pool looks fastest right now. Domain-general routing theory, outside the venture and game-theory lanes; it lives in `ideas/fleet/` per the cross-cutting carve-out.

## The folk belief
If every request greedily picks the fastest available pool, the fleet "self-optimizes" — millions of local best-choices ought to add up to the globally best allocation, and any gap between selfish routing and a central planner should be small and shrink as the system scales. Under this belief you never need a coordinator: greedy lowest-latency dispatch is assumed to be at most a rounding error away from optimal, so the only lever worth pulling is adding capacity.

## The thesis (reasoned to its fuller form — Q-0254 duty)
The folk belief is wrong by a bounded-but-real constant, and the bound is exactly 4/3. Selfish routing ignores the *congestion externality*: when a request joins a pool it raises everyone else's latency there, but it optimizes only its own trip, so demand over-piles onto whichever pool is locally cheapest. The canonical witness is Pigou's two-pool network: a "top" pool whose latency equals its load x (so latency ranges 0→1 as it fills) and a "bottom" pool pinned at constant latency 1. Because the top pool is *never slower* than the bottom (x ≤ 1 always), every selfish request takes the top pool; all demand lands there and the equilibrium average latency is 1. A planner minimizing total latency instead splits the demand — send exactly half to each — for average latency (1/2)(1/2) + (1/2)(1) = 3/4. The ratio is 1 / (3/4) = **4/3**, and Roughgarden & Tardos proved this is the *worst* it ever gets for affine (linear) latencies: for every such instance the equilibrium is ≤ 4/3 of optimal.

The 4/3 is not universal, which is what makes it a lever rather than a curse. The loss appears only when the alternative pool is cheap enough to matter: if the constant pool's latency is at least twice the congestible pool's slope, no request and no planner would ever use it, so selfish routing already *is* the optimum (price of anarchy = 1). Between "always paradoxical" and "never paradoxical" sits a smooth band whose loss the closed form pins exactly. The fleet lesson: greedy dispatch across load-dependent pools is provably at most 33% worse than a central planner — and precisely that bad in the tight case — so the fix for the worst regime is coordination (or a congestion toll), not more capacity.

## The formal model / Pinned world (committed constants)
- Two parallel pools carrying a unit of demand; flow on a pool is a Fraction in [0, 1]; a pool's per-request latency is affine in its own flow, latency = a·flow + b. Average latency equals total cost because demand is unit.
- **PIGOU** (the tight instance, and the head): top = (a=1, b=0) so latency = x; bottom = (a=0, b=1) so latency = 1. Selfish avg latency 1, optimal avg latency 3/4, PoA = 4/3.
- **INTERIOR** (both pools congestible, a genuine interior split): top = (1, 0), bottom = (1, 1/2). Selfish equilibrium flow 3/4, avg latency 3/4; PoA = 24/23.
- Closed forms (exact Fraction): selfish flow x_eq = clamp₀¹((a_bot + b_bot − b_top)/(a_top + a_bot)); optimal flow x_opt = clamp₀¹((2·a_bot + b_bot − b_top)/(2(a_top + a_bot))); PoA = totalcost(x_eq)/totalcost(x_opt).
- SEED = 20260717; Z_GATE = 3.0; GRID = 12 (exhaustive rational grid); K_QUANTA = 4000 (best-response granularity); BR_TRIALS = 50; TRIALS = 20000 (random draws for G3 and G4).

## Pre-registered gates
- **G1 — Exactly-true (closed form ≡ exhaustive rational-grid enumeration), PIGOU.** Over the grid {k/12 : k = 0..12}, the minimizer of the Beckmann potential is the selfish-equilibrium flow and the minimizer of total cost is the social-optimum flow. Assert both grid minimizers equal the closed forms exactly (eq flow = 1, opt flow = 1/2), selfish avg latency = 1, optimal = 3/4, and PoA = 4/3 exactly with 4/3 > 1. Exact-Fraction identity, no sampling.
- **G2 — Closed form vs best-response, INTERIOR.** Run sequential single-request best-response over K = 4000 load quanta from BR_TRIALS = 50 random starts/orders. Assert every run converges to the unique pure equilibrium k\* = 3000 (flow 3/4) and average latency exactly 3/4, matching the closed form (a congestion game is a potential game, so best-response converges to pure Nash).
- **G3 — ≥3σ statistical, random Pigou-family instances (paradox band).** TRIALS = 20000 draws with top slope a ∈ [2, 100] and bottom constant c ∈ [1, a−1] (so 0 < c < a, an interior selfish equilibrium). Assert every instance obeys PoA ≤ 4/3 (frac_within_bound = 1.0 — the ceiling is never violated) and carries strictly positive anarchy loss (frac_positive = 1.0), and that the mean loss is ≥ Z_GATE σ above zero (z ≥ 3.0).
- **G4 — Robustness / regime-shift control.** TRIALS = 20000 draws with the constant pool expensive (c ∈ [2a, 5a], so c ≥ 2a). Here neither a request nor a planner would ever use the constant pool, so selfish routing already is optimal: assert PoA = 1 exactly for every instance (frac_efficient = 1.0) and zero loss. Shows the 4/3 effect is regime-specific, not a modeling artifact.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 all pass under SEED = 20260717 with a byte-identical results-dict sha256 across an in-process double-run and a separate cross-invocation. Any gate failing, or any digest drift, blocks.

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/price_of_anarchy_pigou_bound.py)
- G1: eq flow grid = 1 ≡ closed form 1, opt flow grid = 1/2 ≡ closed form 1/2, selfish avg latency = 1, optimal avg latency = 3/4, **price_of_anarchy = 4/3** (1.333333), over 13 grid points, **exact_match = true** → pass.
- G2: closed-form eq flow 3/4, k\* = 3000, br_k_unique = true, converged avg latency = 3/4 ≡ closed form 3/4, optimal avg latency = 23/32, PoA = 24/23 (1.043478), 50 trials, moves_max = 2829 → pass.
- G3: 20000 trials, frac_within_4/3_bound = 1.0, frac_positive_loss = 1.0, mean_loss = 0.148868, std_loss = 0.091804, **z = 229.325562**, max_poa = 1.328904 → pass.
- G4: 20000 control trials, frac_efficient_poa_1 = 1.0, max_loss = 0 → pass.
- all_pass = true. Results-dict sha256 `9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda` (byte-identical across a second process).

## Reproduce
```
python3 ideas/fleet/price_of_anarchy_pigou_bound.py
```
Prints the pretty results dict then `Results-JSON sha256: 9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda`; exits 0 iff all_pass.

## Verifier
`ideas/fleet/price_of_anarchy_pigou_bound.py`, stdlib only (hashlib, json, math, random, fractions). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the compact-canonical sha256 over the results dict is the digest, the dict carries no self field, Fractions serialized as strings, floats rounded 6 dp, no on-disk JSON, in-process double-run asserts byte-identical. Equilibrium and optimum are computed from exact closed forms (Fraction), cross-checked by exhaustive grid enumeration (G1) and by count-based best-response (G2).

## Why it matters
A fleet that dispatches each request to whatever pool looks fastest is running selfish routing, and this bounds exactly how much that costs: at most 4/3 of what a coordinator would achieve — and precisely 4/3 in the tight Pigou regime, where a "free, always-at-least-as-fast" pool becomes a magnet that every request piles onto until it is no better than the alternative it starved. Two operational reads. First, the loss is bounded and constant, not scale-growing: greedy dispatch never does worse than a 33% latency tax under affine latencies, so the question is whether that 33% is worth a coordinator. Second, and sharper, the tax is regime-specific — it vanishes when the alternative pool is expensive enough (PoA = 1) and maxes at 4/3 when the pools are closely matched — so the same closed form tells you *when* coordination (or a congestion-aware toll that biases dispatch off the locally-cheap pool) pays for itself, and when greedy is already optimal and coordination is wasted effort. Capacity added to a selfishly-routed fleet is not the only lever; the routing rule itself is worth up to a third.

## Dedup
No price-of-anarchy / Pigou / selfish-vs-optimal-ratio head exists in ideas/ (grepped `price of anarchy|pigou|4/3|roughgarden|wardrop|social optim` on origin/main; the phrase appears only as a passing mention *inside* the Braess docs, never as its own head, verifier, or number). Distinct from the three shipped Braess heads (braess-paradox-2026-07-19, braess-selfish-routing-trap-2026-07-17, braess-paradox-added-edge-2026-07-13): those prove *non-monotonicity* — adding a zero-cost edge/link RAISES equilibrium latency — a different claim about a different perturbation. This head is the *tight worst-case efficiency ratio* between the selfish equilibrium and the social optimum on a fixed network (the 4/3 bound and its Pigou witness), which the Braess docs explicitly flagged as a separate, un-built follow-up. Distinct also from the two shipped power-of-two-choices heads (two-choices-routing-cliff-2026-07-18, two-choices-marginal-probe-2026-07-19), which concern *randomized balanced allocations* (max load under d-sampling), not equilibrium efficiency, and from kleinrock-conservation-zero-sum (a conservation identity, not an equilibrium ratio).

## Model basis (declared model-dependence — the P024 discipline)
Depends on: (a) affine (linear) per-pool latency — the 4/3 ceiling is specific to affine latencies; degree-d polynomial latencies push the worst-case PoA up (unboundedly as d grows), so a fleet with sharply superlinear pool latency can exceed 4/3; (b) nonatomic demand (a unit split into infinitesimal requests) — the atomic (finitely-many-jobs) worst case for affine latencies is a larger 5/2, so the 4/3 is the fluid limit; (c) the two-parallel-pool topology for the tight witness (the ≤ 4/3 bound itself holds on any network, but the exactly-4/3 case is Pigou). Relax any and the number moves as stated; the claim is the affine-nonatomic tight ratio, cross-checked exactly on the pinned instances.

## Probe report (v0, 2026-07-20)
**1. Is the head crisp and falsifiable?** Yes — a single exact ratio (4/3) with closed forms for the selfish and optimal average latencies and a byte-pinned verifier; any gate failure or digest drift falsifies it.
**2. Is it counterintuitive-but-true?** Yes — the folk belief that greedy local routing self-optimizes is wrong by a provable constant; selfish routing pays exactly 4/3 of the optimum in the tight Pigou case, and the ≤ 4/3 ceiling holds for every affine instance.
**3. Is the model clean and fully pinned?** Yes — two affine pools, unit demand, the PIGOU and INTERIOR instances, SEED = 20260717, GRID/K_QUANTA/TRIALS all committed; equilibrium and optimum come from exact closed forms with nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — G1 exhaustively enumerates the rational grid and matches the closed forms exactly (eq flow 1, opt flow 1/2, PoA = 4/3 as an exact Fraction), no sampling; G2 confirms best-response converges to the exact equilibrium latency 3/4.
**5. Is it deterministic and reproducible?** Yes — results-dict sha256 9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda is byte-identical across an in-process double-run and separate process invocations.
**6. Is the grounding real and external?** Yes, with an honest caveat — Wikipedia "Price of anarchy" (oldid 1360730011, raw-wikitext sha1 41ef002fa41f05716003462cc43eb203775b5604, 21804 bytes, fetched live 2026-07-20) states the ≤ 4/3 bound for linear latencies verbatim; the sha1 pins the raw wikitext SOURCE fetched via action=raw, not the rendered HTML. The specific Pigou two-pool witness (selfish 1 vs optimal 3/4) is not on that page — it is the textbook tight instance (Pigou 1920; Roughgarden & Tardos 2002) and is established firsthand by the exact G1 enumeration gate.
**7. Could it collide with a shipped proposal?** No — no PoA/Pigou head exists; it is distinct from the three Braess heads (non-monotonicity, not the efficiency ratio), the two power-of-two-choices heads (balanced allocations, not equilibrium efficiency), and kleinrock-conservation (a conservation identity). See Dedup.
**8. What would make sim-lab reject it?** A non-reproducible digest, a gate failing under an independent reimplementation, or the closed forms disagreeing with an independent equilibrium/optimum solver at a second instance — the natural sim-lab generalization is to re-derive the Wardrop and social-optimum flows on a fresh affine instance and confirm PoA ≤ 4/3 with the tight case at Pigou.

**Recommendation: sim-ready**
