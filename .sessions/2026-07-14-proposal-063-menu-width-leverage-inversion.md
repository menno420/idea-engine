# Session — PROPOSAL 063: menu-width leverage inversion — does message-XP widen the D&D menu into FEWER rewards, and can a data-only reorder fix it? (GAME-MECHANICS rotation, round 12)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-14T11:39:14Z (Ideas Lab worker slice — draft the
> round-12 GAME-MECHANICS rotation slot proposal under standing owner
> ORDER 003/004 and inbox ORDER 012 item (3) / ORDER 013 STEP 1. Card born
> in-progress as the designed gate hold; flips complete in this PR's final
> commit)

**📊 Model:** fable-family · content-only slice (idea file, card, superbot-games
index row, outbox append, claim file; no scripts/, no control/status.md or
control/inbox.md writes; nothing in sim-lab or superbot-games)

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 12, under standing owner ORDER 003 (continuous pipeline), ORDER 004
rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's book/product
space → game mechanics → COMPLETELY UNRELATED domains (I want those too)"),
and the EAP-final-day dispatches (inbox ORDER 012 item (3), ORDER 013 STEP 1
— the pipeline went momentarily DRY at P062 → V073 APPROVE). Round 12 opened
at fleet backlogs with P061 (#408) and served venture with P062 (#410), so
game mechanics is next, confirmed against the slot's own spacing-4 history
(P020, P023, P027, P031, P035, P039, P043, P047, P051, P055, P059 → P063).

Source rotation inside the slot: the six most recent draws were gba-homebrew
×2 (r6/r7), superbot ×2 (r8/r9), superbot-mineverse (r10), superbot-idle
(r11) — so round 12 returns to the World repo the slot has not drawn since
round 5: **superbot-games** (P031 explore pacing, P035 mining booster
throttle were its two draws; pokemon-mod-lab, the only never-drawn games
lane, stays excluded as DARK — private since 2026-07-10, the Q-0260 rule-3
carve-out recorded in `ideas/pokemon-mod-lab/` at this repo's HEAD).

Harvest source: the D&D bounded-menu engine, read FIRSTHAND this session on
a read-only shallow clone at superbot-games HEAD
`e3930f134119dd36d9e7f37a7dccb4f4b33e3805` (git clone --depth 1, fetched
2026-07-14T11:31:51Z). The head prices the message-XP → menu-width leverage
(`games/exploration/quest/leverage.py`) THROUGH the resolver's prefix
truncation (`games/dnd/core/resolver.py::_allowed_options` slices
`scene.options[:limit]`) against the shipped scene data
(`games/dnd/data/scenes.py`), where every scene ships mint-first,
default-no-op-last — the pipeline's first menu-composition / reward-gradient
head. The repo's own `games/dnd/sim/menu_sim.py` deliberately bypasses the
width clamp (`_FULL_MENU_XP = 5_000`), so the low-XP prefix regime is
unsimmed anywhere.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot-games/menu-width-leverage-inversion-2026-07-14.md` + the
`ideas/superbot-games/README.md` index row, and the `control/outbox.md`
PROPOSAL 063 append. Seeds 20261389–392 strictly above the V073 high-water
20261388.

## Constraints honored

- control/status.md and control/inbox.md untouched (coordinator/manager-only).
- control/outbox-archive-2026-07-14.md untouched (rolled archive, terminal).
- sim-lab untouched entirely; superbot-games read FIRSTHAND read-only (the
  scratchpad shallow clone at `e3930f1`, git-log-verified); no lane file
  edited.
- Open claims and PRs of other sessions untouched.
- Outbox append-only (appended via shell, never loaded into an editor); no
  renumbering; all timestamps from real `date -u`.
- Seed sweep boundary-aware at drafting HEAD `8e171bd`: max genuine
  allocation 20261388 (V073 registration); the larger standalone numerals
  (20261542/20261664/20261833 and kin) are the documented Fraction-numerator
  data-not-seed specimens.
