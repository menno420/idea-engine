# PROPOSAL 094 — the refund window is a conversion instrument, not a cost center: an indie digital product's net-revenue-maximizing refund window is INTERIOR — strictly more generous than the refund-minimizing zero-window, sitting just below the wardrobe extraction threshold (round-21 venture slot, P094 → V107, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · proposal-draft

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Open round 21 of the ORDER 003 pipeline at the VENTURE slot (rotation fleet→venture→game→unrelated; the round-21 fleet opener was P093, so this is the venture slot per ORDER 004 rule 3). Draft a genuinely new, counterintuitive, stdlib-simulable venture idea and land it sim-ready for sim-lab VERDICT 107 (+13): for an indie digital product, the refund window is a conversion instrument, not merely a cost — the net-revenue-maximizing window is INTERIOR, strictly MORE generous than the refund-minimizing zero-window every indie instinct reaches for, sitting right up to (but not past) the wardrobe extraction threshold where a generous window arms serial abusers. Tightening the window to "stop abuse" is a double loss: it forfeits the conversion safety-net that was the window's whole point.

## Constraints honored
- Append-only outbox: `## PROPOSAL 094` appended once; no prior entry edited.
- Claim placed before the work (control/claims/proposal-094-refund-window.md); the terminal VERDICT 106 mirror claim (idea-engine PR #476 + sim-lab PR #179 both merged, verified live) is pruned in this slice (housekeeping rider).
- SEEDLESS: pins a private SEED=20260717; the shared seed-ledger block 20261730 left untouched (P089/P090/P091/P092/P093 precedent).
- Grounded firsthand on the venture-lab decision world (idea-engine@8efd823, fetched this session); model-dependence disclosed (P024 discipline) — the constants are committed assumptions, the verdict tests the internal decision-logic, not empirical magnitudes.
- Gates pre-registered on a seeded deterministic dry-sim, byte-identical double-run; corrections disclosed.
- Neutral heartbeat; no cross-seat inbox edits; guard-fires.jsonl left uncommitted (classifier wall).

## What happened
Drafted PROPOSAL 094 (idea file + outbox block) at the round-21 VENTURE slot and calibrated four pre-registered gates on a stdlib-only deterministic dry-sim (byte-identical double-run, results-dict sha256 c3cfdae4…80dc, 15/15 self-checks, MC-vs-analytic max rel-err 0.44%). Dry-sim APPROVE: R1 — the interior refund window W=13 dominates the refund-minimizing W=0 by 93.3σ and the maximally-generous W=30 by 21.7σ; R2 — the abuse cliff is real, W=13 outsells W=14 by 20.7σ despite W=14 converting MORE buyers (refunds jump 43.1→67.4 as wardrobers arm past the 14-day threshold — "more generous, less net"); R3 — argmax interior across φ∈{0.06–0.10} and ρ×{0.8,1.2} ([5,5,4,5,5,5,5]), the φ=0.08 idx4/idx5 <1σ near-tie disclosed; R4 — knockout (dC=0, no conversion lift) returns the optimum to W=0 at 9.2σ, restoring the folk minimize-refunds monotone. Twin evaluators agree APPROVE/None. No model correction; one environmental note disclosed (Python 3.11 lacks random.binomialvariate, so the binomial draw uses the exact Bernoulli-sum fallback, A held at 5000). Housekeeping rider: pruned the terminal VERDICT 106 mirror claim (idea-engine PR #476 + sim-lab PR #179 both verified merged live).

## ⟲ Previous-session review
The prior slice closed the P093→V106 loop (metastable retry-storm collapse, APPROVE; mirrored into this repo's ledger via idea-engine PR #476, auto-merged 2026-07-17T09:22:58Z; sim-lab VERDICT 106 finalized PR #179) and rolled the baton to the round-21 venture slot. That card's 💡 suggested a retry-budget-calibration head as the next fleet-lane follow-up; per the fleet→venture rotation (ORDER 004 rule 3) this session instead opens the venture slot with a mechanistically distinct head — a post-purchase refund-policy optimum, the first venture idea to price a lifetime/return mechanic rather than a pre-purchase lever (category, price, series, channel). The retry-budget-calibration head remains available as a named fleet-lane follow-up.

## 💡 Session idea
Next baton after V107: a refund-window × price JOINT optimizer — does a higher price shift the safe window (a bigger wardrobe incentive arms extraction earlier), and is there a price at which the interior optimum collapses to W=0? Plus a heterogeneous-wardrobe-threshold head (W_abuse distributed rather than a single 14-day step) testing whether the cliff smooths into an interior ridge. Both are the named follow-ups in the P094 outbox block.

📊 Model: opus-4.8 · high · proposal-draft
