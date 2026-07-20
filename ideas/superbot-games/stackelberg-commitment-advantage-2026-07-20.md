# PROPOSAL 215 — Stackelberg commitment / first-mover advantage: publicly committing to a quantity beats the simultaneous-move Nash payoff, and the value comes precisely from being *unable* to revise

> **State:** sim-ready
> **Class:** game theory / commitment & sequential-move equilibrium
> **Slot:** round-51 GAME
> **Anchor:** Stackelberg leadership model — the leader moves first and observably commits; the follower best-responds (subgame-perfect / backward induction)
> **Target:** sim-lab (VERDICT 228, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Stackelberg_competition@36004d1bfd7d09b149e3a78e4ea3f6bea0da4f06 · fetched 2026-07-20T14:00:40Z
> **Reference (external, reachable):** https://en.wikipedia.org/w/index.php?title=Stackelberg_competition&oldid=1365066831 — permalink (oldid 1365066831), raw-wikitext sha1 36004d1bfd7d09b149e3a78e4ea3f6bea0da4f06 (self-computed over 29228 raw bytes, full-40 match to the API revision sha1)
> **Verifier (firsthand):** `ideas/superbot-games/stackelberg_commitment_advantage.py` · results-dict sha256 `f6fdd85e2c22a1d49be9af6bd7479ab2e59869be818e1c451d1ca40caba6fb7b`
> 📊 Model: Claude Opus 4.8 · high · idea/planning

## The phenomenon (one line)

In a linear-demand quantity duopoly, a leader who **publicly and irrevocably commits** to an output before the rival chooses earns a payoff of `m²/8`, strictly more than the `m²/9` it gets in the simultaneous-move Cournot (Nash) equilibrium — a commitment advantage of exactly `m²/72 > 0` for every market size `m = A − C > 0`. The edge does not come from information or flexibility; it comes from *throwing flexibility away* in a way the rival can see.

## The folk belief

"Keeping your options open is worth something, and moving first only leaks your hand. In a symmetric game, going first can't help — the mover exposes its choice, the responder gets the last word, so at best the first mover ties the simultaneous outcome and probably does worse by revealing its plan." Committing before you must looks like a strict loss of optionality.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Inverse demand `P(Q) = A − Q`; two firms, symmetric constant marginal cost `C`, no fixed cost; write `m = A − C`. Firm profit is `q_i·(A − q_i − q_j − C)`.

- **Simultaneous (Cournot).** Each firm's best response to `q_j` is `(m − q_j)/2`. The symmetric fixed point is `q* = m/3`, giving each firm `π_cournot = m²/9`.
- **Sequential (Stackelberg).** The leader commits `q_L` first; the follower *observes it* and best-responds `q_F = (m − q_L)/2`. Substituting the follower's reaction into the leader's profit gives `q_L·(m − q_L)/2`, maximised at `q_L = m/2`, so `π_leader = m²/8`, `q_F = m/4`, `π_follower = m²/16`.

The leader's committed quantity `m/2` exceeds the Cournot quantity `m/3`. Under simultaneous play a firm *would like* to produce this much but cannot credibly, because its rival would then flood the market. Commitment makes the aggressive quantity credible: once `q_L = m/2` is on the table and cannot be undone, the follower's own best interest is to *pull back* to `m/4`, ceding share. The leader captures the residual. This is why the advantage is genuinely counterintuitive — the leader profits *because* it cannot revise. As the source page puts it, "once the leader has committed to an output ... it always wants to reduce its output ex-post. However its inability to do so is what allows it to receive higher profits than under Cournot." Optionality is negative value here; a credible hand-tie is positive value.

The magnitude is exact: `π_leader − π_cournot = m²/8 − m²/9 = m²/72 > 0` for all `m > 0`, so the direction (commitment beats simultaneous Nash) is world-independent, and the fractions never leave the rationals.

## The formal model (committed constants — sim-lab must reproduce exactly)

Pinned world `A = 12`, `C = 0` (so `m = 12`, and every optimum — `q_L = 6`, `q_F = 3`, `q_cournot = 4` — lands on an integer grid point). The **follower plays its EXACT (Fraction) backward-induction reaction** `q_F = (m − q_L)/2`; the **leader is enumerated EXHAUSTIVELY** over the integer quantity grid `0..GRID_MAX = 48`. (An integer-argmax follower is the wrong object: it lets the leader exploit the follower's rounding to reach a discretisation artefact of `21` at `q_L = 7`, which is not the Stackelberg value — the exact reaction is what makes the grid optimum equal the closed form.)

## Pinned world (committed constants)

- `SEED = 20260717`, `Z_GATE = 3.0`, `GRID_MAX = 48`, `N_DRAWS = 200000`.
- Boundedly-rational-follower deviation support `EPS_SUPPORT = (−2, −1, 0, 1, 2)` (uniform).
- Independent streams `random.Random(SEED + 11)` (G1) and `random.Random(SEED + 33)` (G3 scaled-world MC).
- Robustness worlds: scaled `A = 24, C = 0` (`m = 24`); cost-shifted `A = 15, C = 3` (`m = 12`).

## Pre-registered gates (APPROVE iff ALL hold, order G1 → G2 → G3 → G4; z_gate = 3.0)

Thresholds were pinned **after** a dry run, to values actually passed.

- **G1 — significance (Monte-Carlo, direction: mean > 0 AND z ≥ +3σ).** Against an ε-noisy follower who deviates uniformly by `{−2..+2}` units from its best response, the leader's realized commitment payoff still beats Cournot on average: `mean_gap = 1.99223` (≈ the exact advantage `m²/72 = 2`), `z_vs_0 = 105.045621 ≥ 3.0`. PASS.
- **G2 — exact (closed-form vs exhaustive enumeration, `fractions.Fraction`, direction: `==`, `==`, `==`, then `>`).** Exhaustive integer-grid leader enumeration with the exact follower reaction gives `leader_profit == 18 == 144/8`, `cournot_profit == 16 == 144/9`, `follower_profit == 9 == 144/16` — each an exact Fraction equality — and `leader (18) > cournot (16)` strictly. PASS.
- **G3 — robustness / shift (direction: `==` and `>` on shifted worlds, plus z ≥ +3σ MC).** Scaled world `m = 24`: enumeration `72/64/36` matches the closed forms exactly, `72 > 64`. Cost-shifted world `m = 12` via `A = 15, C = 3`: enumeration `18/16/9` matches exactly, `18 > 16` (profits depend only on `m`, not the demand/cost split). Scaled-world MC: `mean_gap = 7.94882` (≈ `m²/72 = 8`), `z_vs_0 = 209.424945 ≥ 3.0`. PASS.
- **G4 — falsifiability (a wrong accounting is REJECTED, direction: `wrong ≠ true`, and `wrong < cournot < true`).** The naive *static-follower* accounting — pricing the leader's commitment as if the follower ignored it and kept its Cournot quantity `4` — yields `wrong_static_leader_profit = 12`, which is `≠ true_leader_profit = 18` (rejected) and sits `< cournot = 16 < true = 18`. Ignoring the follower's reaction not only gets the number wrong, it flips the sign of the advantage. PASS.

## Pre-registered decision rule

APPROVE iff `all_pass == true` (G1 ∧ G2 ∧ G3 ∧ G4, evaluated in order) and the reproduced results-dict sha256 equals `f6fdd85e2c22a1d49be9af6bd7479ab2e59869be818e1c451d1ca40caba6fb7b` byte-for-byte. Any gate fail, or any digest mismatch, is a REJECT; `first_failing_gate` names the earliest failure.

## Dry-sim results (SEED=20260717, verbatim stdout of the verifier)

```json
{
  "all_pass": true,
  "closed_forms_pinned": {
    "advantage": [2, 1],
    "cournot": [16, 1],
    "follower": [9, 1],
    "leader": [18, 1],
    "m": 12
  },
  "enum_pinned": {
    "cournot_profit": [16, 1],
    "cournot_q": 4,
    "follower_profit": [9, 1],
    "follower_q": [3, 1],
    "leader_profit": [18, 1],
    "leader_q": 6,
    "n_symmetric_nash": 1
  },
  "eps_support": [-2, -1, 0, 1, 2],
  "first_failing_gate": null,
  "g1_significance": {
    "A": 12, "C": 0, "commit_qL": 6, "draws": 200000, "follower_br": 3,
    "m": 12, "mean_gap": 1.99223, "sd_gap": 8.481575, "seed": 20260728,
    "z_vs_0": 105.045621
  },
  "g2_exact": {
    "cournot_eq": true, "follower_eq": true, "leader_eq": true,
    "leader_gt_cournot": true
  },
  "g3_shift": {
    "cost_shift_world": {
      "A": 15, "C": 3,
      "closed": {"advantage": [2, 1], "cournot": [16, 1], "follower": [9, 1], "leader": [18, 1], "m": 12},
      "enum": {"cournot_profit": [16, 1], "cournot_q": 4, "follower_profit": [9, 1], "follower_q": [3, 1], "leader_profit": [18, 1], "leader_q": 6, "n_symmetric_nash": 1},
      "exact": true
    },
    "mc_scaled": {
      "A": 24, "C": 0, "commit_qL": 12, "draws": 200000, "follower_br": 6,
      "m": 24, "mean_gap": 7.94882, "sd_gap": 16.974197, "seed": 20260750,
      "z_vs_0": 209.424945
    },
    "scaled_world": {
      "A": 24, "C": 0,
      "closed": {"advantage": [8, 1], "cournot": [64, 1], "follower": [36, 1], "leader": [72, 1], "m": 24},
      "enum": {"cournot_profit": [64, 1], "cournot_q": 8, "follower_profit": [36, 1], "follower_q": [6, 1], "leader_profit": [72, 1], "leader_q": 12, "n_symmetric_nash": 1},
      "exact": true
    }
  },
  "g4_falsifiability": {
    "commit_qL": 6, "cournot_profit": [16, 1], "static_follower_q": 4,
    "true_gt_cournot": true, "true_leader_profit": [18, 1],
    "wrong_lt_cournot": true, "wrong_rejected_neq_true": true,
    "wrong_static_leader_profit": [12, 1]
  },
  "gates": {
    "G1_significance": true,
    "G2_exact_enumeration": true,
    "G3_robustness_shift": true,
    "G4_falsifiability": true
  },
  "grid_max": 48,
  "head": "In a linear-demand quantity duopoly the leader who PUBLICLY COMMITS to an output earns strictly more than in the simultaneous Cournot equilibrium (pi_leader=m^2/8 > pi_cournot=m^2/9, advantage m^2/72>0): G1 the advantage survives a noisy follower at >=3 sigma; G2 exhaustive integer-grid enumeration matches the closed forms EXACTLY (Fraction) with leader>cournot; G3 it holds under scaled and cost-shifted worlds; G4 the static-follower accounting that ignores the reaction is correctly rejected (and would flip the sign).",
  "pinned_world": {"A": 12, "C": 0, "m": 12},
  "proposal": 215,
  "seed": 20260717,
  "slot": "round-51 GAME",
  "z_gate": 3.0
}
```

```
G1_significance: PASS
G2_exact_enumeration: PASS
G3_robustness_shift: PASS
G4_falsifiability: PASS
all_pass: True
results_sha256: f6fdd85e2c22a1d49be9af6bd7479ab2e59869be818e1c451d1ca40caba6fb7b
```

## Verifier

`ideas/superbot-games/stackelberg_commitment_advantage.py` — stdlib only (`hashlib`, `json`, `math`, `random`, `sys`, `fractions`). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the results dict carries no digest field; `main()` runs `build_results()` twice in-process, asserts byte-identical compact-canonical (`sort_keys=True, separators=(",",":")`) serializations, prints the pretty (`indent=2, sort_keys=True`) dump, then `results_sha256: <hex>` over the compact-canonical form. Nothing is written to disk; a second, separate process reproduces the identical dict and digest.

## Reproduce

```
python3 ideas/superbot-games/stackelberg_commitment_advantage.py
```
Expect `"all_pass": true`, `"first_failing_gate": null`, and `results_sha256: f6fdd85e2c22a1d49be9af6bd7479ab2e59869be818e1c451d1ca40caba6fb7b` on every invocation (in-process double-run and separate-process runs are byte-identical).

## Why it matters

Every mechanic in which one side moves observably first — a capacity/pricing pre-announcement, an escalating-cost commitment, an opening bid a bot cannot retract, a raid boss whose spawn parameters are published before players queue — carries this lever. A designer who treats "moving first = leaking information = disadvantage" will misprice the first-mover slot; in a Stackelberg-shaped interaction the first mover should *want* to commit hard and publicly, and the correct balance question is how much residual to leave the follower (here exactly half the leader's quantity), not whether commitment helps. For a bot, the actionable rule is: when your move is observable and irrevocable, deliberately over-commit toward the monopoly-leaning quantity `m/2` rather than the Cournot quantity `m/3` — the rival's rational retreat pays for it.

## Dedup (contrast vs prior lane heads)

A grep across ALL lanes in `ideas/` returns zero shipped `stackelberg`, `leader-follower`, `commitment advantage`, or `risk-dominance` heads. The nearby `first-mover` / `commit first` hits are the **opposite** head and are deliberately contrasted here:

- **penney-game-second-mover-advantage / Penney's game:** an intransitive sequence-choice game where the reply map sends every pattern to a beating pattern, so committing first is a **losing** role and "make the other player commit first" is optimal. Stackelberg is the inverse — the mover commits a *quantity* (not a pattern in an intransitive tournament), and committing first is a **winning** role via the follower's smooth best-response.
- **intransitive-efron-dice:** the 2:1 second-mover edge is a sequential-commitment fact of an intransitive die cycle; again committing first *loses*. The Stackelberg mechanism has no intransitivity — the follower's reaction is a single-valued monotone function `(m − q_L)/2`, and the leader profits from the reaction, not from any cycle.
- **pie-rule-opening-trap:** the swap rule makes the *strongest opening* the worst move via the fold `min(f, 1−f)`; that is a side-selection incentive, not a quantity-commitment one, and it *shrinks* the first-mover edge to a coin flip. Here the first-mover edge is real and strictly positive.

The head — first-mover/commitment is a strict **advantage** in a smooth sequential game — is thus a clean complement to the lane's existing "committing first loses" family, not a duplicate.

## Model basis (declared model-dependence)

The head is a deterministic identity of the Stackelberg subgame-perfect equilibrium under linear demand and constant symmetric marginal cost: `π_leader = m²/8`, `π_cournot = m²/9`, advantage `m²/72`. It assumes (a) the follower observes the leader's commitment and best-responds (the standard perfect-information Stackelberg assumption; the source page notes that without observation the game "reduces to Cournot"), (b) the commitment is credible/irrevocable, and (c) linear demand with a single marginal-cost parameter. The direction (leader > Cournot) is world-independent for any `m > 0`; the specific magnitudes track the pinned constants, and G3 confirms invariance to scaling and to the demand/cost split.

## Gate power + margin ledger

| Gate | Statistic | Measured | Null / target | Result | Margin |
|------|-----------|----------|---------------|--------|--------|
| G1 | mean commitment−Cournot gap (noisy follower) vs 0 | 1.99223 | 0 | z = 105.045621 | ~35× z_gate |
| G2 | enum leader/cournot/follower vs closed form | 18 / 16 / 9 | 144/8, 144/9, 144/16 | exact `==`, leader > cournot | exact (Fraction) |
| G3 | scaled + cost-shift exact match; scaled MC gap vs 0 | 72/64/36; 18/16/9; 7.94882 | closed forms; 0 | exact `==`; z = 209.424945 | exact; ~70× z_gate |
| G4 | static-follower accounting vs true | 12 | ≠ 18, and < 16 < 18 | rejected, sign flipped | qualitative |

## Probe report (v0, self-adversarial)

**1. Is `π_leader = m²/8 > π_cournot = m²/9` the genuine Stackelberg value, not an artefact of the grid?** Yes. The follower plays its EXACT (Fraction) reaction `(m−q_L)/2`; the leader is enumerated over the integer grid, and because the continuous optimum `q_L = m/2` is on-grid, the grid maximum equals the closed form `m²/8` exactly (G2). An integer-argmax follower would instead let the leader exploit rounding (profit 21 at `q_L=7`) — that discretisation artefact is explicitly avoided, and the doc's formal-model section flags it.

**2. Does the advantage depend on the specific world `A=12, C=0`?** No. G3 re-runs on a scaled world (`m=24`: 72 vs 64) and a cost-shifted world (`A=15, C=3`, same `m=12`: 18 vs 16), both exact, showing profits depend only on `m = A−C` and the direction holds for any `m>0` (`advantage = m²/72`).

**3. Is the significance gate meaningful or a trivially-positive quantity?** Meaningful: G1's per-draw gap can be strongly negative (a follower deviating `+2` hands the leader a worse outcome than Cournot in that draw), yet the mean is positive at 105σ — the advantage survives a boundedly-rational follower on average, not just at the exact optimum.

**4. Does the grounding source document the specific head?** Yes, firsthand. The Wikipedia "Stackelberg competition" page (rev 1365066831) documents the leader-follower SPNE, backward induction, "its inability to [revise] is what allows it to receive higher profits than under Cournot," a worked linear-demand example (leader profit 2,000,000 vs Cournot `(16/9)·10⁶ ≈ 1.78M` apiece — the exact `m²/8` vs `m²/9` comparison for `m=4000`), and "first-mover advantage" / "credible commitment is a tool for competition." Pinned at raw-wikitext sha1 `36004d1b…` (self-computed, full-40 match to the API revision sha1), oldid 1365066831.

**5. What does the verifier prove that the page does not?** The page gives the continuous-calculus SPNE and a single worked example. The exhaustive integer-grid enumeration, the exact-`Fraction` equality check of the general closed forms `m²/8, m²/9, m²/16`, the ε-noisy-follower significance test, the two-world robustness sweep, and the static-follower falsifiability rejection are the verifier's OWN firsthand computations — accurately scoped in the grounding caveat, not attributed to the page.

**6. Is the falsifiability leg a real test?** Yes. G4 constructs a concrete WRONG accounting (follower ignores the commitment, keeps its Cournot quantity) and shows it yields 12 ≠ the true 18 and even lands below Cournot (12 < 16 < 18) — so mis-modelling the follower's reaction not only errs but reverses the conclusion. A verdict that reproduced only the wrong model would (correctly) reject the head.

**7. Is `all_pass` gameable by a single degenerate parameter?** No. The four gates test four distinct directions (a stochastic mean > 0 at ≥3σ; an exact rational `==` plus strict `>`; robustness across two different worlds; and a directional `≠` rejection). No single degenerate setting satisfies all four; a verdict session reproduces the exact 64-hex digest to confirm every constant.

**8. How will a verdict session know it reproduced the head?** It re-runs the stdlib verifier under `SEED=20260717` and confirms `all_pass=true`, `first_failing_gate=null`, and results-dict sha256 `f6fdd85e2c22a1d49be9af6bd7479ab2e59869be818e1c451d1ca40caba6fb7b` byte-for-byte (in-process double-run and a separate-process run are byte-identical); any gate fail or digest mismatch is a REJECT.

## One-line design fix

When a mechanic lets one side move observably and irrevocably first, price that slot as a strict advantage and let the mover over-commit toward `m/2` (not the Cournot `m/3`) — in a Stackelberg-shaped interaction the rival's rational retreat pays for the commitment, so `π_leader = m²/8 > π_cournot = m²/9`.

**Recommendation: sim-ready**
