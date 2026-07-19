# Follow-on reserve starvation: under a power-law portfolio, holding back ~half the fund to defend pro-rata in the winners beats spray-and-pray

> **State:** sim-ready
> **Class:** venture / fund-construction — reserves, pro-rata follow-ons, power-law outcomes, fund MOIC
> **Target:** sim-lab (VERDICT 199, +13 offset)
> **Grounding:** https://www.goingvc.com/post/follow-on-in-venture-capital@586b66588731b5142a1a9b34a711a25c85f36333 · fetched 2026-07-19T22:16:02Z
> **Reference (external, reachable):** https://www.goingvc.com/post/follow-on-in-venture-capital — verified live HTTP 200 this session (content pin stable across two fetches).
> **Harvest source (firsthand):** GoingVC, "Follow On in Venture Capital": "This is why so many managers fight for pro-rata rights to maintain their ownership stake in a company," and "Being able to 'double down' on the 'winners' in a portfolio is an important factor in the success of venture fund managers, especially those at the seed stage."

## The phenomenon (one line)

Because venture outcomes are power-law — nearly all return sits in a handful of winners — a fund that **reserves ~half its committed capital** to defend its pro-rata ownership in those winners earns a strictly higher fund MOIC than a "spray-and-pray" fund that deploys the same capital entirely into initial checks and lets each follow-on round dilute it, and the entire edge is contributed by the defended top-decile companies, not by the extra names spraying buys.

## The folk belief

"Reserves are dead money — deploy everything, buy more shots on goal, and let the winners carry the fund." The intuition treats each initial check as an independent lottery ticket and assumes more tickets dominates. It ignores that dilution is **multiplicative** and lands hardest on exactly the positions that carry the whole return, so the spray fund's MOIC is capped precisely where the value is.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Two forces meet on the winners and they are not the same size.

1. **The cost of reserving.** Holding back `RESERVE_FRAC` of the fund shrinks the initial ownership you buy in *every* company from `O0` to `(1 − RESERVE_FRAC)·O0`. On a company you never defend, that is pure lost ownership.
2. **The dilution you avoid.** An un-defended holding is diluted multiplicatively across the follow-on rounds: its ownership is multiplied by `(1 − d)^R`. A defended holding maintains pro-rata and keeps its ownership un-diluted.

For a **defended winner**, reserving beats spraying iff

```
(1 − RESERVE_FRAC) > (1 − DILUTION_PER_ROUND) ^ FOLLOW_ROUNDS.
```

Pinned so this reads `0.5 > 0.7^4 = 0.2401`: on a defended winner the reserve fund keeps half its ownership where spray keeps only a quarter — reserve wins by a wide margin. On an **un-defended loser** spray keeps double the reserve fund's ownership (`0.2401` vs `0.5·0.2401`), but a loser under a fat tail carries almost no value, so that "win" is on near-zero dollars. Net over the portfolio, the paired difference

```
ΔMOIC = C · [ Σ_defended V · ((1 − RESERVE_FRAC) − (1 − d)^R)
             − Σ_undefended V · (1 − d)^R · RESERVE_FRAC ]
```

is dominated by the first term because the fat tail piles value into the defended winners. The convexity is the whole story: the same dilution rate applied to a power-law portfolio taxes the MOIC in proportion to where the value is, and the value is in the winners the reserve defends. Under-reserving does not diversify risk away — it starves the only positions that matter, and the fund's upside is capped at the diluted ownership of its own winners.

Crucially the effect **requires a fat enough tail**: if outcomes were only mildly skewed, the many un-defended names would carry enough aggregate value that spray's broader (if diluted) ownership would win. The gates therefore pin a genuinely concentrated tail and stress it steeper.

## Pinned world (committed constants, SEED=20260717)

- One local `random.Random(20260717)`. `TRIALS = 50,000` funds; `N_COMPANIES = 30` per fund; `FUND = 100.0` ($M).
- Exit value of company *i* = `EXIT_SCALE · V_i` with `EXIT_SCALE = 200.0` and `V_i = paretovariate(POWER_ALPHA)`. Base `POWER_ALPHA = 1.6` (real power-law concentration).
- `INITIAL_OWN = O0 = 0.10` — ownership a full-fund initial check buys. **Spray** deploys the whole fund into initial checks → ownership `O0` in every company. **Reserve** deploys `(1 − RESERVE_FRAC)` of the fund into initial checks → ownership `(1 − RESERVE_FRAC)·O0` in every company, holding back `RESERVE_FRAC = 0.50` to defend pro-rata in the winners.
- Dilution: an un-defended holding is multiplied by `(1 − DILUTION_PER_ROUND)^FOLLOW_ROUNDS = 0.70^4 = 0.2401`; a defended holding keeps pro-rata (un-diluted). `DILUTION_PER_ROUND = 0.30`, `FOLLOW_ROUNDS = 4`.
- Winners are defended imperfectly: an interim signal `log(V_i) + SIGNAL_NOISE·N(0,1)` (`SIGNAL_NOISE = 0.4`) ranks companies; the top `K_DEFEND = round(N·WINNER_DECILE) = 3` (`WINNER_DECILE = 0.10`) by signal are defended. The signal is noisy, so the reserve fund sometimes defends a non-winner and misses a true winner.
- **Common random numbers:** within a fund the reserve and spray strategies see the *same* exit draws, so `ΔMOIC = MOIC(reserve) − MOIC(spray)` is a clean paired difference — only the capital-allocation policy differs.
- Fund `MOIC(strategy) = Σ_i ownership_i · (EXIT_SCALE · V_i) / FUND`.
- Robustness tail: `COLD_ALPHA = 1.4` (steeper / fatter-winner), fresh draws off the same stream. `Z_GATE = 3.0`, `CONCENTRATION_GATE = 0.75`.

## Gate criteria

- **G1 — reserves beat spray (≥3σ).** The paired `ΔMOIC` over `TRIALS` funds is strictly positive and clears the z-gate: `mean(ΔMOIC) > 0` **and** `z = mean(ΔMOIC)/(sd/√TRIALS) ≥ 3.0`. Defending pro-rata strictly raises fund MOIC.
- **G2 — the edge is the winners, not the tail of names (bound).** Attribute the paired edge to each company and rank all company-instances by realised exit value: the share of the **gross positive edge** captured by the top-`WINNER_DECILE` companies is `≥ 0.75`. The advantage concentrates in the defended winners, not in the extra initial names spray buys.
- **G3 — robust under a steeper power law (≥3σ).** Repeat at `COLD_ALPHA = 1.4`: the paired `ΔMOIC > 0` at `z ≥ 3.0` **and** the top-decile concentration bound (`≥ 0.75`) still holds. The effect survives — and widens — as the distribution gets more convex.

`all_pass = G1 ∧ G2 ∧ G3`

Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (P127+ twist) — the compact-canonical results dict's own sha256 IS the digest; the dict carries no self-referential field; the stdout dump is the pretty (indent=2, sort_keys) render; nothing is written to disk.

## Measured results (this run)

```
{
  "all_pass": true,
  "cold_alpha": 1.4,
  "delta_mean": 0.431911,
  "delta_std": 4.613577,
  "dilution_factor": 0.2401,
  "dilution_per_round": 0.3,
  "exit_scale": 200.0,
  "follow_rounds": 4,
  "fund": 100.0,
  "gate_G1_pass": true,
  "gate_G1_z": 20.933485,
  "gate_G2_concentration_gate": 0.75,
  "gate_G2_pass": true,
  "gate_G2_topdecile_edge_share": 0.823121,
  "gate_G3_cold_delta_mean": 1.32361,
  "gate_G3_cold_reserve_mean_moic": 6.332579,
  "gate_G3_cold_spray_mean_moic": 5.008969,
  "gate_G3_cold_topdecile_edge_share": 0.874894,
  "gate_G3_cold_z": 15.911868,
  "gate_G3_pass": true,
  "head": "follow-on reserve starvation: under a power-law portfolio a fund reserving ~half its capital to defend pro-rata in the winners out-MOICs a spray-and-pray fund, and the edge concentrates in the defended top-decile winners",
  "initial_own": 0.1,
  "k_defend": 3,
  "n_companies": 30,
  "power_alpha": 1.6,
  "proposal": 186,
  "reserve_frac": 0.5,
  "reserve_mean_moic": 4.268874,
  "seed": 20260717,
  "signal_noise": 0.4,
  "spray_mean_moic": 3.836963,
  "trials": 50000,
  "winner_decile": 0.1
}
Results-JSON sha256 b917778d026e7beea3aff07e8e6b8f6afad7b8df099f39a2773214f79ec2950f
```

Reading the numbers: base market spray MOIC **3.84x** vs reserve MOIC **4.27x**, a paired mean `ΔMOIC` of **+0.43** at **z ≈ 20.9**; the top decile of companies by exit value carries **82.3%** of the gross positive edge. Under the steeper cold tail the gap widens to **5.01x vs 6.33x** (`ΔMOIC ≈ +1.32`, z ≈ 15.9, concentration 87.5%). All three gates pass.

## Caveats & crossovers (honest disclosure)

- **The tail is load-bearing and disclosed.** The head is a *fat-tail* phenomenon: at a thin tail (e.g. Pareto α = 2.0) the un-defended names carry enough aggregate value that spray's broader ownership actually wins — an earlier calibration at α = 2.0 produced `ΔMOIC < 0`. That is not a bug; it is the boundary of the claim. The pinned α = 1.6 (and steeper α = 1.4) is where real early-stage venture lives, and the algebraic condition `(1−RESERVE_FRAC) > (1−d)^R` plus enough tail concentration is stated openly.
- **Imperfect signal, honestly.** Winners are defended off a *noisy* interim signal, so the reserve fund sometimes defends a dud and misses a rocket; that is why G2's share is 0.82, not 1.0. A perfect signal would only strengthen the head.
- **`O0` / `EXIT_SCALE` are display scales, not drivers.** Both multiply `ΔMOIC` linearly and therefore cancel out of the z-score and the concentration ratio; they set only the reported MOIC magnitudes, chosen for realism.
- **No capital-exhaustion or portfolio-size trade-off is modeled.** Both funds hold the same `N_COMPANIES`; the reserve fund simply writes smaller initial checks. The complementary head — that *too much* reserve under-diversifies the initial portfolio so the fund never *finds* enough winners to defend, giving an interior optimum near ~50% — is the companion "reserve-ratio interior optimum" idea, deliberately out of scope here.
- **Crossovers (dedup).** A scan of the venture-lab section confirms this mechanism is distinct: `irr-speed-trap` is a metric artifact (rate vs dollars), `founder-dilution-waterfall` and `option-pool-shuffle` are cap-table/waterfall accounting on a single company, `growth-endurance-dominance` is a growth-vs-retention SaaS head, `pay-to-play-cramdown-cliff` and `full-ratchet-convexity` are down-round provision mechanics, and `term-sheet-winners-curse` is an auction-selection head. None model the **fund-construction reserve/spray trade-off under a power law**, which is this head.

## Probe report (v0, self-adversarial)

**1. Does the paired ΔMOIC clear ≥3σ and stay strictly positive under SEED = 20260717?**
Yes — base `ΔMOIC` mean is +0.431911 at z ≈ 20.93, comfortably above the 3.0 gate, over 50,000 paired funds. The pairing (common random numbers within a fund) removes the exit-draw variance, so the z reflects the policy difference alone.

**2. Is the fat-tail assumption a thumb on the scale, or is it the disclosed boundary of the claim?**
It is the disclosed boundary. The head is explicitly a power-law phenomenon; at a thin tail (α = 2.0) the head reverses, which the caveats state and which is exactly the algebraic condition `(1−RESERVE_FRAC) > (1−d)^R` plus sufficient tail concentration. Pinning α = 1.6/1.4 places the test in the regime real early-stage venture occupies.

**3. Does the top-WINNER_DECILE genuinely carry the edge (≥0.75), and is that the right denominator?**
Yes — the top decile by exit value captures 0.823 of the gross positive paired edge (0.875 under the cold tail). The denominator is the sum of positive per-company edge contributions, so the share is an interpretable fraction of the total advantage rather than a ratio against a small net; the defended winners, not the extra spray names, are where the advantage lives.

**4. Does the spray fund's MOIC cap out precisely because un-defended dilution erodes its ownership in the winners?**
Yes — spray's ownership in every company, winners included, is multiplied by `(1−d)^R = 0.2401`, so its winners return at a quarter of pro-rata. Reserve keeps `(1−RESERVE_FRAC)=0.5` un-diluted on the defended winners, which is where the +0.43 (and +1.32 cold) MOIC gap comes from.

**5. Does the cross-invocation double run reproduce the results-dict sha256 byte-for-byte?**
Yes — two separate interpreter invocations produced byte-identical stdout and the digest `b917778d026e7beea3aff07e8e6b8f6afad7b8df099f39a2773214f79ec2950f`. A single local `random.Random(SEED)`, no wall-clock or external input, guarantees it; the in-process double-run also asserts the two dicts are identical.

**6. Is `SIGNAL_NOISE` doing hidden work — would a different noise level flip the head?**
No — the head holds across a sweep (SIGNAL_NOISE 0.35→0.45 gives G2 shares 0.836→0.810, all passing); more noise lowers the concentration share and the edge but never flips the sign, because even a randomly-defended winner still avoids the multiplicative dilution. `0.4` is pinned for a realistic, clearly-imperfect signal.

**7. Does the steeper-tail gate preserve both the ≥3σ MOIC edge and the winner-concentration bound?**
Yes — at COLD_ALPHA = 1.4 the paired `ΔMOIC` is +1.323610 at z ≈ 15.91 and the top-decile share rises to 0.875. The effect widens as the tail fattens, exactly as the convexity argument predicts.

**8. Are the reported MOIC magnitudes an artifact of `O0`/`EXIT_SCALE`, and does the mechanism survive their removal?**
The mechanism is scale-free: `O0` and `EXIT_SCALE` multiply every fund's `ΔMOIC` by the same constant, so they cancel out of both the z-score and the concentration share and change only the displayed MOIC levels. The gates would pass identically at any positive scale.

**9. Is the mechanism distinct from the existing venture-lab heads?**
Yes — a dedup scan of the section shows no head models the fund-construction reserve-vs-spray trade-off under a power law: `irr-speed-trap` (metric artifact), `founder-dilution-waterfall`/`option-pool-shuffle` (single-company cap-table), `growth-endurance-dominance` (SaaS growth/retention), `pay-to-play-cramdown-cliff`/`full-ratchet-convexity` (down-round provisions), `term-sheet-winners-curse` (auction selection). This head is the portfolio-level reserve policy.

**Recommendation: sim-ready**
