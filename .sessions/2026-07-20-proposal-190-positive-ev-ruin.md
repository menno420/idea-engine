# PROPOSAL 190 — Positive-EV ruin (ergodicity): a repeated multiplicative bet with strictly positive expected value drives the typical investor almost surely to ruin because the time-average growth rate is negative (round-45 VENTURE slot, P190 → V203, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning
>
> **Born-red HOLD (cleared).** This card landed born-red as `in-progress` on the FIRST commit to hold the PR/substrate gate red while the verifier, proposal doc, and outbox block were authored and proven. It flips to `complete` LAST — after the verifier reproduces a byte-identical results-dict sha256 with all gates green AND the outbox block is appended and the heartbeat written. The born-red HOLD is the sole legitimate red before that flip; every other gate red is a real defect.

## Objective
Show that the folk rule "positive EV ⇒ take it and repeat" is exactly wrong under multiplicative compounding. In the Peters coin (heads +50% → ×1.5, tails −40% → ×0.6, each prob 0.5), the ensemble/arithmetic expected multiplier is 1.05 (+5% EV, ensemble mean wealth ≈ 1.05^T rising) yet the time-average (geometric) multiplier is √(1.5·0.6) = 0.94868 < 1, so almost every individual path decays at −5.27%/round and the typical (median) investor is driven toward ruin. Venture lesson: an edge with genuine positive expected value, sized at full-stake and repeated, is not "compound your way to wealth" — it is a near-certain path to ruin unless the bet is Kelly-sized to make the TIME-AVERAGE growth positive.

## Constraints honored
- stdlib-only verifier (random, math, json, hashlib); SEED = 20260717 pinned; a fresh random.Random(SEED) at the start of EACH full run.
- deterministic in-process double-run with an assert; cross-invocation byte-identical results-dict sha256.
- ≥3σ gates: G1 time-average NEGATIVE, G2 arithmetic EV POSITIVE, G3 typical investor RUINED (majority below start), G4 robustness/shift world (U=1.6, D=0.55) preserving all three signs.
- DIGEST-POSTURE: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY; the compact-canonical results-dict sha256 IS the digest; stdout prints the pretty dump (indent=2) with floats at 10 dp; no on-disk JSON.

## Pinned world
- W0 = 1.0; T = 100 rounds/path; P = 20000 paths; z_gate = 3.0; ROUND_DP = 10.
- Base world: U = 1.5 (prob 0.5), D = 0.6 (prob 0.5) — ensemble expected multiplier 1.05, geometric 0.94868.
- Shifted robustness world: U = 1.6, D = 0.55 — ensemble expected multiplier 1.075 (still +EV), geometric √0.88 = 0.93808 (still < 1).

## Gate-plan (pre-registered)
- **G1 time-average negative:** z = −mean_time_avg_growth / SE(time_avg_growth). Pass if mean_time_avg_growth < 0 AND z ≥ 3.
- **G2 arithmetic EV positive:** z = mean_per_round_simple_return / SE(per_round_simple_return over all path-rounds). Pass if mean_per_round_simple_return > 0 AND z ≥ 3.
- **G3 typical investor ruined:** p̂ = frac_below_start; z = (p̂ − 0.5)/√(0.25/P). Pass if p̂ > 0.5 AND z ≥ 3.
- **G4 robustness/shift:** re-run whole sim at U=1.6, D=0.55; time-avg < 0 (z≥3) AND per-round > 0 (z≥3) AND frac_below_start > 0.5 (z≥3).
- all_pass = G1 ∧ G2 ∧ G3 ∧ G4.

## GROUNDING (verified live)
> **Grounding:** https://github.com/elemer1/elemer1.github.io/blob/def46918c26483bdd11580bc0851956536306c56/_markdown/The%20Barrier%20that%20Moved.md@def46918c26483bdd11580bc0851956536306c56 · fetched 2026-07-20T00:52:17Z

Reference (external, reachable): "For the coin with factors 1.5 and 0.6 at probability 1/2: E[m] = 1.05 so E[X_n] = 1.05^n → ∞ (the ensemble diverges to infinite wealth), while E[ln m] < 0 so X_n → 0 almost surely (every individual trajectory is ruined). Positive ensemble growth and almost-sure individual ruin coexist, with no contradiction." — *The Barrier That Moved* (elemer1.github.io), Result 6, GitHub source verified live HTTP 200 this session. Corroborated by Wikipedia "Ergodicity economics" (https://en.wikipedia.org/wiki/Ergodicity_economics, HTTP 200 this session): "over time, with probability one, wealth decreases by about 5% per round, in contrast to the increase by 5% per round of the expected value."

## Probe questions
**1. Is this just "geometric mean < arithmetic mean", i.e. a trivial AM-GM restatement?**
**2. Are the ≥100σ z-scores just an artefact of a huge P·T sample rather than a real effect?**
**3. Could the result be a coding artefact of how "ruin" or the median is computed?**
**4. Does the paradox survive a different world, or is it tuned to U=1.5/D=0.6?**
**5. Is "almost-sure ruin" honestly stated given the ensemble mean is huge and rising?**
**6. Does Kelly-fractional sizing restore positive time-average growth on the same +EV edge?**

## Outcome
Verifier reproduced byte-identical stdout across two separate processes AND an in-process double-run; results-dict sha256 = `8d04b241d3589e2e49337c087da623d73c47dbe84074eaf5596bfa39db3c5336`. all_pass = **true**, first_failing_gate = null.
- **G1 time-avg negative (base):** mean_time_avg_growth −0.0527741776 (< 0 ✓), z = 163.2077618449 (≥ 3 ✓).
- **G2 arithmetic EV positive (base):** mean_per_round_simple_return +0.0499077500 (> 0 ✓), z = 156.8448905713 (≥ 3 ✓).
- **G3 typical investor ruined (base):** frac_below_start 0.8623 (> 0.5 ✓), z = 102.4739147296 (≥ 3 ✓); corroborated by median_final_wealth 0.0051537752 and frac_ruined_10pct 0.75635, against mean_final_wealth 55.6049183908 (ensemble rises).
- **G4 robustness/shift (U=1.6, D=0.55):** time-avg −0.0632973382 (z=169.6825537139), per-round +0.075609 (z=203.6710827592), frac_below_start 0.8627 (z=102.5870518145) — all three signs at ≥3σ ✓.
- all_pass = **true** (G1 ∧ G2 ∧ G3 ∧ G4).

## ⟲ Previous-session review
Round-45 opened in the FLEET slot with P189 (ski-rental keep-warm break-even → V202, +13). The rotation is fleet → venture → game → unrelated; this card opens the VENTURE slot of round-45 (P190 → V203, +13). The prior VENTURE head was P186 (follow-on-reserve-starvation → V199, APPROVED). A venture-lab inventory scan confirmed no time-average/ergodicity/volatility-drag head is shipped — the nearest neighbours (term-sheet winner's curse, follow-on reserve starvation) are order-statistics/selection results with no single-agent multiplicative-compounding mechanism, so this is a fresh lane. Sibling verdict runs and the mirror may run concurrently — rebase-and-union before each push; proposal high-water advances P189 → P190 (union-max, no regress).

## 💡 Session idea
Companion head for a later VENTURE slot: quantify the Kelly-restoration — for the SAME +EV coin, sweep the bet fraction f and locate the f-interval where the time-average growth rate turns positive, the growth-optimal f*, and the "over-betting cliff" beyond which even a positive-EV edge goes back to almost-sure ruin. It converts the paradox from a warning into a sizing rule and gives a fleet-transferable knob for any repeated multiplicative resource bet.
