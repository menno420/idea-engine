# Session — PROPOSAL 059: prestige reset-policy optimality — is the idle engine's own "optimal-play" greedy reset loop actually optimal at the HEAD fold, and what does the flagged reset-spam cap cost? (GAME-MECHANICS rotation, round 11)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T05:07:07Z (Ideas Lab worker slice — draft the
> round-11 GAME-MECHANICS slot proposal under standing owner ORDER 003/004.
> Card born in-progress as the designed gate hold; flipped complete in this
> PR's final commit at 2026-07-14T05:22:08Z)

**📊 Model:** fable-family · content-only slice (idea file, card, lane index
row, outbox append, claim file; no scripts/, no control/status.md or
control/inbox.md writes; nothing in sim-lab or either cloned game repo)

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 11, under standing owner ORDER 003 (continuous pipeline) and ORDER 004
rule 3. Round 11 opened at fleet backlogs with P057 (#391) and served venture
with P058 (#395), so game mechanics is next; the slot's own spacing-4 history
(P020 … P051, P055 → P059) confirms. The slot's five most recent draws were
superbot ×2, mineverse, gba-homebrew ×2 — this slice rotates to the ONE World
repo the slot has never drawn: superbot-idle.

Harvested head: superbot-idle's prestige/reset mechanic at HEAD
`5ddd5a230d4a6504c06b52805cba5dc8b3276b44` — the committed claim that greedy
prestige-iff-eligible play is "optimal" (the SIM-001 harness's own S3
"optimal-play speedrun" label + the prestige.py docstring's "the optimal loop
is reset-and-grow rather than one endless grind"), priced as a pre-registered
deterministic policy-grid sim at the FULL HEAD multiplier fold — which now
includes the milestone bonuses the committed harness omits — plus the lane's
own flagged-but-unpriced reset-spam degeneracy ("~80,796 resets in 14 days …
likely wants a pre-registered cap/cooldown criterion", control/status.md),
priced via cooldown arms.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot-idle/prestige-reset-policy-optimality-2026-07-14.md` + the
`ideas/superbot-idle/README.md` index row, and the `control/outbox.md`
PROPOSAL 059 append. Seeds 20261373–376 strictly above the P058 high-water
20261372. PR #402.

## Constraints honored

- control/status.md and control/inbox.md untouched (coordinator/manager-only).
- control/outbox-archive-2026-07-14.md untouched (rolled archive, terminal).
- sim-lab read-only (dedup ledger read locally at origin/main; nothing edited).
- Open claims and PRs of other sessions untouched (the order-008 housekeeping
  claim; PRs #361/#364 parked owner-held — none mine).
- Outbox append-only (appended via shell, never loaded into an editor); no
  renumbering; all timestamps from real `date -u`.
- superbot + superbot-idle read FIRSTHAND via clone (superbot via add_repo per
  the audit-depth route; superbot-idle via the Q-0272 standing public-clone
  authorization) — zero writes to either.

## 💡 Session idea

**A committed "optimal" label is a claim with a hidden dependency on the
multiplier fold it was evaluated in — every engine slice that adds a factor
to the rate fold silently stales every recorded optimality/pacing label
built on the old fold, and nothing goes red.** Hit live this slice: the
achievements slice extended superbot-idle's production fold with persistent
milestone bonuses, but the committed SIM-001 harness (`tools/simulate.py`,
the artifact whose S3 docstring carries the "optimal-play" label) folds zero
milestones — it still runs green, reproduces all its V038 anchors, and
quietly answers last month's question. The drafting grid shows the drift is
not cosmetic: at the shipped fold the labeled-optimal policy is beaten by
7.98% by a one-detour schedule whose entire edge comes from the factor the
harness omits (the beat inverts to a loss with milestones off). The durable
pattern for any engine repo: a fold-extension PR should carry a checklist
item "re-run or re-scope committed policy labels/harnesses against the new
fold" — the same class as a schema change requiring a consumer sweep, except
no parser fails to force it, so it has to live in the pre-registration
discipline itself.

## ⟲ Previous-session review

Previous card (`.sessions/2026-07-14-proposal-058-rubric-robustness.md`, P058
drafter): a genuinely useful trail. Its rotation restatement ("round 11
opened at fleet backlogs with P057, venture next") made this slice's slot
derivation a one-line read, and its Grounding-line byte-format was mirrored
verbatim here (the CI grounding regex is unforgiving; having a known-green
example in the newest card saved a red). Its 💡 (live-upstream-fetching
checkers make every PR hostage to sibling format drift) held this session —
`check_sections.py` stayed green because the roster didn't regenerate
mid-slice, which is luck, not a fix; ASK 005 routing the generator-side
contract is the right escalation. Its recurring observation that the
seed-sweep recipe lives as oral tradition got confirmed AGAIN: this session
re-derived the boundary-aware regex from that card's own prose — third
consecutive card to note this; the recipe is one committed script away from
never being re-derived. One nit: its card's "three checker legs" phrasing
and the preflight's actual 10-check list drifted apart — this card names the
wrapper (`scripts/preflight.py`) instead of a count.
