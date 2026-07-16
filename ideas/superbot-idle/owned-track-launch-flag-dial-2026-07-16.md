# The milestone that cannot move: under the shipped runtime the owned track's metric is a session CONSTANT — every owned rung is a birth freebie or unreachable forever (flip thresholds exactly ceil(threshold/roster)), all 54 skinned slots on the shipped catalog render 🔒 1/10 or 🔒 2/10 immovably, and the launch flag whose own docstring commits "touches no economy constant" is the track's only in-game lever: a permanent +5%..+15% global production dial with a theme-gate-passing roster back door

> **State:** sim-ready
> **Class:** game-mechanics (pipeline rotation — the standing ORDER 003 GAME
> slot, round 16 third serve; round 16 opened at fleet backlogs with P077
> (#442) and served venture with P078 (#443, merged 2026-07-16T00:04:35Z by
> github-actions[bot]), so game mechanics is next per ORDER 004 rule 3,
> confirmed against the slot's own spacing history (…P067, P071, P075 →
> P079, spacing 4). Source: SUPERBOT-IDLE by least-recently-drawn — the
> slot's source-rotation record reads gba r6/r7, superbot r8/r9, mineverse
> r10, idle r11, games r12, gba r13, superbot hub r14, mineverse r15; the
> P075 card's baton, relayed by the P076 card and deliberately left intact
> by P077 (whose fleet tap took the UNBUILT timed-events scoping doc and
> reserved this slot for the lane's LIVE mechanics — this head is that
> draw: the shipped runtime surface, `tools/play.py` + the live engine).)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264
> pipeline; the deliverable is a committed stdlib sim + a citable measured
> verdict — no lane build)
> **Grounding:** https://github.com/menno420/superbot-idle/blob/884aeae9687742a389a2e2086a4cc930e5a4f3ee/tools/play.py@884aeae9687742a389a2e2086a4cc930e5a4f3ee · fetched 2026-07-16T00:17:22Z
> **Grounding:** https://github.com/menno420/superbot-idle/blob/884aeae9687742a389a2e2086a4cc930e5a4f3ee/idle_engine/economy.py@884aeae9687742a389a2e2086a4cc930e5a4f3ee · fetched 2026-07-16T00:17:22Z
> **Grounding:** https://github.com/menno420/superbot-idle/blob/884aeae9687742a389a2e2086a4cc930e5a4f3ee/docs/design/achievements-v0.md@884aeae9687742a389a2e2086a4cc930e5a4f3ee · fetched 2026-07-16T00:17:22Z
> (FIRSTHAND pin: fresh read-only clone via the local git proxy at
> superbot-idle HEAD `884aeae9687742a389a2e2086a4cc930e5a4f3ee` — the same
> HEAD P077 pinned; the lane has not moved. Read from that tree: the runtime
> grant + dispatch surface + prestige re-grant (tools/play.py), the owned
> ladder and its constants (idle_engine/economy.py), the earned-set fold and
> action-boundary award (idle_engine/achievements.py, engine.py), the 🔒
> lock-line renderer (idle_engine/render.py), the committed sentences
> (docs/design/achievements-v0.md, theme-balance-v0.md, economy-v1.md), the
> theme gate (tools/theme_gate.py, schema/theme.schema.json), and the full
> 18-pack catalog (themes/*.yaml). The sim vendors the engine + runtime
> byte-for-byte, sha256-manifest-pinned — the V017 precedent — and is
> otherwise hermetic: zero repo/network reads at verdict time.)

**Origin:** drafted under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3's rotation, round 16 game slot, with the EAP extension
to 2026-07-21 (ORDER 015) as the standing frame and the owner's live resume
confirmation as the wake authority.

## The harvested tension (both horns committed, verbatim)

- **Horn 1 — the ladder and its framing (achievements-v0.md + economy.py @
  `884aeae`):** the `owned` milestone track watches "TOTAL generators owned,
  summed across all generator kinds", thresholds `(10, 100, 1_000)`, each
  rung a permanent global `+5%` production bonus; "rung 1 is a first-session
  target once generator purchase lands"; "No pay-to-win: no purchase path
  exists or is planned that buys milestones or their bonuses". Every pack
  gets the same engine-derived slots; a theme skins nouns only.
- **Horn 2 — the runtime's innocence claim (tools/play.py @ `884aeae`,
  verbatim):** the shipped entrypoint seeds every fresh save with
  `start_count` of EVERY declared generator and re-seeds exactly that set
  after every prestige ("the engine has no generator purchase verb yet …
  without a starting grant a fresh save produces nothing"); "The starting
  grant is a RUNTIME entrypoint choice … it lives entirely in this tool and
  touches no economy constant." The flag is a documented CLI switch
  (`--start-count`, default 1; the module docstring's own usage example is
  `--start-count 4`).

The committed world these sentences live in (all firsthand @ `884aeae`):
economy-v1.md's "no generator purchase path exists yet in the engine";
`apply_prestige` wipes `owned` and the runtime immediately re-grants the
birth set; the earned set persists forever; the catalog ships 18 packs with
roster multiset {1×1, 2×17} (egg-farm alone is single-generator), base-rate
multiset {1×18, 5×17}, and ALL 18 packs skin ALL THREE owned slots with
goal-shaped flavor (royal-bakery's owned-1: "first hearth lit — Ten ovens
firing at once").

**The collision, in one line:** with no purchase verb, total generators
owned is the session constant s·n (flag × roster) — so the owned ladder
prices CONFIGURATION, not progression, and the only two levers on its
permanent +5%..+15% CORE bonus are the launch flag whose docstring disclaims
economy effect and the roster cardinality that no gate audits.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Six exact structure theorems, EVERY registered numeral produced by the
drafting script this session (`draft_p079.py`, 29/29 checks PASS, exit 0,
~4.7 s, driving the REAL cloned engine + tools/play.py through their public
API; V080 live-verify + V084 NO-DERIVED-LITERALS):

- **T1 — the INVARIANCE LAW.** Total owned equals s·n at every action
  boundary of every committed command sequence (the full dispatch surface:
  status / shop / achievements / buy n / buy max / wait / offline /
  prestige do / save). Structural core: exactly one committed code path
  writes `owned` during play — `apply_prestige` wipes it and the runtime's
  `_prestige` re-grants the identical birth set (a fixed point, verified:
  owned == {tier1: 5, tier2: 5} after reset at s=5). Live enumeration: 18
  packs × the registered 12-value flag grid = **216 cells**, an 11-command
  canonical corpus including a full prestige cycle, invariant checked after
  every dispatch — **216/216, zero violations** (Arm R adds 2,000 random
  traces per seed: 0 violations at 12,874 / 12,779 / 13,179 boundaries).
- **T2 — the BIRTH/NEVER DICHOTOMY.** `milestone_progress` on the owned
  track is a constant function of the session config, so owned-k is earned
  iff s·n ≥ θ_k, and when earned it lands at the FIRST call of
  `award_milestones` — before any player decision has taken effect —
  **216/216 cells** match the closed-form predicate at the first boundary
  AND after the full corpus (the 648 cell-rung Arm-A==Arm-B contact). Flip
  thresholds are exactly **s\* = ceil(θ_k/n)**: 10/100/1,000 on egg-farm,
  **5/50/500 on every two-generator pack** — four registered margin-0
  contacts sit exactly ON the threshold (s·n == θ at (2-gen, s=5), (egg-farm,
  s=10), (2-gen, s=50), (2-gen, s=500); earned at s\*, not at s\*−1, all
  verified live).
- **T3 — the CATALOG CENSUS (the shipped game).** At the default flag every
  committed pack's total owned is 1 or 2 — **all 54 skinned owned slots
  (18 packs × 3 rungs) are unreachable**, and `render_achievements` shows
  the goal as a live locked progress line that can never advance: **"🔒 2 /
  10"** (17 packs), **"🔒 1 / 10"** (egg-farm), byte-identical after the
  entire canonical corpus including a prestige reset (`milestone_progress`
  == 2 after everything). Every one of those 54 slots carries committed
  themed goal flavor sold to the player as a destination.
- **T4 — the DIAL and its floor gate.** The flag is a permanent global
  production dial: s=500 on a 2-gen pack births all three rungs and moves
  total rate **3,000 → 3,450/s (+15% exactly)**. The dial is itself
  floor-gated (V038's committed "felt = integer rate delta > 0" imported):
  egg-farm s ∈ {10..19} EARNS owned-1 whose +5% pays **ZERO** (10 → 10,
  19 → 19; the first paying flag is exactly **20**: 20 → 21), and at the
  2-gen flip s=5 the whole payout is **+1/s, all of it on tier-2** (25 → 26)
  while tier-1 is floor-eaten (5 → 5) — total 30 → 31.
- **T5 — the ROSTER BACK DOOR (schema-legal today).** Roster cardinality is
  a pure SKIN datum (schema cap: 20 generators), yet it is the other factor
  in the birth predicate. Constructed witness pair, validated end-to-end:
  a 10-generator base-20 pack and its 9-generator twin BOTH pass the
  committed theme gate (**exit 0 on the 20-pack catalog including both**,
  zero `balance` blocks) — and at the DEFAULT flag the 10-gen pack is born
  owning 10, earns owned-1 at its first boundary, and runs **210/s vs the
  twin's 180/s, permanently**: the tenth declaration buys +5% that
  theme-balance-v0's "no non-neutral value ships without Q-0264 approval"
  gate cannot see (the pinned neutrality test checks the DECLARED knob
  only).
- **T6 — the BOUNDARY LAG (the award is late even when it is free).** A
  born-blessed config's first span accrues wholly at the pre-award pct
  (awarding is an action-boundary step, committed): at (2-gen, s=5) the
  first 30 s span pays 30/s (**900**), the second 31/s (**930**); with a
  3,600 s first span the crossing of lifetime-1 AND lifetime-2 mid-span
  compounds the lag — first span **108,000** (30/s), second **118,800**
  (33/s, pct 115: owned-1 + lifetime-1 + lifetime-2 banked together at the
  boundary).

## Pinned model (committed constants — grounded + invented-but-pinned, exact)

- **Committed (firsthand @ `884aeae`):** `MILESTONE_OWNED_THRESHOLDS = (10,
  100, 1_000)`, `MILESTONE_BONUS_PERCENT = 5`, `build_milestone_specs`'s
  three owned rungs for every pack (economy.py); the earned-set fold
  `base_rate · count · upgrade_pct · prestige_pct · milestone_pct ·
  theme_pct // 100_000_000`, one floor per generator-second (engine.py);
  `award_milestones` as the explicit action-boundary step and
  earned-once-kept-forever through prestige (achievements.py);
  `new_session`'s grant `{gid: start_count for gid in theme.generators}`,
  `_prestige`'s identical re-grant, and the full dispatch verb set
  (tools/play.py); `render_achievements`'s 🔒/⏳/✅ lock-line composition
  (render.py); the seven pinned sentences (play.py ×2, achievements-v0 ×2,
  theme-balance-v0, economy.py, economy-v1) — presence asserted
  whitespace-normalized at the clone; the catalog: 18 packs, roster multiset
  {1×1, 2×17}, base-rate multiset {1×18, 5×17}, 54 skinned owned slots,
  zero balance blocks; the theme gate + schema (generator list cap 20,
  base_rate bounds 1..1000).
- **Invented-but-pinned (disclosed, swept where applicable):** the flag grid
  s ∈ {0, 1, 4, 5, 9, 10, 19, 20, 49, 50, 499, 500} (chosen to bracket
  every flip threshold with its margin-0 and one-below rows; 4 is the
  module docstring's own usage example); the 11-command canonical corpus
  (includes a full prestige cycle via `offline 200000`); the back-door
  witness pair (10 vs 9 generators, base_rate 20 — 20 chosen as the
  smallest committed-bounds rate where +5% pays exactly at count 1,
  ledger-clean: 20·1.05 = 21); the wedge probe states (owned-only earned
  sets {}, {owned-1}, {owned-1..3} on pinned GameStates).
- **Fixture line (registered, the V089/V090 lesson):** Arm-R draw-order
  grammar — one `random.Random(seed)` per trace set; per trace, draws in
  exactly this order: (1) pack index uniform over the sorted 18-id list,
  (2) flag s uniform over the registered grid tuple, (3) L uniform 3..10,
  then per step exactly TWO draws: (4a) command index uniform over the
  5-tuple ("wait", "offline", "buy-max", "prestige-do", "achievements"),
  (4b) duration uniform 60..7200 (drawn EVERY step, consumed only by
  wait/offline); 2,000 traces per seed; seeds 20261710/711/712
  reporting-only; aux 20261713 NEVER read.

## Pre-registered decision rule (evaluation order: REJECT first)

- **R1 (invariance + dichotomy):** total owned == s·n at every boundary of
  the canonical corpus on all 216 cells AND the earned set equals the
  closed-form predicate {owned-k : s·n ≥ θ_k} at the first boundary and
  after the full corpus on all 216 cells (648 cell-rungs) AND the prestige
  re-grant fixed point holds — all by exact re-derivation on the vendored
  engine.
- **R2 (catalog census):** the shipped catalog lands exactly (18 packs,
  roster multiset {1×1, 2×17}, 54 skinned owned slots) AND at the default
  flag all 54 are unreachable with the lock lines exactly "🔒 2 / 10" /
  "🔒 1 / 10", byte-stable across the corpus.
- **R3 (the dial):** flip thresholds exactly ceil(θ/n) with the four
  margin-0 rows earned-at-s\*/not-at-s\*−1 AND the wedge table exact
  (10→10, 19→19, 20→21; 30→31 with the 5→5 / 25→26 split; 3,000→3,450) AND
  the boundary-lag pairs (900/930, 108,000/118,800).
- **R4 (the back door):** the constructed 10/9-generator pair passes the
  committed theme gate (exit 0, 20 packs) AND the 10-gen pack is
  born-blessed at the default flag with rates exactly 210 vs 180.
- **REJECT** (the owned track, as shipped, is a configuration predicate —
  Horn 1's progression framing and Horn 2's touches-no-economy-constant
  sentence cannot both stand) iff R1 AND R2 AND R3 AND R4. **APPROVE** (the
  track is a genuine progression surface) iff some committed no-load command
  sequence at the default flag changes total owned or earns any owned rung —
  the witness world is constructible (an engine carrying V017's recommended
  unlock-only purchase verb satisfies it), so the ruling genuinely
  discriminates between the shipped surface and its post-build sibling;
  mutually exclusive with REJECT by construction. **NULL** on the named
  axes: (i) the `load` escape hatch — `load` is blob-authoritative and can
  inject ANY owned map (persistence validates types, not rosters), so all
  reachability claims are scoped to the no-load command surface, disclosed;
  (ii) the corpus/grid convention — R1's invariance is also structural
  (single-writer + fixed-point), so a corpus extension or grid bump must
  not flip it, carried as a control; (iii) the future-mechanic boundary —
  the ruling binds the SHIPPED surface only; V017's conditional
  registration row is the named arming event that re-opens it. **INVALID**
  on any gate failure (F1–F6 below).
- Honest-null explicit: every NULL is a finalized, citable finding with its
  exact censuses attached, never a re-run request.

## Gates (run INVALID on any failure)

- **F1 identities:** 18 = pack glob count = census rows; 54 = 18·3 skinned
  owned slots; roster multiset {1×1, 2×17}; base-rate multiset {1×18,
  5×17}; 216 = 18·12 cells; 648 = 216·3 cell-rungs; the seven committed
  sentences present (whitespace-normalized) at the vendored pin.
- **F2 theorems:** T1–T6 re-derived from scratch on the vendored engine
  (zero trust in this file's numbers).
- **F3 census anchors:** 216/216 invariance, 216/216 dichotomy, 648/648
  contact; flip rows (5, 10, 50, 500 with s−1 refusals); lock lines
  "🔒 2 / 10" / "🔒 1 / 10"; dial cells (10,10), (19,19), (20,21), (30,31),
  (5→5, 25→26), (3000,3450); back door (exit 0; 210, 180); lag pairs
  (900, 930), (108000, 118800).
- **F4 pencil worlds:** the (2-gen, s=5) 30 s pair hand-checked (30·30 =
  900; 31·30 = 930); the prestige fixed point {tier1: 5, tier2: 5}; the
  s=500 wedge as pure percent (3450 = 3000 + 15% exactly, no floor loss at
  that fold).
- **F5 degeneracy/convention controls:** s=0 (empty grant: zero production,
  prestige refused, invariant 0); corpus-extension and grid-bump
  non-flipping on R1; the back-door pair differs ONLY in roster length
  (asserted field-by-field).
- **F6 battery:** twin evaluators exact-equal through FOUR typed must-equal
  contacts (C1: 18 == glob == census rows; C2: 54 == 18·3 == frozen
  rendered owned fields at the default flag; C3: the four margin-0 rows,
  s·n == θ exactly AND earned at s\* AND refused at s\*−1; C4: Arm-A
  predicate == Arm-B live award on all 648 cell-rungs); Arm-R determinism
  (each seed reproduces itself byte-identically) and the registered
  draw-order grammar asserted by draw-count sentinels.

**Arms:** Arm A — closed-form constants and the predicate s·n ≥ θ_k
(seedless, exact). Arm B — the REAL vendored engine + runtime driven through
`play.dispatch` / `play.advance` (independently structured: the live walk
must reproduce every Arm-A number through the typed contacts). Arm R —
seeded random command traces REPORTING-ONLY (drafting previews: seed
20261710 → (0 violations, 1,392 blessed traces, 12,874 boundaries), 20261711
→ (0, 1,395, 12,779), 20261712 → (0, 1,415, 13,179); 2,000 traces each); aux
20261713 never read by any leg.

## Expected landing (DISCLOSED per the P048–P078 exact-arm norm)

Drafting-run landing: **REJECT** — R1–R4 all fire at the numbers above
(29/29 drafting checks). The sim re-derives everything from scratch; the
disclosed landing binds nothing. Falsifiability is live and named: a second
committed writer of `owned` anywhere in the play surface would dissolve T1
(swept: `apply_prestige` + the runtime re-grant are the only writers;
`load` is the disclosed NULL axis); a pack shipping ≥ 10 generators would
move T3 from "unreachable" to "born-blessed" (the catalog sweep found
none — max roster 2); a runtime that awards milestones INSIDE spans would
dissolve T6 (the committed docstrings pin the boundary); and the APPROVE
witness world (V017's unlock verb) is constructible, so the ruling genuinely
separates the shipped game from its planned successor.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

REJECT → paste-ready structured choice to the superbot-idle lane,
recommendation first (Q-0263.2), timed to land BEFORE the generator-purchase
build slice re-registers the economy (V017's conditional row is already
waiting):

- **(a, recommended)** re-scope the owned track NOW, one doc revision + one
  docstring amendment, zero engine code: achievements-v0.md pre-registers
  the owned rungs as DORMANT until the purchase verb lands (V017's
  conditional registration row named as the arming event — its own finding
  that the ladder and pacing-compatible purchases are "mutually exclusive
  as registered" means the re-registration must revisit the thresholds
  anyway); play.py's grant docstring drops "touches no economy constant"
  and states the true coupling ("the grant sets the owned-milestone birth
  predicate; values ≥ 5 on a two-generator pack pre-earn owned-1"); and
  theme-balance-v0.md gains the roster-cardinality note (a ≥ 10-generator
  pack is a balance change and routes through Q-0264 like any non-neutral
  value — closing the T5 back door by pre-registration, not code).
- **(b)** make the UI honest instead: render the three owned slots as
  "awaits a future mechanic" (a render.py presentation change; the themed
  flavor stays, the immovable 🔒 progress bar goes) — smallest
  player-facing fix, leaves both committed sentences false at the code
  level.
- **(c)** enforce at the gate: theme-gate rejects packs with ≥ 10 declared
  generators and the runtime clamps `--start-count` below the first flip
  threshold until the purchase slice lands — closes both levers by code,
  at the price of two new committed constants that the purchase slice will
  immediately have to unwind.

Known co-consumers of the verdict: V017's open conditional registration
(the owned-ladder renumbering it already flagged), V070's application guard
(its "a multi-generator world re-opens the owned rungs" sentence is
answered: re-opened and still frozen — the guard can now cite an exact
census), V090's repair discussion (the T4 zero-pay dial cells are one more
row in the smallest-pre-floor-product audit), and every fleet lane that
ships a progress UI over a metric no shipped verb can move (the
transferable audit: for each rendered progress bar, name the committed
action that increments its metric — if none exists, the bar is
configuration, and its reward is a dial).

## Dedup

- Swept at HEAD `dcc0991` (idea-engine, `grep -ri
  'start_count|owned-1|owned track|owned rung|roster card|launch flag'`
  excluding kit machinery) + sim-lab READ-ONLY @ `161aa7f` (newest VERDICT
  090): no proposal P001–P078 and no verdict V001–V090 prices the shipped
  runtime grant, the owned-track invariance, the flag dial, or the roster
  back door. Nearest kins, disclosed and argued:
  - **V017 (P015's T10 cost-curve sweep):** proved "total owned maxes at 2 —
    owned-10/100/1,000 are UNREACHABLE, permanently" IN ITS PASSING SHAPE
    (the unlock-only FUTURE purchase mechanic) and answered achievements-v0
    question 3 for the swept curves. IMPORTED here as the launch point — the
    new objects are the SHIPPED surface V017 never modeled (its world was
    `owned={"tier1":1}` with a candidate purchase driver): the runtime
    grant, the dispatch invariance theorem, the flip-threshold law, the
    catalog census with rendered lock lines, the flag/roster levers, and
    the two collision sentences (play.py postdates V017's pin `c753bc8`).
  - **V070 (P059's prestige reset policy):** asserted Σ owned = 1 as an F4
    conservation control in ITS count-fixed reference world and
    pre-registered "a multi-generator world re-opens the owned rungs and
    the question with them" as an application guard. This head walks
    through exactly that door: the shipped runtime IS the multi-generator
    world (17 packs × 2 generators), and the answer is a census, not a
    policy table — different track (owned vs lifetime), different question
    (metric reachability vs schedule optimality), zero shared fixtures.
  - **V090 / P077 (same repo, the round-16 fleet tap, verdicted REJECT @
    `161aa7f`):** floor-staircase delivery of a percent through the fold,
    in an UNBUILT doc. The T4/T5 zero-pay cells here reuse that elementary
    floor arithmetic as SUPPORTING contacts (V038's "felt = integer rate
    delta" definition imported verbatim, disclosed) — the head is
    orthogonal: reachability/invariance of a progression metric under the
    committed action surface, priced on the SHIPPED runtime, with the
    decision object a pair of committed sentences neither P077 nor V090
    cites. Zero shared fixtures (dispatch traces vs fold lattice).
  - **V088 / P075 (the previous game slot, mineverse):** config-datum-as-
    unvalidated-gate family (max_depth clipping board visibility). Different
    repo, different mechanism (render-layer visibility clip vs progression
    reachability + economy dial), zero shared fixtures — the family
    resemblance is the transferable audit, not the theorem.
  - **V084 / P071 (two game slots back):** trophy-record quantization
    (fishing) — integer-floor family only, different repo and object.
  - **V038:** its "felt = integer rate delta > 0" perception definition and
    low-rate feltness tables are imported for T4's zero-pay rows; its
    object was purchase feltness on the reference world, never the
    milestone birth predicate.
- Word collisions cited: "unreachable" appears in V017 (imported above) and
  V088 (visibility sense); "milestone" throughout the idle verdict family —
  the owned track's SHIPPED semantics are priced nowhere.

## Model basis (declared model-dependence — the P024 discipline)

- **(1) Statistical assumptions:** none in any decision arm — the world is
  deterministic and every decision number is exact integer arithmetic on
  the vendored engine. Arm R is reporting-only.
- **(2) Modeling assumptions:** the flag grid and canonical corpus are
  conventions (disclosed; R1 is also structural — single-writer +
  fixed-point — and the convention controls must show non-flipping); the
  back-door pack is a CONSTRUCTED witness, schema-validated and
  gate-validated, marked invented-but-pinned; `load` is scoped out as a
  named NULL axis (blob-authoritative by committed design, so
  "reachability" means the no-load command surface); the ruling binds the
  shipped surface at `884aeae` only — a purchase verb landing is the named
  re-run event, not a refutation.
- **(3) What a hostile reviewer says:** "V017 already told the lane the
  owned rungs are unreachable." Answer: V017 priced a FUTURE mechanic's
  curves and said so conditionally; meanwhile the lane SHIPPED a runtime
  whose grant flag and roster cardinality silently became the track's only
  levers, behind a docstring that disclaims exactly the coupling it
  creates, with 54 themed goal bars rendered over a constant — and no
  committed record states any of it. The arithmetic is elementary; the
  value is that the shipped game's owned track is now a committed,
  pre-registered, citable object — invariance theorem, flip law, census,
  dial table, back door — attached to the exact sentences it falsifies,
  delivered before the purchase slice re-registers the economy on top of
  it.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained mechanism probe
> on committed constants + the vendored engine, sim is report-only
> evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the
> tree-wide and sim-lab sweeps above returned no prior pricing of the
> shipped owned-track semantics (nearest kins V017/V070/V090/V088/V038
> cited and argued); (b) **kill test NOT triggered** — no prior proposal,
> idea file, or session-card 💡 prices the runtime grant or the owned
> invariance; V070's application guard explicitly NAMES the open question
> this head answers; (c) **feasibility + liveness arithmetic checked
> LIVE** — every registered numeral was PRODUCED by the drafting script
> this session (`draft_p079.py`, 29/29 PASS, exit 0, ~4.7 s, on the real
> clone): the catalog census, the 216-cell enumeration with 648 contact
> rungs, the four margin-0 flip rows, the dial and lag tables, the
> gate-passing back-door pair, the seven sentence pins, and the Arm-R
> previews; expected landing DISCLOSED (REJECT), all four rulings reachable
> under the pre-registered rule, the APPROVE-witness world named, and the
> INVALID controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of what the
owned milestone track IS in the game that actually shipped — taken where
the meaning lives: the committed runtime's own dispatch surface, driven
end-to-end. Six theorems carry it: the invariance law (the metric is a
session constant), the birth/never dichotomy with its exact flip law, the
54-slot frozen census with the rendered lock lines, the flag dial with its
floor-gated payout rows, the gate-passing roster back door, and the
boundary lag. All decision arithmetic is seedless exact integers on the
vendored engine, judged against bands fixed before any code.

**2. What is the possibility space?** (i) Don't run it — the purchase build
slice re-registers the economy with the track's shipped semantics unpriced,
and the flag/roster levers ship into the multiplayer/plugin era as
undocumented +5% dials. (ii) Wait for the purchase verb — prices the
successor, never the year the shipped game actually played this way, and
V017 already covers the successor conditionally. (iii) A prose bug report
("start-count 5 pre-earns a milestone") — states the smell, not the
structure: no invariance theorem, no flip law, no census, no back-door
witness, nothing the re-registration can decide with. (iv) An MC-only sim —
seed noise on exact combinatorics (the V065/V067 lesson); MC is demoted to
reporting.

**3. What is the most advanced capability reachable by the simplest
mechanism?** One multiplication, fully understood: total owned = flag ×
roster, forever. Everything else — the flip law ceil(θ/n), the census, the
dial table, the back door — is that constant read against the committed
ladder. Nothing stochastic, nothing tunable, nothing that cannot be
re-derived from this file in an afternoon.

**4. What breaks it? (assumptions made explicit)** (a) **A second owned
writer** — any committed play-surface code path that changes `owned` would
dissolve T1; swept: `apply_prestige` (wipe) + the runtime re-grant are the
only writers, and `load` is the disclosed blob-authoritative NULL axis.
(b) **A big-roster pack** — one committed pack with ≥ 10 generators flips
T3's census from "unreachable" to "born-blessed"; the catalog sweep found
max roster 2 (and that flip is T5's point, not a refutation). (c) **The
boundary claim** — a runtime awarding milestones inside spans would
dissolve T6; the committed docstrings pin awarding to action boundaries
verbatim. (d) **Perception** — the T4 zero-pay rows read "pays" as integer
rate delta, V038's committed definition; a fractional-rate UI would change
those rows (and the engine exposes none).

**5. What does it unlock?** For the superbot-idle lane: the purchase-slice
re-registration inherits an exact statement of what it is replacing (and
choice (a)'s three one-line repairs land before the successor builds on the
false sentences). For V070's guard: its named open question gets its
census. For the theme lane: the roster-cardinality rule closes a
gate-invisible balance channel before the catalog grows past 2-generator
packs. For the fleet: the transferable one-liner — for every rendered
progress bar, name the committed verb that moves its metric; a bar with no
verb is configuration wearing a goal's clothes, and its reward is a dial
someone controls from outside the game.

**6. What is the cheapest experiment that decides it?** The whole head IS
the cheapest experiment: a stdlib drive of the vendored engine over 216
cells + 2,000×3 reporting traces, ~4.7 s at drafting, no network, no state,
no seeds in any decision arm. The sim adds only the from-scratch
re-derivation, the twin evaluator, the controls, and the report.

**7. What would make this a mistake to run?** If the shipped semantics were
already priced (swept: V017 is conditional-future, V070 is count-fixed and
names this exact question as open); if the purchase verb were already
landing (swept @ `884aeae`: economy-v1's sentence stands, no purchase code
exists, V017's row is still conditional); or if the lane were mid-flight on
a milestone rework this REJECT would whipsaw (the lane's current-state
shows the timed-events step-2 gate as the open decision, and V090 just fed
it — this verdict feeds the OTHER open gate, the purchase re-registration).
None hold.

**8. How will we know it worked?** A committed sim-lab report with: the
invariance and dichotomy censuses at 216/216 and 648/648, the four margin-0
flip rows, the frozen lock-line census, the dial and lag tables at exactly
the registered numbers, the back-door pair passing the real gate at 210 vs
180 (or a documented divergence — which would itself be the finding), the
four typed contacts green, one ruling under the pre-registered rule, and —
downstream, not gating — the lane's purchase-slice re-registration citing
the verdict when it re-scopes the owned ladder, amends the grant docstring,
and closes the roster channel.

**Recommendation: sim-ready**
