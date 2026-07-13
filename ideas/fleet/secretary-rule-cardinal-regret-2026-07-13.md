# The 37% rule off its home objective — the exact cardinal price of look-then-leap's folk cutoff

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain
> slot, round 5; the domain itself is sequential search / optimal stopping — the secretary
> problem's popularized "37% rule" from the decision-science self-help canon — fleet-external
> by design and DIFFERENT from round 1's social choice (PROPOSAL 017), round 2's congestion
> routing (PROPOSAL 024), round 3's tournament seeding (PROPOSAL 028), and round 4's
> pattern-race probability (PROPOSAL 032), so the rotation now spans FIVE domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@a2850e2ed1004db1ac9bd0cc617ab45fe95d44f8 · fetched 2026-07-13T14:34:35Z
> (the dedup-sweep pin — this repo's own tree at drafting HEAD, the only read this head
> takes; the sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 and ratified by the morning tally ("Rotate lanes deliberately: … →
COMPLETELY UNRELATED domains (I want those too)") — PROPOSAL 017 opened the
unrelated-domain lane with social choice, PROPOSAL 024 rotated it into congestion routing,
PROPOSAL 028 into tournament-format design, PROPOSAL 032 into pattern-race probability;
this is round 5's head, rotated into a FIFTH fleet-external domain (sequential search /
optimal stopping). Round 5's other two rotation slots are already served (venture →
PROPOSAL 034, game-mechanics → PROPOSAL 035). **Placement note (decide-and-flag):**
sections are roster-derived and inventing one ad hoc is forbidden (README § Sections;
`check_sections.py` reds an ORPHAN section against the live roster), and that checker's
own carve-out rules that sim-lab-shaped ideas "ride `ideas/fleet/` or the proposing
section" — so this fleet-external head lives here, flagged rather than silently
squatting, exactly as PROPOSALs 017, 024, 028, and 032 did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief.** The secretary problem (canonized mid-century; re-popularized as the
"37% rule" by the decision-science self-help canon) is THE popular algorithm for
sequential choice: N candidates arrive in uniform random order, each must be accepted or
rejected on the spot with no recall, and the advice is **look-then-leap — observe the
first 37% (N/e) without committing, then take the first candidate better than everything
seen**. The popularized story sells one cutoff for every hiring/apartment/dating decision,
on the strength of a real theorem: for the objective P(select THE single best candidate),
with known N and rank-only feedback, the ~N/e cutoff is optimal and wins with probability
→ 1/e. What the story never prices is that almost no real chooser has that objective —
a hirer's payoff is the QUALITY of who they get, not an all-or-nothing bonus for
literally the best — and within the SAME look-then-leap family the value-maximizing
cutoff is radically earlier (calculus on the closed form puts it near √N − 1, not
0.37·N). The settled part is the classical theorem (not in question, and deliberately
reproduced as an anchor, not a band). The measured unknowns are the exact CARDINAL
REGRET curve of the folk cutoff — ΔV(N), how much expected candidate value the 37%
cutoff forfeits against the best cutoff in its own family when values matter — and the
folk story's untold DOWNSIDE profile (with probability ~r/N it never leaps and ends
forced onto the last candidate; how often does the rule hand you a bottom-half hire?).
Numbers nobody carries, in a frame where every one of them is an exact rational a
stdlib file can compute. This mirrors the accepted P017/P024/P028/P032 pattern exactly:
the effect is settled in principle (a known-N rank-objective theorem); its
magnitude/shape on a committed family under the objective people actually hold is the
unknown; and REJECT, APPROVE, and NULL are all live.

**The decision space (fixed, finite, fully enumerable).** N candidates, i.i.d. values
V ~ U[0, 1] arriving in uniform random order (equivalently: a uniform random permutation
of ranks; the cardinal leg reads values through the order-statistics mean — the overall
rank-k candidate has E[V] = (N+1−k)/(N+1) exactly). Policy family: the cutoff rules
CR(r), r ∈ {1..N−1} — observe the first r, then accept the first subsequent running
record. Two end conventions, both computed: **MUST-CHOOSE** (if no record appears after
r, take candidate N — decision-binding, the convention that matches "you have to hire
someone") and **WALK-AWAY** (end empty, payoff 0 — reporting-only). N grid
{5, 10, 20, 50, 100, 200} × all cutoffs r ∈ {1..N−1}: 379 (N, r) cells × 2 objectives
(P(best), E[V]) × 2 conventions. Folk cutoff pinned exactly: r_folk(N) =
clamp(⌊(37·N + 50)/100⌋, 1, N−1) — the popularization's own "37%", nearest-integer in
exact integer arithmetic; the ⌊N/e⌋ variant rides reporting-only with e pinned by the
rational bracket 271828182845/10¹¹ < e < 271828182846/10¹¹ and the two floors asserted
equal per N. Bottom-half hire := overall rank ≥ ⌊N/2⌋ + 1 (rank 1 = best).

**Exact computation — fully deterministic, NO RNG anywhere.** Everything is computed in
exact `fractions.Fraction`; there is no Monte Carlo arm and no seed. (Seed-registry
note, explicit: this sim draws ZERO seeds — the PROPOSAL 035 registry high-water
**20261284** is left unchanged; the next seeded head continues from there.)

- **Arm A (analytic closed forms):** P_best(r, N) = (r/N)·Σ_{j=r}^{N−1} 1/j (the
  classical formula); for the cardinal leg, the per-position acceptance decomposition
  (accept at j ⇔ the max of the first j−1 sits in the first r AND V_j beats it) gives
  E[V_j·1{accept at j}] = (r/2)·(1/(j−1) − 1/(j+1)) exactly, telescoping to
  E_must[V](r, N) = ½·(1 + r/(r+1) − r/N) and
  E_walk[V](r, N) = ½ + r/(2(r+1)) − r/(2N) − r/(2(N+1)). These closed forms are the
  DRAFTING hand-derivation — re-deriving and independently verifying them is exactly
  what Arm B and the census gate exist for.
- **Arm B (independent combinatorial rank census, the structural cross-check):** compute
  the JOINT distribution of (selected position j, selected candidate's overall rank k)
  by direct combinatorial counting over relative-rank configurations — pure finite
  counting (binomial-coefficient ratios of the C(N−k, j−1)/C(N−1, j−1) family plus the
  take-at-N legs), no integrals, no values — then read P_best off the rank-1 row and
  E[V] through Σ_k P(rank k)·(N+1−k)/(N+1). Arm B must equal Arm A by EXACT RATIONAL
  EQUALITY on every (N, r, objective, convention) cell — the seedless-exact analogue of
  the P017/P024 arm-agreement gate and the same discipline P028/P032 ran; any
  inequality invalidates the run.
- **Census gate (algorithm-free third arm):** at N ∈ {5, 6, 7}, full permutation
  enumeration (120 / 720 / 5,040 orders) tallying both objectives, both conventions, and
  the full selected-rank distribution at every r — must equal BOTH arms exactly.
- **Self-checks (all exact, run invalid on failure):** the classic published anchors —
  P_best(1, 3) = 1/2 (the famous 3-candidate case), the small-N optimal-cutoff table
  (N = 4: r* = 1 with 11/24; N = 5: r* = 2 with 13/30); the convention identity
  E_must[V] − E_walk[V] = r/(2(N+1)) on every cell, both sides computed independently;
  the never-leap identities P(take last | must-choose) = r/(N−1) and
  P(end empty | walk-away) = r/N exactly; the rank distribution summing to 1 (must-choose)
  and to 1 − r/N (walk-away); P(rank 1) ≡ P_best across arms; E_must[V](N−1, N) = ½
  exactly; and the ⌊N/e⌋ bracket-floor agreement per N.

**Measured quantities (all exact rationals):**

- **ΔV(N) = E_must[V](r*_V(N)) − E_must[V](r_folk(N))** — the cardinal regret of the
  folk cutoff against the best cutoff in its own family, where r*_V(N) = the exact
  integer argmax of E_must[V] over r (measured by grid scan, ties reported); plus the
  full efficient frontier (P_best, E[V]) across ALL r per N.
- **B(N)** — the untold-downside pin: P(the selected candidate's overall rank is
  bottom-half) under CR(r_folk), must-choose, including the forced-last leg; plus the
  full selected-rank distribution (quartiles) at r_folk, r*_R, and r*_V.
- **ΔR(N) = P_best(r*_R(N)) − P_best(r*_V(N))** — what a value-optimizer concedes on
  the classic objective by moving to r*_V (the other side of the fork), and the folk
  cutoff's own-objective shortfall P_best(r*_R) − P_best(r_folk) (drafting arithmetic
  says this is measured in hundredths of a pp — the fork is in the OBJECTIVE, not in
  the folk rule's arithmetic).
- The take-last / end-empty probability columns, r*_V(N) against the √N − 1 calculus
  prediction, and the ⌊N/e⌋-variant deltas.

**Pre-registered decision bands (fixed BEFORE any code exists — honest guesses, not
tuned; evaluated in this order; the two decision bands are DISJOINT by construction,
1/50 < 1/20):**

- **REJECT** ("the 37% rule is objective-robust — cite it freely, one cutoff serves both
  goals") iff ΔV(N) ≤ 1/50 at EVERY swept N: the folk cutoff never forfeits more than
  2 points of expected value on the 0–1 scale. Checked FIRST — the folk-vindicating
  strict claim, reachable only if the drafting closed forms fail the independent census.
- **APPROVE** ("the objective fork is first-order — 37% is a rank-obsession tax at
  scale") iff ΔV(N) ≥ 1/20 at every swept N ≥ 50 (cells {50, 100, 200}) AND
  B(N) ≥ 3/20 at every swept N ≥ 50: the folk cutoff forfeits ≥ 5 points of value AND
  hands out bottom-half hires ≥ 15% of the time exactly where the popularization's
  hiring story lives.
- **NULL** (anything else — a legitimate reportable outcome): the finding is then the
  exact frontier itself — e.g. the regret is real but the downside conjunct misses its
  band — and the citable pin is the per-N table {ΔV, B, ΔR, r*_V}; neither "37% is
  optimal, full stop" nor "37% is broken" may be cited as settled.

**Band liveness (drafting arithmetic, disclosed — the P034/P035 discipline).** The hand
closed forms (verified at drafting against a full N ≤ 7 permutation census, exact
equality at every cell) put ΔV at {1/60 ≈ 0.017, 0.033, 0.0375, 0.084, 0.103, 0.123}
across the grid — REJECT is therefore live only through a derivation-scale surprise
(which the dual-arm + census gates exist to catch), and the ΔV conjunct of APPROVE is
predicted to clear its 1/20 line at all of N ∈ {50, 100, 200}. The genuinely open
number is **B(N)**: a 200k-draw drafting MC estimate brackets it near 0.19 against the
3/20 = 0.15 band — close enough that the exact rationals decide, and they do not exist
until Arm B runs (the forced-last leg alone contributes ≈ r_folk/(2(N−1)) ≈ 0.186; the
record-leg's bottom-half mass is the unpinned part). Expected landing APPROVE; NULL via
the B conjunct is genuinely reachable; all three rulings stated with their reachability
honestly disclosed, per the P033/P035 precedent.

**What a reader DOES differently on the verdict (so the ruling is actionable, not
trivia).**

- **APPROVE** → the 37% rule may no longer be cited as "the optimal strategy" for
  sequential choice UNQUALIFIED: it is optimal only for the all-or-nothing best-pick
  objective, and anyone whose payoff is the hire's quality (nearly every popular
  application — hiring, apartments, dating) should leap far earlier (the measured
  r*_V(N) curve ships, ≈ √N); every future citation of the rule in fleet prose carries
  the objective caveat, and the downside table (forced-last rate, bottom-half rate)
  ships with it.
- **REJECT** → the folk rule is measured objective-robust: cite it freely with the
  ≤ 2-point value cost attached; no caveat machinery is warranted.
- **NULL** → the honest middle: the exact frontier table is the citable pin, the
  objective caveat applies only where its named cell holds, and the downside profile
  still ships as the side finding either way.

**Reporting-only legs (cannot flip the decision):** the WALK-AWAY convention's full
frontier (both objectives — the convention flip is the strongest known lever on the
folk rule's story and must be visible, not decision-entangled); the ⌊N/e⌋-variant
columns; ΔR(N) and the folk cutoff's own-objective shortfall; the take-last / end-empty
columns; selected-rank quartiles at the three named cutoffs; r*_V(N) vs the √N − 1
prediction; and P_best(r_folk, N) against the 1/e limit (context for how intact the
classic story is on its home objective).

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo reads —
the entire world (the N grid, the cutoff family, the folk-cutoff formula, band
constants, the classic anchor rationals, the e bracket) is constructed in-sim from the
pinned constants in this file, committed as a small fixture JSON alongside one stdlib
file. All arithmetic exact `fractions.Fraction` / exact integers; byte-identical output
on re-run is BY CONSTRUCTION (no floats, no RNG, no environment reads),
platform-independent. Feasibility arithmetic: Arm A is 379 closed-form cells; Arm B is
O(N³) counting per N ≈ 10⁷ exact-integer term operations at the dominant N = 200; the
census gate is 5,886 permutations — minutes in pure CPython, no dependencies.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–035): nothing adjacent by DOMAIN — no proposal prices a
  stopping rule, a hiring/search policy, or any secretary-problem question. Nearest by
  METHOD only: PROPOSALs 028/032 (the same fully-exact, zero-RNG, dual-independent-
  algorithm census discipline — `fractions.Fraction`, rational-equality gate,
  pre-registered disjoint bands, classic-anchor validity gates), and PROPOSALs 017/024
  (the same pre-registered honest-NULL rotation pattern, seeded arms there). No shared
  domain, fixture, metric, or consumer with any of the four.
- vs superficial rhymes, checked by name: PROPOSAL 030 → VERDICT 032 runs a TWO-STAGE
  "produce, observe, then commit" policy — but that is budget ALLOCATION across book
  versions on the venture lane's seeded revenue model (its stage-1 breadth is bought,
  not observed for free), zero shared model/metric/fixture/consumer with a stopping
  rule on a candidate stream; PROPOSAL 034 sweeps threshold DETECTORS on a return
  stream (trust gating, nothing stops); PROPOSAL 027's "optimal-stopping loss-rebate
  harvester" is a casino FARMER POLICY descriptor inside a bankroll-ruin grid —
  mechanical use of the phrase, different question entirely. Tree-wide
  `rg -i "secretary|optimal.?stopp|look.?then.?leap|marriage.problem|37.?percent|best.choice"`
  over ideas/ + control/ + .sessions/ + docs/ (bootstrap.py and .substrate excluded) at
  the grounding pin returns ONLY those casino farmer-policy lines and this head's own
  claim file — no stopping-rule content anywhere in the tree.
- Runners-up this slice, weighed and dropped on merit: **hot-hand streak bias**
  (Miller–Sanjurjo selection bias — a genuinely open magnitude, but it lives on
  coin-sequence statistics, PROPOSAL 032's occupied neighborhood); **friendship paradox
  / acquaintance-immunization heuristic** (real folk belief, but a graph-degree domain
  sitting next to PROPOSAL 024's network neighborhood); **Benford first-digit audit
  rule** (a crisp folk belief, but the honest version needs a float-analytic arm with
  truncation tolerances — weaker than the fully-exact discipline this slot's precedent
  set, and with no committed anchor); **apportionment paradoxes** (PROPOSAL 028's own
  named pass — voting-adjacent to P017's occupied neighborhood).

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumption:** candidates i.i.d. U[0, 1] in uniform random arrival
  order, N known, no recall, and the policy family restricted to cutoff rules CR(r) —
  the folk rule's OWN family and frame (the popularization sells exactly a cutoff).
  The cardinal leg's uniform-values choice is the neutral one; the measured curve is a
  property of THIS frame.
- **(2) Single most-likely-to-flip alternative:** the VALUE DISTRIBUTION — heavy-tailed
  values (a superstar market) reward late leaping and shrink ΔV, while bounded flat
  values enlarge it; "ΔV under a pinned heavy-tail family" is the natural follow-up
  head with both arms' machinery reusable. Softer flips, named as out of the registered
  scope: unknown/random N, recall, interview costs, and NON-cutoff policies (the
  optimal cardinal policy is a threshold rule outside the cutoff family — this head
  prices the folk rule against its OWN family, so every measured regret is a LOWER
  bound on the cost against full optimality, stated in the verdict).

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> stopping-rule sweep above returned zero domain hits at the grounding pin
> (`a2850e2`); PROPOSALs 001–035 re-read at HEAD before drafting, and the four prior
> rotation occupants (P017 social choice, P024 routing, P028 seeding, P032 pattern
> races) are all different domains. (b) **kill test NOT triggered** — no prior
> proposal, idea file, or session-card 💡 touches the secretary problem, stopping
> rules, or search-then-commit policies. (c) **feasibility + liveness arithmetic
> checked** — the closed forms were hand-derived AND verified against a full N ≤ 7
> permutation census at drafting (exact equality); band liveness disclosed in its own
> subsection above; runtime arithmetic in the preamble (minutes, stdlib only).

**1. What is this really?** A pre-registered MEASUREMENT of the most-cited piece of
folk algorithmics: the exact cardinal-regret curve ΔV(N) of the 37% look-then-leap
cutoff against the best cutoff in its own family, plus the rule's untold downside
profile B(N) — every number an exact rational computed twice by structurally
independent algorithms (analytic closed forms vs a pure combinatorial rank census) and
gated by an algorithm-free permutation census at small N, against bands fixed before
any code runs. The sim constructs its entire world from the pinned constants in this
file: zero repo reads, zero network, zero RNG, zero floats.

**2. What is the possibility space?** (i) Don't run it — the round-5 unrelated-domain
slot goes unserved and the rotation's standing rule is dead letter this cycle.
(ii) Re-use a prior round's domain — fails the owner's "rotate" ask (P017/P024/P028/
P032 occupy voting, routing, tournaments, pattern races). (iii) A literature summary
("1/e is optimal; here is the proof sketch") — retells the theorem's own objective,
measures nothing off it, and is not the pipeline's product; the open question is the
exact regret curve under the objective people actually hold, which only enumeration
answers. (iv) Monte-Carlo simulate the policies — strictly worse than exact
computation where a closed rational exists (the P028/P032 stance verbatim). (v) This
head: full (N, r) census on a committed grid, dual independent exact algorithms,
census gate, bands registered first. (vi) Over-scope (unknown N, recall, non-cutoff
threshold policies, heavy-tailed values, interview costs) — each named in `## Model
basis` as a follow-up or an explicitly out-of-scope flip; the cutoff-family restriction
is what makes every regret a lower bound, stated.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~250-line stdlib file: Arm A is six closed-form lines over `fractions.Fraction`;
Arm B is a triple loop of exact binomial-ratio counting; the census gate is
`itertools.permutations` at N ≤ 7. That single file yields the exact price tag of the
world's most popular decision heuristic under the objective its popular applications
actually have — a publication-grade quantitative answer (every number a rational, no
error bars at all) to the question every popularization raises and none measures, from
a sim a verdict session runs cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **The model is the rule's own
canon** — known N, no recall, cutoff family, uniform values on the cardinal leg — and
the `## Model basis` note names the value-distribution flip and the out-of-scope
policy-family widening; the bands quantify only over the swept grid. (b) **Band
placement could cherry-pick** — both bands are committed in this file BEFORE any code,
are DISJOINT by construction, NULL is a first-class outcome, and the liveness
subsection discloses exactly which conjunct is open (B against 3/20) rather than
implying false suspense. (c) **A wrong hand derivation** — the closed forms are the
drafting author's own; they were census-verified at N ≤ 7 at drafting, and the sim
re-verifies them against a structurally independent counting arm on all 379 cells plus
the N ∈ {5, 6, 7} full census — a single inequality invalidates the run, and a REJECT
produced by a genuine derivation failure would be the finding, never silently
absorbed. (d) **Convention sensitivity** — must-choose vs walk-away materially changes
the folk story's tail; both are computed, the decision is pinned to must-choose, and
the identity E_must − E_walk = r/(2(N+1)) gates the pair. (e) **Folk-cutoff
definition games** — r_folk is pinned as an exact integer formula, and the ⌊N/e⌋
variant ships reporting-only with a pinned rational bracket for e.

**5. What does it unlock?** The pipeline's FIFTH fleet-external verdict and the
rotation lane's proof it spans domains (voting → routing → tournaments → pattern races
→ optimal stopping); a measured, citable answer the owner can deploy whenever the 37%
rule comes up (the rule either survives its objective fork with a ≤ 2-point price tag,
or gets its caveat with exact numbers attached); the r*_V(N) ≈ √N curve as a
standalone side pin (the "leap much earlier when quality is the payoff" correction);
and on APPROVE or NULL a natural follow-up head (the heavy-tail value family) with
both arms' machinery already built.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external — by
design: no repo, no network, no dataset, no RNG; every fixture (the N grid, the
r_folk formula, band constants 1/50 · 1/20 · 3/20, the anchor rationals 1/2 · 11/24 ·
13/30, the e bracket) is stated in this file and committed as a small JSON alongside
the sim. Kill tests, run live this slice: a prior stopping-rule head anywhere in the
tree (NOT found — sweep empty at `a2850e2` beyond the casino farmer-policy phrase and
this head's own claim file); an occupied round-5 unrelated slot (NOT found — P034/P035
serve the venture and game-mechanics slots; no claim or open PR on PROPOSAL 036 at
drafting); infeasible runtime (NOT found — arithmetic in the preamble, minutes).
Sim-worthy or judgment-only: sim-worthy — the entire question is a computable set of
exact rationals against pre-registered thresholds; the one judgment call (are 1/20 and
3/20 the RIGHT materiality lines?) is pinned by pre-registration and stated as the
thing a reader may dispute — about the bands, never about the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; the sim file + fixture JSON committed in
its sims/ tree per convention). No fleet lane consumes the verdict as a build input —
the consumer is the owner/manager as READERS (plus, incidentally, any future mechanic
or workflow that ever runs a search-then-commit selection — candidate screening, offer
acceptance, pick-one-of-a-stream game mechanics — which would inherit the frontier
table for free). Duplicates nothing: the domain sweep found zero prior stopping-rule
art in this tree, and no sim-lab verdict through the current ledger touches the
secretary problem or cutoff-policy mathematics.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib file
(closed-form arm + independent combinatorial rank-census arm + permutation census gate
+ self-checks), one fixture JSON ({N grid {5, 10, 20, 50, 100, 200}, the r_folk
formula ⌊(37N + 50)/100⌋ clamped, band constants 1/50 · 1/20 · 3/20 with decision
cells N ≥ 50, the bottom-half definition rank ≥ ⌊N/2⌋ + 1, anchor rationals 1/2 ·
11/24 · 13/30, the e bracket 271828182845/10¹¹ < e < 271828182846/10¹¹}, values copied
verbatim from this file), one results table {per N: the full (P_best, E[V]) frontier
over all r in both conventions; r*_R, r*_V (ties reported) and r_folk; ΔV, B, ΔR and
the own-objective shortfall; the take-last/end-empty columns; rank quartiles at the
three cutoffs; the ⌊N/e⌋-variant deltas} ending in exactly one of APPROVE / REJECT /
NULL per the pre-registered rule — reproducible from the fixtures alone,
byte-identical on re-run BY CONSTRUCTION (exact rationals, no RNG, no floats,
platform-independent), no flags.

**Recommendation: sim-ready** — the question is crisp and completely computable, the
bands and decision rule are registered above BEFORE any code exists with the two
decision bands disjoint by construction and band liveness honestly disclosed, both
genre failure modes are pre-empted (model-dependence → the rule's own canonical frame
+ the `## Model basis` declaration + a NULL band; algorithmic error → dual independent
exact algorithms gated on rational equality plus an algorithm-free permutation census
and eight committed self-checks), and the verdict changes what a reader may cite in
every branch. THE ONE QUESTION for the simulator: *Under the pinned secretary frame
(N candidates, i.i.d. U[0,1] values in uniform random order, known N, no recall;
cutoff rules CR(r) = observe r then take the first running record, MUST-CHOOSE
decision-binding and WALK-AWAY reporting-only; folk cutoff r_folk(N) =
clamp(⌊(37N+50)/100⌋, 1, N−1)), what are the exact cardinal-regret curve ΔV(N) =
E[V](r*_V) − E[V](r_folk) and the downside profile B(N) = P(bottom-half hire under
r_folk) over N ∈ {5, 10, 20, 50, 100, 200} — every number an exact rational computed
over the full 379-cell (N, r) census by analytic closed forms AND independently by a
pure combinatorial rank census with rational equality required on every cell, gated by
a full permutation census at N ∈ {5, 6, 7} and the classic anchors P_best(1,3) = 1/2 ·
11/24 · 13/30 (zero RNG/floats/seeds — the P035 seed-registry high-water 20261284
explicitly untouched) — landing (bands disjoint, REJECT stated first) REJECT ("the 37%
rule is objective-robust") iff ΔV(N) ≤ 1/50 at every swept N, APPROVE ("the objective
fork is first-order — 37% is a rank-obsession tax at scale") iff ΔV(N) ≥ 1/20 AND
B(N) ≥ 3/20 at every swept N ≥ 50, or NULL (anything else: the exact per-N frontier
{ΔV, B, ΔR, r*_V} is the citable pin and neither soundbite may be cited as settled) —
with the walk-away frontier, ⌊N/e⌋ variant, ΔR(N), own-objective shortfall,
take-last/end-empty columns, rank quartiles, and the r*_V vs √N − 1 comparison all
reporting-only?* Done-when: the committed stdlib sim + fixture JSON reproduce the full
results table byte-identically on re-run (exact rationals, platform-independent, no
CPython version sensitivity), every gate passes (Arm A ≡ Arm B rational equality on
all 379 × 2 × 2 cells, the N ∈ {5, 6, 7} permutation census, the classic anchors, the
E_must − E_walk = r/(2(N+1)) identity, the take-last/end-empty and rank-sum
identities, the e-bracket floor agreement), and the verdict issues exactly ONE of
APPROVE/REJECT/NULL per the pre-registered rule — stating the model-basis caveat
(known-N, no-recall, cutoff-family, uniform values; the heavy-tail flip named as the
follow-up, the cutoff-family restriction making every regret a LOWER bound on the cost
against full optimality) and the liveness disclosure (expected landing APPROVE; the B
conjunct the open number; REJECT live only through a derivation-scale surprise);
honest-null explicit: a NULL lands as a finalized verdict pinning the exact frontier,
not a re-run request.
