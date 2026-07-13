# Session — PROPOSAL 047: creature rarity vs skill — can a Common team counter an Epic? (game-mechanics rotation, round 8)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-13T21:21:37Z (Ideas Lab worker slice — draft the
> GAME-MECHANICS rotation round-8 head under standing owner ORDER 003. Card born
> in-progress as the designed gate hold; flips complete in this PR's final commit)

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 8, under standing owner ORDER 003 (continuous pipeline) and ORDER 004
rule 3's rotation. Round 8 opened at fleet backlogs with P045 (#343) and served
venture with P046 (#348), so game mechanics is next per ORDER 004 rule 3.
Slot rounds 1–7 were P020 casino odds → V022 reject, P023 entry fee → V025
reject, P027 comp/stipend → V029 null, P031 explore pacing → V033, P035 mining
booster throttle seal → V046 null, P039 Gloamline survival ceiling → V050
approve, P043 Brineward band necessity → V054. The last two game rounds (P039,
P043) both drew from gba-homebrew, so round 8 rotates the SOURCE to the hub's
own creature game (`menno420/superbot`), deliberately avoiding the nine queued
SIM-REQUEST domains (local ORDERs 005/006: venture pricing ×4, idle economy,
superbot-games mining/fishing/dnd/exploration).

Harvest source: superbot's committed creature PvP battle engine
(`disbot/utils/creatures/battle.py` @ HEAD
`1cc553651a19016a4b1439f048b49e7baa28dfb1`, read via shallow clone) — the
level-normalized anti-P2W ruleset's two load-bearing, never-cross-rarity-tested
lines: "rarer = stronger, but level + type + move choice still let a Common
counter an Epic" (the `RARITY_BUDGET` comment) and "Flat-level PvP makes types
+ team-building + ordering + move choice decide, so it rewards *skill*, not
*time spent*" (module docstring). The in-repo design sim
(`tools/game_sim/creature_battle_sim.py`) validated type balance, level
dominance, normalized fairness, and skill impact — always on same-rarity or
randomly-mixed rosters, never rarity-vs-rarity. Idea file
`ideas/superbot/creature-rarity-skill-counter-2026-07-13.md` (probed
single-pass this slice, sim-ready), then appended to `control/outbox.md` as
PROPOSAL 047. Seeds 20261325–328, strictly above the P046 high-water 20261324
(re-swept this session: digit-boundary + range-notation companion recipe over
this tree and /home/user/sim-lab; sim-lab allocates none — its 20260881–1280
fishing robustness block sits below the proposal series' floor).

**📊 Model:** `fable-5` (family-level self-report from this session's own harness,
per ORDER 001 / Q-0262 — never copied from a schedule surface) · content + outbox
proposal only (idea file, card, section index row, claim file, outbox append; no
product code, no control/status.md or control/inbox.md writes; no sim-lab writes —
the V057 verdict session runs parallel there and its claim
`control/claims/claude-verdict-057-keyword-tiling.md` is untouched)
