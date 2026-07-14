# Why your wait beats the timetable: the inspection paradox at equal means

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 10 closer; a TENTH fleet-external domain: renewal theory & random incidence / the inspection (waiting-time) paradox, disjoint from the nine prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@18f31718b20cb1c5f3fad6cb2767babe124c691a · fetched 2026-07-14T02:47:26Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is invented-but-pinned in this file, zero repo/network reads at verdict time — the P017–P055 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 10 has served fleet backlogs (P053 #379), venture (P054 #382) and game mechanics (P055 #385), so this head is the round-10 UNRELATED closer.

**Placement note (decide-and-flag):** this fleet-external pure-probability head lives in `ideas/fleet/` per the check_sections carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, 044, 048 and 052 did.

## The folk belief

"A bus (shuttle, ferry, elevator, support queue callback) that averages one arrival every μ minutes means a random arriver waits μ/2 on average." Timetables, service-level pages, and back-of-envelope planning all use it: average headway 10 minutes → expected wait 5 minutes. The intuition is symmetric: you land somewhere in the middle of a typical gap.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

The intuition silently assumes you land in a TYPICAL gap. You don't. Under random incidence into an equilibrium renewal stream with i.i.d. headways X (mean μ = E[X]), a uniformly-landing observer falls into a gap with probability proportional to its LENGTH — the length-biased law P(L = x) = x·p(x)/E[X]. Long gaps catch more arrivers precisely because they are long. Conditional on landing in a gap of length x the wait is uniform on (0, x), so the exact expected wait is E[W] = E[X²]/(2·E[X]) = (μ/2)·(1 + CV²) with CV² = Var(X)/μ². The folk rule E[W] = μ/2 is the CV = 0 special case (clockwork schedules) and FAILS for every variable schedule — at high dispersion the average wait can exceed the ENTIRE average headway. The companion identities are just as checkable: the rider-experienced mean gap is E[L] = E[X²]/E[X] = 2·E[W] (riders see longer gaps than the operator's timetable average), and the exceedance law is P(W > w) = E[(X − w)⁺]/E[X].

## Pinned model (committed constants — all invented-but-pinned, exact rationals)

- Renewal stream: i.i.d. integer-minute headways X from a pinned pmf; a passenger lands uniformly at random over a long operating window (random incidence); wait W = time to the next arrival. Landing position within the containing gap is continuous-uniform.
- Decision grid — five schedules, every one with mean EXACTLY μ = 10 (the folk rule predicts E[W] = 5 for all five):
  - **CLOCKWORK** (control): X ≡ 10. Var 0, ρ = 1 exactly.
  - **JITTER**: X ∈ {8, 12} w.p. 1/2 each. Var 4, ρ = 26/25 = 1.04.
  - **SPREAD**: X uniform on {5, 6, …, 15}. Var 10, ρ = 11/10 = 1.10.
  - **MEMORYLESS**: X geometric on {1, 2, …} with success q = 1/10 (P(X = k) = (9/10)^(k−1)/10). Var 90, ρ = 19/10 = 1.90.
  - **BUNCHED** (bus bunching): X ∈ {2 w.p. 4/5, 42 w.p. 1/5}. Var 256, ρ = 89/25 = 3.56.
- Decision statistic: the wait-inflation factor ρ = E[W]/(μ/2) = E[X²]/E[X]² = 1 + CV² — folk belief asserts ρ = 1.
- Arm A (the DECISION arm, seedless): exact `fractions.Fraction` moment arithmetic per cell — E[X], E[X²] (geometric via the exact closed forms E[X] = 1/q, E[X²] = (2 − q)/q², cross-checked against exact rational partial sums to K = 500 plus the exact geometric tail formulas), E[W] = E[X²]/(2E[X]), E[L] = E[X²]/E[X], ρ, and the exceedance table P(W > w) = E[(X − w)⁺]/E[X] for w ∈ {5, 8, 10, 15} — all exact rationals, byte-identical across process runs.
- Arm S (confirmation, seeded): per stochastic cell, build a K = 100,000-interval renewal trajectory via `random.Random(20261361)` (pinned draw order: cells in the listed order JITTER → SPREAD → MEMORYLESS → BUNCHED, all K intervals drawn before any landing; geometric sampled as count-of-Bernoulli(q)-trials, no float log), drop N = 200,000 passengers uniform on [0, T) (T = the trajectory span), wait = next-epoch − landing via bisect, containing-gap length recorded for the E[L] cross-check; agreement gate |mean_S − E_A|/E_A ≤ 1/100 AND ≤ 4·SE on E[W] AND on P(W > 10) per cell (finite-window edge bias is O(1/K), far inside the gate; direction stated).
- Stability leg: seed 20261362, K = 20,000, N = 50,000, reproduces the ruling through twin independently-written decision evaluators.
- Reporting leg: seed 20261363 — median and P90 wait per cell, the w = 15 exceedance column, the E[L] experienced-headway table (rider-vs-timetable), the operator-vs-rider table at BUNCHED (only 1/5 of intervals are the 42-minute gap, yet the length-biased rider share landing in one is 42·(1/5)/10 = 21/25 = 0.84 exact), and the ρ-vs-(1 + CV²) curve; names axes, never flips the decision.
- Aux seed: 20261364, reserved, never read by any decision number.
- Seeds 20261361–364 strictly above P055's 20261360 high-water; boundary-aware re-sweep at HEAD 18f3171 (idea-engine) and the sim-lab working copy READ-ONLY at 135ae4e shows max genuine allocation 20261360 / 20261352 (the larger standalone numerals 20261542/20261664/20261833 are Fraction-numerator digit substrings in results.json-quoting text, and the sim-lab 9-digit hit 202670087 is the decimal-fraction digit substring of `"delta_cond": 0.202670087` in verdict-032 results.json line 12401 — data, not seeds; the P046–P055 sweep-recipe trap re-confirmed with a new specimen).

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the μ/2 folk rule FAILS in the costly direction — headway variability inflates every real wait by the size-bias factor 1 + CV²": ρ(BUNCHED) ≥ 2 AND ρ ≥ 11/10 in ≥ 3 of the 4 stochastic cells AND Arm S confirms within the agreement gate on every stochastic cell. (Costly because the μ/2 rule under-budgets rider time and over-promises service levels exactly when schedules degrade — the bunched regime is where the promise is most wrong.)
- **INVALID** (controls misbehaving — report, no ruling): the F1 pmf re-derivation fails (mass ≠ 1 or mean ≠ 10 exactly, or the geometric closed-form/partial-sum cross-check disagrees), or the F2 size-bias identity fails, or the F3 CLOCKWORK degenerate identities fail, or the F4 monotonicity theorems fail, or the F5 hand identities fail, or the Arm-S agreement gate fails on any cell.
- **APPROVE** — "the folk rule holds to first order": ρ ≤ 21/20 at EVERY stochastic cell AND the seed-20261362 stability leg reproduces the ruling through twin evaluators. (Mutually exclusive with REJECT by arithmetic: 21/20 < 11/10.)
- **NULL** — anything else; pre-registered axes: band-straddle (ρ(BUNCHED) ∈ (21/20, 2), or the 3-of-4 leg misses while BUNCHED fires — the finding is the exact ρ = 1 + CV² curve with the named boundary cell); dispersion-sensitivity (the ruling flips between the low-CV and high-CV halves of the grid — the finding is WHERE on the CV axis the folk rule dies, with the JITTER/SPREAD boundary named); arm disagreement.

## Gates (run invalid on any failure)

- **F1 — pmf anchor:** each pmf re-derived from its committed constants: mass exactly 1, mean exactly 10, variance exactly {0, 4, 10, 90, 256} (Fractions); geometric moments via closed forms AND exact partial sums + tail formulas, agreeing exactly.
- **F2 — size-bias identities:** E[L] = E[X²]/E[X] computed two independent ways (direct length-biased pmf sum vs moment quotient) and E[W] = E[L]/2 exactly, per cell.
- **F3 — degenerate control:** CLOCKWORK posts ρ = 1 exactly, P(W > 10) = 0 exactly, E[W] = 5 exactly.
- **F4 — monotonicity theorems:** ρ = 1 + Var/100 exactly per cell, so ρ ranks the five cells by variance; P(W > w) non-increasing in w per cell; the mean-preserving-spread ordering CLOCKWORK ≺ JITTER ≺ SPREAD ≺ MEMORYLESS ≺ BUNCHED holds on ρ.
- **F5 — hand identities:** JITTER P(W > 8) = 1/5 and E[W] = 26/5 exact; BUNCHED rider-share-in-the-42-gap = 21/25 and P(W > 10) = 16/25 exact; MEMORYLESS P(W > 10) = (9/10)^10 exact.
- **Mechanical:** per-cell draw-count sentinels (K interval draws + N landing draws, geometric draws counted per Bernoulli trial), twin independently-written decision evaluators, stdout + results.json byte-identical across two process runs (Arm A platform-independent exact rationals; Arm S pinned to a stated CPython minor), aux seed 20261364 never read.

## Expected landing (DISCLOSED per the P048–P055 closed-form-arm norm)

REJECT, at the drafter's exact ρ: CLOCKWORK 1 (control), JITTER 26/25 = 1.04, SPREAD 11/10 = 1.10, MEMORYLESS 19/10 = 1.90, BUNCHED 89/25 = 3.56 — the BUNCHED leg fires at 3.56 ≥ 2 with E[W] = 89/5 = 17.8 minutes, EXCEEDING the entire 10-minute average headway, and the ≥ 11/10 leg lands 3 of 4 (SPREAD sits exactly ON the 11/10 edge — exact arithmetic makes ≥ well-defined, and the edge placement is deliberate falsifiability: JITTER at 1.04 genuinely lands APPROVE-side of the band, so a low-variance fleet rescues the folk rule and the bands discriminate). The sim re-derives every value from scratch and must not trust these. Disclosed sharpening: the continuous-exponential analog of MEMORYLESS gives ρ exactly 2 (the classic Poisson doubling); the discrete geometric lands at 19/10 — the discretization gap is disclosed, not laundered.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof plus a transferable method note. REJECT → the μ/2 folk rule retires with numbers and the correction ships: multiply the folk wait by 1 + CV² — and the transfer surface is anything in the fleet that samples an ongoing process at a random instant (a wake landing in the gap between heartbeats, a probe landing inside an outage interval, a user landing between content refreshes): the observed interval is length-biased, and mean-based gap arithmetic understates what a random observer experiences by exactly this factor. APPROVE → the folk rule gains a measured basis for low-dispersion schedules. NULL → the named axis (most likely the exact ρ-vs-CV² boundary) ships with its committed curve.

## Dedup

Tree-wide `rg -i 'inspection paradox|waiting.?time paradox|size.?biased|length.?biased|random incidence|headway|bus.?wait|hitchhiker'` (bootstrap.py/.substrate excluded) at HEAD 18f3171 — zero domain hits; "renewal" prose hits are P029/P050's lease/kill-clock machinery and P045's renewal-drift tool, none a random-incidence head. No proposal P001–P055 and no verdict V001–V066 (V065/V066 in flight = P054 illustration-gate and P055 badge-saturation worlds, zero overlap) prices random incidence, size-biased sampling, or a waiting-time law. Nearest priors argued distinct: **P044 → V055** (checkout pooling — queue DISCIPLINE with servers and service times, M/M/c pooled-vs-split; zero shared machinery — this head has no queue, no server, no service: the object is the length-biased gap a uniformly-landing observer occupies), **P053 → V064** (healthcheck blind window — a DETERMINISTIC cron probe intersecting transient outages, a fleet-infrastructure detection-probability head; no renewal equilibrium, no size-bias identity, no wait law), **P050 → V061** (kill-clock — renewal-reward economics for a stopping decision on censored launches; renewal as a modeling tool, not the random-incidence sampling law), **P012 → V014** (routine-cadence economics — trigger CATCHING where every event waits until collected and nothing is ever missed; no observer landing in a gap). Method kin only: the P017–P055 exact-arm + seeded-confirmation discipline.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'inspection paradox|waiting.?time paradox|size.?biased|length.?biased|random incidence|headway|bus.?wait|hitchhiker'`
> (bootstrap.py/.substrate excluded) at the grounding pin `18f3171` returned zero domain
> hits; the "renewal" prose family (P029 lease-renewal, P050 kill-clock, P045 renewal
> drift) uses renewal processes as MACHINERY for other questions and never prices random
> incidence or a wait law. (b) **kill test NOT triggered** — no prior proposal P001–P055,
> idea file, or session-card 💡 prices the inspection/waiting-time paradox, size-biased
> sampling, or any wait-vs-headway claim. (c) **feasibility + liveness arithmetic
> checked** — runtime bounded (Arm A is five exact-Fraction moment reductions; Arm S is
> 4 × (100k interval draws + 200k bisect landings), seconds, stdlib only); expected
> landing DISCLOSED with its exact drafting-time values (REJECT, ρ(BUNCHED) = 89/25)
> rather than hidden, all rulings reachable under the pre-registered rule, the
> band-straddle NULL axes and the INVALID controls gate both named.

**1. What is this really?** A pre-registered exact MEASUREMENT of the folk rule "average
wait = half the average headway" — does random incidence into an equilibrium renewal
stream inflate the true expected wait by the size-bias factor ρ = E[X²]/E[X]² = 1 + CV²,
and by how much at a committed bus-bunching pin — computed as exact-rational moment
arithmetic over five equal-mean-10 schedules spanning CV² ∈ {0, 1/25, 1/10, 9/10, 64/25},
judged against bands fixed before any code (REJECT `ρ(BUNCHED) ≥ 2 AND ρ ≥ 11/10 in ≥ 3
of 4` first, APPROVE `ρ ≤ 21/20` everywhere with stability reproduction, NULL otherwise),
every decision number an exact `Fraction`, byte-identical across two runs, with a seeded
renewal-trajectory + uniform-landing Monte-Carlo arm cross-validating the closed form.

**2. What is the possibility space?** (i) Don't run it — the round-10 unrelated closer
goes unserved and the rotation closes short. (ii) Re-use a prior round's domain — fails
the owner's "rotate" ask (P017/P024/P028/P032/P036/P040/P044/P048/P052 occupy voting,
routing, tournaments, pattern races, stopping, spatial self-organization, queueing,
ratchets, occupancy). (iii) A literature summary ("E[W] = E[X²]/2E[X], see any renewal
text") — retells the textbook direction, measures nothing against a pre-registered
consumer-relevant band, and dodges the live question (how wrong is μ/2 at an equal-mean
bunched schedule, and does the folk rule survive ANY variability). (iv) An MC-only
estimate — leaves ρ noisy and seed-dependent when an EXACT rational closed form exists,
so the DECISION arm is the exact moment solve and MC is demoted to confirmation. (v) This
head: exact-rational Arm A on the pinned five-cell grid as the ruling, seeded Arm S as
the cross-check, REJECT-first bands on ρ, INVALID gate on the pmf/size-bias/degenerate/
monotonicity/hand identities, robustness disclosed via the exceedance table and the
operator-vs-rider report. (vi) Over-scope (correlated headways, time-varying rates,
multi-line transfers, Palm-calculus generality, the elevator/hitchhiker variants) — each
named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One
~150-line stdlib file: an exact `Fraction` moment kernel (E[X], E[X²], E[W], E[L], ρ, the
exceedance law E[(X − w)⁺]/E[X]) reused across the five cells, plus one renewal-trajectory
+ uniform-landing MC loop parameterized by the pmf. That single file yields an exact,
reproducible ruling on a famous counterintuitive law at a consumer-relevant pin, AND — as
free side pins — the rider-vs-operator table (84% of riders land in the 20%-of-intervals
long gap), the experienced-headway table E[L] = 2·E[W], and the exact exceedance columns,
all from a sim a verdict session runs cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **The i.i.d. renewal assumption is
a choice** — real bus bunching is CORRELATED (a late bus gets later); positive correlation
in gap lengths pushes the observer's length-biased experience WORSE, so an i.i.d. REJECT
is robust in the costly direction (direction stated), and the correlated variant is the
named follow-up. (b) **Band placement could cherry-pick** — both bands (2 and 11/10 for
REJECT, 21/20 for APPROVE) are committed BEFORE any code, are DISJOINT, NULL is
first-class (band-straddle, dispersion-sensitivity, arm disagreement), and the expected
landing is DISCLOSED (REJECT) rather than hidden. (c) **The grid is a choice** — five
schedules pin the CV axis at {0, 1/25, 1/10, 9/10, 64/25}; the JITTER cell at ρ = 1.04
deliberately lands APPROVE-side and the SPREAD cell sits exactly ON the 11/10 edge, so
the falsifiability is real in both directions. (d) **The uniform-landing convention** —
continuous-uniform position inside an integer-minute gap is the pinned incidence model;
integer-landing alternatives shift E[W] by ≤ 1/2 minute and are the named
reporting-sensitivity, never the decision. (e) **An arithmetic slip in the drafter's hand
check** — the sim RE-DERIVES every moment, ρ, and exceedance from scratch with zero trust
in this file's values, and Arm S's independent trajectory-landing simulation cross-checks
by a completely different code path, so a solver bug shows up as an Arm-A/Arm-S
disagreement → INVALID.

**5. What does it unlock?** The pipeline's TENTH fleet-external verdict and the rotation
lane's proof it spans domains (voting → routing → tournaments → pattern races → stopping
→ spatial self-organization → queueing → ratchets → occupancy → random incidence); a
measured, citable answer to "how wrong is the μ/2 wait rule, and when" — the exact ρ
table, the rider-vs-operator share, and the exceedance columns as standalone side pins;
and a transferable correction the fleet can reuse anywhere a session samples an ongoing
process at a random instant (wake-vs-heartbeat gaps, probe-vs-outage windows,
user-vs-refresh gaps): the observed interval is length-biased by exactly 1 + CV².

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: Arm A's five moment reductions settle the ruling in microseconds and
need no seed; Arm S's trajectory-landing loops (seconds per cell) are the cross-check.
The single cheapest probe if a reader doubts a specific leg is the JITTER hand identity
(P(W > 8) = 1/5: land in a 12-gap w.p. 12/20 = 3/5, then need position in its first
12 − 8 = 4 minutes, w.p. 4/12 = 1/3; 3/5 · 1/3 = 1/5), which anchors both the closed form
and the MC against a hand-countable ground truth.

**7. What would make this a mistake to run?** If the exact rational solve were somehow
unavailable (it is not — all five pmfs have rational moments in closed form), or if the
domain duplicated a prior head (it does not — dedup returned zero), or if the ruling were
pre-determined in a way that made it worthless. The last is the sharpest self-check: the
landing is disclosed as REJECT, so is this theater? No — the VALUE is the independent
hermetic re-derivation + MC cross-validation + the exact ρ-vs-CV² curve, the rider-share
table, and the exceedance columns, and the falsifiability is real (JITTER lands
APPROVE-side, SPREAD sits exactly on the band edge, and the APPROVE band is genuinely
reachable by any low-dispersion fleet). It would only be a mistake if run as a bare
"compute a known constant"; framed as re-derive-plus-validate-plus-price-the-consumer-band,
it is a genuine, self-contained knowledge deliverable.

**8. How will we know it worked?** A committed sim-lab report with: Arm A's exact ρ,
E[W], E[L], and exceedance table as `Fraction`s and their `float` renderings per cell;
the verdict token (REJECT / APPROVE / NULL) against the pre-registered bands; Arm S's
seeded empirical means each inside tolerance of Arm A per stochastic cell; the
rider-vs-operator table; the median/P90 wait rows; the F1–F5 gate results; and a
byte-identity note (two process runs produce identical output). A clean run reproduces
ρ(BUNCHED) = 89/25 (the drafter's disclosed reference) from scratch, or — the more
interesting outcome — DISAGREES with it and pins the drafter's arithmetic error, which
the pre-registered rule then rules on honestly.

**Recommendation: sim-ready**
