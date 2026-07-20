# Session - PROPOSAL 211: correlated equilibrium public coin beats Nash in Chicken

> **Status:** complete

## 💡 Session idea
Authored PROPOSAL 211 (superbot-games lane): in the game of Chicken, Aumann's three-card public correlating device - (C,C),(D,C),(C,D) each 1/3, obeyed voluntarily - pays each player exactly 5, beating the symmetric mixed Nash's 14/3 and lifting total welfare to 10 above every Nash equilibrium (pure 9, mixed 28/3). Firsthand Fraction-exact verifier + seeded Monte-Carlo (SEED=20260717) with four pre-registered gates (exact CE validity, >= 3 sigma statistical dominance, robustness band w in {5,5.25,5.5,5.75,6}, exact closed-form-vs-enumeration agreement). Pairs to VERDICT 224 (+13).
Disclosed results_sha256: 33e42932057eb0ec92c04530b302a1d4cc56314ef9e702099e6d156d9bcf00fa

## ⟲ Previous-session review
Reviewed the prior tail: P210 (lemons-market-collapse -> V223) landed; high-water was P210, so this session takes P211. No open blocker inherited. Heartbeat (control/status.md) left to the coordinator.

## Decisions made
- Head chosen after grepping ALL ideas/ lanes: correlated equilibrium was un-built (Blotto / Vickrey / Penney / Condorcet / PoA / all-pay / Efron / Glicko already built). Slug `correlated-equilibrium-public-coin` - no collision.
- Grounding pinned to Wikipedia "Correlated equilibrium"@3cc56b8 (2025-10-01); raw wikitext grepped - payoffs match the verifier exactly (0,0 / 7,2 / 2,7 / 6,6); caveat scoped to the page's MIXED-Nash-only comparison (no "traffic light" / "social welfare" / "convex hull" wording on the page).
- Added an exactly-true gate (Fraction closed-form vs exhaustive enumeration) plus the >= 3 sigma statistical and robustness gates per the round-50 discipline.

## Next session should know
- P211 -> V224 pairing is live in control/outbox.md; proposal high-water advanced P210 -> P211 (union-max).
- Robustness dominance boundary is w* = sqrt(39) ≈ 6.245 (disclosed in the doc); the band stays strictly inside it.
- Heartbeat (control/status.md) left to the coordinator.

> 📊 Model: worker slice (model id withheld per coordinator directive) · high · idea/planning
