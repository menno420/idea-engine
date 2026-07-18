# PROPOSAL 134 — cohort-blended LTV understatement (round-31 VENTURE slot)

> **Status:** `in-progress`
> 📊 Model: opus · high · idea/planning

born-red HOLD: this card lands `in-progress` on the FIRST commit so the substrate-gate stays red until the slice is done; it flips to `complete` as the deliberate LAST commit, which releases the landing workflow. The gate red on this PR is the HOLD, not a defect.

## Objective
Draft and land round-31 VENTURE-slot PROPOSAL 134 → VERDICT 147 (+13, pinned): a genuinely new venture-domain mechanism — collapsing a heterogeneous customer book to one blended churn rate and computing LTV = m/churn UNDERSTATES the portfolio's true average LTV (Jensen on the convex 1/c), with the gap driven by churn dispersion. Deliverable: markdown-first idea doc + committed stdlib verifier (SEED 20260717, three ≥3σ gates, whole-dict sha256), a deterministic dry-sim, the outbox block (P134 → V147), and a heartbeat. VERDICT 147 is a separate future slice — not written here.

## Constraints honored
- One change, one small PR; born-red card first commit, flip complete last.
- Verifier stdlib-only (random, math, json, hashlib); SEED 20260717; WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest; deterministic double-run.
- Outbox append-only, +13 offset cited (P134 → V147); no VERDICT written.
- `python3 bootstrap.py check --strict` green before final push.

## What happened
Authored `ideas/venture-lab/blended-churn-ltv-understatement-2026-07-18.md` (markdown-first) and its committed verifier `ideas/venture-lab/blended_churn_ltv_understatement.py`. Dry-sim ran deterministic (exit 0, identical double-run), all three ≥3σ gates PASS, results-dict sha256 disclosed in the doc + outbox done-when. Appended the PROPOSAL 134 outbox block and advanced the heartbeat (proposal high-water P134; baton → V146/V147 then round-31 GAME-slot P135).

## ⟲ Previous-session review
Round-31 opened with P133 (fan-out tail amplification, FLEET slot, #568, merged at d3e2bb1) — a clean convexity-of-tail-probability result. This slice continues the rotation (fleet→venture) and reuses the disciplined pattern: one closed-form anchor, three pre-registered gates with a dispersion-isolating G3, whole-dict digest. No regressions observed at HEAD; gate was green (advisory-only) before this slice.

## 💡 Session idea
The venture book keeps yielding "one summary statistic is biased" mechanisms (NRR mirage, retention mirage, now blended-churn LTV). A future cross-cutting proposal could unify them: a single verifier that measures the Jensen/aggregation gap of ANY convex unit-economics map (LTV=m/c, payback, magic-number) over a disclosed heterogeneity distribution, reporting the sign and the Var-driven magnitude — turning "which summary stat lies" into a parameterized family rather than one-off proposals.

## GROUNDING
- Base: https://github.com/menno420/idea-engine@d3e2bb18bfedba1bd6c0431c30ba33131caaf952 (origin/main HEAD at slice start, PROPOSAL 133 / #568).
- Refs: https://en.wikipedia.org/wiki/Jensen%27s_inequality + https://en.wikipedia.org/wiki/Customer_lifetime_value (both verified reachable 2026-07-18 via WebFetch).
