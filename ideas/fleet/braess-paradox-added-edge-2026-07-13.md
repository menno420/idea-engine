# Braess's paradox in small routing networks — how often, and by how much, does adding a shortcut edge RAISE selfish travel time?

> **State:** sim-ready
> **Class:** process (pipeline rotation — inbox ORDER 004 rule 3's COMPLETELY-UNRELATED-domain
> slot, round 2; the domain itself is transportation / congestion routing games —
> Wardrop selfish-user equilibrium — fleet-external by design and DIFFERENT from
> PROPOSAL 017's social-choice domain, so the rotation demonstrably spans domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3 ("Rotate lanes deliberately: … → COMPLETELY UNRELATED domains
(I want those too)") — PROPOSAL 017 opened round 1's unrelated-domain lane with social
choice (instant-runoff monotonicity); this is round 2's unrelated-domain head, rotated
into a fresh fleet-external domain (transportation / congestion routing games) so the
rotation spans domains rather than re-mining one. **Placement note (decide-and-flag):**
sections are roster-derived and inventing one ad hoc is forbidden (README § Sections;
`check_sections.py` reds an ORPHAN section against the live roster), and that checker's
own carve-out rules that sim-lab-shaped ideas "ride `ideas/fleet/` or the proposing
section" — so this fleet-external head lives here, flagged rather than silently
squatting, exactly as PROPOSAL 017 did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**Braess's paradox** is the counter-intuitive fact that ADDING a road (an edge) to a
congested network can RAISE every user's equilibrium travel time under selfish routing:
each driver greedily takes the new shortcut, the shortcut floods, and the new
user-equilibrium is worse for everyone than the network without it. That this CAN
happen is textbook — the canonical Braess diamond is in every game-theory course, and
real-world instances (a closed street in Seoul/Stuttgart/New York that *improved* flow)
are cited as folklore. What is genuinely UNMEASURED is how OFTEN and by HOW MUCH:
across a natural, constructible family of small networks, is the paradox a vanishingly
rare curiosity, or is it common/large enough that a designer adding a "shortcut" edge to
any selfishly-routed system (a road network, or any greedy self-routing multi-agent
flow) should audit for it BEFORE shipping the edge? This mirrors the accepted PROPOSAL
017 pattern exactly: non-monotonicity of IRV is POSSIBLE (a theorem) — its FREQUENCY in
close races was the measured unknown. Here Braess's EXISTENCE is settled; its
FREQUENCY and MAGNITUDE in a natural family are not — so NULL (the effect is real but
neither common nor large enough for a blanket design rule) is a live, reportable
outcome, not a fudge.

**Fixed topology (the classic Braess diamond + bridge).** Nodes s, a, b, t. Base edges
e1 = s→a, e2 = a→t, e3 = s→b, e4 = b→t. "Without bridge": two disjoint routes
R1 = s→a→t (edges e1,e2) and R2 = s→b→t (edges e3,e4). "With bridge": add the directed
edge e5 = a→b, enabling the third route R3 = s→a→b→t (edges e1,e5,e4). A unit demand
D = 1 is routed from s to t so that each user minimizes their OWN latency (Wardrop /
user equilibrium: no user can switch route and lower their own travel time). Each edge e
carries an affine latency `l_e(x) = a_e·x + b_e` where x is the flow on that edge and
a_e ≥ 0. For affine non-decreasing latencies the Wardrop equilibrium edge-flow vector is
UNIQUE (it is the minimizer of the strictly convex Beckmann potential
Φ(x) = Σ_e (a_e·x_e²/2 + b_e·x_e) over feasible s→t flows of value 1), so the sim is
fully DETERMINISTIC and exactly computable: enumerate the finite set of route-support
patterns, solve the latency-equalization linear system in exact `fractions.Fraction`,
and keep the unique feasible/optimal one. Total travel cost
`C = Σ_e x_e·l_e(x_e) = Σ_e x_e·(a_e·x_e + b_e)` (equivalently the demand-weighted path
latency at equilibrium). No floats anywhere in this arm.

**Arm A — exhaustive integer census (hermetic, no PRNG).** Enumerate
(a_e, b_e) ∈ {0,1,2}×{0,1,2} independently for each base edge e1..e4, and
(a5, b5) ∈ {0,1}×{0,1} for the bridge → a fixed finite census of 9⁴·4 = 26,244 raw
fixtures. Skip degenerate fixtures whose without-bridge equilibrium cost is 0 (report
the effective census N after the skip). For each surviving fixture compute the
equilibrium total cost WITHOUT the bridge (`cost_without`) and WITH the bridge
(`cost_with`), both exact `Fraction`. Then:
- **f_A = (# fixtures where cost_with > cost_without) / N** — the paradox frequency.
- Among the paradox fixtures (cost_with > cost_without) form the inflation ratio
  **r = cost_with / cost_without**; report **median r** and **max r**.

**Arm S — seeded Monte-Carlo robustness (continuous coefficients).** Draw
a_e ~ U[0,2] and b_e ~ U[0,2] continuously (all five edges), N_draws per seed, with
the four pinned seeds **20260740, 20260741, 20260742, 20260743** (freshly allocated
above the PROPOSAL 023 registry high-water 20260733 — the seed-registry hygiene the
P020/P021/P022/P023 cards carried, extended one slice; noted here so the next head
continues the sweep from one file). `random.Random(seed)` only; documented float
tolerance for the "cost_with > cost_without" comparison (a paradox counts only when it
clears the tolerance, so knife-edge float noise cannot inflate f_S). Report **f_S** as
the pooled paradox frequency across the four seeds. Purpose: guard against an
integer-grid MODELING ARTIFACT — if the discrete {0,1,2} grid over-represents paradox
corners, the continuous draw exposes it.
**Arm-agreement gate (the P017 dual-arm discipline):** the verdict requires BOTH
`|f_S − f_A| ≤ 1.0 pp` AND that the two arms yield the SAME APPROVE/REJECT/NULL call.
If the arms disagree on the call, the verdict is **NULL-by-arm-disagreement** — a
legitimate reportable outcome, not a retry.

**Pre-registered decision bands (fixed BEFORE any run — honest guesses, not tuned).**
- **APPROVE** ("an added-edge Braess audit is warranted") iff `f_A ≥ 0.15` **OR**
  `median-r-among-paradox ≥ 1.15`.
- **REJECT** ("added edges are safe-by-default in this class") iff `f_A ≤ 0.03`
  **AND** `max-r ≤ 1.05`.
- **NULL** (the straddle): anything not fully meeting APPROVE or REJECT — e.g. moderate
  frequency with small inflation, or rare-but-occasionally-large. Also NULL if the two
  arms disagree on the call (NULL-by-arm-disagreement).

**What a reader DOES differently on the verdict (so the ruling is actionable, not
trivia).**
- **APPROVE** → when adding a "shortcut" / extra link to any selfishly-routed system (a
  road network, or any greedy self-routing multi-agent flow), run a Braess check BEFORE
  shipping it; added capacity is NOT monotonically good, and this class carries a
  quantified rate to cite.
- **REJECT** → treat added edges as safe-by-default in this class; skip the design-time
  Braess audit (measured rare AND small exactly where it was supposed to bite).
- **NULL** → the honest outcome: the risk is real but not common/large enough for a
  blanket rule; audit only high-stakes networks case-by-case, and neither "Braess is a
  real design hazard" nor "Braess is a textbook curiosity" may be cited as settled here.

**Grounding / hermeticity.** ZERO network reads at verdict time. Arm A is a
self-contained integer enumeration; Arm S uses only stdlib `random` seeded by the
pinned constants above; all arithmetic is exact `fractions.Fraction` (Arm A) or float
under a documented tolerance (Arm S). No committed fixtures are needed beyond the pinned
topology and coefficient ranges — the entire world is constructible in-sim.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (001–023): nothing adjacent by DOMAIN — 001–016 and 020–023 are fleet
  product / game-mechanics / fleet-meta heads, 017 is social choice, 019 is fleet
  backlogs. Nearest by METHOD only: PROPOSAL 017 (pre-registered dual-arm sim, exact
  enumeration + seeded MC, honest-NULL band) — this head reuses that discipline
  wholesale but shares NO domain, NO fixture, NO consumer. A tree-wide sweep
  (`rg -i 'braess|wardrop|congestion|price of anarchy|selfish rout|routing game|traffic'`,
  bootstrap.py and .substrate excluded) finds ZERO prior routing-game / congestion
  content anywhere in ideas/, .sessions/, or control/.
- Runners-up this slice deduped and dropped: prisoner's-dilemma tournament-strategy
  frequency (method-adjacent to the game-mechanics heads P015/P016/P020/P023 — weakest
  "completely unrelated" claim) and epidemic R0 threshold-crossing frequency (clean, but
  its control arm is monotone by construction, so half the sweep is foregone — the same
  disqualifier P017 flagged for Hamilton apportionment).

## Model basis (dogfooding this slice's 💡 — declared model-dependence)

This verdict's number is CONDITIONAL on an embedded behavioral model, so — per this
slice's session 💡 (an optional `model-basis:` outbox field making model-dependence an
auditable, declared part of every non-pure-arithmetic verdict) — the two modeling
choices the number rides on are named up front:
- **(1) Behavioral assumption:** selfish **Wardrop user equilibrium** (each user
  minimizes own latency) over an affine latency model with coefficients drawn from a
  **uniform grid/range** ({0,1,2} integers in Arm A, U[0,2] in Arm S). The measured
  frequency is a property of THIS routing behavior on THIS coefficient distribution.
- **(2) Single most-likely-to-flip alternative:** the **system-optimal** routing
  objective (minimize TOTAL latency, not each user's own) — under which Braess's
  paradox cannot occur at all (adding an edge weakly lowers the system optimum), so the
  frequency would collapse to 0. A softer flip: a non-uniform coefficient prior
  concentrated away from the paradox-prone corners would move f without changing the
  behavioral assumption. Naming these makes explicit that an APPROVE/REJECT here rules
  on selfish-routing-under-uniform-coefficients, and a reader swapping to
  system-optimal or a skewed prior is outside the verdict's registered scope.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> routing-game sweep above returned ZERO hits; PROPOSALs 001–023 re-read at HEAD
> `15d1802` before drafting. (b) **kill test NOT triggered** — no prior proposal, idea
> file, or session-card 💡 touches routing games, congestion, Braess, Wardrop, or any
> transportation domain; this is round 2's unrelated-domain slot and is a DIFFERENT
> domain from round 1's social-choice occupant (P017). (c) **feasibility arithmetic
> checked** — Arm A is 26,244 fixtures × two tiny linear-system solves each (≤3 routes,
> exact Fraction); Arm S is 4 seeds × N_draws × the same O(1) solve; both are seconds to
> low minutes in pure CPython, no dependencies.

**1. What is this really?** A pre-registered MEASUREMENT settling whether adding a
shortcut edge to a small selfishly-routed network is a real design hazard or a textbook
curiosity — by measuring the FREQUENCY (f_A, f_S) and MAGNITUDE (median/max inflation
ratio r) of Braess's paradox across a natural constructible census, against bands fixed
before any code runs. The sim constructs its entire world (network + affine
coefficients) from integers/pinned draws — the cleanest possible test of the pipeline's
unrelated-domain rotation: zero repo reads, zero network, zero fleet coupling in the
verdict session.

**2. What is the possibility space?** (i) Don't run it — the round-2 unrelated-domain
slot goes unserved and ORDER 004 rule 3 is dead letter this cycle. (ii) Re-use round
1's domain (another voting/social-choice head) — fails the owner's "completely
unrelated, and rotate" ask, since P017 already occupies social choice. (iii) A domain
closer to home (tournaments, matchmaking) — game-adjacent, and P015/P016/P020/P023
covered game mechanics. (iv) A literature summary of Braess instances instead of a sim
— not falsifiable and not the pipeline's product; the whole open question is the RATE,
which only enumeration answers. (v) This head: one fixed topology, exhaustive integer
census + seeded continuous robustness arm, bands registered first. (vi) Over-scope
(larger networks, non-affine latency, multi-commodity) — each multiplies the state
space and breaks the unique-equilibrium guarantee; the 4-node affine diamond is exactly
where the paradox is canonical, and extensions are natural follow-up proposals if this
verdict lands APPROVE.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: a fixture is 10 integers (5 edges × (a,b)); the Wardrop
equilibrium on ≤3 routes is a bounded support-pattern enumeration solved as a small
linear system in `fractions.Fraction`; the census is an `itertools.product` over the
coefficient grid. That single file yields an EXACT paradox frequency (no sampling error
at all in Arm A — a rational) plus seeded continuous estimates whose band edges
(3%/15%) sit many standard errors from plausible outcomes — a publication-grade
quantitative answer to a genuinely unmeasured question, from a sim a verdict session can
run cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **Behavioral model is a model** —
Wardrop selfish routing over a uniform coefficient grid is the standard neutral choice,
not a specific city; that is exactly why Arm S varies the coefficient distribution
(continuous vs integer grid) and why the straddle is a pre-registered NULL, and it is
declared in the `## Model basis` note above with system-optimal routing named as the
most-likely-to-flip alternative (under which f → 0). (b) **Uniqueness depends on affine
non-decreasing latency** — pinned; a_e ≥ 0 is enforced by the coefficient ranges, so the
Beckmann potential is strictly convex and the equilibrium (hence every measured cost) is
a unique exact rational. (c) **Degenerate fixtures** — without-bridge cost 0 fixtures
are excluded and the effective N reported, so f is never inflated by a 0/0 ratio. (d)
**Float tolerance in Arm S** — the paradox comparison uses a documented tolerance so
knife-edge draws cannot register as spurious paradoxes; Arm A is float-free by
construction, so the headline census numbers are platform-independent exact rationals.

**5. What does it unlock?** The pipeline's SECOND fleet-external verdict and its first
DOMAIN ROTATION within the unrelated-domain lane — proof the PROPOSAL→VERDICT loop
produces citable knowledge across genuinely different domains with no repo coupling; a
measured, pre-registered data point the owner can cite whenever "adding capacity must
help" comes up (network design, load balancing, any greedy multi-agent routing); and, on
APPROVE, a natural follow-up family (larger networks, non-affine latency, price-of-
anarchy magnitude) for future unrelated-domain rotation slots.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external — that is
the design: no repo, no network, no dataset; every fixture (topology, coefficient grid,
seeds, N_draws, band constants) is stated in this file and committed as a small JSON
alongside the sim. Kill tests, run live this slice: a prior routing-game head anywhere in
the tree (NOT found — sweep empty), an occupied round-2 unrelated-domain slot with THIS
domain (NOT found — P017 is social choice), infeasible runtime (NOT found — arithmetic in
the preamble, minutes in pure CPython). Sim-worthy or judgment-only: sim-worthy — the
entire question is a computable fraction and ratio against pre-registered thresholds; the
one judgment question (are 3%/15% and r-thresholds the RIGHT materiality lines?) is pinned
by pre-registration and stated as the thing a reader may dispute — about the bands, never
about the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab runs
it (its harness, its verdict grammar; the sim file + fixture JSON committed in its sims/
tree per convention). No fleet lane consumes the verdict as a build input — the consumer
is the owner/manager as READERS, plus any future venture-lab writing-product wanting a
worked example of pre-registered simulation. Duplicates nothing: the domain sweep found
zero prior routing-game art in this tree, and no sim-lab verdict through the current
ledger touches transportation or congestion.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib file
(Wardrop equilibrium solver + census enumerator + both arms), one fixture JSON
({coefficient grid, bridge grid, seeds 20260740–43, N_draws, band constants}, values
copied from this file), one results table {N, f_A, median-r, max-r, f_S, arm-agreement
check} ending in exactly one of APPROVE / REJECT / NULL per the pre-registered rule —
reproducible from the fixtures alone, byte-identical on re-run (Arm A exact rationals;
Arm S pinned seeds + stated CPython minor version), no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule are registered above BEFORE any code exists, both failure modes of the
genre are pre-empted (model-dependence → dual-arm coefficient-distribution requirement +
NULL band + the `## Model basis` declaration; degeneracy → 0-cost exclusion + effective
N), and the verdict changes what a reader may cite either way. THE ONE QUESTION for the
simulator: *Under the pinned Braess diamond (nodes s,a,b,t; base edges e1=s→a, e2=a→t,
e3=s→b, e4=b→t; optional bridge e5=a→b; unit demand D=1 routed to the unique Wardrop
equilibrium under affine latencies l_e(x)=a_e·x+b_e, a_e≥0), how OFTEN and by HOW MUCH
does adding the bridge RAISE equilibrium total travel cost — measured as f_A (paradox
frequency over the exhaustive integer census (a_e,b_e)∈{0,1,2}² on e1..e4 and {0,1}² on
e5, 9⁴·4=26,244 fixtures, 0-cost-without fixtures excluded, effective N reported; exact
Fraction) with median-r and max-r among paradox fixtures (r=cost_with/cost_without), AND
f_S (pooled paradox frequency over seeds 20260740–43, a_e,b_e~U[0,2] continuous,
documented float tolerance) — and does the result land APPROVE (f_A ≥ 0.15 OR median-r ≥
1.15), REJECT (f_A ≤ 0.03 AND max-r ≤ 1.05), or NULL (anything else, or the two arms
disagree on the call — NULL-by-arm-disagreement), with the arm-agreement gate |f_S − f_A|
≤ 1.0 pp AND same call required for any non-NULL ruling?* Done-when: a verdict must
contain N (effective census), f_A, median-r and max-r among paradox fixtures, f_S from
the four seeds, the arm-agreement check, and the resulting APPROVE/REJECT/NULL call
against the registered bands — the committed sim + fixture JSON reproducing that table
byte-identically on re-run (Arm A platform-independent exact arithmetic; Arm S pinned to
a stated CPython minor version), with the model-basis caveat (selfish Wardrop routing
under uniform coefficients; system-optimal named as the flip) stated in the verdict.
