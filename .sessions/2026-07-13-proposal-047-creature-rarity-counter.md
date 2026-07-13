# Session — PROPOSAL 047: creature rarity vs skill — can a Common team counter an Epic? (game-mechanics rotation, round 8)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-13T21:21:37Z (Ideas Lab worker slice — draft the
> GAME-MECHANICS rotation round-8 head under standing owner ORDER 003. Card
> born in-progress as the designed gate hold; flipped complete in this PR's
> final commit at 2026-07-13T21:30:20Z)

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

## 💡 Session idea

**Harvest by validation gap — read a repo's own design-sim/validation tool as
an INDEX of what is settled, and take the check it SKIPPED as the head.** This
slice found P047 exactly that way: superbot's
`tools/game_sim/creature_battle_sim.py` stamps the creature ruleset PLAYABLE
across six named checks (type balance, raw-level dominance, normalized
fairness, skill impact, status-move value, catch grind) — and every battle
check runs on same-rarity or randomly-mixed rosters, so the code's own
"a Common can counter an Epic" comment is the one claim the stamp never
covered. The recipe generalizes at zero tooling: (1) find the lane's
validation artifact (design sim, proof set, golden suite), (2) list what it
CHECKS, (3) diff that list against the claims the adjacent comments/docstrings
MAKE — the un-checked claim is a pre-groomed sim head, because the constants,
the machinery, and the consumer are all already committed around it. Dedup
(this slice, at HEAD `bb6afe7`): P045's 💡 harvests by HEDGE MARKER ("default
suggestion" phrasing), P046's 💡 is the seed-sweep recipe, P043 harvested
never-quantified doc lines — none names the validated-artifact DIFF as the
finder; gba-homebrew's 28-assert proof set and superbot-games' catch_sim are
the two named next surfaces this recipe would index.

## ⟲ Previous-session review

Newest predecessor card
(`.sessions/2026-07-13-proposal-046-keyword-tiling.md`, worker slice ~21:05Z):
closed clean, and its 💡 EARNED ITS KEEP within one session — this slice ran
exactly its pinned seed-sweep recipe (digit-boundary regex + range-notation
companion + results.json exclusion) and it produced the 20261324 high-water
cleanly, no numerator aliases, no truncated-literal misses; that is the
fastest 💡-to-reuse turnaround in the slot's history and worth naming as
evidence the 💡 sections are compounding, not decorative. Its ASK-004
escalation also kept aging as predicted: control/outbox.md was 390,738 bytes
at its close, is larger after this slice's P047 append, and every outbox read
here was still shell-sliced — ASK 004 remains the right fix and remains
unserved. One honest nit: its claim landed via a separate fast-lane
control/-only PR (#346) while this slice's orders put the claim in the work
branch's first commit — two live claim-landing patterns now coexist in
control/claims/ history with no doc naming when each applies
(decide-and-flag: noted for the manager sweep, not expanded into this diff).

## Close-out

All pieces landed before this flip: claim + born-red card @ `2d61ece`
(branch's first commit, PR #350 opened READY immediately after the push —
never draft; merge left to the enabler workflow, no agent merge), idea doc +
section index row @ `66a05b1`, PROPOSAL 047 outbox append @ `b11a6c5` (idea:
link pinned to the `66a05b1` blob; `scripts/check_ideas.py --outbox` exit 0
verified after the append). Rotation verified at HEAD before drafting: round 8
opened at fleet backlogs with P045 (#343), served venture with P046 (#348),
game mechanics next per ORDER 004 rule 3; source rotated off gba-homebrew
(P039/P043's repo) to the hub's creature game, steered around the nine queued
SIM-REQUEST domains in local ORDERs 005/006. Seeds 20261325–328 strictly above
the P046 high-water 20261324. This flip is the branch's last commit; both
checkers (`python3 bootstrap.py check --strict`, `python3
scripts/check_ideas.py --outbox`) run green at flip time or this commit does
not push.
