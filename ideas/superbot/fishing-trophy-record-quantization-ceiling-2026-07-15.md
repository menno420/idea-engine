# The personal best is a finite resource: the committed 2-decimal weight grid gives every species a record ladder with a reachable ceiling, the modal catch's chase provably completes in ~148 casts, and no committed knob can extend it

> **State:** sim-ready
> **Class:** game (pipeline rotation — the standing ORDER 003 GAME-MECHANICS slot, round 14; harvest source: the superbot hub's own fishing subsystem — the shipped trophy-record retention hook priced against the committed weight-quantization law it rides on)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits any other repo)
> **Grounding:** https://github.com/menno420/superbot@f8e2313a087e18cb32e88269d468b0b30a41fad9 · fetched 2026-07-15T08:34:14Z
> (FIRSTHAND: every committed constant below is read from superbot's files at that pin on a read-only shallow clone and cited file@sha; the sim is fully hermetic — every fixture a pinned constant committed with the sim, zero repo/network reads in the verdict session — the P017–P070 precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains"); round 14 opened at fleet backlogs with P069 (#432) and served venture with P070 (#434, merged 2026-07-15T08:16:04Z), so game mechanics is next — this head. Slot spacing history: P020, P023, P027, P031, P035, P039, P043, P047, P051, P055, P059, P063, P067 → P071 (spacing 4). Source rotation inside the slot per the P063/P067 records (gba ×2 r6/r7, superbot ×2 r8/r9, mineverse r10, idle r11, games r12, gba r13): round 14 returns to the superbot hub, undrawn since round 9, with pokemon-mod-lab excluded DARK/private per the standing Q-0260 rule-3 carve-out. Within the hub the mechanic is deliberately DISJOINT from every prior hub draw: P047 priced creature BATTLE budgets (V058), P051 the chicken-farm FAUCET (V062), P020/P023/P027 the casino SINK (V022/V025/V029), P003/P016 encounter SPAWNS (V001/V018) — no prior head touches the fishing weight roll, the trophy/PB record process, or any quantization interaction anywhere in the pipeline.

## The committed claims (harvested @ f8e2313)

1. **The retention hook is committed twice, verbatim.** `disbot/utils/fishing/weight.py` @ f8e2313 opens: "Per-catch weight roll — pure, the basis of the trophy-records goal. The owner design lists **'trophy records per species (biggest caught)'** as a cheap long-tail retention goal" … "a lucky heavy one becomes a personal best worth chasing"; the spread comment adds "so any species can occasionally produce a personal-best lunker". The design doc `docs/planning/fishing-minigame-design-2026-06-22.md` (§ Trophy records, ✅ SHIPPED 2026-06-23, PR #1351): "a fresh record celebrates with '🏅 New personal best!' on the catch. A cheap long-tail goal — 'personal best' beats raw counts for retention" — plus the `!trophies`/`bigfish` "Biggest Catches" hall of fame (PR #1356) built on the same `best_weight` record.
2. **The weight law is committed in four constants and one rounding call.** `disbot/utils/fishing/weight.py`: `_BASE = 0.18`, `_EXP = 1.65`, `_SPREAD_LO = 0.65`, `_SPREAD_HI = 1.55`; `nominal_weight = round(_BASE * size_rank**_EXP, 2)`; `roll_weight = max(0.01, round(nominal × r.uniform(0.65, 1.55), 2))` — **every catch weight is a 2-decimal (0.01 kg) grid point**.
3. **The record comparison is STRICT.** `disbot/services/fishing_workflow.py:267`: `new_best = catch.weight > 0 and (prev_best is None or catch.weight > prev_best)`; the DB write (`disbot/utils/db/games/fishing.py::record_catch`) keeps `GREATEST(best_weight, EXCLUDED.best_weight)` and its docstring pins the same rule ("a new personal best … prior best is None or strictly less"). A tie is never a record. (Storage tie-exactness: `round(x, 2)` yields one deterministic double per grid point, so equal displayed weights are equal stored values — strictness is real, not float-fuzzy.)
4. **The catch mix makes the smallest fish the MODAL catch at every rod.** `disbot/utils/fishing/rewards.py::roll_catch`: `weights = [1.0 / (s.size_rank ** (1.0 / pull)) for s in pool]` — at the Bare Rod's committed `rarity_pull = 1.00` (`disbot/utils/fishing/rods.py` ROD_LADDER) the level-7 shore mix is exactly ∝ 1/rank over ranks 1–21 (`disbot/data/fishing/fish.json`: 21 shore fish, ranks 1..21, rank 1 = minnow; `fish.py`: FISH_PER_LEVEL = 3, MAX_LEVEL = 7, band = ranks ≤ 3·level, so EVERY band contains rank 1). The weights are strictly decreasing in rank for every finite pull (rod ladder tops at Diamond `rarity_pull = 1.70`; weather `rarity_mult` ≤ 1.30, `weather.py`), so rank 1 is strictly modal at every committed rod × weather cell.
5. **No committed knob touches the weight roll.** `roll_weight`'s ONLY caller is `rewards.py:48` — `Catch(species=species, weight=roll_weight(species, r))`. Rod knobs (window/bite/rarity/escape/grace), weather, bait, venue, level: none reaches the weight law (`grep weight` over `bait.py`/`gear.py`/`venue.py`: zero hits). The entire committed progression ladder can change WHICH species you catch — never what weights a species can roll.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

A "biggest caught" chase is a **record process**. For any continuous weight distribution the record law is distribution-free and immortal: P(new record at catch t) = 1/t exactly, E[records in n catches] = H_n → ∞ — a genuine long tail, and the reason "personal best" is a good retention hook in the first place. The committed law is NOT continuous: `round(·, 2)` projects every species' weights onto a **finite atom grid**, and the committed STRICT comparison (claim 3) then makes the chase **provably terminating** — once the record equals the species' top atom, no future catch can ever beat it, and the top atom has strictly positive probability. Three exact structure theorems, none stated anywhere in the committed tree:

- **T1 — the atom census.** With nominal N (an exact 2-decimal number, claim 2) and factor f ~ U(13/20, 31/20), the support of `round(N·f, 2)` is a finite set of consecutive 0.01-grid atoms; each atom's probability is an exact rational (interval length ÷ 9/10; rounding-boundary ties have measure zero). The census is closed-form: |A_r| ≈ 90·N_r + 1. For the minnow (N = 0.18): **exactly 17 atoms** — 0.12 (p = 4/81), 0.13…0.27 (fifteen atoms, p = 5/81 each), 0.28 (p = 2/81); the probabilities sum to 1 exactly.
- **T2 — the reachable ceiling.** The top atom's probability is strictly positive, so the chase is a.s. finite with E[catches to completion] = 1/p_ceiling: minnow **2/81 → 40.5 catches of the species**; at the bare-rod level-7 mix (q₁ = 1/H₂₁, exactly 5173168/18858053 ≈ 0.2743) that is **1527502293/10346336 ≈ 147.6 casts** to provably KILL the modal species' chase. The player is never told: the celebration just stops firing, forever.
- **T3 — the terminating-record law.** For a discrete distribution with atoms (vₖ, pₖ): P(v_k is ever a record) = pₖ / P(X ≥ vₖ), so **E[lifetime PBs] = Σₖ pₖ / P(X ≥ vₖ) — finite**; and P(PB at catch t) = Σₖ pₖ·P(X < vₖ)^(t−1) is **strictly below the continuous 1/t benchmark from t = 2 on** (ties eat records). Minnow: E[lifetime PBs] = **11736310749428605/3026966925030048 ≈ 3.877 celebrations ever** (continuous: unbounded, H_n); all 21 shore species together: **≈ 153.38 lifetime PBs**, front-loaded (≈ 24.9 in the first 50 casts, ≈ 93.0 by 2,000, then ≈ 60 more across an entire remaining career). The refinement lemma signs the cause: re-running the census at a 0.001 grid adds ≈ ln 10 ≈ 2.30 lifetime PBs per species — the finiteness is the ROUNDING's, not the spread's.
- **L1 — modal invariance (lemma).** For every finite pull ≥ 1 the mix weights rank^(−1/pull) are strictly decreasing in rank, and every level band contains rank 1 (claim 4) — so the species with the SHORTEST ladder (17 atoms; every other species has ≥ 52) is the modal catch at every committed rod, weather, and level cell. The committed progression ladder can only make ladder depletion FASTER (more casts/hour, bigger-fish bias never demotes rank 1 from modal); it cannot add a single rung (claim 5).

The tension being priced: the committed hook sells an open-ended chase ("worth chasing", "long-tail", "beats raw counts for retention") while the committed law hands the most-caught species a 17-rung ladder that a casual player completes inside ~150 casts — and the celebration's cadence is strictly below the design's own implicit continuous benchmark from the second catch of every species.

## Pinned model (committed constants @ f8e2313; conventions declared, exact rationals)

- **Weight law:** f ~ U(13/20, 31/20); atom vₖ = k/100 gets p = measure of f with N·f ∈ [(2k−1)/200, (2k+1)/200), clipped to the f-range, ÷ 9/10. Nominals pinned per rank (run once from claim 2's formula, quoted in the fixture): 0.18, 0.56, 1.10, 1.77, 2.56, 3.46, 4.46, 5.56, 6.76, 8.04, 9.41, 10.86, 12.40, 14.01, 15.70, 17.46, 19.30, 21.21, 23.19, 25.23, 27.35. `max(0.01, ·)` is inert (smallest atom 0.12).
- **Mix (decision cell):** bare rod (pull = 1), level 7, shore — qᵣ = (1/r)/H₂₁ exact rationals. Reporting rows: pull ∈ {1.10, 1.25, 1.45, 1.70} (the committed ladder), weather rarity_mult ∈ {1.08, 1.12, 1.30}, levels 1–6 bands, deepwater venue (same rank-atom law; float mixes disclosed as floats).
- **Record law:** strict > (claim 3); first catch of a species is always a PB.
- **Arms:** Arm A — closed-form exact census (atoms by interval arithmetic; E_life = Σ pₖ/Sₖ; P(PB at t) and E[PBs in n] by geometric series; kill-times). Arm B — independently-written twin (atom measures by boundary-point sweep; records-in-n by explicit t = 1..n DP over prefix-CDF partial sums); exact Fraction equality with Arm A required on every registered rational. Arm F — the committed roll re-implemented VERBATIM from claim 2's quoted line (float `round`, `random.uniform`), seeded: support equality with the exact model on ranks {1, 2, 3, 21} required; frequencies a reporting row (drafting already checked support identity against the actual committed module — 17/52/2462 atoms, same min/max, ceiling freq 0.0249 vs 2/81 at 400k draws). Arm R — seeded career traces (PB-event timelines at the decision cell), REPORTING-ONLY. Seeds 20261630–632 (F and R legs); aux 20261633 NEVER read (the P054–P070 aux convention).
- **Print discipline (drafting-discovered hazard, disclosed):** exact E_life rationals for ranks ≥ ~7 exceed CPython's default 4300-digit int-print limit — registered exact anchors are ranks 1–3 (printable) + the |A_r| and p_ceiling tables (small rationals, all 21 ranks); large-rank E_life values are gated by in-memory Fraction equality between the twin arms and REPORTED as 12-significant-digit floats, never printed raw.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** the committed "long-tail retention" claim iff, at the decision cell (bare rod, level 7, shore, committed constants): (i) the modal species' ladder has **≤ 20 rungs** AND p_ceiling ≥ **1/50** (chase provably complete in ≤ 50 catches of the species in expectation), AND (ii) the modal species' exact E[lifetime PBs] ≤ **4**, AND (iii) the strict-record law P(PB at t) < 1/t holds for every t ∈ 2..50 (the cadence never reaches the continuous benchmark the hook implicitly sells).
- **INVALID** on any gate failure (below).
- **APPROVE** iff the modal species' ladder has ≥ **100 rungs** AND its expected completion horizon at the decision-cell mix is ≥ **1000 casts** (the chase outlives a casual career — the hook holds as committed; mutually exclusive with REJECT by arithmetic).
- **NULL** otherwise, on named axes: (n1) the mix axis — if some committed cell demotes rank 1 from modal (L1 falsified), the census re-keys on the true modal species, tables attached; (n2) the float-boundary axis — Arm F support mismatch that survives the INVALID gate localizes real committed-code atoms the exact model misses (the finding is the corrected census); (n3) the display axis — if the Fishdex render is found to round coarser than storage, the player-visible ladder is SHORTER and the direction is signed (REJECT-conservative), disclosed not ruled; (n4) theorem failure without gate failure — the corrected law is the finding. Every NULL is a finalized, citable finding with its exact tables, never a re-run request.

## Gates (run INVALID on any failure)

- **G1 twin arms:** Arm B equals Arm A (exact Fractions, in-memory) on every atom probability, every E_life, every P(PB at t), every E[PBs in n] registered.
- **G2 (T1):** per-rank atom probabilities sum to exactly 1, all 21 ranks; |A_r| table verbatim (17, 52, 99, 160, 232, 312, 402, 502, 610, 724, 848, 978, 1117, 1262, 1413, 1572, 1737, 1910, 2088, 2272, 2462); the rank-1 atom law (4/81, fifteen × 5/81, 2/81) exact.
- **G3 (T2):** p_ceiling(1) = 2/81 exactly; kill-cast identity 1/(q₁·p_ceiling(1)) = 1527502293/10346336 with q₁ = 5173168/18858053 and H₂₁ = 18858053/5173168.
- **G4 (T3):** E_life(1) = 11736310749428605/3026966925030048 exactly; the geometric-series identity Σₜ P(PB at t) → E_life (partial sums monotone, n = 1000 within 1/1000 of the limit); P(PB at t) < 1/t strict for t ∈ 2..50.
- **G5 hand world (derived by hand in this file):** nominal 0.10 → f-intervals [k/10 − 1/20, k/10 + 1/20) for k = 7..15 — **exactly 9 atoms, each p = 1/9**, E_life = H₉ = **7129/2520** ≈ 2.829, E[catches to ceiling] = 9. (The uniform-atom case makes the record law's harmonic skeleton visible by pencil: Σ (1/9)/(i/9) = H₉.)
- **G6 battery:** refinement lemma — grid 0.001 (and 0.0001) re-census gives rank-1 E_life increasing by ln 10 ± 1/10 per decade and P(PB at t) → 1/t from below for t ∈ {2, 3, 5}; degeneracy — spread collapsed to a point ⇒ 1 atom, E_life = 1; E[PBs in n] non-decreasing in n, bounded by both H_n and E_life; L1 — mix weights strictly decreasing in rank at every committed pull × weather cell, every level band contains rank 1.

## Expected landing (DISCLOSED per the P048–P070 exact-arm norm)

Every registered number ran live at drafting (twin computations agreed; the fidelity check imported the ACTUAL committed module and matched support on ranks 1/2/21). **REJECT**: (i) minnow ladder = 17 rungs ≤ 20 and p_ceiling = 2/81 ≥ 1/50 (E[completion] = 40.5 catches; ≈ 147.6 casts at the decision-cell mix, ≈ 74 casts at the level-1 onboarding mix where q₁ = 6/11); (ii) E_life(minnow) ≈ 3.877 ≤ 4 — the committed hook's flagship species carries **fewer than four "🏅 New personal best!" celebrations, ever, in expectation**; (iii) strict-record inequality verified at t ∈ {2, 3, 5, 10, 41} (0.4699 < 1/2 at the second catch already). Career table (exact thinning): E[PB events] ≈ 24.9 @ 50 casts, 44.0 @ 150, 67.4 @ 500, 93.0 @ 2,000, 118.8 @ 10,000, lifetime total ≈ 153.38 — versus the continuous benchmark ≈ 99 @ 2,000 and ≈ 181 @ 100,000 and unbounded beyond. Falsifiability is live and named: a **one-character committed change** (`round(·, 3)`) multiplies every ladder ≈ ×10 — rank-1 rungs 17 → ≈ 163 ≥ 100 and completion horizon ≈ 1,480 casts ≥ 1000 — flipping the verdict to APPROVE outright; and if L1 fails anywhere the decision re-keys (n1). The REJECT indicts the committed retention SENTENCE and the unpriced quantization interaction — never the weight feature (per-catch weights make catches individual regardless), never the strict comparison (correct on its own), never the game.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

- **REJECT →** paste-ready structured choice to the manager for the superbot lane, recommendation first per Q-0263.2: **(a, recommended) store and compare the record at 3 decimals** — one character in `weight.py`'s roll (`round(·, 3)`) or a record-only finer field: every ladder ×≈10, the modal chase's horizon moves ~148 → ~1,480 casts, ≈ +2.3 lifetime PBs per species (+≈ 48 total), display can keep 2 dp everywhere except the trophy row (one extra digit there); (b) **un-quantize the comparison only** — store the raw float weight, round at render: the record process becomes continuous and the immortal distribution-free 1/t law returns exactly (the cheapest true fix; display unchanged); (c) **lean in** — compute each species' ceiling (closed form from the committed constants) and ship ladder completion as content ("perfect specimen" badge at the top atom), converting silent depletion into a visible completionist goal — an intent call the lane owner makes, never ruled here. The ruling conditions on the committed constants @ f8e2313; a later change to the spread, base, exponent, rounding, or comparison means re-run, not reuse.
- **APPROVE →** the committed hook stands, priced; note filed.
- **NULL →** the named axis's corrected table, attached, final.

## Dedup

Nearest priors, argued distinct: **P047 → V058** (same repo, creature BATTLE engine — rarity stat budgets under level normalization; zero shared machinery with the fishing weight roll). **P051 → V062** (same repo, chicken-farm FAUCET — coop cap × cadence coupling in absolute coins; no record process, no quantization). **P020/P023/P027 → V022/V025/V029** (same repo, casino SINK — bankroll ruin under house take). **P003/P016 → V001/V018** (same repo, encounter SPAWN faucet/cooldowns). **V042/V043 + inbox ORDER 006 items (4)–(7)** (superbot-GAMES repo — a different codebase; its fishing verdicts price species SELL curves and progression, `games/fishing/`, not the hub's `disbot/utils/fishing/` weight law). **P055 → V066** (mineverse badge threshold vs faucet — a wealth-crossing time, not a record process). **P059 → V071** (idle prestige reset — optimal-stopping on a growth curve). **P063 → V074** (games menu-width prefix law). **P067 → V080** (gba Wickroad stale-ink determinism). The captured backlog files `fishing-bait-crafting-2026-07-10.md` / `fishing-gear-stats-2026-07-10.md` in this section are link-index rows of superbot's own idea docs (bait recipes, gear stats), not proposals, and neither touches weights or records. Corpus grep at HEAD d165876 (`rg -i 'trophy|personal.best|best_weight|lunker|record.ladder|quantiz'`, bootstrap.py/.substrate excluded): zero hits in any proposal P001–P070 or verdict theme V001–V083 — the pipeline's first record-process head and its first quantization-interaction head.

## Model basis (declared model-dependence — the P024 discipline)

The atom probabilities treat rounding boundaries exactly (half-open intervals; the measure-zero banker's-rounding tie set is disclosed, and Arm F's support check is the committed-float honesty row). The mix model at the decision cell is the committed bare-rod law (exactly ∝ 1/rank); rod/weather/bait/venue/level cells are committed-constant reporting rows, with L1 gating the modal-invariance claim rather than assuming it. The engagement boundary is explicit: this head prices the PB-celebration PROCESS (event counts, cadence, termination) against the committed sentence that names it a retention goal — it measures no live player and claims no retention elasticity; "the celebration stops firing forever after a computable horizon" is the priced fact, its retention WEIGHT is the lane owner's judgment. The career table's casts-per-species split uses expected thinning (exact per-species; the composite over random species counts is the standard thinned-record identity, stated and twin-verified). Deepwater bands and the 11 deepwater fish ride the same rank-atom law and ship as reporting rows.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the corpus sweep
> `rg -i 'trophy|personal.best|best_weight|lunker|quantiz|record'` (bootstrap.py/
> .substrate excluded) at HEAD `d165876` hits only unrelated prose (websites
> healthcheck "records", casino "records" in results tables); the hub-fishing
> neighbors and the superbot-GAMES fishing verdicts (different repo) are argued in
> Dedup. (b) **kill test NOT triggered** — no prior proposal, idea file, or session
> card 💡 prices a record process, a weight roll, or a rounding/quantization
> interaction; no recorded drop of this head exists. (c) **feasibility + every
> registered number checked LIVE** (the V080 lesson — theorem claims verified by
> enumeration at drafting, the P068/P069/P070 norm): the exact atom census ran
> (all 21 ranks, probabilities sum to 1; |A| table 17…2462), the rank-1 atom law
> (4/81, 15 × 5/81, 2/81) and p_ceiling = 2/81 verified, E_life(1) =
> 11736310749428605/3026966925030048 computed exactly, the strict-record
> inequality verified at t ∈ {2, 3, 5, 10, 41}, the career/kill-cast identities
> (H₂₁ = 18858053/5173168; 1527502293/10346336 ≈ 147.6) verified, the G5 hand
> world checked by pencil (9 × 1/9 → H₉ = 7129/2520), AND the committed module
> itself was imported and sampled (support identity ranks 1/2/21; ceiling freq
> 0.0249 ≈ 2/81 at 400k draws) — plus one discovered hazard disclosed (the
> 4300-digit int-print limit; print discipline pinned in the model section).
> Seeds 20261630–633 swept collision-free at HEAD `d165876` (registered prior
> 20261620–623 = P070/V083's set; 20261624–629 the disclosed gap; standalone
> data numerals 20261664/20261833 per the recorded discrimination rule).

**1. What is this really?** A pre-registered EXACT MEASUREMENT of a shipped
retention mechanic against the arithmetic it actually runs on: the hub fishing
game's trophy-record chase ("a cheap long-tail retention goal", committed twice)
re-derived as a record process over the FINITE atom grid the committed
`round(·, 2)` creates, with the committed strict-> comparison making every
species' chase provably terminating. The atom census, ceiling probabilities,
lifetime-PB law, and cadence inequality are exact rationals at every registered
cell, judged against bands fixed before any code (REJECT first: ≤ 20 rungs +
p_ceiling ≥ 1/50 + E_life ≤ 4 + strict sub-1/t cadence; APPROVE: ≥ 100 rungs +
≥ 1000-cast horizon; NULL on four named axes), byte-identical across two process
runs, seeded legs demoted to fidelity/reporting.

**2. What is the possibility space?** (i) Don't run it — the round-14 game slot
goes unserved and the hub's flagship fishing retention hook stays unpriced on the
exact law it ships. (ii) A prose note "rounding shortens the chase" — retells the
direction, measures nothing, misses all three keepers (the exact census, the
terminating-record law, the modal-invariance lemma that pins WHERE it bites
hardest). (iii) Re-tune the spread constants — moves |A| linearly while the cause
is the grid: the refinement lemma shows a decade of grid buys ln 10 of chase, a
decade of spread buys the same at ten times the balance disruption — the sim
ships that comparison instead of guessing. (iv) An MC-only sim — leaves seed
noise on decision numbers that are exact rationals (the V065/V067 lesson); MC is
demoted to Arms F/R. (v) This head: exact census as the ruling, REJECT-first
bands, INVALID on G1–G6, twin-arm verification, falsifiability live (the
one-character `round(·, 3)` world flips to APPROVE). (vi) Over-scope (live
retention telemetry, leaderboard/`!trophies` social dynamics, deepwater balance,
XP/coin economy coupling) — each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~150-line stdlib file: interval arithmetic over a 0.01
grid, two record-law closed forms (pₖ/Sₖ and the geometric-series cadence), a
boundary-sweep twin, a verbatim re-implementation of the committed one-line roll
for the fidelity row, and a grid loop — yielding the full 21-species atom/ceiling/
lifetime census, the career celebration table, the refinement-lemma cause
attribution, and the per-option consequence numbers (×10 ladders, restored 1/t
law, per-species ceiling table for the badge option) — from a sim a verdict
session runs cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **The float boundary** —
the exact model treats rounding intervals in real arithmetic; the committed code
rounds binary doubles. Drafting checked support identity on ranks 1/2/21 against
the actual module; Arm F re-checks in-sim and a surviving mismatch is the named
n2 NULL (the corrected census is the finding, and the ceiling ATOM's existence —
the load-bearing fact — is robust: only boundary CELLS can shift). (b) **The mix
model** — the decision cell is the committed bare-rod law; if any committed cell
demotes rank 1 from modal, L1 fails and n1 re-keys the census (the G6 leg checks
every committed pull/weather/level cell, so this cannot pass silently). (c) **The
engagement boundary** — no retention elasticity is claimed; the priced object is
the committed celebration process itself (its event count is finite and its
cadence strictly sub-benchmark), which is exactly what the committed sentence
promises open-endedness about. (d) **Display coarser than storage** would only
SHORTEN the visible ladder (n3, direction signed, REJECT-conservative).
(e) **An arithmetic slip in the drafter's hand facts** — the sim re-derives
everything from the pinned constants; theorems are gates AND carry the n4
theorem-failure axis, so a wrong hand claim becomes a finalized corrected law,
not a silent bad gate.

**5. What does it unlock?** The round-14 game slot served with the pipeline's
first record-process head; three standalone keepers (the terminating-record law
E = Σ pₖ/Sₖ for any quantized chase; the refinement lemma ln-10-per-decade cost
of grid coarseness; the modal-invariance lemma pinning quantization damage to
the most-caught item); a paste-ready three-option fix menu with exact per-option
numbers for the lane owner; and the transferable audit — every fleet surface
that celebrates "a new best" over a rounded/discretized metric (fastest-time
records at 0.1s, biggest-win records in whole coins, any leaderboard on a
quantized score) inherits the same silent termination law, now priced.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arm A settles every decision number exactly, in
milliseconds, with no seed. The single cheapest probe if a reader doubts a leg
is the minnow pencil count: nominal 0.18, spread 0.65–1.55 ⇒ weights 0.117–0.279
⇒ 2-dp values 0.12–0.28 = **17 possible weights**; a chase with 17 rungs and a
1-in-40 top roll is not a long tail — a three-line hand count that anchors the
whole census.

**7. What would make this a mistake to run?** If the exact arithmetic were
unavailable (it is not — the model is closed-form intervals and geometric
series), if the head duplicated a prior (it does not — the corpus grep is clean;
the superbot-games fishing verdicts price a different repo's sell curves), or if
the disclosed REJECT made the run theater. It does not: the value is the
independent hermetic re-derivation of the census plus the numbers no doc states
(the 17-rung flagship ladder, the ≈ 3.877 lifetime celebrations, the ≈ 147.6-cast
kill horizon, the 153.38 career total vs the divergent benchmark), the L1/G6
sweep that could NULL the modal claim, and an APPROVE world one committed
character away (`round(·, 3)`) — both non-REJECT rulings are genuinely reachable.

**8. How will we know it worked?** A committed sim-lab report with: the full
21-species atom/ceiling/lifetime tables (exact rationals for ranks 1–3 + the
|A|/p_ceiling tables; 12-digit floats elsewhere per the print discipline), the
T1/T2/T3 theorem verifications and the L1 sweep, the G5 hand world, the G6
refinement/degeneracy battery, the twin-arm equality note (two process runs
byte-identical), Arm F's committed-roll fidelity row beside the exact model,
Arm R's seeded career traces (reporting-only), and the verdict token against the
pre-registered bands. A clean run reproduces the drafter's disclosed values
(17 rungs; 2/81; 11736310749428605/3026966925030048; 1527502293/10346336;
H₉ = 7129/2520 hand world; ≈ 153.38 career total) from scratch, or — the more
interesting outcome — DISAGREES and pins the drafter's error, which the
pre-registered rule then rules on honestly (the n4 axis exists for exactly
that).

**Recommendation: sim-ready**
