# PROPOSAL 157 — bullwhip order-variance amplification: an order-up-to policy inflates order variance by 1+2L/p+2L^2/p^2, distribution-free (P157 → V170, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

This card is committed first with Status: in-progress; the substrate gate reports red while a session card is in-progress. The status flips to complete in the final commit once the verifier and proposal doc are in place.

## Objective
Author round-37's FLEET-slot PROPOSAL 157: a fresh, counterintuitive, quantifiable fleet-ops / supply-chain mechanism. Head: even when customer demand is i.i.d. and stationary, a rational order-up-to (base-stock) policy that forecasts lead-time demand with a p-period moving average makes the variance of orders placed upstream exceed the variance of demand by exactly 1 + 2L/p + 2L^2/p^2 — a factor that grows with the replenishment lead time L and shrinks with the forecast window p. The swing an upstream supplier sees is manufactured by the ordering policy, not by the customers, and it is distribution-free in the demand's shape. Deliver a stdlib-only deterministic verifier (SEED pinned, ≥3σ gates including a distribution-free robustness gate) plus a proposal doc a VERDICT 170 session can check independently.

## Constraints honored
- stdlib-only verifier; SEED pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, floats 6 dp).
- +13 offset (P157 → V170). Outbox append-only + dedupe. Proposal high-water take-max, never regress.
- Grounding cites a reachable real-world source; distribution-free/caveat disclosed honestly.
- Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (round-36 tail P155→V168; proposal high-water pre-P157, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): the bullwhip effect — J. Forrester, "Industrial Dynamics" (1961); H. Lee, V. Padmanabhan, S. Whang, "The Bullwhip Effect in Supply Chains," Sloan Management Review (1997); closed form in F. Chen, Z. Drezner, J. Ryan, D. Simchi-Levi, "Quantifying the Bullwhip Effect in a Simple Supply Chain," Management Science 46(3):436-443 (2000). Secondary (reachable): Wikipedia "Bullwhip effect."

## Probe questions
**1.** Is the amplification real or an artifact of the demand distribution? — the ratio 1+2L/p+2L^2/p^2 depends only on the order-up-to recursion coefficients, not the demand law; the verifier draws actual i.i.d. demand and measures Var(Q)/Var(D).
**2.** Does the closed form actually hold in-sample? — G2 gates the measured ratio against 1+2L/p+2L^2/p^2 at ≥3σ within a 5% relative-error ceiling.
**3.** Does distribution shape matter? — G3 re-measures under a heavy-tailed (exponential) demand and a shifted (L,p) and gates the same closed form, confirming the ratio is a policy property, not a value property.
**4.** Real phenomenon or textbook toy? — documented bullwhip effect (Forrester; Lee-Padmanabhan-Whang; Chen et al.) with a published closed form; the reflex it corrects — "reorder exactly what you used and orders stay as stable as demand" — is the folk belief.

## Outcome
(pending — filled after the verifier's cross-invocation double-run)

## ⟲ Previous-session review
(pending)

## 💡 Session idea
(pending)
