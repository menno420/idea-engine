# Session — PROPOSAL 052: the coupon collector's tail — does "almost complete" mean "almost done"? (COMPLETELY-UNRELATED rotation, round 9 closer)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T00:26:42Z (Ideas Lab worker slice — draft the
> COMPLETELY-UNRELATED rotation round-9 closer under standing owner ORDER 003/004.
> Card born in-progress as the designed gate hold; flips complete in this PR's
> final commit once the 💡 slot resolves)

**📊 Model:** Fable (Claude 5 family) · content + outbox proposal only (idea file,
card, index row, outbox append, claim file; no control/status.md or
control/inbox.md writes; no checker or script changes)

## Scope

Draft a genuinely new sim-shaped idea for the COMPLETELY-UNRELATED-domain
rotation slot, round 9 closer, under standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3 ("Rotate lanes deliberately: fleet backlogs →
venture's book/product space → game mechanics → COMPLETELY UNRELATED domains —
I want those too"). Round 9 opened at fleet backlogs with P049 (#358), served
venture with P050 (#371) and game mechanics with P051 (#373), so this slice is
the round-9 UNRELATED **closer** — the last of the four-lane cycle. Confirmed
against the UNRELATED slot's own history: rounds 1–8 were P017 IRV monotonicity
(social choice → V019 null), P024 Braess (congestion routing → V026 null), P028
tournament seeding (Bradley–Terry → V030 approve), P032 Penney's game (pattern
races → V034 approve), P036 secretary/37% (optimal stopping → V047), P040
Schelling (spatial self-organization), P044 checkout pooling (queue discipline),
P048 Parrondo (stochastic ratchets). This head rotates the lane into a NINTH
fleet-external domain — **occupancy & collection problems / the coupon
collector's tail** — deliberately disjoint from all eight prior occupants.

Domain choice: the coupon collector is a canonical counterintuitive
pure-probability result the fleet has never priced, and the "almost complete =
almost done" folk belief is genuinely consumer-relevant (loot-box cosmetics,
gacha banners, card sets, and any fleet "collect all N distinct X" coverage
sweep). The question is answerable in ABSOLUTE exact units: the tail-cost
fraction φ(N) = H_m/H_N is a ratio of harmonic numbers, so the decision arm is
seedless exact `fractions.Fraction` closed form — the strongest hermetic shape
in the P017–P051 battery, no floats, no RNG in the decision path.

Written up as `ideas/fleet/coupon-collector-tail-2026-07-14.md` (probed
single-pass this slice, sim-ready) and appended to `control/outbox.md` as
PROPOSAL 052 (tail verified at HEAD before append: PROPOSAL 051 ·
2026-07-14T00:00:51Z). Homed in `ideas/fleet/` per the `check_sections.py`
non-lane carve-out for cross-cutting heads (flagged in the file's placement
note, exactly as P017/024/028/032/036/040/044/048 did — no ad-hoc section
squatting).

Seed registry: seeds 20261345–348 allocated strictly above the P051 high-water
20261344 (re-swept this session: digit-boundary regex over this tree at HEAD
`a500048` and the sim-lab working copy — idea-engine max 20261344, sim-lab max
20261336; the larger numerals 20261542/20261664/20261833 are Fraction-numerator
digit substrings in sim-lab `results.json`, data not seeds — the
P041/P046/P050/P051 sweep-recipe trap re-confirmed, this block sits below them
with no digit-boundary crossing).

Dedup swept tree-wide at `a500048` (`rg -i
'coupon|collector|occupancy|gacha|loot.?box|birthday|collect.?all|sticker'` with
bootstrap.py/.substrate excluded, plus the sim-lab clone): no proposal P001–P051
and no verdict V001–V061 prices an occupancy/collection/coverage-completion
problem. The 34 grep hits are all incidental — the "occupancy" cluster is
V024/P034's drift-**regime** occupancy (fraction of time a Markov chain sits in
a state, a wholly different meaning); the "collector" hits are P051's
"self-funded collector" (a farm player); and the checkout-pooling idea (P044)
mentions "birthday-collision scheduling" only as a rejected sibling candidate,
which actually confirms the birthday/occupancy family was considered and never
priced. Nearest by counterintuitive-pure-probability are P032 (Penney) and P048
(Parrondo) — zero shared machinery (no harmonic-sum stage-expectation kernel,
no collect-all-distinct absorbing structure); method kin only.

Expected landing DISCLOSED per the P048/P049/P050/P051 closed-form-arm norm:
REJECT at the drafter's exact φ = H_m/H_N (N=20 → ≈0.417, N=50 → ≈0.508, N=100
→ ≈0.565, N=200 → ≈0.612, all ≥ 2/5, 4 of 4), with the sim required to
re-derive from scratch and not trust the disclosure. Falsifiability is real —
the N=20 cell at ≈0.417 sits just above the 2/5 edge, and the APPROVE band 1/5
is reachable via a single-item tail at large N (φ = 1/H_N → small).

## 💡 Session idea

**A future UNRELATED head on the birthday-problem / occupancy collision
probability — the mirror twin of this one.** The coupon collector asks "how
long to fill all N cells?"; the birthday problem asks the dual "how few draws
until a COLLISION — two draws hitting the same cell?", and its own folk belief
("you need ~half the cells' worth of people for a coin-flip collision") is as
wrong in the OTHER direction (√N, not N/2). It surfaced this slice as a rejected
dedup sibling — the P044 checkout-pooling idea already name-drops
"birthday-collision scheduling" as a closed-form candidate it set aside — so
it's a genuinely un-priced, canonical, consumer-relevant head (hash-table load
factors, shard-key collisions, any fleet "will these N random ids clash?"
sizing question), and it reuses THIS head's exact-`Fraction` inclusion-exclusion
CDF kernel almost verbatim, so the drafting cost is low. **Dedup** (this slice,
`rg -i 'birthday|collision|pigeonhole|hash.?collision'` over ideas/ +
.sessions/): the only hit is the P044 set-aside mention — no proposal prices it.
Distinct from THIS head (occupancy-fill vs first-collision are opposite tail
events on the same occupancy structure) and from P048/P032 (no birthday/collision
machinery there at all). A clean round-10 UNRELATED candidate.

## ⟲ Previous-session review

Newest predecessor card
(`.sessions/2026-07-13-proposal-051-chicken-farm-faucet.md`, P051 drafter,
game-mechanics round-9 slot): closed clean and its discipline transferred
directly — its seed-sweep archaeology (the 20261542/20261664/20261833 numerals
are Fraction-numerator data, not seeds — the P046 trap re-confirmed) saved this
slice the same re-derivation, letting the 20261345–348 allocation land in one
pass; the one habit this slice pushes further is the closed-form-arm honesty —
P051's plateau disclosure was numeric-heavy from a deterministic harness, and
this head's φ = H_m/H_N ratio makes the entire decision arm seedless exact
`Fraction`, the cleanest possible form of the same "disclose but don't trust"
norm.
