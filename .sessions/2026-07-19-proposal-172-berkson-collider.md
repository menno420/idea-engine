# PROPOSAL 172 — Berkson's collider paradox: selecting on a sum manufactures a negative correlation between independent traits (P172 -> V185, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

## Objective
Author round-40 UNRELATED-slot PROPOSAL 172 and land it green. Head: among a top-selected elite ranked by the additive composite of two statistically INDEPENDENT traits, the two traits are NEGATIVELY correlated (Berkson's collider paradox); the anti-correlation is a pure selection artifact (full-population correlation ~0), it deepens as the selection tightens (toward -1), and it survives non-normal marginals.

## Constraints honored
- Round-40 rotation fleet -> venture -> game -> UNRELATED (P171 was GAME/Blotto; this is UNRELATED — statistics of selection / collider bias, outside fleet ops, venture econ, and games).
- Firsthand stdlib-only verifier (`math, json, hashlib, random`); SEED=20260717; Z_GATE=3.0; whole-dict / no-self-field / stdout-only; deterministic byte-identical double-run.
- Grounding URL verified reachable this session; documents the specific head.
- +13 offset: P172 -> VERDICT 185.

## GROUNDING (verified at HEAD)
Berkson's paradox (Berkson 1946): conditioning on a collider (here, admission by a composite threshold) induces a spurious association between otherwise-independent causes. Reachability + revision pin recorded in the proposal doc's Grounding line.

## Pre-registered Gate-plan (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate=3.0)
- **G1 — selected elite is negatively correlated.** With gaussian independent traits, the top-10%-by-sum selected set has mean Pearson r < 0 at >= 3 sigma.
- **G2 — the negativity is selection-induced (reversal).** The same draws' full-population correlation is ~0 (|mean r| < 0.01); the selected-minus-population paired difference is negative at >= 3 sigma. The anti-correlation is manufactured by conditioning, not by the generating process.
- **G3 — robust under shifted (non-normal) marginals.** With uniform AND exponential independent marginals, the top-10%-by-sum selected correlation is still negative at >= 3 sigma each. Selection geometry, not gaussianity, drives it.
Non-gated evidence: deepening — tighter selection (top-2%) is more negative than loose (top-40%) at >= 3 sigma, trending toward the r -> -1 limit.

## Probe questions
1. Is the negative correlation an artifact of the composite being a SUM, or does any monotone selection score do it?
2. Could finite-sample bias (not selection) explain a negative r?
3. Does the effect vanish if traits are positively correlated in the population?
4. Is top-k selection materially different from threshold selection?
5. Does non-normality change the sign or only the magnitude?
6. Is the deepening monotonic in stringency?
7. What real decisions does this bias corrupt (admissions, hiring, hospital case-control studies)?
8. What is the closest prior lane head, and how is this distinct?

## Outcome
_pending verifier run — filled before flip._

## ⟲ Previous-session review
P171 (Blotto evenness trap, GAME slot) landed via merge-on-green with the whole-dict/no-self-field/stdout-only verifier posture and a closed-form identity gate. This card mirrors that posture and keeps the +13 offset and round-rotation intact (UNRELATED after GAME).

## 💡 Session idea
A companion "reverse-Berkson corrector": given a selected sample's observed negative trait-correlation and a known selection fraction, back out the true population correlation — turning the paradox into an estimator. Candidate future UNRELATED head.
