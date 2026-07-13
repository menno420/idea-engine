# Session — PROPOSAL 045: mineverse snapshot stale-indicator threshold (fleet-backlogs rotation, round 8)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-13T20:16:50Z (Ideas Lab worker slice — draft the
> FLEET-BACKLOGS rotation round-8 head under standing owner ORDER 003. Card born
> in-progress as the designed gate hold; flips complete in this PR's final commit
> once both checkers verify green and the 💡 slot resolves)

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
high-water 20261316 (re-swept: outbox + tree at HEAD `0cad099` + sim-lab clone
@ `692fcf1` — nothing higher anywhere).
