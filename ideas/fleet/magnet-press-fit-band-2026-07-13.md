# The magnet press-fit band — does the shipped `magnet_fit = 0.15` mm interference default land the pocket in the PRESS band across real printers, and at what loose/unseatable error rate?

> **State:** sim-ready

> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot,
> round 9; the harvest SOURCE returns to curious-research for the slot's SECOND tap of
> that repo — P041 (round 7) harvested the spool-weight-scale project ONLY, and this
> head harvests a DIFFERENT, untapped project subtree (`projects/effector-mount/` plus
> the `projects/tolerance-test-coin/` band semantics as cross-instrument calibration)
> — after round 1 websites (P019), round 2 superbot (P021), rounds 3–4 substrate-kit
> (P025/P029), round 5 superbot (P033), round 6 fleet-manager (P037), round 7
> curious-research/spool-scale (P041), round 8 superbot-mineverse (P045)) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/curious-research@a9fd5faa6a10b4d1364d205dbeac7a8678e1bd73 · fetched 2026-07-13T22:15:32Z
> (the harvest-source pin — read via read-only shallow clone this slice, HEAD
> ls-remote-verified; reading path per superbot docs/fleet-reading-path.md §0. The sim
> itself is fully hermetic: zero repo/network reads at verdict time, every fixture
> constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 8 closed fully served with P048 (#353) at the
unrelated slot (fleet backlogs → P045 #343, venture → P046 #348, game mechanics → P047
#352), so round 9 reopens at the FLEET-BACKLOGS slot and this slice is the round-9
opener. ORDER 004 rule 4 is untouched: nothing here builds makerbench — this head is
harvest → probe → outbox only, and curious-research's own files are never edited by this
repo (routing is the manager's per Q-0260).
**Placement note (decide-and-flag):** sections are roster-derived and inventing one ad
hoc is forbidden (README § Sections; `check_sections.py` reds an ORPHAN section against
the live roster) — curious-research is not a roster-derived section here, so this head
rides `ideas/fleet/`, flagged rather than silently squatting, exactly as the P041
curious-research head and the P019/P037 fleet-backlog heads did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** The effector-mount magnet tool — the first tool
on the arm's shared mount standard — retains its one working part, a neodymium disc, by a
press-fit pocket whose tightness is a single shipped constant
(`projects/effector-mount/magnet_tool.scad` @ `a9fd5fa`, lines 52 and 56–59, verbatim):

```
magnet_d      = 12.0;   // magnet DIAMETER (mm). Common discs: 10, 12, 15, 20.
```

```
magnet_fit    = 0.15;   // how much SMALLER the pocket is than the magnet (mm).
                        // 0.10-0.20 = a firm press-fit on most printers. Won't go
                        // in? Raise it (e.g. 0.25) or sand the magnet. Drops out?
                        // Lower it, or add a drop of glue.
```

The geometry consumes it at line 83: `pocket_d = magnet_d - magnet_fit;` — a DIAMETRAL
interference of 0.15 mm. Its own BENCH WORDS block (lines 40–41) names both failure axes:
*"press-fit : a pocket a hair SMALLER than the magnet so it wedges in and stays with no
glue. Loose? A drop of glue fixes it."* — and the file's SAFETY header (line 30) prices
the other side: *"Neodymium magnets are brittle"*. The README repeats the dial
(`projects/effector-mount/README.md` lines 113–117): *"The pocket prints this much
smaller than the magnet so it wedges in. If your printer runs tight and the magnet won't
seat, raise it; if the magnet drops out, lower it (or add a drop of glue)"* with the
inline echo `magnet_fit = 0.15;   // <- 0.10–0.20 firm press-fit; raise if too tight`.
The file has NEVER been printed — its own header (lines 22–24): *"authored with no
OpenSCAD installed, so this has NOT been rendered or sliced"*. So `0.15` and the claim
"a firm press-fit on most printers" are shipped, load-bearing, and never priced.

**The repo already owns the pricing instrument.** The SAME repo's tolerance-test-coin
project defines the band semantics this head needs
(`projects/tolerance-test-coin/tolerance-test-coin.scad` @ `a9fd5fa`, lines 26–28,
verbatim):

```
clear_min  = 0.10;   // smallest radial clearance to test (mm, per side)
clear_max  = 0.50;   // largest  radial clearance to test (mm, per side)
clear_step = 0.05;   // gap between tested clearances (mm)
```

with the unit rule at lines 14–16 (*"It is measured PER SIDE here: a hole labelled 0.20
has 0.20 mm of gap on every side, so the two sides add up to 0.40 mm across the diameter
-- the classic gotcha"*) and the band definitions in
`projects/tolerance-test-coin/clearance-results.md` lines 10–12 (verbatim):

```
- **Press** — tightest gap that pushed in firmly and held (no wobble).
- **Snug** — gap that slid in snug with no side-to-side play.
- **Loose** — gap where the pin dropped in and rattled.
```

and exactly ONE example row (line 36 — the repo's only filled row, shipped as a
delete-me exemplar; this file treats it as the PINNED EXEMPLAR and says so):

```
| Generic grey PLA | 2026-07-13 | 0.10 | 0.20 | 0.45 | 210 °C, 0.2 mm layer, elephant-foot 0.2 |
```

The coin's own doctrine (scad lines 9–11): *"the number engraved next to the best-feeling
hole is YOUR printer's real clearance number -- reuse it in every future design that has
to fit together."* The magnet tool is exactly such a design — and it ships a universal
constant instead. That tension is the head.

**A disclosed harvest observation (reporting-only, decidable by inspection — flagged,
never gated):** the geometry (line 83, `pocket_d = magnet_d - magnet_fit`) means RAISING
`magnet_fit` makes the pocket SMALLER, i.e. tighter — yet both shipped remedy texts point
the dial the other way: the scad comment says *"Won't go in? Raise it (e.g. 0.25)"* /
*"Drops out? Lower it"*, and the README says *"won't seat, raise it; if the magnet drops
out, lower it"* / *"raise if too tight"*. Under the shipped geometry each remedy as
written makes its failure WORSE. This is a doc/geometry sign inconsistency in the source
repo, quoted here so the manager can route the one-line doc fix lane-side on ANY ruling
(Q-0260 — this repo never edits curious-research files); the sim does not gate on it (a
monotonicity theorem, not a measurement).

**The falsifiable core.** Under a pinned printer/filament dimensional-variance model
whose calibration center is the repo's own exemplar coin row, does the shipped
`magnet_fit = 0.15` mm interference default land the as-printed joint in the PRESS band
(wedges in AND holds — the coin's own band semantics translated to interference), and at
what error rate does it instead produce DROPS-OUT (loose — the magnet falls off
mid-move) or UNSEATABLE (too tight — won't seat, crack risk on a brittle magnet)?
Feasibility is priced over a pre-registered fit grid, so the verdict either ratifies the
shipped default, replaces it with a better grid cell, or retires the universal-default
framing in favor of the repo's own calibrate-first coin doctrine.

**The pinned model (every constant exact and committed in this file — the P017–P048
hermetic precedent; all lengths INTEGER HUNDREDTHS of a millimetre (cmm), all DIAMETRAL
unless said otherwise — the coin's per-side values are doubled on entry per its own
lines 14–16; all probabilities exact `fractions.Fraction` on the equiprobable integer
lattice).**

- **Fit grid (the swept design constant).** `F ∈ {5, 10, 15, 20, 25, 30}` cmm
  (0.05–0.30 mm designed diametral interference) — brackets the scad's own narrative
  span (0.10–0.20 named "firm", 0.25 named in the remedy note) by one step on each side.
  The shipped default is the cell `F = 15`.
- **Exemplar calibration (pinned reading, disclosed).** The coin row's per-side designed
  clearances double to diametral 20 (Press) / 40 (Snug) / 90 (Loose) cmm. Pinned
  reading: SNUG ("slid in snug with no side-to-side play") ≡ zero effective as-printed
  gap, so the printed-pin-in-printed-hole pair's total systematic print offset is
  `S = 40` cmm; the hole's share is pinned at `ρ = 1/2` (a CHOICE, disclosed — the coin
  measures pin + hole combined; the H sensitivity pair below brackets it), giving the
  population CENTER of systematic hole undersize `H₀ = 20` cmm. The Press row then
  reads: actual interference 20 cmm seats and holds (in-band); the Snug row reads:
  actual interference 0 slides with no grip (below hold).
- **Printer/filament population.** `H ~ uniform integer {0..40}` cmm of systematic hole
  undersize (center = the exemplar's 20; the ±20 span is INVENTED, pinned, disclosed —
  the coin project's own premise is that printers differ enough to need per-printer
  calibration; sensitivity pair `{10..30}` narrow / `{−10..50}` wide, reporting-only —
  the wide leg admits slicer hole-compensated printers whose holes print oversize).
- **Per-print noise.** `η ~ uniform integer {−10..+10}` cmm diametral (print-to-print +
  around-the-bore variance at fixed setup — INVENTED, pinned, disclosed; sensitivity
  `{−5..+5}` / `{−20..+20}`, reporting-only).
- **Magnet diameter error.** `m ~ uniform integer {−5..+5}` cmm (catalog neodymium discs
  are ground far tighter than FDM bores; the magnet-vs-printed-pin asymmetry against the
  coin's world is named in Model basis — INVENTED, pinned, disclosed; sensitivity `{0}` /
  `{−10..+10}`, reporting-only). All three draws independent (named in Model basis).
- **Actual diametral interference.** `I(F) = F + H + m − η`.
- **Outcome bands (actual interference — the coin bands translated to hole-vs-magnet).**
  - **DROPS-OUT** iff `I < 10` (below hold: the exemplar's Snug point calibrates I = 0 as
    no-grip, its Press point calibrates I = 20 as held; `I_hold = 10` is the pinned
    midpoint of that bracket — sensitivity `{5, 15}`, reporting-only).
  - **PRESS** iff `10 ≤ I ≤ 50` (the design intent: wedges in and stays).
  - **UNSEATABLE** iff `I > 50` (`I_seat = 50` cmm = 0.50 mm diametral ≈ 4.2% hoop
    strain on the 12 mm bore, past hand-seating on rigid FDM walls — INVENTED, pinned,
    disclosed; sensitivity `{40, 60}`, reporting-only).
- **Metrics per F (exact).** `DROP(F)`, `UNSEAT(F)`, `FAIL(F) = DROP(F) + UNSEAT(F)` over
  the `41 × 11 × 21 = 9,471` equiprobable lattice cells; plus the glue-fallback view
  `FAIL_glue(F) = UNSEAT(F)` (the repo's own "a drop of glue fixes it" applied to every
  DROP), reporting-only.

**The two arms.**

- **Arm A — DECISION (seedless, exact).** Full enumeration of the 9,471-cell lattice per
  grid F; every probability an exact `Fraction`. Fully hermetic, byte-identical across
  process runs, no seed read. The ruling rides Arm A alone.
- **Arm B — VALIDATION (seeded MC).** Independently confirm Arm A by direct sampling:
  `N = 200,000` (H, m, η) scenario draws, pinned draw order H → m → η, COMMON RANDOM
  NUMBERS across all six F (one scenario set, six evaluations). Agreement gate:
  `|FAIL̂(F) − FAIL(F)| ≤ 1/100` absolute AND ≤ 4·se on every grid cell — any breach is
  a control failure (INVALID), never overridden. Arm B is validation only.

**Seeds (pre-registered, strictly above the P048 high-water 20261332 — sweep quoted in
Relations).**

- `20261333` — Arm B headline: the N = 200,000 common-random-numbers validation run
  across all six F cells (the agreement gate above).
- `20261334` — Arm B control: the zero-noise identity world (`η ≡ 0, m ≡ 0, H ≡ 20`) —
  `I = F + 20 ∈ [25, 50]` for every grid F, so every cell must return PRESS with
  probability EXACTLY 1 in both arms (exact identity, not a tolerance); any other value
  is a misbehaving control → INVALID.
- `20261335` — Arm B sensitivity confirmations: MC re-runs of the reporting-only
  sensitivity worlds (H narrow/wide, η narrow/wide, m degenerate/wide, I_hold {5, 15},
  I_seat {40, 60}), N = 20,000 each; reporting-only, can never flip the decision.
- `20261336` — stability leg: re-run the headline at N = 20,000; PASS iff the ruling
  class reproduces through the twin evaluators.

**Decision rule (pre-registered, evaluated in this order — REJECT checked FIRST; all
band constants exact rationals; decision numbers are Arm A's exact Fractions only).**

1. **REJECT** ("the shipped universal default is dishonest — across the pinned printer
   population it misses the PRESS band more than one print in ten, so the fit line's
   'on most printers' claim retires and the honest instruction is the repo's own
   calibrate-first doctrine: print the tolerance coin, put YOUR row's number in
   `magnet_fit`") iff `FAIL(15) > 1/10`.
2. **INVALID** (report, do not rule — controls misbehaving) iff the seed-20261334
   zero-noise identity fails in either arm, OR a monotonicity theorem gate fails
   (`DROP(F)` non-increasing and `UNSEAT(F)` non-decreasing in F — theorems under shared
   enumeration/common random numbers, so any violation is an implementation defect), OR
   Arm B breaches the agreement gate on any cell.
3. **APPROVE** ("the shipped default is right-sized for the pinned population") iff
   `FAIL(15) ≤ 1/20` AND `FAIL(15) ≤ min_F FAIL(F) + 1/100` (within one percentage point
   of the best grid cell) AND the seed-20261336 stability leg reproduces the ruling.
4. **NULL** — anything else; four pre-registered axes: (i) **band-miss** —
   `FAIL(15) ∈ (1/20, 1/10]` (works-mostly, short of ratification; the measured rate IS
   the finding); (ii) **wrong-center** — `FAIL(15) ≤ 1/20` but some grid F beats it by
   more than `1/100` (the default is serviceable but off-center; the better cell is the
   finding); (iii) **stability non-reproduction**; (iv) **sensitivity straddle** — a
   reporting-only world lands a primary conjunct on the other side of a band edge (the
   named axis is the finding; reporting legs never flip the decision).

**Liveness — expected landing DISCLOSED (closed-form decision arm; the P048-card norm:
when the decision arm is exact, withholding a computable landing is the dishonest
move).** Drafting-time hand check (stdlib `fractions`, NON-authoritative — the sim
re-derives everything from the pinned constants and must not trust these values):
`FAIL(5) = 145/861 ≈ 0.168` (DROP-heavy: DROP `125/861`), `FAIL(10) = 40/287 ≈ 0.139`
(the grid minimum, split evenly `20/287 + 20/287`), `FAIL(15) = 145/861 ≈ 0.168` with
the mass on the UNSEAT side (UNSEAT `125/861 ≈ 0.145`, DROP `20/861 ≈ 0.023`),
`FAIL(20) = 340/1353 ≈ 0.251`, `FAIL(25) = 15/41 ≈ 0.366`, `FAIL(30) = 20/41 ≈ 0.488`.
So the honest **expected landing is REJECT**: `145/861 > 1/10`, and even the grid's best
cell (F = 10) fails ≈ 13.9% — at the pinned population width NO universal default is
honest, which is precisely the coin project's own doctrine. Two sharpenings the sim
delivers beyond the sign: (a) the shipped 0.15 errs toward UNSEATABLE, the EXPENSIVE
direction — the repo's own glue line rescues a loose magnet but nothing un-cracks a
brittle one, so under the glue-fallback view `FAIL_glue(15) ≈ 0.145` barely improves
while `FAIL_glue(5) ≈ 0.023` collapses — the default sits on the wrong side of its own
asymmetry; (b) the per-H conditional curve names WHICH printers the default fails.
Falsifiability is real, not theater: the narrow-population sensitivity world lands
`FAIL(15) ≈ 0.045 ≤ 1/20` (the APPROVE/NULL region) and the `I_seat = 60` world lands
≈ 0.046, so the pre-registered bands genuinely discriminate — REJECT is a property of
the pinned population width, and the rule would rule differently at nearby pins.

**Reporting-only side pins (never gate the ruling).** (i) the full DROP/UNSEAT/FAIL × F
table with the DROP-vs-UNSEAT split per cell (the glue-asymmetry exhibit); (ii)
`FAIL_glue(F) = UNSEAT(F)` — the grid re-read under the repo's own one-drop-of-glue
remedy; (iii) the per-H conditional `FAIL(15 | H)` curve (which printers the default
fails); (iv) every sensitivity world named in the model (H, η, m, I_hold, I_seat); (v)
the remedy-direction observation quoted above, carried as a doc-fix flag.

**What a reader DOES differently on the verdict.**

- **APPROVE** → the fit line's "0.10-0.20 = a firm press-fit on most printers" gains its
  measured basis, routed lane-side per Q-0260 (this repo never edits curious-research
  files); the inverted remedy direction still routes as a one-line doc fix.
- **REJECT** → the universal-default framing retires: the fit comment becomes
  calibrate-first ("print `projects/tolerance-test-coin/`, put YOUR Press row in
  `magnet_fit`"), wiring the repo's two projects together — the coin finally gets the
  in-repo consumer its own doctrine promises; the remedy-direction fix rides along.
- **NULL** → the named axis ships with its measured table; the cheapest live probe is
  named below.

## Model basis — what is pinned vs a choice

- **The exemplar row is the repo's ONLY measured row** (shipped as a delete-me example).
  Pinning it as the population center is a disclosed necessity, not a measurement claim:
  no bench datapoint for the magnet tool exists anywhere in the fleet (the scad has
  never been rendered, by its own header). The sweeps bracket scale, not shape.
- **`ρ = 1/2` (the hole's share of the coin pair's offset) is a CHOICE**, disclosed; the
  H sensitivity pair {10..30}/{−10..50} brackets it in both directions.
- **The population width, η, m, I_hold, I_seat are INVENTED-but-pinned**, each disclosed
  inline with a reporting-only sensitivity pair. The steel-magnet-vs-printed-pin
  asymmetry is named: the coin calibrates printed-on-printed; this joint is
  printed-on-ground-steel, which is exactly why only the hole's share ρ·S enters.
- **Independence of H, m, η is an assumption**; the single most-likely-to-flip
  alternative is slicer/firmware hole compensation (many profiles enlarge small bores),
  which shifts the population center BELOW 20 — fewer UNSEAT, more DROP; direction
  stated, the wide-H leg brackets it, and the named live probe measures it directly.
- **Exact rationals throughout Arm A** — no float in the decision path; floats appear
  only in Arm B's empirical estimates and this file's `≈` annotations.
- **Cheapest live probe (pre-priced, on NULL or on demand):** print ONE tolerance coin
  and ONE magnet cup at the shipped default on the owner's printer and run the repo's
  own hand-fit test (README § "Hand-fit test — do this with the servo power OFF") — one
  print bed, zero new tooling; it pins H and both band edges for the one printer that
  matters first.

## Relations — dedup sweep (verify-first, live this slice)

Tree-wide sweep at drafting HEAD `dec6ec4` (ripgrep, kit excluded):
`rg -i -g '!bootstrap.py' -g '!.substrate' 'press.?fit|interference.fit|tolerance.coin|clearance|magnet' ideas/ control/outbox.md .sessions/` returns ZERO
domain hits in `control/outbox.md` and only four file hits, all non-domain: (a)
`ideas/fleet/spool-scale-go-no-go-margin-2026-07-13.md` — P041, the nearest prior (below);
(b) `ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md` — the makerbench gift-repo
BLUEPRINT, whose rows list "Tolerance test coin + fit calculator" and M3 clearance holes
as PLAN items (no sim head, no decision rule, no error model; ORDER 004 rule 4 keeps
makerbench unbuilt and this head does not touch it); (c)–(d) a websites idea file and its
session card where "clearance" is the VERDICT-003 approval sense, not a mechanical gap.
The seed sweep `rg -P '(?<![0-9])20261[0-9]{3}(?![0-9])' --glob '!results.json'` over
this tree AND /home/user/sim-lab (plus the range-notation companion) found max allocation
20261332 (P048), so 20261333–336 are clean.

**Nearest priors (disclosed, both distinct):**

- **P041 → V052 (same repo, DIFFERENT project — the disclosed second tap).** P041
  harvested `projects/spool-weight-scale/` and priced a GO/NO-GO MARGIN on a noisy stock
  estimate (do I have enough filament — a threshold gate on scale error). This head
  harvests `projects/effector-mount/` and prices INTERFERENCE-BAND PLACEMENT of a shipped
  design constant under population variance (does a fixed press-fit land a three-sided
  band). Different project subtree, different mechanism (margin sizing vs band
  placement), different failure structure (one-sided run-out vs two-sided
  drop-out/unseatable), zero shared fixture. Moreover P041's Relations explicitly
  weighed and DROPPED "curious-research tolerance-test-coin clearances" as a standalone
  head ("the doc's own point is that the answer is printer-specific — a sim would
  launder bench variance it cannot know"). This head does NOT resurrect that dropped
  head: the coin enters only as the repo's own BAND SEMANTICS plus one pinned exemplar
  row, the head under test is the effector-mount's shipped universal `magnet_fit`
  default, and printer-specificity is MODELED AS THE POPULATION SPREAD H — the exact
  structure whose absence made the dropped head unpriceable — rather than laundered
  into a single fake bench number.
- **P045 → V056 (method kin only).** The same "price a shipped, hedged default on its
  own two named failure axes over a pre-registered grid" MOVE (error-budget threshold
  shape: false-stale vs latency there, drop-out vs unseatable here), but its world is
  snapshot staleness in time — zero shared fixture, metric, or consumer. Method
  precedent, not overlap.

No prior proposal (001–048 re-scanned at HEAD), sim-lab verdict, idea file, or
session-card 💡 touches press-fit/interference fits, tolerance bands, dimensional
variance of printed parts, or any physical joint-retention rule.

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe over a pinned
> public repo, sim is report-only evidence, no spend/publish/irreversible surface —
> README § probe battery). Verify-first ran FIRST, live this slice: (a) **source
> verified at HEAD** — curious-research shallow-cloned, HEAD
> `a9fd5faa6a10b4d1364d205dbeac7a8678e1bd73` ls-remote-confirmed (unchanged since
> P041's pin); every harvested line quoted verbatim above with file + line numbers; the
> source repo's own `control/outbox.md` carries no SIM-REQUEST to duplicate. (b)
> **dedup** — the tree-wide sweep quoted in `## Relations` returned zero domain hits;
> the two nearest priors are disclosed with their distinguishing mechanism, including
> the P041-dropped-runner-up distinction. (c) **kill test NOT triggered** — no prior
> proposal, verdict, or 💡 touches interference fits or printed-part dimensional
> variance. (d) **feasibility + liveness arithmetic checked** — runtime bounded (Arm A
> is 6 × 9,471 lattice cells of integer comparisons; Arm B is one 200k loop + small
> legs; well under a minute, stdlib only); expected landing DISCLOSED with its exact
> drafting-time values (REJECT at the headline pin) per the P048-card norm for
> closed-form decision arms, with the sensitivity worlds shown to land in other bands
> so the rule genuinely discriminates.

**1. What is this really?** A pre-registered exact MEASUREMENT of a shipped, never-printed
design constant: does `magnet_fit = 0.15` mm land the as-printed magnet pocket in the
PRESS band (per the same repo's tolerance-coin band semantics) across a pinned
integer-lattice printer population, and at what DROP-OUT vs UNSEATABLE split — computed
as exact `Fraction` outcome probabilities by full enumeration (Arm A, the decision arm),
validated by a seeded common-random-numbers MC (Arm B), judged against bands fixed before
any code (REJECT `> 1/10` first, INVALID on misbehaving controls, APPROVE `≤ 1/20` and
within 1/100 of the grid best, NULL with four named axes), byte-identical across two
process runs.

**2. What is the possibility space?** (i) Don't run it — the round-9 fleet-backlogs slot
goes unserved. (ii) Re-harvest a fully-untapped repo — the remaining candidates
(pokemon-mod-lab is DARK per the reading path's own rule) are thinner than the second
project subtree of a repo whose backlog was built for exactly this pricing; the second
tap is disclosed, not hidden. (iii) A prose answer ("0.15 is fine, most guides say
0.1–0.2") — retells the same folklore the scad comment already ships, measures nothing.
(iv) A bench experiment — the RIGHT eventual step but owner hardware and owner hands;
the sim prices the decision NOW and its probe line names that exact bench step. (v) This
head: hermetic, exact-arithmetic, pre-registered, with the repo's own coin as the band
authority. (vi) Over-scope (thermal expansion, pull-force modeling in newtons, PETG vs
PLA material split, magnet chamfers) — named as follow-ups, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~150-line stdlib file: an exact lattice enumerator parameterized by (F, bands,
population) — reused for the headline, every sensitivity world, and the zero-noise
control — plus one seeded sampling loop. That single file yields the ratify/retune/retire
verdict on the shipped constant, the DROP/UNSEAT asymmetry exhibit, the per-printer
conditional curve, and a reusable band-placement error-budget pattern (the P041 margin
pattern's two-sided sibling) for any future fixed-allowance fit in the fleet.

**4. What breaks it? (assumptions made explicit)** (a) **The invented widths** — H span,
η, m, I_hold, I_seat carry no bench datapoint (disclosed; every one has a sensitivity
pair; the named probe measures the two that matter most). (b) **The ρ = 1/2 hole share**
— a choice bracketed by the H sensitivity pair, disclosed. (c) **Band placement could
cherry-pick** — all bands committed here BEFORE any code, REJECT checked first, the
expected landing DISCLOSED rather than hidden, and the sensitivity worlds shown to land
in other bands so there is no room to retrofit. (d) **The premise could silently fail** —
a broken enumerator would corrupt every cell; the zero-noise identity control (exact 1s,
not tolerances) and the two monotonicity theorems rule INVALID before any ruling issues.
(e) **Metric myopia** — the ruling is on band-landing probability, the quantity the
shipped comment claims; pull-force in newtons and long-term creep are out of scope and
named as follow-ups, not smuggled in.

**5. What does it unlock?** The fit line's folklore becomes a measured basis or a
calibrate-first doc fix wiring the repo's coin to its first in-repo consumer (routed
lane-side per Q-0260); the inverted remedy direction gets its citable flag either way;
the fleet gains the two-sided band-placement error-budget pattern (P041 priced a
one-sided margin; this is its natural completion); and the rotation ledger's
fleet-backlogs slot opens round 9 with a disclosed, mechanism-distinct second tap —
the precedent that a rich source repo can be re-harvested honestly.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment for the population claim: Arm A settles the ruling by exact
enumeration in under a second. For the one printer that actually matters first, the
named live probe (one coin + one cup + the repo's own hand-fit test) decides the
owner-local question at one print bed of cost — and it is pre-priced as the NULL/next
step, not a prerequisite.

**7. What would make this a mistake to run?** If the landing being disclosed made the
sim worthless — it does not: the value is the independent re-derivation, the MC
cross-check, the DROP/UNSEAT asymmetry split (which the hand check says indicts the
default's DIRECTION, not just its width), and the per-H curve, with REJECT/APPROVE/NULL
all reachable at disclosed nearby pins. If the head duplicated P041 or resurrected its
dropped runner-up uncritically — the Relations section shows it does neither. If the
sim were asked to validate the remedy-direction inversion — it is not: that is decidable
by inspection and carried as a quoted flag, not a gate.

**8. How will we know it worked?** A committed sim-lab report with: Arm A's exact
DROP/UNSEAT/FAIL × F table as `Fraction`s and float renderings; the glue-fallback and
per-H conditional columns; the verdict token (APPROVE / REJECT / NULL, or INVALID) against
the pre-registered bands; Arm B's headline agreement gate outcome on every cell; the
zero-noise control at exact 1s; both monotonicity theorems passing; every sensitivity
world's table; and a byte-identity note (two Arm-A process runs identical). A clean run
reproduces `FAIL(15) = 145/861` from scratch — or DISAGREES with it and pins the
drafter's arithmetic error, which the pre-registered rule then rules on honestly.

**Recommendation: sim-ready**
