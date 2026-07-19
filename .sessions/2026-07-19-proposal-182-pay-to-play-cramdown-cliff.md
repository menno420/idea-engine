# Session — PROPOSAL 182 · pay-to-play cramdown cliff (round-43 VENTURE slot)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**BORN-RED HOLD.** This card lands first as `in-progress` on the opening commit to hold the PR red under the substrate-gate; it flips to `complete` on the final commit (after the verifier is green, the proposal doc is written, and the outbox block is appended), which clears the hold and releases the landing workflow.

## Objective

Author PROPOSAL 182 for the round-43 VENTURE slot: a fresh, quantifiable startup-economics mechanism — the **pay-to-play cramdown cliff**. In a down round carrying a pay-to-play provision, an existing preferred investor who does not write its pro-rata check is not merely diluted: its preferred is converted to common and its liquidation preference is wiped. The head is that, conditional on a non-home-run exit, the marginal pro-rata dollar is the highest-return dollar on the cap table, and the driver is the preferred→common CONVERSION, not the dilution — and the effect sharpens in cold markets. Targets sim-lab VERDICT 195 (+13 offset).

## Constraints honored

- Stdlib-only verifier; `SEED = 20260717`; deterministic; in-process double-run asserts identical results dicts; results-dict sha256 is the digest (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, P127+ twist).
- Dedup: scanned ideas/venture-lab/ and control/outbox.md. Distinct from the shipped fundraising/dilution cluster (option-pool-shuffle, founder-dilution-waterfall, full-ratchet-convexity, post-money-safe-stacking, term-sheet-winners-curse) and from the retention/LTV cluster (blended-churn-ltv-understatement, retention-survivorship-mirage, nrr-composition-mirage): pay-to-play conversion is a distinct named provision, none of the shipped heads touch it.
- ≥3σ gates; a robustness gate under a shifted (cold-market) exit distribution.
- Grounding URL verified live and documents the specific provision.

## Gate-plan (pre-registered — must match the shipped verifier)

Base config: existing investor A holds a prior $4M 1x preferred and 25% fully-diluted ownership entering a down round ($5M new money at $5M pre; post $10M). A's pro-rata is $1.25M. Exit value ~ lognormal (median $18M, sigma=0.95). Danger band = exit <= $15M (a non-home-run outcome). Single pari-passu 1x non-participating preferred tranche; seniors take the greater of pref-share or as-converted, common splits the residual.

Shifted config: cold market — lognormal (median $11M, sigma=1.20), fatter left tail into the preference stack.

- **G1 — marginal-dollar return (in-band):** conditional on a danger-band exit, expected value preserved by participating, per dollar of pro-rata check, >= 2.0 (RATIO_GATE) at >= 3 sigma.
- **G2 — conversion is the driver (in-band):** conditional on a danger-band exit, the value preserved by avoiding the preferred->common conversion is >= 1.5x (CONV_GATE) the value preserved by avoiding dilution, at >= 3 sigma (per-trial premium conv - 1.5*dil, mean > 0).
- **G3 — cold-market amplification:** the danger-band probability is strictly higher under the cold-market distribution than the base, at >= 3 sigma (two-proportion z), and the in-band conversion-dominance still holds under cold.

`all_pass = G1 ∧ G2 ∧ G3`

## GROUNDING (verified at HEAD)

Pay-to-play / cramdown is a real, documented down-round provision: a non-participating preferred holder's shares convert to common (losing the liquidation preference and anti-dilution). External reference verified live at authoring time (see the proposal doc front-matter Reference line for the pinned URL). Origin HEAD at branch cut: `cf06fddb`.

## Probe questions

1. Does the danger-band conditioning honestly scope the head, or does it cherry-pick the region where the effect exists?
2. Is the single-pari-passu-tranche waterfall convention (seniors take max of pref-share or as-converted; common splits residual) a fair simplification, or does it bias the cliff?
3. Is the 1:1 conversion assumption (no punitive pull-up) conservative for the head, and would a punitive conversion only strengthen it?
4. Does G2 genuinely isolate the conversion penalty from ordinary dilution, or do the two leak into each other?
5. Is the cold-market amplification (G3) an artifact of the sigma change rather than the median shift?
6. Would a participating (not non-participating) preferred, or a stacked multi-tranche stack, change the sign of the head?
7. Is the lognormal exit model doing load-bearing work, or does the cliff survive a different exit family?
8. Does the results-dict digest reproduce bit-identically across a fresh interpreter invocation?

## Outcome

`(filled at flip)`

## ⟲ Previous-session review

`(filled at flip)`

## 💡 Session idea

`(filled at flip)`
