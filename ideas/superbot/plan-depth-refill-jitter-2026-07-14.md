# "Depth >= the cadence" is only never-dry because the marker forgives lateness: the Q-0164 plan-depth bar under refill-lag jitter

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot, round 12 OPENER; harvest source: superbot's committed autonomous-loop planning constants — the slot's THIRD repo-level superbot tap, disclosed below, on a document and constant family neither prior tap touched)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits superbot files)
> **Grounding:** https://github.com/menno420/superbot@50481b7167e6315dd10f496deec8ac9f0dc03d77 · fetched 2026-07-14T06:15:51Z
> (FIRSTHAND: add_repo + shallow clone this session, first attempt succeeded — no wall; every harvested constant below read from that working tree at HEAD 50481b7; secondary anchor sweep at idea-engine HEAD `369caf2` + the sim-lab local clone READ-ONLY; every MODEL constant below is invented-but-pinned in this file, zero repo/network reads at verdict time — the P017–P060 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains"); round 11 closed fully served (fleet backlogs → P057 #391, venture → P058 #395, game mechanics → P059 #402, COMPLETELY UNRELATED → P060 #404), so round 12 REOPENS at fleet backlogs — this head.

**Third-tap disclosure (repo level, not slot level):** the fleet-backlogs slot has drawn superbot twice before — P021 → V023 (the session-journal shared append point; reject) and P033 → V035 (assign-at-merge queue tax, M/D/1 serialization; null). Both priced the JOURNAL/MERGE append mechanics. This head prices a document and constant family neither touched: the autonomous loop's PLANNING inventory rule (`docs/operations/autonomous-routines.md`) and its cadence guard (`scripts/check_reconciliation_due.py`). Zero shared machinery, argued in Dedup below.

## The committed claims (harvested head, quoted verbatim @ 50481b7)

superbot's self-driving loop refills its plan queue on a COUNT-TRIGGERED cadence and commits an inventory rule for how deep each refill must be:

1. **The cadence:** `scripts/check_reconciliation_due.py:39` — `STEP = 30  # the cadence: a pass per multiple-of-30 PR band (10→20 2026-06-12; 20→30 2026-06-14, Q-0134)`; the due rule at `:132` is `latest // STEP > marker // STEP` — a docs-reconciliation pass fires when merged PRs cross a new multiple-of-30 band since the last marked pass.
2. **The depth bar:** `docs/operations/autonomous-routines.md:199–201` — "The bar is DEPTH >= the cadence — leave enough genuine buildable work to reach the NEXT pass (~30 PRs of capacity)" — restated machine-side in the checker's own issue body (`check_reconciliation_due.py:68`): "plans the next full band (depth >= the cadence, Q-0164)".
3. **The committed incident (the bar's own evidence):** same lines — "The old \"~9 PRs\" horizon drained the queue ~20 PRs before each refill (Q-0164)."
4. **The marker convention:** `autonomous-routines.md:246–247` — after a pass, "Reset the \"Last reconciliation pass: PR #N\" marker … #N is the **latest merged PR** (the reset target), NOT the pass's own PR number."
5. **The lateness environment:** the pass does not land at the band crossing — it is issue-triggered and lands later; the repo's own measurements: "at burst velocity a 20-band crossed in under a day and fired the docs pass several times daily" (`check_reconciliation_due.py:12–14`) and GitHub-schedule-class delays "frequently **hours late or occasionally dropped**", observed "~4¾ h late" (`autonomous-routines.md:387–390`).
6. **The dry state is committed as a SIGNAL:** `autonomous-routines.md:209–211` — a pass that "STILL can't fill the band … that is the SIGNAL, not a failure (Q-0164): set a loud `⚠️ PLAN BACKLOG THIN` line" for the owner.

"DEPTH >= the cadence" is a periodic-review order-up-to (base-stock) inventory rule, adopted from one incident, never measured. Whether depth 30 against cadence 30 actually delivers never-dry — and WHAT property of the system its safety really rides on — is exactly computable.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Model the loop in merged-PR time. The pass lands ℓ PRs after its band crossing (the lag), the marker is reset to the LANDING count t₀, and the next trigger fires at the first multiple of K = 30 strictly above t₀, so the next landing comes at t₁ = 30·(⌊t₀/30⌋ + 1) + ℓ′. Since t₀ mod 30 = ℓ (for ℓ < 30), the refill-to-refill window is exactly

**W = 30 − ℓ_prev + ℓ_cur.**

Three exact consequences, none stated anywhere in the harvested docs:

- **The forgiveness theorem (the marker convention's unmeasured virtue):** under ANY constant lateness ℓ, W ≡ 30, consumption in a window is at most W = 30 ≤ S = 30, and the queue CANNOT run dry — resetting the marker to the latest merged PR (not the crossing) makes every window borrow back exactly the lateness of the previous landing. "Depth = cadence" is exactly right, at zero safety stock, no matter HOW late every pass is — provided it is always equally late.
- **The jitter tax:** dryness at S = 30 is possible ONLY when lateness grows between consecutive passes (W = 30 + ℓ_cur − ℓ_prev > 30). At q = 1 (every merged PR consumes a plan slice) this is an identity: P(dry) = P(ℓ_cur > ℓ_prev), independent of the lag distribution's shape — the committed bar's failure probability IS the probability that the pass landed later than last time.
- **Mean-cadence conservation:** E[W] = 30 exactly for every lag distribution — the convention conserves the average cadence perfectly; only the VARIANCE of lateness is ever dangerous.

So the committed bar's guarantee silently rides on lag regularity that nothing in the loop measures — while the realized lag ledger already exists for free: the marker residue N mod 30, committed in every pass record, IS the landing lateness. And the queue-dry state is not harmless: it is the state where dispatch fires with nothing planned and the ⚠️ PLAN BACKLOG THIN escalation fires at the owner — if geometry alone can produce it at a measurable rate, the THIN signal carries geometry-born false positives ("we're out of ideas" when the truth is "the pass was later than last time").

## Pinned model (committed constants harvested @ 50481b7; model constants invented-but-pinned, exact rationals)

- **Cadence** K = 30 (committed: `STEP = 30`). Trigger arithmetic implemented VERBATIM: due iff `latest // 30 > marker // 30`; marker := landing count (committed reset convention). K is held fixed — retuning K is the checker's own "retune there" note, out of scope.
- **Refill:** at each pass landing the plan queue is set to depth S (order-up-to; the committed bar plans "the next full band"). Decision cell S = 30 (the committed bar); published grid S ∈ {9, 20, 30, 33, 36, 39, 45} (9 = the old committed horizon, 20 = the pre-Q-0134 cadence, the rest bracket the safe-depth scan); exact safe depth S\*(q, mix) = min{S : p_dry(S) ≤ 1/100} computed by scan.
- **Consumption:** each merged PR consumes one plan slice with probability q, i.i.d. (dispatch slices consume; the docs pass itself, dependabot merges, bug fixes, self-initiated work do not). Grid q ∈ {3/5, 3/4, 9/10, 1}, decision cell q = 9/10 — calibrated against the committed incident: at the old horizon S = 9 and q = 9/10 the model's expected drained span is ≈ 20.0 PRs, dead on the committed "drained the queue ~20 PRs before each refill" (F4 gates it; q = 1 gives exactly 21, also in-band).
- **Lag (invented-pinned-disclosed):** lateness in merged-PR units between band crossing and pass landing. Decision mix L0 = {0: 3/10, 1: 3/10, 3: 1/5, 6: 1/10, 12: 1/10} — scaled from the repo's own measurements: the dispatch cadence `0 */2 * * *` and the "20-band crossed in under a day" burst put burst velocity at ~12–20+ merged PRs/day, so a healthy issue-triggered landing (fires "in under a minute", #776) is 0–1 PRs late, the measured "~4¾ h late" scheduler class is ~3–6, and a full-day stall is ~12. Sensitivity mixes (reporting-only): PROMPT = {0: 1/2, 1: 1/2}, HEAVY = {0: 1/4, 1: 1/4, 3: 1/4, 12: 1/8, 24: 1/8}. All lag support < 30 (single-band regime; the ROUTINE_PAT-lapse silent-stall class — "the issues silently revert to bot-authored", `autonomous-routines.md:59–62` — is a ≥ 1-band outage, a DIFFERENT failure mode, named follow-up, excluded by construction).
- **Steady state:** lags i.i.d. across passes; window W = 30 − ℓ_prev + ℓ_cur exact (derived above, F1 re-derives it by direct event-walk of the verbatim trigger arithmetic). Windows are 1-dependent through shared endpoints; per-cycle quantities are exact expectations over the independent lag pair, and long-run PR-fractions follow by renewal-reward with E[W] = 30 exactly (gated).
- **Metrics (all exact `fractions.Fraction`):** per-cycle dry probability p_dry(S, q, mix) = Σ_pairs P(pair) · P(Bin(W, q) ≥ S + 1); expected drained span E[max(0, W − T_S)] (T_S = arrival index of the S-th consuming PR — the "drained N PRs before refill" length the incident line reports); expected dry-PR span fraction = E[drained span]/30; dry consuming-arrivals E[max(0, Bin(W, q) − S)].
- **Arm A (the DECISION arm, seedless):** exact Fraction closed forms — binomial tails + negative-binomial span sums over the lag-pair lattice; byte-identical across process runs.
- **Arm B (twin, seedless):** an INDEPENDENTLY-WRITTEN queue-level DP event-walk — for each (pair, S, q) cell, step PR-by-PR through the window carrying the exact queue-level distribution; must reproduce every Arm-A number EXACTLY.
- **Arm R (seeded, REPORTING-ONLY):** mechanism-trace MC of the LITERAL counter/marker/trigger system at the decision cell — N = 100,000 cycles via `random.Random(20261381)` (pinned draw order per cycle: one uniform inverted through the pinned lag cdf, then W Bernoulli uniforms in PR order; draw counts counted and asserted); stability leg `random.Random(20261382)` at N = 20,000; presentation shuffle 20261383 (published-table row order only). NO statistical gate rides Arm R — a trace estimate drifting from the exact value is a named finding, never a ruling; its only gates are the draw-count sentinel and byte reproducibility.
- **Aux seed:** 20261384, reserved, NEVER read by any leg (the P054–P060 aux convention).
- Seeds 20261381–384 strictly above P060's 20261380 high-water; boundary-aware re-sweep this session — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD 369caf2 (bootstrap.py/.substrate excluded) and the sim-lab local clone READ-ONLY — maxes at genuine 20261380; the larger standalone numerals 20261542/20261833 (Fraction-numerator digit substrings) and the 9-digit 202670087 (a decimal-fraction digit substring in results.json-quoting text) are data, not seeds — the P046–P060 sweep-recipe trap re-confirmed.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the committed DEPTH >= cadence bar is not a never-dry rule — it is a never-dry-IF-LATENESS-IS-STEADY rule; under the pinned lateness jitter the committed depth 30 goes dry in a sizable share of cycles, the honest safe depth is cadence + lateness headroom, and the ⚠️ PLAN BACKLOG THIN escalation inherits a geometry-born false-positive rate": at the decision cell (S = 30, q = 9/10, L0), p_dry ≥ 1/20 exact, AND S\*(9/10, L0) ≥ 33, AND the expected dry-PR span fraction ≥ 1/50 exact. (Checked FIRST because the costly direction is fleet-wide: "depth = cadence" is the portable heuristic every seat inherits — this repo's own ORDER 003 "pipeline never dry" duty included — and adopting it without the lag-regularity condition ships a silent dry-rate into every count-triggered refill loop.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the committed bar holds as stated at the pinned lateness": p_dry(S = 30) ≤ 1/100 at the decision cell AND S\*(9/10, L0) ≤ 30 AND dry-span fraction ≤ 1/100. (Mutually exclusive with REJECT by arithmetic on every clause.)
- **NULL** — anything else; pre-registered axes: **band-straddle** (p_dry ∈ (1/100, 1/20), or S\* ∈ {31, 32}, or dry-span fraction ∈ (1/100, 1/50) — the finding is the exact p_dry(S) curve with the safe-depth scan); **prompt-cell-inversion** (the PROMPT reporting mix lands p_dry(30) ≥ 1/20 — the fragility would NOT be jitter-magnitude-born and the drafter's mechanism story is wrong; the finding is the corrected attribution); **forgiveness-theorem failure without gate failure** (a constant-lag cell shows p_dry(30) > 0 while F1–F6 pass — the drafter's window algebra is wrong, and the finding is the corrected law); **twin-arm disagreement** surviving the INVALID diagnosis.

## Gates (run INVALID on any failure)

- **F1 — model & mechanism identities:** all three lag pmfs sum to 1 exactly; binomial rows sum to 1; the window closed form W = 30 − ℓ_prev + ℓ_cur reproduced EXACTLY by a direct event-walk of the verbatim committed trigger arithmetic (`latest // 30 > marker // 30`, marker := landing count) over every lag pair; mean-window conservation Σ P(pair)·W = 30 exactly on all three mixes.
- **F2 — the forgiveness theorem:** p_dry(S = 30) = 0 EXACTLY under every constant lag c ∈ {0, 1, 3, 6, 12} at every grid q (hand proof pinned above: W ≡ 30 and Bin(30, q) ≤ 30 ≤ S surely).
- **F3 — the q = 1 identity:** p_dry(30, q = 1, mix) = P(ℓ_cur > ℓ_prev) exactly on all three mixes — reference values L0: 19/50, PROMPT: 1/4, HEAVY: 25/64 (distribution-free: dry at q = 1 iff the window exceeds 30 iff lateness grew).
- **F4 — the committed-incident anchor:** at the OLD committed horizon S = 9, constant lag (W = 30): E[drained span] ∈ [18, 22] at q = 9/10 AND = 21 exactly at q = 1 (the harvested "drained the queue ~20 PRs before each refill" reproduced by the model at the old committed depth; drafting value ≈ 20.0000 at the decision q).
- **F5 — hand world:** K = 4, S = 2, q = 1/2, lag uniform on {0, 1}: windows {3, 4, 5} w.p. {1/4, 1/2, 1/4}, tails {1/8, 5/16, 1/2}, p_dry = 5/16 by hand.
- **F6 — battery:** Arm B reproduces every Arm-A value exactly on every published cell; twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinels counted and asserted; aux seed 20261384 never read; stdout + results.json byte-identical across two process runs (Arms A/B platform-independent exact rationals; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P060 closed-form-arm norm)

REJECT on all three conjuncts, at the drafter's exact prototype values (the sim re-derives everything from scratch and must not trust these): decision-cell p_dry(30, 9/10, L0) = 1101510756549069125820660830403305561487141/6250000000000000000000000000000000000000000 ≈ 0.176242 (≥ 1/20 by 3.52×); the safe-depth scan p_dry(38) ≈ 0.018095 > 1/100 > p_dry(39) ≈ 0.008070 so S\* = 39 = cadence + 9 (≥ 33 with margin 6); dry-span fraction ≈ 0.027816 ≥ 1/50 (margin 1.39× — the thinnest clause, disclosed). Falsifiability is real on every clause: under the PROMPT mix the committed bar HOLDS — p_dry(30) ≈ 0.009538 < 1/100 and S\*(PROMPT) = 30 exactly, so the committed rule is exactly right when passes land promptly (one lag-regime step moves the ruling; the decision genuinely rides on the pinned mix, which is why it is disclosed as invented and why branch (a) below names the free measured replacement); the dry-span clause sits only 1.39× over its line; and the q = 3/5 column lands p_dry(30) ≈ 0.00237 APPROVE-side (a docs-heavy PR mix dissolves the fragility — the consumption calibration matters and is anchored by F4). Disclosed sharpenings, reporting-only: the OLD committed world S = 9 goes dry in ≈ 99.99993% of cycles with expected drained span ≈ 20.0 (the model retrodicts the committed incident almost exactly); the pre-Q-0134 depth row S = 20 still dries in ≈ 90.9% of cycles; HEAVY-mix S\* = 50; per-cycle dry consuming-arrivals at the decision cell ≈ 0.751 (the average dry cycle strands most of one plan slice's worth of dispatch fires); E[W] = 30 exactly on every mix (the conservation pin).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no superbot file, nothing here builds/publishes/spends)

APPLICATION GUARD, two conditions: (1) the verdict conditions on the committed constants @ 50481b7 — `STEP = 30`, the depth bar "~30 PRs of capacity", the marker-reset-to-latest convention; a retuned STEP, a changed reset convention, or a stock-triggered (rather than count-triggered) refill means re-run, not reuse; (2) it conditions on the single-band lag regime (lateness < 30 PRs) — the ROUTINE_PAT-lapse full-stall class is out of scope by construction. REJECT → paste-ready structured choice for the manager to route, recommendation first per Q-0263.2 — **(a, recommended: zero code, one doc line + one free measurement)** the Q-0164 bar gains its lag-inclusive companion ("depth >= cadence + pass-lateness headroom"; at the pinned jitter the measured 1%-safe depth is 39 ≈ cadence + max lateness) AND the free probe is named: the marker residue N mod 30, already committed in every pass record in `docs/current-state.md` history, IS the realized lateness ledger — one file read replaces the invented lag mix with measured lags before anyone re-tunes anything; **(b)** keep depth = 30 as-is, now explicitly accepting the measured per-cycle dry rate under jittery landings (≈ 0.18 at the pinned mix) and that the ⚠️ PLAN BACKLOG THIN escalation carries geometry-born false positives at that rate — with the forgiveness theorem's doc line still worth shipping (see below); **(c)** make the refill lateness-aware (plan depth = 30 + last observed residue, or fire the reconcile issue early by the last lag) — an owner/lane intent call, never ruled by fiat. On EVERY branch the marker convention itself comes out vindicated-with-numbers: resetting to the latest merged PR (not the crossing) cancels steady lateness EXACTLY and conserves mean cadence EXACTLY — an unstated virtue worth its one line in the ops doc, so nobody "fixes" it into a crossing-reset that would break the forgiveness. APPROVE → the committed bar gains a measured basis at the pinned lateness and the safe-depth table ships anyway. NULL → the named axis ships with the exact p_dry(S) curve and safe-depth scan. Transfer surface, named: every count-or-cadence-triggered refill loop in the fleet (this repo's own ORDER 003 never-dry pipeline duty with its WIP-3 cap, the manager's wake-chain work queues, venture's kill-clock checkpoints) inherits the same law — order-up-to-cadence is safe against steady lateness and unsafe against growing lateness, and the fix is headroom or measurement, not a faster scheduler. Follow-ups named, none in scope: the ≥ 1-band stall class (PAT expiry — a detection problem, kin to P053's blind window, not an inventory problem); stock-triggered refill (the P019/V021 policy class) as an alternative mechanism; correlated/bursty consumption.

## Dedup

Tree-wide `rg -i 'reorder|base.stock|order.up.to|periodic review|refill|reconciliation band|plan queue|low.water|depth.*cadence'` (bootstrap.py/.substrate excluded) at HEAD 369caf2, plus the ledger read: **no proposal P001–P060 and no verdict V001–V071** (V069 finalized REJECT on P058's rubric world; V070/V071 in flight on P059/P060's prestige/reciprocity worlds — zero overlap with inventory or cadence) prices an order-up-to depth rule, a count-triggered refill cadence, refill-lag jitter, or any depth-vs-cadence law. Nearest priors argued distinct: **P019 → V021** (the nearest neighbor — websites' backlog "~3" low-water bullet; verdict N\* = 1): a CONTINUOUS-review REORDER-POINT SIGNAL question — when to raise a flag as stock falls, with replenishment routed on demand; this head is the OTHER classical inventory family (PERIODIC review, order-up-to depth, refill forced by a count cadence regardless of stock), whose failure mode — refill-lag jitter against a marker convention — has no analog in P019's world (zero shared fixtures, different repo, different committed constants, different consumer); **P012 → V014** (routine-cadence economics): wake scheduling for trigger CATCHING where nothing is ever lost and the price is latency — here the priced event is a genuine degraded state (dispatch fires unplanned, the owner gets escalated) and the refill is count-triggered; **P033 → V035** (the same repo's assign-at-merge M/D/1 queue tax): serialization LATENCY of a build mechanism, zero inventory content — the disclosed third-tap sibling; **P037 → V048** (fleet-manager review-queue row threshold): a CLASSIFICATION threshold (which PRs enter a queue), not a depth/cadence law; **P053 → V064** (probe-cadence blind window): DETECTION probability of external transients — method kin at most (both price a committed cadence constant; nothing else shared); **P056 → V067** (inspection paradox): length-biased SAMPLING of intervals — this head's windows are never size-biased-sampled, the lag algebra is a different object. Method kin only: the P017–P060 exact-arm + pre-registered-bands discipline (nearest: P057's exact binomial-tail machinery, reused on a different object — refill windows, not grading windows). Same-subsystem CAPTURED link-index rows checked by name, neither a conflict: `ideas/superbot/planned-slice-hit-rate-tracker-2026-07-10.md` (captured — an accountability TRACKER for the reconciliation queue, no depth/cadence law, no sim question) and `ideas/superbot/product-lanes-gated-balance-flag-2026-07-10.md` (captured — a companion FLAG to PLAN-BACKLOG-THIN, prose only); this head supplies the measured law both would merely report. sim-lab sweep (read-only, same regex): sims through V068 committed touch none of this; the karma/queue prose hits are fixture text.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) **the lag mix is INVENTED** (scaled from the repo's own burst/lateness measurements but not fitted to logged data — the pass-landing lag ledger exists yet is unread at drafting); direction two-sided and DISCLOSED as the decision's hinge: prompt landings hold the committed bar (APPROVE-side), heavier jitter worsens it — which is exactly why branch (a) names the free measured replacement (marker residues) before any re-tune. (2) **i.i.d. Bernoulli consumption** at q = 9/10, calibrated to the committed incident (F4); real dispatch slices arrive in runs — positive correlation fattens the consumption tail, the REJECT direction, stated never simulated; the q grid brackets the mix. (3) **merged-PR time** — PR NUMBERS share their sequence with issues, so number-gaps make real bands cross in fewer merged PRs (shorter windows: the APPROVE direction for dryness, the REJECT direction for pass frequency; the checker's own "PR-number gaps" caveat, carried as a stated boundary). (4) **dry = the committed degraded state, not an outage** — Q-0172 lets dispatch self-promote ideas when the queue is empty; the head prices how often that fallback and the ⚠️ THIN escalation fire from cadence GEOMETRY alone, which is precisely what makes the false-positive reading actionable. The forgiveness theorem (F2) and the q = 1 identity (F3) are robust to (1)–(3) — they are convention facts, not mix facts.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained fleet-ops knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **harvest verified FIRSTHAND** — superbot
> cloned shallow at HEAD `50481b7` this session (Q-0272 standing public-read authorization,
> re-read at superbot docs/fleet-reading-path.md @ 50481b7); every quoted constant
> re-read from the working tree (`STEP = 30` at check_reconciliation_due.py:39, the due
> rule at :132, the depth bar + incident at autonomous-routines.md:199–201, the marker
> convention at :246–247, the THIN signal at :209–211). (b) **dedup** — the tree-wide
> inventory/cadence sweep at grounding pin `369caf2` returned no domain hit (see Dedup;
> P019's reorder-point world argued distinct by policy family); sim-lab (read-only)
> returned fixture prose only. (c) **kill test NOT triggered** — no prior proposal, idea
> file, or session-card 💡 prices depth-vs-cadence, refill lag, or the marker convention.
> (d) **feasibility + liveness arithmetic checked** — runtime bounded (Arms A/B are
> exact binomial/DP sums over a ≤ 25-pair lag lattice × small grids, sub-second; Arm R
> is 100k short cycles, seconds, stdlib only); expected landing DISCLOSED with its exact
> drafting values (REJECT, p_dry ≈ 0.176 at the decision cell) rather than hidden, all
> rulings reachable under the pre-registered rule, the straddle/prompt-inversion NULL
> axes and the INVALID controls gate all named.

**1. What is this really?** A pre-registered exact MEASUREMENT of a committed fleet-ops
inventory rule, taken where it lives: superbot's autonomous loop refills its plan queue
to depth ~30 whenever merged PRs cross a 30-band ("DEPTH >= the cadence", Q-0164), with
the refill landing LATE by a jittery number of PRs and the cadence marker reset to the
landing point. The head computes, in exact `fractions.Fraction` arithmetic over a pinned
lag-pair lattice, the per-cycle dry probability of the committed depth, the exact safe
depth S\*, the drained-span law that retrodicts the committed "~9 drained ~20 early"
incident, and two convention theorems (constant lateness is EXACTLY forgiven by the
marker rule; at q = 1 the dry probability IS P(lateness grew)), judged against bands
fixed before any code (REJECT first), byte-identical across two runs, with a seeded
mechanism-trace arm demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-12 opener goes
unserved and the slot's committed-constant harvest lane skips the fleet's most
load-bearing autonomous loop. (ii) Re-audit a prior slot source (websites/kit/
fleet-manager/curious-research/mineverse/trading-strategy all drawn; superbot's two
prior draws priced journal/merge mechanics — this is a NEW document + constant family,
disclosed third repo tap). (iii) A prose note ("add safety stock") — states the
direction, measures nothing, and misses both exact theorems (forgiveness;
the q = 1 identity) that make the finding actionable rather than generic. (iv) An
MC-only trace — leaves every decision number seed-noisy when the whole lattice is
exactly summable; the decision arms are exact and MC is demoted to reporting (the
V065/V067 lesson). (v) This head: exact per-cycle dry law + safe-depth scan +
convention theorems, REJECT-first bands, INVALID on the F1–F6 identity/theorem/
anchor/hand-world/twin gates, the lag-mix dependence disclosed with its measured
replacement named. (vi) Over-scope (the PAT-lapse full-stall class, stock-triggered
refill, correlated consumption, retuning STEP) — each named as a follow-up or boundary,
none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~150-line stdlib file: an exact binomial-tail/negative-binomial kernel over the
lag-pair lattice (Arm A), an independently-written queue-level DP event-walk (Arm B),
and a literal trigger-arithmetic walker (F1) — yielding the full p_dry(S) surface over
{9, 20, 30, 33, 36, 39, 45} × {3/5, 3/4, 9/10, 1} × three mixes, the exact safe-depth
scan, the drained-span retrodiction of the committed incident, both convention
theorems verified as THEOREM CHECKS rather than estimates, and the dry-arrivals
column — all from a sim a verdict session runs cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **The lag mix is invented** —
pinned, disclosed, two-sided (PROMPT holds the bar, HEAVY breaks it worse), and the
decision's dependence on it is itself the finding's shape: the committed rule is
regime-safe, not depth-safe; branch (a) replaces the mix with the free marker-residue
ledger before any action. (b) **Consumption independence** — dispatch slices run in
bursts; correlation fattens the tail REJECT-ward (stated, never simulated); the q grid
plus the F4 incident calibration bracket it. (c) **PR-number vs merged-count drift** —
number gaps shorten real windows (APPROVE-ward for dryness), stated boundary from the
checker's own caveat. (d) **Band placement could cherry-pick** — the 1/20, 1/100, 1/50,
and S\* ≥ 33 constants are committed BEFORE the sim, the landing is DISCLOSED (REJECT),
and falsifiability is two-sided: the dry-span clause clears its line by only 1.39×, the
PROMPT cell lands APPROVE-side, and q = 3/5 lands APPROVE-side — the bands can see the
regime flip. (e) **An algebra slip in the drafter's window derivation** — the sim
re-derives W by walking the verbatim committed trigger arithmetic (F1), the forgiveness
theorem is gated (F2) and separately carries its own NULL axis, so a wrong hand proof
becomes a finalized corrected-law finding, not a silent bad gate.

**5. What does it unlock?** A measured, citable answer to whether the fleet's most
copied planning heuristic ("depth = cadence") actually delivers never-dry, with three
standalone side pins (the marker-forgiveness theorem — steady lateness costs NOTHING
under the committed reset convention, an unstated virtue now provable; the q = 1
identity — the bar's failure probability equals P(lateness grew), distribution-free;
the exact retrodiction of the committed Q-0164 incident from first principles); the
safe-depth table any count-triggered refill loop in the fleet can consume (this repo's
ORDER 003 never-dry duty, manager wake-chains, venture kill-clocks); and a
false-positive rate for the ⚠️ PLAN BACKLOG THIN owner escalation, separating "out of
ideas" from "the pass was late twice differently".

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: Arms A/B settle every decision number exactly in sub-second time
with no seed. The single cheapest probe if a reader doubts the kernel is the q = 1
identity by hand (dry ⟺ window > 30 ⟺ ℓ_cur > ℓ_prev; count the lag pairs — 19/50
under L0), which anchors the window algebra and the dry event in three lines of
pencil arithmetic.

**7. What would make this a mistake to run?** If the exact solve were unavailable (it
is not — binomial tails over a 25-pair lattice), if the head duplicated a prior verdict
(it does not — the sweep's nearest hit is P019's reorder-point SIGNAL world, a
different inventory family argued distinct by policy class, trigger, metric, and
consumer), or if the disclosed REJECT made the run theater. It does not: the PROMPT
cell and the q = 3/5 column both land APPROVE-side so the ruling was arithmetically
open until the lattice existed, the dry-span clause sits 1.39× over its line, and the
run's value is the independent hermetic re-derivation PLUS the parts no hand argument
gives — the exact safe-depth scan (39 = cadence + max lateness at the pinned mix), the
incident retrodiction, and the theorem checks.

**8. How will we know it worked?** A committed sim-lab report with: the full exact
p_dry(S, q, mix) surface (Fractions + float renderings), the safe-depth scan with its
1/100 bracket (p_dry(38)/p_dry(39) both published), the drained-span table with the
S = 9 incident row, the constant-lag zero table (F2), the q = 1 identity values
(19/50, 1/4, 25/64), the F1–F6 gate results, the verdict token against the
pre-registered bands, Arm R's trace estimates beside the exact values
(reporting-only), and a byte-identity note (two process runs identical). A clean run
reproduces the drafter's disclosed values (p_dry(30) ≈ 0.176242, S\* = 39, span
fraction ≈ 0.027816) from scratch, or — the more interesting outcome — DISAGREES and
pins the drafter's error, which the pre-registered rule then rules on honestly (the
forgiveness-theorem NULL axis exists for exactly that).

**Recommendation: sim-ready**
