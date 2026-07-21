# Erlang-C delay probability: for an M/M/c pool of agents the probability an arriving task must wait (finds all c busy) is exactly C(c,a) — C(2,1)=1/3, C(10,6)=1458/14393 — refuting both "delay = utilization ρ" and "delay = Erlang-B blocking"

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · queueing
**Proposal:** 241 → Verdict 254 (+13 offset)
**Verifier:** [`verify_241_erlang_c_delay.py`](verify_241_erlang_c_delay.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = 4d382264…dc39`

## Claim

Model a pool of **c parallel agents** as an **M/M/c queue**: Poisson arrivals at rate λ, exponential service at rate μ per agent, offered load **a = λ/μ** Erlangs (require **a < c** for stability), utilization **ρ = a/c**. The probability that an arriving task **must WAIT** — it finds all c agents busy — is **exactly** the Erlang-C formula

    C(c,a) = [ a^c/c! · c/(c−a) ] / [ Σ_{k=0}^{c−1} a^k/k!  +  a^c/c! · c/(c−a) ].

(Writing cρ = a, this is Wikipedia's `C(c, λ/μ)` verbatim.) Headline exact rationals:

- C(2,1) = **1/3** (c=2 agents, a=1 Erlang, ρ=1/2),
- C(10,6) = **1458/14393** (c=10 agents, a=6 Erlangs, ρ=0.6).

This **refutes two naive foils**, each evaluated on the same (c=2, a=1) Monte-Carlo sample:

- **(F1) "delay probability = utilization ρ = a/c".** At c=2, a=1 that gives ρ = 1/2, but the true delay probability is 1/3 (1/2 ≠ 1/3).
- **(F2) "delay = blocking, i.e. Erlang-C = Erlang-B".** The loss (blocked-calls-cleared) probability is B(2,1) = 1/5, a **different object** from the delay (queued) probability: 1/3 ≠ 1/5.

## Exact reference

The Erlang-C delay probability C(c,a), computed three independent exact ways (all `fractions.Fraction`, a passed as a Fraction, c an int, a < c required), agreeing bit-for-bit:

    (a) direct      tail = a^c/c! · c/(c−a);  S = Σ_{k=0}^{c−1} a^k/k!;  C = tail/(S+tail)
    (b) Erlang-B    B via B(0,a)=1, B(k,a)=a·B(k−1,a)/(k + a·B(k−1,a));
                    C = B / (1 − ρ(1−B)),  ρ = a/c
    (c) stationary  birth-death weights w_n = a^n/n! (n ≤ c) with geometric tail
                    Σ_{n≥c} w_n = a^c/c! · 1/(1−ρ);  C = P(n≥c) = tail/(head+tail)

Exact identity panel (a < c, a rational), each row `direct == from_b == stationary`:

| c | a | C(c,a) exact |
|---|---|---|
| 2  | 1    | 1/3 |
| 3  | 2    | 4/9 |
| 5  | 3    | 81/343 |
| 10 | 6    | 1458/14393 |
| 10 | 17/2 | 2015993900449/3804757737514 |
| 20 | 15   | 81091461181640625/505465130094278011 |

Erlang-B (the M/M/c/c **loss** system, no queue) is a distinct object: B(2,1) = 1/5 ≠ 1/3 = C(2,1). The direct definition and the birth-death stationary reconstruction both give `tail = a^c/c! · 1/(1−ρ)`, and the Erlang-B bridge `C = B/(1−ρ(1−B))` is the classical loss→delay conversion — all three collapse to the same Fraction.

## Four gates (each in its own direction)

- **G1 — exact identity (direct == from_b == stationary, exact `fractions.Fraction`).** Over the panel {(2,1),(3,2),(5,3),(10,6),(10,17/2),(20,15)} the three independent routes to C(c,a) agree **exactly** (Fraction equality) on every row; `error_count = 0`. Records C(2,1) = 1/3 and C(10,6) = 1458/14393.
- **G2 — Monte-Carlo agreement (PASTA).** A correct FIFO discrete-event M/M/c simulator (c servers, interarrivals ~ Exp(λ), services ~ Exp(μ); on each arrival the number in system is inspected **before** admission, and "must wait" = that count ≥ c). To keep the binomial standard error honest under the queue's arrival-to-arrival autocorrelation, the estimator records every THIN=50-th post-warmup arrival (thinned arrival epochs still satisfy PASTA, so the estimate stays unbiased for C while consecutive recorded samples decorrelate); warm-up = 10 000 arrivals discarded, then MC_N = 200 000 measured arrivals. For (c=2, λ=1, μ=1 → a=1, expect 1/3) z = **−0.2355896857**; for (c=10, λ=6, μ=1 → a=6, expect 1458/14393) z = **0.8459716886**; both |z| < 3 [Z_ACCEPT=3.0].
- **G3 — invariance / robustness (its own direction: time-scale invariance).** C(c,a) is a function of (c, a=λ/μ) only. (i) EXACT: C for (λ,μ) ∈ {(1,1),(3,3),(7,7)} (all a=1, c=2) are the **identical** Fraction 1/3 (`exact_identical = True`, `mismatch_count = 0`). (ii) MC: the DES at (λ,μ)=(3,3) and (7,7) with c=2 each agree with 1/3 at z = **−0.2355896857** and z = **−0.2355896857** — byte-identical to the (1,1) run, because at a=1 the whole sample path scales by 1/λ so the event ordering and every wait decision are literally unchanged (time-scale invariance at the sample-path level); both |z| < 3.
- **G4 — falsifiability (its own direction, on the SAME (c=2,a=1) MC sample).** (F1) naive "delay = ρ = 1/2": z_naive_rho = **−149.2933145858**, |z| ≥ 6 REJECTED [Z_REJECT=6.0]. (F2) naive "Erlang-C = Erlang-B": exactly C(2,1) = 1/3 ≠ 1/5 = B(2,1) (`exact_distinct = True`), and on the same sample z_naive_b = **148.7935533928**, |z| ≥ 6 REJECTED.

All four gates PASS; `all_gates_pass=true, first_failing_gate=null, decision=PASS, results_sha256=4d382264df161dcd033abc0592afc58a84173b58aaf061449d6c7d72d832dc39`. Deterministic: in-process double-run and separate re-invocation byte-identical; `--selfcheck` prints "SELFCHECK: byte-identical".

## Grounding

One pinned Wikipedia revision (API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match):

- **"M/M/c queue"**, oldid 1349283273:
  `https://en.wikipedia.org/w/index.php?title=M/M/c_queue&oldid=1349283273@ec41df9795740aa40235813bf7d391255d8a3873` (15 241 bytes).

- **Quoted** literally on the pinned "M/M/c queue" revision: the delay-probability statement verbatim — "The probability that an arriving customer is forced to join the queue (all servers are occupied) is given by" the exact Erlang-C fraction `C(c,λ/μ) = ((cρ)^c/c!)(1/(1−ρ)) / [ Σ_{k=0}^{c−1} (cρ)^k/k! + ((cρ)^c/c!)(1/(1−ρ)) ]` (with cρ = λ/μ = a, this is C(c,a) verbatim); the name — "referred to as **Erlang's C formula** and is often denoted C(c, λ/μ)"; the utilization and stability — "we write ρ = λ/(cμ) for the server utilization and require ρ < 1 for the queue to be stable"; the birth-death **stationary distribution** π_0 = [Σ_{k=0}^{c−1}(cρ)^k/k! + (cρ)^c/c!·1/(1−ρ)]^{−1} with π_k = π_0 (cρ)^k/k! for k<c and π_0 (cρ)^k c^{c−k}/c! for k≥c; and that the M/M/c/c queue "is also known as the **Erlang-B model**" (confirming Erlang-B as the distinct c=K loss variant that foil F2 conflates).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the **name** "offered load a = λ/μ Erlangs" (the *quantity* λ/μ is quoted — it is the second argument of C and equals cρ — but the symbol/name "offered load a" is ours); the Erlang-B→Erlang-C bridge `C = B/(1−ρ(1−B))` (the page gives the algebraic reciprocal form `1/(1+(1−ρ)(c!/(cρ)^c)Σ…)`, not the loss→delay bridge); "PASTA" (the justification for reading C off arrival-epoch wait frequencies); the exact rational instances C(2,1)=1/3, C(10,6)=1458/14393, and B(2,1)=1/5 (grep 0 for "1/3", "1458", "14393", "1/5"); the two foil numbers (ρ=1/2, Erlang-B=1/5); and every z-value and the digest. Honest posture — the Erlang-C delay formula, its name, ρ=λ/(cμ), the stability condition, and the birth-death stationary law are QUOTED textbook material on the single pinned page; the firsthand contribution is the exact rational instances, the three-route exact cross-check (including the Erlang-B bridge and stationary reconstruction), the correct discrete-event PASTA simulator, the time-scale-invariance leg, and the two falsifications. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes C(c,a) three independent exact ways — the direct Erlang-C sum, the Erlang-B bridge C = B/(1−ρ(1−B)), and the birth-death stationary reconstruction — entirely in `fractions.Fraction`, and they agree bit-for-bit on every panel row (error_count = 0). C(2,1) = 1/3 and C(10,6) = 1458/14393 are exact rationals, no float involved.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The exact identity (G1) is fixed before any RNG is touched. The Monte-Carlo gates (G2/G3) only confirm the *frequency* an arriving task finds all servers busy; by PASTA that frequency estimates C. The simulator is a standard FIFO M/M/c discrete-event loop (c servers via a departure-time heap, a FIFO wait queue, memoryless service assigned at service start), and its estimate lands at |z| < 1 for both headline configs.

**3. What is the most plausible wrong belief this could be confused with?** Two, both pre-registered in G4. "Delay = utilization ρ" — the seductive guess that a pool at 50% utilization makes half its arrivals wait; rejected at |z| ≈ 149 on the same sample where 1/3 agrees at |z| < 1. And "delay = blocking (Erlang-C = Erlang-B)" — conflating the M/M/c queue with the M/M/c/c loss system; B(2,1) = 1/5 ≠ 1/3 exactly, rejected at |z| ≈ 149.

**4. Is the verifier deterministic and self-checking?** Yes. Each Monte-Carlo run consumes its own `random.Random(20260717)`-seeded stream in a fixed event order; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). Exact rationals serialize via `str(Fraction)` and every float (z-values, p_hat) via a fixed `f"{v:.10f}"` string, so the bytes are stable. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate process invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 4d382264df161dcd033abc0592afc58a84173b58aaf061449d6c7d72d832dc39`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and, unusually, tight. The single pinned "M/M/c queue" revision carries the exact Erlang-C delay formula under the literal sentence "the probability that an arriving customer is forced to join the queue (all servers are occupied)", plus its name, ρ = λ/(cμ), the stability condition, and the full birth-death stationary law. Flagged derived-not-quoted: the *name* "offered load a" (the quantity λ/μ is quoted), the Erlang-B→Erlang-C bridge, "PASTA", the exact rational instances, the foil numbers, and the z-values/digest. Neither oversold nor undersold.

**6. Does it scale / is it robust?** The claim is a closed-form probability valid for every (c, a) with a < c. G1 anchors it exactly across c = 2…20 including a non-integer a = 17/2. G3 adds a robustness leg specific to the object: because C depends only on (c, a = λ/μ), rescaling (λ, μ) at fixed a leaves it invariant — verified exactly (identical Fraction 1/3 across three time scales) and via the DES (byte-identical wait decisions, a sample-path-level demonstration of time-scale invariance).

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers two plausible-but-wrong beliefs and refutes both on the same evidence: "delay = ρ = 1/2" (rejected at ≈149σ where 1/3 agrees at <1σ) and "delay = Erlang-B = 1/5" (exact 1/3 ≠ 1/5, and ≈149σ on the sample). A wrong crossing between the delay and loss models, a biased sampler, or an off-by-one in the "all servers busy" test would break the exact G1 identity or push a G2 z past the accept band.

**8. Any residual risk before ruling?** The Monte-Carlo leg uses thinning (record every 50th post-warmup arrival) so the reported binomial standard error is honest under queue autocorrelation — without thinning, a single 200 000-arrival window for the c=10 config carries ≈3× the iid standard error and the naive iid z-gate is not a fair test; thinning restores near-independence and the estimate lands at |z| < 1. The exact identity (G1) is what carries the claim and is RNG-free. The Erlang-C formula, its name, ρ = λ/(cμ), the stability condition, and the stationary law are textbook (Kleinrock; the pinned M/M/c page) and cited as such; the firsthand contribution is the exact rational instances, the three-route cross-check, the PASTA simulator, the invariance leg, and the two falsifications. The paired sim-lab VERDICT 254 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
