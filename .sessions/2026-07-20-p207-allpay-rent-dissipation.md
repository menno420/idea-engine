# Session 2026-07-20 — P207 complete rent dissipation in the all-pay auction (round-49 GAME slot)

> **Status:** in-progress

## 💡 Session idea
Land PROPOSAL 207: complete rent dissipation in the symmetric complete-information all-pay auction. Among n ≥ 2 risk-neutral bidders for a prize worth V (highest bid wins, EVERYONE pays their own bid), the symmetric mixed equilibrium (CDF F(b) = (b/V)^(1/(n-1))) burns total expected effort EXACTLY V — independent of n — and every bidder's expected net payoff is EXACTLY zero. Competition fully dissipates the rent: more rivals do not raise total effort, they only split the same V into thinner per-head slices (V/n each). Counterintuitive (naive: more competitors ⇒ more total effort) but exactly true. A deterministic stdlib verifier proves it in closed form (F(b)^(n-1) = b/V collapses to a rational, so Π(b) = V·(b/V) − b = 0 exactly with no irrational arithmetic), then confirms the ≥3σ effect and the R̂/V→1 robustness grid by Monte-Carlo. Pairs to VERDICT 220 (+13). Disclosed results_sha256 f771cd427068cd273eb545a40179233ddbc5ec7658e69cf4e6cadb97dbb91d70.

## ⟲ Previous-session review
Prior GAME slot was P203 (voting power ≠ voting weight, Banzhaf/Shapley–Shubik, → VERDICT 216). Boot outbox high-water: P206 → V219 (round-49 VENTURE slot, independent-screens ladder, landed idea-engine #763). Dedup: `grep -ri` across ideas/** for all-pay / rent dissipation / rent-seeking / Tullock / war-of-attrition returned ZERO shipped heads (only a forward-looking mention in the P199 Vickrey card) — the all-pay head is clear, no pivot to the Chicken-CE fallback needed. Advancing outbox high-water P206 → P207 (union-max). This card is born red to HOLD the PR until authoring + preflight are green; flipping it to complete releases merge-on-green. Heartbeat (control/status.md) left to the coordinator.

> 📊 Model: worker slice (model id withheld per coordinator directive) · high · idea/planning

## Decisions made
- Primary head landed (no pivot): complete rent dissipation in the symmetric complete-information all-pay auction. Total revenue = V and net payoff = 0 are EXACT for every n ≥ 2; the win-probability identity F(b)^(n-1) = b/V makes the break-even check exact-rational (fractions.Fraction, no floats, no irrational roots).
- Three pre-registered gates, feasibility-probed first: G1 exact (n=2..8 × V∈{1,2,3,1/2}, revenue+payoff residuals both 0); G2 ≥3σ effect (n=5, M=100k, z_below_naive = 800.47 measured ≪ naive n·V/2 = 2.5, consistency |Δ|=0.00164 < 3σ); G3 robustness (36-cell n×V grid, max_dev_z = 2.37 < 3, all R̂/V within 3σ of 1). Determinism verified across three separate process invocations.
- Grounding byte-pinned to Wikipedia "All-pay auction" rev 1345188183 (sha1 276dc7a5…), which states firsthand "expected pay-offs are zero" for the complete-information mixed equilibrium. Honest caveats disclosed: the page does not print "total bids = V" (arithmetic consequence, derived firsthand), and its E[R]=1/3 worked example is the DIFFERENT incomplete-information IPV model, not our common-value model.
- Verifier lives beside the doc in ideas/superbot-games/ (single-repo PROPOSAL convention, per P203/P206); sim-lab reproduces at VERDICT 220 time.

## Next session should know
- P207 → VERDICT 220 (+13) is now awaiting sim-lab reproduction of digest f771cd42…b91d70; outbox high-water advanced P206 → P207. Heartbeat (control/status.md) left to the coordinator.
- A reusable stdlib all-pay-equilibrium harness (exact Fraction closed-form + seeded Monte-Carlo effect/robustness gates) now lives in ideas/superbot-games/allpay-rent-dissipation-2026-07-20.py.
