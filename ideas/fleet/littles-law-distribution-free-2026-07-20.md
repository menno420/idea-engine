# Change the scheduler, change every wait — but throughput times mean-latency still counts the queue to the bit

> **State:** sim-ready
> **Class:** fleet-ops / queueing / capacity-planning
> **Target:** sim-lab (VERDICT 226, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Little%27s_law&oldid=1362803400@1f5cd6c91d404f83bacff533e81c0c509b973c36 · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 51c34924d9bc600417a69ad84c60780c337efda7d70fd3929e3d2801daf4131f

## The phenomenon (one line)
The time-average number of jobs in a work-conserving queue equals arrival-rate × mean-time-in-system exactly — on every sample path, with no assumption about the service-time distribution or the scheduling discipline.

## The folk belief
"To predict how many requests are in flight (queue depth / concurrency) you must model the service-time distribution and its variance." (The Pollaczek–Khinchine reflex: variance drives waiting, so surely variance drives occupancy.)

## The Little's-law thesis (reasoned to fuller form — Q-0254 duty)
Pollaczek–Khinchine tells you the *mean wait* from the service distribution. But GIVEN the mean time-in-system, occupancy needs zero further distributional input. Little's law L = λW is not an ensemble approximation; in its sample-path (Brumelle H=λG) form it is a bookkeeping identity: the area under the number-in-system curve is, by construction, the sum of the individual sojourn times. It holds for any arrival process, any service distribution, and any work-conserving discipline — and it holds exactly per realization, not merely in expectation.
The non-trivial twist this proposal pins: switch FIFO→LIFO→SIRO→priority on the *same* arrival and service streams and you change who waits, how long each waits, AND the time-average number in system L — yet the final emptying time T (hence λ) is byte-identical, and L = λW holds exactly for every discipline. L and W are discipline-dependent; their relation to λ is not.

## The formal model (committed constants, exact)
Single server, non-preemptive, work-conserving (idle only when no job is present). n customers; arrival times = cumulative non-negative integer gaps; service times = positive integers (rationals via `fractions.Fraction`, so all arithmetic is exact). N(t) = number arrived but not departed. area = integral_0^T N(t) dt computed as an exact step-function integral; T = last departure. Disciplines: FIFO (earliest arrival), LIFO (latest arrival), SIRO (seeded uniform among waiting), priority (seeded random key).

## Pinned world (committed constants)
- SEED = 20260717
- Exact gate: 200 realizations × n=30, gap∈[0,4], service∈[1,7], all four disciplines.
- Robustness gate: 200 realizations × n=30, mean service m=4; deterministic (svc=4) vs high-variance bimodal (svc∈{1,7}, same mean).
- MC gate: M/M/1, ρ=0.7, μ=1, 120000 arrivals, 20000 warmup, 40 time-batches. Closed form L=ρ/(1−ρ)=2.333…; wrong alternative L_q=ρ²/(1−ρ)=1.633….
- Pre-registered thresholds: Z_AGREE=4.0, Z_SEP=6.0.

## Pre-registered gates (sim-ready iff ALL hold, in order)
**G1 — pathwise identity + throughput invariance (exactly-true).** For all 200 realizations and all four disciplines, `area == Σ(dep−arr)` as exact Fractions, AND the final emptying time T is identical across disciplines in every realization. *Direction:* exact equality (zero tolerance); any mismatch fails.
**G2 — non-triviality (L is discipline-dependent).** In >0 realizations, FIFO and LIFO yield different L (area). *Direction:* count > 0 — proves the identity is not holding because the quantities are trivially constant.
**G3 — Monte-Carlo ≥3σ discrimination.** For M/M/1 the batch-means estimate L̂ agrees with the correct closed form (|z_correct| < Z_AGREE) and is separated from the wrong alternative (mean *queue* length) by |z_wrong| > Z_SEP. *Direction:* |z_correct| below Z_AGREE AND |z_wrong| above Z_SEP.
**G4 — robustness + falsifiability.** The identity holds exactly under both deterministic and high-variance service (invariance to service-time variance), and a deliberately perturbed accounting (dropping one sojourn) is rejected (`area != Σ_bad`). *Direction:* exact equality under correct accounting; strict inequality under perturbation.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 all pass AND the results-dict sha256 is identical across an in-process double-run and a separate process invocation.

## Dry-sim results
```json
{
  "determinism_double_run_ok": true,
  "exact_gate": {
    "L_discipline_dependent_count": 200,
    "identity_exact_all": true,
    "lambda_invariant_all": true,
    "n_per_realization": 30,
    "realizations": 200
  },
  "gates": {
    "G1_pathwise_identity_and_lambda_invariance": true,
    "G2_L_discipline_dependent": true,
    "G3_mc_mm1_3sigma_discrimination": true,
    "G4_robustness_and_falsifiability": true
  },
  "mc_gate": {
    "L_hat": 2.303624,
    "L_true_closed_form": 2.333333,
    "L_wrong_alt": 1.633333,
    "n_arrivals": 120000,
    "nbatches": 40,
    "rho": 0.7,
    "se": 0.032095,
    "z_correct_abs": 0.92568,
    "z_wrong_abs": 20.884821
  },
  "robustness_gate": {
    "identity_exact_deterministic_service": true,
    "identity_exact_highvariance_service": true,
    "mean_service": 4,
    "perturbed_accounting_rejected": true,
    "realizations": 200
  },
  "seed": 20260717,
  "sim_ready": true,
  "thresholds": {
    "Z_AGREE": 4.0,
    "Z_SEP": 6.0
  }
}
```
results_sha256=51c34924d9bc600417a69ad84c60780c337efda7d70fd3929e3d2801daf4131f

**Disclosed results-dict sha256 = `51c34924d9bc600417a69ad84c60780c337efda7d70fd3929e3d2801daf4131f`**

## Verifier
`ideas/fleet/littles-law-distribution-free-2026-07-20.py` (stdlib-only).
```reproduce
python3 ideas/fleet/littles-law-distribution-free-2026-07-20.py
# prints the results dict then `results_sha256=<digest>`; exit 0 iff sim_ready and deterministic
```

## Why it matters
Capacity planning for a fleet needs concurrency = throughput × latency, and this says you can read it straight off two black-box measurements (requests/s and mean end-to-end latency) with no model of the service internals, no independence assumption, no distribution fit. It also warns the other way: changing the scheduler to cut tail latency will move your average in-flight count, and the two move in exact lockstep with λ — you cannot lower L and W independently at fixed throughput.

## Dedup
No existing `ideas/**` card covers Little's law (grep: only incidental mentions in palm-spares-insensitivity, bufferbloat, assign-at-merge). Distinct from the built work-conservation card (kleinrock-conservation-zero-sum: unfinished-WORK invariance) — this is the number-in-system accounting identity and its discipline-dependence, a different quantity. Distinct from Erlang-B, hedged-request, USL, two-choices.

## Model basis (declared model-dependence — the P024 discipline)
Assumes a single-server, non-preemptive, work-conserving queue that starts and ends empty over the observation window (so boundary terms vanish and area == ΣW is exact). Size-based/preemptive disciplines (SRPT) can change the number-in-system trajectory and are out of scope of the discipline-invariance-of-T claim; the identity L=λW still holds per discipline whenever the window opens and closes empty. The MC gate assumes M/M/1 stationarity and ρ<1.

## One-line design fix
Instrument throughput and mean latency; multiply for average concurrency — skip the queueing-model fit, and never promise to cut in-flight count and latency independently at fixed load.

## Probe report (v0, 2026-07-20)
**1. Is the head counterintuitive but exactly true under the stated model?** Yes — "occupancy needs no service-distribution model, and the identity is exact per sample path" reads as too-general, yet the area/ΣW bookkeeping makes it exact; G1 confirms zero-tolerance equality.
**2. Is the exactly-true gate genuinely exact (no floating point)?** Yes — G1/G2/G4 use `fractions.Fraction` throughout; equality is bit-exact.
**3. Could the identity be holding trivially (all quantities equal/constant)?** No — G2 shows L differs across disciplines in a positive fraction of realizations (L_discipline_dependent_count=200/200) while the identity still holds.
**4. Does the MC gate have real discriminating power?** Yes — G3 separates the correct L (|z_correct|=0.93 < 4.0) from a plausible wrong alternative (mean queue vs mean system, |z_wrong|=20.88 > 6.0) by >Z_SEP σ, not merely "fails to reject".
**5. Is the result robust to service-time variance?** Yes — G4 holds the identity exactly under deterministic and high-variance bimodal service at equal mean.
**6. Is the grounding citation external and accurately caveated?** Yes — Wikipedia "Little's law" (pinned oldid 1362803400 + raw-wikitext sha1 1f5cd6c91d404f83bacff533e81c0c509b973c36). The page states L=λW and explicitly that "the relationship is not influenced by the arrival process distribution, the service distribution, the service order, or practically anything else" — i.e. distribution-free and service-order (discipline)-free generality of the *relationship*. The page does NOT contain the sample-path / Brumelle (H=λG) per-realization form (the words "Brumelle"/"sample path"/"pathwise" do not appear), nor the experiment showing that L and W individually DEPEND on the discipline while T/λ do not; those two are this verifier's firsthand contribution, not asserted by the page.
**7. Is it deterministic and reproducible cross-invocation?** Yes — SEED=20260717, floats rounded to 6dp before hashing; double-run and separate-invocation digests match (51c34924…).
**8. Is it in-scope (fleet-ops) and non-duplicative?** Yes — capacity/queueing, and no prior Little's-law card exists; distinct from the work-conservation and Erlang-B cards.
**Recommendation: sim-ready**
