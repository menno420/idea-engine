# PROPOSAL 235 — the value of a 2×2 zero-sum game (von Neumann minimax): for a no-saddle payoff matrix M=[[a,b],[c,d]] the value is the exact rational v = (a·d − b·c)/(a + d − b − c), refuting the "value == pure security level" rule

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-20T23:48:03Z

💓 Heartbeat:
- round/slot: game-theory · strategic-form / minimax value
- lane: P235 → V248 (+13 offset)
- branch: claude/proposal-235-zerosum-value
- verifier: ideas/fleet/verify_235_zerosum_2x2_value.py (stdlib only)
- SEED: 20260717 · results_sha256: a8d766a845b4cd53518fc572f30041dfb154148a67f399c39463476ec1e4276a
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT value identity via fractions.Fraction — 4-game no-saddle rational panel: closed-form v == indifference-route v AND mixes interior on every row, plus a saddle-game cross-check · pass
- G2 MC agreement — 400000 trials, both players sampling their optimal mix, estimator vs exact target v=1/7, z=0.345941, |z|<3.0 · pass
- G3 invariance — (a) minimax guarantee: row fixed at optimal mix pays exactly v vs every column in a panel; (b) affine invariance: M→αM+β shifts value to αv+β exactly, mixes unchanged · pass
- G4 falsifiability — naive "value == pure-strategy security level (maximin)=−1" rejected at z_naive=462.564053, |z|≥6.0 · pass
- all_pass: true · first_failing_gate: null · decision: sim-ready

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it now flips to complete as the deliberate LAST commit, after the idea doc, verifier, the full-64 digest match, and all four gates landed, and after the owner review checkpoint (fm ORDER 048). The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing the value of a 2×2 zero-sum game as an exact, machine-checked closed-form identity — von Neumann's minimax value v = (a·d − b·c)/(a + d − b − c) for a no-saddle row-maximiser matrix — and ships a stdlib-only firsthand verifier. Fills a confirmed gap: the foundational 2×2 zero-sum minimax value is untaken across both repos (the nearest neighbours are a 3×3 skew-symmetric value-0 pick-rate head and Penney's nontransitive minimax edge, both categorically distinct).

## Method
Exact rational game theory over `fractions.Fraction`. For the reference matrix M=[[3,−1],[−2,1]] the closed form gives v=1/7 with row=(3/7,4/7), column=(2/7,5/7); the pure-strategy security level (maximin) is only −1, strictly below v. G1 cross-checks the closed-form value against an independent indifference-equation route on a 4-game no-saddle panel and confirms each mix is interior; a Monte-Carlo agreement gate (both players drawing their optimal mix) confirms E[payoff]=v; an invariance gate covers the minimax guarantee and affine reparametrisation; a falsifiability gate rejects the "value == security level" error on the same MC sample.

## ⟲ Previous-session review
PROPOSAL 234 (put-call parity, → V247) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped strategic set into the foundational 2×2 zero-sum minimax value, an atom distinct from the strategic heads already verified (P211 correlated eq, P214 Nash bargaining, P215 Stackelberg, P223 folk theorem, P171 Blotto, P195 Efron dice).

## 💡 Session idea
Next untaken zero-sum / minimax atoms surfaced in dedup: (a) the 2×n / m×2 zero-sum value via the lower/upper envelope (graphical method) as an exact rational; (b) the minimax theorem as LP duality — primal maximin == dual minimax objective on a rational panel; (c) skew-symmetric ⇒ value-0 with a symmetric optimum as a general-n identity (the 3×3 case is P135; the n-atom is open). All grep-checked today.
