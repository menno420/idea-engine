# The never-dry pipeline is a limit, not a rule: WIP cap 3 prices the committed never-dry floor at a fifth of the clock — and the tax is variance-born

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot, round 14 OPENER; harvest source: THIS SEAT'S OWN COMMITTED BUS — the owner's ORDER 004 "WIP cap 3, backpressure holds" rule and ORDER 003's "the PROPOSAL→VERDICT pipeline is never dry" floor in `control/inbox.md`, priced against the seat's own committed append cadence in `control/outbox.md` + both dated archives, with TWO lived DRY events already on the committed record)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits any other repo)
> **Grounding:** https://github.com/menno420/idea-engine@dc155cb214b033893d8a1e07bc4eccb069989443 · fetched 2026-07-15T07:23:08Z
> (FIRSTHAND: every harvested sentence and every measured timestamp below is read from THIS repo's committed files at HEAD dc155cb and cited file@sha; every MODEL constant is invented-but-pinned in this file, and the DECISION arms are seedless exact rationals with zero repo/network reads at verdict time — the P017–P068 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains"); round 13 closed fully served (fleet backlogs → P065 #428, venture → P066 #429, game mechanics → P067 #430, unrelated → P068 #431, merged 2026-07-15T06:49:09Z), so round 14 REOPENS at fleet backlogs — this head. Slot spacing history P057, P061, P065 → P069 (spacing 4) confirms the placement.

**Placement note (decide-and-flag):** a fleet-doctrine head about this seat's own pipeline lives in `ideas/fleet/` by the section's own charter (cross-cutting workflow/process ideas) — no carve-out needed, unlike the fleet-external rotation heads that squat here flagged.

**Harvest-tap disclosure (slot history):** the fleet-backlogs slot has drawn websites (P019, P053), fleet-manager (P037, P065 — P065's convention was fm-owned though its byte constants were measured on this repo's bus), curious-research (P041, P049), superbot-mineverse (P045), trading-strategy (P057), and superbot (P061). This head is the slot's FIRST tap of the seat's own committed ORDER text and append cadence as the harvested constants. Kinship with P065 disclosed and bounded: P065 measured stub/block BYTE SIZES to price the rollover convention's growth law; this head measures block header TIMESTAMPS and the inbox cap/floor sentences to price a queueing pair — different files-of-fact, different mechanism, zero shared fixtures.

## The committed claims (harvested verbatim @ dc155cb)

The owner committed BOTH horns of an unpriced tension into this seat's standing orders, and the committed record already contains the collision:

1. **The cap:** `control/inbox.md:50` @ dc155cb (ORDER 004, owner verbatim) — "Keep the cycle spinning continuously: harvest → probe → verdict → outbox; **WIP cap 3, backpressure holds**." Restated in the same order's done-when (`:54`): "cycle continuous with WIP cap 3".
2. **The floor:** `control/inbox.md:31` @ dc155cb (ORDER 003 done-when) — "standing — **the PROPOSAL→VERDICT pipeline is never dry**: at all times ≥1 new PROPOSAL drafted-or-in-flight in idea-engine's outbox".
3. **Lived dry event #1:** `control/inbox.md:188` @ dc155cb (ORDER 012, 2026-07-14) — "the pipeline is momentarily **DRY** (P062 verdicted as sim-lab VERDICT 073, merged 09:10:49Z; **no unverdicted proposal exists**)".
4. **Lived dry event #2:** `control/inbox.md:219` @ dc155cb (ORDER 014, 2026-07-14) — "**pipeline DRY at P063 → V074** (sim-lab#140 @ 9aaf72b)".
5. **The measured cadence (drafting side):** the `## PROPOSAL 0NN · <ISO8601>` block headers across `control/outbox.md` + `control/outbox-archive-2026-07-14.md` + `control/outbox-archive-2026-07-15.md` @ dc155cb — 68 committed appends P001–P068. The round-13 burst gaps, verbatim seconds: P064→P065 = 1622, P065→P066 = 2674, P066→P067 = 2263, P067→P068 = 1387 (mean **S_d = 3973/2 s ≈ 33.1 min**). The 2026-07-13 night burst P016→P034: 30847 s over 18 gaps (mean 30847/18 ≈ 28.6 min). Lifetime P001→P068: 391243 s over 67 gaps (mean ≈ 97.3 min — the day-pause regime).
6. **The measured cadence (verdict side):** `control/outbox.md:15` @ dc155cb (the ROLLOVER 002 pointer) — "VERDICT 078 (**finalized 2026-07-15T05:37:45Z**, on this repo's P065)"; P065 was appended 05:00:19Z (its own block header), so the one committed append→finalization pair on the bus is **S_v = 2246 s ≈ 37.4 min**.

Both dry events were reported upward as pipeline anomalies requiring same-day drafting ("author PROPOSAL 063 — the pipeline is momentarily DRY … and standing ORDER 003 requires ≥1 PROPOSAL at all times"). Nobody has priced whether a WIP-capped loop can satisfy a never-dry floor AT ALL — and it cannot, exactly, and by how much it misses is computable from the seat's own committed cadence.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Model the seat's pipeline as what the two orders literally describe: a CLOSED two-station cyclic loop (CONWIP). K tokens — the WIP cap — circulate between station 1 (drafting, this repo) and station 2 (verdicting, sim-lab). The state is n = the number of unverdicted proposals in flight, n ∈ {0..K}: a drafting completion is a birth (rate λ) permitted only while n < K ("backpressure holds" — at n = K the drafter is blocked/harvest-diverted), a verdict finalization is a death (rate μ) while n > 0. DRY is the committed record's own definition (claim 3: "no unverdicted proposal exists") — the state n = 0, where the verdict consumer starves. With memoryless service the stationary law is a truncated geometric: π(j) ∝ r^j with **r = λ/μ = S_v/S_d**, and every quantity below is an exact rational in (K, r). Three structure theorems carry the head, each an exact gate, none stated anywhere in the committed orders:

- **T1 — the impossibility (never-dry is not a policy option):** D(K, r) = π(0) = 1/Σ_{j=0}^{K} r^j **> 0 strictly, for every finite K and every r ∈ (0, ∞)**. A WIP cap and a never-dry floor committed on the same buffer are jointly unsatisfiable as a stationary guarantee — the dry state always carries positive mass. The two lived DRY events are not anomalies; they are the cap's own arithmetic firing on schedule.
- **T2 — the monotone frontier (what a cap raise can and cannot buy):** D is strictly decreasing in K and in r, and the K→∞ frontier is **lim D = max(0, 1 − r)** exactly. So dryness can be paid down but never off — and on the r < 1 side (drafting slower than verdicting) NO cap raise reaches below 1 − r: the binding constraint is drafting speed, not WIP. The floor is purchasable only in the joint limit K→∞ AND r > 1 — i.e., "never dry" names a LIMIT, not a rule.
- **T3 — the balanced knee (what the committed cap costs at parity):** at r = 1 the law is uniform — D(K, 1) = B(K, 1) = 1/(K + 1) exactly (B = π(K), the blocked-drafter/backpressure-engaged fraction), and throughput is exactly K/(K + 1) of the bottleneck. At the committed **K = 3**: dry a quarter of the clock, blocked a quarter of the clock, running at exactly 3/4 of capacity; the marginal cap lift buys ΔD(3→4) = 1/20 exactly.

And one exact exhibit that relocates the blame: the dryness is **VARIANCE-born, not cap-born**. Under DETERMINISTIC service at the same means, the closed loop's station-2 idle fraction has the exact closed form D_det(K, r) = max(0, 1 − K·r/(1 + r)) — at the committed cell (K = 3, r = r̂ below) this is **0 exactly** (K ≥ 2 already suffices): a clockwork cadence satisfies the committed pair perfectly, while memoryless dispersion at the SAME means misses the floor by ~20.6%. The committed record's own dispersion (burst gaps 1387–2674 s; night mean 1714 s; lifetime mean 5839 s) says the real cadence is at least exponential-grade dispersed across regimes — the folk pair fails exactly where the seat actually lives.

Measured anchor, exact: **r̂ = S_v/S_d = 2246/(3973/2) = 4492/3973 ≈ 1.1306** (drafting slightly faster than verdicting at burst cadence). Second anchor from the night burst: r₂ = 2246/(30847/18) = 40428/30847 ≈ 1.3106. Reporting anchor from the lifetime cadence: r_life = 150482/391243 ≈ 0.3846 (the day-pause regime — where D(3, r_life) ≈ 0.63, and where both lived DRY events in fact occurred).

## Pinned model (measured constants harvested @ dc155cb; model constants invented-but-pinned, exact rationals)

- **The loop:** closed cyclic 2-station single-server network, population K; state n = unverdicted in-flight ∈ {0..K}; births at rate λ iff n < K, deaths at rate μ iff n > 0; r = λ/μ. Stationary law π(j) = r^j / Σ_{i=0}^{K} r^i (uniform at r = 1). Exponential service is the pinned decision model (declared, directional — see Model basis); the deterministic-service closed form D_det(K, r) = max(0, 1 − K·r/(1 + r)) is a pinned EXACT exhibit, reporting-only.
- **Grids:** K ∈ {1, 2, 3, 4, 6, 12}, decision cell **K = 3** (the committed cap, claim 1); r ∈ {1/2, 3/4, 1, r̂ = 4492/3973, r₂ = 40428/30847, 2}, decision cell **r̂** (the burst anchor — deliberately the dryness-MINIMIZING regime choice: continuous night-run drafting; the lifetime anchor r_life = 150482/391243 is a reporting cell, disclosed, where dryness is far worse). Cadence extraction rule pinned: ISO timestamps from the `## PROPOSAL 0NN ·` headers (claims 5–6), gaps in integer seconds, means as exact Fractions — S_d = 3973/2 s (burst gaps 1622, 2674, 2263, 1387), S_v = 2246 s (the one committed pair, P065 05:00:19Z → V078 05:37:45Z).
- **Metrics, all exact `fractions.Fraction`:** DRY fraction D(K, r) = π(0); backpressure fraction B(K, r) = π(K); throughput TH(K, r) = μ(1 − π(0)) with the flow identity λ(1 − π(K)) = μ(1 − π(0)); efficiency E(K, r) = TH/min(λ, μ); mean cycle time via Little W(K, r) = K/TH (reporting); the safe-cap scan K\*(r, d) = min{K : D(K, r) ≤ d} for d ∈ {1/10, 1/20, 1/100} (reporting — the consequence menu's table).
- **Arm A (the DECISION arm, seedless):** the truncated-geometric closed forms, exact Fractions at every grid cell; byte-identical across process runs.
- **Arm B (twin, seedless):** an INDEPENDENTLY-WRITTEN exact stationary solve — build the (K+1)-state generator Q and solve πQ = 0, Σπ = 1 by Fraction Gaussian elimination; must reproduce every Arm-A number EXACTLY. (Both arms were run at drafting and agreed on every rational — the disclosed landing below is a measured reproduction target, not a hand estimate.)
- **Arm R (seeded, REPORTING-ONLY):** discrete-event traces of the literal loop at the decision cell under three service-time shapes at the same pinned means — exponential, deterministic (beside its exact closed form), and the measured two-point empirical mix (the four burst gaps resampled uniformly; S_v degenerate at 2246) — N = 100,000 cycles via `random.Random(20261610)` (pinned draw order: station-1 draw then station-2 draw per event epoch; draw counts counted and asserted); stability leg `random.Random(20261611)` at N = 20,000; presentation shuffle 20261612 (published-table row order only). NO statistical gate rides Arm R — a trace drifting from the exact value is a named finding, never a ruling.
- **Aux seed:** 20261613, reserved, NEVER read by any leg (the P054–P068 aux convention).
- Seeds 20261610–613 allocated from 20261610 per the coordinator relay: 20261600–603 are P068/V081's registered set and the gap 20261604–609 is the disclosed in-flight buffer, so 20261610 is the next free index — strictly above both. Boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD dc155cb (bootstrap.py/.substrate excluded) confirms the standalone numerals 20261664 / 20261833 / 202670087 are digit-substrings (Fraction numerators, results-JSON decimals), data not seeds — the P046–P068 sweep-recipe trap re-confirmed.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the committed pair (WIP cap 3, never-dry floor) is jointly unsatisfiable as a stationary guarantee, at the seat's own measured burst cadence the floor is missed a FIFTH of the clock, the miss survives a 4× cap raise, and the backpressure clause binds the drafter a fifth of the clock too — 'never dry' names a limit (K→∞ AND r > 1), not a rule, and dry events inside the priced band are arithmetic, not anomalies": at the decision cell, **D(3, r̂) ≥ 1/10** exact, AND **D(3, r) ≥ 1/20 at every grid r** (robustness across the full bracket 1/2 ≤ r ≤ 2), AND **D(12, r̂) ≥ 1/40** exact (the cap-lift clause), AND **B(3, r̂) ≥ 1/5** exact (the backpressure price). (Checked FIRST because the costly direction is fleet-wide: every seat inherits ORDER-shaped "keep a capped pipeline AND never starve the consumer" pairs — SIM-REQUEST intake queues, the fm review-queue drain, baton chains — and committing cap + floor without pricing D ships a standing violated SLA that then fires as apparent seat failure and triggers escalation work, exactly as the two lived DRY events did.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the pair is compatible in practice at the committed constants": D(3, r̂) ≤ 1/50 AND B(3, r̂) ≤ 1/20. (Mutually exclusive with REJECT by arithmetic on both clauses.)
- **NULL** — anything else; pre-registered axes: **band-straddle** (D(3, r̂) ∈ (1/50, 1/10), or the grid-robustness clause alone fails, or B(3, r̂) ∈ (1/20, 1/5) — the finding is the exact D/B table with the safe-cap scan); **anchor fragility** (r̂ and r₂ disagree on the D ≥ 1/10 headline clause — the measurement-window finding; disarmed at drafting: D(3, r₂) ≈ 0.159, both anchors clear); **theorem failure without gate failure** (T1 positivity, T2 monotonicity/frontier, T3 balanced laws, or the swap symmetry fails while F1–F6 pass — the drafter's chain algebra is wrong and the corrected law is the finding); **twin-arm disagreement** surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067 lesson, applied): the sim is FULLY DETERMINISTIC at every decision cell — every decision clause and every F-gate is an exact-rational identity or a byte comparison; the only seeded arm is reporting-only with NO statistical gate (its sole gates are the draw-count sentinel and exact reproducibility, pass probability 1 for a correct implementation); JOINT pass probability across all gates for a correct implementation = 1 EXACTLY (the P059–P068 no-stochastic-gate precedent), and decision separation is noise-free exact arithmetic — the disclosed landing clears the headline band at 2.06×, the grid-robustness band at 1.33× (worst cell r = 2), the cap-lift band at 1.33×, and the backpressure band at 1.49×, so the ruling cannot move except via a mis-implemented model, which the anchor gates catch as INVALID.

## Gates (run INVALID on any failure)

- **F1 — chain identities:** πQ = 0 with residual exactly zero at every grid cell (Arm B); Σπ = 1 exactly; per-level detailed balance λπ(j) = μπ(j+1); the flow-conservation identity λ(1 − π(K)) = μ(1 − π(0)) exactly; E(K, r) = 1 − D iff r ≥ 1 and E = 1 − B iff r ≤ 1.
- **F2 — the three structure theorems, exact at every grid cell:** (a) T1 positivity — D(K, r) > 0 at every finite (K, r), with the exact lower bound D ≥ 1/(K + 1) · min(1, r^(−K)); (b) T2 — strict monotone decrease of D in K along every r-row and in r along every K-column, and the frontier check: at r = 1/2, D(40, 1/2) ∈ (1 − r, 1 − r + 10⁻¹⁰) — the max(0, 1 − r) floor approached from above, never crossed; (c) T3 — π uniform at r = 1 with D = B = 1/(K + 1) and TH = K/(K + 1)·μ exactly, and ΔD(3→4, r = 1) = 1/20 exactly.
- **F3 — census anchors (reference values, exact):** D(3, r̂) = 62712728317/304425042745 (= 3973³/(3973³ + 3973²·4492 + 3973·4492² + 4492³)); B(3, r̂) = 90639863488/304425042745; D(3, r₂) = 29352074455423/184314341266075; D(3, 1) = 1/4; D(3, 1/2) = 8/15; D(3, 2) = 1/15; D(12, r̂) ≈ 0.0332081 (exact rational pinned in the fixture); D_det(3, r̂) = 0 exactly with the threshold K_det(r̂) = ⌈(1 + r̂)/r̂⌉ = 2; r̂ = 4492/3973, r₂ = 40428/30847, r_life = 150482/391243 re-derived from the pinned gap integers.
- **F4 — the hand worlds:** K = 1 → D = 1/(1 + r) by pencil (a one-token loop is dry exactly while its token drafts); K = 2, r = 2 → π = (1/7, 2/7, 4/7) by pencil; r = 1, K = 3 → the uniform quarter.
- **F5 — the swap symmetry & degeneracies:** station relabelling — π_j(K, r) = π_{K−j}(K, 1/r) exactly at every grid cell (so D(K, r) = B(K, 1/r): one seat's dryness is the mirror seat's backpressure); the r → 0 limit direction (D → 1, an infinitely fast verdict side starves itself) and r → ∞ direction (D → 0, B → 1) checked at the grid ends as strict orderings.
- **F6 — battery:** Arm B reproduces every Arm-A number exactly; twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinels counted and asserted; the Arm-R deterministic-shape trace sits beside the exact D_det closed form (reporting); aux seed 20261613 never read; stdout + results.json byte-identical across two process runs (Arms A/B platform-independent exact rationals; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P068 exact-arm norm)

REJECT, at the drafter's exact values (the sim re-derives everything from scratch and must not trust these; computed at drafting by BOTH arms — closed form and independent Fraction Gaussian-elimination solve — agreeing on every rational): decision cell (K = 3, r̂ = 4492/3973) — **D = 62712728317/304425042745 ≈ 0.20600** ≥ 1/10 (2.06×): the committed cap misses the committed floor a fifth of the clock in the seat's own BEST regime (continuous burst drafting); grid robustness — worst cell D(3, 2) = 1/15 ≈ 0.0667 ≥ 1/20 (1.33×), best-for-the-folk cell D(3, 1/2) = 8/15 ≈ 0.533; cap-lift — **D(12, r̂) ≈ 0.03321** ≥ 1/40 (1.33×): a 4× WIP raise still misses "never" by every reading of the word; backpressure — **B(3, r̂) = 90639863488/304425042745 ≈ 0.29774** ≥ 1/5 (1.49×): "backpressure holds" is true and is the same coin's other face — the drafter is cap-blocked (harvest-diverted) ~30% of the clock. The variance exhibit: **D_det(3, r̂) = 0 exactly** (clockwork cadence at the same means satisfies the pair perfectly, from K = 2 up) — the entire 20.6% is dispersion-born, and the committed record's own regime spread (burst 1387–2674 s gaps; lifetime mean 5839 s vs burst mean 1986.5 s) says the lived cadence is dispersed WORSE than memoryless across regimes; consistently, D(3, r_life) ≈ 0.629 at the lifetime anchor, and both lived DRY events (claims 3–4) occurred in exactly that day-pause regime. Falsifiability is real on every clause: the deterministic leg shows the folk pair is genuinely satisfiable in a low-variance world (a steadier lane kills the REJECT — APPROVE is not vacuous); the (K = 12, r = 2) corner lands D = 1/8191 ≈ 0.00012 (deep cap + fast drafter IS effectively never-dry — the bands are live); and one grid step from r̂ to r = 2 already drops the headline D below its own 1/10 clause (1/15), so the headline genuinely rides the MEASURED anchor, not the model shape. T3's quarter-quarter-3/4 balanced law and T2's max(0, 1 − r) frontier are the standalone keepers: the first prices any parity pipeline's cap instantly, the second says when a cap raise is the WRONG lever (r < 1 — speed the producer up instead).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-doctrine head: the verdict CONSUMER is the manager/kit layer that words seat orders, plus this seat itself as first subject. REJECT → paste-ready structured choice, recommendation first per Q-0263.2: **(a, recommended)** keep cap 3, RESTATE the floor as a priced SLA — replace "never dry" with "stationary dryness ≤ d at the measured cadence" using the sim's exact K\*(r, d) table, and reclassify dry events inside the priced band as arithmetic (no escalation work), outside it as signal — the committed ⚠-style escalations then carry a geometry-corrected false-positive rate exactly as P061 found for superbot's THIN signal; **(b)** buy dryness with VARIANCE, not WIP — steady the drafting cadence toward clockwork at the same mean (the exact D_det law prices this as fully curative at K ≥ 2, where T2 proves no affordable cap raise is); **(c)** raise the cap only on the r > 1 side and only with the table in hand (0.206 → 0.033 for a 4× raise; for r < 1 the frontier max(0, 1 − r) makes drafting speed the only lever). Owner/lane intent call, never ruled here. APPROVE → the committed pair gains a measured basis and the two lived DRY events demand a different explanation (the model or the anchors are wrong — the corrected attribution ships). NULL → the named axis ships with the exact D/B/K\* tables. Known co-consumers of the verdict: every fleet surface pairing a WIP/queue cap with a never-starve expectation (build seats' SIM-REQUEST intake under the ORDER 032 priority rule, the fm review-queue drain P037 priced, baton/wake chains), and the named follow-ups (multi-lane multi-class extension — 4 rotating lanes share the cap; the verdict-side batching reality; measured service-time distributions from a richer verdict-latency ledger once sim-lab's timestamps are harvested in bulk; the transient — not stationary — dryness of a pipeline that starts full).

## Dedup

Tree-wide `rg -i 'conwip|closed.network|gordon.newell|wip.cap|birth.death|truncated.geometric|dryness|never.dry|cyclic.queue|kanban'` (bootstrap.py/.substrate excluded) at HEAD dc155cb: every hit is either THIS head's harvested source sentences (`control/inbox.md` — the cap/floor/dry-event quotes themselves; outbox/archive echoes of the same order text) or a distinct-mechanism neighbor argued here. Nearest priors: **P061 → plan-depth refill jitter** (the heaviest `never-dry` hit, and the true nearest kin — but an OPEN-loop periodic-review base-stock head: superbot's order-up-to depth S against a count-triggered refill window W = 30 − ℓ_prev + ℓ_cur, failure mode = refill LATENESS JITTER, guarantee riding lag regularity; no WIP cap, no backpressure/blocking, no closed circulation, no stationary chain — this head's object is the CLOSED loop where the cap itself makes never-dry impossible at ANY service regularity short of clockwork, on different harvested constants from a different repo's orders; zero shared fixtures); **P019 → backlog low-water signal** (a reorder-point ALARM threshold for manager routing — prices when to SIGNAL, not whether cap + floor cohere; its dry-wake fraction is a wake-economics cost, not a stationary starvation law); **P065 → outbox rollover stub saturation** (same bus, different physics — byte growth vs queueing; disclosed above); **P033/V035 → assign-at-merge queue tax** (superbot, OPEN M/D/1 serialization delay — no cap, no closed loop); **P044 → checkout pooling** (the unrelated slot's OPEN M/M/c pooling-vs-split wait ratios — no population constraint, no dryness); **V014 → routine cadence economics** (wake policy per trigger — prices WHEN the seat wakes, not what the WIP cap does to the buffer between two seats). Method kin only: the P048/P060/P064 exact-Fraction stationary-solve discipline (chain solves + twin arms), reused as machinery on a new object (a closed-loop cap-vs-floor feasibility frontier with the swap symmetry and the deterministic-service exhibit — this head's own additions). No proposal P001–P068 and no verdict prices a WIP cap, a closed/CONWIP loop, blocking-based backpressure, or the cap-floor joint-feasibility question.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) **MEMORYLESS service is the pinned decision model** — real drafting/verdict times are neither exponential nor independent; the deterministic exhibit D_det (dryness 0 at the same means) brackets the low-variance side, so the exponential choice INFLATES D relative to a clockwork world — direction APPROVE-ward disclosed — while the committed record's cross-regime dispersion (burst/night/lifetime means 1986.5 / 1714 / 5839 s) argues the lived process is MORE dispersed than any single-rate memoryless model, direction REJECT-ward; the decision rides the pinned model and says so, and Arm R's three service shapes report the bracket. (2) **The burst anchor is the dryness-minimizing regime choice** — r̂ is measured on the seat's fastest committed drafting stretch; every other committed regime (r₂, r_life) lands HIGHER dryness at K = 3, so the headline clause is conservative in the direction that favors the folk claim. (3) **Single-class single-server stations** — the 4 rotating lanes ride one class and the verdict side is one server; multi-class and batching are named follow-ups (they redistribute, not remove, the positive dry mass — T1 is population-structure-free). (4) **Stationarity** — the head prices the long-run law, not the transient of a freshly-filled pipe; the two lived DRY events occurred ≥ 3 days into continuous operation, inside the stationary reading. The T1 impossibility and T2 frontier are robust to (1): positivity of π(0) holds for ANY service distribution with unbounded busy-period variability, and D_det = 0 marks the exact boundary case — the theorems are stated model-conditional and the sim verifies them within the pinned chain.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'conwip|closed.network|gordon.newell|wip.cap|birth.death|truncated.geometric|dryness|never.dry|cyclic.queue|kanban'`
> (bootstrap.py/.substrate excluded) at the grounding pin `dc155cb` returned only
> this head's own harvested source sentences plus the distinct-mechanism neighbors
> argued in Dedup (P061 open-loop refill, P019 signal threshold, P065 byte growth,
> P033/P044 open queues, V014 wake economics). (b) **kill test NOT triggered** — no
> prior proposal P001–P068, idea file, or session-card 💡 prices a WIP cap, a closed
> loop, or the cap-floor pair; no recorded drop of this head exists. (c)
> **feasibility + liveness arithmetic checked LIVE** — both arms (closed form +
> independent Fraction Gaussian-elimination stationary solve) ran at drafting in
> < 1 s stdlib and agreed on every exact rational; the measured constants were
> extracted from the committed headers this session (gaps 1622/2674/2263/1387 s;
> S_v = 2246 s); expected landing DISCLOSED with its exact drafting values (REJECT,
> D = 62712728317/304425042745 ≈ 0.206, B ≈ 0.298, D(12) ≈ 0.033) rather than
> hidden, all rulings reachable under the pre-registered rule, the deterministic
> D_det = 0 exhibit and the (K = 12, r = 2) near-zero corner both named as the live
> APPROVE-side edges, and the INVALID controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of a pair of
committed owner rules against each other, taken where they actually live: this
seat's own pipeline, whose WIP cap ("WIP cap 3, backpressure holds") and never-dry
floor ("the PROPOSAL→VERDICT pipeline is never dry") were committed separately and
never priced jointly — although the committed record already contains two lived DRY
events. On exact `fractions.Fraction` chain arithmetic the dry fraction D(K, r), the
backpressure fraction B(K, r), the flow identities, the impossibility/frontier/knee
theorems, and the safe-cap table are all exact at every grid cell, judged against
bands fixed before any code (REJECT first: D(3, r̂) ≥ 1/10 AND grid-robust D ≥ 1/20
AND D(12, r̂) ≥ 1/40 AND B(3, r̂) ≥ 1/5; APPROVE: D ≤ 1/50 AND B ≤ 1/20; NULL
otherwise with named axes), byte-identical across two runs, with the seeded traces
demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-14 fleet-backlogs
opener goes unserved and the cap-floor pair stays an unpriced standing SLA that
fires as false seat-failure signal. (ii) Treat the two lived DRY events as incidents
to be individually post-mortemed — mistakes the mechanism for its symptoms; the
stationary law says the events recur at a computable rate forever. (iii) A prose
note "caps cause starvation sometimes" — retells the direction, measures nothing,
misses the three exact keepers (the impossibility, the max(0, 1 − r) frontier that
says when cap raises are the wrong lever, the quarter-quarter-3/4 balanced knee).
(iv) An MC-only sim — leaves every decision number seed-noisy when the (K+1)-state
chain is exactly solvable (the V065/V067 lesson): the decision cells are closed-form
rationals, MC is demoted to the service-shape bracket. (v) This head: exact chain
census as the ruling, REJECT-first bands on dryness + robustness + cap-lift +
backpressure, INVALID on the F1–F6 identity/theorem/anchor/hand/symmetry/battery
gates, honesty rows via the deterministic exhibit and the lifetime anchor. (vi)
Over-scope (multi-class lanes, verdict batching, transient analysis, measured
service distributions in bulk) — each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~150-line stdlib file: a truncated-geometric closed form, a Fraction
Gaussian-elimination stationary solve, and a grid loop — that single kernel yields
the exact dry/backpressure/throughput surfaces, all three theorems verified as
THEOREM CHECKS rather than estimates, the swap symmetry, the deterministic-service
boundary law, and the K\*(r, d) safe-cap table the consequence menu ships — from a
sim a verdict session runs cold in under a second.

**4. What breaks it? (assumptions made explicit)** (a) **Memoryless service is a
choice** — disclosed with BOTH directions priced: the deterministic exhibit
(D_det = 0) brackets the APPROVE-ward error, the committed cross-regime dispersion
argues the REJECT-ward one; the decision rides the pinned chain and says so.
(b) **The anchor is one committed verdict pair** — S_v = 2246 s is the only
append→finalization pair echoed on this repo's own bus; the grid brackets r across
[1/2, 2], the second anchor r₂ agrees on the headline clause (disarmed NULL axis),
and a bulk verdict-latency harvest is the named follow-up. (c) **Band placement
could cherry-pick** — the 1/10, 1/20, 1/40, 1/5 clauses are committed BEFORE the
sim, the expected landing is DISCLOSED (REJECT), and falsifiability is two-sided:
D_det = 0 and D(12, 2) = 1/8191 are live APPROVE-side edges, and the headline
clause fails one grid step away at r = 2. (d) **DRY definition** — pinned to the
committed record's own words ("no unverdicted proposal exists", n = 0), not to
ORDER 003's softer "drafted-or-in-flight" reading (under which n = 0 with a draft
in progress still satisfies the floor — that reading is priced too: it equals
1 − B ≥ station-1-busy, and the REJECT's B clause prices exactly its cost).
(e) **An arithmetic slip in the drafter's hand facts** — the sim re-derives
everything; all theorems are F2 gates AND carry the theorem-failure-without-gate-
failure NULL axis, so a wrong hand claim becomes a finalized corrected law, not a
silent bad gate.

**5. What does it unlock?** The round-14 fleet-backlogs opener served with the
slot's first self-referential ORDER-text head; a measured, citable answer to "can a
WIP-capped pipeline honor a never-dry SLA" with three standalone keepers (the
impossibility theorem T1; the max(0, 1 − r) frontier T2 that tells any seat when a
cap raise is the wrong lever; the balanced knee T3 that prices any parity
pipeline's cap by pencil); the reclassification of this seat's own two lived DRY
events from anomaly to arithmetic; and a transferable correction for every fleet
surface that pairs a cap with a never-starve expectation — price the pair's joint
feasibility frontier BEFORE committing both, and buy dryness with variance
reduction where the frontier says WIP cannot reach.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arm A settles every decision number exactly in
milliseconds with no seed. The single cheapest probe if a reader doubts a specific
leg is the K = 1 hand world by pencil (a one-token loop is dry exactly while its
token is being drafted: D = S_d/(S_d + S_v) = 1/(1 + r) — at r̂ that is already
3973/8465 ≈ 47% dry, and no rule wording changes it), which anchors the chain
machinery against a two-line hand count.

**7. What would make this a mistake to run?** If the exact solve were unavailable
(it is not — a (K+1)-state chain solves in milliseconds), if the head duplicated a
prior (it does not — P061 is open-loop refill lateness on another repo's constants;
P019 is an alarm threshold; no prior touches the cap or the closed loop), or if the
disclosed REJECT made the run theater. It does not: the value is the independent
hermetic re-derivation of the three theorems PLUS the parts no order states — the
exact 20.6%/29.8% price of the committed pair at the seat's own measured cadence,
the D_det = 0 variance attribution, and the K\*(r, d) table the consequence menu
needs — and both non-REJECT rulings are genuinely reachable (the deterministic and
deep-cap corners are exact APPROVE-side witnesses; the headline clause dies at
r = 2, one grid step from the anchor).

**8. How will we know it worked?** A committed sim-lab report with: the exact
D/B/E/W surfaces over the full (K, r) grid (Fractions + float renderings), the
three theorem verifications plus the swap symmetry, the flow identities, the
deterministic-service exhibit beside its Arm-R trace, the K\*(r, d) safe-cap table,
the F1–F6 gate results, the verdict token against the pre-registered bands, Arm R's
three service-shape rows beside the exact values (reporting-only), and a
byte-identity note (two process runs identical). A clean run reproduces the
drafter's disclosed values (D(3, r̂) = 62712728317/304425042745, B(3, r̂) =
90639863488/304425042745, D(12, r̂) ≈ 0.0332, D_det(3, r̂) = 0) from scratch, or —
the more interesting outcome — DISAGREES and pins the drafter's error, which the
pre-registered rule then rules on honestly (the theorem-failure NULL axis exists
for exactly that).

**Recommendation: sim-ready**
