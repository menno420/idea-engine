# Parrondo's paradox at a conservative discrete pin — do two individually-losing games combine into a winner, and by a material margin?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain
> slot, round 8; the domain itself is stochastic-ratchet / capital-dependent game switching
> — Parrondo's paradox from the statistical-mechanics-of-games canon — fleet-external by
> design and DIFFERENT from round 1's social choice (PROPOSAL 017), round 2's congestion
> routing (PROPOSAL 024), round 3's tournament seeding (PROPOSAL 028), round 4's pattern
> races (PROPOSAL 032), round 5's optimal stopping (PROPOSAL 036), round 6's spatial
> self-organization (PROPOSAL 040), and round 7's queue-discipline design (PROPOSAL 044),
> so the rotation now spans EIGHT domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@b56d80218750c548161224cb0e2221e512087544 · fetched 2026-07-13T21:49:43Z
> (the dedup-sweep pin — this repo's own tree at drafting HEAD, the only read this head
> takes; the sim itself is fully hermetic: zero repo/network reads at verdict time, every
> fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established by
ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 8's other three slots are already served (fleet
backlogs → PROPOSAL 045 #343, venture → PROPOSAL 046 #348, game mechanics → PROPOSAL 047
#352), so this slice closes the round at the unrelated slot; PROPOSAL 017 opened the lane
with social choice, and it has since rotated through congestion routing (P024), tournament
seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization
(P040), and queue-discipline (P044); this is round 8's closer, rotated into an EIGHTH
fleet-external domain (Parrondo's paradox / capital-dependent stochastic ratchets).
**Placement note (decide-and-flag):** sections are roster-derived and inventing one ad hoc
is forbidden (README § Sections; `check_sections.py` reds an ORPHAN section against the live
roster), and that checker's own carve-out rules that sim-lab-shaped ideas "ride
`ideas/fleet/` or the proposing section" — so this fleet-external head lives here, flagged
rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, and 044
did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief.** Parrondo's paradox is the most-cited counterintuitive result in the
statistical mechanics of games: *two games that each LOSE money in the long run can, when
you alternate between them, WIN money in the long run.* It reads like a violation of common
sense (a mixture of two losers should still be a loser) and is the discrete, game-theoretic
cousin of the Brownian-ratchet / flashing-ratchet motors of physics — directed motion
extracted by switching between two potentials, each of which alone produces no net drift.
Harmer & Abbott (1999) gave the canonical construction; every popular retelling states the
qualitative direction as settled. What is NOT settled — and never is, without pinning the
exact numbers — is whether the paradox actually *manifests, and by a material margin,* at a
deliberately CONSERVATIVE integer-lattice parameterization: pushing the losing bias of each
game harder (a larger ε) eventually KILLS the paradox (the combined game turns loser too),
and the surviving positive drift, when it survives, is famously *thin*. So the folk claim
"two losers make a winner" is a direction; the sim prices it as a magnitude on a pinned
frame where REJECT is genuinely live.

**The mechanism (why it is not magic).** Game B is *capital-dependent*: which coin you flip
depends on your current capital modulo `M = 3`. Alone, Game B spends a disproportionate
fraction of its time in the "bad" residue class (state 0), because the dynamics funnel it
there, so its time-averaged win rate falls below fair despite the good coin being reachable
two-thirds of the residues. Game A is a plain losing coin. Alternating them lets Game A
*reshuffle the residue occupancy* away from Game B's self-inflicted bad state, so the mixed
process visits the good coins more than Game B alone does — and the combined drift turns
positive. It is a real effect (a ratchet), not an arithmetic illusion, and the sim exhibits
the mechanism (the stationary residue distribution) as a first-class side pin, not just the
headline sign.

**The pinned model (every constant exact and committed in this file — the P017–P044
hermetic precedent).**

- **Bias.** `EPS = 1/100` (deliberately larger than Harmer–Abbott's 0.005 — the conservative
  pin: each game is pushed *further* into losing territory than the textbook case, so the
  paradox has more to overcome and REJECT is live).
- **Modulus.** `M = 3` (the capital residue class for Game B's branch).
- **Game A (capital-independent).** Win probability `a = 1/2 − EPS = 49/100`; on win capital
  `+1`, on loss `−1`. Isolated drift `2a − 1 = −1/50 < 0` (LOSING — a gate, not an assumption).
- **Game B (capital-dependent on `s = capital mod 3`).** `s == 0` → "bad" coin
  `b0 = 1/10 − EPS = 9/100`; `s ∈ {1, 2}` → "good" coin `b1 = 3/4 − EPS = 37/50`; win `+1`,
  loss `−1`. Isolated drift (under Game B's OWN stationary residue law) must be `< 0` (LOSING
  — a gate).
- **Switching policy (headline).** RANDOM: at each step play A with probability `1/2`, else B
  (independent per step). The effective win probability at residue `s` is
  `w_s = (a + b_s)/2` → `w_0 = 29/100`, `w_1 = w_2 = 123/200`.
- **Reduced chain.** On residues `s ∈ {0, 1, 2}`: from `s`, go to `(s+1) mod 3` w.p. `w_s`
  (a win) and to `(s−1) mod 3` w.p. `1 − w_s` (a loss). The long-run drift is
  `D = Σ_s π_s · (2 w_s − 1)` where `π` is the chain's stationary distribution.

**The two arms.**

- **Arm A — DECISION (seedless, exact).** Build the three-residue transition matrix from the
  pinned constants, solve for the stationary distribution `π` in exact `fractions.Fraction`
  (3×3 rational linear solve), and compute the three long-run drifts as exact rationals:
  `D_A` (pure A), `D_B` (pure B, its own chain), `D_mix` (the random-switch chain). The
  ruling is a comparison of `D_mix` against pre-registered rational bands. Fully hermetic,
  byte-identical across process runs, no seed read.
- **Arm B — VALIDATION (seeded Monte Carlo).** Independently confirm the exact chain by
  direct capital simulation: run `N = 200,000` steps and measure the empirical per-step
  drift, checking it lands within tolerance of Arm A's closed form. Seeds are pre-registered
  BELOW; Arm B is reporting/validation only and never overrides Arm A.

**Seeds (pre-registered, strictly above the P047 high-water 20261328).**

- `20261329` — Arm B headline: random-switch mixed drift, `N = 200,000`; PASS iff
  `|D̂_mix − D_mix| ≤ 4·se` (se the standard error of the per-step mean).
- `20261330` — Arm B control: pure Game A, `N = 200,000`; confirms `D̂_A ≈ −1/50` (the
  A-losing precondition, live).
- `20261331` — Arm B control: pure Game B, `N = 200,000`; confirms `D̂_B ≈ D_B < 0` (the
  B-losing precondition, live).
- `20261332` — stability leg: re-run the mixed headline at a second seed; PASS iff the sign
  and the ≥ `1/1000` margin both reproduce.

**Decision rule (pre-registered, REJECT checked FIRST).** Let `D_mix` be Arm A's exact
combined drift.

1. **REJECT (checked first)** iff `D_mix ≤ 0` — the paradox FAILS to manifest at the
   conservative pin (the folk law does not survive `EPS = 1/100`). Also REJECT-adjacent
   **INVALID** (report, do not rule) iff either isolated-loss gate fails (`D_A ≥ 0` or
   `D_B ≥ 0`) — then the premise "two LOSING games" is not met and the test is void.
2. **APPROVE** iff `D_mix ≥ 1/1000` AND the `20261332` stability leg reproduces the sign and
   margin — the paradox manifests by a MATERIAL margin.
3. **NULL** iff `0 < D_mix < 1/1000` — the paradox manifests but is negligibly thin (a
   "technically-true-but-immaterial" honest null), OR any validity conjunct fails (Arm B
   disagrees with Arm A beyond tolerance, or a gate is INVALID).

**Liveness — expected landing DISCLOSED (this is a closed form, not an MC gamble).** Because
Arm A is a finite exact computation, honesty demands disclosing the drafting-time hand check
rather than pretending the landing is unknown: at the pinned constants this session computed
(stdlib `fractions`, disclosed as a NON-authoritative design-soundness check the sim
re-derives from scratch and must not trust) `D_A = −1/50 ≈ −0.0200` (losing ✓),
`D_B = −1529/87950 ≈ −0.01738` (losing ✓, stationary residues `π_B = (673/1759,
1633/10554, 4883/10554)`), and `D_mix = 26673/4429850 ≈ +0.006021` (winning ✓, stationary
residues `π_mix = (30529/88597, 1186/4663, 35534/88597)`). So the honest **expected landing
is APPROVE** — but thinly: the surviving margin is ≈ 0.6%/step, only ~6× the `1/1000`
material threshold, and a modestly larger `EPS` would cross both the NULL band and then
REJECT. The sim's value is therefore NOT suspense over the sign but (a) an INDEPENDENT
hermetic re-derivation guarding against the drafter's arithmetic, (b) the MC cross-check that
the discrete capital chain actually behaves as the closed form claims, and (c) the
reporting-only critical-`EPS` locator below. REJECT and NULL are both genuinely reachable
under the pre-registered rule (they would fire at a different pin), which is what keeps the
claim falsifiable.

**Reporting-only side pins (never gate the ruling).** (i) the stationary residue
distributions `π_B` and `π_mix` (exhibit the ratchet mechanism); (ii) a critical-`EPS`
sweep over `EPS ∈ {1/100, 3/200, 1/50, 1/40, 1/25}` reporting the sign of `D_mix(EPS)` — the
robustness margin (how far the conservative pin can be pushed before the paradox dies); (iii)
a periodic-switch comparator (the deterministic `[A, A, B, B]` pattern on the phase×residue
product chain) reported alongside the random-switch headline, to show the effect is not an
artifact of the mixing rule.

## Model basis — what is pinned vs a choice

- **`EPS = 1/100` is a conservative CHOICE.** A larger bias makes each game more strongly
  losing and eventually kills the paradox; a smaller one (e.g. the textbook 0.005) makes it
  survive more comfortably. Pinning `1/100` — twice the textbook bias — is the deliberate
  stress: the bands quantify only over this pin, and the critical-`EPS` sweep (reporting-only)
  discloses the full robustness picture.
- **`M = 3` and the coin triple `(1/2, 1/10, 3/4)` are the canonical Harmer–Abbott
  structure**, shifted by `EPS`; they are pinned, not swept (the sweep is over `EPS` only).
- **Random 1/2–1/2 switching is the headline; periodic `[A,A,B,B]` is a reporting-only
  comparator.** Both are named; only the random rule gates.
- **The isolated-loss gates are PRE-CONDITIONS, not results** — the sim asserts `D_A < 0` and
  `D_B < 0` before the combined drift is allowed to count as a paradox, so an accidental pin
  that made a game a winner is caught as INVALID, never mis-ruled as APPROVE.
- **Exact rationals throughout Arm A** — no float appears in the decision path; floats appear
  only in Arm B's empirical estimates and in the `≈` annotations of this file.

## Relations — dedup sweep (verify-first, live this slice)

Tree-wide sweep at the grounding pin `b56d802` (ripgrep, kit excluded) for
`parrondo|ratchet|losing game|capital.dependent|flashing ratchet|Harmer|Abbott` returned
ZERO domain hits across `ideas/`, `control/outbox.md`, and the section READMEs. PROPOSALs
001–047 re-scanned at HEAD before drafting; the seven prior rotation occupants (P017 social
choice, P024 congestion routing, P028 tournament seeding, P032 pattern races / Penney, P036
optimal stopping, P040 spatial self-organization, P044 queue-discipline) are all different
domains. **Nearest priors (disclosed, all distinct):** P032 Penney's game also lives in
elementary probability and also turns on a counterintuitive non-transitivity, but its
mechanism is a two-player PATTERN RACE over coin sequences (who sees their triple first),
with no capital, no state-dependence, and no ratchet — Parrondo is a single-player
CAPITAL-DEPENDENT drift where the "paradox" is a sign flip of long-run growth, a different
object entirely. P024 Braess is the other "adding a good thing makes it worse" head, but in
congestion routing over a fixed network (Wardrop equilibria), not stochastic game mixing.
No prior head, idea file, or session-card 💡 touches Markov-chain drift, capital-dependent
games, or ratchet dynamics.

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep quoted in
> `## Relations` returned ZERO domain hits at the grounding pin `b56d802`; PROPOSALs 001–047
> re-scanned, the seven prior rotation occupants are all different domains, and the nearest
> priors (P032 pattern races, P024 Braess) are disclosed with their distinguishing mechanism.
> (b) **kill test NOT triggered** — no prior proposal, idea file, or session-card 💡 touches
> Parrondo, capital-dependent games, Markov-chain drift, or ratchet dynamics. (c)
> **feasibility + liveness arithmetic checked** — runtime bounded (Arm A is a 3×3 rational
> solve, Arm B is four 200k-step loops; well under a minute, stdlib only); expected landing
> DISCLOSED with its exact drafting-time value (APPROVE, thinly) rather than hidden, all three
> rulings reachable under the pre-registered rule, the material-margin NULL band and the
> INVALID gate both named.

**1. What is this really?** A pre-registered exact MEASUREMENT of the most-cited
counterintuitive result in the statistical mechanics of games — does "two losing games
combine into a winner" actually manifest, and by a MATERIAL margin (operationalized: combined
per-step drift `≥ 1/1000`), at a deliberately CONSERVATIVE integer-lattice pin (`EPS = 1/100`,
twice the textbook bias) — computed as the exact-rational long-run drift `D_mix` of the
capital-mod-3 random-switch Markov chain, judged against bands fixed before any code (REJECT
`≤ 0` first, APPROVE `≥ 1/1000` with stability reproduction, NULL in the thin band or on
validity failure), every decision number an exact `Fraction`, byte-identical across two runs,
with a seeded Monte-Carlo arm cross-validating the closed form.

**2. What is the possibility space?** (i) Don't run it — the round-8 unrelated slot goes
unserved and the rotation closes short. (ii) Re-use a prior round's domain — fails the
owner's "rotate" ask (P017/P024/P028/P032/P036/P040/P044 occupy voting, routing, tournaments,
pattern races, stopping, spatial self-organization, queueing). (iii) A literature summary
("Parrondo's games win, see Harmer–Abbott 1999") — retells the textbook direction, measures
nothing on a committed frame, and dodges the live question (does it survive the conservative
pin, and by how much). (iv) An MC-only estimate of the sign — leaves the answer noisy and
seed-dependent when an EXACT rational closed form is available for the reduced chain, so the
DECISION arm is the exact solve and MC is demoted to validation. (v) This head: exact-rational
Arm A on the pinned chain as the ruling, seeded Arm B as the cross-check, REJECT-first bands
on `D_mix`, INVALID gate on the isolated-loss preconditions, robustness disclosed via a
reporting-only critical-`EPS` sweep. (vi) Over-scope (history-dependent Game B, `M > 3`,
mean-reverting biases, quantum Parrondo, spatial/networked variants) — each named here as a
follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One
~200-line stdlib file: a `Fraction` 3×3 stationary solver (Gaussian elimination on rationals)
parameterized by a per-residue win-probability vector — reused three times (pure A, pure B,
mixed) — plus one capital-stepping MC loop parameterized by a policy callable. That single
file yields an exact, reproducible ruling on a famous counterintuitive law at a stress pin,
AND — as free side pins — the stationary residue distributions that exhibit the ratchet
mechanism, the critical-`EPS` robustness curve, and a periodic-switch comparator, all from a
sim a verdict session runs cold in under a minute.

**4. What breaks it? (assumptions made explicit)** (a) **The pin is a choice** — `EPS = 1/100`
is one point; `## Model basis` names it as conservative and the critical-`EPS` sweep discloses
the full robustness curve; the bands quantify only over the pin. (b) **Band placement could
cherry-pick** — both bands are committed here BEFORE any code, are DISJOINT (`0 < 1/1000`),
NULL is first-class (the thin band AND validity failure), and the expected landing is
DISCLOSED (APPROVE, thinly) rather than hidden, so there is no room to retrofit. (c) **The
premise could silently fail** — an accidental pin making Game A or Game B a winner would make
"two losers → winner" vacuous; the isolated-loss gates assert `D_A < 0` and `D_B < 0` FIRST
and rule INVALID otherwise, never mis-APPROVE. (d) **An arithmetic bug in the drafter's hand
check** — the sim RE-DERIVES `π` and all three drifts from the pinned constants with zero
trust in this file's `≈` values, and Arm B's independent capital simulation cross-checks the
sign and magnitude by a completely different code path (direct stepping vs stationary solve),
so a solver bug shows up as an Arm-A/Arm-B disagreement → NULL. (e) **Metric myopia** — the
ruling is on LONG-RUN drift (the renewal-reward rate), the quantity the folk claim is about;
finite-capital ruin behavior, variance, and first-passage times are explicitly out of scope
and named as follow-ups, not smuggled into the headline.

**5. What does it unlock?** The pipeline's EIGHTH fleet-external verdict and the rotation
lane's proof it spans domains (voting → routing → tournaments → pattern races → stopping →
spatial self-organization → queueing → stochastic ratchets); a measured, citable answer to
"can mixing two losers win, and is the effect material or a curiosity" — the exact drift, the
robustness margin, and the mechanism-exhibiting residue distributions as standalone side pins;
and a clean, fully-hermetic exact-rational Markov-chain template (stationary solve + renewal
drift) that any later drift/absorption question in the fleet can reuse.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: Arm A's 3×3 rational solve settles the ruling in microseconds and needs
no seed; Arm B's four 200k-step loops (≈ a second) are the cross-check. The single cheapest
probe if a reader doubts a specific leg is the periodic-switch comparator at one `EPS` (one
extra product-chain solve), which shows the positive drift is not an artifact of the random
mixing rule.

**7. What would make this a mistake to run?** If the exact rational solve were somehow
unavailable (it is not — a 3-state chain always has a rational stationary law), or if the
domain duplicated a prior head (it does not — dedup returned zero), or if the ruling were
pre-determined in a way that made it worthless. The last is the sharpest self-check: the
landing is disclosed as APPROVE, so is this theater? No — the VALUE is the independent
hermetic re-derivation + MC cross-validation + the robustness curve, and the falsifiability is
real (REJECT and NULL fire at nearby pins; the pre-registered rule is genuine). It would only
be a mistake if run as a bare "compute a known constant"; framed as re-derive-plus-validate
-plus-locate-the-critical-boundary, it is a genuine, self-contained knowledge deliverable.

**8. How will we know it worked?** A committed sim-lab report with: Arm A's exact `D_A`, `D_B`,
`D_mix` as `Fraction`s and their `float` renderings; the stationary residue distributions;
the verdict token (APPROVE / REJECT / NULL) against the pre-registered bands; Arm B's four
seeded empirical drifts each inside tolerance of Arm A; the critical-`EPS` robustness column;
the periodic-switch comparator; and a byte-identity note (two process runs of Arm A produce
identical rationals). A clean run reproduces `D_mix = 26673/4429850` (the drafter's disclosed
reference) from scratch, or — the more interesting outcome — DISAGREES with it and pins the
drafter's arithmetic error, which the pre-registered rule then rules on honestly.

**Recommendation: sim-ready**
