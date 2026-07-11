# Session — probe: channel-role-scoped-authority-gap (superbot section, TOP-5 item 3)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~14:50Z (worker slice, coordinator-dispatched,
> two-phase: research+claim, then probe+ship)

## Scope

Battery v0 probe of `ideas/superbot/channel-role-scoped-authority-gap-2026-07-10.md`
— the standing TOP-5 item 3 ("rebuild wave at pace"). Claim landed first via
fast-lane PR #175 (claim file `control/claims/probe-channel-role-authority-gap.md`,
branch `probe/channel-role-authority-gap-claim` per the workprefix+`-claim`
convention, merged `c10af1a` by the auto-merge enabler on green; claim file
DELETED at this close-out).

## What this session did

- **Inbox FIRST**: read at origin/main HEAD `2e03391` at wake and re-verified
  unchanged at `c10af1a` post-claim — still exactly ORDER 001 (standing
  per-session rule, re-satisfied by this card's 📊 Model line) + ORDER 002 (done
  by #158). No new orders; nothing preempts a superbot-section probe.
- **Claim ritual honored**: sole live claim verified by `ls control/claims/` at
  `c10af1a` post-merge (only this claim + README); work branch reset onto the new
  origin/main before building.
- **Verify-first at the LIVE heads** (phase-1 sweep, shallow clones): superbot-next
  HEAD N = `168ef80` (fetched 2026-07-11T14:36:46Z), superbot HEAD S = `9f46cb7`
  (fetched 14:36:49Z). Findings, all pinned in the report: the A-12/R-16
  `Lane.ROLE_SET` engine primitive is LIVE AND UNIT-TESTED at N
  (`sb/spec/authority.py:54`, `sb/kernel/authority/channel_access.py:52-59`,
  `resolve.py`, `decision.py:58`; tests `test_resolve_authority.py:136`,
  `test_channel_access.py:78`) — but has ZERO consumers (no `authority_ref="role:`
  in any manifest, no `channel_role_sets` writers outside kernel+tests) and the
  role/proof_channel EFFECT ports are still unarmed per the lane's 13:40Z
  heartbeat. NEW counter-evidence: the capture's live-bot claim is partially
  false — `channel_cog.py` `!set` (`:214`) and `!permissions` (`:677`) already do
  per-role overwrites, byte-identical at the capture pin `fd638e3` and at S,
  predating the 2026-07-07 research.
- **Probe shipped**: state `captured` → `parked(routed — rebuild leg MOOTED …)`;
  `> **Sequence:** before the superbot-next role/proof_channel effect-arming
  slice` added (expiry-bound verdict); full 8-question battery + park
  recommendation appended with 3 regex-clean Grounding pins; index bullet
  re-badged to the matching state echo. The arming-seam sequencing constraint is
  CITED from the parked head
  `ideas/superbot-next/effect-arming-compensator-checklist-2026-07-10.md`, not
  re-derived (that head owns it).
- **NO outbox proposal** — no sim-shaped evidence question survives Q7: the
  authority model has live unit tests; the open work is consumer wiring + arming,
  i.e. building, not uncertainty. Outbox tail stays PROPOSAL 008.
- **Heartbeat overwritten LAST**: TOP-5 item 3 marked PROBED→parked(routed); the
  FOUR-decision ≤07-14 sitting bundle, all standing ⚑ entries, sweep flags, and
  the ORDER 002 Self-review section preserved verbatim.
- Reflect residue (`.substrate/guard-fires.jsonl`) rides this PR per precedent.

**📊 Model:** fable-5 · probe slice (idea-file battery + state flip + Sequence
line + index re-badge + card + heartbeat + claim clear; no product code, Q-0260)

## 💡 Session idea

**A capture-time "already-served?" grep for gap-shaped captures.** This capture's
live-bot premise ("no command targets an arbitrary role") was falsifiable at its
own research date by one stem-grep of `channel_cog.py` for role-typed command
signatures — the two disproving commands predate the capture by a day. The
README battery already mandates verify-first at probe time; the cheaper rule is
harvest/capture-time: a capture claiming "X does not exist in lane L" should
carry one grep transcript (or a "not checked" honesty line) when first indexed.
Anchors: the reachability-check paragraph in README § The probe battery; the
harvest slices' capture template. Evidence: this file, plus the #56-card lesson
(fingerprint-greps false-MOOT) as the symmetric failure on the other side.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-usage-limit-routines-probe.md` (status
`complete`; the coordinator briefing named `2026-07-11-verdict-007-fanin.md` as
previous, but tree order wins — that card is two slices back; #174's merge
commit `2e03391` added the usage-limit card after it). Spot-checked against the
tree at `c10af1a`: its probe report exists where claimed
(`ideas/superbot/usage-limit-aware-routines-2026-07-10.md` — state
`parked(routed — …)`, 5 Grounding pins, Sequence line `before
EAP-window-wrap-2026-07-14`, park recommendation ending the report); its claim
file is gone from `control/claims/` (deleted at close per convention); its
heartbeat promises held (⚑ sitting bundle carries FOUR decisions, Self-review
preserved, TOP-5 item 4 marked done). Its handoff named the PROPOSAL 008 verdict
fan-in as ripest-when-V008-finalizes — still pending at this wake, so this slice
correctly took the next-ripest standing item (TOP-5 item 3) instead. No
reconciliation debt handed to this slice.

## Handoff → next wake

Inbox first, as always. TOP-5 item 3 is now DONE — the ripest next slice remains
the PROPOSAL 008 verdict fan-in when sim-lab finalizes V008. After that: TOP-5
item 5 (sector-scoped-lean-boot-for-cheap-models, watching fm model-matrix
allocation), and the manager-side watches (theme-schema promotion half-armed;
superbot-idle V006 guardrails). Lane-side, nothing to chase from here: the
remaining channel/role authority work is superbot-next's own sequenced queue
(compensator checklist → role/proof_channel arming → consumer wiring), and
live-bot item 4 is superbot backlog. This card's 💡 (capture-time
already-served grep for "X doesn't exist" claims) is the queued small
improvement.
