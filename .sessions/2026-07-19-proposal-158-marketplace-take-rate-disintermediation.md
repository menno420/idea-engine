# PROPOSAL 158 — marketplace take-rate disintermediation: net rake revenue is a hump in the take-rate, and the aggressive rake is strictly dominated (P158 → V171, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-37's VENTURE-slot PROPOSAL 158: a fresh, counterintuitive, quantifiable venture / marketplace-economics mechanism. Head: a marketplace's net take-rate (rake) revenue is NON-MONOTONIC in the rake — raising the take-rate t drives sellers whose idiosyncratic switching cost falls below t to transact off-platform (disintermediation), so on-platform GMV = GMV0·S(t) with S(t)=P(c≥t) the switching-cost survival curve, and platform revenue R(t)=t·S(t)·GMV0 is a hump: an interior revenue-optimal rake t* exists and the aggressive "charge what you can" rake is strictly dominated, with a large relative revenue loss for overshooting. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT 171 session can check independently. Hand to VERDICT 171 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED=20260717 pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, floats 6 dp, compact canonical payload hashed).
- three ordered z-gates (z_gate=3.0): G1 domination sign, G2 relative-effect vs the 0.10 null, G3 robustness under a shifted (lower-loyalty) switching-cost distribution.
- +13 offset (P158 → V171). Outbox append-only + dedupe. Proposal high-water take-max, never regress. Born-red HOLD.
- Grounding cites a reachable real-world source; model-dependence / crossover disclosed honestly. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (round-37 FLEET P157 → V170 opener is the tail; proposal high-water pre-P158, +13 offset).
- External phenomenon (reachable): the marketplace-rake disintermediation limit — Bill Gurley, "A Rake Too Far: Optimal Platform Pricing Strategy" (Above the Crowd, 2013): high take-rates invite off-platform leakage and competitive undercut, so the revenue-optimal rake is lower than "charge what the market bears" intuition.

## Probe questions
**1.** Is the hump real or an artifact of the linear-demand (uniform switching-cost) model? — the rake-as-price / leakage-as-demand structure R=t·S(t) is the monopoly-pricing identity; with c~Uniform[0,C] the argmax is the closed form t*=C/2, and G3 re-tests under a shifted distribution to confirm the sign is not tuned to one draw.
**2.** Does the aggressive rake really lose revenue in-sample? — G1 gates mean[R(t*)−R(t_max)] > 0 at ≥3σ; G2 gates the RELATIVE loss ≥ 10% at ≥3σ.
**3.** Is the optimum location model-dependent? — yes, disclosed (P024): the argmax LOCATION depends on the switching-cost law; the SIGN (a hump exists, the aggressive rake is dominated) and the order of magnitude survive the shifted draw (G3), where the optimum moves lower as loyalty falls.
**4.** Real phenomenon or textbook toy? — the documented marketplace-rake ceiling (Gurley, "A Rake Too Far"); the reflex it corrects — "the rake is a direct multiplier on revenue, charge as much as the market bears" — is the folk belief.

## Outcome
_(filled at flip — verifier numbers, digest, gate z-scores, outbox block, PR)_

## ⟲ Previous-session review
Round-37 opened at the FLEET slot with P157 (bullwhip order-variance amplification) → V170; the verifier discipline (whole-dict digest, shifted-distribution robustness gate, honest model-dependence disclosure) carries forward here into the VENTURE slot P158 → V171 (+13).

## 💡 Session idea
Named, not authored: the "rake ratchet under competitive entry" follow-on — once a rival marketplace exists, each platform's revenue-optimal rake falls further (Bertrand pressure on the rake), quantifying how the optimum t* shifts with the number of competing venues; a distinct marketplace-pricing counterintuition with a clean multi-platform verifier.
