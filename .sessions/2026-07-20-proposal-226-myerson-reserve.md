# Session 2026-07-20 — PROPOSAL 226 Myerson optimal reserve r*=1/2 for iid Uniform[0,1] (round-54 VENTURE slot)

> **Status:** `in-progress`
>
> Born-red HOLD: this card lands born-red (`in-progress`) on the FIRST commit to hold the PR red until the slice is genuinely done. It flips to `complete` as the deliberate LAST commit — after the idea doc + outbox block land and `python3 bootstrap.py check --strict` plus the outbox check go green. The sim-lab verifier is ALREADY landed (VERDICT 239, PR #320, squash 71365ae). LEFT RED until the flip; the landing workflow auto-merges once green + card flipped.

## 💡 Session idea
Myerson's optimal reserve for iid Uniform[0,1] bidders. Sell one indivisible item to n bidders with private values iid Uniform[0,1]. Myerson's optimal-auction theory allocates to the highest non-negative VIRTUAL value psi(v) = v − (1−F(v))/f(v) and charges the threshold. For Uniform[0,1], F(v)=v, f(v)=1, so psi(v) = 2v−1, zero at v=1/2. Hence the optimal mechanism is a second-price auction with a RESERVE r*=1/2, INDEPENDENT of n, and expected revenue

    R*(n) = 2n/(n+1) − 1 + (1/2)^n/(n+1)   (exact rational)

At n=2 this is R*(2) = 5/12 versus the no-reserve second-price revenue 1/3 — the reserve captures an extra EXACT 1/12. The counter-intuitive lesson: the revenue-maximizing reserve does not depend on how many bidders arrive (two or two hundred, r*=1/2 for Uniform[0,1]) and is strictly positive — "just run Vickrey with no floor" leaves 1/12 on the table at n=2. Verifier proves the core three exact ways (closed form, virtual-surplus integral, first-principles sell-decomposition) agreeing for n=1..5, Monte-Carlo agreement within |z|<3 at n=2,3, a dyadic-grid robustness sweep confirming r=1/2 is grid-optimal for n∈{2,3,5}, and a paired-MC falsifier rejecting "no reserve optimal" at z≈175. Disclosed results-dict sha256 = `b125afaf186e8d2430783b89af1a877193a65752db77884458485ced7ec918f0`.

## ⟲ Previous-session review
Round-54 opened with FLEET P225 (balls-into-bins collision count → V238, sibling session in flight). The rotation is fleet → venture → game → unrelated; this takes the round-54 VENTURE slot as P226 (P226 → V239, +13). The sim-lab verifier is already landed firsthand (VERDICT 239, PR #320, squash-merge 71365ae, digest b125afaf186e8d2430783b89af1a877193a65752db77884458485ced7ec918f0). High-water advance P224 → P226 (union-max; P225 held by a sibling — keep the ledger union-resolved).

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1: control/claims/2026-07-20-p226-myerson-reserve.md.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head: Myerson optimal reserve r*=1/2 for iid Uniform[0,1], earning R*(n)=2n/(n+1)−1+(1/2)^n/(n+1); 5/12 at n=2 vs no-reserve 1/3, an exact 1/12 gain. Chosen as the round-54 VENTURE slot (economics / mechanism design) — the cleanest closed-form instance of "optimize virtual values, not values," exactly true and reproducible stdlib-only.
- 7 pre-registered gates: G1 psi(1/2)=0 exact (Fraction); G2 three exact routes agree (closed form == virtual-surplus integral == sell-decomposition) for n=1..5; G3 R*(2)=5/12, no-reserve 1/3, gain 1/12 (Fraction); G4 MC n=2 vs 5/12 |z|<3 (z=−0.822); G5 MC n=3 vs 17/32 |z|<3 (z=1.816); G6 grid-optimal at r=1/2 on dyadic grid for n∈{2,3,5}; G7 paired-MC rejects "no reserve" at z=175.4.

## Next session should know
PROPOSAL 226 → VERDICT 239 (+13 offset). Verifier ALREADY landed in sim-lab: `sims/verdict-239-myerson-reserve/myerson-optimal-reserve.py` (+ run-stdout.txt + probe-report.md), PR #320, squash-merge 71365ae, digest b125afaf186e8d2430783b89af1a877193a65752db77884458485ced7ec918f0. Grounding pins Wikipedia "Regular distribution (economics)" oldid 1304906615 (rev sha 45d380f12e80c8a69f221ff09bd3eb34b44cfe05); caveat scoped — the revision quotes the virtual-valuation formula w(v)=v−(1−F(v))/f(v) and the Myerson reserve-at-zero-virtual-value principle, but does NOT specialize to Uniform[0,1], does not compute psi(v)=2v−1, and does not solve psi(r*)=0; so r*=1/2, R*(2)=5/12, the no-reserve 1/3, and the 1/12 gain are DERIVED here, not quoted. This card is LEFT RED (in-progress) until the deliberate final flip; the landing workflow auto-merges once green + card flipped.
