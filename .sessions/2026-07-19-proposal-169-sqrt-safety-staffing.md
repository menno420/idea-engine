# PROPOSAL 169 — Square-root safety staffing: safety headroom ≈ β√R, so larger fleets safely run hotter (P169 → V182, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands first with `Status: in-progress` to hold the substrate gate red on this PR (born-red HOLD). It flips to `complete` as the final commit, after the verifier, proposal doc, outbox block, and heartbeat are in place — that flip releases the landing workflow. Gate-red until the flip is intended, not a defect.

## Objective

Round-40 FLEET-slot opener. Author PROPOSAL 169 and its stdlib verifier for a fresh, counterintuitive, quantifiable fleet-capacity mechanism: the **square-root safety-staffing law** (Halfin–Whitt QED regime). Pairs with sim-lab VERDICT 182 (+13).

Head: to hold the probability an arriving unit must wait fixed at a target α, an M/M/c fleet needs only c = R + β√R servers (R = λ/µ the offered load; β the service grade solving α = [1 + βΦ(β)/φ(β)]⁻¹). Safety headroom grows only as √R, so per-unit slack (c−R)/R = β/√R → 0 and utilization ρ = 1 − β/√R → 1 as the fleet grows — yet delay stays ≈ α. Larger fleets safely run hotter at the same service quality; fixed fractional headroom over-provisions without bound.

## Constraints honored

- Stdlib-only verifier (`hashlib, heapq, json, math, random`); SEED = 20260717.
- Deterministic: each simulation uses its own integer-seeded RNG, so output is byte-identical in-process and across invocations; run() double-run asserted identical; sha256 of the canonical results dict disclosed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY).
- Grounding fetched live this session and confirmed to document the specific c = R + β√R form and the α = [1 + βΦ(β)/φ(β)]⁻¹ limit (eqs 14–15).

## GROUNDING (verified at HEAD)

Gans, Koole & Mandelbaum, "Telephone Call Centers: Tutorial, Review, and Research Prospects," §4.1.1 "Square-Root Safety Staffing," eqs (14)–(15): https://www.columbia.edu/~ww2040/tutorial.pdf — WebFetch-resolved (HTTP 200) this session; eq (15) states N = R + β√R, eq (14) the delay-probability limit.

## Pre-registered gates (must match the shipped verifier), z_gate = 3.0

- **G1 — pooling decouples utilization from delay (≥3σ, exponential service):** at the largest fleet (R = 1024), nominal utilization ρ ≈ 0.98 yet simulated P{wait} ≈ α, far below the ρ a single un-pooled server at the same load would suffer. Effect = ρ − P{wait} is ≥ 3σ positive.
- **G2 — square-root staffing form (deterministic identity):** headroom/√R converges to β at scale; |headroom(R_max)/√R_max − β| < 0.05.
- **G3 — robustness under a shifted service distribution (≥3σ):** repeat G1 with hyperexponential service (SCV > 1, same mean); the pooling decoupling survives (ρ − P{wait} ≥ 3σ) and delay stays unsaturated (P{wait} < 0.9).

all_pass = G1 ∧ G2 ∧ G3.

## Probe questions

**1.** Does the grounding source state the specific √R form, not just Erlang-C generally? Yes — eq (15) N = R + β√R verbatim; confirmed live this session.

**2.** Is the effect an artifact of the exponential-service assumption? G3 re-runs under hyperexponential service to show the decoupling is distributional-robust (the known M/G/c QED property).

**3.** Is c = R + β√R actually near-minimal? The verifier also reports the exact minimal integer staffing c_tight (smallest c with Erlang-C ≤ α) alongside the √R staffing for each load, for an independent check.

**4.** Could G1 be trivial (any staffing beats a single server)? The contrast is sharp precisely because the fleet runs at ρ ≈ 0.98 — a regime where the folk belief predicts near-certain queueing — yet holds P{wait} ≈ α.

## Outcome

Pending — filled at the flip commit with the run digest, gate z-values, merge SHA, and PR number.

## ⟲ Previous-session review

P168 (round-39 UNRELATED slot, Condorcet voting cycle) landed sim-ready; this seat opens round-40 in the FLEET slot per the fleet→venture→game→unrelated rotation, targeting VERDICT 182 (+13). No regressions observed in the outbox ledger at HEAD.

## 💡 Session idea

A companion FLEET head: **the pooling-vs-dedication tension** — square-root staffing quantifies the gain from one shared pool, but a following proposal could measure how much of that √R economy survives when skills/regions force partial dedication (the "flexibility structure" question), sharpening when a fleet should consolidate queues versus keep them separate.
