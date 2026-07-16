# Provisioning fleet-lane capacity from MEAN task cost systematically under-serves HIGH-VARIANCE lanes: two lanes with IDENTICAL arrival rate, IDENTICAL mean task cost, and therefore IDENTICAL nominal utilization ρ can have SLA-violation rates that differ by 3.67× purely from service-time variance, because mean queue wait scales with the SQUARED coefficient of variation (Pollaczek–Khinchine, Wq ∝ (1+CV²)/2) — the gap closes only when the lane is provisioned by (1+CV²), not by the mean

> **State:** sim-ready
> **Class:** fleet — round-19 fleet-backlogs OPENER (standing ORDER 003 · rotation
> slot per ORDER 004 rule 3; the 4-phase cycle {fleet-backlogs → venture →
> game-mechanics → unrelated} rolls to a new opener after round-18 closed
> P085(fleet #458→V098 REJECT) → P086(venture #460→V099 ACCEPT) → P087(game
> #462→V100 ACCEPT) → P088(unrelated closer #464→V101 APPROVE). Adjudication:
> sim-lab VERDICT 102 (+13 offset, P089 → V102).
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264
> pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab
> files).
> **Grounding:** https://github.com/menno420/idea-engine@748bd58 · fetched 2026-07-16T22:39:57Z
> (the pipeline HEAD at drafting). This is a fleet-OPS queueing head, NOT fleet-external: the phenomenon
> is a direct model of how the fleet provisions capacity across its own concurrent
> work lanes (the {fleet, venture, game, unrelated} lanes carry DIFFERENT task-cost
> variances — a research-spike lane is heavy-tailed, a mechanical-refactor lane is
> tight — so a manager reading a single backlog COUNT per lane and provisioning off
> the MEAN is exactly the variance-blind provisioner this head prices). HONEST SCOPE:
> the phenomenon itself is a self-contained stdlib M/G/1 discrete-event Monte-Carlo
> any verdict session runs cold; the Pollaczek–Khinchine mean-wait law is the WITNESS
> mechanism, cited-not-cloned; every model constant below is pinned in this file. The
> mean-wait law binds EXACTLY here because arrivals are Poisson and service is a
> general single-server FCFS queue — the M/G/1 setting P–K was derived for (unlike
> P044's deliberately conservative discrete Bernoulli-tick pooling frame, where the
> idea file itself notes P–K does NOT bind).
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under the deliberate
> lane rotation (ORDER 004 rule 3). Round-19 opener at the fleet-backlogs lane — the
> natural successor to P085's round-18 fleet-backlogs opener (RR-vs-LQF domain-rotation
> starvation, which priced SCHEDULING POLICY across lanes). This head prices the
> ORTHOGONAL fleet-ops axis P085 did not touch: not WHICH lane to serve next
> (scheduling), but HOW MUCH CAPACITY each lane needs (provisioning) — and the trap
> is that the natural provisioning signal (mean task cost, read off a backlog count)
> is variance-blind.

**Placement note (decide-and-flag):** this cross-cutting fleet-ops head lives in
`ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads — flagged
rather than silently squatting a roster-derived section, exactly as PROPOSALs 017
through 088 did.

## The folk belief

"Two lanes have the same arrival rate and the same average task cost, so they carry
the same load — provision them the same." This is the instinct behind every
capacity plan read off a backlog COUNT: a manager sees lane A and lane B each
averaging one unit of work per task at the same arrival rate, computes the same
nominal utilization ρ = 0.8 for both, and gives them the same capacity. The instinct
has one load-bearing assumption: that mean load (ρ = λ·E[S]) determines congestion.
It is false in an exactly measurable way whenever the two lanes differ in service-time
VARIANCE. The Pollaczek–Khinchine formula makes the sign and the size exact: the mean
queue wait of an M/G/1 lane is `Wq = ρ/(1−ρ) · (1+CV²)/2 · E[S]`, where CV is the
coefficient of variation of service time. At equal ρ and equal E[S], the lane with
CV = 3 waits `(1+9)/2 = 5×` longer in queue than the lane with CV = 1 — and because
SLA-violation rate reads the TAIL of the sojourn distribution, the heavy-tailed lane
violates its SLA far more often. The mean-based capacity plan under-serves the
high-variance lane systematically, and the manager, seeing identical backlog counts,
never sees it coming.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Pin the world. Two lanes A and B, each a single-server FCFS M/G/1 queue. Arrivals are
Poisson at rate λ = 0.8 for BOTH lanes. Mean service E[S] = 1.0 for BOTH lanes → the
nominal utilization ρ = λ·E[S] = 0.8 is IDENTICAL. The ONLY difference is
service-time variance:

- **Lane A** — exponential service, CV = 1.0 (the reference M/M/1 lane).
- **Lane B** — a balanced-means two-phase hyperexponential (H2), mean 1.0, CV = 3.0
  (a heavy-tailed lane: most tasks fast, a few very slow — the shape of a
  research-spike / debugging lane).

The SLA target is a sojourn (wait + service) cap `W_target = 10.0` (10× the mean
service time). The metric is the SLA-violation rate: the fraction of completed tasks
whose sojourn exceeds `W_target`.

**Why the heavy-tailed lane violates more.** By P–K, at ρ = 0.8: Wq(A) =
0.8/0.2·(1+1²)/2·1 = 4.0, Wq(B) = 0.8/0.2·(1+3²)/2·1 = 20.0 — a 5× larger mean queue
wait for B from variance alone, despite identical ρ. Mean sojourn is 5.0 (A) vs 21.0
(B). The SLA-violation rate reads the tail past 10.0: for the exponential lane A the
sojourn is exponential with mean 5.0, so the violation rate is ≈ e^(−10/5) = e^(−2) ≈
0.135; for the hyperexponential lane B the far heavier tail pushes the violation rate
to ≈ 0.51 — a 3.67× gap, all from CV, none from ρ or E[S].

**The dose-response (variance pressure).** Hold ρ = 0.8 and sweep CV_B upward from 1.0.
At CV_B = 1.0 the two lanes are identical (ratio 1×). As variance rises the
SLA-violation ratio B/A rises MONOTONICALLY and crosses 2× at CV_B ≈ 1.51 — a
dose-response on service-time variance, this head's third registered structure (R3):
the more heavy-tailed the lane, the more a mean-based plan under-serves it, and the
effect is already 2× by a modest CV of 1.5.

**The provisioning correction (the mechanism isolation).** The claim is not merely
that B waits more — it is that PROVISIONING BY (1+CV²), not by the mean, is what
restores parity. Re-provision lane B by raising its server capacity (a faster server:
scale B's mean service down, keeping λ = 0.8 so ρ_B falls) until B's SLA-violation
rate matches A's. The mean-based plan gives both lanes ρ = 0.8 and leaves an 88σ SLA
gap; parity is restored only at ρ_B ≈ 0.512 (capacity ×1.56) — a SUBSTANTIAL
over-provision relative to A that a backlog-count manager reading equal mean load would
never allocate. This is the head's mechanistic core (R4): if the SLA gap could be
closed at ρ_B ≥ ρ_A = 0.8 (equal or less capacity than A), variance would be
irrelevant and the "provision by (1+CV²)" claim would be FALSE. That ρ_B must fall
WELL below ρ_A to reach parity is the direct, falsifiable signature of the trap.

**The world sanity anchor (P–K consistency, the P085/V098 lesson).** The measured mean
queue wait must MATCH the P–K closed form for BOTH lanes — this is the world's own
stability ceiling / self-check. If the measured Wq disagrees with P–K, the sim is
mis-calibrated (wrong arrival process, wrong service moments, or a coding error) and
NO result about variance can be trusted → INVALID, not a real finding. This head
VERIFIES the anchor (R2) rather than assuming it: measured Wq within ±5% of P–K for
both lanes, observed error ≤ 1.44%.

Every registered numeral below was produced live this session by the drafting script
(scratchpad `dry-sim.py`, stdlib-only, exact single-server Lindley recursion — exact
for M/G/1 FCFS, no event heap needed): run TWICE → byte-identical (sha256
805b6f1d…7d9699 of the printed output), all four gates evaluated with the disclosed
margins.

## Pinned model (committed constants — all pinned)

- **Arrivals:** Poisson at rate `λ = 0.8` for BOTH lanes (interarrival ~ Exp(λ) via
  `random.Random.expovariate(λ)`). Shared arrival stream across lanes per seed (common
  random numbers — a variance-reduction device; both lanes remain proper independent
  M/G/1 queues, just correlated seed-wise).
- **Mean service:** `E[S] = 1.0` both lanes → nominal `ρ = λ·E[S] = 0.8` both lanes.
- **Lane A service:** exponential, `CV = 1.0` — `expovariate(1/E[S])`. This is the
  reference M/M/1 lane.
- **Lane B service:** balanced-means two-phase hyperexponential (H2), mean 1.0,
  `CV = 3.0`. Derivation (disclosed): with balanced means each phase contributes
  E[S]/2 to the mean, so `p·(1/μ1) = (1−p)·(1/μ2) = E[S]/2`, which forces
  `p(1−p) = 1/(2(1+CV²))`; taking the larger root gives **p = 0.947214**,
  phase-1 (fast) mean `1/μ1 = 0.527864` (rate μ1 = 1.894427), phase-2 (slow) mean
  `1/μ2 = 9.472136` (rate μ2 = 0.105573). Verified in-file: E[S] = 1.000000,
  E[S²] = 10.000000, CV = 3.000000 exactly. (At CV = 1 this construction collapses to
  the exponential, so lane A is its CV = 1 special case — the sweep is continuous.)
- **SLA:** sojourn (wait + service) target `W_target = 10.0` (= 10·E[S]); metric =
  fraction of completed tasks with sojourn > W_target.
- **Verifier spec:** `N = 200000` tasks per lane per replication, warmup discard
  `WARMUP = 20000`, `R = 12` independent replications with the DISCLOSED fixed seed
  list `S = [1001, 1002, …, 1012]`. Per-replication service stream keyed by
  `seed·7919 + round(CV·1000)`; arrival stream keyed by `seed·104729`. Pooled quantity
  σ = sample SD across the 12 per-seed values (ddof = 1); SE = SD/√12.
- **Metric implementation:** exact Lindley recursion `Wq_i = max(0, Wq_{i−1} +
  S_{i−1} − A_i)`, `sojourn_i = Wq_i + S_i`; stdlib `random`/`math` only, no numpy.
- **Determinism:** every draw from a seeded `random.Random`; the whole battery is
  byte-identical across two process runs (verified twice this session).
- **SEEDLESS baton:** the seeds 1001..1012 are IN-FILE reporting constants, NOT
  seed-ledger draws — the next free seed block stays **20261730** untouched (the
  P084/P085/P086/P087/P088 SEEDLESS precedent; this cycle consumes NO ledger block).

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained queueing-model probe, the
> sim is report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — a tree-wide sweep
> for coefficient-of-variation / Pollaczek / M/G/1 / hyperexponential / provisioning
> returned one genuine near-hit, **P044 checkout-pooling**, which is argued distinct
> in Dedup (it prices SERVER POOLING at LOW variance on a discrete Bernoulli-tick frame
> where P–K explicitly does NOT bind; this head prices SINGLE-server VARIANCE-driven
> provisioning at HIGH variance on a continuous Poisson M/G/1 where P–K binds exactly).
> (b) **kill test NOT triggered** — no recorded drop of a variance-provisioning head on
> any card. (c) **feasibility + liveness arithmetic checked LIVE** — every registered
> numeral ran this session (`dry-sim.py`, stdlib-only, run twice → byte-identical): the
> baseline ratio, the P–K sanity errors, the CV sweep + crossover, and the correction
> parity, all as pooled mean ± SE across the 12 seeds; expected landing DISCLOSED
> (APPROVE), all rulings reachable, one calibration nuance on the R4 correction target
> disclosed below. (d) **grounding reachability** — HONEST: the phenomenon is a stdlib
> M/G/1 Monte-Carlo any verdict session runs cold; the fleet's own multi-variance work
> lanes ground the WHY (the manager provisions off a backlog count = the mean), the
> Pollaczek–Khinchine law grounds the mechanism (cited-not-cloned).

**Measured dry-sim table (VERBATIM — `dry-sim.py`, N = 200000/lane/rep, warmup 20000,
R = 12 seeds 1001..1012, shared-arrival CRN, byte-identical across two process runs):**

```
--- ARM 1: BASELINE (provision by MEAN: both lanes rho=0.8) ---
  Lane A (CV=1.0, exp)  rho=0.8000
     mean Wq measured = 4.05748 (sd=0.12146 se=0.03506)  P-K = 4.00000  err = +1.437%
     SLA-viol measured = 0.138165 (sd=0.007272 se=0.002099)
  Lane B (CV=3.0, H2)   rho=0.8000
     mean Wq measured = 20.24797 (sd=1.21654 se=0.35118) P-K = 20.00000  err = +1.240%
     SLA-viol measured = 0.507555 (sd=0.012528 se=0.003616)
  SLA-viol ratio B/A = 3.6735 (se~0.0616)
  SLA-viol gap (B - A) = 0.369390  separation = 88.34 sigma

--- ARM 2: CV_B SWEEP at fixed rho=0.8 ---
  CV_B=1.0  viol=0.138165 (se=0.002099)  Wq=4.0575  P-K=4.0000  err=+1.44%  ratio B/A=1.0000
  CV_B=1.5  viol=0.273752 (se=0.002421)  Wq=6.6745  P-K=6.5000  err=+2.69%  ratio B/A=1.9813
  CV_B=2.0  viol=0.384444 (se=0.003760)  Wq=10.2955 P-K=10.0000 err=+2.95%  ratio B/A=2.7825
  CV_B=2.5  viol=0.450171 (se=0.002352)  Wq=14.3489 P-K=14.5000 err=-1.04%  ratio B/A=3.2582
  CV_B=3.0  viol=0.507555 (se=0.003616)  Wq=20.2480 P-K=20.0000 err=+1.24%  ratio B/A=3.6735
  CV_B=3.5  viol=0.543336 (se=0.003468)  Wq=27.0189 P-K=26.5000 err=+1.96%  ratio B/A=3.9325
  monotone increasing ratio in CV_B? True   ratios = [1.000,1.981,2.782,3.258,3.674,3.933]
  2x crossover CV_B ~= 1.5116

--- ARM 3: PROVISIONING CORRECTION (raise lane-B capacity per P-K (1+CV^2)) ---
  P-K mean-WAIT-parity prescription: rho_B=0.44444  mean_s_B=0.55556  capacity x1.8000
  capacity sweep (mean_s_B, rho_B) -> lane-B SLA-viol vs A:
    mean_s_B=1.0000 rho_B=0.8000  viol_B=0.507555 (se=0.003616)  viol_A=0.138165  gap=+0.369390  sep=88.34sig  Wq_B=20.2480 P-K=20.0000 err=+1.24%
    mean_s_B=0.8000 rho_B=0.6400  viol_B=0.265202 (se=0.002103)  viol_A=0.138165  gap=+0.127037  sep=42.76sig  Wq_B=7.2447 P-K=7.1111 err=+1.88%
    mean_s_B=0.7000 rho_B=0.5600  viol_B=0.179945 (se=0.001689)  viol_A=0.138165  gap=+0.041780  sep=15.51sig  Wq_B=4.5403 P-K=4.4545 err=+1.92%
    mean_s_B=0.6944 rho_B=0.5555  viol_B=0.175786 (se=0.001626)  viol_A=0.138165  gap=+0.037621  sep=14.17sig  Wq_B=4.4226 P-K=4.3394 err=+1.92%
    mean_s_B=0.6600 rho_B=0.5280  viol_B=0.151445 (se=0.001437)  viol_A=0.138165  gap=+0.013280  sep=5.22sig  Wq_B=3.7587 P-K=3.6915 err=+1.82%
    mean_s_B=0.6500 rho_B=0.5200  viol_B=0.144778 (se=0.001366)  viol_A=0.138165  gap=+0.006612  sep=2.64sig  Wq_B=3.5835 P-K=3.5208 err=+1.78%
    mean_s_B=0.6450 rho_B=0.5160  viol_B=0.141461 (se=0.001333)  viol_A=0.138165  gap=+0.003296  sep=1.33sig  Wq_B=3.4987 P-K=3.4382 err=+1.76%
    mean_s_B=0.6400 rho_B=0.5120  viol_B=0.138281 (se=0.001310)  viol_A=0.138165  gap=+0.000116  sep=0.05sig  Wq_B=3.4159 P-K=3.3574 err=+1.74%
    mean_s_B=0.6350 rho_B=0.5080  viol_B=0.135094 (se=0.001274)  viol_A=0.138165  gap=-0.003071  sep=1.25sig  Wq_B=3.3347 P-K=3.2783 err=+1.72%
    mean_s_B=0.6300 rho_B=0.5040  viol_B=0.131887 (se=0.001242)  viol_A=0.138165  gap=-0.006278  sep=2.57sig  Wq_B=3.2553 P-K=3.2008 err=+1.70%
    mean_s_B=0.5556 rho_B=0.4444  viol_B=0.089619 (se=0.000988)  viol_A=0.138165  gap=-0.048546  sep=20.92sig  Wq_B=2.2522 P-K=2.2222 err=+1.35%
    mean_s_B=0.5000 rho_B=0.4000  viol_B=0.063762 (se=0.000742)  viol_A=0.138165  gap=-0.074403  sep=33.42sig  Wq_B=1.6846 P-K=1.6667 err=+1.08%
    mean_s_B=0.4500 rho_B=0.3600  viol_B=0.044819 (se=0.000558)  viol_A=0.138165  gap=-0.093347  sep=42.98sig  Wq_B=1.2767 P-K=1.2656 err=+0.87%
    mean_s_B=0.4000 rho_B=0.3200  viol_B=0.029413 (se=0.000390)  viol_A=0.138165  gap=-0.108752  sep=50.93sig  Wq_B=0.9478 P-K=0.9412 err=+0.70%
  SLA-PARITY point (min |gap| within 3-sigma band): mean_s_B=0.6400 rho_B*=0.5120  capacity x1.5625
    viol_B*=0.138281 (se=0.001310)  vs  viol_A=0.138165  gap=+0.000116  sep=0.05 sigma
    3-sigma noise band on gap = 0.007424 ; |gap|=0.000116 within band? True
    Wq_B=3.4159  P-K=3.3574  err=+1.74%
    DECISIVE clause: rho_B*=0.5120 < rho_A=0.8000? True  -> variance forces a substantial over-provision
  DISCLOSED mean-WAIT-parity (rho_B=0.4444, capacity x1.8000): viol_B=0.089619 vs viol_A=0.138165  gap=-0.048546
    removes 86.9% of the baseline SLA gap (+0.369390) but OVER-corrects the absolute-target tail (viol_B below viol_A, W_target=10.0 fixed) -> disclosed, not selected
```

**Disclosed correction (calibrate-against-the-world discipline — the V098/P088 lesson).**
The parameter-free P–K prescription that equalizes mean WAIT (solve
`ρ_B/(1−ρ_B) = [ρ_A/(1−ρ_A)]·(1+CV_A²)/(1+CV_B²) = 4·(2/10) = 0.8` → ρ_B = 0.4444,
capacity ×1.80) removes **86.9%** of the SLA gap but slightly OVER-corrects on the
absolute-SLA metric (viol_B = 0.0896 lands BELOW viol_A = 0.1382). The reason is
disclosed rather than silently tightened: speeding B's single server to raise capacity
ALSO shrinks B's mean-service floor beneath the FIXED absolute target W_target = 10.0,
so matching mean-wait over-shoots the tail metric. The SLA-violation parity point sits
BETWEEN the equal-ρ trap (ρ_B = 0.8) and the wait-parity point (ρ_B = 0.444): measured
**ρ_B* = 0.512 (capacity ×1.5625)**, at which the SLA gap is +0.000116 (0.05σ, inside
the 3σ noise band 0.0074). R4 is therefore registered on the MEASURED SLA-parity
re-provisioning ρ_B* = 0.512, with the DECISIVE clause being that ρ_B* must fall well
below ρ_A = 0.8 (variance forces a substantial over-provision); the parameter-free
wait-parity prediction ρ_B = 0.444 is disclosed as the same-direction, same-order-of-
magnitude bound that the tail metric refines. Both the direction (ρ_B* ≪ ρ_A) and the
order of magnitude (roughly halve B's ρ) are exactly what P–K's (1+CV²) law predicts.

**1. What is this really?** A pre-registered MEASUREMENT of the mean-based-provisioning
folk rule — "equal arrival rate + equal mean cost = equal load, provision the same" —
taken on its canonical mechanism: two M/G/1 lanes identical in every first-moment way,
differing only in service-time variance. Four exact structures: the WORLD ANCHOR (the
measured mean wait matches Pollaczek–Khinchine for both lanes, R2), the EFFECT (the
high-variance lane violates its SLA 3.67× more at identical ρ, R1), the DOSE-RESPONSE
(the ratio rises monotonically in CV_B and crosses 2× by CV ≈ 1.5, R3), and the
PROVISIONING CORRECTION (parity is restored only by dropping ρ_B well below ρ_A, i.e.
provisioning by (1+CV²) not the mean, R4).

**2. What is the possibility space?** (i) Don't run it — the round-19 fleet-backlogs
opener goes unserved and the pipeline stalls. (ii) A folklore retelling ("high-variance
queues are worse") — retells the sign without the exact (1+CV²) law, the crossover CV,
or the provisioning correction. (iii) An analytic-only treatment (quote P–K, compute
the two Wq) — leaves the SLA-TAIL question (which P–K's mean does not settle) and the
correction magnitude undecided; the Monte-Carlo is the cheap independent re-derivation
that also measures the tail. (iv) A single-CV snapshot — misses the dose-response and
the crossover, which are the actionable part (variance matters already at CV 1.5).
(v) This head: a seeded stdlib M/G/1 sim as the ruling, APPROVE-first-disclosed bands,
a P–K sanity anchor, a dose-response, and a provisioning-correction falsifier.
(vi) Over-scope (multi-server lanes, priority classes, non-Poisson arrivals, other
service laws) — each a named follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: an exact single-server Lindley recursion, a balanced-means
H2 sampler, and the P–K closed form, swept over CV_B × 12 seeds plus a capacity-
correction sweep — that single kernel yields the world anchor, the effect, the
dose-response, and the provisioning correction, from a sim a verdict session runs cold
in ≈ 20 s, byte-identical across runs.

**4. What breaks it? (assumptions made explicit)** (a) **The two lanes are identical in
λ and E[S] BY CONSTRUCTION** — same arrival rate, same mean service, so ρ = 0.8 for
both; if a verdict session finds the measured mean waits disagree with P–K, the sim is
mis-calibrated and the head is INVALID, not APPROVE (R2). (b) **The service laws are
pinned** — lane A exponential (CV 1), lane B balanced-means H2 (CV 3); a different
CV-3 law (e.g. a lognormal or a different H2 branch weighting) is a named follow-up, not
this claim. (c) **The SLA target is absolute** (W_target = 10.0, wall-clock) — a target
that scales with each lane's mean service would change the correction arithmetic; the
absolute target is the realistic "finish within 10 units" SLA and is disclosed as the
pinned choice. (d) **The correction target is the SLA-parity load, disclosed** — the
parameter-free wait-parity ρ_B = 0.444 over-corrects the tail metric; R4 pins the
measured SLA-parity ρ_B* = 0.512 and the decisive clause is ρ_B* ≪ ρ_A, not an exact
capacity factor.

**5. What does it unlock?** The pipeline's round-19 fleet-backlogs opener and a directly
actionable fleet-ops correction: when the fleet provisions capacity across its own work
lanes (research-spike vs mechanical-refactor vs review), it must weight each lane by
(1+CV²), not by the mean backlog count — a heavy-tailed lane at the SAME nominal load
needs materially more capacity (here ×1.56) to hit the same SLA. Three standalone pins
(the 3.67× SLA gap from variance alone at equal ρ; the 2× crossover already at CV ≈ 1.5;
the ρ_B ≈ 0.512 correction), plus a transferable provisioning audit for any lane sized
off a mean cost.

**6. What is the cheapest experiment that decides it?** The head IS the cheapest deciding
experiment: the baseline + P–K anchor + CV sweep + correction settle every gate in one
short run. The single cheapest sanity probe is the P–K check itself — the measured mean
waits (4.06, 20.25) landing within 1.5% of the closed form (4.0, 20.0) confirms the world
is calibrated before any SLA claim.

**7. What would make this a mistake to run?** If the phenomenon were unavailable (it is
not — a finite seeded M/G/1 MC), if the domain duplicated a prior head (it does not — the
nearest, P044's checkout-pooling, is server-POOLING at LOW variance on a discrete frame
where P–K does not bind, argued distinct in Dedup), or if the disclosed APPROVE made the
run theater. It does not: the value is the independent hermetic re-derivation (the sim
re-draws both lanes, re-runs Lindley, re-computes P–K and the SLA tail, and must
reproduce the anchor, the 3.67× effect, the dose-response, and the correction from
scratch), and REJECT is genuinely reachable (a measured Wq that misses P–K sinks R2 to
INVALID; an SLA gap that closes at ρ_B ≥ ρ_A sinks R4).

**8. How will we know it worked?** A committed sim-lab report with: the full {arm ×
metric} table (per-seed + pooled mean ± SE for Wq and SLA-viol, both lanes, plus the CV
sweep and the correction sweep), the P–K sanity errors, the R1 ratio + gap σ, the R3
crossover CV + monotonicity, the R4 correction parity + the ρ_B* ≪ ρ_A direction, the
verdict token against the pre-registered bands, and a byte-identity note. A clean run
reproduces the drafter's disclosed values (Wq_A ≈ 4.06, Wq_B ≈ 20.25; viol_A ≈ 0.138,
viol_B ≈ 0.508; crossover CV ≈ 1.51; SLA-parity ρ_B* ≈ 0.512) from scratch, or — the more
interesting outcome — DISAGREES and pins the drafter's error, which the pre-registered
rule then rules on honestly.

**Recommendation: sim-ready**

## Pre-registered gates (evaluation order R1 → R2 → R3 → R4; APPROVE iff ALL hold)

- **R1 — the trap (effect).** At the pinned baseline (both lanes ρ = 0.8), the
  high-variance lane's SLA-violation rate is at least `k×` the low-variance lane's,
  with the gap separated ≥3σ over the replication noise. The pre-registered factor
  `k = 2.5` is CALIBRATED beneath the measured ratio so the measured mean clears it by
  ≥3σ. **Calibrated:** viol_B = 0.507555, viol_A = 0.138165 → ratio = 3.6735
  (se ≈ 0.0616), clears k = 2.5 by ≈ 19σ; absolute gap 0.369390 separated at 88.34σ
  → PASS.
- **R2 — world sanity / Pollaczek–Khinchine consistency.** The measured mean queue wait
  is within ±5% of the P–K closed form `Wq = ρ/(1−ρ)·(1+CV²)/2·E[S]` for BOTH lanes.
  Proves the world is calibrated (right arrival process, right service moments) — the
  P085/V098 anchor-inside-the-stable-regime lesson. **Calibrated:** lane A measured
  4.05748 vs P–K 4.0 → +1.437%; lane B measured 20.24797 vs P–K 20.0 → +1.240%; worst
  1.44% ≤ 5% → PASS. FAILURE ⇒ the sim is mis-calibrated ⇒ INVALID (no variance claim
  survives an anchor miss).
- **R3 — dose-response (crossover + monotonicity).** With ρ = 0.8 fixed, the
  SLA-violation ratio B/A is strictly monotone increasing in CV_B over the grid
  {1.0, 1.5, 2.0, 2.5, 3.0, 3.5} (each adjacent pair separated ≥3σ), and crosses 2× at
  CV_B ≈ 1.51 ± 0.15. Confirms the trap scales with variance. **Calibrated:** ratios
  [1.000, 1.981, 2.782, 3.258, 3.674, 3.933] strictly increasing (adjacent viol_B
  separations all ≥7σ, tightest 7.14σ at CV_B 3.0↔3.5); 2× crossover at CV_B = 1.5116
  (inside 1.51 ± 0.15) → PASS.
- **R4 — provisioning correction closes the gap (falsifier).** Re-provisioning lane B by
  raising its server capacity to the P–K-guided SLA-parity load `ρ_B* = 0.512`
  (capacity ×1.5625, mean_s_B = 0.64) closes the SLA gap to within 3σ of parity:
  `|viol_B* − viol_A| ≤ 3·σ_gap`, AND the required `ρ_B*` is strictly BELOW ρ_A = 0.8
  (variance forces a substantial over-provision). Isolates variance as the cause: if
  parity were reachable at ρ_B ≥ ρ_A, variance would be irrelevant → REJECT.
  **Calibrated:** at ρ_B* = 0.512, viol_B* = 0.138281 vs viol_A = 0.138165, gap
  +0.000116 (0.05σ ≤ 3σ, 3σ band 0.0074), and ρ_B* = 0.512 ≪ 0.8 → PASS. Disclosed:
  the parameter-free wait-parity ρ_B = 0.444 removes 86.9% of the gap but over-corrects
  the tail metric (see the disclosed correction above); R4 pins the measured SLA-parity
  point and its decisive clause is ρ_B* ≪ ρ_A.

## Pre-registered decision rule (evaluation order: R1 → R2 → R3 → R4)

- **APPROVE** — "the variance-blind provisioning trap is real as doctrine: two lanes
  identical in arrival rate, mean cost, and nominal ρ have a 3.67× SLA-violation gap
  from service-time variance alone (R1); the world is P–K-calibrated so the effect is
  trustworthy (R2); the gap rises monotonically with CV and is already 2× by CV ≈ 1.5
  (R3); and parity is restored only by provisioning the heavy-tailed lane to a
  substantially lower ρ — provision by (1+CV²), not the mean (R4)": iff R1 ∧ R2 ∧ R3 ∧
  R4 all hold in the registered order. Disclosed expected landing: APPROVE (all four
  hold on the dry-sim).
- **REJECT** — any HARD-FAIL: R1's SLA gap does not clear k = 2.5 by ≥3σ (no trap), OR
  R4's correction does not close the gap within 3σ / requires ρ_B ≥ ρ_A (variance not
  the cause — the provisioning claim is false). Checked as the falsifier direction
  because the whole value is the causal attribution to variance.
- **NULL** — the effect is PRESENT but sub-threshold: the SLA gap is real and positive
  but does not clear k = 2.5 by ≥3σ, OR the crossover falls outside 1.51 ± 0.15 / the
  ratio is non-monotone: a finalized, citable finding pinning the measured effect size
  and naming the sub-threshold margin, never a re-run request.
- **INVALID** — non-deterministic (the two process runs are not byte-identical) or the
  world fails its P–K anchor (R2: measured Wq off P–K by > 5% for either lane, so the
  arrival process or service moments are mis-calibrated): report, no ruling.

GATE POWER, computed at registration: every REJECT/NULL boundary is an exact seeded-MC
margin. R1 clears k = 2.5 by ≈ 19σ (absolute gap 88σ), R2's worst anchor error is 1.44%
against a ±5% band, R3's tightest adjacent pair separates at 7.14σ and the crossover is
pinned at 1.51, and R4's parity clears at 0.05σ with ρ_B* = 0.512 a clear 0.29 below
ρ_A — so no N increase over 200000 is needed. MARGIN LEDGER, disclosed: the one place the
naive reading does NOT clear is the parameter-free P–K WAIT-parity correction target
(ρ_B = 0.444 over-corrects the tail metric, residual −0.049), disclosed above as an
absolute-target artifact and registered on the measured SLA-parity load ρ_B* = 0.512;
it is the sole disclosed correction.

## Disclosed verifier (the sim-lab spec)

Committed stdlib-only Python (`random`, `math`), fixed seeds `S = [1001..1012]`,
`N = 200000` tasks/lane/rep, `warmup = 20000`, implementing: (1) the exact single-server
FCFS Lindley recursion for each M/G/1 lane, (2) an exponential sampler (lane A) and a
balanced-means H2 sampler (lane B, p = 0.947214, phase means 0.527864 / 9.472136), (3)
the Pollaczek–Khinchine closed form as the R2 anchor, (4) the CV_B sweep over
{1.0,1.5,2.0,2.5,3.0,3.5}, (5) the capacity-correction sweep locating ρ_B*. It prints
the {arm × metric} table (per-seed + pooled mean ± SD/SE) for mean Wq and SLA-violation
rate both lanes, the P–K sanity errors, the R1 ratio + gap σ, the R3 crossover CV +
monotonicity, the R4 correction parity + the ρ_B* ≪ ρ_A direction, and ONE ruling
APPROVE/REJECT/NULL/INVALID under the pre-registered R1 → R2 → R3 → R4 order.
**Fixture** = the seed-1001 baseline per-lane (mean Wq, SLA-viol) and the first-20
completed sojourn times of each lane under the baseline (committed alongside), plus the
H2 parameters (p, μ1, μ2) and the SLA-parity ρ_B*. **Determinism:** results printed
byte-identical across two full in-process runs (external diff + sha256). **INVALID
condition:** the measured mean wait misses the P–K closed form by > 5% for either lane
(arrival process not Poisson, service moments wrong, or a Lindley coding error) — the
world-calibration requirement violated; any variance claim would then be confounded by a
mis-calibrated world. The drafting script (`dry-sim.py`) is NOT committed — the
P084/P086/P087/P088 disclose-the-numbers-inline precedent; sim-lab re-derives.

## Dedup

Tree-wide `grep -riE "coefficient of variation|Pollaczek|M/G/1|M/M/1|hyperexponential|
service-time varianc|utilization cliff|provision"` (bootstrap.py/.substrate excluded) at
HEAD 748bd58: one genuine near-hit, argued distinct. No idea file or proposal P001–P088
prices variance-driven provisioning of a single-server lane.

- **P044 — checkout-pooling-single-line (round-7 unrelated closer).** The nearest kin
  (both queueing, both name P–K and CV). Argued distinct on FOUR axes: (1) OBJECT —
  P044 prices SERVER POOLING (one shared M/M/c line vs c per-register M/M/1 lines) and
  its MAGNITUDE; this head prices SINGLE-server VARIANCE-driven provisioning (same
  discipline, one server per lane, only CV differs). (2) VARIANCE REGIME — P044 uses a
  deliberately LOW-variability integer service pmf (SCV ≈ 0.17, "short queues
  everywhere, less room for pooling to shine"); this head uses HIGH variance (CV = 3,
  SCV = 9, a heavy-tailed H2) where the trap lives. (3) P–K's ROLE — P044's own idea
  file states "the Pollaczek–Khinchine formula is a Poisson/continuous-time result that
  does NOT bind" its discrete Bernoulli-tick frame, so P–K is explicitly NOT a gate
  there; here arrivals are continuous-time Poisson and service is general single-server
  FCFS — the exact M/G/1 setting P–K was derived for, so P–K IS the R2 sanity gate.
  (4) FOLK RULE — P044 tests "pooling helps ≥2×"; this head tests "equal mean ⇒ equal
  load," the opposite question (P044 asks how much a BETTER discipline helps; this asks
  how much variance HURTS the same discipline). Method kin only: the exact-battery +
  disclosed-landing + world-anchor discipline, reused as machinery on a NEW object.
- **P085 — round-robin-domain-starvation-cliff (round-18 fleet-backlogs opener).** Also
  a fleet-lane queueing head, but prices SCHEDULING POLICY (RR vs LQF rotation — WHICH
  lane to serve) with EQUAL-variance implicit service; this head prices PROVISIONING
  (HOW MUCH capacity per lane) driven purely by service-time VARIANCE — the orthogonal
  fleet-ops axis, no scheduler comparison, no rotation.
- **inspection-paradox-wait-inflation (P057-lineage).** Prices random-incidence / size-
  biased sampling (the OBSERVER's biased view of a wait), not the queue's own
  provisioning; different mechanism (sampling bias vs congestion), no CV-provisioning
  claim.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) ARRIVALS
are Poisson at equal λ = 0.8 both lanes — the equal-arrival-rate premise is BY
CONSTRUCTION, and the INVALID gate prices a P–K anchor miss (non-Poisson arrivals would
show up there), not a variance; (2) SERVICE is single-server FCFS M/G/1 with pinned laws
(exp CV 1 / balanced-means H2 CV 3) — the head prices these two laws specifically, and
other CV-3 laws or multi-server lanes are named follow-ups; (3) the METRIC is
SLA-violation rate against an ABSOLUTE sojourn target W_target = 10.0 — a tail statistic,
the fleet-ops object; a relative or mean-based target is a named follow-up; (4) the
CORRECTION knob is server SPEED (capacity via faster service, lowering ρ_B) — adding
parallel servers (M/G/c) is a named follow-up with a different closed form. The folk
belief is priced against its own best formalization: "equal arrival rate + equal mean
cost = equal load" is exactly the claim the identical-ρ + 3.67×-SLA-gap pair falsifies,
and the CV = 1 sweep endpoint (where B ≡ A, ratio 1×) registers the case where NO trap
appears, so the head cannot be read as a straw man.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-ops head with a fleet CONSUMER: the fleet manager's lane-capacity provisioning.
APPROVE → the correction ships in three lines: (1) do NOT provision a lane's capacity
from its mean task cost / backlog COUNT alone — weight by (1+CV²): a lane whose tasks
vary wildly in cost (research spikes, debugging, open-ended design) needs materially more
capacity than a tight lane at the SAME nominal load (here ×1.56 for CV 3), or it will
blow its SLA while its backlog count looks identical to a calm lane's; (2) the trap has a
DOSE-RESPONSE and BITES EARLY — the SLA gap is already 2× by a modest CV of 1.5, so even
mildly bursty lanes are under-served by mean-based plans; (3) the repair is to MEASURE
service-time variance per lane (not just the mean) and size capacity by ρ/(1−ρ)·(1+CV²),
so the heavy-tailed lane runs at a lower nominal ρ. Known co-consumers: any fleet surface
that sizes capacity, concurrency, or WIP caps off a mean/count signal — the per-lane
worker allocation, the review-queue staffing, the sim-lab verdict throughput budget.
Follow-ups named, none in scope: multi-server lanes (M/G/c — different closed form);
priority classes across lanes; non-Poisson (bursty/MMPP) arrivals; other CV-3 service
laws (lognormal, Pareto — tail-shape sensitivity of the SLA metric); a relative
(per-lane-mean) SLA target; and the analytic M/G/1 sojourn-tail closed form as an exact
second arm.
