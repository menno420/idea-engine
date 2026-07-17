# A competitive game's "streak shield" — banked after W consecutive wins to negate the next loss, sold as anti-tilt protection for STRUGGLING players — is REGRESSIVE: it boosts the rating of an already-high-skill cohort MORE than the low-skill cohort it is marketed to protect, the high-vs-low rating-uplift gap exceeding 3σ.

> **State:** sim-ready
> **Class:** superbot-games · competitive rating dynamics · matchmaking / anti-tilt mechanic design
> **Target:** sim-lab (VERDICT 116, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@dc75cb3 · fetched 2026-07-17T23:43:08Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/streak_shield_regression.py` (random, math, json, hashlib) — dry-sim exit 0, gate PASS, results-dict sha256 0294f757…022c09b4 (see Verifier + Dry-sim below).

## The phenomenon (one line)
Give players a "streak shield" — after W=3 consecutive wins they bank a shield that negates their next loss (the loss is scored as a win) — and the mechanic marketed as protection for the players who tilt and lose actually amplifies the rating of the players who were already winning: a high-skill cohort (per-game win prob 0.55) gains a mean rating uplift of +35.3 versus +21.6 for a low-skill cohort (0.45) over 200 games, a gap of +13.7 at 153σ.

## The folk belief
"A streak shield is anti-tilt protection — it catches struggling players before a bad run snowballs, keeping the bottom of the ladder from rage-quitting." The mechanic is pitched (to players and to the designer tuning retention) as a floor under the weak: a safety net that absorbs one loss so a cold streak doesn't spiral. The intuition is that the players who *need* protection — the ones losing more — are the ones the shield helps most.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
The shield is earned by WINNING (W consecutive true wins banks one shield) and spent NEGATING A LOSS (a −1 outcome becomes a +1, a net rating swing of +2 per shield consumed). So the resource that funds "protection" is manufactured by the same skill that makes protection unnecessary. Which cohort banks more shields? The rate of completing a length-W win run is monotone increasing in the per-game win probability p — a p=0.55 player strings three wins together far more often than a p=0.45 player — so the high-skill cohort accrues shields (and therefore the +2 loss-negation swings) at a strictly higher rate. Both cohorts have plenty of losses available to absorb, so the binding constraint on uplift is shield SUPPLY, which is regressive in skill. The result: the "anti-tilt" mechanic delivers more rating protection to the cohort that was already ahead than to the cohort it is sold to protect. The counterintuitive core — a protection benefit gated on a win-streak is a benefit gated on skill, so it flows uphill. The honest one-line fix is to invert the trigger: grant shields on LOSS streaks (bank a shield after W consecutive losses), which funds the safety net from the exact signal — a cold run — the mechanic claims to catch, making the benefit progressive instead of regressive.

## The formal model (committed constants — sim-lab must reproduce exactly)
- A player plays GAMES=200 games; each game is a true win with probability p (Bernoulli, iid).
- Streak counter: each true win increments the streak; on reaching STREAK_W=3 it banks one shield and resets the streak to 0.
- On a true loss: if the shield policy is active and a shield is banked, consume one shield — the loss is scored as a WIN (+1 instead of −1) and the streak resets to 0; otherwise the loss is scored as a loss and the streak resets to 0.
- Net rating = (wins scored) − (losses scored). A consumed shield is a +2 swing versus the no-shield baseline (a −1 becomes a +1).
- **Uplift** for a player = net rating WITH shield − net rating WITHOUT shield, on the SAME per-game outcome sequence (paired Monte Carlo — the only difference between the two scorings is whether shields are honored).
- Cohort uplift = mean of per-player uplift over N_PER_COHORT=10000 players; standard error = sample-sd / √N.
- Regressive claim: high-skill cohort mean uplift − low-skill cohort mean uplift, over the two-sample standard error √(se_low² + se_high²), is ≥ SIGMA_GATE=3.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- N_PER_COHORT = 10000 (players simulated per cohort)
- GAMES = 200 (games per player)
- STREAK_W = 3 (consecutive true wins to bank one shield)
- LOW_P = 0.45 (low-skill per-game win probability — the cohort the shield is marketed to protect)
- HIGH_P = 0.55 (high-skill per-game win probability — the already-strong cohort)
- SIGMA_GATE = 3.0

## Pre-registered gates (APPROVE iff ALL hold)
- **G1 — regressive amplification (headline):** high-skill cohort mean uplift exceeds low-skill cohort mean uplift by ≥ 3σ, where σ is the two-sample standard error √(se_low² + se_high²). This is the regressivity claim: the "protection" flows uphill.
- **G2 — both cohorts positive:** low-skill cohort mean uplift > 0 AND high-skill cohort mean uplift > low-skill cohort mean uplift. Confirms the shield helps everyone SOME (it is a positive-sum buff, not a redistribution) but helps the strong strictly more — the regressivity is in the DERIVATIVE, not a sign flip.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `passed` field encodes exactly `uplift_gap_sigma ≥ 3 AND low_uplift_mean > 0 AND high_uplift_mean > low_uplift_mean`). Gate failing → REJECT (the regressive-amplification claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- low_uplift_mean = 21.6436 (se 0.05745)
- high_uplift_mean = 35.313 (se 0.068073)
- uplift_gap = 13.6694
- **G1 regressive-amplification:** uplift_gap_sigma = 153.4585 — PASS (≥ 3σ; high cohort gains 1.63× the low cohort's protection)
- **G2 both-positive / strict ordering:** low_uplift_mean = 21.6436 > 0 AND high_uplift_mean 35.313 > low 21.6436 — PASS
- regressive = true; passed = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = 0294f75799989decfe6c0166136691509239a91ac8eaba75d1932074022c09b4**

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/superbot-games/streak_shield_regression.py`. Seeds once with SEED=20260717, then for each cohort simulates N_PER_COHORT=10000 players of GAMES=200 iid Bernoulli(p) outcomes, scoring each outcome sequence TWICE (shield on / shield off) on the SAME draws and recording the per-player uplift. It computes each cohort's mean uplift and standard error, the high-vs-low gap and its two-sample σ, evaluates G1/G2, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff the gate passes.

Reproduce:

```
python3 ideas/superbot-games/streak_shield_regression.py
```

Expected: passed=true, exit 0, uplift_gap_sigma=153.4585, results-dict sha256 = 0294f75799989decfe6c0166136691509239a91ac8eaba75d1932074022c09b4.

## Why it matters (game design)
"Anti-tilt" / loss-protection mechanics are a live retention lever in ranked competitive games (streak shields, loss-forgiveness tokens, MMR-decay dampers). They are justified internally as help for the bottom of the ladder — the churning, tilting, cold-streak players. This proposal shows that when the protection is EARNED BY WINNING (a win-streak trigger), it is regressive: it amplifies the rating of the cohort that was already winning more than the cohort it is sold to protect, because shield supply scales with skill. Decision rule for a designer: audit any protection mechanic by the cohort-conditional benefit, not the average benefit — if the resource that funds the safety net is gated on a success signal (win streak, high MMR, spend), the net flows uphill and widens the skill-to-rating gap the mechanic claims to close. The fix is to gate the protection on the DISTRESS signal it targets: grant the shield on a LOSS streak (bank after W consecutive losses), so the players catching cold runs are exactly the ones funded — turning a regressive buff into a progressive floor.

## Dedup
Distinct from the nearby game priors:
- **shop-reroll-ruin** (P099): optimal-stopping / accept-threshold economics — an interior optimal reroll bar with a per-reroll cost; a single-agent spend-lever value trap. No cohort-conditional / regressivity axis, no rating dynamics.
- **pity-anticipation-collapse** (P091): gacha *pity* — a hard/soft counter guaranteeing a drop after N misses; a single-player anticipation distortion, not a skill-conditional rating amplifier. This proposal is explicitly NOT a gacha-pity mechanic.
- **rubber-band-controller-instability** (P095): a discrete-time proportional (PID / rubber-band) catch-up controller with a stability boundary; a control-theory instability on a signed gap. This proposal is explicitly NOT a PID / rubber-band controller — it is a regressive-incidence claim on a discrete win-streak resource, measured by a paired-difference cohort contrast, with no feedback loop or stability boundary.
- This proposal is **competitive-rating incidence** — who captures the benefit of a win-streak-gated loss-protection resource — with a distinct lever (streak-banked shield), distinct mechanism (skill-monotone shield supply), and distinct math (paired-difference cohort uplift contrast, not an interior optimum, pity counter, or feedback controller).

## Model basis (declared model-dependence — the P024 discipline)
The regressive direction is robust to the specific constants but DOES depend on structural assumptions: (a) shields are earned on a WIN streak of length W ≥ 2 (so supply is monotone increasing in p); (b) both cohorts have enough losses that shield SUPPLY, not loss availability, is the binding constraint on uplift (holds whenever p is not so high that losses are scarce — at LOW_P/HIGH_P around 0.45/0.55 both cohorts lose ~90/110 games of 200); (c) a consumed shield is a fixed +2 rating swing (loss→win). If shields were instead granted on a loss streak, or W=1 (every win banks), or p were high enough that losses became the scarce resource, the incidence would change — the LOSS-streak trigger is the pre-registered fix precisely because it inverts assumption (a). The claim is scoped: under the (common) win-streak-gated loss-protection regime, the mechanic is regressive — demonstrated on the pinned constants, mechanism-explained (shield supply ∝ length-W win-run rate ∝ p), not asserted as a universal law.

## Probe report (v0, 2026-07-17)

**1. What is this really?** A regressive-incidence claim on a competitive-game "streak shield": a resource banked after W=3 true wins that negates the next loss (a +2 rating swing). Because length-W win-run frequency rises with per-game win probability p, the high-skill cohort (p=0.55) banks and spends more shields than the low-skill cohort (p=0.45), so the "anti-tilt protection" delivers a strictly larger mean rating uplift to the already-strong cohort.
**2. What would make it false?** If the high-skill cohort's mean uplift did NOT exceed the low-skill cohort's by ≥3σ (no regressivity), or if the low-skill cohort's mean uplift were ≤ 0 (the shield doesn't help them at all — a different, stronger claim than regressivity). Either → REJECT.
**3. Simplest version that still bites?** SEED=20260717, two cohorts of 10000 players × 200 iid Bernoulli games at p∈{0.45,0.55}, W=3; score each sequence with and without the shield on the same draws; contrast cohort mean uplifts.
**4. What is the counterintuitive core?** The resource that funds "protection for the weak" is manufactured by WINNING — a win-streak trigger gates the benefit on the exact skill that makes protection unnecessary, so the safety net flows uphill. A mechanic sold as a floor under the bottom of the ladder widens the skill-to-rating gap it claims to close.
**5. Where could I be fooling myself?** If losses were scarce (very high p) shield supply would stop being the binding constraint and the contrast could compress; at p=0.45/0.55 both cohorts have ~90–110 losses per 200 games, so supply binds and the gate σ sits far above 3 (153σ). The +2 swing assumes a symmetric win/loss rating unit; a different rating map would rescale magnitudes but not the regressive direction (shield supply is still skill-monotone). Paired scoring removes per-player outcome-luck variance, tightening the σ honestly rather than inflating it.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 regressive-amplification uplift_gap_sigma=153.46σ (high +35.31 vs low +21.64, gap +13.67); G2 both-positive/strict-ordering PASS (low +21.64 > 0, high > low) — clears the ≥3σ bar; exit 0; results-dict sha256 0294f757…022c09b4.
**7. What decision does it change?** Audit protection mechanics by cohort-conditional incidence, not average benefit; if the safety net is funded by a success signal (win streak / high MMR / spend) it is regressive by construction — gate it on the distress signal instead (grant the shield on a LOSS streak) to make the floor progressive.
**8. How will we know it worked?** The committed stdlib verifier reproduces the paired cohort-uplift contrast under SEED=20260717 with both gates holding (uplift_gap_sigma ≥ 3, both cohorts positive, high > low) and the results-dict sha256 matching 0294f757…022c09b4.

## One-line design fix
Grant the shield on a LOSS streak (bank after W consecutive losses), not a win streak — this funds the safety net from the cold-run distress signal it targets, making the protection progressive instead of regressive.

**Recommendation: sim-ready**
