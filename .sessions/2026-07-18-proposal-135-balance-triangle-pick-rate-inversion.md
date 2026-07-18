# PROPOSAL 135 — balance-triangle pick-rate inversion (round-31 GAME slot)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD released: this card held the PR red from its first commit until the slice was complete and verified; flipping to `complete` here releases the landing workflow.

## Objective

Draft and land round-31 GAME-slot PROPOSAL 135 — the balance-triangle pick-rate inversion: a weighted rock-paper-scissors metagame is a skew-symmetric zero-sum game whose mixed-strategy Nash equilibrium plays each unit in proportion to the margin of the matchup it is NOT part of, so buffing one unit's winning margin can LOWER its own equilibrium pick rate and RAISE its counter's — the intuitive "make pick rates equal" reading of balance is exploitable, and the game value stays 0. Ship a markdown-first card, a committed stdlib verifier, three pre-registered ≥3σ gates, and a disclosed results-dict sha256. VERDICT 148 (P135 → V148, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, ≥3σ gates on independently-computed exact closed forms.
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 135 block appended once per grammar (+13 offset → V148); did NOT write the verdict.
- Deduped against all ideas/ cards + full outbox history — first zero-sum matrix-game / minimax-equilibrium card in the game lane; distinct from the guild-volunteer-dilemma (N-player public-goods provision, not zero-sum), the matchmaking-winrate-mirage (Elo compression), the single-elim favorite-collapse (tournament order statistics), and Penney's game (fleet-lane sequence-race intransitivity).

## What happened

Synced to origin/main HEAD 787483a (VERDICT 147 mirror landed; round-31 verdict side non-contiguous with V146 for P133 still pending). Deduped a first pick (coupon-collector completion wall) and DROPPED it — coupon-collector is already a card (`ideas/fleet/coupon-collector-tail-2026-07-14.md`, and P132 explicitly deduped against it) — pivoting to a genuinely fresh mechanism. Claimed P135, branched `claude/proposal-135-balance-triangle-pick-rate-inversion`, opened PR #572 READY on the born-red card. Committed the stdlib verifier; the dry run passed all three gates (G1 equilibrium/indifference max|z|=1.314, G2 inversion R-vs-uniform +0.06721 z_exist=+120.37 matching anchor (a−c)/3=0.066667 z_anchor=+0.975, G3 placebo symmetric-triangle exploitability 0.0 exactly z=+0.594), byte-identical across two runs, exit 0, results-dict sha256 92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b. Authored the game-lane card, appended the outbox PROPOSAL 135 block (+13 → V148, offset cited from the P134 → V147 predecessor row + the status baton), updated the heartbeat (proposal high-water P134 → P135; baton → V148 for P135 then round-31 UNRELATED-slot P136; routines line unchanged coordinator-bound), then flipped this card to release the landing workflow. `python3 bootstrap.py check --strict` before the flip failed only on the designed born-red HOLD (all claims/owner-action/seat-digest warnings are "never exit-affecting").

## ⟲ Previous-session review

The round-31 VENTURE slot (P134 blended-churn LTV understatement, PR #570; V147 mirror @c6bf5e5b) landed clean on the whole-dict / no-self-field / stdout-only digest posture and the +13 offset held unbroken (P133→V146 pending, P134→V147 landed). This slice inherits that posture verbatim and continues the rotation into the round-31 GAME slot (fleet→venture→game). No regressions observed; the born-red HOLD behaved exactly as designed — the substrate session gate stayed red until the flip, and the only exit-affecting check finding was that designed hold.

## 💡 Session idea

Pick rate is a lagging, self-referential balance signal: because equilibrium usage of a unit tracks the margin of a matchup it is not even in (x*∝(b,a,c)), a "buff the under-played unit" patch pushes usage around the beat-cycle to that unit's counter, not to the unit itself. Candidate follow-up: a "margin-matrix balance dashboard" card that reads a roster's pairwise win margins and reports the *predicted* equilibrium pick rates x*∝(inverse margins) versus observed usage, flagging when a proposed buff will land its usage effect one step around the cycle — pairing this equilibrium identity with the matchmaking-winrate-mirage (P111) into a single "usage-is-not-balance" playbook.

## GROUNDING

- Verifier (firsthand, ground truth): https://github.com/menno420/idea-engine/blob/main/ideas/superbot-games/balance_triangle_pick_rate_inversion.py — results-dict sha256 92de2d5454c34f274869bc83d302682909b376380c16e60b6afcb12756424a4b, SEED=20260717, three ≥3σ gates PASS, deterministic double-run, exit 0.
- Idea card: https://github.com/menno420/idea-engine/blob/main/ideas/superbot-games/balance-triangle-pick-rate-inversion-2026-07-18.md
- External reference (reachable): Rock paper scissors — Wikipedia, https://en.wikipedia.org/wiki/Rock_paper_scissors (weighted/unbalanced variants shift the optimal mix off uniform 1/3) — verified reachable 2026-07-18; anchor von Neumann (1928) minimax + skew-symmetric matrix-game value 0 (Gale, Kuhn & Tucker 1950).
- Grounding commit: https://github.com/menno420/idea-engine@787483a · HEAD at start 787483aadad5671441a82e7bb7518f12d56784fb. PR: #572.
