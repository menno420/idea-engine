# The service-variance wait tax: same load, same mean service, yet queue wait runs 2× to 5× longer — the M/G/1 factor (1+C²)/2 that no utilization dashboard shows

> **State:** sim-ready
> **Class:** fleet / distributed-systems queueing latency (round-32 FLEET slot)
> **Target:** sim-lab — VERDICT 150 (PROPOSAL 137 → VERDICT 150, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@8c7d2b5 · fetched 2026-07-18T15:07:28Z
> **Reference (external, reachable):** Pollaczek–Khinchine mean-value formula (Kleinrock, Queueing Systems Vol.1, 1975, §5.6) — https://en.wikipedia.org/wiki/Pollaczek%E2%80%93Khinchine_formula
> **Verifier (firsthand):** ideas/fleet/service_variance_wait_tax.py · results-dict sha256 `ab44d56a22c24f83c4a2048af56dc3dbdbf462d3aa9990bd19c64426891e4307` (SEED=20260717, N_JOBS=600000, WARMUP=150000, REPLICATIONS=30)

## The phenomenon

A single-server FIFO queue fed by Poisson arrivals (an M/G/1 queue) has a mean queue wait that scales with the VARIANCE of its service time, not just its mean. Two servers with identical arrival rate and identical average job can wait wildly different amounts.

## The folk belief

"Same utilization + same mean service ⇒ same latency." Operators read a utilization/throughput dashboard, see two servers both at ρ=0.8 processing jobs that average 1 time-unit, and conclude the two queues feel the same — and that adding identical capacity helps them equally.

## The probabilistic thesis (Q-0254)

For an M/G/1 FIFO queue the Pollaczek–Khinchine mean-value law gives mean queue wait W_q = (ρ/(1−ρ))·E[S]·(1+C²)/2, where C²=Var(S)/E[S]² is the squared coefficient of variation of SERVICE time. Hold ρ and E[S] fixed and W_q depends ONLY on C²: the term (1+C²)/2 is a multiplicative *variance tax*. At ρ=0.8, E[S]=1.0 the wait is exactly 2.0 for deterministic service (C²=0), 4.0 for exponential (C²=1), and 10.0 for a C²=4 hyperexponential — a 1 : 2 : 5 spread. Same load, same average job, 5× the queue wait; and because the tax is multiplicative, adding identical capacity to both leaves the high-variance server proportionally worse. Capacity math that watches only ρ and throughput never sees it.

## The formal model

- Single-server FIFO queue, Poisson arrivals at rate λ (interarrival T~Exp(λ)), general service time S. Utilization ρ=λ·E[S].
- Pollaczek–Khinchine mean queue wait: W_q = (ρ/(1−ρ))·E[S]·(1+C²)/2, with C²=Var(S)/E[S]².
- Equivalently W_q = λ·E[S²]/(2(1−ρ)), since E[S²]=E[S]²(1+C²): the wait reads the second moment of service.
- Three service laws, all with mean m=1.0: **D** constant m (C²=0); **M** exponential rate 1/m (C²=1); **H2** balanced-means two-phase hyperexponential with C²=4.
- H2 closed form: p1=0.5·(1+√((C²−1)/(C²+1)))=0.8872983346 for C²=4, p2=1−p1; branch means 1/μ1=m/(2p1)=0.5635083269, 1/μ2=m/(2p2)=4.4364916731. This yields mean m=1.0 and C²=4 exactly (E[S²]=(m²/2)/(p1·p2)=(0.5)/0.1=5.0 ⇒ Var=4 ⇒ C²=4).
- Measurement: the exact single-server Lindley recursion W_1=0, W_{i+1}=max(0, W_i + S_i − T_i) — exact for M/G/1 FIFO, no event heap needed.

## Pinned world

SEED=20260717 · ρ=0.8 · E[S]=1.0 ⇒ λ=0.8 · C²_H2=4 · N_JOBS=600000 · WARMUP=150000 · REPLICATIONS=30 · Z_GATE=3.0. Method of INDEPENDENT REPLICATIONS (Lindley waits are autocorrelated, so naive std/√n is invalid): each replication runs N_JOBS jobs, discards the first WARMUP, and contributes ONE sample — its post-warmup mean W_q; sub-seeds are drawn from a master random.Random(SEED) via getrandbits(64) so no stream couples across reps. z = (grand_mean − W_q_theory)/(std_across_reps/√R).

## Pre-registered gates (≥3σ, /se z convention)

- **G1 — deterministic service (M/D/1, C²=0):** measured mean W_q matches the P-K closed form 2.0. Pass iff |z| < 3.
- **G2 — exponential service (M/M/1, C²=1):** measured mean W_q matches the P-K closed form 4.0. Pass iff |z| < 3.
- **G3 — hyperexponential service (M/H2/1, C²=4):** measured mean W_q matches the P-K closed form 10.0. Pass iff |z| < 3.

Each z is (grand_mean − theory) over the standard error across the 30 independent replications; the three closed-form anchors 2.0 / 4.0 / 10.0 are computed independently of the simulation, so a mis-calibrated world (wrong arrival process, wrong service moments, or a Lindley coding error) fails its gate rather than sliding through.

## Pre-registered decision rule

sim-ready ⇔ all three gates pass in a deterministic dry run (exit 0, byte-identical double run). The mechanism is exact, so a correctly-sized sim WILL pass with margin — a failure means a sim bug (fix it), never a reason to loosen a gate below 3σ.

## Dry-sim results (firsthand, exit 0, double-run identical)

| service | C² | W_q (sim) | W_q (exact) | std across reps | se | z |
|---|---|---|---|---|---|---|
| D (M/D/1) | 0 | **2.002221** | 2.0 | 0.024515 | 0.004476 | **+0.496** |
| M (M/M/1) | 1 | **3.987717** | 4.0 | 0.071994 | 0.013144 | **−0.934** |
| H2 (M/H2/1) | 4 | **9.921619** | 10.0 | 0.233594 | 0.042648 | **−1.838** |

Gates: **G1 z=+0.496 PASS · G2 z=−0.934 PASS · G3 z=−1.838 PASS**. `all_pass: true`. The measured ratio 2.00 : 3.99 : 9.92 reproduces the 1 : 2 : 5 tax. Results-dict sha256 **`ab44d56a22c24f83c4a2048af56dc3dbdbf462d3aa9990bd19c64426891e4307`** (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY; stdout dump pretty indent=2, digest preimage compact canonical).

## Verifier

`ideas/fleet/service_variance_wait_tax.py` — stdlib only (hashlib, json, math, random). `run()` returns the results dict (no self-digest field): config, h2_params, theory, per_dist (grand_mean + std + se + z + pass), gates, all_pass. `main()` computes the compact-canonical sha256, prints the pretty dump + a `Results-JSON sha256:` line, and exits 0/1 on `all_pass`. Exact single-server Lindley recursion; method of independent replications for valid standard errors.

## Reproduce

    python3 ideas/fleet/service_variance_wait_tax.py
    # → prints the results JSON, then: Results-JSON sha256: ab44d56…91e4307 ; exit 0

## Why it matters

Every shared fleet server — a request handler, a lock-holding worker, a merge/CI queue, a sim-lab verdict runner — is an M/G/1 (or M/G/c) queue whose latency the P-K tax governs. Two lanes at the same ρ and same mean cost can feel 5× different purely because one has heavy-tailed jobs (research spikes, debugging, cold caches) and the other tight ones. The tax is invisible on a utilization/throughput dashboard, so teams chase phantom "load" problems while the real lever is service-time VARIANCE: cut the tail (timeouts, work-splitting, caching, deterministic fast paths) to shrink C², or — since the tax is multiplicative — recognize that uniform capacity increases don't equalize two lanes of different variance. The numbers to remember: at fixed ρ=0.8, C²=0/1/4 give W_q=2/4/10 — a **5× wait spread from variance alone**.

## Dedup

Distinct from every existing fleet card. Nearest neighbor is [[variance-blind-provisioning-trap]] (P089) — that card prices the *SLA-violation rate* of two lanes and the *(1+CV²) capacity-provisioning correction* (how much extra capacity a heavy-tailed lane needs to hit an absolute SLA), a two-lane dose-response + correction sweep at C²=3; this card prices the *pure P-K queue-WAIT law/tax itself* across three canonical service laws D/M/H2 (C²=0/1/4) at fixed ρ and mean, the 2.0/4.0/10.0 headline the operator never sees on a utilization dashboard — the LAW, where P089 is the operational FIX. Also distinct from [[inspection-paradox-wait-inflation]] (observer / size-biased *sampling* of a wait, not the queue's own service-variance law), [[correlated-fleet-variance-floor]] (N_eff=1/ρ aggregation floor across correlated servers, not a single queue), and [[checkout-pooling-single-line]] (M/M/c server-*pooling* magnitude on a discrete Bernoulli-tick frame where P-K explicitly does not bind). No card states the M/G/1 (1+C²)/2 queue-wait tax across D/M/H2 at fixed load.

## Model basis (P024 discipline)

Three modeling commitments carry the verdict, each pinned and directional: (1) ARRIVALS are Poisson at λ=0.8 (interarrival Exp(λ)) — the M/G/1 premise P-K was derived for; a non-Poisson arrival process would break the closed form and show up as a gate miss. (2) SERVICE is single-server FIFO with three pinned laws (D constant, M exponential, H2 balanced-means C²=4) — the head prices these three specifically; other C²=4 laws (lognormal, Pareto) or multi-server (M/G/c) queues are named follow-ups. (3) The METRIC is the mean queue wait W_q measured by the exact Lindley recursion and anchored to the independently-computed P-K closed form; the /se z-gate against the anchor is the world-calibration self-check — a measured W_q that misses P-K means the sim, not the theory, is wrong. The folk belief is priced against its own best formalization ("same ρ + same E[S] ⇒ same wait"), which the D-vs-M-vs-H2 spread at identical ρ and E[S] falsifies exactly; the D endpoint (C²=0, tax (1+0)/2=0.5) registers the low-variance case, so the head cannot be read as a straw man.

## Probe report (v0)

**1. Is the claim counterintuitive?** Yes — a utilization/throughput dashboard shows two servers as identical (same ρ, same mean job), yet the M/H2/1 waits **5×** longer than the M/D/1 purely from service-time variance.
**2. Is it falsifiable?** Yes — three ≥3σ /se gates against independently-computed P-K closed forms (2.0/4.0/10.0); a wrong arrival process, wrong service moments, or a Lindley bug fails a gate.
**3. Is the anchor real?** Yes — the Pollaczek–Khinchine mean-value formula (Kleinrock, *Queueing Systems* Vol.1, 1975, §5.6), the canonical M/G/1 result; the mean queue wait's dependence on service-time variance is textbook.
**4. Is the sim deterministic?** Yes — SEED=**20260717**, byte-identical double run, disclosed results-dict sha256 **ab44d56…91e4307**, exit 0.
**5. Is it stdlib-only?** Yes — hashlib/json/math/random; exact Lindley recursion, no numpy.
**6. Does it dedupe?** Yes — distinct object from P089 variance-blind-provisioning-trap (SLA + capacity correction) and from the inspection-paradox / N_eff-floor / pooling heads.
**7. Is the number memorable?** Yes — at ρ=0.8, C²=0/1/4 give W_q=**2/4/10** (a 1:2:5 tax); the factor is (1+C²)/2.
**8. Is there a lever?** Yes — cut service-time variance (tail-trim, work-split, caching, deterministic fast paths) to shrink C²; do NOT expect uniform capacity increases to equalize lanes of different variance (the tax is multiplicative).

## One-line correction

Not "same utilization and same mean service ⇒ same latency" — for an M/G/1 queue W_q = (ρ/(1−ρ))·E[S]·(1+C²)/2, so at fixed ρ=0.8 and fixed E[S]=1.0 the queue wait is 2.0 / 4.0 / 10.0 for C²=0 / 1 / 4, a 5× spread set entirely by service-time variance that no utilization dashboard shows.

**Recommendation: sim-ready** — reproduce the committed verifier byte-identical in sim-lab, confirm results-dict sha256 ab44d56a22c24f83c4a2048af56dc3dbdbf462d3aa9990bd19c64426891e4307 EXACT and all three ≥3σ gates PASS, then APPROVE as VERDICT 150.
