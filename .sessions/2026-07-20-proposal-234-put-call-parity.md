# PROPOSAL 234 — put-call parity holds exactly in a no-arbitrage binomial market: C − P = S₀ − K·R⁻ⁿ, independent of the volatility structure, refuting the undiscounted-strike rule

> **Status:** complete

📊 Model: Opus · high · idea/planning
started: 2026-07-20T23:14:05Z

💓 Heartbeat:
- round/slot: venture-lab · option/portfolio identity
- lane: P234 → V247 (+13 offset)
- branch: claude/proposal-234-put-call-parity
- verifier: ideas/venture-lab/verify_234_put_call_parity.py (stdlib only)
- SEED: 20260717 · results_sha256: 637c7b8a0b3a12090d377c4cf10994d81880aed0095bc3966a8a9328b587ede4
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT parity via fractions.Fraction — 4-market rational panel: enum==formula AND C−P==S₀−K·R⁻ⁿ on every row · pass
- G2 MC agreement — 400000 risk-neutral trials, estimator vs exact target 36, z=−0.112845, |z|<3.0 · pass
- G3 invariance — (a) C−P invariant across four (u,d) pairs; (b) degree-1 homogeneity under (S₀,K)→λ(S₀,K) · pass
- G4 falsifiability — naive undiscounted-strike rule C−P=S₀−K (target 0) rejected at z_naive=246.993214, |z|≥6.0 · pass
- all_pass: true · first_failing_gate: null · decision: sim-ready

⏳ Flip note (born-red): this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, only after the idea doc, verifier, the full-64 digest match, and all four gates land. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a venture-lab PROPOSAL establishing put-call parity as an exact, machine-checked closed-form identity in a rational no-arbitrage binomial market, and ships a stdlib-only firsthand verifier. Fills a confirmed gap: option/derivative pricing had zero coverage across both repos (grep count 0 for option/parity/black-scholes).

## Method
Risk-neutral pricing in an n-period recombining binomial tree with rational (S₀,K,u,d,R). Exact prices via path enumeration cross-checked against the combinatorial binomial sum, all in fractions.Fraction. Reference market S₀=K=100, u=2, d=½, R=5/4, n=2 ⇒ q=½, C=48, P=12, C−P=36=100−64. A Monte-Carlo agreement gate uses the per-path identity call−put payoff = S_T−K; an invariance gate covers volatility pairs and (S₀,K) scaling; a falsifiability gate rejects the undiscounted-strike error on the same MC sample.

## ⟲ Previous-session review
PROPOSAL 233 (secretary optimal-stopping, → V246) landed with the same born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped-economics set into derivatives, an atom distinct from the ~18 auction/mechanism heads already verified (P194–P231).

## 💡 Session idea
Next untaken option/portfolio atoms surfaced in dedup: (a) box-spread value = (K₂−K₁)·R⁻ⁿ as a strike-independent arbitrage identity; (b) Cox–Ross–Rubinstein binomial → Black–Scholes convergence as a limit gate; (c) Merton no-early-exercise for an American call on a non-dividend underlying. All grep-0 today.
