# Derangement routing: when N agents are assigned N tasks by a uniformly-random permutation, the chance that NO agent lands on its own home task is p_N = D_N/N! = Σ(−1)^k/k! — converging to 1/e ≈ 36.8%, and it never decays to 0

> **State:** sim-ready
> **Class:** fleet (round-54 FLEET slot)
> **Target:** sim-lab (VERDICT 242, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Derangement&oldid=1364530247@ba6f5759199b761a56d50342132212bbc99ed505 · fetched 2026-07-20
> **Reference (external, reachable):** [Derangement — Wikipedia](https://en.wikipedia.org/w/index.php?title=Derangement&oldid=1364530247) — supports the head firsthand: the pinned revision states the closed form `D_n = n! \sum_{i=0}^n (-1)^i/i!` and the limit `lim D_n/n! = e^{-1} ≈ 0.367879…` as "the limit of the probability that a randomly selected permutation … is a derangement." Byte-pinned to the raw-wikitext sha1 of the cited revision.
> **Verifier (firsthand):** ideas/fleet/verify_229_derangement_routing.py · results-dict sha256 `1f68c3d1cb6003f6ede1bc1d47e18f27a996bea9fa716f759d38fc2c3832365a`

## The phenomenon (one line)
Shuffle a fleet's task assignment uniformly at random — every agent gets a distinct task — and the chance that *nobody* ends up on their own home task settles at about 37%, no matter how big the fleet, and it is provably NOT the naive "each agent independently misses home" guess.

## Domain
Probability / combinatorics of random permutations — derangements, subfactorials, the rencontres k=0 atom. A fleet-routing instance of the classical hat-check / coincidence problem: a uniform random bijection agents→tasks, and the event "no fixed point."

## The folk belief
Two wrong intuitions: (a) "with a big enough fleet, surely at least one agent always lands on its home task" — people expect the no-match probability to shrink toward 0 as N grows; (b) if pressed for a number, people reach for the independence estimate — each agent misses home with probability (1−1/N), so "nobody home" ≈ (1−1/N)^N. Both are wrong: the true probability floors at 1/e ≈ 0.368 forever, and (1−1/N)^N is a different number that the data rejects decisively.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Model the routing as one uniform random permutation π of {0,…,N−1} (agent i → task π(i)); a *fixed point* π(i)=i is an agent routed to its home task, and a *derangement* (no fixed point) is the "nobody home" event.

1. **The exact probability is the derangement ratio.** The number of fixed-point-free permutations is the subfactorial D_N, so P(no agent home) = D_N/N!. By inclusion–exclusion this equals the alternating partial sum p_N = Σ_{k=0}^{N} (−1)^k/k!.
2. **It converges to 1/e, not 0.** Since e^{−1} = Σ_{k=0}^{∞} (−1)^k/k!, the partial sums converge to 1/e ≈ 0.3678794 extremely fast (the error at N is < 1/(N+1)!). The first folk intuition is inverted: about 37% of routings leave *everyone* off their home task, and that floor never erodes with fleet size.
3. **Two independent exact routes agree.** D_N satisfies both the subfactorial recurrence D_N = (N−1)(D_{N−1}+D_{N−2}) (with D_0=1, D_1=0) and the alternating-sum closed form; computing p_N each way and getting the identical rational is a genuine cross-check, not a restatement.
4. **The naive independence model is a distinct, falsifiable number.** Treating each agent's fixed-point event as independent predicts q_N = (1−1/N)^N. This is close but NOT equal to p_N — at N=7, q_7 = (6/7)^7 ≈ 0.3399 versus the true p_7 = 1854/5040 ≈ 0.3679, a gap of ≈ 0.028 that a large Monte-Carlo sample resolves at tens of sigma. The events are negatively correlated (a permutation constraint), so independence is the wrong model, and the data says so.

Fuller form, one sentence: *the "nobody-home" probability of a uniform random routing is the exact rational p_N = D_N/N! = Σ(−1)^k/k!, converging to 1/e from alternating sides, and it is provably not the independence estimate (1−1/N)^N.*

## The formal model / Pinned world (committed constants)
- Object: uniform random permutation of {0,…,N−1} via a seeded Fisher–Yates shuffle (`random.Random(SEED)`).
- Fixed point: agent i with π(i)=i. Derangement: zero fixed points.
- SEED = 20260717; a single `random.Random(SEED)` is consumed once, in the Monte-Carlo pass; the SAME sample feeds both G2 (exact-model agreement) and G4 (naive-model rejection).
- Exact arithmetic via `fractions.Fraction`; subfactorials via the recurrence, alternating sums as Fractions.
- Committed constants: G1 n = 1..12; G2/G4 N = 7, T = 2,000,000, Z_ACCEPT = 3.0, Z_REJECT = 8.0; G3 second recurrence n = 1..15, 0<p_n<1 for n = 2..15, straddle n = 2..12 against high-order rational bounds on 1/e.

## Pre-registered gates
- **G1 — EXACT identity, two independent routes (Fraction, n=1..12).** For every n, p_n computed as (a) Fraction(D_n, n!) with D_n from the subfactorial recurrence and (b) the alternating sum Σ_{k=0}^n (−1)^k/k! are EXACTLY equal. *Direction:* every n equal; a single mismatch fails.
- **G2 — Monte-Carlo agreement at N=7 (|z| < 3).** T = 2,000,000 seeded Fisher–Yates permutations; phat = derangements/T; z = (phat − p_7)/√(p_7(1−p_7)/T). *Direction:* two-sided consistency with the exact p_7; small |z| = agreement.
- **G3 — invariants / robustness (exact).** The second recurrence D_n = n·D_{n−1} + (−1)^n holds exactly (integers) for n = 1..15; 0 < p_n < 1 for every n ≥ 2 (Fraction); and p_n straddles 1/e with the correct alternating sign — p_even > 1/e > p_odd — verified against tight rational bounds lo < 1/e < hi built from a high-order (order-40) partial sum. *Direction:* every identity exact; any mismatch fails.
- **G4 — falsifiability (naive independence REJECTED).** The naive independence model predicts q_N = (1−1/N)^N. On the SAME MC sample at N=7, z_naive = (phat − q_7)/√(q_7(1−q_7)/T). *Direction:* PASS iff the exact model is accepted (|z| < 3 from G2) AND the naive model is rejected at large |z_naive| (> 8).

## Determinism & digest
`SEED = 20260717`; one `random.Random(SEED)` consumed once (the MC pass is the sole RNG consumer). `build_results()` is a pure function of the seed and fixed constants; `main()` runs it twice in-process and asserts byte-identical canonical JSON, and a separate re-invocation is byte-identical. Whole-dict sha256 over the compact canonical JSON (no self-field), printed as the full 64 hex on stdout:

`results_sha256 = 1f68c3d1cb6003f6ede1bc1d47e18f27a996bea9fa716f759d38fc2c3832365a`

Observed gate results (this pinned world): **G1 PASS** (exact, all n=1..12; p_7 = 1854/5040 = 103/280). **G2** z = −1.151504 (|z| < 3), phat = 0.3674645 over 734,929/2,000,000. **G3 PASS** (second recurrence exact n=1..15; 0<p_n<1 n=2..15; alternating straddle n=2..12). **G4** z_naive = 82.246356 (> 8), q_7 = (6/7)^7 = 0.339917 REJECTED. `all_pass = true`, `first_failing_gate = null`.

## Grounding & scope
Grounding pins English Wikipedia "Derangement" at oldid 1364530247, raw-wikitext sha1 `ba6f5759…99ed505` (27,877 bytes; the API revision sha1 and a self-computed sha1 of the `action=raw` wikitext agree exactly). Quoted vs derived, scrupulously separated:

**On that pinned revision (QUOTED — literally present, matching lines pasted):**
- The alternating-sum closed form: `<math display="block">D_n = n! \sum_{i=0}^n \frac{(-1)^i}{i!}</math> for … n \geq 0` (also appears in the inclusion–exclusion derivation).
- The subfactorial recurrence: `<math display="block">D_n = \left(n-1\right) \bigl(D_{n-1} + D_{n-2}\bigr)</math> for … n \geq 2`.
- The second recurrence: `n \cdot D_{n-1} + (-1)^n & \text{if }n > 0.` (the `\begin{cases}` form with D_0=1).
- The limit as a probability: `\lim_{n\to\infty} {D_n \over n!} = … = e^{-1} \approx 0.367879\ldots.` immediately followed by "This is the limit of the probability that a randomly selected permutation of a large number of objects is a derangement."
- The nearest-integer fact `D_n = [n!/e]` and the subfactorial value D_7 = 1,854 (from the small-n table row `1 || 0 || 1 || 2 || 9 || 44 || 265 || 1,854 …`).
- The hat-check framing itself is named on the page: "Counting derangements … amounts to the hat-check problem …".

**Derived here, NOT on the pinned revision:**
- The **fleet-routing framing** (agents/tasks/home task) — the page uses hats/people, not fleet routing.
- The **specific ratio p_7 = 1854/5040 = 0.367857…** written as a probability (the page tabulates D_7 = 1,854 but never forms this ratio).
- The **naive independence alternative q_N = (1−1/N)^N** and its rejection — the page states no such model.
- Every **Monte-Carlo number** (z = −1.151504, z_naive = 82.246356, phat) — firsthand from the verifier.

Honest posture: the *core mathematical claim* (p_N = D_N/N! = Σ(−1)^k/k! → 1/e, interpreted as the derangement probability) is QUOTED essentially verbatim from the pinned revision; this proposal's firsthand contribution is the fleet-routing framing, the two-route exact reproduction, the seeded Monte-Carlo confirmation, and the pre-registered rejection of the independence model. Nothing is oversold as novel.

## Relationship to the existing hat-check card
This is distinct from `ideas/fleet/hat-check-fixed-points-invariance-2026-07-20.md` (PROPOSAL 204 → VERDICT 217), which pins the fixed-point COUNT as Poisson(1) with mean and variance exactly 1. This slice pins the k=0 atom — the "nobody-home" RATIO p_N — as a two-route exact identity with an explicit independence-model falsifier and different grounding (the "Derangement" article vs "Rencontres numbers"). Complementary, not duplicative.

## Reproduce

```
python3 ideas/fleet/verify_229_derangement_routing.py
# exit 0; prints the results dict, in_process_double_run: IDENTICAL,
# results_sha256: 1f68c3d1cb6003f6ede1bc1d47e18f27a996bea9fa716f759d38fc2c3832365a
# decision: sim-ready
```

## Probe report (v0, self-adversarial)

**1. Is the core identity exactly true (not merely approximate)?** Yes. G1 computes p_n two independent ways (subfactorial recurrence vs alternating sum) as `fractions.Fraction` for n = 1..12 and asserts exact equality — no floats, zero slack (e.g. p_7 = 103/280 both ways).

**2. Could the 1/e be an artefact of the sampler?** No. The value is a counting identity proved exactly in G1/G3; the Monte-Carlo gate G2 only confirms the finite-N ratio agrees (|z| = 1.15), and G3 ties p_n to 1/e by the exact alternating-straddle bound.

**3. What is the most plausible wrong belief this could be confused with?** The independence estimate (1−1/N)^N. G4 pre-registers it as the falsifier and rejects it at z_naive ≈ 82 on the same sample — the two numbers (0.3399 vs 0.3679 at N=7) are decisively distinguished.

**4. Is the verifier deterministic and self-checking?** Yes. Single seeded RNG consumed once in a fixed order; in-process double-run + separate re-invocation both byte-identical; whole-dict sha256 with no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** The closed form, both recurrences, and the 1/e derangement-probability limit are quoted verbatim from the pinned revision; the routing framing, the p_7 ratio, and the falsifier are explicitly flagged derived — the citation is neither over- nor under-claimed.

**6. Does it scale / is it robust?** G3 holds the second recurrence exactly through n=15 and the alternating straddle through n=12; the limit is size-independent by construction and the error at N is < 1/(N+1)!.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong independence alternative and rejects it at z ≈ 82; had the sampler produced an independence-like law, G4 would fire.

**8. Any residual risk before ruling?** The exact gates cover n up to 12–15; the asymptotic 1/e rests on the quoted, exactly-convergent series. Monte-Carlo is confirmatory only, at N=7. No blocker.

**Recommendation: sim-ready**
