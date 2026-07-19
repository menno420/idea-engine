# Adding a zero-cost shortcut to a congested routing network raises the selfish-equilibrium travel time for every driver

> **State:** sim-ready
> **Class:** counterintuitive-equilibrium / everyday-systems (unrelated slot)
> **Slot:** round-35 unrelated
> **Target:** sim-lab (VERDICT 165, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/80e432d2682e7b602138a91a8cabb14956f27b1c/control/outbox.md @ ae852cc89f270fbf1e3e5ec8822d5d0a2043bb37 (VERDICT 163 mirror = current tail; proposal high-water P150, +13 offset)
> **Reference (external, reachable):** Wikipedia "Braess's paradox" — https://en.wikipedia.org/wiki/Braess%27s_paradox (verified reachable via WebFetch); original: D. Braess (1968), "Über ein Paradoxon aus der Verkehrsplanung"; field cases: Seoul Cheonggyecheon expressway removal (2003), Stuttgart, New York 42nd Street.
> **Harvest source (firsthand):** ideas/fleet/braess_paradox.py + its recorded double-run (this branch).

## The phenomenon (one line)
In a congested network where each driver picks the route fastest *for them*, adding a new zero-cost road can make *everyone's* trip slower — and removing a road can make everyone's trip faster.

## The folk belief
More capacity is never worse: a new shortcut can only help, or at worst do nothing. Engineers who tore out roads (Stuttgart, Seoul, NYC 42nd St) were warned of gridlock; flow improved instead.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Canonical 4-node network S → {A,B} → T with demand D drivers:
- S→A and B→T are congestion-priced: cost = flow / CAP (minutes).
- A→T and S→B are fixed: cost = FIXED = 45 min regardless of load.
Two routes exist: R1 = S→A→T and R2 = S→B→T. Each combines one priced edge and one fixed edge, so by symmetry the user (Wardrop) equilibrium splits demand 50/50:
    t_without(D) = FIXED + D / (2·CAP).
Add a zero-cost link A→B. A third route appears: R3 = S→A→B→T, using *both* priced edges and *neither* fixed edge. Each driver individually reasons: two priced edges beat a 45-min fixed edge, so I switch. As drivers switch, both priced edges carry more flow. At equilibrium every driver is on R3 (for D ≤ FIXED·CAP), both priced edges carry the full demand, and
    t_with(D) = 2·D / CAP.
No one can improve by deviating — switching back to R1/R2 now costs D/CAP + FIXED ≥ 2·D/CAP. The network settled into a *worse* equilibrium than before the road existed, purely from individually-rational choices. Exact piecewise form over the tested window:
    t_with(D) = 2·D/CAP      for D ≤ FIXED·CAP (= 4500)
    t_with(D) = 2·FIXED      for FIXED·CAP < D ≤ 2·FIXED·CAP (4500..9000)
The gap t_with − t_without = 1.5·D/CAP − FIXED (first regime) is positive exactly when D > 30·CAP = 3000 — a congested-enough regime; the honest boundary, disclosed below.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · CAP=100 · FIXED=45 · N_TRIALS=20000 · base demand D~Normal(mean=4000, sd=250) · shifted demand D~Normal(mean=3500, sd=300) · validity window (30·CAP, 90·CAP) = (3000, 9000). Demand redrawn per trial, clamped ≥1.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — the paradox has the right sign.** mean(t_with − t_without) > 0 at z ≥ 3. Observed gap_mean = **+14.983575**, z = **+572.883357**, frac_worse = 1.000000.
- **G2 — the degradation is large, not marginal.** mean(t_with/t_without − 1) > 0.10 at z ≥ 3 (one-sample z vs null 0.10). Observed rel_mean = **+0.229465** (≈ +22.9%), z = **+347.899519**.
- **G3 — robust to a shifted demand distribution.** under D~Normal(3500, 300), mean(t_with − t_without) > 0 at z ≥ 3. Observed gap_mean = **+7.492692**, z = **+236.126110**, frac_worse = 0.951250.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**.

## Disclosed verifier (the sim-lab spec)
`ideas/fleet/braess_paradox.py` — stdlib only (hashlib, json, math, random). Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY. Builds the ordered results dict, asserts an in-process double run is byte-identical, prints the pretty dict and its sha256. Expected results-dict sha256:
    d0e4e57d3ecb455442d44b59ef09092c1ed3a66425501e3c7b18616384605ad0
Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass.

## Why it matters
Braess is the load-bearing counterexample to "adding a resource can't hurt." The same logic — rational agents collapsing onto a locally-cheap shared resource until it degrades for all — recurs beyond traffic: interconnects that worsen power-grid or packet-routing congestion, extra choices that slow a queue, a scheduler "fast path" everyone stampedes. It is a clean, quantitative instance of the gap between selfish equilibrium and social optimum (price of anarchy), grounded in physical road removals that measurably improved flow.

## Dedup (contrast vs prior lane heads)
- vs **coordinated omission (P149)** — a *measurement* artifact (dropped samples hide latency); this is a *strategic-equilibrium* artifact (added capacity, worse outcome). No overlap.
- vs **founder-dilution waterfall (P150)** — venture payoff ordering; no network / equilibrium routing.
- vs **Parrondo-type game (P151, concurrent)** — alternates *losing* games into a *winning* combination (time-mixing); Braess adds a *helpful-looking* edge yielding a *worse* equilibrium (spatial routing). Opposite direction, different domain.
- vs **quota-cliff bunching / Gresham hoarding / Will Rogers stage migration** — incentive-cliff, monetary, and classification-shift effects; none is a congestion-network equilibrium.
- Crossover honesty: Braess is a *price-of-anarchy* phenomenon, adjacent to any prior "selfish vs social" framing, but no prior head models routing flow or a Wardrop equilibrium. Distinct mechanism.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: linear (affine, zero free-flow term) congestion cost, symmetric two-route topology, atomic-demand Wardrop equilibrium, zero-cost shortcut. NOT a claim about a specific real road; the claim is that this documented mechanism is real, sign-correct, large, and robust to demand noise within its validity window. Dependence disclosed: strongly-convex costs or asymmetric topology move the magnitude; the *sign* is structural for the congested regime.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | sign | mean gap > 0, z≥3 | +14.983575 | +572.883357 | PASS |
| G2 | effect size | mean rel > 0.10, z≥3 | +0.229465 | +347.899519 | PASS |
| G3 | robustness | shifted mean gap > 0, z≥3 | +7.492692 | +236.126110 | PASS |

## Probe report (v0, self-adversarial)
**1. Real equilibrium or hand-picked route?** Real Wardrop equilibrium: from the all-R3 profile a unilateral switch to R1/R2 costs D/CAP + FIXED ≥ 2·D/CAP for D ≤ FIXED·CAP — no driver gains; the piecewise branch handles D > FIXED·CAP where R1/R2 re-enter.
**2. Knife-edge at D=4000?** No — G1 samples 20k demands ~Normal(4000,250); every trial shows gap>0 (frac_worse=1.0). A broad regime, not a point.
**3. Where does it break?** Below D = 30·CAP = 3000 the gap is negative — the shortcut genuinely helps at low demand. G3 shifts demand toward that boundary (mean 3500, sd 300); the mean gap stays positive at z=236 but frac_worse drops to 0.951, i.e. ~4.9% of shifted draws fall below 3000 and reverse. Disclosed, not hidden.
**4. z inflated by huge N?** The z is large because the effect is large relative to demand-noise variance, not merely because N=20000. G2's z is against a *non-zero* null (0.10) to test magnitude, not just sign.
**5. Determinism?** SEED pinned; in-process double run asserted byte-identical; cross-invocation double run printed IDENTICAL with sha256 d0e4e57d… A verdict re-run must reproduce that digest.
**6. Cost model rigged?** Textbook Braess instance (CAP=100, FIXED=45, canonical D≈4000 → 65 vs 80 min); no free parameter tuned to force a pass. Constants pinned and stated.
**7. Float ordering perturbing the digest?** All dict floats round()-ed to 6 dp before hashing; sums in fixed trial order; no set/dict-ordering nondeterminism. The in-process assert catches drift.
**8. Real or toy?** Documented field reversals — Seoul Cheonggyecheon removal (2003), Stuttgart, NYC 42nd St closure (1990) — improved flow, the observable signature of exiting the bad equilibrium.

**Recommendation: sim-ready**
