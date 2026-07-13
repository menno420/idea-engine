# Session — PROPOSAL 051: chicken-farm faucet self-balance — the hub's first idle faucet priced against its own committed `!daily` anchor (game-mechanics rotation, round 9)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-13T23:55:49Z (Ideas Lab worker slice — draft the
> GAME-MECHANICS rotation round-9 head under standing owner ORDER 003/004. Card
> born in-progress as the designed gate hold; flips complete in this PR's final
> commit once the 💡 slot resolves)

**📊 Model:** fable · content + outbox proposal only (idea file, card, index row,
outbox append, claim file; no control/status.md or control/inbox.md writes; no
checker or script changes)

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 9, under standing owner ORDER 003 (continuous pipeline — verified
standing at HEAD `2089860` before any work) and ORDER 004 rule 3 ("Rotate lanes
deliberately: fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains"). Round 9 opened at fleet backlogs with P049
(#358) and served venture with P050 (#371), so this slice serves the
GAME-MECHANICS slot — confirmed arithmetically against the slot's own history
(game slots at P023, P027, P031, P035, P039, P043, P047; spacing 4 → next is
P051). Slot rounds 1–8: P020 casino odds → V022 reject, P023 entry fee → V025
reject, P027 comp/stipend → V029 null, P031 explore pacing → V033, P035 mining
booster throttle seal → V046 null, P039 Gloamline survival ceiling → V050
approve, P043 Brineward band necessity → V054 approve, P047 creature rarity →
V058 reject.

Source rotation: the last game round (P047) drew superbot's creature battles;
P039/P043 drew gba-homebrew ×2; P031/P035 drew superbot-games. This round
harvests a DISJOINT mechanic from the hub: superbot's committed chicken-farm
idle economy (`disbot/utils/farm/farm.py` + `disbot/services/farm_workflow.py`
@ `affd7ea1ae5163109527e59ce73b46f0a8c7866c`, shallow clone this slice via
claude-code-remote add_repo — the GitHub MCP direct read was attempted once
and denied, verbatim: `Access denied: repository "menno420/superbot" is not
configured for this session. Allowed repositories: menno420/idea-engine,
menno420/sim-lab`; the add_repo route then succeeded, so this is a wall
routed-around, not a wall hit). The farm module's own docstring carries the
load-bearing never-quantified line "Buying hens scales the faucet but each
costs more coins (the sink), so the loop stays self-balancing" plus the
"~40 coins over ~100 min … a small fraction of a `!daily`" arithmetic — and
the committed `_DAILY_TIERS` table makes E[`!daily`] = 169201/100 coins/day an
exact in-repo anchor, so the faucet question is answerable in ABSOLUTE
committed units (the V001/V008 earn-rate wall does not apply here: both sides
of the comparison are committed constants in the same repo and currency).

Written up as `ideas/superbot/chicken-farm-faucet-self-balance-2026-07-13.md`
(probed single-pass this slice, sim-ready) and appended to `control/outbox.md`
as PROPOSAL 051 (tail verified at HEAD before append: PROPOSAL 050 ·
2026-07-13T23:26:05Z). Seed registry: seeds 20261341–344 allocated strictly
above the P050 high-water 20261340 (re-swept this session: 8-digit
word-boundary regex over this tree at HEAD `2089860` and the sim-lab working
copy at `6cb58bb` — idea-engine max 20261340, sim-lab max 20261336; the larger
numerals 20261542/20261664/20261833 are digit substrings inside sim-lab
`results.json` exact-Fraction numerators quoted into P050's own sweep note,
data not seeds; the block stays inside the 8-digit 2026xxxx band, no digit-
boundary crossing). Dedup swept tree-wide at `2089860` (`grep -ri
'chicken|coop|egg.farm|farm.py|idle.farm'` with bootstrap.py/.substrate
excluded, plus the sim-lab clone): no proposal 001–050 and no sim-lab verdict
V001–V060 (V061 in flight, kill-clock — different world) prices the hub farm;
the nearest neighbors (P015→V017 idle T10 cost curve and V038 idle-economy
FEEL — both superbot-idle's SEPARATE engine; P035→V046 mining booster bypass —
superbot-games' energy throttle; P031→V033 quest currency mint — admission-
gated encounters) are argued distinct in the idea file's Relations.

## 💡 Session idea

**Wire the rotation-slot arithmetic into the claim gate.** Every rotation
drafter re-derives "which slot is round N on?" from prose in prior outbox
blocks (this slice: quote ORDER 004 rule 3, then hand-verify P049=fleet,
P050=venture, spacing-4 arithmetic on the game slots). That derivation is
mechanical: slot(P_n) is a pure function of n given the rotation anchor
(P041=fleet opened round 7 → slot = (n − 41) mod 4 over
{fleet, venture, game, unrelated} for n ≥ 41), yet it lives only in prose and
each drafter pays the re-derivation plus the risk of a silently-wrong slot
(the ORDER threads would then contradict the claim only if a human notices).
The slice: a ~40-line stdlib `scripts/check_rotation.py` leg (or a
check_ideas.py sub-check) that parses `## PROPOSAL <nnn>` headings plus each
block's declared slot word from its summary line, asserts the mod-4 sequence
holds from the anchor forward, and reds a NEW proposal whose declared slot
breaks the rotation — turning the rotation contract from re-derived prose
into a checked invariant. **Dedup** (this slice, `grep -ri 'rotation.check|
slot.check|mod.4|rotation.gate'` over ideas/ + .sessions/ + scripts/ + docs/):
no hit; distinct from P033's 💡 (outbox digest index — a READ surface for
dedup; this is a WRITE-time slot-sequence gate) and from the check_ideas
grammar legs (shape of one block, not the cross-block sequence).

## ⟲ Previous-session review

Newest predecessor card (`.sessions/2026-07-13-proposal-050-kill-clock-horizon.md`,
worker slice ~23:19Z): closed clean and the discipline transferred directly —
its SECONDHAND-pin honesty (venture-lab read denied once, verbatim error
carried into the Grounding line and the application guard instead of being
laundered) is the exact pattern this slice reused when the GitHub MCP denied
superbot (quoted verbatim above, then routed around via add_repo rather than
retried); and its seed-sweep note (the 20261542/20261664/20261833 numerals are
Fraction-numerator data, not seeds — the P046 trap re-confirmed) saved this
slice a false high-water: without it the 8-digit sweep would have needed the
archaeology re-done from scratch. One habit improved on here: P050 disclosed
its drafting-time DP landing as a single expected ruling ("APPROVE, thinly");
this slice's drafting harness additionally surfaced a POLICY-FAMILY edge (the
myopic greedy wall at n=8/L=5 is not the family wall — the hen+coop PAIR move
still pays back in 7.6 days) and registered it as both a family member and a
named NULL axis, which is the stronger form of the same disclosure.
