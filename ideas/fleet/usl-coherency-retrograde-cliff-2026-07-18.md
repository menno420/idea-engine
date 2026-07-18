# More agents is NOT more throughput — a fleet has an OPTIMAL size and adding agents past it makes it SLOWER: with any pairwise coordination cost, throughput follows the Universal Scalability Law `C(N)=N/(1+α(N−1)+βN(N−1))`, which PEAKS at `N*=√((1−α)/β)` and then DECLINES ("retrograde scaling"). Amdahl only caps speedup at `1/α`; the coherency term `β` makes it fall. On the pinned world (α=0.03, β=0.001 ⇒ N*=31) a 31-agent fleet peaks at ~11× while a 200-agent fleet delivers only ~4.3× — the extra 169 agents roughly HALVE the output. The optimal fleet is finite, and "throw more agents at it" is negative-return past N*.

> **State:** sim-ready
> **Class:** fleet (multi-agent fleet-sizing / parallel-scalability economics) · the coordination-overhead retrograde-throughput cliff (the Universal Scalability Law)
> **Target:** sim-lab (VERDICT 138, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@18c80a1 · fetched 2026-07-18T07:56:53Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Amdahl%27s_law — the parallel-speedup law `S=1/(1−p+p/s)` with the serial-fraction ceiling `S(∞)=1/(1−p)` (the β=0 contention baseline / the G2 control), whose "See also" links the Universal Scalability Law; plus https://en.wikipedia.org/wiki/Neil_J._Gunther — Gunther's "universal law of computational scalability" (the USL, the coherency-term retrograde extension). Both verified reachable 2026-07-18 (WebFetch: Amdahl page confirms the formula and the `1/(1−p)` ceiling; the Gunther page confirms the USL as Gunther's universal scalability law).

## The phenomenon (one line)
Run one coordinated job on a fleet of `N` agents and its relative throughput (speedup) is **not** `N`, and does **not** merely saturate — it follows the **Universal Scalability Law** `C(N)=N/(1+α(N−1)+βN(N−1))`, which **PEAKS at `N*=√((1−α)/β)` and then DECLINES**. On the pinned world (α=0.03 contention, β=0.001 coherency) `N*=31`: throughput peaks at **C(31)≈10.95×** and a 200-agent fleet delivers only **C(200)≈4.28×** — a **2.56×** drop from the peak. Set β=0 (Amdahl only) and the same fleet is monotone-faster (speedup saturates at `1/α≈33×` but never falls) — the retrograde cliff is entirely the coherency term.

## The folk belief
"Agents are fungible horsepower: if one agent does the job in time T, then N agents do it in T/N — throughput scales with the fleet. Worst case (Amdahl) a serial part means you saturate at some ceiling, but you never go BACKWARDS: adding capacity can't make the system slower, so when a job is behind, throw more agents at it. Bigger fleet ⇒ at-least-as-much work done." The intuition treats coordination as free and scaling as monotone — it prices in serialization (Amdahl) at worst, and never the pairwise crosstalk that grows as the SQUARE of the fleet.

## The scalability thesis (reasoned to its fuller form — Q-0254 duty)
Two costs stand between a fleet and linear speedup, and they are qualitatively different. **(1) Contention (α)** — a serial fraction that cannot be parallelized: a shared lock, a single writer, a barrier. Amdahl's law prices exactly this: `C(N)=N/(1+α(N−1)) → 1/α` as `N→∞`. Contention SATURATES throughput (a horizontal asymptote) but never reverses it — with contention alone, more agents is never worse. **(2) Coherency (β)** — the cost of keeping the agents *consistent with each other*: every pair must exchange state (locks, cache lines, gossip, review, merge conflicts), so the coordination work grows like the number of PAIRS, `∝ N(N−1)`. Add that quadratic penalty to Amdahl's denominator and you get the **Universal Scalability Law**

    C(N) = N / (1 + α(N−1) + βN(N−1)).

Because the coherency cost in the denominator grows as `N²` while the useful-work numerator grows only as `N`, `C(N)` cannot be monotone: it rises, peaks, and falls. Rewrite the completion time `T(N)=T(1)/C(N)` (T(1)=1):

    T(N) = (1−α)/N  +  (α−β)  +  βN,

three competing pieces — a parallel term `(1−α)/N` that shrinks with N, a constant `(α−β)`, and a **coherency term `βN` that GROWS linearly with N**. Minimize over N (`dT/dN = −(1−α)/N² + β = 0`) and the optimal fleet size is

    N* = √((1−α)/β),

past which the `βN` coordination cost dominates the shrinking parallel term and every extra agent makes the fleet **slower** — *retrograde scaling*. This is the fact the folk belief misses: it is not that scaling saturates (Amdahl), it is that scaling **reverses** once coordination overhead outweighs marginal parallelism. Two consequences. **(a) The optimum is finite and computable.** `N*=√((1−α)/β)` depends only on the ratio of contention to coherency — at α=0.03, β=0.001, `N*=31`, not "as many agents as you have." **(b) Coherency, not contention, is the culprit.** With β=0 (Amdahl) throughput is monotone up to the `1/α` ceiling; the retrograde peak appears the instant β>0. So "add agents when behind" is right up to N* and *negative-return* past it — the honest read is that a fleet has a throughput-optimal size, and over-provisioning a coordinated job is not merely wasteful (paying for idle agents) but actively **counterproductive** (the agents spend more time coordinating than working).

## The formal model (committed constants — sim-lab must reproduce exactly)
- Contention (serial fraction) `α = ALPHA`; coherency coefficient `β = BETA`. Closed-form speedup `C(N)=N/(1+α(N−1)+βN(N−1))`; completion time `T(N)=(1−α)/N+(α−β)+βN` (T(1)=1); optimum `N*=√((1−α)/β)` rounded to the nearest integer.
- Each fleet realization at concurrency `N` draws its completion time as `T(N) = (1−α)/N·Ā + (α−β)·S + β·B`, with unit-mean parts:
  - `Ā = (1/N)·Σ_{j=1..N} u_j`, `u_j ~ Exp(1)` — the parallel term; the **1/N speedup EMERGES by averaging N per-agent work draws**. A sum of `N` iid `Exp(1)` is exactly `Gamma(N,1)`, so `Σu_j` is sampled as `gammavariate(N,1)` (O(1), distribution-exact — the averaging is intact, not asserted).
  - `S ~ Exp(1)` — the serial/contention constant.
  - `B = Σ_{j=1..N} p_j`, `p_j ~ Exp(1)` — the coherency term; the **linear-in-N coordination cost EMERGES by summing N pairwise-coordination draws** (sampled as `Gamma(N,1)`, mean N).
  - `E[T(N)] = (1−α)/N + (α−β) + βN` is exactly the USL time, so the retrograde peak arises from the competing `1/N`-vs-`βN` draws, not a plug-in of the final curve.
- The Amdahl control passes `β=0`: `T0(N)=(1−α)/N + α` (serial coefficient `α`, no coherency term) — monotone decreasing in N.
- A statistic's mean and standard error are taken over `TRIALS = 400` trials, each the mean of `BATCH = 200` fleet realizations, `se = sample-sd/√TRIALS` (the P104…P124 /se convention: z on an estimated statistic).

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- ALPHA = 0.03 (contention / serial fraction), BETA = 0.001 (coherency coefficient)
- TRIALS = 400 trials, BATCH = 200 fleet realizations per trial
- N_GRID = (1, 2, 4, 8, 16, 24, 31, 48, 64, 96, 128, 200); N_STAR = round(√((1−α)/β)) = 31; N_HI = 200
- SIGMA = 3.0
- Closed-form anchors: `N*=√(0.97/0.001)=31.1448 → 31`; `C(31)=10.954064`; `C(200)=4.276245`; peak/hi ratio `2.561608`; Amdahl ceiling `1/α=33.333`.

## Pre-registered gates (APPROVE iff ALL hold)
- **G1 — retrograde existence (the counterintuitive headline):** the mean fleet completion time at `N_HI=200` EXCEEDS the time at the optimum `N*=31` by ≥3σ. More agents ⇒ MORE time ⇒ LESS throughput past the peak — scaling reverses.
- **G2 — coherency-necessity (control):** with `β=0` (Amdahl only) the mean completion time at `N_HI=200` is LESS than at `N*=31` by ≥3σ (the difference flips sign, z ≤ −3). The SAME fleet is monotone-faster without coherency, so the retrograde is 100% the β term, not fleet size or a sim artifact.
- **G3 — closed-form USL anchor + peak location:** the measured mean time reproduces the USL closed form `(1−α)/N+(α−β)+βN` at both `N*` and `N_HI` (each `|z|<3`), AND the grid argmin of the measured time equals `N*=31` (the throughput peak sits where the USL predicts).

Plus a reported (non-gated) cross-check: the full-grid max `|z|` of measured-vs-closed-form time, and the measured speedup curve `C(N)=T(1)/T(N)` against the USL `C(N)`.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `all_pass` field encodes exactly `G1 ∧ G2 ∧ G3`). Any gate failing → REJECT (the coherency-driven retrograde-cliff claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ on the standard error of the estimated statistic.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- optimum `N* = round(√((1−α)/β)) = 31` (closed form `31.1448`); peak speedup `C(31) = 10.954064`, `C(200) = 4.276245`, **peak/hi ratio 2.561608** — a 200-agent fleet delivers under half the 31-agent peak.
- measured speedup curve `C(N)=T(1)/T(N)`: N=1 → **1.000**, N=16 → **9.510**, N=31 → **11.019** (peak), N=64 → **9.302**, N=128 → **6.114**, N=200 → **4.302** — rises to the peak at 31, then falls (retrograde).
- measured mean time: `T(31) = 0.091285` (cf `0.091290`), `T(200) = 0.233791` (cf `0.233850`); grid argmin at **N=31**.
- **G1 retrograde existence:** mean(T(200) − T(31)) = **0.142452** (se 0.000148) > 0 at z = **959.9168σ** — PASS (adding agents past the peak strictly increases completion time).
- **G2 coherency-necessity (β=0 control):** mean(T0(200) − T0(31)) = **−0.026410** (se 0.000140) < 0 at z = **−189.0673σ** — PASS (Amdahl-only is monotone-faster; the retrograde vanishes without coherency).
- **G3 USL anchor + peak:** `|z_star| = 0.0507 < 3` and `|z_hi| = 0.5417 < 3` and grid argmin = **31** = N* — PASS; full-grid max `|z|` = **1.6993** (the measured time-curve reproduces the USL to within ~1.7σ everywhere).
- all_pass = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = e496837c6dd8bbbaec79701528507185a0a08cb8c008255317d3719d99795557**
  (this is the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` over the results dict BEFORE its `results_sha256` self-field is added — the value the verifier prints as `Results-JSON sha256:`; the P104/P112/P116/P120/P124 SELF-FIELD posture. The pretty-printed on-disk `usl_coherency_retrograde_cliff_results.json` artifact's own `sha256sum` is NOT this digest, and that artifact is not committed.)

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/usl_coherency_retrograde_cliff.py`. Seeds once with SEED=20260717, then over TRIALS=400 trials (each the mean of BATCH=200 fleet realizations) measures the completion time of an N-agent fleet across N_GRID for the USL (β>0) and the Amdahl control (β=0), where each realization draws `T(N)=(1−α)/N·Ā+(α−β)·S+β·B` from unit-mean components (the parallel `Ā` averaging N Exp(1) draws via `Gamma(N,1)/N`, the coherency `B` summing N Exp(1) draws via `Gamma(N,1)`). It evaluates G1/G2/G3 on the /se margin, cross-checks the measured time-curve and speedup-curve against the exact USL closed form, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/fleet/usl_coherency_retrograde_cliff.py
```

Expected: all_pass=true, exit 0, G1 z=959.9168σ, G2 z=−189.0673σ, G3 |z_star|=0.0507 / |z_hi|=0.5417 / argmin=31, full-grid max|z|=1.6993, peak C(31)=10.954064 vs C(200)=4.276245, results-dict sha256 = e496837c6dd8bbbaec79701528507185a0a08cb8c008255317d3719d99795557.

## Why it matters (fleet economics)
Any fleet running a *coordinated* job — agents contending on shared state (a repo, a queue, a status file), reviewing/merging each other's work, gossiping to stay consistent — pays a coherency cost that grows with the number of pairs, so its throughput has a finite optimum `N*=√((1−α)/β)` and DECLINES past it. Decision rule for a coordinator sizing a lane: (1) never assume "more agents = more throughput" — that holds only up to `N*`; past it the fleet spends more time coordinating than working and total output FALLS, so over-provisioning a coordinated job is negative-return, not merely wasteful. (2) Estimate the two coefficients from a scaling curve (contention α from where speedup bends, coherency β from where it PEAKS) and size the fleet at `N*` — the optimum is set by the α:β ratio, not by how many agents exist. (3) To raise the ceiling you must cut β (reduce pairwise coordination: partition the work so agents don't touch shared state, batch/serialize the merges, replace all-to-all gossip with a hub) — adding agents cannot; and (4) a job with genuinely independent sub-tasks (β≈0) is the ONLY regime where "throw more agents at it" scales, and even then Amdahl caps it at `1/α`. The transferable one-liner: coordinated fleets don't scale linearly and don't merely saturate — they have a peak, and the lever past the peak is less coordination, not more agents.

## Dedup
Distinct from the nearby fleet and multi-agent priors:
- **correlated-fleet-variance-floor** (P109, fleet — multi-agent estimation): shares the "adding agents has diminishing/limited returns" flavor but the OBJECT is different — P109 is the VARIANCE of a mean ESTIMATOR (`MSE_N → ρσ²`, a statistical-accuracy floor for averaging noisy estimates, N_eff→1/ρ, still MONOTONE-improving toward a floor), while this is a THROUGHPUT-vs-CONCURRENCY curve (`C(N)=N/(1+α(N−1)+βN(N−1))`, a scalability object) that is NON-monotone — it PEAKS and REVERSES. A variance floor (estimation) ≠ a retrograde throughput cliff (scaling); no shared metric (MSE vs speedup), gate, or anchor (equicorrelation formula vs USL).
- **two-choices-routing-cliff** (P113, fleet — load balancing): a queue-max object (power-of-two-choices, `ln ln n` tail); this is a fleet-SIZING/throughput object. Different mechanism (sampling d workers vs coordination overhead), different anchor (balanced allocations vs USL/Amdahl).
- **variance-blind-provisioning-trap** (fleet — M/M/1 queueing tail), **metastable-retry-storm-collapse** (fleet — congestion feedback / bistability), **checkout-pooling-single-line** (fleet — queue pooling): all queueing/feedback objects about WAIT or congestion under a fixed server count; this is about how TOTAL THROUGHPUT scales with the NUMBER of agents and where it peaks — a scalability curve, not a queue tail or a feedback collapse.
- **cascade-independence-quota** (fleet — sequential Bayesian herding): about information cascades destroying INDEPENDENCE of votes (an accuracy object, majority-vote benchmark); this is a physical THROUGHPUT-scaling object (contention + coherency time), no voting, no herding, no Condorcet — different domain and math.
- **winners-curse-task-auction** (P101), **delegation-loop-collapse** (P105), **hedged-request-tail-cure** (P121, tail LATENCY of a fanned-out request), **checkpoint-interval-optimum** (P117, Young–Daly checkpoint spacing): an auction bias, a delegation-graph collapse, a latency-tail cure, and a checkpoint-interval optimum respectively — none is a speedup-vs-fleet-size curve with a coherency-driven retrograde peak.
- **Amdahl's law itself** is the β=0 SPECIAL CASE (monotone saturation at 1/α) and appears here only as the G2 control — the novel object is the retrograde REVERSAL that the coherency term β adds (the Universal Scalability Law), which Amdahl alone cannot produce.

## Model basis (declared model-dependence — the P024 discipline)
The exact anchor is the Universal Scalability Law `C(N)=N/(1+α(N−1)+βN(N−1))` (Gunther), whose completion-time form `T(N)=(1−α)/N+(α−β)+βN` has the analytic optimum `N*=√((1−α)/β)`; Amdahl's law is the `β=0` sub-case. The claim rests on standard structural choices, all pinned: (a) throughput is limited by an additive serial/contention fraction (Amdahl) PLUS a pairwise-coherency cost that grows as `N(N−1)` — the canonical two-parameter scalability model; heavier coordination topologies change α, β but not the peak-then-decline shape as long as β>0; (b) the simulated completion time is an UNBIASED draw of that model (`E[T(N)]` equals the USL time exactly, by unit-mean Gamma/Exp components), so the anchor gate G3 measures the sim landing on the closed form, and the retrograde peak in G1 EMERGES from the competing `1/N` (averaged parallel work) and `βN` (summed coherency) draws rather than being asserted; (c) the β=0 control isolates coherency as the cause (Amdahl is monotone). The QUALITATIVE claim — a coherency cost makes fleet throughput peak at `N*=√((1−α)/β)` and decline, and Amdahl alone only saturates — is the classical USL/Amdahl result; the pinned constants (α=0.03, β=0.001) just fix `N*=31` and make the anchor exact and the seed reproducible. The claim is scoped: for a job with a serial fraction α and pairwise-coherency coefficient β>0 the relative throughput follows the USL and peaks at `N*=√((1−α)/β)`, demonstrated on the pinned constants, mechanism-explained (competing parallel vs coordination terms) with an Amdahl specificity control — not asserted as the throughput law of every workload.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A scalability claim: the relative throughput of an N-agent fleet on a coordinated job is `C(N)=N/(1+α(N−1)+βN(N−1))` (the Universal Scalability Law), which is NON-monotone — it peaks at `N*=√((1−α)/β)` and then DECLINES, because the coherency cost in the denominator grows as `N²` while useful work grows as `N`. Controls: with β=0 (Amdahl) the same fleet is monotone-faster (saturates at `1/α`, never falls).
**2. What would make it false?** If the many-agent completion time did NOT exceed the `N*` time by ≥3σ (G1 — no retrograde, scaling is monotone), or the β=0 Amdahl control did NOT flip to monotone-faster by ≥3σ (G2 — the drop isn't caused by coherency), or the measured time-curve did NOT reproduce the USL closed form at `N*`/`N_hi` within 3σ or its argmin ≠ `N*` (G3 — wrong law / wrong peak). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, 400 trials × 200 realizations; draw `T(N)=(1−α)/N·Ā+(α−β)·S+β·B` (α=0.03, β=0.001) with `Ā=Gamma(N,1)/N`, `S=Exp(1)`, `B=Gamma(N,1)`; measure the mean time across N∈{1..200}; check T(200)>T(31), the β=0 control reverses, and the curve matches `(1−α)/N+(α−β)+βN` with argmin at 31.
**4. What is the counterintuitive core?** "More agents is more throughput (or at worst saturates)" is wrong — with any pairwise coordination cost, throughput PEAKS at a finite `N*=31` and then FALLS: a 200-agent fleet (**4.28×**) does less than half the work of a 31-agent fleet (**10.95×**). The optimal fleet is finite, and over-provisioning a coordinated job is negative-return, not just wasteful.
**5. Where could I be fooling myself?** The specificity control G2 is the guard against "it's just Amdahl / any big fleet is slow": with β=0 the SAME fleet is monotone-FASTER (mean drop −0.026410, z=−189.07σ), so the retrograde is caused by the coherency term, not fleet size. The anchor is the EXACT USL `(1−α)/N+(α−β)+βN`, and the measured curve matches it to full-grid max |z|=**1.6993** with argmin exactly at N*=31; the sim time is an unbiased draw of the model, so G3 is a genuine landing, not a tautology.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 mean(T(200)−T(31))=0.142452 (se 0.000148) z=**959.9168σ**; G2 mean(T0(200)−T0(31))=−0.026410 (se 0.000140) z=**−189.0673σ**; G3 |z_star|=0.0507, |z_hi|=0.5417, argmin=31, full-grid max|z|=1.6993 — G1/G2 clear their ≥3σ bars by hundreds of σ and the curve matches the USL within ~1.7σ; exit 0; results-dict sha256 e496837c…5557.
**7. What decision does it change?** When sizing a fleet for a coordinated job, don't scale to "as many agents as you have" — estimate `N*=√((1−α)/β)` and stop there; past the peak, adding agents REDUCES throughput. To go faster past N*, cut coordination (partition state, batch merges, hub-not-mesh gossip) to lower β, which raises N* and the peak — adding agents cannot.
**8. How will we know it worked?** The committed stdlib verifier reproduces the retrograde cliff under SEED=20260717 with all three gates holding (G1 late-fleet time above the peak time by ≥3σ, G2 the β=0 control reversing to monotone-faster by ≥3σ, G3 the USL anchor matching at N*/N_hi within 3σ with argmin at N*=31), the measured curve tracking the USL to full-grid max |z|≈1.7, and the results-dict sha256 matching e496837c6dd8bbbaec79701528507185a0a08cb8c008255317d3719d99795557.

## One-line correction
Fleet throughput on a coordinated job is not `N×` and does not merely saturate — with any pairwise coordination cost `β>0` it follows the Universal Scalability Law and PEAKS at `N*=√((1−α)/β)`, then DECLINES, so a fleet has a finite optimal size (here 31) and adding agents past it makes the fleet slower; the lever beyond the peak is less coordination (lower β), not more agents.

**Recommendation: sim-ready**
