# Why an eye for an eye goes blind at any error rate: Tit-for-Tat vs the complete memory-one field under execution noise

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 11 closer; an ELEVENTH fleet-external domain: repeated games & the evolution of cooperation / reciprocity under trembling-hand execution noise, disjoint from the ten prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052), random incidence (P056))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@db5074e2df040b0a7310a600b9bd206ac60263ab · fetched 2026-07-14T05:51:47Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is invented-but-pinned in this file, zero repo/network reads at verdict time — the P017–P056 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 11 has served fleet backlogs (P057 #391), venture (P058 #395) and game mechanics (P059 #402), so this head is the round-11 UNRELATED closer. Provenance: this exact domain is P024's card-recorded runner-up, deduped and DROPPED that slice ("prisoner's-dilemma tournament-strategy frequency — method-adjacent to the game-mechanics heads P015/P016/P020/P023, weakest 'completely unrelated' claim"); reopened here with the drop reason answered — see Dedup.

**Placement note (decide-and-flag):** this fleet-external pure-game-theory head lives in `ideas/fleet/` per the check_sections carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, 044, 048, 052 and 056 did.

## The folk belief

"Tit-for-Tat is the best strategy in the repeated prisoner's dilemma." Axelrod's tournaments made it a management-book staple: cooperate first, then mirror your counterparty's last move — be nice, retaliatory, forgiving, clear — and you top the table. The popular reading quietly generalizes it twice: from Axelrod's curated 1980 entrant pool to STRATEGY SPACE ("the best"), and from perfectly-executed moves to the real world, where an intended cooperation occasionally comes out as a defection (a dropped message, a missed deadline, a flaky handshake).

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Both generalizations are load-bearing, and the second one hides an exact, ε-independent collapse. Give each player a trembling hand — the executed move flips the intended one with probability ε, independently per player per round. Two TFTs then echo any slip forever: one tremble turns mutual cooperation into an alternating retaliation pattern that only another tremble can break, and the breaking tremble is as likely to make things worse as better. The clean way to see it: a TFT-vs-TFT round maps last round's executed pair (a, b) to next round's pair (flip₁(b), flip₂(a)) — two INDEPENDENT ε-flips of a permuted state — so the uniform distribution over the four states {CC, CD, DC, DD} is stationary at EVERY ε ∈ (0, 1), and the long-run mutual payoff is exactly (3 + 0 + 5 + 1)/4 = 9/4, independent of ε. Not "degrades with noise": one part per thousand of execution error costs a strict mirror rule a full quarter of the cooperation surplus, the same as ten percent does. Meanwhile a repair rule — win-stay lose-shift (WSLS/"Pavlov": keep your move after a good round, change it after a bad one) — steers the pair back to CC in two rounds after a slip, so its self-play payoff is 3 − O(ε), and strategies that simply defect harvest the field's exploitable half unpunished by anyone but the reciprocators. Whether "best" survives any of this in the COMPLETE deterministic memory-one strategy space — all 16 rules (c_CC, c_CD, c_DC, c_DD) ∈ {0,1}⁴, not a curated entrant pool — is exactly computable: each ordered pair of rules under noise is a 4-state Markov chain whose stationary distribution is an exact rational linear solve, no simulation error, no seed.

## Pinned model (committed constants — all invented-but-pinned, exact rationals)

- Stage game: standard PD payoffs to the row player u(C,C) = 3, u(C,D) = 0, u(D,C) = 5, u(D,D) = 1 (T=5 > R=3 > P=1 > S=0 and 2R > T+S — both preconditions asserted in-sim).
- Strategy space Π: ALL 16 deterministic memory-one rules r = (c_CC, c_CD, c_DC, c_DD) ∈ {0,1}⁴ — the intended move given last round's executed (my move, opponent's move); named members TFT = (1,0,1,0), WSLS = (1,0,0,1), ALLC = (1,1,1,1), ALLD = (0,0,0,0). No curation: the complete field, closed under every relabeling.
- Noise: trembling-hand execution — executed move = intended move flipped w.p. ε, independent per player per round. Noise grid ε ∈ {1/1000, 1/100, 1/20, 1/10} in pinned order, decision cell ε = 1/100; control cells ε = 1/2 (F5 degeneracy) and ε = 0 (orbit leg, reporting + hand anchors).
- Value: for each ordered pair (i, j) and each grid ε, the 4-state chain on executed pairs (a, b) has transition P((a,b) → (x,y)) = q(x | rᵢ(a,b)) · q(y | rⱼ(b,a)) with q(x|m) = 1−ε if x = m else ε; the chain is irreducible for 0 < ε < 1 (every entry ≥ ε² > 0), the stationary π is the unique exact-`Fraction` solution of πP = π, Σπ = 1, and v(i,j) = Σ_s π(s)·u(s). First moves provably don't enter the ε > 0 limit (unique stationary chain); at the ε = 0 orbit leg both players open C (pinned convention, disclosed boundary) and v₀(i,j) is the exact average over the deterministic orbit's cycle.
- Tournament score: score(i) = (1/16) Σ_j v(i,j) over all 16 opponents including self (round-robin with self-play, uniform weights — Axelrod's own convention); rank = descending-score position (dense; exact-Fraction comparisons, ties broken lexicographically by rule tuple for the printed table only, never by any decision clause).
- Arm A (the DECISION arm, seedless): exact `fractions.Fraction` Gaussian elimination per pair per ε — 4 grid ε × 256 ordered pairs of 4×4 solves — plus the ε = 0 orbit evaluator (cycle detection on ≤ 4 states) and the ε = 1/2 degeneracy check; every decision number an exact rational, byte-identical across process runs.
- Arm B (twin, seedless): an INDEPENDENTLY-WRITTEN evaluator solving each stationary system by a different exact method (Cramer's rule / adjugate over `Fraction`s); must reproduce every v(i,j) EXACTLY at every grid ε.
- Arm R (seeded, REPORTING-ONLY): finite-horizon tournament estimate at ε = 1/100 — all 136 unordered pairs, T = 4,000 rounds per game, both open C, trembles via `random.Random(20261377)` (pinned draw order: pairs in lexicographic rule order, exactly 2 uniform draws per round); stability leg `random.Random(20261378)` at T = 1,000; presentation shuffle 20261379. NO statistical gate rides Arm R — a finite-horizon estimate drifting from the stationary value is a named finding (mixing time), never a ruling; Arm R's only gates are its draw-count sentinel (2T per game, counted and asserted) and byte reproducibility.
- Aux seed: 20261380, reserved, never read by any leg (the P054–P059 aux convention).
- Seeds 20261377–380 strictly above P059's 20261376 high-water; boundary-aware re-sweep this session — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD db5074e and the sim-lab clone READ-ONLY at 09782df (GitHub HEAD 49833d0 verified control/inbox.md-only via commit stats, +7 lines, no seeds) — maxes at genuine 20261376 / 20261372; the larger standalone numerals 20261542/20261833 (Fraction-numerator digit substrings) and the 9-digit 202670087 (the decimal-fraction substring of `"delta_cond": 0.202670087`, sim-lab verdict-032 results.json) are data, not seeds — the P046–P059 sweep-recipe trap re-confirmed.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the folk claim fails in the complete field under any execution noise — TFT's self-play collapses by the exact ε-independent echo factor to 9/4 (75% of full cooperation) while the repair rule WSLS holds 3 − O(ε), and TFT's tournament mean sits materially below WSLS at realistic noise": at the decision cell ε = 1/100, score(WSLS) − score(TFT) ≥ 2/5 exact, AND v(TFT,TFT) = 9/4 exactly at EVERY grid ε, AND rank(TFT) strictly worse (numerically larger) than rank(WSLS) at EVERY grid ε, AND v(WSLS,WSLS) ≥ 14/5 at ε = 1/100. (Checked FIRST because the costly direction is codifying a strict mirror rule anywhere errors exist: the echo identity says the tax is 25% of the cooperation surplus at ANY error rate — it does not shrink as execution improves.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the folk claim survives the complete noisy field": rank(TFT) = 1 at the decision cell ε = 1/100 AND rank(TFT) ≤ rank(WSLS) at EVERY grid ε. (Mutually exclusive with REJECT by arithmetic on the rank conjunct.)
- **NULL** — anything else; pre-registered axes: margin-straddle (the rank conjuncts hold but the ε = 1/100 gap lands in (0, 2/5) — the finding is the exact gap-vs-ε curve with the decision cell named); noise-floor-conditional (the ε = 1/1000 cell inverts the TFT/WSLS rank order relative to the decision cell — the finding is WHERE on the ε axis reciprocity dies, with the ε = 0 orbit table as the boundary exhibit); echo-identity-failure-without-gate-failure (v(TFT,TFT) ≠ 9/4 at some grid ε while F1–F6 all pass — the drafter's hand proof is wrong, and the finding is the corrected law); twin-arm disagreement surviving the INVALID diagnosis.

## Gates (run INVALID on any failure)

- **F1 — field & solve identities:** the 16 rules re-enumerated as all of {0,1}⁴ with the four named indices reproduced; the PD preconditions (T > R > P > S, 2R > T + S) asserted; every stationary solve: entries ≥ 0, Σπ = 1 exactly, residual πP − π = 0 exactly (all `Fraction`s).
- **F2 — the echo theorem:** TFT-vs-TFT stationary = (1/4, 1/4, 1/4, 1/4) exactly at every grid ε (hand proof pinned above: next-state coordinates are independent flips of the permuted pair, so the uniform law is invariant); hence v = 9/4 exactly.
- **F3 — closed-form anchors** at every grid ε, exact: v(ALLC,ALLC) = 3(1−ε)² + 5ε(1−ε) + ε²; v(ALLD,ALLD) = (1−ε)² + 5ε(1−ε) + 3ε²; v(ALLD,ALLC) = 5(1−ε)² + 3ε(1−ε) + ε(1−ε) + ε² · 0 — reference values at ε = 1/100: 29899/10000, 10299/10000, 49401/10000 (independent-marginal products, no linear solve).
- **F4 — transpose conservation:** for every ordered pair and grid ε, v(i,j) from the row-player accounting equals the column-player value of the transposed solve (j,i) — computed both ways, exact equality.
- **F5 — the ε = 1/2 degeneracy:** EVERY pairwise value = 9/4 exactly (executed moves are fair coins regardless of rule; uniform stationary for all 256 pairs).
- **F6 — battery:** Arm B reproduces every Arm-A v(i,j) exactly at every grid ε; ε = 0 orbit hand anchors (v₀(TFT,ALLD) = 1 — one slip-free absorption into DD; v₀(WSLS,ALLD) = 1/2 — the CD↔DD two-cycle; v₀(TFT,TFT) = v₀(WSLS,WSLS) = 3); twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinels (2T per game) counted and asserted; aux seed 20261380 never read; stdout + results.json byte-identical across two process runs (Arms A/B platform-independent exact rationals; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P059 closed-form-arm norm)

REJECT, at the drafter's exact prototype values (the sim re-derives everything from scratch and must not trust these): v(TFT,TFT) = 9/4 at all four grid ε (the echo identity); v(WSLS,WSLS) = 187188187/62500000 ≈ 2.9950 (ε = 1/1000), 737773/250000 = 2.951092 (1/100), 5553/2000 = 2.7765 (1/20), 1301/500 = 2.602 (1/10); decision-cell scores score(TFT) = 66320495249/30396000000 ≈ 2.181882, score(WSLS) = 152492158669156561/57041072808000000 ≈ 2.673375, gap = 9345083308624553/19013690936000000 ≈ 0.4915 ≥ 2/5; ranks TFT 10 / WSLS 5 at ALL four grid ε; ALLD tops the table at every noisy ε (597/200 = 2.985 at 1/100) and ties at 3 with two exploiters at ε = 0. Falsifiability is real: the gap conjunct held nothing a priori — the gap SHRINKS with noise (0.5216 → 0.4915 → 0.3738 → 0.2581 across the grid; already below 2/5 at ε = 1/20, so one decision-cell step right lands margin-straddle NULL) and the ε = 0 orbit gap is only 1/12 ≈ 0.083 (a noise-free world lands NULL, not REJECT — the margin is noise-BORN, which is the point); the rank conjunct could have failed at the near-noiseless ε = 1/1000 cell and did not. Disclosed sharpenings, reporting-only: v(TFT,TFT) is DISCONTINUOUS at ε = 0 (orbit value 3; exactly 9/4 for every ε > 0 — a genuine singular perturbation, the sharpest statement of the echo tax); TFT still beats WSLS in the vs-ALLD column (v₀ 1 vs 1/2 at ε = 0; 510001/500000 vs 107/200 at 1/100) — retaliation's genuine virtue, priced and reported, it just cannot pay the echo tax; ALLD's table-top is a statement about UNIFORM COMPLETE fields (an exploiter's paradise by construction), not an evolutionary equilibrium — boundary stated below.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof plus a transferable method note. REJECT → the folk rule retires with numbers and the correction ships in two exact lines: (1) a strict mirror rule pays 9/4 of 3 — a permanent 25% cooperation tax — at ANY nonzero error rate (the tax does not shrink as execution improves; it is ε-independent), and (2) repair beats retaliation under noise (WSLS's 3 − O(ε) vs TFT's 9/4) while pure exploitation tops uniform fields that no one curates. The transfer surface is anywhere the fleet codifies counterparty-mirroring: retry/backoff handshakes between seats, tit-for-tat trust rules in review exchanges ("respond in kind to the last interaction"), any protocol where an agent echoes the counterparty's last observed behavior and observations can be wrong — the echo identity says mirror rules lock error in forever, and the fix is a WSLS-shaped repair clause ("after a bad round, change something"), not a lower error rate. APPROVE → the folk rule gains a measured basis in the complete field. NULL → the named axis ships with the exact gap-vs-ε and rank-vs-ε curves. Follow-ups named, none in scope: replicator/ecological dynamics on the same exact table (Axelrod's second tournament ecology), mixed/stochastic memory-one strategies (zero-determinant strategies live there), longer memories, observation noise (misperceiving vs misexecuting — a different chain).

## Dedup

Tree-wide `rg -i 'prisoner|tit.?for.?tat|axelrod|reciprocit|pavlov|win.?stay|lose.?shift|iterated game|repeated game|trembling|memory.one'` (bootstrap.py/.substrate excluded) at HEAD db5074e — exactly ONE domain hit: P024's Braess card records this domain as a runner-up deduped and DROPPED that slice ("prisoner's-dilemma tournament-strategy frequency — method-adjacent to the game-mechanics heads P015/P016/P020/P023 — weakest 'completely unrelated' claim"). Reopened here with the drop reason answered on both horns: (1) the "method-adjacent" worry named MC frequency-estimation shared with early game-mechanics heads — this head is exact stationary-chain arithmetic with a hand-provable identity as its centerpiece, seeded MC demoted to reporting-only, so the shared machinery is gone; (2) the game-mechanics lane heads (P015/P016/P020/P023 … P059) price SPECIFIC fleet game economies (idle folds, casino envelopes, badge crossings, escort mints) — none prices a two-player strategy space, a stage-game payoff matrix, or an equilibrium/tournament claim; ten rounds later the slot's coverage spans ten domains and strategic reciprocity is in none of them. sim-lab sweep (read-only, same regex): only karma/reputation PROSE in intake-001 probe fixtures — no repeated-game content. No proposal P001–P059 and no verdict V001–V070 (V069 = P058's rubric world finalized REJECT; V070 in flight on P059's prestige world, zero overlap) prices a repeated game, a strategy tournament, or reciprocity under noise. Nearest priors argued distinct: **P032 → V043** (Penney's game — a two-"player" pattern-race on coin flips: no strategy space, no stage payoffs, no repeated interaction; the object is first-occurrence waiting times), **P048 → V059** (Parrondo — a SINGLE gambler's capital walk switching between two losing games: no opponent, no strategic response, the paradox is a ratchet on a modular chain), **P028 → V039** (tournament seeding — bracket STRUCTURE for exogenous strengths: who meets whom, never how agents choose actions), **P040 → V051** (Schelling — many-agent threshold relocation on a lattice: no payoff matrix, no dyadic repeated play), **P059 → V070-in-flight** (a policy grid for a single-player idle economy against its own committed label — policy-vs-policy but zero strategic interaction). Method kin only: the P017–P059 exact-arm + pre-registered-bands discipline (nearest: P048's exact stationary solve — reused as machinery on a different object: 256 strategic chains vs one capital chain).

## Model basis (declared model-dependence — the P024 discipline)

Three modeling commitments carry the verdict, each pinned and directional: (1) TREMBLING EXECUTION (my own move flips) rather than misperception (I misread yours) — execution noise is the standard Axelrod-era robustness probe and admits the product-form chain; misperception is a different transition kernel, named follow-up, direction unstated. (2) The COMPLETE UNIFORM field with self-play — the honest reading of "the best strategy" as a strategy-space claim; a curated or evolutionarily-weighted field is a different (named) question, and the boundary is stated in the landing: ALLD topping a uniform complete field is not an equilibrium claim. (3) LONG-RUN AVERAGE payoff (stationary limit) rather than discounted — the ε > 0 chains are irreducible so the limit exists and is start-independent; discounting re-admits first-move effects, named follow-up. The echo identity (9/4 at every ε) is robust to (2) and (3) — it is a two-player fact, not a field fact.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'prisoner|tit.?for.?tat|axelrod|reciprocit|pavlov|win.?stay|lose.?shift|iterated game|repeated game|trembling|memory.one'`
> (bootstrap.py/.substrate excluded) at the grounding pin `db5074e` returned ONE
> domain hit — P024's recorded dropped runner-up, reopened with the drop reason
> answered (see Dedup); sim-lab (read-only) returned prose-only fixture hits.
> (b) **kill test NOT triggered** — no prior proposal P001–P059, idea file, or
> session-card 💡 prices a repeated game, a strategy tournament, or reciprocity
> under noise. (c) **feasibility + liveness arithmetic checked** — runtime bounded
> (Arms A/B are 4 × 256 exact 4×4 rational solves + a 256-pair orbit sweep,
> sub-second; Arm R is 136 × 4,000 two-draw rounds, seconds, stdlib only);
> expected landing DISCLOSED with its exact drafting-time values (REJECT,
> gap ≈ 0.4915 at the decision cell) rather than hidden, all rulings reachable
> under the pre-registered rule, the margin-straddle/noise-floor NULL axes and
> the INVALID controls gate all named.

**1. What is this really?** A pre-registered exact MEASUREMENT of the folk claim
"Tit-for-Tat is the best strategy in the repeated prisoner's dilemma", taken where the
claim actually lives: the COMPLETE 16-rule deterministic memory-one strategy space under
trembling-hand execution noise ε ∈ {1/1000, 1/100, 1/20, 1/10} — every pairwise long-run
payoff an exact `fractions.Fraction` stationary solve of a 4-state Markov chain (256
ordered pairs per ε), the tournament table and ranks exact, judged against bands fixed
before any code (REJECT first: decision-cell gap score(WSLS) − score(TFT) ≥ 2/5 AND the
9/4 echo identity at every ε AND grid-wide rank inversion AND WSLS self-play ≥ 14/5;
APPROVE: TFT rank 1; NULL otherwise with named axes), byte-identical across two runs,
with a seeded finite-horizon arm demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-11 unrelated closer
goes unserved and the rotation closes short. (ii) Re-use a prior round's domain — fails
the owner's "rotate" ask (P017/P024/P028/P032/P036/P040/P044/P048/P052/P056 occupy
voting, routing, tournaments, pattern races, stopping, spatial self-organization,
queueing, ratchets, occupancy, random incidence). (iii) A literature summary ("noise
hurts TFT, Pavlov wins — see Nowak & Sigmund") — retells the direction, measures nothing
against a pre-registered band, and misses the sharpest exact fact (the ε-INDEPENDENT 9/4
echo identity and its ε = 0 discontinuity). (iv) An MC-only tournament — leaves every
table entry seed-noisy when the whole object is exactly solvable, so the DECISION arms
are the exact stationary/orbit solves and MC is demoted to reporting (the V065/V067
lesson, applied at drafting). (v) This head: complete-field exact table as the ruling,
REJECT-first bands on the gap + ranks + the echo identity, INVALID on the
F1–F6 identity/anchor/degeneracy/transpose/twin gates, robustness disclosed via the
gap-vs-ε curve and the vs-ALLD column. (vi) Over-scope (replicator ecologies, mixed and
zero-determinant strategies, longer memories, misperception noise, discounting) — each
named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: a 4×4 exact-`Fraction` stationary solver (Gaussian
elimination; the twin re-solves by Cramer) parameterized by two 4-bit rules and ε, a
≤ 4-state orbit-cycle evaluator for ε = 0, and one loop over 16 × 16 × grid. That single
kernel yields the complete exact tournament table at every noise level, the exact ranks,
the echo identity verified as a THEOREM CHECK rather than an estimate, the ε = 0
discontinuity exhibit, and the vs-ALLD retaliation column — all from a sim a verdict
session runs cold in under a minute.

**4. What breaks it? (assumptions made explicit)** (a) **Execution-vs-perception noise
is a choice** — the pinned trembling hand is the standard robustness probe and gives the
product-form kernel; misperception (players disagree about history) is a DIFFERENT chain
on a larger state space, named follow-up, direction unstated by design. (b) **The
uniform complete field is a choice** — it is the honest reading of "the best strategy"
as a strategy-space claim, but it is deliberately exploiter-friendly (every sucker
strategy present at equal weight); the boundary is stated in the landing (ALLD's
table-top is not an equilibrium claim), the nice-subfield restriction ships as a
reporting table, and the replicator ecology is the named follow-up. (c) **Band placement
could cherry-pick** — the 2/5 gap band, the 14/5 WSLS floor, and the rank conjuncts are
committed BEFORE the sim, the expected landing is DISCLOSED (REJECT), and the
falsifiability is two-sided: the gap already fails 2/5 at ε = 1/20 (one decision-cell
step lands NULL) and the ε = 0 orbit world's gap of 1/12 would land NULL — the REJECT
margin is noise-born and the bands can see that. (d) **Self-play inclusion and uniform
weights** — Axelrod's own convention, pinned; excluding self-play or reweighting is a
reporting sensitivity, never the decision. (e) **An arithmetic slip in the drafter's
hand proof** — the sim re-derives everything from scratch; the echo identity is gated
(F2) and separately the decision rule carries the
echo-identity-failure-without-gate-failure NULL axis, so a wrong hand proof becomes a
finalized finding (the corrected law), not a silent bad gate.

**5. What does it unlock?** The pipeline's ELEVENTH fleet-external verdict and the
rotation lane's proof it spans domains (voting → routing → tournaments → pattern races →
stopping → spatial self-organization → queueing → ratchets → occupancy → random
incidence → repeated-game reciprocity); a measured, citable answer to "is TFT actually
the best, and what does noise do to reciprocity" with three standalone side pins (the
exact ε-independent 9/4 echo identity and its ε = 0 discontinuity; the exact gap-vs-ε
curve showing the WSLS margin is noise-born; the vs-ALLD column showing retaliation's
real virtue survives even as its self-play collapses); and a transferable protocol
correction for anywhere the fleet codifies counterparty-mirroring under fallible
observation: mirror rules lock errors in forever at ANY error rate — add a repair
clause, don't chase a lower ε.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: Arms A/B settle every decision number exactly in sub-second time
with no seed. The single cheapest probe if a reader doubts a specific leg is the echo
identity by hand (from any state, next state = (flip of opp's last, flip of my last);
sum over the four equally-weighted states of two independent flips lands uniform again;
uniform × payoffs {3,0,5,1} averages 9/4), which anchors the entire noisy kernel against
a three-line pencil proof.

**7. What would make this a mistake to run?** If the exact solve were unavailable (it is
not — 4-state chains with rational ε have rational stationary laws), if the domain
duplicated a prior head (it does not — the sweep's one hit is P024's recorded DROP of
this very domain, reopened with the drop reason answered), or if the disclosed REJECT
made the run theater. It does not: the value is the independent hermetic re-derivation
of a hand-provable identity PLUS the parts no hand proof gives — the exact gap-vs-ε
curve (which crosses the 2/5 band INSIDE the grid), the grid-wide rank stability of the
inversion, and the complete-field table itself — and both non-REJECT rulings are
genuinely reachable (a gap under 2/5 lands NULL one grid step from the decision cell;
rank 1 for TFT was arithmetically open until the table existed).

**8. How will we know it worked?** A committed sim-lab report with: the full 16 × 16
exact value table per grid ε (Fractions + float renderings), the score/rank table per ε,
the ε = 0 orbit table, the F1–F6 gate results, the verdict token against the
pre-registered bands, Arm R's finite-horizon estimates beside the exact values
(reporting-only), and a byte-identity note (two process runs identical). A clean run
reproduces the drafter's disclosed reference values (gap ≈ 0.4915, ranks 10/5, 9/4
everywhere on the TFT diagonal) from scratch, or — the more interesting outcome —
DISAGREES and pins the drafter's error, which the pre-registered rule then rules on
honestly (the echo-identity NULL axis exists for exactly that).

**Recommendation: sim-ready**
