# Session — PROPOSAL 045: mineverse snapshot stale-indicator threshold (fleet-backlogs rotation, round 8)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-13T20:16:50Z (Ideas Lab worker slice — draft the
> FLEET-BACKLOGS rotation round-8 head under standing owner ORDER 003. Card born
> in-progress as the designed gate hold; flipped complete in this PR's final commit
> at 2026-07-13T20:26:06Z)

## Scope

Draft a genuinely new sim-shaped idea for the FLEET-BACKLOGS rotation slot, round 8,
under standing owner ORDER 003 (continuous pipeline — verified open and standing at
HEAD `0cad099` before any work) and ORDER 004 rule 3's rotation ("fleet backlogs →
venture's book/product space → game mechanics → COMPLETELY UNRELATED domains").
Round 7 closed fully served (P041 fleet-backlogs → P042 venture → P043 game
mechanics → P044 unrelated), so round 8 reopens at fleet backlogs and this slice
serves it. Verified before claiming: `control/claims/` carries no P045 claim and
the open-PR list is empty at HEAD (the parallel V055 intake claim rides sim-lab,
different world).

Harvest source rotates to a SEVENTH repo for the slot, and the first untapped by
ANY prior proposal: `menno420/superbot-mineverse` @ live HEAD
`ae98dd094100f7b864f2c36b91494c8fb2cd1f31` (shallow clone, ls-remote-verified).
The head: the mining snapshot READ contract's stale-indicator rule
(`docs/mining-data-contract.md` § Delivery expectations) — 60 s target push
cadence, "default suggestion: 3 missed cycles ≈ 180 s" before the frontend stops
presenting old numbers as live. The threshold is the contract's own decide-and-flag
constant, never priced on its two named failure axes (false-stale cry-wolf vs
outage detection latency). Idea file
`ideas/superbot-mineverse/snapshot-stale-indicator-threshold-2026-07-13.md`
(probed single-pass this slice, sim-ready), appended to `control/outbox.md` as
PROPOSAL 045. Seed registry: seeds 20261317–320 allocated strictly above the P044
high-water 20261316 (re-swept three surfaces: outbox + tree at HEAD `0cad099`,
`rg -o -g '!bootstrap.py' -g '!.substrate' '202613[0-9][0-9]'` maxing at 20261316,
AND a fresh sim-lab shallow clone at live HEAD `692fcf1` — same maximum).

**📊 Model:** `fable-5` (family-level self-report from this session's own harness,
per ORDER 001 / Q-0262 — never copied from a schedule surface) · content + outbox
proposal only (idea file, card, section index row, claim, outbox append; no product
code, no control/status.md or control/inbox.md writes; no sim-lab writes — the V055
verdict session runs parallel there and its claim
`control/claims/2026-07-13-verdict-055.md` is untouched)

## 💡 Session idea

**Add a hedge-word sweep to the fleet-backlogs harvest router: binding
contracts/design docs carry the slot's best sim heads as HEDGED CONSTANTS, and no
backlog index ever lists them.** Measured this slice, not speculated: two prior
surveys had already dismissed superbot-mineverse as sim-dry (P025's slot survey
"mineverse SECTION COMPLETE"; P041's Relations dropped its founding-day backlog @
`f79d0ae` as "all UI/refactor/cosmetic or externally-blocked") — and both were
right about the surfaces they read, because the head that became P045 never lived
in any backlog: it sits inside a BINDING contract as a self-confessed guess
("default suggestion: 3 missed cycles ≈ 180 s"), exactly as P041's own head sat
inside project docs as "leave yourself margin" (hedge phrase, no number). Two
consecutive fleet-backlog heads found by hedge language, zero found by backlog
indexes, is a pattern: the slot's sourcing step should grep the target repo's
binding/design docs for hedge markers (`default suggestion`, `leave yourself
margin`, `roughly`, `sounds right`, `TBD`, `placeholder`, `provisional`) BEFORE
walking its ideas/ index — a one-line rg over a shallow clone, zero new tooling.
Dedup (this slice, at HEAD `0cad099`): P039's card 💡 is a machinery index (where
the ENGINES are — this is where the QUESTIONS are); P035's 💡 is a seed registry;
P044's 💡 is outbox rollover; `rg -i 'hedge' -g '!bootstrap.py' -g '!.substrate'`
returns only incidental prose — no prior 💡 or head proposes harvest-by-hedge-marker.

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-044-checkout-pooling.md`,
worker slice ~19:42Z): closed clean, and its rituals transferred verbatim here
(blob-pinned `idea:` link — P045's outbox append pins the `62821c5` idea-doc
commit; seed high-water re-sweep — carried forward and EXTENDED per its own
spirit: P044 swept this tree, this slice added the sim-lab clone as a third
surface and confirmed the same 20261316 maximum). Its 💡 (outbox rollover for
CLOSED blocks — the file outgrowing its own tooling) gained fresh evidence this
slice without any new failure needed: the outbox is now 368,007 bytes at HEAD
(+~8 KB in ~35 min of normal operation) and this session read it exclusively via
shell slicing on the dispatch brief's own warning — the workaround it predicted
every consumer would need is now standard operating procedure, which is the
strongest argument that the rollover head should graduate from card-💡 to idea
file soon. One thing visible only from here: its ⟲ predicted the claim-corpse
census would run "always one slice behind" — confirmed: `control/claims/` at HEAD
still holds the P043 AND P044 claim files post-merge (census n = 2 + the backfill
claim), and this scope-limited slice did not prune them either (decide-and-flag:
noted here rather than silently expanding a worker diff; the standing-prune-step
suggestion in the P044 card remains unserved and is the right fix).

## Close-out

All pieces landed before this flip: card born in-progress + claim @ `937c522`,
idea doc + section index row @ `62821c5`, PROPOSAL 045 outbox append @ `23d4af3`
(idea: link pinned to the `62821c5` blob; `scripts/check_ideas.py --outbox` exit
0 re-verified after the append), PR #343 opened READY immediately after the push
(never draft; merge left to the enabler workflow, no agent merge; PR activity
subscribed same minute). Rotation verified at HEAD before drafting: ORDER 004
rule 3 quoted verbatim in the idea doc's Origin; P041/P042/P043/P044 blocks
self-declare round 7's four slots served. This flip is the branch's last commit;
both checkers (`python3 bootstrap.py check --strict`, `python3
scripts/check_ideas.py --outbox`) run green at flip time or this commit does not
push.
