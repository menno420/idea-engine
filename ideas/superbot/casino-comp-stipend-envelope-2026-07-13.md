# Comp/stipend envelope — price the LAST routed lever on the fee frame's surviving substrate

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot` (the hub's minigame/casino
> consolidation — the World seat's own night-run work; verification target
> `menno420/sim-lab` per the Q-0264 pipeline)
> **Sequence:** after VERDICT 025 (entry-fee ticket envelope, reject — "the fee
> frame cannot do it either", finalized this night), whose own recommendation
> names this head verbatim: "the comp/stipend envelope sim — the THIRD routed
> lever, now the last unpriced one (the natural successor head this REJECT
> routes)" — and before the World seat closes its fairness-lever triage.

**Origin:** drafted this slice under standing owner ORDER 003 (continuous
pipeline) + ORDER 004 rule 3's rotation — the GAME-MECHANICS slot, round 3
(round 1: PROPOSAL 020 → VERDICT 022, odds lever REJECTED; round 2: PROPOSAL
023 → VERDICT 025, entry-fee lever REJECTED). VERDICT 022 routed exactly three
non-odds levers to the World seat: rake-only PvP (priced FREE by its own
rake ≡ edge identity — even-money PvP with pot-rake r is G1 at e = r, no sim
needed), entry-fee-with-prize (priced by VERDICT 025: REJECT as a one-rule
house frame — the fee fixes SAFE, not SINK: T1's parent SAFE gap closed 57×
while T2/T3's SINK walls reproduced), and **session comp/stipend** — the one
lever no verdict has touched (sim-lab local clone @
`5e356ed7d255377cefedf4f6ede1544617bd0c89`, verdicts V001–V027 finalized;
`sims/verdict-025-ticket-envelope/REPORT.md` "Named follow-ups" block). The
consumer window is inbox ORDER 004's own verbatim text ("World's balance
pins"). Zero network reads even at drafting: both parents' committed
REPORT.md + results.json supply every anchor constant from the local clone.

## The idea (reasoned to its fuller form — Q-0254 duty)

Two verdicts have now measured the same tension from opposite sides. VERDICT
022: the odds lever cannot hold FUN ∧ SAFE ∧ SINK — its best cell (G1,
e=0.05, m=0.05) passed FUN 0.2738 and SINK 0.0895 and died only on SAFE
(0.1358). VERDICT 025: the fee structure closes exactly that SAFE gap — the
transposed cell T1 (t=0.05, c=5) passes ALL THREE bands (worst-policy P_wipe
0.0024, 57× under the parent's failure) and is the grid's ONE surviving cell
— but FUN is knife-edge there (0.2738 vs the 0.25 band) and dies outright at
the sink-firm take (t=0.10: FUN 0.1346), so the house is pinned to the
low-take row and its 5.2%-of-B₀ expected session price tag. The comp/stipend
lever attacks exactly the residual axis: the house RETURNS value on a
schedule the player cannot convert into variance — a stipend or rebate — so
FUN (which reads final wealth INCLUDING comp) can be bought back at takes
where the sink is firm. What no one has priced is the guard rail: comp is a
FAUCET. Every chip of comp is minted by the house, and a policy that farms
the comp while minimizing exposure to the take (wash-betting the qualifying
handle, chasing the rebate cap, harvesting a loss-rebate under optimal
stopping — the classic loss-rebate exploit) turns the casino from a sink
into a pump. So the successor question is a four-band race on the fee
frame's surviving substrate: the three inherited bands (FUN/SAFE/SINK, held
from BOTH parents BY DESIGN for cell-addressable comparison) plus a new
pre-registered **MINT** band — no swept policy, including a per-design
farmer family, may have positive expected session net including comp.

The three canonical comp designs have provably different band signatures,
which is what makes the sweep informative rather than decorative:

- **D1 qualified stipend** (S = σ·B₀ at session end, iff session handle
  ≥ B₀): shifts the FUN threshold without touching in-session walks — the
  grinder still faces the full take t. The candidate that threads FUN, SINK,
  and MINT simultaneously.
- **D2 handle rebate** (σ·F back per ticket, continuous, session cap
  2σ·B₀): buys the same reference-leg FUN as D1 (identity, asserted) but
  cuts the grinder's EFFECTIVE take to t − σ — it should re-arm SINK exactly
  where FUN needs σ large. The pre-registered self-defeat candidate.
- **D3 loss rebate** (ρ·(B₀ − final)⁺ at session end): CANNOT move FUN at
  all — a rebate on losses never lifts a losing session above B₀ for ρ ≤ 1
  (analytic identity, asserted in-sim). It buys SAFE only, and it is the
  design the optimal-stopping farmer attacks hardest. The "cashback"
  design, priced honestly.

Every outcome is decision-grade for the World seat: APPROVE hands the
consolidation a COMPOSED house row (the VERDICT 025 ticket frame + a comp
line) that unlocks the sink-firm take; REJECT closes the triage with all
three routed levers measured dead — the incumbent low-take row and rake-only
PvP are what remains; NULL ships the per-design signature table as the pin.

**The sim (fully hermetic — the PROPOSAL 017–026 precedent; every fixture is
a pinned constant committed with the sim, zero repo/network reads in the
verdict session):** integer-chip bankroll walks in exact F-units on the
VERDICT 025 frame, inherited BY DESIGN: B₀ = 1,000 chips; ticket price
F = 0.01·B₀ = 10; per-round ticket cap **c = 5 fixed** (both parents measured
the tight cap load-bearing: V022's "pin MAXBET ≤ 0.05·B₀" rider, V025's "c=5
is load-bearing" — at c ≥ 25 the greedy re-buyer wipes 0.12–1.00 of
sessions); prize shapes **T1 double-up** {2F w.p. (1−t)/2} and **T2 tiered**
{8F, 3F, 1F w.p. (1−t)·{0.05, 0.10, 0.30}} (E[prize] = (1−t)·F exactly, per
(shape, t), asserted in Fractions). **T3 jackpot is EXCLUDED BY CITATION,
not re-run:** V025 measured its SINK wall 0.148–0.346 and SAFE 0.275–1.000
across ALL (t, c), and comp weakly RAISES P_double (more end wealth, never
less) — monotonicity stated here and spot-asserted in-sim on one T3
reporting cell; a lever that only adds player value cannot rescue a shape
whose SINK already fails without it. Take grid **t ∈ {0.05, 0.10}** — the
surviving take and the FUN-dead sink-firm take; t ≤ 0.02 excluded by V025's
own measurement (grinder cap_frac 0.17–0.32, indeterminate — comp only
slows those walks further); t=0 control rides reporting-only. Comp designs
and sizes as above: D1/D2 over **σ ∈ {0.02, 0.05, 0.10, 0.20}**, D3 over
**ρ ∈ {0.2, 0.4, 0.6, 0.8}** (D3's size axis is its rebate rate; the
implied per-session house cost E[rebate]/B₀ is reported exactly per cell).
Decision cells: 2 shapes × 2 takes × 3 designs × 4 sizes = **48**, plus 4
σ=0 baseline cells (per shape × take) that must REPRODUCE V025's committed
rows — the VERDICT 016/018 baseline-leg discipline. Re-buy policies (V025
verbatim; b ≤ c and b ≤ ⌊bankroll/F⌋; b tickets = b independent draws):
**R1** b=1; **R5** b=min(5,·); **RG** greedy; **MC** chase b=min(2^L,·).
Profiles (V025 verbatim): **CASUAL** 100 rounds or bankroll < F — P_ahead =
P(final + comp > B₀), P_wipe = P(final + comp ≤ 0.1·B₀); **GRINDER** to
≥ 2·B₀ or ≤ 0.5·B₀ (wealth including comp: D2's rebate credits continuously;
D1/D3's end-comp folds in via shifted stop targets), hard cap 4,000 rounds,
> 1% cap-hits marking the cell indeterminate (a NULL path, never silently
absorbed; measured P_double stays a LOWER bound so SINK failures stand);
**COMPULSIVE** reporting-only, R1, to ruin or 20,000 rounds. **FARMER family
(the MINT attack, per design):** D1 wash-qualifier — R1 for exactly 100
rounds (minimum qualifying handle), stop, collect; D2 cap-chaser — R1 until
the rebate cap or 2,000 rounds, stop; D3 stopper grid — b ∈ {1, 5} × target
τ ∈ {1.1, 1.25, 1.5}·B₀ × floor φ ∈ {0, 0.5·B₀}, stop-and-collect, 12
variants, max EV taken. **Bands (evaluated per cell, determinate cells
only):** FUN — reference-leg (R1) P_ahead ≥ 0.25; SAFE — max-policy P_wipe
≤ 0.05; SINK — max-policy P_double ≤ 0.10 (all three inherited verbatim from
V022/V025 BY DESIGN); **MINT** — max over the 4 swept policies AND the
farmer family of E[session net including comp] ≤ 0 (weak inequality; the
σ = t knife-edge, where D1/D2 farmer EV = 0 exactly, is disclosed and its
cells marked boundary). **Arm A (analytic, seedless, exact rationals):** FUN
for ALL cells — T1 via `math.comb` binomial with the comp-shifted ahead
threshold (R1 reference: ahead iff wins > 50 − 50σ for D1/D2; the σ=0
baselines must equal V022/V025's committed Fractions by EXACT rational
equality — 0.46020538… at t=0, 0.27375402… at t=0.05, 0.13457621… at
t=0.10), T2 via V025's exact integer-support DP convolution with the
shifted line; the identities D1-FUN ≡ D2-FUN (reference leg) and D3-FUN ≡
baseline-FUN asserted exactly; D1/D2 farmer EV closed form (σ − t)·B₀ (D2
clamped by its cap) — the pump line σ = t asserted; D3 stopper EV and
P_double via exact bounded-state DP on T1 (integer F-units); the t=0
optional-stopping control P_double = 1/3 exactly (both parents' control).
**Arm S (seeded MC):** `random.Random(20260752)`, pinned loop order (shape
T1→T2, t ascending, design D1→D2→D3, size ascending with the σ=0 baseline
first, policy R1/R5/RG/MC → reference → farmer variants, profile casual →
grinder → compulsive, replications sequential, one `rng.random()` per
ticket); M = 5,000 casual / 2,000 grinder / 500 compulsive per cell-policy;
Arm S must agree with Arm A within 1.0 pp absolute on every Arm-A-covered
cell or the run is invalid; half-M decision-stability leg seed 20260753 must
reproduce the same ruling; reporting legs seed 20260754 (t=0 control,
compulsive, the house-net table, the T3 monotonicity spot cell, and the
per-round aggregated-draw spot check — 1,000 rounds, must reproduce the
per-ticket kernel, the PROPOSAL 017 breakpoint-clause precedent); aux
self-check stream seed 20260755, never read by any decision number. Seeds
20260752–55 allocated strictly above the PROPOSAL 026 registry high-water
20260751. Feasibility: T1 legs are largely analytic; the MC volume is below
V025's (48 + 4 cells at c=5 only — no c=100 leg), which ran ~5.2 min; stdlib
only, CPython minor pinned, stdout + results.json byte-identical across two
process runs.

**Pre-registered target cells, bands and decision rule** (set BEFORE any
code runs; evaluated in this order):

- **Target cells** — the parents' measured failures adjacent to survival:
  **C1 = (T1, t=0.10)** — the FUN-dead sink-firm take (baseline FUN
  0.13457621…, V022's committed G1 e=0.10 value, V025-identical binomial);
  **C2 = (T2, t=0.05)** — the SAFE near-miss (V025: worst-policy P_wipe
  0.0608 vs the 0.05 band, binding policy RG, its SINK/FUN passing).
  **Rescued** := all four bands (FUN ∧ SAFE ∧ SINK ∧ MINT) pass at that
  (shape, take) for some (design, size), determinate cells only.
- **REJECT** ("the third lever falls — the triage is complete") iff NO
  (design, size) rescues C1 AND none rescues C2, in both arms where covered
  — all three of VERDICT 022's routed levers are then measured dead (odds
  V022, fee V025, comp here); the World seat keeps the incumbent row (T1,
  t=0.05, c=5, no comp) as the only house-bankable cell and routes
  everything else to rake-only PvP (already priced free by the parent's
  rake ≡ edge identity); the verdict quantifies, per design, the binding
  band at that design's best cell.
- **APPROVE** ("comp completes the casino") iff some design D\* rescues C1
  with ≥ 2 CONSECUTIVE sizes all-four-pass (a band, not a knife-edge),
  stability-reproduced → recommended COMPOSED house row: the VERDICT 025
  ticket frame + the comp line (design, size band, qualifying rule), with
  the house-net-per-session table attached — whether (t=0.10 + comp)
  dominates the incumbent (t=0.05, no comp, 5.2%·B₀ expected session cost)
  at equal-or-better FUN.
- **NULL** otherwise — a legitimate reportable outcome: C2-only rescues,
  single-size knife-edges, MINT-boundary-only passes, or indeterminate
  cells in the passing set. The per-design signature table IS the pin, with
  the flip axis named via per-axis pass shares — expected candidates: the
  DESIGN axis (D3 provably cannot move FUN; D2's continuous rebate cuts the
  grinder's effective take to t − σ and should re-arm SINK exactly where
  FUN needs σ ≥ 0.05 — the pre-registered race is whether D1's
  end-of-session qualification threads FUN, SINK, and MINT simultaneously
  at (t=0.10, σ ∈ {0.05, 0.10})) and the σ = t mint knife-edge.
  Indeterminate cells route to NULL, never to APPROVE.

**Chained anchors (reporting-only, cannot flip the decision):** (i) the σ=0
baseline cells vs V025's committed rows — T1 (t=0.05, c=5) {FUN exact
0.27375402…, worst-policy P_wipe 0.0024, P_double 0.0000 measured /
4.5e−05 uncapped exact} and the C2 cell's 0.0608 wipe; (ii) the FUN
Fractions vs V022's committed G1 values (exact rational equality — the
grid's third chained verdict on one binomial); (iii) the t=0 control; (iv)
the house-net price tag per all-pass cell vs the incumbent 5.2%·B₀ (casual)
/ 25.2%·B₀ (worst policy) — V025's measured expected-loss row.

**Consequence:** on APPROVE — the consolidation adopts the composed row
(ticket quantum + cap + take band + comp line), the sink-firm take unlocks,
and the per-game balance question stays a one-line declaration check (prize
table + comp participation). On REJECT — the World seat's fairness-lever
triage CLOSES with all three routed levers measured: tonight's consolidation
ships the incumbent V025 row as the only house-banked cell and routes casino
ambitions to rake-only PvP; no design effort goes to comp schemes that
measurably mint or self-defeat. On NULL — the per-design signature table
ships as the pin (e.g. "stipend rescues FUN only at the mint knife-edge;
cashback buys SAFE, never FUN; handle rebate re-arms the grinder"), and
neither "comp fixes it" nor "comp is dead" may be cited as settled.
Boundaries, stated: all conclusions are bankroll-RELATIVE — nothing here
prices the casino sink against fishing/mining faucet mint in absolute
chips/hr; the live earn-rate baseline whose absence V001/V008 named (and
V022/V025 restated) stays walled, the telemetry caveat applies verbatim.
Tickets are i.i.d. (strategy spread folds into the take as REALIZED take).
Comp accounting is PER-SESSION: cross-session comp banking is out of scope,
and the multi-session mint rate is bounded linearly by the per-session
farmer EV the MINT band caps (stated). The finite policy + farmer sets
bracket unit, bounded, greedy, loss-chasing, wash-qualifying, cap-chasing,
and optimal-stopping behavior (stated, not proven). The FUN/SAFE/SINK lines
are the parents' pre-registered judgments, held BY DESIGN; full curves ship
so a re-drawn line re-reads, never re-runs.

## Model basis

The number rides on the i.i.d. ticket-walk family with LINEAR comp
accounting (every comp chip is worth one chip, sessions independent). The
single most-likely-to-flip alternative: comp-triggered BEHAVIOR change —
real comp schemes alter session frequency and stake appetite (comp as
marketing), which no within-session walk can see. That axis is deliberately
the same measurement as the NULL-case live probe: if the consolidation
ships any comp line, the cheapest reality check is session-frequency
telemetry before/after the comp toggle on one game — zero new balance sims.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–026, re-read at HEAD `0716140`): nearest by
  every axis is **PROPOSAL 023 → VERDICT 025** (offset per sim-lab's own
  `finalizes-as` lines, never derived) — the parent, deliberately: same
  frame (its surviving substrate inherited cell-for-cell), same three
  bands. Its answered question (can the FEE frame be the one house rule?
  REJECT) is settled and not re-asked; this head prices the LAST routed
  lever ON that frame, adds the MINT band and the farmer family (neither
  exists in any prior grid), and its own "Named follow-ups" block requests
  this sim verbatim. **PROPOSAL 020 → VERDICT 022** is the grandparent
  (odds lever, REJECT; source of the lever list and the bands). PROPOSAL
  009 touches the same wager seams but asks correctness, never balance;
  PROPOSALs 015/016 → VERDICTs 017/018 are pacing, settled. PROPOSALs
  017–019, 021–022, 024–026 are method precedent only (hermetic
  pre-registered dual-arm grids; zero shared domain).
- vs the ORDER 004 lead list, judged on merit: superbot-idle T11+ rebuy
  pacing is REGISTERED LANE-SIDE by P015's own card ("Registering T11 WITH
  the mechanic's landing PR honors economy-v1.md's own verdict semantics")
  — not an open sim head tonight; mining/fishing reward-pacing pins hit the
  V001/V008 earn-rate-baseline wall directly (both verdicts ruled absolute
  rates unpineable without the named telemetry); a browser-game
  session/difficulty pin has no committed in-tree baseline to chain to
  tonight. This head is the only game-mechanics candidate with a same-night
  verdict chain requesting it by name.
- vs superbot's harvested backlog (237 docs, this section's README):
  `wager-flow-map` (parked(routed)) maps where money moves, never what the
  house should return; `giveaway-competitive-teardown` is FREE-entry
  giveaway research (a giveaway is 100% comp and 0% game — the degenerate
  corner this grid's MINT band prices, not a balance question there);
  `games-economy-faucet-sink-diagnostic` is observational. Grep of the
  index for comp/stipend/rebate/cashback/loyalty: nothing else.
- Tree-wide dedup sweep (`rg -i -g '!bootstrap.py' -g '!.substrate'` for
  comp/stipend / rebate / cashback / rakeback / loss-rebate / loyalty over
  ideas/ + .sessions/ + control/ + docs/ and the sim-lab clone @ `5e356ed`):
  hits are ONLY the two parents' own lever lists and routing lines
  (PROPOSAL 020/023 text, VERDICT 022/025 reports) — no proposal, idea
  file, card, or verdict prices a comp design anywhere; no verdict V001–
  V027 contains a MINT/faucet band or an exploit-policy (farmer) leg.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained probability-model
> head, sim is report-only evidence, no spend/publish/irreversible surface —
> README § probe battery). Verify-first ran FIRST, live this slice, zero
> network reads: (a) **grounding** — both parent verdicts are committed
> evidence in the local sim-lab clone @ `5e356ed`
> (`sims/verdict-022-casino-fairness/`, `sims/verdict-025-ticket-envelope/`:
> rulings, the routed lever list, the surviving cell row 0.2738/0.0024/
> 0.0000, the C2 near-miss 0.0608, the T3 walls, the follow-ups block naming
> this head); the consumer window is inbox ORDER 004's own verbatim text
> ("World's balance pins"). (b) **dedup** — the sweeps above. (c)
> **feasibility arithmetic** — in the sim-spec paragraph; no leg heavier
> than V025's measured 5.2-minute run.

**1. What is this really?** A pre-registered four-band envelope sweep for
the comp/stipend lever on the fee frame's measured surviving substrate: can
a stipend, handle rebate, or loss rebate buy FUN back at the sink-firm take
(or close the tiered shape's SAFE near-miss) without any swept policy —
including a per-design farmer family — extracting positive expected value
from the house (the MINT band), with a dual analytic arm (exact binomials,
DP convolutions, ruin/stopping DPs, closed-form pump lines) pinning the
seeded MC, and every baseline cell reproducing the parents' committed
numbers exactly.

**2. What is the possibility space?** (i) Don't run it — the triage VERDICT
022 opened stays two-thirds priced forever, and the consolidation either
forgoes the lever or ships a comp scheme against an untested faucet. (ii)
Trust the lever's intuition — but the loss-rebate exploit is the oldest
positive-EV trick in casino history, and an unpriced comp line is exactly
the invented constant this program exists to kill. (iii) Ask the owner —
zero evidence attached, strictly worse after two verdicts priced the
sibling levers (Q-0263.2). (iv) This head: 48 cells, four bands, three
design signatures, REJECT and NULL both decision-grade. (v) Over-scope
(cross-session comp banking, dynamic comp tiers, comp-as-marketing
behavior) — named boundaries; the Model basis names the live probe.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~350-line stdlib file: the V025 ticket kernel shape
plus a comp-accounting layer and a farmer-policy family, exact
binomial/DP/stopping arms, and a 48-cell four-band table that CLOSES a
three-verdict triage — the program's first three-generation chained verdict
line (V022 → V025 → this), every generation sharing bands and cell
addresses.

**4. What breaks it? (assumptions made explicit)** (a) **Linear per-session
comp accounting** — no cross-session banking; the multi-session mint rate
is per-session farmer EV × sessions, linear, so the MINT band caps it
(stated). (b) **i.i.d. tickets** — realized take folds strategy spread into
t. (c) **Finite policy + farmer sets** — R1/R5/RG/MC plus the three farmer
attacks bracket the behavior space; the D3 stopper grid is 12 variants, not
an optimum proof (max over the grid is a LOWER bound on the exploit — a
MINT failure stands, a MINT pass at the D3 boundary is marked). (d)
**Boundary effects** — integer F-units, qualification exactly at handle =
B₀, the σ = t knife-edge; the identities (D3-FUN ≡ baseline, D1 ≡ D2
reference FUN, pump line EV = (σ−t)·B₀, t=0 → 1/3) catch kernel bugs before
any cell is believed. (e) **PRNG stability** — seeds 20260752–55 fresh
above the P026 high-water 20260751, loop order pinned, CPython minor
pinned.

**5. What does it unlock?** The World seat's fairness-lever triage ENDS —
every routed lever priced by measurement within one night: APPROVE composes
the first complete house rule (structure + comp) and unlocks the sink-firm
take; REJECT retires the last lever with quantified gaps and pins the
incumbent row + rake-only PvP as the casino's whole design space; NULL pins
which comp design buys which band. Plus the reusable shape: a MINT band and
a farmer family any future economy sim (loyalty points, daily bonuses,
season passes) can import.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at sim time — every fixture ({B₀, F, c, shapes, t-grid, design
definitions, σ/ρ grids, policy and farmer constants, profile stop rules, M
per profile, seeds, band constants, anchor constants}) is stated in this
file and committed as JSON alongside the sim. Kill tests, run live this
slice: a prior comp/stipend balance head anywhere in either tree (NOT found
— sweeps above), a sim-lab verdict covering the lever (NOT found — V025's
own follow-ups block routes it here), the consolidation having already
picked (NOT found — V025 finalized this same night; the third lever rode
unpriced), infeasible runtime (NOT found — lighter than V025's measured
run). Sim-worthy or judgment-only: sim-worthy — bounded-walk tails and
exact EV lines against pre-registered thresholds; the judgment questions
(the band lines) were settled by the parents' pre-registrations and are
inherited unchanged, which is the comparability contract.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (its harness, its verdict grammar; the verdict-022/-025
dirs are the sibling precedents — V025's kernel shape is reusable art).
The verdict's consumer is the superbot World seat's minigame/casino
consolidation, with superbot-games inheriting the row if house-banked games
land plugin-side (the V018 shared-surface precedent). Duplicates nothing:
V022 killed odds, V025 killed the fee-as-house-rule and measured the
surviving substrate; this prices the last routed lever ON that substrate —
successor, not re-run.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one
stdlib file (ticket kernel + comp layer + farmer family + analytic arm),
one fixture JSON (all constants copied verbatim from this file), one
results table {P_ahead, P_wipe, P_double, E[session net], farmer EVs,
cap-hit fraction, house-net} × (shape, t, design, size, policy) plus the
rescue summary for C1/C2 and the chained anchors — ending in exactly one of
APPROVE/REJECT/NULL per the pre-registered rule, reproducible from the
fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the
bands and decision rule (with stated evaluation order) are registered above
BEFORE any code exists, the parent verdict itself routed the head by name,
and every outcome closes or pins the World seat's lever triage. THE ONE
QUESTION for the simulator: *Under the pinned comp-envelope model on VERDICT
025's surviving ticket substrate (B₀ = 1,000 integer chips; F = 10; cap
c = 5 fixed; shapes T1 double-up {2F w.p. (1−t)/2} and T2 tiered {8F, 3F, 1F
w.p. (1−t)·{0.05, 0.10, 0.30}} with E[prize] = (1−t)·F exact and T3 excluded
by V025's measured walls + comp monotonicity; takes t ∈ {0.05, 0.10} + t=0
control; comp designs D1 qualified stipend σ·B₀ at session end iff handle
≥ B₀, D2 handle rebate σ·F per ticket continuous with session cap 2σ·B₀,
D3 loss rebate ρ·(B₀ − final)⁺ at session end — D1/D2 over σ ∈ {0.02, 0.05,
0.10, 0.20}, D3 over ρ ∈ {0.2, 0.4, 0.6, 0.8}; 48 decision cells + 4 σ=0
baseline cells that must reproduce V025's committed rows; re-buy policies
R1/R5/RG/MC and profiles CASUAL/GRINDER/COMPULSIVE verbatim from V025 with
comp counted in final wealth; farmer family per design — D1 wash-qualifier,
D2 cap-chaser, D3 12-variant stopper grid; Arm A exact — comp-shifted
binomial/DP FUN for all cells with the σ=0 Fractions equal to V022/V025's
committed values by exact rational equality, the D3-FUN ≡ baseline and
D1 ≡ D2 reference identities, the (σ − t)·B₀ pump line, the D3 stopper DP,
and the t=0 P_double = 1/3 control; Arm S seeded `random.Random(20260752)`
M = 5,000/2,000/500 with the 1.0 pp agreement gate, half-M stability leg
seed 20260753, reporting legs seed 20260754, aux stream seed 20260755), for
which (design, size) cells do FUN (reference P_ahead incl. comp ≥ 0.25),
SAFE (max-policy P_wipe incl. comp ≤ 0.05), SINK (max-policy P_double incl.
comp ≤ 0.10), and MINT (max over policies ∪ farmers of E[session net incl.
comp] ≤ 0) hold simultaneously — and do any RESCUE the pre-registered
target cells C1 = (T1, t=0.10) (the FUN-dead sink-firm take, baseline
0.13457621…) and C2 = (T2, t=0.05) (the SAFE near-miss, 0.0608) — landing
REJECT (no cell rescues C1 and none rescues C2 → all three routed levers
measured dead; the incumbent row + rake-only PvP are the casino's whole
design space, per-design binding bands quantified), APPROVE (some design
rescues C1 with ≥ 2 consecutive sizes, stability-reproduced → the composed
house row: V025's ticket frame + the comp line, house-net table attached),
or NULL (anything else → the per-design signature table is the pin, flip
axis named via per-axis pass shares — expected candidates the design axis
and the σ = t mint knife-edge; indeterminate cells route to NULL, never
APPROVE)?* Done-when: the committed sim + fixture JSON reproduce the full
four-band results table, the C1/C2 rescue summary, and the chained anchors
(the σ=0 baselines vs V025's committed rows and V022's G1 Fractions; the
t=0 control; the house-net price tag vs the incumbent 5.2%·B₀)
byte-identically, Arm S passes the agreement gate, all four analytic
identities hold, the stability leg reproduces the same ruling, and the
verdict issues exactly one of APPROVE/REJECT/NULL per the pre-registered
rule (evaluation order stated) with the bankroll-relative boundary, the
V001/V008 earn-rate caveat restated verbatim, the per-session comp-
accounting boundary, and the reporting-only legs (t=0 control, compulsive
harm context, T3 monotonicity spot cell, house-net table) stated as legs
that cannot flip the decision.
