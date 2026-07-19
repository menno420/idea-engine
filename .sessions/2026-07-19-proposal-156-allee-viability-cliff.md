# PROPOSAL 156 — the Allee viability cliff: below a critical density a "growing" population is deterministically doomed (P156 → V169, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-36's UNRELATED-slot PROPOSAL 156: a fresh, counterintuitive, quantifiable mechanism from population ecology. Head: the strong Allee effect — below a critical density threshold `A`, per-capita growth turns negative, so a population that is nominally "growing" (positive `r`, below carrying capacity `K`) is nonetheless deterministically doomed to extinction. The viability boundary is a step function at `A`, not a smooth gradient: just below `A` the basin drains to zero, just above `A` it climbs to `K`. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a shifted demographic-noise robustness gate) plus a proposal doc a VERDICT 169 session can check independently. Hand to VERDICT 169 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED=20260717 pinned; deterministic in-process double-run + cross-invocation double-run asserts; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, pretty indent=2 dump).
- three ordered z-gates on the `/se` convention (z_gate=3.0): G1 basin-boundary location, G2 extinction-fraction vs the 0.5 no-doom null, G3 robustness under a shifted (heavier) demographic-noise distribution.
- +13 offset (P156 → V169). Outbox append-only + dedupe. Status high-water take-max, never regress. Born-red HOLD; merge-on-green landing.
- Grounding cites a reachable real-world source; crossover/caveat disclosed honestly. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (VERDICT mirror = current tail; proposal high-water pre-P156, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): the strong Allee effect — a critical-density viability threshold below which per-capita growth is negative. https://en.wikipedia.org/wiki/Allee_effect@854835807f66e5b253350b8a3e79e9408b466b9e · fetched 2026-07-19T04:56:46Z — Allee (1931), *Animal Aggregations*; Courchamp, Berec & Gascoigne, *Allee Effects in Ecology and Conservation* (2008). The step-function extinction threshold is the field signature.

## Probe questions
**1.** Does the deterministic basin boundary sit at exactly the Allee threshold `A`, invariant across different `(r, K)`? — the noise-free map `x_{t+1} = x_t + r x_t (1 - x_t/K)(x_t/A - 1)` has an unstable fixed point at `A`; the verifier locates the basin boundary and measures its invariance across sampled `(r, K)` pairs.
**2.** Is the extinction fraction just BELOW `A` decisively above the 0.5 no-doom null while just ABOVE `A` it is ≈0? — G2 measures the extinction fraction in a thin band below `A` (expect →1) against the null 0.5, and confirms the fraction just above `A` collapses to ≈0.
**3.** Does the viability cliff survive a shifted (heavier) demographic-noise distribution? — G3 re-runs the below-`A` extinction fraction under a shifted, heavier-tailed demographic-noise draw and reports it stays decisively above 0.5, an honest robustness gate.
**4.** Crossover, not the claim: a fleet/venture "critical-mass adoption" reading exists (a product/network below a critical adoption density decays deterministically). Is it disclosed as a crossover, not asserted as the ecological claim? — disclosed as a crossover analogy only; the verified claim is the population-ecology step function.

## Outcome
Verifier `ideas/fleet/allee_viability_cliff.py` + doc `ideas/fleet/allee-viability-cliff-2026-07-19.md` committed at `7ffc453`. Three z-gates PASS in order — G1 doomed-below z=+20.0 (p_below=1.0), G2 safe-above z=+20.0 (p_above=0.0), G3 robust-under-shifted-noise z=+6.29325 (p_below_hi=0.9125, p_above_hi=0.09, gap=0.8225); all_pass=true, first_failing_gate=null. Deterministic basin boundaries [30.0, 30.0, 30.0] all at A=30 (invariant across (r,K)). results-dict sha256 `bbc42b796c1dab6fae0b4be5da91e277a737cfdd5fd61246700fe826600b9471` reproduced byte-identical across an in-process + cross-invocation double-run. Outbox PROPOSAL 156 block appended (status: sim-ready, P156 → V169, +13). PR #619.

## ⟲ Previous-session review
Round-36 prior slice (P154 growth-endurance dominance → V167) landed clean on three ≥3σ gates with the whole-dict digest and shifted-distribution robustness posture; that verifier discipline carries forward here into the unrelated slot P156 → V169 (+13).

## 💡 Session idea
Allee hysteresis / rescue effect: once a population collapses below `A`, re-establishment requires pushing density back above `A` — quantify the bistability hysteresis / recovery gap between the collapse threshold and the re-establishment threshold. Named, not authored.
