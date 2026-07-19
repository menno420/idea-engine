# PROPOSAL 162 — the option-pool shuffle: a pre-money option pool dilutes founders alone, leaving the investor's post-money stake invariant to pool size (P162 → V175, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-38's VENTURE-slot PROPOSAL 162: a fresh, counterintuitive, quantifiable mechanism from startup cap-table economics. Head: the "option-pool shuffle" — when a priced round's option pool is created PRE-money (standard VC term-sheet practice), the incoming investor's post-money ownership fraction equals I/(P+I) and is INVARIANT to the pool size q, so founders absorb 100% of the pool's dilution. Relative to a "fair" pro-rata pool (which would dilute the investor to (I/(P+I))·(1−q)), the shuffle transfers exactly q·I/(P+I) of the company from founders to the investor. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT 175 session can check independently. Hand to VERDICT 175 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED=20260717 pinned; deterministic in-process double-run + cross-invocation double-run asserts; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, pretty indent=2 dump).
- three ordered z-gates (z_gate=3.0): G1 investor-fraction invariance to pool size (rejects the pro-rata null), G2 founders→investor wealth transfer = q·I/(P+I), G3 robustness under a shifted (mega-round / higher-pool) distribution.
- +13 offset (P162 → V175). Outbox append-only + dedupe. Status high-water take-max, never regress. Born-red HOLD; merge-on-green landing.
- Grounding cites a reachable real-world source (verified live 200 this session); crossover/caveat disclosed honestly. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (PROPOSAL 161 / P161 high-water = current tail; +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): the option-pool shuffle — a term-sheet option pool created pre-money lowers the founders' effective valuation and dilutes them, not the incoming investor. https://venturehacks.com/option-pool-shuffle · fetched 2026-07-19 (verified live HTTP 200 this session: "Slipping the option pool in the pre-money lowers your effective valuation ... The actual value of the company you have built is $6M, not $8M."). Canonical primary: Babak Nivi with Brad Feld, "The Option Pool Shuffle" (Venture Hacks).

## Probe questions
**1.** Is the investor's post-money fraction genuinely invariant to the pool size q under the pre-money (shuffle) convention? — G1 measures, over N paired draws, the change in the investor's realized integer-cap-table fraction between a low pool q_lo and a high pool q_hi at fixed (P, I); under the shuffle it stays ≈0 while the pro-rata null predicts a change of −(I/(P+I))·(q_hi−q_lo), and the divergence is reported at z ≥ 3.
**2.** Does the founders→investor wealth transfer equal q·I/(P+I) exactly (the shuffle vs a pro-rata pool)? — G2 measures the investor-fraction gap between the shuffle and a pro-rata pool at matched (P, I, q) and checks it against the closed form q·I/(P+I) at z ≥ 3.
**3.** Does the invariance survive a shifted distribution (mega-rounds, pools up to 30%)? — G3 re-runs G1 under a shifted regime (larger pre-money, higher pool band, wider investor-target band) and confirms the invariance holds and the divergence stays decisively above the null at z ≥ 3.
**4.** Crossover, not the claim: a "who bears the dilution" reading generalizes to any pre-round carve-out (advisor pools, warrant coverage). Is it disclosed as a crossover, not asserted as the verified claim? — disclosed as a crossover; the verified claim is the option-pool-shuffle invariance under the standard priced-round cap-table model.

## Outcome
Verifier `ideas/venture-lab/option_pool_shuffle.py` + doc `ideas/venture-lab/option-pool-shuffle-2026-07-19.md` committed at `81c591f`. Three z-gates PASS in order — G1 investor-fraction invariance z=+194.139005 (prorata_minus_shuffle_change_mean=-0.0283, shuffle_change_absmean=0.0), G2 founders→investor transfer = q·t z=+260.109119 (transfer_mean=0.04526 = predicted, relerr_mean=0.0), G3 robust under the shifted mega-round distribution z=+246.501756 (prorata_minus_shuffle_change_mean=-0.024062); all_pass=true, first_failing_gate=null. results-dict sha256 `f588004512fce81ea824be9fec0c95a3ba2f3e2a8ec03af5867b526bbcb5b4b5` reproduced byte-identical across an in-process + cross-invocation double-run. Grounding verified live HTTP 200 this session (venturehacks.com/option-pool-shuffle). Outbox PROPOSAL 162 block appended (status: sim-ready, P162 → V175, +13); proposal high-water take-max advanced P161 → P162. PR #633.

## ⟲ Previous-session review
Round-38 FLEET opener (P161 Palm's theorem / M/G/∞ spares insensitivity → V174) landed clean on three ≥3σ gates with the whole-dict digest and shifted-distribution robustness posture; that verifier discipline — invariance framed as an exact insensitivity claim plus a distribution-shift robustness gate — carries forward here into the venture slot P162 → V175 (+13).

## 💡 Session idea
Anti-dilution ratchet invariance: under a full-ratchet anti-dilution provision the conversion-price reset (and hence founder dilution) depends only on the down-round PRICE, not the SIZE of the down round — a $1 down-round issuance triggers the same per-share reset as a $10M one, the exact counter-flip of weighted-average anti-dilution where dilution scales with the raise. Named, not authored.
