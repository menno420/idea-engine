# PROPOSAL 187 — Glicko rating order-sensitivity: an identical 6W-6L record against an identical opponent field ends at a DIFFERENT Glicko rating depending only on the ORDER of the results, because RD shrinks after each game and weights early games more (round-44 GAME slot, P187 → V200, +13)

> **Status:** in-progress
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD — active.** This card lands on the FIRST commit with `Status: in-progress`, deliberately holding the substrate-gate red while the verifier is authored and proven. The flip to `complete` (LAST commit, after the heartbeat) releases the HOLD (merge-on-green); until then the gate-red is the born-red exception, not a defect.

## Objective
Show, with a deterministic stdlib Monte-Carlo over the Glicko-1 rating system, that a player who posts the SAME multiset of game results (6 wins, 6 losses) against the SAME field of opponents ends at a materially DIFFERENT final rating depending only on the ORDER in which those games are processed (one game per rating period). The driver is the RD-weighted update: after each game the rating deviation RD shrinks, so the step size on the rating decays monotonically through the sequence — early (high-RD) games move the rating far more than late (low-RD) games. Processing all six wins first and then all six losses ("streak" order) therefore lands well BELOW processing them alternating W,L,W,L,... ("alternating" order), even though the record, the opponents, and the outcomes are identical. Order is not information, yet a sequential Glicko update prices it in.

## Constraints honored
- stdlib-only (`random, math, json, hashlib`); Python 3.
- SEED = 20260717 pinned; fully deterministic.
- Common random numbers: within each trial the streak and alternating regimes process the SAME 12 (opponent, result) pairs — only the ORDER differs — so the per-trial effect (streak − alt) is a clean paired difference.
- In-process double-run determinism asserted (`compute()` run twice, canonical dicts must be identical).
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: sha256 of the compact-canonical results dict IS the digest; the dict carries no self-referential sha field; pretty dump to stdout (indent=2, sort_keys), floats 6 dp; no on-disk JSON.
- Pre-registered ordered gates G1→G2→G3, matching the shipped verifier exactly.
- Grounding URL verified to resolve live and document the RD-weighted Glicko update.
- Timestamps from `date -u`.

## Pinned world (committed constants — sim-lab must reproduce exactly)
SEED = 20260717 · TRIALS = 5000 · N_GAMES = 12 (6 wins on even indices, 6 losses on odd indices) · R0 = 1500.0 (player start rating) · RD0 = 350.0 (player start deviation, max uncertainty) · OPP_RD = 30.0 (established opponents) · OPP_SD = 200.0 (opponent rating spread) · BASE_MEAN = 1500.0 · SHIFT_MEAN = 1700.0 (+200 shifted robustness field) · Q = ln(10)/400 · Z_GATE = 3.0 · SIGN_FRAC = 0.90 · MIN_POINTS = 5.0 · floats rounded 6 dp · whole-dict / no-self-field / stdout-only. Regimes: "alternating" = process the 12 pairs in index order (W,L,W,L,...); "streak" = process all six win-pairs (even indices) first, then all six loss-pairs (odd indices). Both consume the identical pair multiset; only the order differs. Effect(trial) = final_rating(streak) − final_rating(alternating). Base rng seed = SEED; shifted rng seed = SEED + 1.

## Gate-plan (pre-registered — must match the shipped verifier; z_gate = 3.0)
- **G1 — order matters (≥3σ).** In the base regime the mean per-trial effect (streak − alternating) is nonzero at |z| = |mean/(sd/√TRIALS)| ≥ Z_GATE = 3.0. Same record, same opponents, different order → a statistically overwhelming rating difference.
- **G2 — the effect is real and material (sign + magnitude bound).** The fraction of trials whose effect shares the sign of the mean is ≥ SIGN_FRAC = 0.90 (a consistent directional effect, not sampling noise), AND the absolute mean effect is ≥ MIN_POINTS = 5.0 Glicko rating points (materially larger than a rounding artifact).
- **G3 — robust under a shifted opponent field (≥3σ).** Repeat with the opponent field shifted +200 (SHIFT_MEAN = 1700): the mean effect clears |z| ≥ 3.0 AND keeps the SAME sign as the base regime. The order-sensitivity is not an artifact of one opponent-strength regime.

all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified live at HEAD)
The Glicko rating system (Mark E. Glickman) replaces a static Elo step with an RD-weighted update: g(RD) and the expected-score E enter a rating change scaled by the player's current rating deviation, and RD SHRINKS after each rated game (and grows during inactivity). Because the step size is a decreasing function of the number of games already processed, the SAME game contributes a larger rating move early (high RD) than late (low RD) — which is exactly what makes a sequential Glicko update order-dependent. Grounded to Glickman's Glicko write-up (https://www.glicko.net/glicko/glicko.pdf); verified live this session (HTTP 200, 6-page PDF; verbatim RD / g(RD) / E and "game outcomes always decrease a player's RD" quotes disclosed in the doc). Backup source: the Wikipedia "Glicko rating system" article, same formulas.

## Probe questions
**1.** Does the base-regime mean effect (streak − alternating) clear |z| ≥ 3.0 under SEED = 20260717?
**2.** Is the effect directionally consistent (same-sign fraction ≥ 0.90) and material (|mean| ≥ 5.0 Glicko points)?
**3.** Does the +200 shifted opponent field preserve both |z| ≥ 3.0 and the base-regime sign (robustness)?
**4.** Does the cross-invocation double run reproduce the results-dict sha256 byte-for-byte?
**5.** Does the in-process double-run assertion hold (compute() twice → identical canonical dict)?
**6.** Does the grounding URL resolve live and document the RD-weighted Glicko update (g(RD), E, RD shrink)?
**7.** Is the effect caused by RD-weighting specifically — i.e. would a batched (order-invariant) Glicko update show zero order effect by construction?
**8.** Are the pre-registered gates here identical to the gates the verifier ships?

## Outcome
Measured — all three gates PASS; born-red HOLD active, cleared at the flip. Verifier `ideas/superbot-games/glicko_rd_order_sensitivity.py` + doc `ideas/superbot-games/glicko-rd-order-sensitivity-2026-07-19.md` authored and proven; outbox PROPOSAL 187 block targets sim-lab VERDICT 200 (P187 → V200, +13).
- Results-dict sha256: `d4f690a51493a8fc32dd0971548078b059277ba81b6e02c84364415f4d168ba6` (byte-identical across two cross-invocation runs)
- G1 order-effect: base mean −60.205174 Glicko points, z = −118.692568 (|z| ≥ 3σ, PASS)
- G2 sign+magnitude: base same-sign fraction 0.9996, |mean| 60.205174 (≥ 0.90 and ≥ 5.0, PASS)
- G3 robust (+200 shift): shifted mean −54.313763, z = −100.513794, same sign as base (both negative) (PASS)
- all_pass = `true`
- Grounding: https://www.glicko.net/glicko/glicko.pdf resolved live (HTTP 200, 6-page PDF); documents the RD-weighted Glicko update.
- Targets sim-lab VERDICT 200 (P187 → V200, +13).

## ⟲ Previous-session review
PROPOSAL 186 (follow-on reserve starvation, round-44 VENTURE slot, sim-ready, targets V199, +13): under a power-law venture portfolio a fund that reserves ~half its capital to defend pro-rata ownership in its winners earns a higher fund MOIC (reserve 4.268874x vs spray 3.836963x, mean ΔMOIC +0.431911) than spray-and-pray, with the edge concentrated in the top-decile winners (0.823 of gross positive edge); gates pre-registered at ≥3σ with a steeper-tail (α=1.4) robustness gate, all_pass true, landed at PR #690. This P187 continues round-44 with the GAME slot (rotation FLEET → VENTURE → GAME → UNRELATED); no blocker seen.

## 💡 Session idea
Companion GAME head for a future slot: **the inactivity-return overshoot** — Glicko's RD grows during a lay-off (RD' = min(√(RD² + c²·t), 350)), so a genuinely strong player who takes a break returns with an inflated RD and the system moves their rating by an oversized step on the first result back; simulate a fixed-true-skill player under continuous play vs a play → gap → resume schedule and show the returning player's rating RMSE (and first-game overshoot) is materially larger despite the lay-off carrying zero information, gated at ≥3σ with a gap-length dose-response. Stdlib-checkable; grounds to the same Glicko RD literature.

(End of card content.)
