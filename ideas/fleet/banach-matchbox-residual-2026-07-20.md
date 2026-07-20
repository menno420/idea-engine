# Banach's matchbox problem — the moment you reach into a pocket and find one of two N-match boxes EMPTY, the OTHER box is almost never empty too: it still holds on average (2N+1)·C(2N,N)/4^N − 1 ≈ 2·sqrt(N/π) − 1 matches (about 7 at N=50), not the ≈0 that the "both boxes drain symmetrically" folk intuition insists on

> **State:** sim-ready
> **Class:** unrelated (round-47 UNRELATED slot)
> **Target:** sim-lab (VERDICT 213, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Banach%27s_matchbox_problem&oldid=1356179739@2a9bfea32a4ea817258b2a97ef8366cbaf7e6ec3 · fetched 2026-07-20
> **Reference (external, reachable):** [Banach's matchbox problem — Wikipedia](https://en.wikipedia.org/w/index.php?title=Banach%27s_matchbox_problem&oldid=1356179739) — live English Wikipedia "Banach's matchbox problem" revision oldid 1356179739; my computed sha1 of the raw wikitext byte-matches MediaWiki's own reported revision sha1 `2a9bfea32a4ea817258b2a97ef8366cbaf7e6ec3` (clean byte-pin). The "Solution" section states the head verbatim: `P[K=k] = C(2N−k, N−k)(1/2)^(2N−k)` (equal to C(2N−k, N)·2^(−(2N−k)) by binomial symmetry, since (2N−k)−(N−k)=N), the asymptotic `2·sqrt(N/π)−1`, and the worked example "starting with boxes with N=40 matches, the expected number of matches in the second box is approximately 7." Caveat: the sha1 pins the raw wikitext (not rendered HTML); the closed forms appear in `<math>` LaTeX markup, and the printed exact-expectation expression carries a wikitext typo (a stray "r"), but the P[K=k] formula and the 2·sqrt(N/π)−1 asymptotic are unambiguous. The exact forward-DP identity and the Monte-Carlo gates below are firsthand.
> **Verifier (firsthand):** ideas/fleet/banach_matchbox_residual.py · results-dict sha256 e162890959eba728cf83004508a213f3585009bcc8fbc6e8bebdab753c576f56

## The phenomenon (one line)
Two matchboxes each start with N matches; each pick takes one match from the left or right box with probability 1/2; the first time a chosen box is found EMPTY, the number K of matches left in the OTHER box is not ≈0 — its expectation is E[K] = (2N+1)·C(2N,N)·2^(−2N) − 1 ≈ 2·sqrt(N/π) − 1, about 7 matches at N=50 and still ~15 at N=200.

## Domain
Probability / everyday life — the residual (negative-binomial) count in the not-yet-empty box of a symmetric two-box depletion process. This is outside fleet-ops and outside venture/game theory; a cross-cutting probability-intuition head (a classic Feller problem, Banach's matchbox), filed in the fleet cross-cutting lane.

## The folk belief
Symmetry says each box is picked equally often, so the two boxes ought to drain in lock-step and empty at essentially the same time — hence when you discover one box empty the other should be empty too, and K should be ≈0. The mental image is "two water levels falling together": find one at the bottom and the other must be at the bottom as well.

## The thesis (reasoned to its fuller form — Q-0254 duty)
The folk image confuses "equal expected draw counts" with "equal realized draw counts at the stopping time," and it ignores that the stopping event is triggered by an OVER-draw, not by an exact tie. Two facts fix it:

- **The trigger is the (N+1)-th pick of a box, not the N-th.** A box is only discovered empty when it is chosen once more after its last match is gone — so at the stopping time the emptied box has been picked N+1 times while the other has been picked some smaller, random number of times. The gap between the two picks is exactly the residual K.
- **That gap is a negative-binomial fluctuation of order sqrt(N).** Treat the other box as effectively unlimited; let M be the number of times it is picked before the emptied box is chosen N+1 times. Then M is the count of successes before N+1 failures in fair Bernoulli trials — negative binomial with p=1/2 — so P[M=m] = C(N+m, m)·(1/2)^(N+1+m), and K = N − M conditioned on this box being the survivor gives

  P[K=k] = 2·P[M=N−k] = C(2N−k, N)·2^(−(2N−k)),  k = 0..N,

  with E[K] = (2N+1)·C(2N,N)·2^(−2N) − 1 ≈ 2·sqrt(N/π) − 1. The typical imbalance between two fair random walks after ~2N steps is Θ(sqrt(N)), not 0 — so the survivor box keeps Θ(sqrt(N)) matches. The symmetry intuition is right about the MEAN pick counts and exactly wrong about the SPREAD at the stopping time, which is where K lives.

## The formal model / Pinned world (committed constants)
- Two boxes, each initially N matches; each step picks left/right with probability 1/2 and removes one match; a box discovered empty (chosen when already at 0 remaining) STOPS the process; K = matches left in the other box.
- N_head = 50 (the reported head); robustness grid N ∈ {10, 50, 200}; SEED = 20260717; TRIALS = 2,000,000 Monte-Carlo simulations at N_head; Z_GATE = 3.0.
- Exact leg (G1) uses fractions.Fraction: a forward dynamic program over states (a,b) = matches already drawn from left/right, processed in increasing (a+b) order, with the four transitions (both-nonempty split; one-box-emptied continue-or-terminate; both-emptied terminate) accumulating exact probability mass into K-bins. Run at N ∈ {10, 50}.
- Ratio statistic (G4): ratio_N = (E[K] + 1)/sqrt(N); band [1.10, 1.20]; must strictly decrease across N=10 > N=50 > N=200 toward 2/√π ≈ 1.128379.

## Pre-registered gates
- **G1 EXACTLY-TRUE (Fraction-exact equality).** For N ∈ {10, 50}: `closed_form_pmf(N) == exact_dp_pmf(N)` elementwise AND `closed_form_EK(N) == Σ k·exact_dp_pmf(N)[k]`, all as fractions.Fraction; each pmf also sums to exactly 1. **PASS DIRECTION:** exact equality — any elementwise or expectation mismatch FAILS. (This is the optimality/identity proof: an independent exact enumeration reproduces the closed form to the last rational.)
- **G2 ≥3σ SIGNAL (folk-belief refutation).** At N=50, TRIALS=2,000,000, z2 = sim_mean / se against the null E[K]=0. PASS iff z2 ≥ 3. **PASS DIRECTION:** LARGE z is the signal — the other box is emphatically NOT empty (expected z ~ hundreds+).
- **G3 AGREEMENT (|z|<3).** z3 = (sim_mean − float(EK_closed(50))) / se. PASS iff |z3| < 3. **PASS DIRECTION:** SMALL |z| — the simulation reproduces the closed-form E[K].
- **G4 ROBUSTNESS/SHIFT.** For N ∈ {10, 50, 200}, ratio_N = (EK_closed(N)+1)/sqrt(N). PASS iff every ratio ∈ [1.10, 1.20] AND the ratios strictly decrease (N=10 > N=50 > N=200) AND every ratio exceeds 2/√π (convergence from above). **PASS DIRECTION:** monotone convergence inside the band = robust across scale.
- **Determinism.** The whole computation runs TWICE in-process; the two canonical results dicts are asserted byte-identical; SEED fixed; cross-invocation digest identical across two separate process runs.

## Pre-registered decision rule
sim-ready iff G1 (Fraction-exact pmf and E[K] equality both N), G2 (z2 ≥ 3), G3 (|z3| < 3), and G4 (all three ratios in band, strictly decreasing, above 2/√π) ALL hold, with a byte-identical results-dict sha256 across an in-process double-run AND a separate cross-invocation. Any gate failing, or any digest drift, blocks. The verifier exits 0 iff all gates hold, exit 1 otherwise.

## Dry-sim results (SEED=20260717, verbatim from banach_matchbox_residual.py)
- **G1 EXACTLY-TRUE:** N=10 and N=50 both `pmf_equal=true`, `ek_equal=true`, `sum_is_one=true` (closed-form pmf == exact forward-DP pmf elementwise as fractions.Fraction; E[K]closed == Σk·pmf) → pass.
- **P(K=0):** at N=50, P(K=0) = 0.079589 (and P(K=1) = 0.079589 — the pmf is flat at its top); at N=10, P(K=0) = 0.176197.
- **E[K] (N=50):** closed form = 7.038513, exact = 1115296899859219265664919877185/158456325028528675187087900672. E[K](N=10) = 2.700138; E[K](N=200) = 14.98759.
- **G2 ≥3σ SIGNAL:** sim_mean = 7.04112, se = 0.003828 → z2 = 1839.497873 ≥ 3 → pass (folk "K≈0" refuted by ~1839σ).
- **G3 AGREEMENT:** z3 = (7.04112 − 7.038513)/0.003828 = 0.681218, |z3| < 3 → pass (simulation reproduces the closed form).
- **G4 ROBUSTNESS:** ratios (E[K]+1)/sqrt(N): N=10 → 1.170086, N=50 → 1.136817, N=200 → 1.130493 — all in [1.10, 1.20], strictly decreasing, each above 2/√π = 1.128379 → pass.
- **Determinism:** in-process double-run byte-identical + separate cross-invocation identical. `results-dict sha256 e162890959eba728cf83004508a213f3585009bcc8fbc6e8bebdab753c576f56` (full 64 hex), all_pass=true, exit 0.

## Honest nuance (disclosed)
- E[K] grows like 2·sqrt(N/π) − 1, so "≈7" is specifically the N=50 value; the residual is unbounded in N (it is small only relative to N, being Θ(sqrt(N))). The head's "≈7" is the pinned N=50 (and, per Wikipedia's own example, N=40) figure, not a universal constant.
- K=0 is not impossible — it is simply not the mode's whole story: P(K=0) ≈ 0.0796 at N=50, so both boxes ARE found effectively empty about 8% of the time; the point is that the MEAN is ~7, not that K is never 0. The pmf is heavily right-shifted, not a spike at 0.
- The clean negative-binomial derivation treats the survivor box as effectively unlimited during the count; the exact forward DP (G1) makes no such approximation and reproduces the closed form to the last rational, so the "unlimited box" device is a derivation convenience, not a modeling assumption in the verified leg.

## Reproduce
```
python3 ideas/fleet/banach_matchbox_residual.py
```
Prints the pretty results dict then `results_sha256=e162890959eba728cf83004508a213f3585009bcc8fbc6e8bebdab753c576f56`; exits 0 iff every gate holds. Run twice — the digest is byte-identical across invocations (SEED fixed).

## Verifier
`ideas/fleet/banach_matchbox_residual.py`, stdlib only (hashlib, json, math, random, fractions). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the compact-canonical sha256 over the results dict is the digest, the dict carries no self field, floats rounded to 6 dp (E[K] additionally stored exact as a "num/den" string), no on-disk JSON, and an in-process double-run asserts byte-identical results. The exact leg is a fractions.Fraction forward DP over drawn-count states (no sampling); the empirical leg is a seeded simulation (no wall-clock).

## Why it matters
The trap is the "symmetry ⇒ simultaneous exhaustion" reflex — reading equal expected pick counts as equal realized counts at a stopping time. Banach's matchbox is the clean counterexample: the stopping event is an over-draw, and the gap between two fair processes at their stopping time is Θ(sqrt(N)), not 0. The transferable lesson for any depletion/threshold system with two symmetric consumers (dual buffers, redundant caches, paired inventories, twin token buckets): when ONE side is first observed exhausted, the other side is NOT near-exhausted — it typically still holds Θ(sqrt(N)) headroom, so "one empty ⇒ both empty" provisioning under-counts the survivor's residual by ~2·sqrt(N/π). Reserve/alarm thresholds keyed to "both drain together" mis-size the surviving buffer.

## Dedup
No Banach / matchbox / residual-in-the-other-box head exists in ideas/ before this (grepped `banach`, `matchbox`, `match box` across ideas/ on this branch — the only hit is this proposal's own verifier `ideas/fleet/banach_matchbox_residual.py`; nothing on origin/main). Distinct from the nearby probability heads in ideas/fleet/: **birthday-collision-sqrt-n** is the sqrt(N) collision THRESHOLD in occupancy (when a duplicate first appears), not the residual after a stopping event; **coupon-collector-tail** is the N·ln N + Θ(N) time to collect ALL coupons (a maximum-of-waiting-times tail), not a two-box imbalance; **german-tank-mvue** is a max-order-statistic point estimate of an unknown N, not a depletion residual; **inspection-paradox-wait-inflation** is length-biased sampling of intervals, not a two-consumer stopping gap. This head is uniquely the exact negative-binomial residual K in the survivor box at the first-empty stopping time, with an exact-pmf == forward-DP identity.

## Model basis (declared model-dependence)
Depends on: (a) exactly two boxes, each starting with the SAME N matches; (b) independent picks, each left/right with probability EXACTLY 1/2 (a biased p breaks the symmetric closed form — the residual law shifts); (c) the stopping rule "first time a chosen box is found empty" (K is defined at that specific stopping time, not at first-emptiness-of-either-count). Change the bias off 1/2, the starting counts to be unequal, or the stopping rule (e.g. stop when a box's last match is TAKEN rather than when the empty box is next REACHED) and the numbers move; the exactly-true G1 identity and the 2·sqrt(N/π)−1 asymptotic are claims about this pinned symmetric-fair-1/2 model. The result is a property of symmetric fair depletion, not a universal law of any two-consumer system.

## Probe report (v0, 2026-07-20)
**1. What is the precise claim, as a mechanism?** When two boxes each start with N matches and each pick removes a match from a uniformly-random side, the first box found empty is discovered on its (N+1)-th pick; the number K of matches left in the OTHER box then has pmf P[K=k] = C(2N−k, N)·2^(−(2N−k)) for k=0..N, with E[K] = (2N+1)·C(2N,N)·2^(−2N) − 1 ≈ 2·sqrt(N/π) − 1 — about 7 at N=50, because the imbalance between two fair processes at the stopping time is Θ(sqrt(N)), not 0.
**2. Why is it counterintuitive — what does naive intuition predict?** Symmetry suggests both boxes drain together and empty simultaneously, so K should be ≈0. Reality: the stopping event is an over-draw (the N+1-th pick), and the survivor box still holds Θ(sqrt(N)) matches — E[K]=7.038513 at N=50, refuted by the simulation at z2=1839.497873σ against the K=0 null.
**3. Is the model clean and stdlib-simulable deterministically?** Yes — two boxes, fair 1/2 picks, a seeded simulation (random.Random(20260717), no wall-clock), stdlib only (hashlib/json/math/random/fractions); the results-dict digest reproduces byte-identically in-process (double-run assert) and across two separate invocations.
**4. Where is the exactly-true content, and how is it gated?** G1: an independent exact forward DP over drawn-count states (fractions.Fraction, no sampling) reproduces the closed-form pmf elementwise AND the closed-form E[K] = Σk·pmf, for N∈{10,50}, with each pmf summing to exactly 1 — a rational identity, `pmf_equal=ek_equal=sum_is_one=true` both N.
**5. What are the ≥3σ empirical gates and their z-scores?** G2 folk-refutation (must be LARGE): z2 = sim_mean/se = 7.04112/0.003828 = 1839.497873 ≥ 3 (the other box is not empty). G3 agreement (must be SMALL): z3 = (sim_mean − E[K]closed)/se = 0.681218, |z3| < 3 (the simulation matches the closed form).
**6. What is the robustness/shift check?** G4: the scale-invariant ratio (E[K]+1)/sqrt(N) across N=10/50/200 = 1.170086 / 1.136817 / 1.130493 — all inside the band [1.10, 1.20], strictly decreasing, and each above 2/√π=1.128379, i.e. monotone convergence to the Stirling limit from above; the phenomenon is not an N=50 artifact.
**7. What could falsify it or where does it break?** Any elementwise pmf mismatch or E[K] mismatch in G1; a wrong-sign or vanishing folk signal (z2<3); a simulation that disagrees with the closed form (|z3|≥3); a ratio out of [1.10,1.20], non-monotone, or below 2/√π; or a digest drift across the double-run/cross-invocation. Biasing p off 1/2, unequal starting counts, or a different stopping rule also moves the numbers (declared model-dependence).
**8. What external source grounds the head, and does it support the specific claim?** English Wikipedia "Banach's matchbox problem" oldid 1356179739, raw wikitext byte-pinned (self-computed sha1 = MediaWiki's reported sha1 2a9bfea32a4ea817258b2a97ef8366cbaf7e6ec3); the "Solution" section states P[K=k] = C(2N−k, N−k)(1/2)^(2N−k) (= C(2N−k,N)·2^(−(2N−k)) by binomial symmetry), the asymptotic 2·sqrt(N/π)−1, and the worked example "N=40 matches ⇒ expected ≈ 7." Caveat: the sha1 pins raw wikitext, not rendered HTML; the formulas are in `<math>` markup and the printed exact-expectation expression carries a wikitext typo (a stray "r"), but the pmf and asymptotic are unambiguous; the exact forward-DP identity and the Monte-Carlo gates are firsthand.

**Recommendation: sim-ready**
