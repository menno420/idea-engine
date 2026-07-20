# Grim trigger / folk theorem: the exact grim-trigger cooperation threshold δ* = (T−R)/(T−P)

> **State:** sim-ready
> **Status:** `sim-ready` — PROPOSAL 223 (round-53 GAME slot) → VERDICT 236 (+13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Grim_trigger&oldid=1292515670@beb2798d4ee3752cda422e6192a02e0ca3ea7926 · fetched 2026-07-20T17:40:53Z
>
> Verifier (merged firsthand in sim-lab): `sims/verdict-236-grim-trigger-folk-theorem/grim-trigger-folk-theorem.py` (sim-lab PR #316, merge SHA 41d3bb8). Paired verdict: VERDICT 236 (offset +13).
> results_sha256 = `7f00cea0bd40b2133ae9e91110c5112e8d5bf16bbcd90809a91911015215334f`

## Head

In an infinitely-repeated symmetric Prisoner's Dilemma with stage payoffs `T > R > P > S` (temptation, reward, punishment, sucker), the **grim trigger** strategy — cooperate until any defection, then defect forever — sustains mutual cooperation `(C, C)` as a **subgame-perfect equilibrium iff the discount factor satisfies** `δ ≥ δ*` with the **EXACT threshold**

```
δ* = (T − R) / (T − P).
```

The claim is not "sufficiently patient players cooperate" (the loose folk statement) but the closed-form patience floor, derived firsthand by the one-shot-deviation principle:

- Cooperate-forever value: `V_C(δ) = R / (1 − δ)`.
- One-shot deviation value (defect once, then eat the grim punishment forever): `V_D(δ) = T + δ·P / (1 − δ)`.
- Indifference `V_C(δ*) = V_D(δ*)` solves to `δ* = (T − R) / (T − P)`; cooperation is a best response for every `δ ≥ δ*` and strictly not below it.

Punishment is **credible**, so grim trigger is subgame-perfect and not merely a Nash threat: mutual defection `(D, D)` is itself a stage Nash equilibrium (nobody gains by unilaterally switching back to `C` during punishment, since `S < P`), so the trigger never has to carry out a non-credible promise. For the canonical PD `(T, R, P, S) = (5, 3, 1, 0)` the threshold is exactly `δ* = 1/2`.

## Why it matters (fleet framing)

Cooperation among self-interested agents is a **patience threshold, not a personality trait**. Whether a repeated-interaction protocol (a reputation system, a tit-for-defect enforcement lane, a repeated-bargaining channel between fleet lanes) can hold a cooperative equilibrium is decided by ONE inequality: does the per-round discount factor clear `(T − R)/(T − P)`? Two design traps fall out. First, the naive belief that "any positive patience buys cooperation" is exactly wrong — below `δ*` a one-shot deviation is *strictly* profitable, which the falsifiability gate kills at 448σ. Second, the intuitive but wrong closed form `δ_wrong = (T − R)/(T − S)` (dividing by the FULL temptation-to-sucker spread instead of temptation-to-punishment) is a plausible impostor a designer might write down; it is rejected at 140σ. The correct floor divides by `T − P` because the deviator is punished down to `P`, never to `S`.

## Exact core identities (proved firsthand by the verifier)

- **Headline indifference** `(T, R, P, S) = (5, 3, 1, 0)`: `δ* == Fraction(1, 2)` and the incentive gap `V_C(δ*) − V_D(δ*) == Fraction(0, 1)` exactly — the equilibrium condition binds with zero slack at the threshold.
- **Grid of exact thresholds** (all as reduced `Fraction`s, each strictly interior `0 < δ* < 1`):
  - `(5, 3, 1, 0) → δ* = 1/2`
  - `(5, 4, 1, 0) → δ* = 1/4`
  - `(5, 2, 1, 0) → δ* = 3/4`
  - `(9, 8, 1, 0) → δ* = 1/8`
  - and for every tuple the indifference gap `V_C(δ*) − V_D(δ*) == 0/1` exactly.

## Gate battery (SEED=20260717, N_MC=200000, Z_GATE=3.0, deterministic; each direction stated)

| Gate | Kind | Direction / PASS rule | Result |
|---|---|---|---|
| G1 | Exact indifference (EQUALITY, `Fraction`) | headline `(5,3,1,0)`: `δ* == 1/2` AND gap `V_C(δ*)−V_D(δ*) == 0/1` | exact equal ✅ |
| G2 | Exact grid (EQUALITY across grid, `Fraction`) | `δ* ∈ {1/2, 1/4, 3/4, 1/8}`, every gap `== 0/1`, each `0 < δ* < 1` | 0 mismatch ✅ |
| G3 | MC agreement (AGREEMENT, `|z| < 3`) | at `δ* = 0.5` the simulated deviation payoff matches theory | z=1.404082 ✅ |
| G4 | MC grid (AGREEMENT across grid, `max|z| < 3`) | all four tuples agree within 3σ | max|z|=1.150506 ✅ |
| G5 | Falsify wrong formula (REJECTION, `|z| > 6`) | naive `δ_wrong=(T−R)/(T−S)=2/5`; exact `E[D]=−2/3 ≠ 0` | z=−140.372466 REJECTED ✅ |
| G6 | Falsify below threshold (REJECTION, `z < −6`) | at `δ*/2=1/4`, exact `E[D]=−4/3 < 0` (deviation strictly profitable) | z=−448.661725 REJECTED ✅ |

All six PASS; `all_pass=true`, `first_failing_gate=null`. Each gate is checked **in its own direction**: the exact-equality gates require zero rational error, the two Monte-Carlo agreement gates require the simulated deviation gap to sit inside 3σ of the theoretical zero, and the two falsifiability gates require the wrong model to be rejected far *outside* the band. The per-tuple z-scores in G4 are `1/2 → −1.150506`, `1/4 → 0.654137`, `3/4 → 0.630256`, `1/8 → −0.319587` (max magnitude 1.150506).

## Determinism & digest

`build_results()` is a pure function of `SEED=20260717` and the fixed payoff grid (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture). `main()` runs it twice and asserts the canonical JSON forms are byte-identical; a separate re-invocation reproduces the same digest. Full 64-hex:

```
results_sha256: 7f00cea0bd40b2133ae9e91110c5112e8d5bf16bbcd90809a91911015215334f
```

## Grounding & scope

The grim-trigger strategy and its subgame-perfect discount-factor condition are grounded in the English Wikipedia article **"Grim trigger"** at pinned revision `https://en.wikipedia.org/w/index.php?title=Grim_trigger&oldid=1292515670`@`beb2798d4ee3752cda422e6192a02e0ca3ea7926` (rev 2025-05-27T10:39:41Z). The `action=raw` wikitext bytes hash to exactly the MediaWiki-reported rev sha1 (`sha1sum` of the fetched bytes = `beb2798d4ee3752cda422e6192a02e0ca3ea7926`, MATCH).

**Scope caveat (verified by grep of the pinned wikitext).** The pinned revision DOES state, verbatim: the grim-trigger strategy ("cooperate in the first round … as long as his opponent does not defect … Once the player finds that the opponent has betrayed … he will then defect forever"); that "the strategy is an SPE only if the discount factor is `δ ≥ 1/2`"; that `(D, D)` is "the unique Nash equilibrium … the punishment profile"; and the one-shot-deviation-style value comparison that yields it — including the subgame-perfect argument that cooperation must best-respond to cooperation and defection to defection "for every subgame." It does **NOT** give the general closed form `δ* = (T − R)/(T − P)` for arbitrary `T > R > P > S`: the page works a single normalized PD whose threshold is `1/2` (consistent with this card's `(5,3,1,0)` headline). The general `(T − R)/(T − P)` threshold, the exact-`Fraction` grid, the Monte-Carlo agreement, the two falsifiability legs, and the results-dict digest are therefore established **FIRSTHAND by the verifier**, machine-checked, not taken from Wikipedia — neither oversold nor undersold.

## Reproduce

```
python3 sims/verdict-236-grim-trigger-folk-theorem/grim-trigger-folk-theorem.py   # (in sim-lab)
```

Exit 0 iff all six gates pass; prints the results dict and `results_sha256:`. The verifier is stdlib-only (`fractions`, `random`, `json`, `hashlib`, `math`) and already merged in sim-lab (PR #316, merge SHA 41d3bb8); an in-process double-run and a separate re-invocation are byte-identical.

## Probe report (v0, self-adversarial)

**1. Is the threshold identity a coincidence of the `(5,3,1,0)` payoff choice?** No. G2 recomputes `δ* = (T − R)/(T − P)` as an exact reduced `Fraction` on a grid `{(5,3,1,0), (5,4,1,0), (5,2,1,0), (9,8,1,0)}` and gets four *different* interior thresholds `{1/2, 1/4, 3/4, 1/8}`, each with the indifference gap exactly `0/1`. If the formula were fitted to the canonical `1/2` it would fail the other three tuples; it does not. The `1/2` is just the `(5,3,1,0)` instance, not a tuned constant.

**2. Is the derivation actually a valid one-shot-deviation argument, or a hand-wave?** It is the one-shot-deviation principle applied correctly: `V_C = R/(1−δ)` versus deviate-once-then-punished `V_D = T + δP/(1−δ)`. Setting `V_C = V_D` gives `R/(1−δ) − δP/(1−δ) = T`, i.e. `(R − δP) = T(1 − δ)`, i.e. `δ(T − P) = T − R`, i.e. `δ* = (T − R)/(T − P)`. G1 confirms the gap `V_C(δ*) − V_D(δ*)` is exactly `0/1` at that δ*, so the algebra binds with zero slack.

**3. Is the Monte-Carlo model the right stochastic interpretation, or a decoration?** The MC leg (G3/G4) simulates the discounted deviation payoff difference and checks it agrees with the exact theoretical value (zero at δ*) within 3σ over N_MC=200000 draws — an independent estimator that would diverge if the closed form were wrong. It is corroboration, not the proof; the proof is the exact-`Fraction` gates. Honest scope: the MC leg assumes the discounting/payoff model, it does not re-derive optimality — the exact gates do.

**4. Is the falsified alternative actually the naive one someone would pick?** Yes — deliberately. `δ_wrong = (T − R)/(T − S)` divides by the temptation-to-*sucker* spread, the most plausible wrong denominator for anyone who forgets the deviator is punished down to `P`, not `S`. G5 shows this impostor has exact theoretical `E[D] = −2/3 ≠ 0` and rejects it at z=−140.372466. The wrong formula is a genuine near-miss, not a straw man.

**5. Does the result distinguish subgame-perfection from mere Nash?** Yes, and it must. The threshold is stated as a *subgame-perfect* equilibrium condition because the punishment `(D, D)` is itself a stage Nash equilibrium (`S < P` means switching back to `C` during punishment is worse), so the grim threat is credible and holds in every subgame — exactly the argument the pinned Wikipedia revision makes ("this is true for every subgame"). A pure-Nash reading would admit non-credible threats and a looser bound; this card claims the tighter SPE floor.

**6. Are the falsifiability gates real teeth or trivially satisfied?** Real. G5 (wrong formula, z=−140) and G6 (below-threshold deviation strictly profitable, exact `E[D] = −4/3 < 0`, z=−448.661725) are *rejection* gates in the opposite direction to the agreement gates G3/G4 — a verifier that reproduced only a wrong model would (correctly) fail them. G6 specifically refutes the folk overreach "cooperation holds for all δ > 0" by exhibiting a strictly profitable deviation at `δ*/2 = 1/4`.

**7. Is `all_pass` gameable by a single degenerate parameter?** No. The six gates test distinct directions: two exact-rational equality gates (headline + four-tuple grid), two within-3σ Monte-Carlo agreement gates, and two beyond-6σ rejection gates in the opposite sign. No single degenerate payoff tuple or δ satisfies all six; a verdict session reproduces the exact 64-hex digest to confirm every constant.

**8. How will a verdict session know it reproduced the head?** It re-runs the stdlib verifier under `SEED=20260717`, `N_MC=200000`, and confirms `all_pass=true`, `first_failing_gate=null`, the four exact thresholds `{1/2, 1/4, 3/4, 1/8}` with zero-gap, the four gate z-scores (`1.404082`, `max 1.150506`, `−140.372466`, `−448.661725`), and results-dict sha256 `7f00cea0bd40b2133ae9e91110c5112e8d5bf16bbcd90809a91911015215334f` byte-for-byte (in-process double-run and separate-process run byte-identical). Any gate fail or digest mismatch is a REJECT. This paired verifier already merged as sim-lab PR #316 (merge SHA 41d3bb8, VERDICT 236).

## One-line design fix

When you need self-interested agents to sustain cooperation in a repeated interaction, do not assume patience alone buys it — compute the exact floor `δ* = (T − R)/(T − P)` from the stage payoffs and make the per-round discount factor clear it, remembering the denominator is temptation-minus-*punishment* (not minus-sucker) and that the punishment must be a credible stage equilibrium or the threshold does not hold.

**Recommendation: sim-ready**
