# Secretary / best-choice optimal stopping: the threshold rule "reject the first r−1, then take the first record" selects the best of n uniformly-ordered rank-observed candidates with probability EXACTLY P(r,n)=((r−1)/n)·Σ_{i=r}^{n} 1/(i−1), optimised at r*(n) → win probability 1/e≈36.8%, provably beating the naive take-first rule (win prob 1/n)

> **State:** sim-ready
> **Class:** fleet (cross-cutting slot — optimal stopping / selection mechanism over a candidate fleet)
> **Target:** sim-lab (VERDICT 246, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Secretary_problem&oldid=1356180684@9257ff8e73001e2b517dca2adab94ea46dc6a7e2 · fetched 2026-07-20
> **Reference (external, reachable):** [Secretary problem — Wikipedia](https://en.wikipedia.org/w/index.php?title=Secretary_problem&oldid=1356180684) — supports the head: the pinned revision states the exact closed form `P(r) = \frac{r-1}{n}\sum_{i=r}^{n}\frac{1}{i-1}`, the special case `P(1)=1/n`, the relative-rank-only stopping strategy, the "reject the first r−1 then take the first candidate better than all preceding" rule, the 1/e≈0.368≈37% asymptotic win probability, and a table of optimal thresholds r for n=1..10 (r=1,1,2,2,3,3,3,4,4,4). Byte-pinned to the raw-wikitext sha1 of the cited revision.
> **Verifier (firsthand):** ideas/fleet/verify_233_secretary_stopping.py · results-dict sha256 `048261949a65653b7ad49d90c4968780cc5af2cb77705c9292d409743da68cac`

## The phenomenon (one line)
Interview n applicants of distinct quality in random order, judging each only by how it ranks against those already seen and deciding on the spot; the strategy "let the first r−1 go, then hire the first one that beats everyone so far" hires the very best with probability P(r,n)=((r−1)/n)·Σ_{i=r}^{n} 1/(i−1), and the best cutoff r*(n) drives that up to ≈36.8% = 1/e — far above the take-the-first-one baseline of 1/n.

## Domain
Optimal stopping / sequential selection — the classical secretary (best-choice) problem: a scheduling/selection mechanism over a fleet of n sequentially arriving candidates, observed only by relative rank, with an irrevocable accept/reject decision at each arrival. The object is the exact finite-n win probability of a threshold (cutoff) rule and its optimiser.

## The folk belief
Two wrong intuitions: (a) "you can't do much better than luck — picking the best out of a long random stream must be near-hopeless, or at best 1/n like grabbing the first one"; (b) "if a rule does work, its success must fade to zero as n grows." Both are wrong: the cutoff rule holds a constant ≈36.8% win probability for every large n (the limit is exactly 1/e), while the naive take-first rule really does fade as 1/n → 0. The gap between a constant and a vanishing rate is the whole point.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Let n candidates of distinct qualities arrive in uniformly random order, each observed ONLY by its relative rank among those already seen; a decision is irrevocable.

1. **Exact finite-n win probability of the threshold rule.** For the rule "reject the first r−1, then take the first candidate better than every one seen so far," the probability it selects the overall-best candidate is EXACTLY P(r,n)=((r−1)/n)·Σ_{i=r}^{n} 1/(i−1) for r≥2, with the degenerate case P(1,n)=1/n ("just take the first candidate"). This is exact for every finite n (no limit yet): candidate at position i is the global best (prob 1/n) and is selected iff the best of the first i−1 lies in the first r−1 (prob (r−1)/(i−1)).
2. **Two independent exact routes agree.** P(r,n) can be computed by brute-force enumeration over ALL n! arrival orders OR by a forward record-indicator dynamic program that multiplies the raw record/no-record factors (1−1/s) without ever invoking the telescoped closed form; getting the identical Fraction across a spread of (r,n) is a genuine cross-check of the identity, not a restatement.
3. **The optimal cutoff and the 1/e asymptote.** The optimal cutoff r*(n) is the smallest r≥1 with Σ_{k=r}^{n−1} 1/k ≤ 1 (equivalently argmax_r P(r,n)); r*(n)/n → 1/e, and the optimal win probability P(r*(n),n) → 1/e ≈ 0.36787944117144233 as n→∞. For n=100 the optimal cutoff is r*=38 with P(38,100)≈0.3710 — already within 0.003 of the 1/e limit.
4. **The naive take-first rule is a distinct, falsifiable number.** The r=1 policy wins with probability exactly 1/n (→0). At n=100 a large Monte-Carlo sample lands the optimal rule on p̂≈0.3708 (agreeing with P(38,100)≈0.3710 at |z|≈0.25) while the naive rule lands on p̂≈0.0099 — statistically consistent with its own 1/100 yet rejecting the optimal target at z≈−334.
5. **Rank-only invariance.** Because only relative rank matters, redrawing candidate qualities from any strictly-monotone distribution (e.g. quality = U³) leaves the win rate statistically unchanged — a robustness signature that the mechanism reads ordinal, not cardinal, information.

Fuller form, one sentence: *the threshold rule's exact win probability is P(r,n)=((r−1)/n)Σ_{i=r}^{n}1/(i−1), maximised at the cutoff r*(n)=smallest r with Σ_{k=r}^{n−1}1/k≤1, giving a win probability that tends to 1/e≈36.8% and provably beats the naive take-first 1/n.*

## The formal model / Pinned world (committed constants)
- Object: n candidates of distinct qualities arriving in uniformly random order, observed only by relative rank; the threshold-r rule rejects the first r−1 then takes the first record (better than all seen). Win = selecting the global best.
- Exact arithmetic via `fractions.Fraction`; brute force via `itertools.permutations`; MC via a seeded `random.Random`.
- SEED = 20260717; each Monte-Carlo pass instantiates its own `random.Random(seed)` so the hashed payload is independent of call order.
- Committed constants: G1 exact enumeration over n∈{4,5,6,7} and all r∈{1..n}; G2/G4 MC at n=100, N=200000 seeded orderings, Z_ACCEPT=3.0, Z_REJECT=6.0; G3(a) exact DP over the same {4,5,6,7} set, G3(b) rank-only MC at n=100, N=200000, quality=U³, independent seed SEED+1.

## Pre-registered gates
- **G1 — EXACT identity, brute vs closed form.** For every n∈{4,5,6,7} and every r∈{1..n}, the empirical win fraction (win_count / n!) as a `Fraction` equals the closed form ((r−1)/n)Σ_{i=r}^{n}1/(i−1) as a `Fraction`; argmax_r of the closed form equals r*(n)=smallest r with Σ_{k=r}^{n−1}1/k≤1; and P(1,n)==Fraction(1,n). *Direction:* every equality exact (no float tolerance); a single mismatch fails. r*={4:2,5:3,6:3,7:3}; P(r*,n)={11/24,13/30,77/180,29/70}.
- **G2 — Monte-Carlo agreement under the optimal rule (|z|<3).** n=100, r*=38; p0=float(P(38,100)); p̂=wins/N; z=(p̂−p0)/√(p0(1−p0)/N). *Direction:* small |z| = agreement.
- **G3 — invariance / robustness (BOTH sub-checks).** (a) An independent forward record-indicator DP (raw (1−1/s) products, never the telescoped form) reproduces P(r,n) as a `Fraction` for all r and all n∈{4,5,6,7}. (b) Rank-only MC: redraw qualities from U³ (strictly monotone, independent seed); the win rate agrees with the SAME p0 at |z|<3. *Direction:* exact DP equality for all (r,n) AND small |z| for the invariance draw.
- **G4 — falsifiability (naive take-first REJECTED).** On the SAME MC sample as G2, the r=1 rule wins at p̂≈1/n; it is (i) statistically consistent with its OWN exact 1/n (|z|<3) yet (ii) REJECTS the optimal target p0=P(r*,n) at |z_naive|≥6. *Direction:* PASS iff the optimal rule is accepted (G2) AND the naive rule both self-anchors and rejects the optimal claim.

## Determinism & digest
`SEED = 20260717`; each MC pass instantiates its own `random.Random(seed)` (G2/G4 share one pass; G3(b) uses SEED+1). `build_results()` is a pure function of the seed and fixed constants; `main()` runs it twice in-process and asserts byte-identical canonical JSON, and a separate re-invocation is byte-identical. Whole-dict sha256 over the compact canonical JSON (no self-field), printed as the full 64 hex on stdout:

`results_sha256 = 048261949a65653b7ad49d90c4968780cc5af2cb77705c9292d409743da68cac`

Observed gate results (this pinned world): **G1 PASS** (exact, all n∈{4,5,6,7}; argmax==r*={4:2,5:3,6:3,7:3}; P(1,n)=1/n; P(r*,n)=11/24,13/30,77/180,29/70). **G2** z_optimal=−0.247895 (|z|<3), p̂=0.370775, p0=P(38,100)≈0.371042778712643 vs asymptote 1/e≈0.36787944117144233. **G3 PASS** (exact DP == closed form all r,n; rank-only invariance z_invariance=0.798199, p̂=0.371905, |z|<3). **G4** z_naive_self=−0.40452 (consistent with 1/100) and z_naive_vs_optimal=−334.317693 (|z|≥6), naive take-first REJECTED. `all_gates_pass=true`, `first_failing_gate=null`.

## Grounding & scope
Grounding pins English Wikipedia "Secretary problem" at oldid 1356180684, raw-wikitext sha1 `9257ff8e73001e2b517dca2adab94ea46dc6a7e2` (46,543 bytes; the API revision sha1 and a self-computed sha1 of the returned wikitext agree exactly). Quoted vs derived, scrupulously separated by literal grep of the pinned wikitext:

**On that pinned revision (QUOTED — literally present, grepped):**
- The exact finite-n closed form `P(r) = \frac{r-1}{n} \sum_{i=r}^{n} \frac{1}{i-1}` and the special case `P(1) = 1/n` ("the only feasible policy is to select the first applicant").
- The relative-rank-only stopping strategy (a strategy that "depends on only the relative ranks … and not on their numerical values") and the rule "rejects the first r−1 … then select the first candidate … better than all preceding ones."
- The 1/e≈0.368≈37% asymptotic win probability, the optimal cutoff tending to n/e, and the max-over-r form `\max_{r} \frac{r-1}{n}\sum_{i=r}^{n}\frac{1}{i-1}`.
- The table of optimal thresholds r for n=1..10 (r = 1,1,2,2,3,3,3,4,4,4; P decimals 1.000,0.500,0.500,0.458,0.433,0.428,0.414,…), so the optimal r values r*(4)=2, r*(5)=3, r*(6)=3, r*(7)=3 are present, computed on the page via argmax.

**Derived here, NOT on the pinned revision (grep count 0):**
- The **Σ-inequality cutoff characterization** "r*(n) = smallest r≥1 with Σ_{k=r}^{n−1} 1/k ≤ 1" — the page obtains r* by argmax / calculus, not this stopping inequality.
- The **specific large-n cutoff and probability** r*(100)=38 and p0=P(38,100)=0.371042778712643 (and its exact rational form) — the page's table stops at n=10.
- The **exact reduced-`Fraction` forms** P(r*,n)=11/24, 13/30, 77/180, 29/70 — the page gives decimals (0.458, 0.433, 0.428, 0.414), not exact rationals.
- The **independent forward record-indicator DP** that multiplies the raw (1−1/s) factors as a second exact route.
- The **naive take-first 1/n falsifier** framed as a pre-registered hypothesis and its Monte-Carlo rejection, the **rank-only invariance experiment** (quality=U³), and **every Monte-Carlo z-value** (z_optimal=−0.247895, z_invariance=0.798199, z_naive_self=−0.40452, z_naive_vs_optimal=−334.317693) — firsthand from the verifier — plus the **results_sha256**.

Honest posture: the *core theory* (the exact closed form, P(1)=1/n, the relative-rank rule, the 1/e≈37% asymptote, and the small-n optimal-r table) is QUOTED essentially verbatim from the pinned revision; this proposal's firsthand contribution is the Σ-inequality cutoff characterization, the two-route exact reproduction (brute n! enumeration + independent record-indicator DP) as exact `Fraction`s, the large-n cutoff r*(100)=38, the seeded Monte-Carlo confirmation and rank-only invariance check, and the pre-registered rejection of the naive take-first 1/n model. Nothing is oversold as novel — the mechanism itself is a textbook result; the exactification, the large-n reproduction, and the falsifier are the firsthand work.

## Reproduce

```
python3 ideas/fleet/verify_233_secretary_stopping.py
# exit 0; prints the results dict, in_process_double_run: IDENTICAL,
# results_sha256: 048261949a65653b7ad49d90c4968780cc5af2cb77705c9292d409743da68cac
# decision: sim-ready
```

## Probe report (v0, self-adversarial)

**1. Is the core identity exactly true (not merely approximate)?** Yes. G1 computes the win count two independent ways — brute force over ALL n! orders vs the closed form — as `fractions.Fraction` for every r and n∈{4,5,6,7} and asserts exact equality (e.g. P(2,4)=11/24 both ways), no floats, zero slack.

**2. Could the 1/e be an artefact of the sampler?** No. The finite-n value is a counting identity proved exactly in G1 and re-derived exactly by the record-indicator DP in G3(a); the Monte-Carlo gate G2 only confirms the n=100 rate agrees (|z|=0.25), and the 1/e asymptote is the quoted calculus limit.

**3. What is the most plausible wrong belief this could be confused with?** The pessimistic "you can't beat 1/n" (take the first candidate). G4 pre-registers it as the falsifier: the naive rule self-anchors on 1/100 (z=−0.40) yet rejects the optimal target at z≈−334 on the same sample — 0.0099 vs 0.371 is decisively distinguished.

**4. Is the verifier deterministic and self-checking?** Yes. Each MC pass uses its own seeded RNG consumed in a fixed order; in-process double-run + separate re-invocation both byte-identical; whole-dict sha256 with no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** The closed form, P(1)=1/n, the relative-rank rule, the 1/e≈37% asymptote, and the small-n optimal-r table are quoted verbatim from the pinned revision; the Σ-inequality cutoff, the large-n cutoff r*(100)=38, the exact `Fraction` forms, the independent DP, the naive falsifier, and every z-value are explicitly flagged derived — the citation is neither over- nor under-claimed.

**6. Does it scale / is it robust?** G1 and G3(a) are exact through n=7; G2 confirms the rate at n=100 already sits within 0.003 of the 1/e limit; G3(b) confirms rank-only invariance under a monotone requality (U³), showing the mechanism reads ordinal information only.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong take-first 1/n alternative and rejects it at z≈−334; had the optimal rule behaved like the naive one, G4 would fire.

**8. Any residual risk before ruling?** The exact gates cover n∈{4,5,6,7}; the 1/e asymptote rests on the quoted calculus limit; Monte-Carlo is confirmatory only, at n=100. No blocker.

**Recommendation: sim-ready**
