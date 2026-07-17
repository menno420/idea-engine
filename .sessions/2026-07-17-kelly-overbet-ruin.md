# Session — PROPOSAL 100: Kelly overbet ruin (round-22 UNRELATED-slot closer)

> **Status:** `complete`

- **Seat:** Ideas Lab work-slice (coordinator-dispatched)
- **Branch:** `claude/proposal-100-kelly-overbet-ruin`
- **Scope:** Draft + land PROPOSAL 100 (round-22 UNRELATED-domain closer, rotation fleet→venture→game→unrelated): markdown-first proposal + committed stdlib verifier + dry-sim + gates + disclosed digest. Domain = information theory / mathematical finance (Kelly 1956 growth-optimal capital allocation) — fleet-external pure-mechanism head. VERDICT 113 is the NEXT slice (P100 → V113, +13; out of scope here).
- **HEAD at start:** `a8c10e3`
- Card born red (`in-progress`) holds the substrate-gate until the flip-complete last commit; the auto-merge-enabler lands the PR on green.

## Plan
- [x] Claim filed
- [x] Idea doc + stdlib verifier committed
- [x] Dry-sim run — gates PASS, digest disclosed
- [x] PROPOSAL 100 appended to control/outbox.md
- [x] Heartbeat control/status.md
- [x] Flip complete

## Close-out

- 💡 **Session idea:** The Kelly overbet trap and P099's shop-reroll trap are the same optimal-control shape seen through two lenses — an interior optimum with a ruinous far side — but they split on additive-vs-multiplicative accounting. A follow-up head worth pricing: a MIXED-horizon Kelly with a finite-round terminal utility (a bounded game, not the infinite limit), where the growth-optimal fraction is no longer a constant f* but a state-dependent schedule f*(rounds-remaining, wealth-vs-target) — and test whether a "bet-to-hit-a-target" objective (finish above W_target) pushes the optimal fraction ABOVE or BELOW the log-optimal f*, i.e. whether goal-seeking rationalizes the very overbetting the infinite-horizon criterion forbids. This bridges the round-22 unrelated closer to a genuinely new mechanism rather than a re-skin.
- **📊 Model:** opus-4.8 · medium · idea/planning
- **Previous-session review:** the previous session landed VERDICT 112 mirror for P099 (shop-reroll ruin) at HEAD a8c10e3 (PR #491) — the game slot closed cleanly and the baton (proposal high-water P099 → next UNRELATED closer P100) was recorded accurately in control/status.md; this slice picked it up with zero re-derivation. One small friction carried forward: the two stale claim files (proposal-099, verdict-112) were left un-pruned at HEAD and both backtick their trailing date, which trips the check_claims duplicate scan against any new same-day claim — I side-stepped it by un-backticking my own date (bt-controller shape), and flagged the stale pair for the successor prune.
- No unresolved `[[fill:]]` placeholders remain in any file written this session.
