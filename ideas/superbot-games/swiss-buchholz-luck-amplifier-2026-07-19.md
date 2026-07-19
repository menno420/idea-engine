# PROPOSAL 179 — Swiss-system Buchholz tiebreak is a luck amplifier (round-42 GAME slot, P179 → V192, +13)

> **State:** sim-ready
> **Class:** superbot-games · tournament-scoring / tiebreak-fairness · strength-of-schedule luck-vs-skill decomposition
> **Slot:** round-42 GAME
> **Target:** sim-lab (VERDICT 192, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning

## Head (one line)

Among players finishing tied on match points in a Swiss-system tournament, the Buchholz strength-of-schedule tiebreak ranks the luckier opponent draw ahead of the stronger player: it reflects the tied players' own TRUE skill only weakly (p_skill ≈ 0.60) but their opponent-draw luck strongly (p_luck ≈ 0.80) — a ≈3× luck-to-skill signal ratio at an even field. Buchholz measures whom you happened to play, not how good you are.

## The folk belief

Organizers treat Buchholz ("strength of schedule") as a MERIT tiebreak: two players on the same match points are separated by summing their opponents' scores, on the theory that the player who beat the harder field earned the same points against tougher competition and is therefore the better player. The intuition is that a higher Buchholz signals a stronger player. The claim here is that among equal-score players Buchholz is set far more by the luck of WHICH opponents the pairing engine happened to hand you than by your own skill — so it ranks the luckier draw ahead of the stronger player far more often than intuition allows.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Model an N-player, R-round Swiss tournament with Elo-logistic match outcomes and standard rematch-avoiding score-group pairing. Each player i carries a hidden TRUE skill θ_i ~ Gaussian(1500, σ). Round by round players are ranked by current points (ties broken by a pinned RNG), then greedily paired top-down against the nearest not-yet-played opponent; a win probability of 1/(1 + 10^((θ_b − θ_a)/400)) decides each game (win/loss only, no draws). After R rounds:

- **Buchholz(i)** = Σ points of i's opponents (the shipped strength-of-schedule statistic).
- **luck(i)** = Σ TRUE skill θ of i's opponents (how strong a field the pairing engine actually handed i).
- **skill(i)** = i's own TRUE skill θ_i.

Then form every unordered pair of players finishing on EQUAL match points — the tied cohort Buchholz is meant to arbitrate. For each such pair (a, b) with distinct Buchholz, distinct own-skill, and distinct opponent-luck, the Buchholz-winner is whoever has the higher Buchholz. Record two indicators:

- **skill_agree** — the Buchholz-winner is also the higher-TRUE-skill player of the pair.
- **luck_agree** — the Buchholz-winner is also the player who drew the higher summed opponent TRUE skill (the luckier/tougher draw).

p_skill and p_luck are the means of these indicators over all tied pairs. If Buchholz were a clean merit tiebreak p_skill would be high and p_luck near a coin flip; the head is that the reverse holds — p_luck is high and p_skill only weakly above 0.5 — because within a tied cohort the players have, by construction, nearly the same record, so the dominant thing separating their Buchholz totals is the exogenous luck of opponent assignment, not the small residual skill gap.

## GROUNDING (verified live)

GROUNDING: https://en.wikipedia.org/wiki/Swiss-system_tournament@1357112228

Note: quoting the article verbatim — "If players remain tied, a tie-break score is used, such as the sum of all opponents' scores (Buchholz system)." This documents that Buchholz is the SUM of a player's opponents' scores, i.e. a strength-of-schedule tiebreak — exactly the statistic this head decomposes into luck vs. skill. Fetched live HTTP 200 at revision 1357112228, verified 2026-07-19. (The companion article "Tie-breaking in Swiss-system tournaments" @1346952931, also live 2026-07-19, states the same strength-of-schedule idea: "the player that played the harder competition to achieve the same number of points should be ranked higher.")

## Checkable gate criteria (measured, SEED=20260717)

Verifier: `ideas/superbot-games/swiss_buchholz_luck_amplifier.py` — stdlib only (`math`, `json`, `hashlib`, `random`). SEED=20260717 pinned; Z_GATE=3.0; in-process double-run asserted identical before hashing; WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture (results dict carries no digest field). Results-dict sha256 `0e591bb44f57f72fdff6536417a3ba009b74dfb9c07f2c41073bdbd9876c0fa8`. all_pass = **true**.

**Base field** — N=64, R=7, σ=200, 1200 tournaments, **442632** tied-cohort pairs: p_luck **0.804910**, p_skill **0.597399**, z_luck **511.920239**, z_diff (paired luck−skill) **234.751939**, ratio |p_luck−0.5|/|p_skill−0.5| **3.130521**, mean_d **0.207511**.

**Shifted field** — N=128, R=9, σ=350, 400 tournaments, **548135** tied-cohort pairs: p_luck **0.870756**, p_skill **0.686809**, z_luck **818.237315**, z_diff **265.698695**, ratio **1.984682**, mean_d **0.183947**.

Gate thresholds (APPROVE iff all hold, G1 → G2 → G3):

- **G1 — luck dominates (head):** p_luck ≥ 0.70 AND z_luck ≥ 3.0. Measured base p_luck 0.804910, z_luck 511.92 → **PASS**.
- **G2 — luck beats skill:** base ratio ≥ 3.0 AND z_diff ≥ 3.0 AND (p_luck − p_skill) ≥ 0.15. Measured ratio 3.130521, z_diff 234.75, gap 0.207511 → **PASS**.
- **G3 — robustness (shifted distribution):** under wider σ and larger bracket the dominance persists — shift p_luck ≥ 0.70 AND z_diff ≥ 3.0 AND (p_luck − p_skill) ≥ 0.10. Measured shift p_luck 0.870756, z_diff 265.70, gap 0.183947 → **PASS**.

## Probe report

**1. Is the result an artifact of the specific rematch-avoidance pairing rule?** The greedy nearest-not-yet-played pairing is the standard Swiss shape; rematch-avoidance is what INJECTS opponent-draw variance into a tied cohort (it forces different players onto different opponents), so it is the mechanism, not a confound. A no-rematch-avoidance variant would only make the draw more idiosyncratic; sensitivity to the exact greedy vs. optimal (blossom) pairing is a named out-of-scope refinement, not a threat to the sign.

**2. Does the win/loss-only (no-draw) simplification bias the head?** Chess Buchholz sees draws worth ½; this model is win/loss only. Draws would compress score spread and grow tied cohorts — enlarging, not shrinking, the population Buchholz must arbitrate — so the no-draw model is if anything conservative on cohort size. The head is about the luck-vs-skill composition of the tiebreak, which draws do not reverse; a ½-point-draw replication is a disclosed robustness follow-up.

**3. Would median/cut Buchholz variants (Median-Harkness, Modified Median) kill the effect?** Discarding the highest/lowest opponent scores trims tail variance but still sums opponents' scores — it remains a strength-of-schedule statistic driven by WHICH opponents you drew. The head targets raw/Solkoff Buchholz (sum, no cut); the cut variants are expected to attenuate but not remove the luck dominance, and are named as an out-of-scope robustness axis.

**4. Does p_skill > 0.5 mean skill genuinely leaks into Buchholz?** Yes, and we disclose it: p_skill ≈ 0.60 (base) / 0.69 (shift) is meaningfully above a coin flip — a stronger player does tend to have beaten tougher opponents, so some skill signal is real. The head is NOT "zero skill signal"; it is that opponent-draw luck is the DOMINANT signal (≈3× at an even field), so Buchholz systematically ranks the luckier draw ahead of the stronger player far more often than a merit tiebreak should.

**5. Why does the luck/skill ratio COMPRESS under wider σ (base 3.13 → shift 1.98)?** With a wider TRUE-skill spread, the residual own-skill gap between two tied players is larger and more legible, so Buchholz picks it up more often (p_skill rises 0.60 → 0.69) and the ratio shrinks. This is honest and expected — it is exactly why G3 gates the DOMINANCE (p_luck ≥ 0.70, z_diff, gap), not the ratio. The systematic luck-over-skill dominance is what proves robust; the ratio is a base-field descriptor.

**6. Does the model align with real FIDE / tabletop Buchholz tiebreaks?** FIDE and most tabletop organizers use exactly "sum of opponents' scores" (grounded above) as a primary or secondary tiebreak among equal-score players — the precise setting modeled. Real fields add draws, byes, forfeits, and floats; those are named refinements. The structural claim (a strength-of-schedule sum among near-identical records is luck-dominated) does not depend on them.

**7. How sensitive is the head to the number of rounds R?** More rounds sharpen the standings and shrink tied cohorts but do not change the composition of the tiebreak WITHIN a cohort; the shifted field (R 7 → 9) already tests a longer tournament and the dominance strengthens (p_luck 0.80 → 0.87). Very short tournaments (R ≪ log2 N) would give huge tied cohorts and even more luck-dominated Buchholz — the same direction.

**8. Determinism and reproduction?** SEED=20260717 pinned; `compute()` run twice in-process and asserted equal before hashing; two cross-invocation runs printed byte-identical stdout with results-dict sha256 `0e591bb44f57f72fdff6536417a3ba009b74dfb9c07f2c41073bdbd9876c0fa8`; all dict floats round()-ed to 6 dp, sort_keys canonical — no set/dict-ordering nondeterminism.

## Honest caveats / crossovers

- **(a) The luck/skill RATIO compresses under a wider skill spread** — base 3.130521 → shift 1.984682 — because a larger σ makes each tied pair's own-skill gap more legible, so p_skill climbs (0.597 → 0.687) and the ratio falls. This is disclosed, not hidden: the ROBUST quantity is the dominance (p_luck ≥ 0.70, the paired-difference z_diff, and the p_luck − p_skill gap), which G3 gates directly; the ratio is a base-field descriptor, not a robustness claim.
- **(b) Win/loss (no-draw) simplification** — real chess Buchholz counts draws at ½ and handles byes/forfeits/floats; the model is win/loss only. This changes cohort sizes and score granularity but not the luck-vs-skill composition the head measures; draw-aware and cut-variant (Median/Modified-Median) replications are named out-of-scope robustness follow-ups.
- **(c) Dedup search (game lane + fleet).** The game lane already ships pity/gacha timers, MMR/Elo rating deflation, drop-rate/loot median gaps, and the pie-rule first-move head; the fleet ships tournament-seeding-bracket-optimality (single-elimination bracket/seeding luck) and the secretary-rule head. The Buchholz Swiss-TIEBREAK statistic has no prior head: it is a within-Swiss strength-of-schedule luck-vs-skill decomposition among EQUAL-score players, distinct from single-elim seeding/bracket order-statistics (different tournament format, different luck channel — opponent-assignment among the already-tied, not bracket placement) and distinct from the rating-dynamics and payout-distribution heads (no rating fixed point, no heavy tail here).

**Recommendation: sim-ready**
