# Session — PROPOSAL 055: badge saturation — does the mineverse achievement catalog's Coin Magnate line survive the hub's own committed daily faucet, or is it an account-age badge? (GAME-MECHANICS rotation, round 10)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-14T02:17:36Z (Ideas Lab worker slice — draft the
> GAME-MECHANICS rotation round-10 slot under standing owner ORDER 003/004. Card
> born in-progress as the designed gate hold; flips complete in this PR's final
> commit once the 💡 slot resolves)

**📊 Model:** fable-family · content + outbox proposal only (idea file, card,
index row, outbox append, claim file; no control/status.md or control/inbox.md
writes; no checker or script changes; nothing in sim-lab, superbot-mineverse,
or superbot)

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 10, under standing owner ORDER 003 (continuous pipeline) and ORDER 004
rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's book/product
space → game mechanics → COMPLETELY UNRELATED domains"). Round 10 opened at
fleet backlogs with P053 (#379) and served venture with P054 (#382), so game
mechanics is next; the slot's own spacing-4 history (P023, P027, P031, P035,
P039, P043, P047, P051 → P055) confirms.

Harvest source: **superbot-mineverse, read FIRSTHAND this session** —
`add_repo` + read-only shallow clone pinned at HEAD
`b983291cd9fc4b0d037a25a139c7ef5991e1236f`; the anchor repo **superbot** also
read FIRSTHAND (GitHub-MCP direct read denied once, verbatim in the idea
file's Grounding header; the add_repo clone route then succeeded — the P051
precedent) at HEAD `34775943da081dd0a1dc7cf858efc0889726fcf6`. Harvested
head: the mineverse achievement catalog (`server/views.py` — the repo's only
committed game-mechanic constants: `COIN_MAGNATE_THRESHOLD = 10_000`,
`PACKRAT_THRESHOLD = 200`, five more), whose own calibration comments claim
per-badge discrimination ("some miners hit it … and some don't"), judged on
the SHARED wallet (`docs/mining-data-contract.md`: `coins` is mutated only by
`economy_service`) — never priced against the hub's committed faucet
`_DAILY_TIERS` (E[`!daily`] = 169201/100 coins/day exactly, the P051/V062
anchor, re-read firsthand at `3477594`).

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot-mineverse/badge-saturation-coin-magnate-2026-07-14.md` + the
`ideas/superbot-mineverse/README.md` index row, and the `control/outbox.md`
PROPOSAL 055 append. Seeds 20261357–360 strictly above the P054 high-water
20261356.
