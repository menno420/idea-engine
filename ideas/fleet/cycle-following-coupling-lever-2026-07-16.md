# The 50/50 crowd that wins a third of the time: with ONE shared random source, joint odds are a design variable the marginals cannot see — the cycle-following coupling lifts 100 "independent" coin flips from 2⁻¹⁰⁰ to exactly 1 − Σ₅₁..₁₀₀ 1/k ≈ 0.3118 (3.953 × 10²⁹× the independent baseline, floored above 1 − ln 2 forever) while every single player's odds stay exactly 1/2 — and of the two folk repairs against an adversary, relabeling is a conjugation NO-OP (0/720) while the one-sided remap restores the full 276/720

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 16 closer; a SIXTEENTH fleet-external domain: correlation design under shared randomness — the exact dependence structure of success EVENTS coupled through one random permutation's cycle skeleton (coordinated search / the cycle-following pointer strategy), disjoint from the fifteen prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052), random incidence (P056), repeated-game reciprocity (P060), information cascades (P064), two-sided matching (P068), group testing / screening design (P072), algebraic error detection (P076) — and deliberately NOT adjacent to the last three unrelated slots' domains: no two sides, no preferences, no stability and no market (vs P068's matching); no prevalence prior, no pooled tests, no locating of defectives and no cost curve (vs P072's group testing — that head priced a STOCHASTIC screening economy against an exogenous defect rate; here nothing is screened or located — the decision object is the joint-vs-marginal GAP of success events under one shared draw); no codes, no check algebra, no typos and no detection censuses (vs P076's error detection — that head was deterministic algebra on a single codeword; permutations appear in both, but there as pinned CHECK MAPS, here as the random OBJECT whose cycle skeleton carries the coupling))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@16480dbf0a630df3fe9d6b81bd1df7698e124b9f · fetched 2026-07-16T02:23:41Z
> (the dedup-sweep HEAD — the session branch head, containing main 636e21d — the only read this head takes; every model constant below is invented-but-pinned in this file, and the DECISION arms are exact seedless integer/Fraction arithmetic with zero repo/network reads at verdict time — the P017–P076 hermetic precedent; sim-lab dedup-swept READ-ONLY on the local clone @ 418de3e090ea89762a2135bcd63f4c229b2e8054, VERDICT 092 newest)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under the deliberate lane rotation (rule 3, "COMPLETELY UNRELATED domains — I want those too"); round 16 opened at fleet backlogs (P077 #442), served venture (P078 #443) and game mechanics (P079 #444, merged 2026-07-16), so this head is the round-16 UNRELATED closer. Slot spacing history P064, P068, P072, P076 → P080 (spacing 4) confirms the placement.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in `ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017 through 076 did.

## The folk belief

"Independent 50/50 chances multiply. A hundred people who each succeed half the time succeed together once in 2¹⁰⁰ tries — and since no strategy changes anyone's individual odds, no strategy can change the group's." This is the instinct behind every risk model that multiplies per-leg pass rates into a joint number, every redundancy design that counts replicas as independent, and every "each check passes 99% of the time, so the chain passes 0.99ᵏ" chain estimate. The instinct has two load-bearing halves: (1) that the joint probability is DETERMINED (or at least tightly constrained) by the marginals; (2) that a fix which provably leaves every marginal untouched is therefore group-neutral. Both are false in an exactly measurable way whenever the trials share a randomness source — and the classic coordinated-search world (2n players, 2n boxes, one hidden uniform permutation, each player opens n boxes hunting their own number) makes the gap exact: the marginals are pinned at 1/2 by an iron law, while the JOINT is a free design variable ranging from 0 (everyone opens the same n boxes) through 2⁻²ⁿ (independent random sets) up to ≈ 0.3118 (the cycle-following coupling) — a lift of thirty orders of magnitude with zero marginal movement.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

One uniform random permutation π of {1..m}, m = 2n (box b contains number π(b)); player i may open up to b boxes adaptively; the **pointer strategy**: open box i, read content c, open box c, follow the pointers. Player i succeeds iff the cycle of π containing i has length ≤ b; the GROUP succeeds iff NO cycle exceeds b — one shared event, not 2n independent ones. Five exact structure theorems, each verified live at drafting by enumeration and exact Fraction arithmetic (`draft_p080.py`, 41/41 checks PASS, exit 0, ~1.2 s). **T1 — the LEVER.** For b ≥ n at most one cycle can exceed b, and #{permutations of m with a cycle of length exactly k > b} = m!/k — so joint success = 1 − Σ_{k=b+1}^{m} 1/k EXACTLY. Verified three independent ways: brute enumeration at m ∈ {4, 6, 8} (censuses exactly **10 / 276 / 14,736**), the per-length law at m = 6 (180/144/120 = 6!/4, 6!/5, 6!/6), and the cycle-type partition census at m = 10 (**1,285,920** = 10!·P₅ = 10!·893/2520). Headline m = 100, b = n = 50: P₅₀ = 1 − Σ₅₁..₁₀₀ 1/k = an exact 41-digit/41-digit fraction ≈ **0.3118278207**, against the independent-random-sets baseline of EXACTLY 2⁻¹⁰⁰ ≈ 7.889 × 10⁻³¹ (independence holds given ANY fixed arrangement — the sets are independent draws; pencil) — a lift of exactly P₅₀·2¹⁰⁰ ≈ **3.953 × 10²⁹** — and the same-set baseline of EXACTLY 0 (pigeonhole: any fixed n-box set leaves n numbers outside it forever). Small worlds exact: P₁ = 1/2, P₂ = 5/12, P₃ = 23/60, P₄ = 307/840, P₅ = 893/2520. **T2 — MARGINAL INVARIANCE.** The cycle length of a FIXED element of a uniform permutation is uniform on {1..m} — exactly (m−1)! permutations per length (enumerated at m ∈ {4, 6, 8}) — so each player's own success probability at budget b is exactly **b/m** (enumerated 240/360/480 of 720 at m = 6, b ∈ {2, 3, 4}): the headline coupling moves NOTHING individually — 1/2 before, 1/2 after; the entire 10²⁹ lift lives in the dependence structure. **T3 — FAILURE CONCENTRATION.** The coupling doesn't reduce failure mass, it CONCENTRATES it: when the group fails, the long cycle's members fail together — E[# failing | joint failure] = 50/T₅₀ ≈ **72.6562** of 100 (exact Fraction; the survivors are exactly the short-cycle members). The budget dial is exact for b ≥ n: P(b) at m = 100 lands 0.4062346943 / 0.4924928953 / 0.7139781129 / 0.8951930852 / 99/100 at b = 55/60/75/90/99, with the monotone decrement law T_{n+1} − T_n = 1/((2n+1)(2n+2)) exact (verified n = 1..199) and the floor certified: P_n > 1 − ln 2 FOREVER (rational bracket for ln 2 via Σ 1/(k·2ᵏ) partial sums with tail bound; gap at n = 50 exactly ≈ 0.0049750). **T3b — where the shortcut LIES.** Below b = n the harmonic formula is WRONG (two long cycles can coexist) and the error is itself exact: at m = 10, b = 4 the true census is **632,736** = naive 560,160 + 10!/50 (the (5,5) double count); at m = 8, b = 3 it is **5,916** = naive + 8!/32 — the inclusion-exclusion correction registered as its own contact. **T4 — the ADVERSARY and the TWO REPAIRS.** Against an adversarial arrangement the deterministic pointer guarantee is exactly **0** (any single 2n-cycle kills ALL 2n players at once). The folk repair — "relabel the boxes with a shared random σ" — is a conjugation σ⁻¹πσ, which PRESERVES cycle type: enumerated over all 720 σ at m = 6, the 6-cycle arrangement stays lost **0/720** forever (and 3+3 stays won 720/720 — relabeling can neither break nor fix what cycle type already decided). The CORRECT repair composes one-sidedly: start at box σ(i) and read content c as pointer to box σ(c) — the effective permutation is π∘σ, uniform for ANY fixed π — restoring EXACTLY **276/720** (the uniform census) against every pinned arrangement (identity, the 6-cycle, 3+3 — all three enumerated). The drafting surprise worth the head: the repair pair differs only in WHICH SIDE of the composition the shared randomness enters, one side is a provable no-op and the other a full restoration — and the folk vocabulary ("randomize the labels") cannot tell them apart.

## Pinned model (committed constants — all invented-but-pinned, exact integers/Fractions)

- World: m = 2n boxes and players, one uniform random permutation π (box b holds number π(b)); each player opens up to b boxes ADAPTIVELY; group success = every player finds their own number. Headline m = 100, n = b = 50.
- Strategies pinned: **POINTER** (start at own label, follow contents); **INDEPENDENT** (each player an independent uniform n-subset — joint success exactly 2⁻ᵐ given any fixed arrangement, pencil); **SAME-SET** (all open one fixed n-set — joint success exactly 0, pigeonhole); **ONE-SIDED REMAP** (shared uniform σ: start at σ(i), read content c as σ(c) — effective permutation π∘σ); **CONJUGATION** (shared relabeling σ⁻¹πσ — the folk repair, priced as the no-op it is).
- Adversary arm: π chosen adversarially instead of uniformly; pinned arrangements at m = 6: identity, the 6-cycle (1,2,3,4,5,0), the 3+3 double cycle (1,2,0,4,5,3); the m = 100 adversarial witness is any single 100-cycle.
- Enumeration sizes: brute force m ∈ {4, 6, 8} (24 / 720 / 40,320 permutations, full loops); cycle-type partition census m ∈ {8, 10} (independent counting method); closed-form Fraction arithmetic at every m (the harmonic law).
- Budget grid at m = 100: b ∈ {50, 55, 60, 75, 90, 99} (harmonic-exact region b ≥ n); the below-n breakdown priced at (m, b) = (10, 4) and (8, 3) with exact correction terms.
- Arm A (DECISION, seedless): the harmonic law + per-length law + partition censuses + marginal law + repair/conjugation censuses + the floor bracket — all exact integer/Fraction, byte-identical across process runs.
- Arm B (twin, seedless, INDEPENDENTLY-WRITTEN): full brute enumerations at m ∈ {4, 6, 8} (joint censuses, per-length counts, per-element marginals) and the 720-σ repair loops — must equal Arm A through the typed contacts C1–C4 below.
- Arm R (seeded, REPORTING-ONLY): m = 100 episodes, one Fisher–Yates permutation per episode (exactly m − 1 = 99 `randrange` draws, i from 99 down to 1 — the registered draw-order grammar, one `random.Random` per seed); N = 20,000 on seed **20261714** (drafting preview: wins **6,131**, failing episodes **13,869**, total failing-player mass **1,007,767**; draws exactly **1,980,000**), stability leg N = 8,000 on **20261715** (preview: **2,455 / 5,545 / 403,116**; draws **792,000**), presentation shuffle **20261716** (presentation legs only). NO statistical gate rides Arm R — measured rates sit beside the exact censuses as a trace, never a ruling.
- Aux seed: **20261717**, reserved, never read by any leg (the P054–P079 aux convention).
- Seeds 20261714–717 allocated from 20261714 per the P079 card's baton: 20261710–713 are P079/V092's registered set (aux 20261713 never read), so 20261714 is the next free index. Boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at the grounding HEAD maxes at genuine 20261713, and the sim-lab clone READ-ONLY at 418de3e maxes at genuine 20261713 (V092's registered set); the standalone numerals 20261833 / 20261962 / 202670087 / 2026964142 are digit-substrings inside committed exact-fraction values — data, not seeds; the P046–P079 sweep-recipe trap re-confirmed.
- Typed must-equal contacts: **C1** — brute joint census == m!·P_{m/2} at m ∈ {4, 6, 8} (10 / 276 / 14,736) AND partition census == 10!·P₅ at m = 10 (1,285,920): three independent counting methods, one number. **C2** — per-length counts of a fixed element's cycle == (m−1)! each, summing to m!. **C3** — one-sided-remap census == 276 for ALL THREE pinned arrangements; conjugation census == {720, 0, 720}, frozen to cycle type. **C4** — true census == naive harmonic + the exact inclusion-exclusion term at (10, 4) (+10!/50) and (8, 3) (+8!/32).
- Runtime disclosure: the heaviest legs are the 8! brute loop and the 720² repair loops — the whole drafting battery runs in ~1.2 s; every other leg is ≤ 10⁵ operations plus big-Fraction arithmetic.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the independence multiplication is wrong as doctrine wherever trials share a randomness source: the joint is a DESIGN VARIABLE the marginals do not constrain — a coupling exists that lifts the group from 2⁻¹⁰⁰ to ≈ 0.3118 while provably moving no marginal; the lift is floored above 1 − ln 2 forever; failures concentrate instead of thinning; and of the two folk repairs, one is a conjugation no-op and the other a full restoration, distinguishable only by composition algebra": **(R1, the lever)** joint pointer success == 1 − Σ_{k=b+1}^{m} 1/k exactly for b ≥ n, C1's three counting methods agreeing (10 / 276 / 14,736 / 1,285,920), P₅₀ landing 0.3118278207 with the ratio to the independent baseline exactly P₅₀·2¹⁰⁰ ≈ 3.953 × 10²⁹ and the same-set pole exactly 0; **(R2, marginal invariance)** each player's own success at budget b == b/m exactly at every enumerated m (the (m−1)!-per-length law; 240/360/480 at m = 6) — the lift is pure dependence; **(R3, concentration + floor)** E[# failing | joint failure] = 50/T₅₀ ≈ 72.6562 of 100; P_n strictly decreasing with decrement exactly 1/((2n+1)(2n+2)) and P_n > 1 − ln 2 certified by the rational bracket (gap at n = 50 ≈ 0.0049750); **(R4, the repairs)** the adversarial 2n-cycle zeroes the deterministic pointer (all 2n fail at once), the conjugation repair stays 0/720 on the 6-cycle (cycle type frozen: {720, 0, 720} across the three arrangements), and the one-sided remap restores exactly 276/720 == the uniform census against EVERY pinned arrangement. (Checked FIRST because the costly direction is fleet-wide: every joint-risk estimate that multiplies per-check pass rates, every redundancy count, and every "each retry is a fresh 50/50" assumption silently asserts a coupling it never designed — and the fleet's own gate chains share seeds, branch state, and container images.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the folk belief holds: marginals determine the joint up to negligible slack, and no shared-source strategy materially beats the independent product": the pointer census equals the 2⁻ᵐ product census at any enumerated m (arithmetically excluded by C1 — 276 ≠ 720/2⁶ · 720; mutually exclusive with REJECT), or some enumerated marginal lands off b/m.
- **NULL** — anything else; pre-registered axes: **census-contact mismatch** (a C1/C4 counting method disagrees while each arm internally reproduces — the drafter's inclusion-exclusion or partition law is wrong; the corrected law is the finding, and this axis is genuinely LIVE: the harmonic shortcut really is false below b = n, and the registered corrections are exactly one sign error away from a real drafter regression); **repair-algebra mismatch** (the one-sided remap census ≠ 276 or the conjugation census moves off {720, 0, 720} — the composition direction is wrong; the corrected algebra is the finding); **floor-bracket failure** (the rational ln 2 bracket fails its own tail bound — the certificate construction is wrong; R3's floor clause falls back to the finite decrement law alone and the corrected bracket is the finding); twin-arm disagreement surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067 lesson, applied): the sim is FULLY DETERMINISTIC in every decision leg — every clause is an exact integer census, an exact Fraction identity, or a certified rational bracket; the only seeded arm is reporting-only with NO statistical gate (its sole gates are the draw-count sentinel 99N and exact reproducibility, pass probability 1 for a correct implementation); JOINT pass probability across all gates for a correct implementation = 1 EXACTLY (the P059–P076 no-stochastic-gate precedent), and decision separation is noise-free exact counting. MARGIN LEDGER, disclosed (the V083 practice): every REJECT clause is an exact-equality census or identity — the ledger names the registered EQUALITY cells a verdict session must land on exactly: the C1 triangle (10 / 276 / 14,736 / 1,285,920), the marginal cells (exactly b/m — saturated by the uniform-cycle-length law, no room to move), the conjugation row {720, 0, 720} (frozen by cycle-type invariance — 0 and 720 are the two poles, no interior), the repair row 276 == the uniform census (equality BY THE COMPOSITION THEOREM, not clearance), and the floor gap ≈ 0.0049750 (the one strict inequality, certified with an explicit rational margin). A census landing anywhere off these exact values is INVALID-or-NULL by the pre-registered axes, never a "close enough".

## Gates (run INVALID on any failure)

- **F1 — model identities:** cycle lengths of every enumerated permutation partition m (sum == m); factorial counts (24 / 720 / 40,320); the per-length counts sum to m! with each == (m−1)!; T_n and P_n definitions reproduce P₁..P₅ = 1/2, 5/12, 23/60, 307/840, 893/2520; the Fisher–Yates loop consumes exactly m − 1 draws per episode.
- **F2 — the structure theorems, exact:** (a) LEVER — the per-length law m!/k at m = 6 (180/144/120); the harmonic censuses at m ∈ {4, 6, 8} and the partition census at m = 10 (C1); the headline P₅₀, ratio, and 2⁻¹⁰⁰ values. (b) MARGINAL — the uniform-cycle-length law enumerated at m ∈ {4, 6, 8}; budget marginals 240/360/480 at m = 6 (C2). (c) BREAKDOWN — the below-n corrections at (10, 4) and (8, 3) with the partition census confirmed by brute force at (8, 3) (C4). (d) REPAIRS — the adversarial 6-cycle zero; the 720-σ one-sided and conjugation censuses across all three arrangements (C3). (e) FLOOR — the decrement identity for n = 1..199; the ln 2 rational bracket inside its own tail bound; P₅₀ > 1 − ln 2 with the gap value.
- **F3 — census anchors (reference values, exact):** 10 · 276 · 14,736 · 1,285,920 · 632,736 = 560,160 + 72,576 · 5,916 · P₅₀ = 0.3118278207 (41/41-digit fraction) · ratio ≈ 3.953 × 10²⁹ · 2⁻¹⁰⁰ ≈ 7.889 × 10⁻³¹ · E[# failing | fail] = 50/T₅₀ ≈ 72.6562 · budget rows 0.4062346943 / 0.4924928953 / 0.7139781129 / 0.8951930852 / 99/100 · marginals 240/360/480 · repairs 276/720 ×3 · conjugation {720, 0, 720} · floor gap ≈ 0.0049750.
- **F4 — the hand worlds (pencil):** (a) m = 2: pointer succeeds iff π = identity — P₁ = 1/2, vs the independent baseline 1/4 — the lever visible in the smallest possible world; (b) the decrement identity in three lines: T_{n+1} − T_n = 1/(2n+1) + 1/(2n+2) − 1/(n+1) = 1/((2n+1)(2n+2)); (c) same-set pigeonhole: any n-box set leaves n numbers outside it — their owners never see them, joint success 0 by inspection; (d) the independent baseline given a fixed arrangement: each set covers its target box with probability n/m = 1/2, sets independent, joint (1/2)ᵐ — no averaging needed.
- **F5 — degeneracy controls:** b = m gives P = 1 (everyone opens everything); b = m − 1 gives exactly 1 − 1/m (only the full m-cycle kills); b = 99 at m = 100 == 99/100 exactly; the identity arrangement succeeds under every strategy variant; the conjugation control on identity and 3+3 (720/720 — relabeling cannot break what cycle type already blessed).
- **F6 — battery:** Arm B enumerations equal Arm A closed forms through the FOUR typed must-equal contacts C1–C4; twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinel (exactly 99N: 1,980,000 / 792,000 at drafting) and exact reproducibility; presentation seed 20261716 read by presentation legs only; aux seed 20261717 never read; stdout + results.json byte-identical across two process runs (Arms A/B pure integer/Fraction arithmetic, platform-independent; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P076 exact-arm norm)

REJECT on all four conjuncts, at the drafter's exact values (the sim re-derives everything from scratch and must not trust these; every number below was computed live at drafting, 41/41 checks PASS, exit 0, ~1.2 s): **R1** — censuses 10 / 276 / 14,736 (brute) and 1,285,920 (partition == 10!·893/2520), P₅₀ ≈ 0.3118278207 (exact 41/41-digit fraction), ratio ≈ 3.953 × 10²⁹, poles 2⁻¹⁰⁰ ≈ 7.889 × 10⁻³¹ and 0; **R2** — (m−1)! per length everywhere enumerated, marginals exactly b/m (240/360/480 of 720); **R3** — 50/T₅₀ ≈ 72.6562, decrement 1/((2n+1)(2n+2)) for n = 1..199, floor gap ≈ 0.0049750 certified; **R4** — adversarial zero, conjugation {720, 0, 720}, one-sided remap 276/720 ×3. Falsifiability is real and named on three axes: (i) the **marginal-mover world** — if ANY enumerated budget marginal landed off b/m, R2 dies and with it the head's whole "the lift is free at the individual level" claim; the uniform-cycle-length law is gated by direct count, not cited; (ii) the **composition world** — a reader who believes any shared relabeling defeats the adversary is refuted by the head's own 0/720 conjugation row, and a reader who believes NO randomization can help is refuted by the 276/720 one-sided row — the head prices both sides of the algebra and would be falsified by either census landing elsewhere; (iii) the **shortcut world** — the harmonic formula is genuinely FALSE below b = n (naive at (10, 4) undercounts by exactly 10!/50): a verdict session reproducing the naive value as the true census would be finding a real drafter regression, and the census-contact NULL axis exists for exactly that. Disclosed sharpenings, reporting-only: the Arm-R previews ((6,131, 13,869, 1,007,767) at 20261714; (2,455, 5,545, 403,116) at 20261715 — both means within 0.006 of the exact values with zero tuning); the failure-mass trace (measured 72.6633 vs exact 72.6562); and the scale row — the coupling's lift over the independent baseline is ≈ 3.953 × 10²⁹ while the individual delta is EXACTLY zero.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof (a sixteenth domain) plus a transferable joint-risk correction. REJECT → "independent-looking marginals multiply into the joint" retires with numbers and the correction ships in three lines: (1) never multiply marginals into a joint without naming the coupling — with one shared randomness source the joint is DESIGNABLE from 0 to ≈ 1/3 while every marginal stays pinned at 1/2, so a chain estimate 0.99ᵏ over legs that share a seed, a branch state, or a container image is an assumption about dependence, not arithmetic (the fleet's own multi-check gates and retry ladders are the local instance); (2) failure CONCENTRATION is a design lever, not an accident — under the pointer coupling the group fails in one lump (≈ 72.66 of 100 together), which is exactly what shared-fate batching, all-or-nothing retries, and blast-radius design engineer on purpose: if you must fail, fail together and pay recovery once; (3) repairs against adversarial structure must be ALGEBRA-CHECKED, not vibed — the two folk-indistinguishable randomizations differ only in composition side, and one is a theorem-level no-op (conjugation preserves cycle type) while the other is a full restoration (one-sided composition is uniform against any arrangement). APPROVE → the independence default gains a measured basis and the census machinery ships as the priced non-fix. NULL → the named axis ships with the corrected law and full censuses. Follow-ups named, none in scope: OPTIMALITY of the pointer coupling among all strategies (the classic analytic result — an exhaustive strategy-space search is infeasible at m = 100 and the analytic proof is not an enumeration; this head prices the lever's existence and exact value, never its maximality); k-of-m partial-success objectives (a different risk shape); non-uniform permutation priors (weighted worlds); the anti-coupling direction (engineering the joint DOWN below the product for hedging — the same algebra, opposite sign, needs its own fixtures).

## Dedup

Tree-wide `rg -i 'prisoner|cycle.?follow|box.?opening|permutation cycle|longest cycle|pointer.?strategy'` (bootstrap.py/.substrate excluded) at the grounding HEAD: word collisions only — `ideas/fleet/braess-paradox-added-edge-2026-07-13.md` and `ideas/fleet/noisy-reciprocity-tft-collapse-2026-07-14.md` (+ its archived outbox block) say "prisoner" as PRISONER'S DILEMMA, the repeated 2-player game (P060's domain — zero shared object with coordinated search over a permutation). sim-lab READ-ONLY swept the same way at 418de3e: one hit, `sims/verdict-071-noisy-reciprocity/README.md`, the same Prisoner's-Dilemma word. Companion sweeps `rg -i 'harmonic|coupling|correlated failure'`: word-level only (grounding-pin "coupling" prose in checker doctrine files; no harmonic-sum decision object anywhere). No recorded drop of this domain exists on any card. No proposal P001–P079 and no verdict V001–V092 prices permutation cycle structure, coordinated search, joint-vs-marginal coupling design, or an adversary/repair composition census. Nearest priors argued distinct: **P052 → occupancy & collection** (coupon-collector tails price COMPLETION TIME of independent uniform draws — no permutation, no coupling design, no adversary; the shared word is "collection"); **P056 → random incidence** (length-biased WAITING at a random arrival — the nearest MATHEMATICAL kin since both exploit a size/length distribution law, but its object is a renewal process's interval bias and its decision a sampling correction; here the law in play is the UNIFORM cycle length of a fixed element — the anti-bias fact — and the decision object is a joint-probability design gap); **P060 → repeated-game reciprocity** (Prisoner's DILEMMA: strategic choice under payoffs, nothing hidden in boxes); **P064 → cascades** (sequential Bayesian inference — no beliefs here); **P068 → matching** (two-sided preferences — no sides here); **P072 → group testing** (pooled subset tests locating defectives under a prevalence prior — a screening ECONOMY; here nothing is located and no test has a cost); **P076 → error detection** (permutations as pinned check maps in a deterministic algebra — here the permutation is the random object itself and every decision quantity is a probability). Method kin only: the P028/P032/P048/P060/P072/P076 exact-census + twin-arm + no-stochastic-gate discipline, reused as machinery on a new object — this head's own additions to the battery: a THREE-method counting triangle (brute enumeration / cycle-type partition census / harmonic closed form) tied as one typed contact, an exact inclusion-exclusion correction registered as its own live NULL axis, and a repair PAIR priced by composition algebra (no-op vs full restoration) inside one fixture.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) the SHARED SOURCE is one uniform random permutation — the canonical exchangeable coupling surface; adversarial (non-random) arrangement is priced in R4 with its repair, and non-uniform priors are a named follow-up; (2) the STRATEGY CLASS pinned is {pointer, independent sets, same set, one-sided remap, conjugation} — optimality of the pointer coupling over ALL strategies is deliberately NOT claimed, gated, or needed (the head prices the gap between the independence doctrine and ONE constructive coupling; maximality is a named follow-up); (3) SMALL-m enumerations stand in for m = 100 via the counting identities (the C1 triangle and the m!/k law are m-uniform theorems, verified at every enumerated m and applied at 100 as exact Fraction arithmetic — an identity, not an extrapolation); (4) the BASELINES are pinned poles: independent uniform n-subsets (exactly 2⁻ᵐ given any arrangement, pencil-proved in F4) and same-set (exactly 0 by pigeonhole) — the folk belief is priced against its own best formalization, not a straw man. The ln 2 bracket is a pinned CONSTRUCTION whose tail bound is a gate — a wrong bracket fails F2(e) as INVALID and the floor-bracket NULL axis prices exactly that.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'prisoner|cycle.?follow|box.?opening|permutation cycle|longest cycle|pointer.?strategy'`
> (bootstrap.py/.substrate excluded) at the grounding HEAD returned word collisions
> only (Prisoner's-Dilemma prose in the P024/P060 files), and the sim-lab READ-ONLY
> sweep at 418de3e returned the same single word-class (verdict-071's README).
> (b) **kill test NOT triggered** — no prior proposal P001–P079, idea file, or
> session-card 💡 prices permutation cycle structure, coordinated search, or
> coupling design; no recorded runner-up drop of this domain exists. (c)
> **feasibility + liveness arithmetic checked LIVE** — every registered numeral ran
> this session by enumeration and exact Fraction arithmetic (the V080 lesson):
> the brute censuses at m ∈ {4, 6, 8}, the partition census at m = 10, the m!/k law,
> the uniform-cycle-length law, the below-n corrections, the 720-σ repair and
> conjugation loops, the headline P₅₀ / ratio / poles, the floor bracket with its
> gap, the budget rows, the failure-concentration value, the pencil worlds, and the
> seeded Arm-R previews with their 99N draw-count sentinel; expected landing
> DISCLOSED (REJECT) rather than hidden, all rulings reachable under the
> pre-registered rule, the marginal-mover / composition / shortcut falsifiability
> worlds all named, the genuinely-false-below-n harmonic shortcut disclosed with its
> exact correction terms, and the INVALID controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of the independence
folk belief — "marginals multiply into the joint, and a strategy that moves no
marginal cannot move the group" — taken where the belief actually breaks: success
events coupled through one shared random permutation's cycle skeleton. The three
exact structure facts the belief denies: the LEVER (joint success = 1 − Σ 1/k
exactly — ≈ 0.3118 at m = 100 against the independent product's 2⁻¹⁰⁰, a 10²⁹ lift),
MARGINAL INVARIANCE (each player exactly b/m always — the lift is pure dependence),
and the REPAIR ALGEBRA (conjugation is a cycle-type-frozen no-op, one-sided
composition a full restoration). All decision arithmetic is seedless exact
integer/Fraction counting judged against bands fixed before any code (REJECT first:
lever + invariance + concentration/floor + repairs; APPROVE: the product census or
a moved marginal; NULL otherwise on named axes), byte-identical across two runs,
with the seeded episode traces demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-16 unrelated
closer goes unserved and the rotation lane's coverage claim stalls at fifteen
domains. (ii) Re-use a prior round's domain — fails the owner's "rotate" ask; the
three most recent occupants (matching, group testing, error detection) are the
specific adjacencies this slot must avoid, and each is argued in the Dedup.
(iii) A folklore retelling ("the 100 prisoners riddle has a cute answer, look it
up") — retells a number without pre-registered bands, and misses what the exact
treatment uniquely gives: the three-method counting triangle, the below-n
correction the folklore never states (the harmonic formula is FALSE for b < n and
nobody says so), the marginal-invariance law gated by direct count, and the repair
PAIR priced by composition side — the no-op half is absent from every popular
telling. (iv) An MC-only sim — leaves every decision number seed-noisy when the
whole object is exactly countable (the V065/V067 lesson): the decision cells are
exact censuses and Fraction identities, MC is demoted to the episode trace. (v)
This head: exact counting as the ruling, REJECT-first bands on lever + invariance +
concentration/floor + repairs, INVALID on the F1–F6 gates, falsifiability via the
marginal-mover, composition, and shortcut worlds. (vi) Over-scope (strategy-space
optimality, k-of-m objectives, non-uniform priors, anti-coupling design) — each
named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: a cycle-length walker, three `itertools.permutations`
loops (24 / 720 / 40,320), a 720-σ repair loop, an integer-partition census, and
exact `Fraction` harmonic sums — that single kernel yields the joint census by
three independent methods, the headline 41-digit exact fraction and its 10²⁹ ratio,
the marginal-invariance law by direct count, the exact price of the below-budget
shortcut error, both repair censuses with their algebra decided, the certified
1 − ln 2 floor, and the seeded episode traces — from a sim a verdict session runs
cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **The shared source is the
model** — with genuinely independent per-player randomness the product law is
CORRECT and the head says so (the independent-sets pole is a pinned baseline, not a
victim); the verdict binds joint estimates over SHARED sources, and says so.
(b) **The strategy class is pinned, not exhaustive** — the head prices one
constructive coupling against the folk poles; a better coupling would only WIDEN
the gap (direction stated), and optimality is a named follow-up, never a clause.
(c) **Small-m enumeration stands in for m = 100 via m-uniform theorems** — the
counting triangle is gated at every enumerated size and the closed forms are
identities, not fits; a triangle mismatch is a named NULL, not a silent
extrapolation. (d) **Band placement could cherry-pick** — every band is an
exact-equality census committed before the sim, the expected landing is DISCLOSED
(REJECT), and the falsifiability worlds are structural: one moved marginal, one
wrong composition side, or one naive below-n census would each kill a clause.
(e) **The ln 2 bracket is a pinned construction** — a bracket failure is INVALID
plus a live NULL axis, and R3's decrement law stands independently of it.

**5. What does it unlock?** The pipeline's SIXTEENTH fleet-external verdict and the
rotation lane's domain-coverage proof extended (voting → routing → tournaments →
pattern races → stopping → spatial self-organization → queueing → ratchets →
occupancy → random incidence → reciprocity → observational learning → two-sided
matching → group testing → algebraic error detection → correlation design under
shared randomness); a measured, citable answer to "do marginals determine the
joint" with three standalone pins (the 10²⁹ lift at zero marginal cost; the exact
failure-concentration value 50/T₅₀; the conjugation-vs-composition repair
censuses); and a transferable joint-risk correction for every fleet surface that
multiplies per-leg pass rates over legs sharing a seed, a branch state, a container
image, or a wake schedule.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arm A settles every decision number exactly in
seconds with no seed. The single cheapest probe if a reader doubts a specific leg
is pencil: at m = 2 the pointer group wins iff the permutation is the identity —
probability 1/2 where independence predicts 1/4 — and the same-set group NEVER
wins; the lever, the pole, and the pigeonhole all visible in a two-box world.

**7. What would make this a mistake to run?** If the exact treatment were
unavailable (it is not — every decision quantity is a finite census or an exact
Fraction identity), if the domain duplicated a prior head (it does not — zero
domain hits in both trees, the Prisoner's-Dilemma word collisions cited and
distinct, the P056 mathematical kinship argued and severed), or if the disclosed
REJECT made the run theater. It does not: the value is the independent hermetic
re-derivation of the counting triangle (three methods, one number — a wrong
partition census or a wrong inclusion-exclusion term breaks the contact loudly),
the marginal law re-counted rather than cited, the repair algebra re-enumerated on
all three arrangements, and both non-REJECT rulings genuinely reachable (APPROVE is
one census-equality away; the census-contact and repair-algebra NULLs are one real
mistake away).

**8. How will we know it worked?** A committed sim-lab report with: the joint
censuses at every enumerated m by all three methods, the per-length marginal
tables, the below-n correction identities, the 720-σ repair and conjugation
censuses across all three pinned arrangements, the headline exact fraction with
ratio and poles, the budget rows, the concentration value, the certified floor
bracket with its gap, the F1–F6 gate results, the verdict token against the
pre-registered bands, Arm R's measured rates beside the exact censuses
(reporting-only, 99N draw counts asserted), and a byte-identity note (two process
runs identical). A clean run reproduces the drafter's disclosed reference values
(10 / 276 / 14,736 / 1,285,920; P₅₀ = 0.3118278207; 240/360/480; {720, 0, 720} and
276 ×3; 632,736 = 560,160 + 72,576; gap 0.0049750) from scratch, or — the more
interesting outcome — DISAGREES and pins the drafter's error, which the
pre-registered rule then rules on honestly (the census-contact, repair-algebra, and
floor-bracket NULL axes exist for exactly that).

**Recommendation: sim-ready**
