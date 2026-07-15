# The hint that hides — the world views treat the OPTIONAL max_depth hint as an unvalidated visibility gate: 14 of the 80 valid (hint × depth × record) cells render a miner NOWHERE while the same document ranks them #1, the Deep Diver badge is exact-equality and so non-monotone (digging past the hint LOSES it), and omitting the optional field is strictly safer than supplying it

> **State:** sim-ready
> **Class:** game (pipeline rotation — the standing ORDER 003 GAME-MECHANICS slot, round 15; harvest source: superbot-mineverse, the World flagship web game — its committed world-presentation mechanics (depth ladder, position minimap) and its flagship depth badge priced against the one optional envelope field all three trust without validation)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits mineverse files)
> **Grounding:** https://github.com/menno420/superbot-mineverse@b9ade33ae6019eff45195684fa6fd6f02da4bee0 · fetched 2026-07-15T10:45:57Z
> (FIRSTHAND: read-only public-HTTPS shallow clone per the Q-0272 git transport, the P073/P074 precedent — the SAME pin P073 grounded at this morning; the lane has not moved. Every committed constant and sentence below is quoted from the files at that pin with file:line cites. The sim is fully hermetic: every fixture a pinned constant committed with the sim, zero repo/network reads in the verdict session — the P017–P074 precedent. Dedup-sweep HEADs: idea-engine c1b97be, sim-lab 9e22abb READ-ONLY, fetched 2026-07-15T10:57:11Z.)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation); round 15 opened at fleet backlogs with P073 (#437, merged 2026-07-15T09:59:51Z) and served venture with P074 (#438, merged 2026-07-15T10:32:39Z), so game mechanics is next — this head. Slot spacing history: P020, P023, P027, P031, P035, P039, P043, P047, P051, P055, P059, P063, P067, P071 → P075 (spacing 4). Source rotation inside the slot per the P063/P067/P071 records (gba ×2 r6/r7, superbot ×2 r8/r9, mineverse r10, idle r11, games r12, gba r13, superbot hub r14): round 15 returns to **superbot-mineverse**, undrawn in this slot since round 10, pokemon-mod-lab excluded DARK/private per the standing Q-0260 rule-3 carve-out. Same-round disclosure: P073 (fleet slot, this round) harvested the SAME repo's WRITE contract (docs/mining-write-contract.md + tests/shim/shim_bot.py); this head reads the READ projection (server/views.py + the snapshot schema) — zero shared fixtures, argued in Dedup.

## The committed claims (harvested @ b9ade33)

1. **The hint is committed as OPTIONAL and soft, twice.** `schemas/mining_snapshot.v1.schema.json:24-25`: `max_depth` — "OPTIONAL world-shape hint: deepest reachable depth index. Oracle-confirmed depth bands are 0-3. **Consumers must fall back gracefully when absent.**" — integer, minimum 0, maximum 3, NOT in the envelope's `required`. The contract table says the same (`docs/mining-data-contract.md:39`: "World-shape hint … | no |"). Miner `depth` ("Current depth index", 0–3, REQUIRED) and `record_depth` ("Deepest depth ever reached", 0–3, REQUIRED) are bounded by the SCHEMA, not by the hint: the snapshot schema carries **zero cross-field applicators** (no `if`/`then`/`allOf`/`anyOf`/`oneOf`/`not`/`dependent*` anywhere in the file — verified by keyword sweep at drafting), so `{max_depth: 0, miners: [{depth: 3, record_depth: 3, …}]}` is a fully conforming v1 document, and the committed validator (`server/snapshot_validation.py::validate_snapshot`) accepts it — drafting ran it (all 80 lattice cells below ACCEPTED).
2. **The world views use the hint as a hard render bound.** `server/views.py::build_ladder` (line 216) and `::build_minimap` (line 316) both iterate `for depth in range(max_depth + 1)` — bands/panels exist ONLY up to the hint. `build_views` (lines 633-634) substitutes the schema bound (`depth_max()` = 3) **only when the hint is absent or non-int** ("schema fallback when the hint is absent"), pinned by `tests/test_views.py:568` ("No max_depth hint → the schema's depth bound backstops the ladder").
3. **The repo's own committed doctrine is honest listing.** `build_minimap`'s docstring promises names "**listed honestly, never silently dropped**" (views.py:310-311 — scoped to position-malformed miners, and structurally unable to reach a miner whose band is never rendered); `shape_gear` "renders an honest empty slot **instead of hiding it**" (views.py:113-114); `shape_position` → "an honest 'position unknown' **instead of plotting garbage**" (views.py:155-156). Honest-visibility is the committed house style of this exact file.
4. **The flagship depth badge is exact-equality on the hint.** `earned_achievements` (views.py:446-448): `miner["record_depth"] == max_depth` → `deep_diver`; catalog description "**record depth equals the world's max depth**" (views.py:401-402). Same `max_depth` argument, same unvalidated trust.
5. **Every accepted document is served.** `server/app.py`: the snapshot "is re-read fresh and v1-validated on EVERY request" (line 90; the one load-validate-or-503 path, lines 494-526), and the FLAG-1 ingest seam persists any verified+valid POST for the very next read (`server/ingest.py:25-28`). Schema-valid = rendered. The bot-side exporter that would keep the pair consistent by construction is **unbuilt** (external FLAG 1) — exactly the write-side situation P073 priced, on the read side.
6. **The frontend inherits the clip.** `web/app.js::renderLadder` renders only the served bands ("bands 0–3, current + record markers", line 1183; record chips `"Name · record"` lines 1216-1222); the miner-card depth meter is `(miner.depth / world.max_depth) * 100`% with a falsy-zero guard (line 1173).

## The mechanism (reasoned to its fuller form — Q-0254 duty)

One optional envelope integer drives three deterministic subsystems — band rendering, panel rendering, badge law — and none of the three (nor the validator in front of them) checks it against the per-miner fields it bounds. Enumerate the FULL conforming lattice: hint m ∈ {absent, 0, 1, 2, 3} × depth d ∈ 0..3 × record r ∈ 0..3 = **80 cells**, every one accepted by the committed `validate_snapshot` (ran at drafting). Write m_eff = 3 when absent, else m. Four exact theorems, every numeral RAN live at drafting against the ACTUAL committed views.py + snapshot_validation.py (the V080 live-verify rule; the V084 NO-DERIVED-LITERALS lesson — drafting script ALL PASS, exit 0):

- **T1 — the visibility law and its censuses.** Live chip iff d ≤ m_eff; record chip iff r ≤ m_eff ∧ r ≠ d (the `elif` is per-BAND, so a live miner also gets a record chip at band r — a drafting-run correction to the drafter's first hand-hypothesis, disclosed); minimap presence iff d ≤ m_eff. So a miner is **FULLY INVISIBLE** — no `here` row, no `record_only` row, no minimap `points`, not even minimap `unplotted` — iff d > m_eff ∧ r > m_eff. Exact censuses over the 80 cells: fully-invisible = **(3−m)² per present hint** — {m=0: 9, m=1: 4, m=2: 1, m=3: 0}, **total 14/80**; minimap-invisible = 4·(3−m), **total 24/80**; ghost-only cells (a stale "Name · record" chip at a shallow band is the ONLY trace of a miner whose live position renders nowhere) = (3−m)(m+1), **total 10/80**. All three closed forms matched the exhaustive enumeration exactly.
- **T2 — the badge is non-monotone in digging.** deep_diver ⇔ r == m_eff on all 80 cells (**20/80** earn). Consequences, all enumerated: **12 flip cells** (m ∈ {0,1,2} × d ∈ 0..3) where raising the record from r = m to r = m+1 — digging ONE band deeper — **loses** the badge whose description says "deepest"; **24 overshoot cells** (r > m, hint present) where the record strictly EXCEEDS the world's stated max and the badge is denied; and the m = 0 inversion — in a valid surface-only world the never-dug newcomer (r = 0) EARNS Deep Diver while the r = 3 explorer is denied it.
- **T3 — the composite witness.** One document, ACCEPTED by the committed validator at drafting: m = 2; miner A (d = 3, r = 3, top coins/XP), miner B (d = 2, r = 2). Served result, ran live: A is **#1 on the depth board AND #1 on the coins board** while appearing in **zero** ladder bands and **zero** minimap panels (not even `unplotted`), and A is NOT deep_diver while the strictly shallower B IS. Omitting the hint from the SAME document flips all three at once: A becomes visible, A gains the badge, B loses it. Three served surfaces disagree about who is deepest, inside one response body.
- **T4 — the hint only ever hides.** Over all 64 (m present, d, r) comparisons against the absent-hint twin: visibility(absent) ≥ visibility(m) EVERYWHERE, strictly greater on exactly the 14 fully-invisible cells. The optional field can only remove miners from the world views, never add one — the contract's mandated graceful-degradation path is **strictly safer than the informative path**. (Corollary, frontend reporting rows: the depth meter renders 150% at (d=3, m=2), 300% at (d=3, m=1), and 0% for EVERY miner at m=0, because integer 0 is falsy in `world.max_depth ? … : 0` — a valid schema value silently treated as absent.)

The tension being priced: a repo whose committed house style is honest-listing (claim 3) and whose validator exists to refuse bad documents (claim 5) trusts ONE optional hint, cross-field-unchecked, as a hard visibility gate and an exact badge law — and the committed sample never shows it, because the sample sits at m = 3 where every census term is zero (drafting re-ran the sample: 7 miners, zero drop cells — the fault is LATENT, armed by any m < 3 document the unbuilt FLAG-1 exporter, a torn last-write-wins export (the contract's own Ordering section: "no sequence key", `docs/mining-data-contract.md:193-197`), or any future world-reshape ships).

## Pinned model + margin-0 ledger (V083 discipline)

- **Lattice:** m ∈ {absent, 0, 1, 2, 3} × d ∈ 0..3 × r ∈ 0..3, one miner per document, all other miner fields held at the pinned sample-derived valid values (quoted in the fixture). Multi-miner interactions are linear (per-miner shaping), pinned by the T3 two-miner witness.
- **Laws re-implemented from the pinned quotes:** bands = `range(m_eff + 1)`; `here` on d == band, per-band `elif` record on r == band; minimap panel filter d == band with `points`/`unplotted`; deep_diver r == m_eff; fallback m_eff = 3 iff hint absent/non-int (claims 2, 4).
- **Validator model:** the schema constants verbatim (bounds, required tuples, zero cross-field applicators — the pinned keyword-sweep fact from claim 1); the sim re-derives acceptance of all 80 cells from those constants.
- **Margin-0 ledger (registered knife-edges):** (i) d = m_eff is the LAST visible band — the entire drop census sits one integer past an exact contact; (ii) deep_diver's `==` is itself a two-sided margin-0 law (r = m earns; r = m±1 does not); (iii) at m_eff = 3 the `>=` repair is **byte-identical** to the committed `==` (r ≤ 3 by schema) — today's world sits exactly ON the degeneracy cell where the bug has no observable consequence, which is why the sample calibration cannot see it; (iv) the m = 0 meter row rides the falsy-zero boundary (0 is a valid hint AND JavaScript-falsy).
- **Arms:** **Arm A** — the closed forms ((3−m)², 4·(3−m), (3−m)(m+1), the iff-laws, 20/12/24 badge censuses). **Arm B** — independently-written exhaustive enumerator over the 80 cells (dict-of-cells, no shared code with Arm A); exact integer equality with Arm A required on every census and every cell verdict. **Arm F** — the committed functions re-implemented VERBATIM from the pinned source quotes (band loop, elif, minimap filter, badge check, fallback), run over all 80 cells; must equal Arm B cell-by-cell (at drafting this leg ran the ACTUAL committed module — all matched). **Arm R** — seeded random fully-valid documents (k ∈ 1..7 miners, uniform valid fields), REPORTING-ONLY rates of drop/ghost/badge events under uniform sampling. Seeds **20261670–672** read by Arm R only; **aux 20261673 NEVER read** (the P054–P074 aux convention).
- **Determinism:** Arms A/B/F are seedless and exact; two process runs must be byte-identical.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** ("the hint is an unpriced trust — the world views and the badge law need either a conformance rule or an overflow rendering") iff ALL of: **(R1)** the fully-invisible census over the accepted lattice is ≥ 1 (expected exactly 14) AND every such cell is verified absent from `here`, `record_only`, `points`, AND `unplotted` — genuinely unlisted anywhere in the served world views; **(R2)** the badge non-monotonicity census is ≥ 1 (expected exactly 12 flip cells), with the overshoot-denial census attached (expected 24); **(R3)** hint-domination holds (T4: absence ≥ presence on all 64 comparisons, strict somewhere) — supplying the optional field is never safer and somewhere strictly worse.
- **INVALID** on any gate failure (G1–G6 below).
- **APPROVE** ("the committed pair already enforces or renders cross-field consistency") iff the fully-invisible census = 0 AND the flip census = 0 over the accepted lattice — mutually exclusive with REJECT by arithmetic.
- **NULL** otherwise, on named axes: **(n1)** the conformance axis — if the pinned schema or validator text is found to carry a cross-field rule binding d, r ≤ m (the fixture carries the schema verbatim and the applicator inventory; the sweep is the check), the drop cells are non-conforming input and the finalized finding is the corrected conformance boundary; **(n2)** the acceptance axis — if the sim's re-derived validator disagrees with the pinned validator semantics on any lattice cell, the corrected acceptance table IS the finding; **(n3)** the intent axis — if a committed mineverse sentence is produced ratifying the hint as authoritative-not-hint (none found at drafting; the fixture carries the claim-1 and claim-3 quotes to check against), direction signed: REJECT would downgrade to a documentation gap on the same numbers, disclosed not ruled. Every NULL is a finalized, citable finding with its exact tables, never a re-run request.

## Gates (run INVALID on any failure)

- **G1 twin arms:** Arm B equals Arm A on every census, every closed form, every cell verdict (exact integers); Arm F equals Arm B cell-by-cell on all 80 × 4 outputs.
- **G2 acceptance:** all 80 lattice cells + the T3 witness pass the re-derived schema check (bounds, required fields, types), and the applicator inventory of the pinned schema is empty of conditional/cross-field keywords.
- **G3 censuses:** fully-invisible {9, 4, 1, 0} = (3−m)², total 14; minimap-invisible 24 = 4·Σ(3−m); ghost-only 10 = Σ(3−m)(m+1); badge censuses 20 / 12 / 24; all exact.
- **G4 laws:** live ⇔ d ≤ m_eff; ghost ⇔ r ≤ m_eff ∧ r ≠ d; map ⇔ d ≤ m_eff; deep_diver ⇔ r == m_eff; T4 domination on all 64 comparisons with strictness exactly on the 14.
- **G5 hand world (pencil-checkable, derived in this file):** m = 0, four miners (d, r) = (0,0), (1,0), (2,2), (3,3) → ONE band; P(0,0) live; Q(1,0) ghost chip "Q · record" only; S(2,2) and T(3,3) fully invisible; deep_diver = {P, Q} (the never-dug pair earns "deepest", the two divers are denied). Five facts, checkable by eye against the four laws.
- **G6 consequence battery (falsifiability live, numbers RAN):** (a) the conformance-applicator world (require d ≤ m ∧ r ≤ m when the hint is present) shrinks the accepted lattice 80 → **46** cells (16 absent-hint + Σ(m+1)² = 30) with every invisibility census ZERO and zero surviving flip pairs — the REJECT flips to APPROVE, live; (b) the overflow-band render world (bands = max(m_eff, deepest miner d or r)) gives invisible = 0/80 — R1 flips; (c) the deep_diver-as-`>=` world earns on 44/80 cells with ZERO non-monotone flips and is **byte-identical to the committed `==` at m_eff = 3** — R2 flips with today's sample semantics provably untouched.

## Expected landing (DISCLOSED per the P048–P074 exact-arm norm)

**REJECT**, with every registered numeral produced by the drafting script this session against the actual committed code (ALL PASS, exit 0): R1 census 14 (per-hint {9, 4, 1, 0}), all 14 verified unlisted on all four surfaces; R2 flips 12 + overshoot 24 + the m = 0 inversion; R3 domination with strictness on exactly the 14. Falsifiability is live and named: all three G6 repair worlds flip the corresponding clause, and the n1/n3 axes are genuine outs (a cross-field applicator or an authoritative-hint sentence anywhere in the pinned tree kills the head — drafting swept and found neither). The REJECT indicts the **unvalidated cross-field trust and the exact-equality badge law** — never the hint field itself (world shape is real data), never the fallback (correct and pinned by the repo's own test), never the game.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

- **REJECT →** paste-ready structured choice to the manager for the mineverse lane, recommendation first per Q-0263.2: **(a, recommended) enforce the cross-field rule at the validator** — reject `depth > max_depth` or `record_depth > max_depth` when the hint is present (one check in `snapshot_validation.py`'s semantic layer + a 400 reason; the write/ingest seam already refuses invalid documents, so this closes the corridor at the door) AND render an overflow band in `build_ladder`/`build_minimap` (`range(max(max_depth, max miner depth/record) + 1)`) so even a pre-fix document can never hide a miner — G6a+G6b numbers attached (46-cell lattice, all censuses zero); **(b)** treat the hint as display-only everywhere: overflow bands (G6b) + `deep_diver` on `record_depth >= max_depth` (G6c: zero flips, byte-identical today) — no validator change, exporter freedom preserved; **(c)** status quo + a contract sentence making cross-field consistency the EXPORTER's conformance duty ("miners never exceed `max_depth` when present"), testable in FLAG-1's vendor-pinned contract file before it is ever built — the cheapest ink, the trust stays. The ruling conditions on the committed code @ b9ade33; a later change to the band loops, the badge law, or the schema means re-run, not reuse.
- **APPROVE →** the committed pair stands, priced; note filed.
- **NULL →** the named axis's corrected table, attached, final.

## Dedup

Nearest priors, argued distinct: **P045 → V056** (same repo — the READ contract's staleness CONSTANT, `generated_at` timing; no visibility, no lattice, no badge). **P055 → V066** (same repo, same FILE — the Coin Magnate threshold vs superbot's faucet; its only deep_diver contact is a static REPORTING row, verbatim "deep_diver saturation note (record_depth ∈ {0..3} caps at the contract's own max — two of seven sample miners already hold it)" — a saturation observation at m = 3, never the equality law, never non-monotonicity, never the visibility clip, never a decision object; zero shared fixtures — P055's decision fixtures are the faucet `_DAILY_TIERS` and coin thresholds, this head's are the band loops and the schema bounds). **P073 → in flight** (same repo, same ROUND — the WRITE contract's rate-limit tiers, `docs/mining-write-contract.md` + `shim_bot.py`; disjoint documents, disjoint functions, disjoint theorems; shared only the repo pin b9ade33, disclosed). **P071 → V084** (superbot hub fishing — record LADDERS under quantization; "record" there is a maximum over TIME on a weight grid, here "record_depth" is a field VS a cross-field gate — no shared machinery). **P063 → V074** (games menu prefix law), **P067 → V080** (gba stale-ink), **P059 → V071** (idle prestige) — different repos entirely. Corpus grep at HEAD c1b97be (`rg -i 'max_depth|minimap|visibility|world-shape|deep.diver'`, bootstrap.py/.substrate excluded): hits only P055's reporting row (above), P073's unrelated write-contract text, and archive echoes — no proposal P001–P074 and no sim-lab verdict (swept READ-ONLY @ 9e22abb) prices a cross-field visibility lattice, an optional-field trust boundary, or a non-monotone badge law. The pipeline's first render-clip head and its first hint-domination theorem.

## Model basis (declared model-dependence — the P024 discipline)

The lattice enumerates DOCUMENTS the committed validator accepts — the conformance boundary — not documents a truthful atomic exporter would emit: with a single-oracle atomic export, d ≤ m holds by construction and every drop cell is unreachable; the priced object is the committed pair's behavior over its own accepted input space, exactly the boundary the unbuilt FLAG-1 exporter, the sequence-key-free last-write-wins ingest (claim 5), and any future world reshape will exercise first. The engagement boundary is explicit: "a top-ranked miner renders nowhere and the deepest digger loses the deepest badge" is the priced fact; how much that matters to players is the lane owner's judgment. Frontend rows (meter percentages, record-chip copy) are REPORTING — the decision numbers are all server-side. Multi-miner documents shape per-miner (verified by the two-miner witness); no interaction terms exist to model.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — corpus grep at HEAD
> `c1b97be` (pattern above, kit machinery excluded) + sim-lab swept READ-ONLY at
> `9e22abb`: the only contacts are P055's static saturation row and P073's
> same-repo-different-document write head, both argued in Dedup; (b) **kill test
> NOT triggered** — no prior proposal, verdict, idea file, or mineverse session-card
> 💡 prices this head (the mineverse hats card's 💡 is the display-name JOIN
> collision — a different fragility in a different function, and its OWN recorded
> idea, deliberately not drafted here); (c) **feasibility + every registered number
> checked LIVE** (V080 rule, V084 lesson — scratchpad `draft_p075.py`, ALL PASS,
> exit 0, running the ACTUAL committed views.py + snapshot_validation.py @ b9ade33):
> the 80-cell acceptance sweep, the four iff-laws, the censuses 14/24/10 with their
> closed forms (3−m)² / 4(3−m) / (3−m)(m+1), the badge censuses 20/12/24 + the
> m=0 inversion, the T3 witness (accepted; #1 on two boards; zero world-view rows;
> badge inverted; absent-hint triple flip), T4 domination (64 comparisons, strict
> exactly on the 14), the G5 hand world, the three G6 repair worlds (46-cell
> lattice / 0-census / 44-earn-0-flip with the m_eff=3 byte-identity), and the
> meter rows (150%, 300%, falsy-0). One drafting-run correction disclosed: the
> drafter's first hand-hypothesis for the ghost law (`elif` read as per-miner) was
> WRONG — the enumeration corrected it to per-band (r ≤ m_eff ∧ r ≠ d), which is
> exactly what the live-verify rule exists to catch. Seeds 20261670–673 swept
> collision-free at HEAD `c1b97be` (registered prior 20261660–663 = P074/V087's
> set; 20261664 is a standalone DATA numeral per the recorded discrimination rule,
> NOT a seed; the gap 20261665–669 is the disclosed in-flight buffer).

**1. What is this really?** A pre-registered EXACT MEASUREMENT of the trust
boundary between one optional envelope field and the three committed subsystems
that consume it: the full 80-cell conforming lattice enumerated against the
committed band loops, badge law, and validator, with closed-form censuses as the
ruling, REJECT-first bands fixed before any code, twin/fidelity arms, and seeded
legs demoted to reporting.

**2. What is the possibility space?** (i) Don't run it — the round-15 game slot
goes unserved and the World flagship's world views keep an unpriced trust that its
unbuilt exporter will inherit blind. (ii) A prose note "validate max_depth
cross-field" — states the direction, measures nothing, misses the domination
theorem, the non-monotone badge, the ghost-chip census, and the byte-identity
fact that makes fix (c) free today. (iii) Price only the badge — misses that the
same integer also hides miners entirely. (iv) MC-only — seed noise on numbers
that are exact small integers (the V065/V067 lesson); MC is demoted to Arm R.
(v) This head: exact lattice as the ruling, three named repair worlds with their
numbers already run. (vi) Over-scope (live exporter telemetry, multi-guild
envelopes, the leaderboard tie-order question, the hats name-join fragility) —
each named, none in scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~120-line stdlib file: a document factory over the pinned
valid-field values, a re-derived bounds/required checker, the four laws from the
pinned quotes, an exhaustive 80-cell loop, three repair-world variants, and the
closed-form comparators — yielding every decision number in milliseconds, cold,
no dependencies, byte-identical across runs.

**4. What breaks it? (assumptions made explicit)** (a) A cross-field applicator
the keyword sweep missed → n1, and the corrected conformance boundary is the
finding. (b) A validator-semantics divergence between the sim's re-derived
checker and the pinned module → n2, corrected acceptance table. (c) An
authoritative-hint sentence somewhere in the pinned tree → n3, direction signed.
(d) The truthful-exporter objection — priced in Model basis: the lattice is the
ACCEPTED input space, and the repo's own doctrine (validate everything, degrade
honestly, "never silently dropped") is the standard the head measures against.
(e) A drafter hand-fact error — the ghost-law correction already demonstrates
the failure mode AND the recovery: laws are gates, and n-axes turn a wrong hand
claim into a finalized corrected law.

**5. What does it unlock?** The round-15 game slot served with the pipeline's
first visibility-lattice head; three standalone keepers (the hint-domination
theorem — an optional field that can only hide; the (3−m)² drop census pattern
for any band-clipped render; the exact-equality-badge non-monotonicity law); a
three-option repair menu with every consequence number already computed,
including one repair (deep_diver `>=`) proven byte-identical to today's
behavior; and the transferable audit — every fleet surface that renders a
collection clipped to a separately-supplied bound (pagination caps, tier caps,
level caps vs entity levels) inherits the same silent-drop lattice, now priced.

**6. What is the cheapest experiment that decides it?** The G5 hand world: one
band, four miners, five facts checkable by eye — a surface-only world where the
two actual divers are invisible and the two never-dug miners hold the "Deep
Diver" badge. If a reader doubts the head, that single pencil check settles the
mechanism in thirty seconds.

**7. What would make this a mistake to run?** If a cross-field rule existed
(drafting swept the schema, the validator, and the contract — none), if the head
duplicated a prior (corpus + sim-lab greps clean; the two same-repo contacts are
argued distinct), or if the disclosed REJECT made the run theater. It does not:
the value is the hermetic independent re-derivation, the exact censuses no doc
states, the domination theorem, the three repair worlds with their numbers, and
two genuine non-REJECT outs (n1/n2 conformance surprises; the G6 worlds show
APPROVE is one applicator away).

**8. How will we know it worked?** A committed sim-lab report with: the 80-cell
table (four outputs per cell), the census tables with closed-form matches, the
badge law + flip/overshoot/inversion tables, the T3 witness transcript, the T4
domination table, the G5 hand-world check, the G6 repair-world numbers, twin-arm
and fidelity equality notes (two process runs byte-identical), Arm R's seeded
reporting rates, and the verdict token against the pre-registered bands. A clean
run reproduces {14, 24, 10, 20, 12, 24, 46, 44, 0} from scratch — or disagrees
and pins the drafter's error, which the pre-registered rule then rules on
honestly (n2/n4-style axes exist for exactly that).

**Recommendation: sim-ready**
