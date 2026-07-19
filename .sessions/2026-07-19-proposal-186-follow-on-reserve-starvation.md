# PROPOSAL 186 — Follow-on reserve starvation: under a power-law portfolio, holding back ~half the fund to defend pro-rata in the winners beats spray-and-pray (round-44 VENTURE slot, P186 → V199, +13)

> **Status:** in-progress
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands on the FIRST commit with `Status: in-progress`, holding the substrate-gate red while the verifier is authored and proven. The final commit flips it to `complete`, releasing merge-on-green. Gate-red before the flip is the born-red exception, not a defect.

## Objective
Show, with a deterministic stdlib Monte-Carlo over a power-law venture portfolio, that a fund which RESERVES ~half its committed capital for pro-rata follow-ons in its eventual winners earns a strictly higher fund MOIC than a "spray-and-pray" fund that deploys the same capital entirely into initial checks (more names, zero reserves). The driver is convexity: outcomes are power-law, so nearly all return comes from a handful of winners; each un-defended follow-on round dilutes the fund's ownership in exactly those winners, and because the winners carry the whole return, the dilution tax lands disproportionately on the MOIC. Under-reserving does not "diversify away" risk — it starves the only positions that matter, capping the fund's upside.

## Constraints honored
- stdlib-only (`random, math, json, hashlib, sys`); Python 3.
- SEED = 20260717 pinned; fully deterministic.
- Common random numbers: the reserve and spray funds draw the SAME per-company outcome + dilution stream per trial, so ΔMOIC is a clean paired difference (only the capital-allocation policy differs).
- In-process double-run determinism asserted (`compute()` run twice, canonical dicts must be identical).
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: sha256 of the compact-canonical results dict IS the digest; the dict is not self-referential; pretty dump to stdout (indent=2, sort_keys), floats 6 dp; no on-disk JSON.
- Pre-registered ordered gates G1→G2→G3, matching the shipped verifier exactly.
- Grounding URL returns HTTP 200 and documents the specific head.
- Timestamps from `date -u`.

## Pinned world (committed constants — sim-lab must reproduce exactly)
SEED = 20260717 · TRIALS = 200000 · N_COMPANIES = 30 · FUND = 100.0 ($M) · INITIAL_CHECK = 2.0 · RESERVE_FRAC = 0.5 (reserve fund holds back $50M for follow-ons; spray fund deploys the full $100M into initial checks) · POWER_ALPHA = 2.0 (Pareto exit-multiple tail) · X_MIN = 1.0 · DILUTION_PER_ROUND = 0.20 · FOLLOW_ROUNDS = 3 · WINNER_DECILE = 0.10 · Z_GATE = 3.0 · MOIC_GATE = 1.0 (reserve/ spray MOIC ratio floor, in expectation) · COLD_ALPHA = 1.6 (steeper tail robustness) · floats rounded 6 dp · whole-dict / no-self-field / stdout-only.

## Gate-plan (pre-registered — must match the shipped verifier; z_gate = 3.0)
- **G1 — reserves beat spray (≥3σ).** Paired ΔMOIC = MOIC(reserve) − MOIC(spray) over TRIALS funds is positive at ≥3σ: z = mean(ΔMOIC)/(sd/√TRIALS) ≥ 3.0 AND mean(ΔMOIC) > 0. Defending pro-rata strictly raises fund MOIC.
- **G2 — the edge is the winners, not the tail of names (bound).** Decompose ΔMOIC by company rank: the share of the reserve fund's MOIC advantage contributed by the top-WINNER_DECILE companies is ≥ a pre-registered majority (≥ 0.75) at ≥3σ. The advantage concentrates in the winners the follow-ons defend, not in the extra initial names spray buys.
- **G3 — robust under a steeper power law (≥3σ).** Repeat at COLD_ALPHA = 1.6 (fatter winner tail): paired ΔMOIC > 0 at ≥3σ AND the G2 winner-concentration bound still holds. The effect survives — and widens — as the distribution gets more convex.

all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified at HEAD)
Follow-on reserves / pro-rata defense in venture: a fund holds back a large fraction of committed capital to buy its pro-rata in later rounds of its winners, because power-law returns concentrate in a few names and unreserved dilution erodes exactly those positions. To be verified live at HEAD before the flip (target: an established VC-practice reference on reserve ratios and pro-rata rights, e.g. a partner essay / primer documenting the ~50% reserve heuristic), with a `<url>@<40-hex-pin>` grounding pin captured this session. Grounds to the Pareto/power-law law of venture outcomes and the pro-rata participation right.

## Probe questions
**1.** Does the paired ΔMOIC = MOIC(reserve) − MOIC(spray) clear ≥3σ and stay strictly positive under SEED = 20260717?
**2.** Does the top-WINNER_DECILE contribute ≥ 0.75 of the reserve fund's MOIC advantage (the edge is the defended winners, not the extra names)?
**3.** Does the spray fund's MOIC cap out because un-defended dilution erodes its ownership in the winners across FOLLOW_ROUNDS rounds?
**4.** Does the cross-invocation double run reproduce the results-dict sha256 byte-for-byte?
**5.** Does the in-process double-run assertion hold (determinism)?
**6.** Does the grounding URL resolve live and document the reserve / pro-rata-defense head?
**7.** Does the steeper-tail gate (COLD_ALPHA = 1.6) preserve both the ≥3σ MOIC edge and the winner-concentration bound?
**8.** Are the pre-registered gates here identical to the gates the verifier ships?

## Outcome
Pending — born-red HOLD. Verifier `ideas/venture-lab/follow_on_reserve_starvation.py` + doc `ideas/venture-lab/follow-on-reserve-starvation-2026-07-19.md` to be authored next; this section is filled with the measured results-dict sha256, per-gate numbers, and the PR number on the flip to `complete`.
- Results-dict sha256: `<pending>`
- G1 reserves-beat-spray: `<pending>`
- G2 winner-concentration: `<pending>`
- G3 robust (steeper tail): `<pending>`
- all_pass = `<pending>`
- Targets sim-lab VERDICT 199 (P186 → V199, +13).

## ⟲ Previous-session review
PROPOSAL 185 (bufferbloat standing-queue, round-44 FLEET slot, sim-ready, targets V198, +13): a clean M/M/1/K queueing head — on a saturated server (ρ > 1) enlarging the finite buffer K makes mean sojourn time grow ~linearly (a permanent standing queue) while goodput stays pinned at μ, so the extra buffer buys latency and zero throughput. Gates pre-registered at ≥3σ with a shifted-load (ρ = 1.5) robustness gate, grounding pinned live to Bufferbloat, all_pass true, landed at PR #688. This P186 continues round-44 with the VENTURE slot (rotation FLEET → VENTURE → GAME → UNRELATED); no blocker seen.

## 💡 Session idea
Companion VENTURE head for a future slot: **the reserve-ratio interior optimum** — sweep RESERVE_FRAC from 0 to 0.8 and show fund MOIC is single-peaked, not monotone: too little reserve starves the winners (this P186), but too much reserve under-diversifies the initial portfolio so the fund never *finds* enough winners to defend, and the peak sits near the ~50% practitioner heuristic. Quantify the knee as a function of POWER_ALPHA (steeper tails push the optimum toward MORE reserve) and gate the peak's dominance over both endpoints at ≥3σ. Stdlib-checkable; grounds to the same power-law / pro-rata literature.

(End of card content.)
