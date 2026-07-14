# Session — PROPOSAL 055: badge saturation — does the mineverse achievement catalog's Coin Magnate line survive the hub's own committed daily faucet, or is it an account-age badge? (GAME-MECHANICS rotation, round 10)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T02:17:36Z (Ideas Lab worker slice — draft the
> GAME-MECHANICS rotation round-10 slot under standing owner ORDER 003/004. Card
> born in-progress as the designed gate hold; flipped complete in this PR's final
> commit at 2026-07-14T02:27:02Z once the 💡 slot resolved)

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

## 💡 Session idea

**A read-projection repo's game surface is its CONSUMER-side constants — the
harvest recipe is the pairing, not the repo.** Mineverse looked "thin" as a
game-mechanics source: every rate lives bot-side, and its only committed game
constants are display-layer thresholds (the achievement catalog). The head
only became decidable by PAIRING the consumer-side threshold with the
producer repo's committed faucet (`COIN_MAGNATE_THRESHOLD = 10_000` ×
`_DAILY_TIERS`, both pinned firsthand) — and that pairing is a reusable
harvest recipe for every projection/viewer lane the fleet runs: websites'
arcade panels, product-forge's viewers, any future "reach N currency" badge
or unlock rendered over someone else's economy. The transferable rule: when
a repo renders another repo's state, harvest its thresholds and price them
against the producer's committed rates — the pair is sim-shaped even when
neither repo alone is. Free corollary this slice: re-reading the anchor at
its CURRENT head (`3477594`, byte-identical to P051's `affd7ea` quote) is
zero-cost drift detection on the anchor itself. **Dedup** (this slice, `rg
-i 'consumer-side constant|threshold.*faucet pairing|projection-repo
harvest' ideas/ .sessions/` kit-excluded): no card or idea names the
consumer-threshold × producer-faucet pairing recipe.

## ⟲ Previous-session review

Newest predecessor card
(`.sessions/2026-07-14-proposal-054-illustration-gate.md`, P054 drafter,
round-10 VENTURE slot): closed clean and paid forward twice here — its
seed-sweep line (high-water 20261356, the Fraction-numerator-substring trap
re-documented) let this slice land 20261357–360 in one pass, and its 💡
(walls are session-scoped; re-probe denials, never inherit them) got a
refining datapoint this session: the superbot GitHub-MCP denial DID recur
verbatim (it is a scope POLICY, standing by design), while the add_repo
clone route succeeded immediately — so the denial ledger should record the
ROUTE, not just the repo. P054's "re-attempt every wall" holds, and this
session's split (route-scoped standing wall vs session-scoped transient
wall) is the next precision step its own 💡 asked for. One push further this
slice: P054 disclosed which invented pins already land REJECT-side as
fragility axes; this head did the same for its σ = 9/10 flip AND shipped the
drafting grid that shows exactly where the ruling survives (the p = 1/10
cell) — fragility disclosure is becoming the slot's standing norm, which is
what makes REJECT-first registration honest.
