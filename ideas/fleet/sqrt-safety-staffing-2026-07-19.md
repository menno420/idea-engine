# PROPOSAL 169 — Square-root safety staffing: a fleet's safety headroom grows only as √R, so larger fleets safely run hotter

> **State:** sim-ready
> **Class:** queueing / capacity-planning law
> **Slot:** round-40 FLEET
> **Anchor:** big fleets run hotter, not slacker-per-unit
> **Target:** sim-lab (VERDICT 182, +13 offset)
> **Grounding:** https://www.columbia.edu/~ww2040/tutorial.pdf@23095ffff7ec6f4187af59d0fdc1fb47d37494e7faa8d3631c68771c1caee4c3 · fetched 2026-07-19T12:49:43Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Erlang_(unit)
> **Verifier (firsthand):** `ideas/fleet/sqrt_safety_staffing.py` — Results-JSON sha256 `2597a50513127f663123c741aaca2bf646198035388a3325cbf4706e29092de8`
> 📊 Model: Claude Opus · high · proposal/idea-generation

## The phenomenon (one line)
To keep the chance an arriving unit has to wait pinned at a target α, an M/M/c fleet needs only c = R + β√R servers (R = λ/µ the offered load); the safety margin β√R grows as the square root of load, so at R = 1024 the fleet runs at 98.4% utilization yet still holds only a ~48.5% chance of waiting — where a single server at 98.4% utilization would make ~98% of arrivals wait.

## The folk belief
Utilization trades off against delay roughly one-for-one: to keep waits low you must keep servers slack, and to hold a fixed service level as demand grows you keep a fixed fractional headroom (say 10% spare capacity). Running a fleet at 98% busy is assumed to mean near-certain queueing.

## The mechanism (reasoned, Q-0254 duty)
The number of busy servers under offered load R fluctuates with a standard deviation of order √R (a Poisson-like count), so to sit a fixed number of standard deviations away from saturation you need headroom proportional to √R, not to R. That is the whole engine. Make it precise: in the many-server heavy-traffic (QED) regime you set c = R + β√R, and the scaled number-in-system converges to a diffusion whose probability of delay is the Halfin–Whitt limit α = [1 + βΦ(β)/φ(β)]⁻¹ — a constant that depends only on the service grade β, not on the fleet size R. Because the buffer against stochastic variability is β√R while demand is R, the FRACTIONAL slack (c − R)/R = β/√R vanishes as R grows, so utilization ρ = 1 − β/√R climbs toward 1 — and yet the delay probability stays at the same α. A bigger shared pool converts the identical service grade into higher utilization: the √R law IS an economy of scale. The folk "fixed fractional headroom" rule scales the buffer as R when only √R is required, so it over-provisions ever more wastefully as the fleet grows.

## The formal model (committed constants)
M/M/c with µ = 1 and offered load R = λ; staffing c = ⌈R + β√R⌉ with β solving the Halfin–Whitt limit for α = 0.5 (β = 0.506054). Exact P{wait} from the Erlang-C formula at each load. A separate M/G/c FCFS discrete-event simulation (15 independent replications, a 15000-arrival warmup discarded, 25000 counted arrivals per replication) supplies a valid replication-based standard error and is run ONLY at loads where it reaches steady state; the robustness variant swaps exponential service for a hyperexponential H2 (p = 0.9, phase means 0.2 / 8.2; overall mean 1, SCV ≈ 12.5) to test off the exponential assumption.

## Pinned world (committed constants)
SEED=20260717; z_gate=3.0; α_target=0.5 → β=0.506054; ledger loads R∈{16,64,256,1024}; DES loads R∈{16,64} (steady-state-reachable); robustness load R=64; REPS=15; WARMUP=15000; COUNT=25000.

## Pre-registered gates (G1→G2→G3, z_gate=3.0)
- **G1 — pooling decoupling (deterministic, exact Erlang-C at R_max=1024):** the fleet runs at ρ ≥ 0.95 yet exact P{wait} ≤ α + 0.02, with the gap to the M/M/1-at-the-same-utilization delay (which is ρ) at least 0.40 and per-unit slack (c − R)/R < 0.05. Rejects the folk one-for-one utilization/delay tradeoff.
- **G2 — square-root staffing form (deterministic identity):** headroom/√R converges to β at scale; |headroom(R_max)/√R_max − β| < 0.05.
- **G3 — robustness under a shifted service distribution (≥3σ, replicated DES at R=64):** under hyperexponential service (SCV ≈ 12.5, same mean) the decoupling survives — ρ − mean P{wait} is ≥3σ positive across replications and delay stays unsaturated (mean P{wait} < 0.9).

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 all pass; otherwise revise. The shipped verifier's `all_pass` field is exactly this conjunction (G1 ∧ G2 ∧ G3), so a green `all_pass=true` and the decision rule are the same statement.

## Dry-sim results
```json
{
  "all_pass": true,
  "des_matches_exact_within_3sigma": true,
  "des_replicated": [
    {
      "R": 16,
      "c": 19,
      "des_exp_pwait": 0.376968,
      "des_exp_se": 0.004955,
      "des_exp_util": 0.842664,
      "des_h2_pwait": 0.417219,
      "des_h2_se": 0.009695,
      "des_h2_util": 0.846978,
      "erlangC_pwait": 0.373569,
      "rho": 0.842105,
      "z_exp_vs_erlangC": 0.686047
    },
    {
      "R": 64,
      "c": 69,
      "des_exp_pwait": 0.440691,
      "des_exp_se": 0.015534,
      "des_exp_util": 0.929724,
      "des_h2_pwait": 0.494776,
      "des_h2_se": 0.028067,
      "des_h2_util": 0.93277,
      "erlangC_pwait": 0.432521,
      "rho": 0.927536,
      "z_exp_vs_erlangC": 0.52593
    }
  ],
  "erlangC_ledger": [
    {
      "R": 16,
      "c": 19,
      "c_tight_exact": 19,
      "erlangC_pwait": 0.373569,
      "headroom": 3,
      "headroom_over_sqrtR": 0.75,
      "mm1_pwait_same_rho": 0.842105,
      "per_unit_slack": 0.1875,
      "rho": 0.842105
    },
    {
      "R": 64,
      "c": 69,
      "c_tight_exact": 69,
      "erlangC_pwait": 0.432521,
      "headroom": 5,
      "headroom_over_sqrtR": 0.625,
      "mm1_pwait_same_rho": 0.927536,
      "per_unit_slack": 0.078125,
      "rho": 0.927536
    },
    {
      "R": 256,
      "c": 265,
      "c_tight_exact": 265,
      "erlangC_pwait": 0.466705,
      "headroom": 9,
      "headroom_over_sqrtR": 0.5625,
      "mm1_pwait_same_rho": 0.966038,
      "per_unit_slack": 0.035156,
      "rho": 0.966038
    },
    {
      "R": 1024,
      "c": 1041,
      "c_tight_exact": 1041,
      "erlangC_pwait": 0.48514,
      "headroom": 17,
      "headroom_over_sqrtR": 0.53125,
      "mm1_pwait_same_rho": 0.98367,
      "per_unit_slack": 0.016602,
      "rho": 0.98367
    }
  ],
  "gates": {
    "G1_pooling_decoupling_exact": {
      "R": 1024,
      "effect": 0.49853,
      "erlangC_pwait": 0.48514,
      "mm1_pwait_same_rho": 0.98367,
      "pass": true,
      "per_unit_slack": 0.016602,
      "rho": 0.98367
    },
    "G2_sqrt_staffing_form": {
      "beta": 0.506054,
      "gap": 0.025196,
      "headroom_over_sqrtR_at_Rmax": 0.53125,
      "pass": true
    },
    "G3_hyperexp_robustness_replicated": {
      "R": 64,
      "des_h2_pwait": 0.494776,
      "des_h2_se": 0.028067,
      "effect": 0.43276,
      "pass": true,
      "rho": 0.927536,
      "z": 15.418819
    }
  },
  "meta": {
    "alpha_target": 0.5,
    "beta": 0.506054,
    "count": 25000,
    "des_loads": [
      16,
      64
    ],
    "grounding": "https://www.columbia.edu/~ww2040/tutorial.pdf (Gans-Koole-Mandelbaum sec 4.1.1, eqs 14-15)",
    "head": "square-root safety staffing: safety headroom ~ beta*sqrt(R), so larger fleets safely run hotter at a fixed delay grade",
    "ledger_loads": [
      16,
      64,
      256,
      1024
    ],
    "reps": 15,
    "seed": 20260717,
    "warmup": 15000,
    "z_gate": 3.0
  }
}
Results-JSON sha256: 2597a50513127f663123c741aaca2bf646198035388a3325cbf4706e29092de8
```

## Verifier
`ideas/fleet/sqrt_safety_staffing.py` — stdlib only (`hashlib`, `heapq`, `json`, `math`, `random`, `statistics`), seeded at SEED=20260717. Two independent lines of evidence: exact Erlang-C (deterministic, carries the high-ρ claim, since an M/M/c relaxation time ~ 1/(1−ρ)² makes finite simulation untrustworthy near saturation) and a replicated M/G/c FCFS discrete-event simulation (valid replication SE, run only where it reaches steady state, extends the result to non-exponential service). `main()` runs `run()` twice in-process and asserts the two compact-canonical (sorted-keys, 6-dp-rounded) serializations are byte-identical before hashing; the digest is the results dict's OWN sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: no digest field on the dict, nothing written to disk).

## Reproduce
```
python3 ideas/fleet/sqrt_safety_staffing.py
```
Prints the results JSON then the `Results-JSON sha256:` line; deterministic across invocations (a second run is byte-identical); exit 0 with `all_pass=true`.

## Why it matters
Any pooled fleet of interchangeable workers — dispatch queues, autoscaling replicas, connection pools, GPU/job schedulers, on-call or support agents — can be sized by the √R rule instead of a fixed fractional buffer. Consolidating many small queues into one shared pool lets the merged fleet run at far higher utilization for the same wait probability, and the larger the fleet the larger the win; conversely, splitting one pool into k dedicated silos multiplies the safety staffing carried, because each silo re-pays its own β√R. The law says exactly when consolidation pays and how much slack a target service level actually needs — usually far less than a percentage-headroom rule of thumb budgets, and the gap widens with scale.

## Dedup (contrast vs prior lane heads)
- vs **`ideas/fleet/erlang-b-trunking-efficiency-2026-07-18.md`** (Erlang B) — that head is a LOSS system (blocked arrivals cleared, no queue) and its point is trunk-blocking efficiency; this is a DELAY system (Erlang C, arrivals queue) whose point is the √R staffing/utilization scaling. Different system, different quantity.
- vs **`ideas/fleet/palm-spares-insensitivity-2026-07-19.md`** (M/G/∞ spares, Palm's theorem) — infinite servers, no staffing decision at all; here the entire question is the finite minimal c and how it grows with load.
- vs **`ideas/fleet/service-variance-wait-tax-2026-07-18.md`** (Pollaczek–Khinchine variability tax) — that isolates how service VARIABILITY inflates wait at fixed capacity; this head fixes the delay probability and asks how STAFFING must scale with LOAD — a different axis (variability vs scale). G3 touches variability only to show the scaling is distribution-robust.
- vs **`ideas/fleet/two-choices-routing-cliff-2026-07-18.md`** / **`ideas/fleet/correlated-fleet-variance-floor-2026-07-18.md`** — those are load-balancing / variance-floor results at fixed capacity; this is a capacity-sizing law.

## Model basis (P024 discipline)
Exact Erlang-C (closed form, no fitted parameters) plus a parameter-free M/G/c simulation; β is solved from the target α, never tuned. The √R staffing form and the delay-probability limit are the documented eqs (14)–(15) of the grounding source, fetched live this session; G1's magnitudes are exact, and G3's are measured, not fitted.

## Gate power + margin ledger
| Gate | quantity | observed | threshold | margin |
|------|----------|----------|-----------|--------|
| G1 | ρ − P{wait} at R=1024 (exact) | 0.498530 | ≥ 0.40 | 0.098530 |
| G1 | per-unit slack (c−R)/R at R=1024 | 0.016602 | < 0.05 | 0.033398 |
| G2 | \|headroom/√R − β\| at R=1024 | 0.025196 | < 0.05 | 0.024804 |
| G3 | robustness z (ρ − P{wait}_H2 at R=64) | 15.418819 | z ≥ 3.0 | 12.418819 |
| — | DES vs Erlang-C max \|z\| (validation) | 0.686047 | \|z\| < 3.0 | 2.313953 |

## Probe report (v0, self-adversarial)
**1. Is the √R headroom real or a rounding artifact?** Real — headroom/√R falls 0.75 → 0.625 → 0.5625 → 0.531 across R=16→1024, converging to β=0.506; the ⌈·⌉ rounding only adds an O(1/√R) term that vanishes at scale (G2 gap 0.025 at R_max).
**2. Why gate the high-load claim on exact Erlang-C rather than the simulation?** An M/M/c queue's relaxation time grows like 1/(1−ρ)², so at ρ ≈ 0.98 a finite simulation cannot reach steady state; the exact closed form is the only trustworthy estimate there. The simulation is used only where it demonstrably converges (ρ ≤ 0.93) — disclosed, not hidden.
**3. Is the simulation's standard error valid?** Per-arrival wait indicators are autocorrelated, so a naive Bernoulli SE would understate the variance; the verifier instead runs 15 INDEPENDENT replications and takes the SE across replication means — the standard, valid estimator — and the DES matches exact Erlang-C to within 0.7σ at both DES loads (the validation row).
**4. Could G1 be trivial — doesn't any staffing beat one server?** The contrast is sharp precisely because the fleet runs at ρ=0.984, the regime where the folk belief predicts near-certain queueing; holding P{wait}=0.485 there is the non-obvious content, and G1 requires the gap to the single-server line to exceed 0.40.
**5. Is the effect an artifact of exponential service?** G3 re-runs under hyperexponential service (SCV ≈ 12.5) and the decoupling persists at ≥15σ — the known M/G/c QED robustness; disclosed that the exact α value shifts with service variability while the √R scaling does not.
**6. Is determinism real?** Every replication draws from its own integer-seeded random.Random; run() is executed twice in-process and asserted byte-identical before hashing; the digest reproduces cross-invocation (confirmed: two runs byte-identical).
**7. Does α=0.5 cherry-pick a flattering grade?** No — β is solved from α, so any α ∈ (0,1) gives its own β and the same √R form; α=0.5 is a mid-range service grade, and the law (headroom ∝ √R, ρ → 1) holds for every β > 0.
**8. What breaks the law?** Heavy-tailed (infinite-variance) service or strongly correlated arrivals leave the QED regime, and abandonment or blocking change the constant; the √R form is a many-server, finite-variance result — disclosed as the boundary, not claimed universal.

## One-line design fix
Size a pooled fleet by c = R + β√R (β set from the target wait probability), not by a fixed fractional headroom — and consolidate interchangeable queues rather than dedicating silos, since each split re-pays its own √R safety staffing.

**Recommendation: sim-ready**