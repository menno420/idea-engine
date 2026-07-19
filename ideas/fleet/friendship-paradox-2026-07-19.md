# PROPOSAL 164 — friendship paradox: your friends have more friends than you do; averaged over the endpoints of a uniformly random friendship a person has E[k] + Var(k)/E[k] friends, strictly more than the E[k] friends of a uniformly random person whenever degrees vary, because following a friendship is a size-biased draw that over-represents high-degree people (Feld 1991)

> **State:** sim-ready
> **Class:** fleet · network science / social-network sampling · size-biased (length) sampling of a degree distribution
> **Slot:** round-38 UNRELATED
> **Anchor:** a uniformly random edge-endpoint has the size-biased degree law, whose mean is <k^2>/<k> = E[k] + Var(k)/E[k]; so the mean friend is more connected than the mean person by exactly the degree variance-to-mean ratio, a non-negative gap that is strict for any degree spread and grows with the tail
> **Target:** sim-lab (VERDICT 177, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Friendship_paradox@1358630351 · fetched 2026-07-19T09:38:47Z
> **Reference (external, reachable):** Wikipedia, "Friendship paradox" — fetched live HTTP 200 at revision 1358630351; the article states "most people have fewer friends than their friends have, on average" and derives the mean friend degree by choosing a uniformly random edge and endpoint, invoking the variance of the degrees to express the expected friend degree as the mean plus a variance-over-mean term. Origin: Scott L. Feld (1991), "Why Your Friends Have More Friends Than You Do," American Journal of Sociology 96(6):1464-1477.
> **Verifier (firsthand):** `ideas/fleet/friendship_paradox.py` · results-dict sha256 `0df9954e7378ae4c896e892c4614ff2967a117b646276fdde3f21ec874b0bd4f`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Pick a random person in a social network (mean degree mu = <k>); pick a uniformly random one of their friends, and that friend's expected degree is nu = <k^2>/<k> = mu + Var(k)/mu — strictly larger than mu for any network whose degrees are not all identical. On average your friends are more popular than you, and the gap is exactly the degree variance divided by the degree mean.

## The folk belief
"On average I have about as many friends as my friends do — popularity is symmetric, so my friend count and my friends' friend counts should match." This is the equal-popularity null, and it predicts a zero gap. It is false for every network with degree spread: a high-degree person is a friend of many people, so when you sample a person BY FOLLOWING A FRIENDSHIP you over-count the popular ones — the friend you land on is drawn size-biased (proportional to degree), not uniformly. The average person is typical; the average friend is not, and the systematic difference is Var(k)/E[k], zero only when everyone has the identical degree.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Take any undirected network with degree sequence {k_i}. Two different sampling rules give two different "typical degrees":

    random PERSON:  choose a node uniformly            => mean degree  mu = (1/N) sum k_i = <k>
    random FRIEND:  choose a uniformly random edge,    => the endpoint's degree is size-biased:
                    then a uniformly random endpoint       P(pick node i) = k_i / sum_j k_j
                                                           => mean degree  nu = sum k_i^2 / sum k_i = <k^2>/<k>

Because <k^2> = <k>^2 + Var(k), the friend mean factors exactly:

    nu = <k^2>/<k> = <k> + Var(k)/<k> = mu + Var(k)/mu.

So the friendship-paradox gap is

    nu - mu = Var(k)/mu  >= 0,   strict whenever Var(k) > 0.

The gap is not a behavioural tendency or a sampling artifact — it is an algebraic identity of the degree distribution. It is zero only for a regular graph (all degrees equal) and grows without bound as the degree tail gets heavier (Var/mu increases). This is the same length-biased-sampling mechanism as the waiting-time / inspection paradox (a random instant lands in a long inter-event gap more often than a short one): following an edge is a size-biased draw on nodes.

Concretely (SEED = 20260717, R = 40 independent networks of N = 4000 nodes, degrees k_i = max(1, round(2 * Pareto(alpha)))): at alpha = 3.5 the measured friend-minus-person gap is 0.575478 (gap_se 0.012362, z = +46.553724 against the zero-gap null, every one of the 40 networks positive); a size-biased Monte-Carlo estimate of the friend mean over 20000 random edge-endpoints per network agrees with the closed form <k^2>/<k> at a mean standardized residual z = -0.867047 (|z| < 3); and under a HEAVIER tail alpha = 2.6 the gap grows to 2.011742 (z = +11.565060) — bigger, as Var/mu predicts, and still >= 3 sigma positive.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Draw N node degrees iid: k_i = max(1, round(DEG_SCALE * X)) with X ~ Pareto(alpha) via `random.paretovariate(alpha)` (alpha > 2 keeps the degree variance finite). This is a heavy-tailed but finite-variance stand-in for a social-network degree distribution.
- random PERSON mean: mu = mean(k_i). random FRIEND closed form: nu = sum(k_i^2) / sum(k_i) = <k^2>/<k>. Degree variance: Var = <k^2> - mu^2. Identity under test: nu - mu = Var/mu.
- A random friend is drawn size-biased with `random.choices(population=degrees, weights=degrees, k=TRIALS)` — the exact law of a uniformly random edge-endpoint — and its sample mean estimates nu with SE sqrt((<k^3>/<k> - nu^2)/TRIALS).
- Base condition: alpha = 3.5 (feeds G1 head + G2 mechanism). Shift condition: alpha = 2.6, heavier tail (feeds G3 robustness).
- **Model note (declared):** the head is an objective identity of the degree distribution — mu and nu are pure functionals of {k_i}, and nu - mu = Var/mu is exact (measured identity residual 0.0). The single declared modelling choice is the degree distribution (Pareto-tailed integer degrees); the SIGN of the effect (friend mean > person mean) is distribution-independent because it follows from Var(k) >= 0, and G3 re-derives it under a different, heavier tail.

## Pinned world (committed constants)
- SEED = 20260717
- Z_GATE = 3.0
- R = 40 (independent networks per condition)
- N = 4000 (nodes per network)
- TRIALS = 20000 (size-biased draws per network for G2)
- ALPHA_BASE = 3.5, ALPHA_SHIFT = 2.6, DEG_SCALE = 2.0
- Identity: nu - mu = Var(k)/mu (measured max abs residual 0.0)

## Pre-registered gates (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate = 3.0)
- **G1 — head (paradox is positive, >=3 sigma).** Across the R base networks the friend-minus-person gap nu - mu is strictly positive in EVERY network and its mean is >= 3 sigma above the equal-popularity null 0: z = gap_mean / gap_se >= 3. (Measured gap_mean = 0.575478, gap_se = 0.012362, z = +46.553724, all_networks_positive = true.)
- **G2 — mechanism (size-biased sampling closed form).** A size-biased Monte-Carlo estimate of the friend mean matches the closed form nu = <k^2>/<k> within sampling error; the mean standardized residual PASSES when |z| < 3 — validation that the paradox IS length-biased sampling, not an artifact. (Measured mean standardized residual z = -0.867047.)
- **G3 — robustness (heavier tail, >=3 sigma).** Re-run the head under a HEAVIER-tailed distribution (alpha = 2.6) and confirm the gap is >= 3 sigma positive AND strictly LARGER than the base gap (Var/mu grows with the tail). (Measured gap_mean = 2.011742 > base 0.575478, z = +11.565060, heavier_tail_bigger_gap = true.)

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing => REJECT/REVISE naming first_failing_gate. Observed all_pass = true, first_failing_gate = null.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "first_failing_gate": null,
  "g1_paradox_positive": {
    "all_networks_positive": true,
    "equal_popularity_null": 0.0,
    "gap_mean": 0.575478,
    "gap_se": 0.012362,
    "pass": true,
    "z": 46.553724
  },
  "g2_mechanism_size_bias": {
    "closed_form": "nu = sum(k^2)/sum(k) = <k^2>/<k>",
    "mean_std_residual_z": -0.867047,
    "note": "two-sided match test; PASS when |z| < 3",
    "pass": true
  },
  "g3_robust_shift": {
    "all_networks_positive": true,
    "gap_mean": 2.011742,
    "gap_mean_base": 0.575478,
    "gap_se": 0.17395,
    "heavier_tail_bigger_gap": true,
    "pass": true,
    "z": 11.56506
  },
  "gates": [true, true, true],
  "params": {
    "N": 4000, "R": 40, "TRIALS": 20000,
    "alpha_base": 3.5, "alpha_shift": 2.6, "deg_scale": 2.0
  },
  "proposal": 164,
  "seed": 20260717,
  "sigma_gate": 3.0,
  "slot": "round-38 UNRELATED (network science / social-network sampling)",
  "theory": {
    "gap_equals_var_over_mean": "nu - mu = Var(k)/mu",
    "identity_max_abs_residual": 0.0,
    "var_over_mean_mean_base": 0.575478
  }
}
Results-JSON sha256: 0df9954e7378ae4c896e892c4614ff2967a117b646276fdde3f21ec874b0bd4f
```
Results-dict sha256: `0df9954e7378ae4c896e892c4614ff2967a117b646276fdde3f21ec874b0bd4f` (deterministic double-run, exit 0 both times, two cross-invocation stdouts byte-identical).

## Verifier
`ideas/fleet/friendship_paradox.py` — stdlib only (`math, json, hashlib, random`). Draws R = 40 independent networks of N = 4000 Pareto-tailed integer degrees under one seeded stream; for each computes the exact person mean mu and friend mean nu = <k^2>/<k>, the gap and its Var/mu identity, and a size-biased Monte-Carlo friend-mean over TRIALS = 20000 random edge-endpoints. Runs three ordered z-gates (G1 gap > 0 across all networks at z >= 3; G2 size-biased MC matches the closed form nu at |z| < 3; G3 the same head under a heavier tail alpha = 2.6, gap >= 3 sigma AND larger). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact-canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture). Writes no JSON to disk; asserts the in-process double-run digests are identical before printing.

## Reproduce
```
python3 ideas/fleet/friendship_paradox.py
```
Expected: prints the results JSON, `Results-JSON sha256: 0df9954e7378ae4c896e892c4614ff2967a117b646276fdde3f21ec874b0bd4f`, exit 0 (all_pass=true).

## Why it matters (network science / sampling)
Any procedure that reaches people by following their connections inherits this size-bias. (1) Immunization and intervention: vaccinating a random person's random FRIEND targets a higher-degree, more-central node than vaccinating a random person — the friendship-paradox nomination strategy detects outbreaks earlier for free, because the friend you name is drawn size-biased toward the hubs that spread disease. (2) Survey and estimation bias: respondent-driven / snowball sampling that recruits via social ties over-represents high-degree respondents by Var(k)/E[k], so naive estimates of the mean degree (and anything correlated with it) are inflated unless the size-bias is corrected. (3) Perception: on any platform where you see your friends' friend counts (or followers), the feed is a size-biased sample, so "everyone is more connected than me" is the mathematically expected feeling, not evidence you are unpopular. The right instrument is the variance-to-mean ratio of the degree distribution, not the mean alone.

## Dedup (contrast vs prior fleet heads)
- vs **regression-to-mean (P108) / German-tank MVUE (P120) / Stein shrinkage (P128)** — those are estimation-bias and selection-on-extremes results about ESTIMATORS of a fixed parameter; this is a SAMPLING identity: two sampling rules on the same fixed network give means separated by Var/mean. No estimator is being corrected; the gap is exact.
- vs **arcsine lead illusion (P116) / Cauchy no-averaging (P160)** — those are order-statistics / heavy-tail results about a sequence of i.i.d. draws; this is a size-biased draw on a degree distribution (length bias), a different mechanism from the arcsine lead law and the LLN failure.
- vs **Braess's paradox / two-choices routing / Erlang-B** — those are network EQUILIBRIUM / load-balancing results about flows and blocking; this is a static property of the degree distribution's first two moments, no dynamics.
- Crossover honesty: the effect GENERALIZES to the "generalized friendship paradox" — any node attribute x positively correlated with degree (citations, followers, income) is over-stated among friends by Cov(x,k)/E[k] — and to the waiting-time/inspection paradox (the same length bias on inter-event gaps). The VERIFIED claim here is the DEGREE friendship paradox (gap = Var(k)/E[k]); the attribute and waiting-time generalizations are disclosed as crossovers, not asserted.

## Model basis (declared model-dependence — the P024 discipline)
The head is an **objective identity of the degree distribution**, not a behavioural claim: mu = <k> and nu = <k^2>/<k> are pure functionals of the degree sequence, and nu - mu = Var(k)/mu is exact (measured identity residual 0.0), so the friend mean strictly exceeds the person mean whenever Var(k) > 0 — confirmed by the size-biased Monte-Carlo anchor (G2 matches nu at |z| = 0.87). The **one declared modelling choice** (flagged, not hidden): the degree distribution is Pareto-tailed integer degrees; the SIGN of the effect is distribution-independent (it follows from Var(k) >= 0), and G3 re-derives it under a different, heavier tail. Dependence disclosed: (a) the identity is for the GLOBAL edge-endpoint sampling rule; Feld's per-person "mean of your friends' degrees averaged over people" statistic is a closely related but distinct average that also exceeds mu for any non-regular graph — both express the same size-bias, and the global edge-endpoint form is the clean closed-form used here; (b) real networks add degree-degree correlation (assortativity) that can further shift the per-person magnitude, but not the SIGN. The magnitudes (gap 0.575 base, 2.01 heavier tail) are pinned to (alpha, DEG_SCALE, N); the SIGN and the Var/mean scaling are structural to size-biased sampling.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | head + separation | z >= 3, gap > 0 all nets | gap_mean 0.575478 | +46.553724 | PASS |
| G2 | mechanism anchor | \|z\| < 3 vs <k^2>/<k> | residual mean | -0.867047 | PASS |
| G3 | robustness (heavier tail) | z >= 3, gap > base | gap_mean 2.011742 > 0.575478 | +11.565060 | PASS |

## Probe report (v0, self-adversarial)
**1. What is this really?** A size-bias identity. Two sampling rules on the same network — uniform person vs uniform edge-endpoint — give mean degrees mu and <k^2>/<k>, separated by exactly Var(k)/mu. Following a friendship over-samples the popular, so the average friend is more connected than the average person.
**2. What would make it false?** If the friend-minus-person gap were NOT positive across networks (G1 — the head is wrong), or if the size-biased Monte-Carlo friend-mean did NOT match the closed form <k^2>/<k> (G2 — the mechanism is not length bias), or if a heavier tail did NOT keep the gap >= 3 sigma positive and larger (G3 — the Var/mean scaling is an artifact of alpha=3.5). Any of G1/G2/G3 failing => REJECT.
**3. Simplest version that still bites?** A network of 4000 people; a random person has mu friends, but a random FRIEND has 0.58 more friends than that, on average — and nobody's network was rigged: the gap is just the degree variance over the degree mean.
**4. What is the counterintuitive core?** "Popularity is symmetric" is inverted: it is not, because you meet friends by following edges, and edges terminate on popular people more often. The bias has a closed form, Var(k)/E[k], and is zero only if literally everyone has the same number of friends.
**5. Where could I be fooling myself?** The G2 anchor is a TWO-SIDED test (small |z| = MC matches the closed form), so it cannot be inflated into a false pass by large TRIALS — a wrong mechanism shows |z| >> 3. G1/G3 are one-sided separations whose z is large because the effect is real and the network-to-network variance of the gap is small, not because of over-precision; the identity residual 0.0 confirms nu - mu is genuinely Var/mu, not a coincidence.
**6. Determinism?** SEED = 20260717 pinned; one `random.Random(SEED)` stream; in-process double run asserted byte-identical before hashing; cross-invocation double run printed IDENTICAL stdout with sha256 0df9954e...b0bd4f. All dict floats round()-ed to 6 dp; sums accumulated in fixed order; compact JSON with sort_keys; `random.choices` / `random.paretovariate` are the only stochastic calls.
**7. Real or toy?** The friendship paradox is a load-bearing, empirically validated network fact (Feld 1991; the basis of friendship-nomination outbreak detection, Christakis & Fowler 2010) and the size-bias correction is standard in respondent-driven sampling. The Var/mean identity is textbook (Wikipedia, "Friendship paradox"). Not a toy.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED = 20260717, the paradox head (G1), the size-biased-sampling mechanism anchor (G2), and the heavier-tail robustness head (G3) at Z_GATE = 3.0, with the results-dict sha256 matching 0df9954e7378ae4c896e892c4614ff2967a117b646276fdde3f21ec874b0bd4f across a deterministic double-run.

## One-line design fix
When you sample or intervene by following social ties, price the size-bias: a random friend's expected degree is E[k] + Var(k)/E[k], not E[k] — use the degree variance-to-mean ratio to de-bias mean-degree estimates, or to deliberately target the hubs a friendship-nomination reaches for free.

**Recommendation: sim-ready**
