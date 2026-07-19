# PROPOSAL 169 — Square-root safety staffing: safety headroom ≈ β√R, so larger fleets safely run hotter (P169 → V182, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed first with `Status: in-progress` to hold the substrate gate red on this PR while the verifier, proposal doc, and outbox block were assembled; this flip to `complete` is the final commit and releases the landing workflow.

## Objective

Round-40 FLEET-slot opener. Author PROPOSAL 169 and its stdlib verifier for a fresh, counterintuitive, quantifiable fleet-capacity mechanism: the **square-root safety-staffing law** (Halfin–Whitt QED regime). Pairs with sim-lab VERDICT 182 (+13).

Head: to hold the probability an arriving unit must wait fixed at a target α, an M/M/c fleet needs only c = R + β√R servers (R = λ/µ the offered load; β the service grade solving α = [1 + βΦ(β)/φ(β)]⁻¹). Safety headroom grows only as √R, so per-unit slack (c−R)/R = β/√R → 0 and utilization ρ = 1 − β/√R → 1 as the fleet grows — yet delay stays ≈ α. Larger fleets safely run hotter at the same service quality; fixed fractional headroom over-provisions without bound.

## Constraints honored

- Stdlib-only verifier (`hashlib, heapq, json, math, random, statistics`); SEED = 20260717.
- Deterministic: each simulation replication uses its own integer-seeded RNG, so output is byte-identical in-process and across invocations; run() double-run asserted identical; sha256 of the canonical results dict disclosed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY).
- Grounding fetched live this session and confirmed to document the specific c = R + β√R form and the α = [1 + βΦ(β)/φ(β)]⁻¹ limit (eqs 14–15).

## GROUNDING (verified at HEAD)

Gans, Koole & Mandelbaum, "Telephone Call Centers: Tutorial, Review, and Research Prospects," §4.1.1 "Square-Root Safety Staffing," eqs (14)–(15): https://www.columbia.edu/~ww2040/tutorial.pdf — WebFetch-resolved (HTTP 200) this session; eq (15) states N = R + β√R, eq (14) the delay-probability limit.

## Pre-registered gates (match the shipped verifier), z_gate = 3.0

Method note: the high-utilization claim is carried by exact closed-form Erlang-C (an M/M/c relaxation time ~ 1/(1−ρ)² makes finite simulation untrustworthy near saturation), and the discrete-event simulation — with independent replications for a valid standard error — is run only where it reaches steady state and supplies the non-exponential robustness gate.

- **G1 — pooling decouples utilization from delay (deterministic, exact Erlang-C at R_max=1024):** ρ ≥ 0.95 yet exact P{wait} ≤ α + 0.02, with the gap to the M/M/1-at-same-utilization delay (ρ) ≥ 0.40 and per-unit slack (c−R)/R < 0.05.
- **G2 — square-root staffing form (deterministic identity):** headroom/√R converges to β at scale; |headroom(R_max)/√R_max − β| < 0.05.
- **G3 — robustness under a shifted service distribution (≥3σ, replicated DES at R=64):** under hyperexponential service (SCV ≈ 12.5, same mean), the decoupling survives (ρ − mean P{wait} ≥ 3σ across replications) and delay stays unsaturated (mean P{wait} < 0.9).

all_pass = G1 ∧ G2 ∧ G3.

## Probe questions

**1.** Does the grounding source state the specific √R form, not just Erlang-C generally? Yes — eq (15) N = R + β√R verbatim; confirmed live this session.

**2.** Is the effect an artifact of the exponential-service assumption? G3 re-runs under hyperexponential service to show the decoupling is distribution-robust (the known M/G/c QED property).

**3.** Is the simulation's significance valid given autocorrelated wait indicators? The verifier uses independent replications (not a naive Bernoulli SE) and runs the DES only where it reaches steady state; the exact Erlang-C carries the high-ρ claim.

**4.** Could G1 be trivial (any staffing beats a single server)? The contrast is sharp precisely because the fleet runs at ρ ≈ 0.98 — a regime where the folk belief predicts near-certain queueing — yet holds P{wait} ≈ α.

## Outcome

Landed on PR #653. Verifier `ideas/fleet/sqrt_safety_staffing.py` runs deterministically (two invocations byte-identical), `all_pass=true`, Results-JSON sha256 `2597a50513127f663123c741aaca2bf646198035388a3325cbf4706e29092de8`. Gates: G1 exact ρ=0.98367 vs P{wait}=0.48514 (gap 0.49853, per-unit slack 0.016602); G2 headroom/√R=0.53125 vs β=0.506054 (gap 0.025196); G3 R=64 z=15.418819, mean P{wait}_H2=0.494776. DES matches exact Erlang-C within 0.69σ (validation). Verifier+doc commit 711112d5; outbox PROPOSAL 169 block appended, proposal high-water P168 → P169; claim released.

## ⟲ Previous-session review

P168 (round-39 UNRELATED slot, Condorcet voting cycle) landed sim-ready; this seat opens round-40 in the FLEET slot per the fleet→venture→game→unrelated rotation, targeting VERDICT 182 (+13). No regressions observed in the outbox ledger at HEAD.

## 💡 Session idea

A companion FLEET head: **the pooling-vs-dedication tension** — square-root staffing quantifies the gain from one shared pool, but a following proposal could measure how much of that √R economy survives when skills/regions force partial dedication (the "flexibility structure" question), sharpening when a fleet should consolidate queues versus keep them separate.