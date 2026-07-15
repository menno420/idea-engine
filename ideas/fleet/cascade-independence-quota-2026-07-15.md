# The crowd that stops learning after three and a half moves: information cascades, the knife-edge theorem, and the price of a mandated blind-first quota

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 12 closer; a TWELFTH fleet-external domain: sequential observational learning / information cascades (the Bikhchandani–Hirshleifer–Welch mechanism), disjoint from the eleven prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052), random incidence (P056), repeated games & reciprocity (P060))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@1ff66b9425b3ca64e65885d80578338ae0f5fa48 · fetched 2026-07-15T04:22:04Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is invented-but-pinned in this file, zero repo/network reads at verdict time — the P017–P060 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 12 has served fleet backlogs (P061 #408), venture (P062 #410) and game mechanics (P063 #419), so this head is the round-12 UNRELATED closer. Flagged, not obeyed: the EAP close-out walkthrough §E baton line "round 13 opens at the fleet-backlogs slot" miscounts (it skips this unserved closer); the committed slot arithmetic (P017/P020, P024, P028, P032, P036, P040, P044, P048, P052, P056, P060 → P064, spacing 4) and the round-12 sequence both put P064 here.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in `ideas/fleet/` per the check_sections carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, 044, 048, 052, 056 and 060 did.

## The folk belief

"More visible history never hurts — let everyone see what everyone before them chose, and the crowd self-corrects; with enough people the truth wins out." The wisdom-of-crowds reading treats observational transparency as free information: each newcomer gets their own evidence PLUS everyone else's choices, so a bigger crowd should always be a smarter crowd, and forcing anyone to ignore the crowd ("decide blind") reads as pure waste. The popular reading quietly assumes what it needs to prove: that predecessors' CHOICES still carry their EVIDENCE.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

They don't, and the failure is exact, early, and permanent. Let agents act in sequence on a binary question (state A or B, prior 1/2), each holding one private signal that is right with probability p ∈ (1/2, 1), each seeing all predecessors' ACTIONS (never their signals). A Bayesian agent follows its own signal only while the observed history is close to balanced; the moment the revealed lead reaches 2, the history outweighs any single signal, the agent copies the herd regardless of what it privately saw — and from that point every action is an echo, carrying zero information. The crowd's learning STOPS: with the standard follow-own-signal tie-break the revealed lead is a ±1 random walk (up w.p. p) absorbed at ±2, the herd locks after 2/(1 − 2pq) actions in expectation (q = 1 − p; exactly 100/29 ≈ 3.45 actions at p = 7/10), and the probability the entire infinite crowd herds on the WRONG answer is q²/(1 − 2pq) — an N-INDEPENDENT constant (9/58 ≈ 0.155 at p = 7/10). One hundred agents or a million: the crowd's accuracy is capped at 49/58 ≈ 84.5% forever, while the same hundred signals aggregated INDEPENDENTLY (majority vote) would be right 99.998% of the time. The cascade wastes almost all of the crowd's information, and it is individually rational — a late agent free-riding on the herd scores 84.5% > its solo 70%, so no one defects voluntarily. That is exactly the shape of problem a MECHANISM must fix and advice cannot: mandate an independence quota — the first k actors must follow their own signal (equivalently: they act blind, or their evidence is published instead of their conclusion) — and the k revealed signals hand every later Bayesian a majority-of-k head start. Whether the shipped k = 0 world ("everyone sees everything, everyone free-rides") is actually optimal, what the optimal quota k\* is at a finite horizon, and where the quota's leverage physically lives in the walk — all of it is exactly computable: the post-quota process is the same absorbing walk started from a Binomial(k, p) lead, every accuracy an exact `fractions.Fraction`, no simulation error, no seed. Drafting found three hand-provable structure theorems that the sim must confirm as gates: (1) QUOTA-NULL — k = 1 and k = 2 change NOTHING (the process is identical to k = 0: the first speaker is effectively blind anyway, and the tie-break makes the second reveal too); (2) PARITY — e(2m+1) = e(2m+2) exactly (the even panel member is informationally FREE: an odd panel's lead is odd, and odd leads never sit on the cascade boundary); (3) KNIFE-EDGE — the quota's entire long-run leverage flows through panels landing EXACTLY on the boundary lead ±2 (every interior lead is harmonically null: h(0) = q·h(−1) + p·h(1) makes one more signal a wash; the improvement e(2m) − e(2m+1) equals the rescue term at lead −2 minus the damage term at lead +2, in closed form). Consequence of (2)+(3): the optimal quota is ALWAYS odd — and it was, at every one of the twelve computed grid cells.

## Pinned model (committed constants — all invented-but-pinned, exact rationals)

- State θ ∈ {A, B}, prior 1/2. Signals i.i.d. given θ, correct w.p. p; grid p ∈ {11/20, 7/10, 4/5, 9/10} in pinned order, decision cell p = 7/10; control cells p = 1/2 (F5 degeneracy) and p = 1 (perfect-signal anchor). All published accuracies computed conditioned θ = A; an in-sim SYMMETRY gate (relabel A↔B, signals flipped) certifies the unconditional values equal the conditioned ones.
- Agents i = 1..N act once, in order, each seeing all prior ACTIONS plus own signal; payoff 1 iff action = θ. Horizon grid N ∈ {25, 100, 400}, decision cell N = 100.
- Bayesian rule, derived in-sim from likelihood ratios (p/q)^ℓ over the revealed lead ℓ: strict posterior preference acts on it; INDIFFERENCE follows OWN signal (pinned tie-break convention — the boundary section prices this choice; the random tie-break is the named follow-up). Consequences, gated not assumed: pre-cascade agents act = own signal; the revealed lead is a ±1 walk absorbed at |ℓ| = 2; absorbed agents copy the herd (actions uninformative, cascades never break).
- Mechanism: an independence quota k — agents 1..k are mandated to act = own signal (publicly known indices; their actions reveal their signals exactly). Post-quota lead L_k = 2·Bin(k, p) − k; |L_k| ≥ 2 cascades immediately, else the walk resumes. Quota grid k ∈ {0, 1, …, min(N, 120)}, argmax interiority gated (k\* ≤ 118).
- Metrics, all exact `Fraction`: ruin probabilities h(ℓ) = P(hit −2 before +2 | ℓ) for ℓ ∈ {−1, 0, 1}; wrong-herd probability e(k, p) = P(L_k ≤ −2) + Σ_{|ℓ|≤1} P(L_k = ℓ)·h(ℓ); per-agent accuracy trajectory acc_i(k); welfare V(N, k, p) = Σ_{i≤N} acc_i = k·p + Σ_{i>k} acc_i; optimal quota k\*(N, p) = argmax_k V (ties broken to the smallest k, ties reported); gain G(N, p) = V(N, k\*) − V(N, 0); runner-up margins; expected lock-in time 2/(1 − 2pq); the knife-edge decomposition; the independent-aggregation benchmark (majority of N i.i.d. signals, exact, reporting-only).
- Arm A (the DECISION arm, seedless): forward absorbing-walk DP over states {lead −1, 0, 1, cascade-A, cascade-B} with the Binomial quota initial condition — exact `fractions.Fraction` throughout, byte-identical across process runs. Runtime bounded: the full grid is minutes, stdlib only.
- Arm B (twin, seedless): an INDEPENDENTLY-WRITTEN backward memoized recursion over (agents remaining, lead-or-cascade) — must reproduce every Arm-A number EXACTLY; plus the algorithm-free census gate: exhaustive enumeration of all 2^12 signal paths at N = 12 (every grid p, every k ≤ 12), equal to BOTH arms exactly.
- Arm R (seeded, REPORTING-ONLY): Monte-Carlo trace of the literal 100-agent process at the decision cell, k ∈ {0, k\*} — per episode: 1 uniform for θ, then N uniforms for signals, pinned draw order, draw counts (N + 1 per episode) counted and asserted; 100,000 episodes on `random.Random(20261563)`; stability leg `random.Random(20261564)` at 20,000; presentation shuffle 20261565. NO statistical gate rides Arm R — an MC drift from the exact curves is a named finding, never a ruling.
- Aux seed: 20261566, reserved, never read by any leg (the P054–P063 aux convention).
- Seeds 20261563–566 strictly above the fleet high-water 20261562 (V074's registration 20261559–62, recorded at docs/HANDOFF.md §3 / walkthrough §E and re-swept FIRSTHAND this session); boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD 1ff66b9 (max genuine 20261392, P063's allocation) and the sim-lab clone READ-ONLY at origin/main aa8627e (max genuine 20261562) — the larger standalone numerals 20261833 (Fraction-numerator digit substring) and 9-digit 202670087 (the decimal-fraction substring of sim-lab verdict-032 results.json) are data, not seeds; the P046–P063 sweep-recipe trap re-confirmed.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "full observational transparency is not free: the shipped k = 0 'everyone sees everything' regime pays a permanent herding tax, and a mandated blind-first quota materially beats it — the mechanism, not more people or better signals, is what recovers the crowd's information": at the decision cell (p = 7/10, N = 100), G ≥ 6 expected correct actions exact, AND k\* ≥ 5, AND e(k\*) ≤ (1/2)·e(0) exact. (Checked FIRST because the costly direction is fleet-wide: protocols that show later deciders their predecessors' CONCLUSIONS — recommendation-first asks, visible review approvals, verdict-token-first summaries — inherit the cascade cap, and codifying "more visible history is always better" ships a permanent, N-independent accuracy ceiling.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the transparent herd is near-optimal — a mandated independence quota wastes information": G ≤ 2 AND k\* ≤ 2 at the decision cell. (Mutually exclusive with REJECT by arithmetic on both clauses.)
- **NULL** — anything else; pre-registered axes: band-straddle (G ∈ (2, 6), or k\* ∈ {3, 4}, or the e-halving clause alone fails — the finding is the exact V(k) and e(k) curves with the decision cell named); parity-theorem failure without gate failure (e(2m+1) ≠ e(2m+2) somewhere while F1–F6 pass — the drafter's hand proof is wrong and the corrected law is the finding); knife-edge-decomposition failure without gate failure (same shape — the corrected boundary algebra is the finding); twin-arm disagreement surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067 lesson, applied): the sim is FULLY DETERMINISTIC — every decision clause and every F-gate is an exact-rational identity, structural assertion, or byte comparison; the only seeded arm is reporting-only with NO statistical gate (its sole gates are the draw-count sentinel and exact reproducibility, pass probability 1 for a correct implementation); JOINT pass probability across all gates for a correct implementation = 1 EXACTLY (the P059–P063 no-stochastic-gate precedent: determinism proven by byte-identical re-run, not estimated), and decision separation is noise-free exact arithmetic — the disclosed landing clears the G band at 1.44×, the k\* band at 3×, and the e-halving band at 2.34×, so the ruling cannot move except via a mis-implemented model, which the anchor gates catch as INVALID.

## Gates (run INVALID on any failure)

- **F1 — model & Bayes identities:** the Bayesian action table re-derived in-sim from the likelihood ratios (p/q)^ℓ, including the tie-break (pre-cascade agents provably act own signal; absorption at |ℓ| = 2; cascades never break); state-mass conservation at every DP step (Σ = 1 exact); every acc_i ∈ [0, 1]; V(N, N) = N·p exactly; the θ-relabeling SYMMETRY gate (the θ = B run reproduces every published number).
- **F2 — the three structure theorems, exact at every grid cell:** (a) QUOTA-NULL — the k ∈ {0, 1, 2} processes yield identical e AND identical V at every (N, p); (b) PARITY — e(2m+1) = e(2m+2) for every published m ≥ 1 (and e(0) = e(1) = e(2)); (c) the harmonic identities h(0) = q·h(−1) + p·h(1), h(1) = q·h(0), h(−1) = q + p·h(0), plus the KNIFE-EDGE decomposition e(2m) − e(2m+1) = P(L = −2)·(1 − q − p·h(−1)) − P(L = +2)·q·h(1) — reference value 441/14500 at (p = 7/10, m = 1). Hand proofs pinned in the mechanism section.
- **F3 — closed-form anchors:** e(0) = q²/(1 − 2pq) — reference 81/202, 9/58, 1/17, 1/82 across the p grid; h(−1), h(0), h(1) at p = 7/10 = 237/580, 9/58, 27/580; expected lock-in time 2/(1 − 2pq) = 100/29 at 7/10; the p = 1 anchor (e = 0, V = N exactly).
- **F4 — the hand world:** p = 2/3 — h = (7/15, 1/5, 1/15), e(3) = 23/135, V(6, 3) = 350/81, all by a pinned pencil walk (the three-state ruin solve plus one 6-agent tree).
- **F5 — the p = 1/2 degeneracy:** e(k) = 1/2 for EVERY k and V(N, k) = N/2 exactly (signals are coins; no mechanism can help).
- **F6 — battery:** Arm B reproduces every Arm-A number exactly; the 2^12 exhaustive path census at N = 12 equals both arms exactly (every grid p, every k ≤ 12); k\* interior to the quota window (k\* ≤ 118); twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinels (N + 1 per episode) counted and asserted; aux seed 20261566 never read; stdout + results.json byte-identical across two process runs (Arms A/B platform-independent exact rationals; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P063 closed-form-arm norm)

REJECT, at the drafter's exact prototype values (the sim re-derives everything from scratch and must not trust these): decision cell (p = 7/10, N = 100) — V(100, 0) ≈ 83.983353 (per-agent 0.839834), k\* = 15 (unique argmax; runner-up k = 17 by ≈ 0.004925 — thin and disclosed, stable under exact arithmetic on the pinned world), V(100, 15) ≈ 92.634608, G ≈ 8.651255 ≥ 6 (1.44×); e(0) = 9/58 ≈ 0.155172, e(15) = 481791730791717/14500000000000000 ≈ 0.033227 ≤ 9/116 ≈ 0.077586 (2.34×); k\* = 15 ≥ 5 (3×). Full k\* table (all ODD, every cell): p = 11/20 → 9 / 33 / 109 across N = 25 / 100 / 400; p = 7/10 → 7 / 15 / 29; p = 4/5 → 5 / 9 / 15; p = 9/10 → 3 / 5 / 7. Gain table G(N, p): 0.4139 / 7.3513 / 69.9867 (11/20); 0.7402 / 8.6513 / 50.8877 (7/10); 0.3801 / 3.7539 / 20.2465 (4/5); 0.0905 / 0.7859 / 4.1973 (9/10). Falsifiability is real on every clause: the N = 25 cell lands G ≈ 0.7402 ≤ 2 with k\* = 7 (a MIXED cell — one horizon step left of the decision cell lands band-straddle NULL, the quota's value is horizon-born); the p = 9/10 column lands G ≈ 0.7859 at N = 100 (one signal-quality step up and the gain clause fails — good signals barely cascade wrong); the p = 4/5 cell lands G ≈ 3.7539 ∈ (2, 6) (straddle territory one step up); and k\* ≤ 2 (= APPROVE) was arithmetically open until the welfare table existed — the QUOTA-NULL theorem says small quotas do literally nothing, so the mechanism could have been worthless everywhere. Disclosed sharpenings, reporting-only: the bounded-learning constant — baseline crowd accuracy 1 − e(0) = 49/58 ≈ 0.8448 at p = 7/10 is N-INDEPENDENT (25 or 400 agents: same cap; expected lock-in after 100/29 ≈ 3.45 actions) while majority-vote over 100 INDEPENDENT signals scores ≈ 0.9999845 — the herd wastes almost all of the crowd's information; the individual-rationality wedge — a late transparent-world agent scores 49/58 ≈ 84.5% > solo p = 70%, so herding is individually RATIONAL and the fix genuinely needs a mandate (each quota member accepts 70% < the 84.5% it would get free-riding — the mechanism pays a named, priced sacrifice k·(0.845 − 0.7) ≈ 2.2 actions and buys ≈ 10.8 back); the parity/knife-edge structure — even panel members are exactly free long-run (e(2m+1) = e(2m+2)) and strictly wasteful finite-horizon (V(100, 2m+2) < V(100, 2m+1) at every computed m ≥ 1, e.g. V(100, 16) ≈ 92.3846 < V(100, 15)), so panels should always be odd; expected wrong agents at the decision cell fall 16.02 → 7.37 out of 100.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof (a twelfth domain) plus a transferable protocol correction. REJECT → the folk rule retires with numbers and the correction ships in two lines: (1) wherever later deciders see predecessors' CONCLUSIONS but not their EVIDENCE — recommendation-first structured-choice asks (the Q-0263.2 protocol shape), visible-approval review chains, verdict-token-first summaries — publish the SIGNAL alongside the conclusion (evidence-forward summaries restore full learning at zero accuracy cost; the cascade exists only because actions are coarser than signals); (2) where only conclusions can be shown, blind the first speakers — a mandated independence quota sized ≈ k\*(N, p), always ODD (the parity theorem: an even panel's last member contributes exactly nothing long-run and less than nothing finite-horizon). The knife-edge theorem is the transferable design lens: a mechanism that injects independent information into a stopping process has leverage ONLY at the process's own stopping boundary — audit where an intervention binds before pricing it. APPROVE → the transparent-herd default gains a measured basis and the quota machinery ships as the priced non-fix. NULL → the named axis ships with the exact V(k)/e(k) curves. Follow-ups named, none in scope: the random tie-break convention (the classic BHW belief-state chain — different constants, same bounded-learning shape); heterogeneous/costly signals; actions visible only in a moving window; strategic misreporting; richer action spaces (continuous reports dissolve cascades — the boundary section states it).

## Dedup

Tree-wide `rg -i 'cascade|herd(ing)?|bandwagon|social.learning|observational.learning|bikhchandani|wisdom.of.crowds|conformity|groupthink|independence quota'` (bootstrap.py/.substrate excluded) at HEAD 1ff66b9: ZERO domain hits — every match is a word collision in another sense (API "quota" capability notes; "quotation-negation" in the heartbeat-linter head; prose in audit tables). sim-lab sweep (READ-ONLY at origin/main aa8627e, same regex): the verdict-046 "purchase cascade" is an idle-economy fluid-refill model (resources cascading through purchase windows — no agents, no signals, no inference) and the verdict-012 fixture hits are quoted UI prose — no sequential-learning content anywhere. No recorded drop of this domain exists on any card (unlike P060's reopened P024 runner-up — this is the slot's first entry into the domain). No proposal P001–P063 and no verdict V001–V076 (ledger read FIRSTHAND at sim-lab origin/main aa8627e: 76 verdicts, newest V074 by timestamp plus the V075/V076 pair) prices sequential observational learning, Bayesian inference from observed actions, herding, or an information-flow mechanism. Nearest priors argued distinct: **P060 → V071** (the nearest kin by "multi-agent + folk claim" — repeated games price dyadic STRATEGIC payoff interdependence: a strategy space, a stage-game payoff matrix, payoffs coupled to the opponent's move; here payoffs depend ONLY on matching an exogenous state — no strategy space, no payoff coupling, agents are one-shot Bayesian best-responders and the priced object is INFORMATION FLOW through coarse observed actions), **P017 → V018** (social choice — aggregation RULES over fixed submitted ballots; no signals, no sequential observation, no inference: the cascade head has no voting rule at all, and its failure is informational, not preference-aggregation), **P036 → V047** (optimal stopping — ONE decision-maker timing ONE decision on its own observation stream; no inter-agent inference, and the walk here is a state variable, not a stopping payoff), **P044 → V055** (queue discipline — waiting-time systems, zero inference) and **P062 → V073** (deterministic sequencing of a FIXED known to-do list — the only "order" kin, and it has no uncertainty anywhere), **P040 → V051** (Schelling — threshold RELOCATION on a lattice; no state to learn, no Bayesian content), **P053 → V064** (detection of an external transient by ONE observer on a cadence — no social observation). Method kin only: the P048/P060/P061 exact absorbing/stationary-chain discipline, reused as machinery on a new object (an absorbing lead walk with a mechanism-indexed Binomial initial condition — the quota grid is this head's own addition).

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) the FOLLOW-OWN-SIGNAL tie-break — the convention that makes the revealed lead a clean ±1 walk and gives the quota-null/parity/knife-edge theorems their exact form; the classic random tie-break yields a different (belief-state) chain with the SAME bounded-learning shape (wrong-herd probability bounded away from zero, N-independent) but different constants — named follow-up, and the theorems are stated as convention-conditional. (2) BINARY actions — the coarseness of the action space IS the cascade engine; continuous/graded reports restore full learning, so this head prices FIXED binary-choice surfaces (approve/reject, adopt/skip), stated in the landing. (3) HOMOGENEOUS signal quality p, known mechanism (quota indices public) — heterogeneity and hidden mechanisms are named follow-ups; publicity is what makes quota actions fully informative. (4) WELFARE = unweighted sum of per-agent correctness over a KNOWN horizon N — the planner's objective; discounted or last-agent-only objectives re-weight the same exact trajectory (reporting flavors, never the decision). The bounded-learning constant e(0) = q²/(1 − 2pq) is robust to (3) and (4) — it is a two-boundary walk fact, not a welfare fact.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'cascade|herd(ing)?|bandwagon|social.learning|observational.learning|bikhchandani|wisdom.of.crowds|conformity|groupthink|independence quota'`
> (bootstrap.py/.substrate excluded) at the grounding pin `1ff66b9` returned zero
> domain hits (word collisions only: API-quota capability notes, quotation-negation
> prose); sim-lab READ-ONLY at origin/main `aa8627e` returned an idle-economy
> "purchase cascade" fluid model and quoted UI prose — no sequential-learning
> content. (b) **kill test NOT triggered** — no prior proposal P001–P063, idea
> file, or session-card 💡 prices observational learning, herding, or an
> information-flow mechanism; no recorded runner-up drop of this domain exists.
> (c) **feasibility + liveness arithmetic checked** — runtime bounded (Arm A is
> an exact-Fraction 5-state DP over N ≤ 400 × a ≤ 121-cell quota grid × 4 signal
> cells, minutes, stdlib only; the 2^12 census and Arm R are seconds); expected
> landing DISCLOSED with its exact drafting-time values (REJECT, G ≈ 8.65 at the
> decision cell) rather than hidden, all rulings reachable under the
> pre-registered rule, the straddle/theorem-failure NULL axes and the INVALID
> controls gate all named.

**1. What is this really?** A pre-registered exact MEASUREMENT of the folk claim
"more visible history never hurts — the crowd self-corrects", taken where the claim
actually lives: a sequential binary-choice crowd whose members see predecessors'
ACTIONS but not their EVIDENCE, priced against the cheapest counter-mechanism (a
mandated blind-first independence quota k), on exact `fractions.Fraction`
absorbing-walk arithmetic — the wrong-herd probability e(k), the welfare surface
V(N, k), and the optimal quota k\*(N, p) all exact at every grid cell, judged against
bands fixed before any code (REJECT first: decision-cell gain ≥ 6 correct actions AND
k\* ≥ 5 AND e(k\*) ≤ e(0)/2; APPROVE: gain ≤ 2 AND k\* ≤ 2; NULL otherwise with named
axes), byte-identical across two runs, with the seeded trace demoted to
reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-12 unrelated
closer goes unserved a second time (the EAP shutdown already left it unserved once,
and the walkthrough baton's round-13 miscount would have buried it). (ii) Re-use a
prior round's domain — fails the owner's "rotate" ask (the eleven occupants span
voting, routing, tournaments, pattern races, stopping, spatial self-organization,
queueing, ratchets, occupancy, random incidence, reciprocity). (iii) A literature
summary ("cascades are fragile and wrong with positive probability — see BHW 1992")
— retells the direction, measures nothing against a pre-registered band, and misses
what the exact treatment uniquely gives: the THREE structure theorems (quota-null,
parity, knife-edge) and the exact optimal-quota table. (iv) An MC-only sim — leaves
every decision number seed-noisy when the whole object is exactly solvable (the
V065/V067 lesson, applied at drafting): the decision arms are exact DP/recursion,
MC is demoted to reporting. (v) This head: exact welfare surface as the ruling,
REJECT-first bands on gain + quota size + error halving, INVALID on the
F1–F6 identity/theorem/anchor/degeneracy/census gates, robustness disclosed via the
full 12-cell k\*/gain tables and their two live edges. (vi) Over-scope (random
tie-break chains, heterogeneous signals, strategic misreporting, moving windows,
continuous actions) — each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~250-line stdlib file: a three-value exact ruin solve, a Binomial initial
condition, and a forward 5-state `Fraction` DP — that single kernel yields the exact
wrong-herd curve e(k, p), the exact welfare surface V(N, k, p) with its optimal-quota
table, all three structure theorems verified as THEOREM CHECKS rather than estimates,
the knife-edge decomposition in closed form, the bounded-learning constant beside the
independent-majority benchmark, and the individual-rationality wedge — from a sim a
verdict session runs cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **The tie-break convention is
a choice** — follow-own-signal gives the clean walk and the exact theorem forms; the
classic random tie-break changes constants (not the bounded-learning shape) and is
the named follow-up; every theorem is stated convention-conditional. (b) **Binary
actions are a choice** — they are the cascade engine; the head prices fixed
binary-choice surfaces and says so in the landing (continuous reports dissolve the
whole phenomenon). (c) **Band placement could cherry-pick** — the 6/2 gain bands, the
k\* ≥ 5 / ≤ 2 clauses, and the e-halving clause are committed BEFORE the sim, the
expected landing is DISCLOSED (REJECT), and the falsifiability is two-sided: the
N = 25 cell and the p = 9/10 column both land the gain clause under 2 (one grid step
moves the ruling), the p = 4/5 cell sits inside the straddle band, and QUOTA-NULL
made "the mechanism is worthless" (APPROVE) arithmetically live until the table
existed. (d) **The thin k\* runner-up margin** — k\* = 15 beats k = 17 by only
≈ 0.0049 expected actions; exact arithmetic on the pinned world reproduces it
deterministically, and no decision clause reads the runner-up gap (k\* enters only
via k\* ≥ 5 vs ≤ 2, which the 15-vs-17 ambiguity cannot cross); the margin is
disclosed as reporting. (e) **An arithmetic slip in the drafter's hand proofs** — the
sim re-derives everything from scratch; all three theorems are F2 gates AND carry
their own theorem-failure-without-gate-failure NULL axes, so a wrong hand proof
becomes a finalized finding (the corrected law), not a silent bad gate.

**5. What does it unlock?** The pipeline's TWELFTH fleet-external verdict and the
rotation lane's domain-coverage proof extended (voting → routing → tournaments →
pattern races → stopping → spatial self-organization → queueing → ratchets →
occupancy → random incidence → reciprocity → observational learning); a measured,
citable answer to "is transparency free, and what does a blind-first quota buy" with
four standalone side pins (the N-independent bounded-learning constant beside the
independent-majority benchmark; the ~3.45-action expected lock-in time; the
quota-null + parity + knife-edge theorem set with the always-odd-panel corollary;
the individual-rationality wedge showing why the fix needs a mandate); and a
transferable protocol correction for anywhere the fleet shows conclusions without
evidence — publish the signal, or blind the first speakers, and never mandate an
even panel.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arms A/B settle every decision number exactly in
minutes with no seed. The single cheapest probe if a reader doubts a specific leg is
the quota-null identity by hand (agent 1 has no history, so its Bayesian action
already equals its signal — a k = 1 mandate changes nothing; at lead ±1 the
tie-break makes agent 2 reveal either way — k = 2 changes nothing; both are one-line
consequences of the harmonic identity h(0) = q·h(−1) + p·h(1)), which anchors the
walk model against a three-line pencil proof.

**7. What would make this a mistake to run?** If the exact solve were unavailable
(it is not — a 5-state absorbing walk with rational p has rational absorption laws
and finite-horizon marginals), if the domain duplicated a prior head (it does not —
the sweep returned zero domain hits in both repos and no recorded drop exists), or
if the disclosed REJECT made the run theater. It does not: the value is the
independent hermetic re-derivation of three hand-proved theorems PLUS the parts no
hand proof gives — the exact optimal-quota table (k\* = 15 at the decision cell was
not derivable by hand; the always-odd pattern across all twelve cells was a
drafting-time DISCOVERY), the exact gain surface with its two live edges, and the
knife-edge decomposition constants — and both non-REJECT rulings are genuinely
reachable one grid step from the decision cell.

**8. How will we know it worked?** A committed sim-lab report with: the exact
e(k, p) curves and V(N, k, p) surface (Fractions + float renderings), the
k\*/gain/runner-up tables over all twelve cells, the three theorem verifications,
the knife-edge decomposition values, the bounded-learning constant beside the
majority-vote benchmark, the F1–F6 gate results, the verdict token against the
pre-registered bands, Arm R's traces beside the exact curves (reporting-only), and
a byte-identity note (two process runs identical). A clean run reproduces the
drafter's disclosed reference values (G ≈ 8.6513, k\* = 15, e(15) ≈ 0.033227, the
odd k\* table) from scratch, or — the more interesting outcome — DISAGREES and pins
the drafter's error, which the pre-registered rule then rules on honestly (the
theorem-failure NULL axes exist for exactly that).

**Recommendation: sim-ready**
