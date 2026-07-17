# Session — PROPOSAL 099: shop-reroll ruin (round-22 game slot)

> **Status:** `complete`

- **Seat:** Ideas Lab work-slice (coordinator-dispatched)
- **Branch:** `claude/proposal-099-shop-reroll-ruin`
- **Scope:** Draft + land PROPOSAL 099 (round-22 game slot): markdown-first proposal + committed stdlib verifier + dry-sim + gates + disclosed digest. VERDICT 112 is the NEXT slice (out of scope here).
- **HEAD at start:** `74d6d46`
- Card born red (`in-progress`) holds the substrate-gate until the flip-complete last commit; the auto-merge-enabler lands the PR on green.

## Plan
- [x] Claim filed
- [x] Idea doc + stdlib verifier committed
- [x] Dry-sim run — gates PASS, digest disclosed
- [x] PROPOSAL 099 appended to control/outbox.md
- [x] Heartbeat control/status.md
- [x] Flip complete

## Close-out

- 💡 **Session idea:** Extend the reroll model from the infinite-horizon accept-threshold to a *finite gold budget*: solve the stochastic dynamic-programming optimal policy where each reroll spends from a bounded purse (state = gold remaining), yielding a budget-dependent threshold tau*(g) that rises as the purse grows — and layer a two-item "lock one slot, reroll the rest" shop mechanic on top, where the optimal-stopping bar becomes conditional on the locked item's power. Would test whether the value-trap gap widens or collapses under budget pressure.
- **📊 Model:** Claude Opus family · effort standard · task-class: proposal-drafting + stdlib-sim landing
- **Previous-session review:** previous session landed VERDICT 111 mirror for P098 via PR #489 — chain healthy at HEAD 74d6d46.
- No unresolved `[[fill:]]` placeholders remain in any file written this session.
