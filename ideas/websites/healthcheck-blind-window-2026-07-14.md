# The healthcheck blind window — what does the shipped 6-hourly point-probe liveness net actually SEE, and does "up to 6 hours" survive the workflow's own delay-or-drop caveat?

> **State:** sim-ready

> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot,
> round 10 opener; the harvest SOURCE returns to websites for the slot's SECOND tap of
> that repo — P019 (round 1) harvested the SAME backlog file's "~3" low-water reorder
> bullet ONLY, and this head harvests a DIFFERENT, shipped constant (the healthcheck
> cron cadence + its hard-window claim) — after round 1 websites (P019), round 2
> superbot (P021), rounds 3–4 substrate-kit (P025/P029), round 5 superbot (P033),
> round 6 fleet-manager (P037), round 7 curious-research (P041), round 8
> superbot-mineverse (P045), round 9 curious-research second tap (P049)) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/websites@3076e9d1a092b81fd88a982405cb70af483f3931 · fetched 2026-07-14T01:08:43Z
> (the harvest-source pin — read via read-only shallow clone this slice, HEAD
> ls-remote-verified; public repo per the Q-0272 standing authorization, reading path
> per superbot docs/fleet-reading-path.md §0. The sim itself is fully hermetic: zero
> repo/network reads at verdict time, every fixture constructed in-sim from the pinned
> constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"), the rotation established
by ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 9 closed fully served with P052 (#375) at the
unrelated slot (fleet backlogs → P049 #358, venture → P050 #371, game mechanics → P051
#373), so round 10 reopens at the FLEET-BACKLOGS slot and this slice is the round-10
opener. Nothing here edits websites files — routing is the manager's per Q-0260.
**Placement note:** websites IS a roster-derived section here (`ideas/websites/`,
README § Sections), so this head rides its matching lane section exactly as the P045
superbot-mineverse head did — no `ideas/fleet/` carve-out needed; the section claim
rides the P053 claim file per the claims README.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested decision, stated back.** The websites repo stands a scheduled liveness
watch: `.github/workflows/healthcheck.yml` @ `3076e9d` fires `scripts/healthcheck.py`
on cron `17 */6 * * *` (line 22 — every 6 hours at minute 17), probing the live
services' `/healthz` + `/`, the `/fleet` manifest parse, the arcade URLs, and every
open tester-task `product_url`. Its own header commits the framing (lines 3–10,
verbatim): *"Standing liveness verification … every 6 hours … Turns liveness from a
thing a session remembers to probe into a thing the repo verifies on its own clock —
the gen-1 retro handed over with 'liveness unverified at handover'; this closes that
class."* The same header commits the delivery caveat (lines 16–18): *"minute 17
offsets the top-of-hour cron congestion GitHub documents (a busy top-of-hour can delay
or drop scheduled runs)"* — and the notification asymmetry (lines 13–16): *"NOT a
required check — it gates nothing; a failed run notifies via the failed-workflow email
the owner already receives"* (a run that never fires sends nothing). The backlog
consumes the cadence as a hard window (`docs/ideas/backlog.md` lines 889–891,
tester-task bullet, verbatim): a drifted URL *"leaves testers pointed at a dead host
for up to 6 hours until the cron probe fires"*. And the repo's own cron-slot incident
(backlog lines 621–625) already taught it that fire slots are wall-clock, not
relative: *"the incident case (`17 */6 * * *` after 21:03Z → 00:17Z, not '+6h') is a
pinned test."* So `T = 6 h` is shipped, load-bearing, claimed as a worst-case window —
and never priced against what a point-probe at that cadence can actually detect.

**The founding doc already recorded an in-window miss.** The workflow's source idea doc
(`docs/ideas/scheduled-healthcheck-workflow-2026-07-10.md` lines 22–25, verbatim)
records that the manual probe it automated read green while reality was red the same
day: *"2026-07-10 01:02Z probe: all three 200/PASS, including the dashboard that had
real build failures at 03:46Z the same day."* A point-probe sees the instant it fires,
nothing between fires — the exact blindness this head prices.

**The falsifiable core.** Under a pinned outage population and a pinned
probe-delivery model built from the workflow's own committed caveat, (a) what fraction
of TRANSIENT outages (the merge=deploy redeploy-blip / platform-flap class) does the
shipped `T = 360 min` net ever detect, and (b) at what rate does the backlog's
"up to 6 hours" hard window FAIL for PERSISTENT faults (the dead-until-fixed rename
class) once per-fire delay and drop are priced? Both are computed exactly over a probe
cadence grid so the verdict either ratifies the shipped cadence's framing, quantifies
its blind window, or names the honest scope line the docs should carry.

**The pinned model (every constant exact and committed in this file — the P017–P052
hermetic precedent; all times INTEGER MINUTES; all probabilities exact
`fractions.Fraction` on equiprobable integer lattices).**

- **Probe cadence grid (the swept design constant).** `T ∈ {60, 180, 360, 720, 1440}`
  minutes. The shipped default is the cell `T = 360` (cron `17 */6 * * *`). Fires are
  scheduled at `s_k = k·T`; the wall-clock minute-17 phase is a fixed offset that
  cancels under the uniform onset phase below (noted in Model basis).
- **Probe delivery (the workflow's own caveat, priced).** Each scheduled fire is
  independently DROPPED with probability `q = 1/20` (INVENTED, pinned, disclosed —
  the header commits "delay or drop" qualitatively, no fleet measurement exists;
  sensitivity pair `q ∈ {0, 1/10}`, reporting-only) and otherwise executes at
  `s_k + d_k` with delay `d_k ~ uniform integer {0..30}` minutes (INVENTED, pinned,
  disclosed; sensitivity `{0}` degenerate / `{0..60}` wide, reporting-only). Drops and
  delays independent across fires and of everything else.
- **Transient outages.** Duration `D ∈ {5, 30, 60, 180, 360}` minutes, onset phase
  `φ ~ uniform integer {0..T−1}`; the outage occupies `[φ, φ+D)`. Headline mix:
  equiprobable over the five D cells (INVENTED, pinned, disclosed — the repo commits
  no outage-duration measurement; sensitivity mixes short-heavy `(5,4,3,2,1)/15` and
  long-heavy `(1,2,3,4,5)/15`, reporting-only). DETECTED iff some non-dropped fire
  executes inside the window. Conditional on φ, per-fire failure events are
  independent, so `P(miss | φ)` is an exact product — no approximation.
- **Persistent faults.** Dead-until-fixed, onset `φ ~ uniform integer {0..T−1}`;
  detection latency `L` = earliest successful execution at/after onset, minus onset.
  `WINDOW(T) = P(L > 360)` — the backlog's "up to 6 hours" claim read as the hard
  window it states, evaluated at every grid T (same product form, exact).
- **Metrics (exact).** `DET(T, D)` per cell; `DET_mix(T)` under the headline mix;
  `WINDOW(T)`; reporting-only: `E[L]` per T (closed geometric tail), the full
  `DET × (T, D)` table, the per-φ conditional at the shipped cell, and the cost
  column `runs/day = 1440/T` (the Actions-minutes view — a cadence table a reader
  can size against).

**The two arms.**

- **Arm A — DECISION (seedless, exact).** Full lattice enumeration: for each (T, D)
  and each φ, the exact product over the (finitely many) fires whose delayed execution
  could intersect the window, every probability an exact `Fraction`. Byte-identical
  across process runs, no seed read. The ruling rides Arm A alone.
- **Arm B — VALIDATION (seeded MC).** `N = 200,000` scenario draws (φ, per-fire drops,
  per-fire delays), pinned draw order, COMMON RANDOM NUMBERS across all five T cells
  (one scenario set, five evaluations). Agreement gate:
  `|EST − EXACT| ≤ 1/100` absolute AND `≤ 4·se` on every reported cell (both metric
  families) — any breach is a control failure (INVALID), never overridden. Arm B is
  validation only.

**Seeds (pre-registered, strictly above the P052 high-water 20261348 — sweep quoted in
Relations).**

- `20261349` — Arm B headline: the N = 200,000 common-random-numbers validation run
  across the full T grid, both metric families (the agreement gate above).
- `20261350` — Arm B control: the zero-noise identity world (`q = 0, d ≡ 0`) — exact
  identities in both arms: `MISS(T, D) = (T−D)/T` for `D ≤ T` and `0` for `D ≥ T`
  (e.g. `MISS(360, 180) = 1/2` exactly), `WINDOW(360) = 0` exactly,
  `WINDOW(720) = 359/720` exactly; any other value is a misbehaving control → INVALID.
- `20261351` — Arm B sensitivity confirmations: MC re-runs of the reporting-only
  sensitivity worlds (q ∈ {0, 1/10}; delay {0} / {0..60}; short-/long-heavy mixes),
  N = 20,000 each; reporting-only, can never flip the decision.
- `20261352` — stability leg: re-run the headline at N = 20,000; PASS iff the ruling
  class reproduces through twin independently-written decision evaluators.

**Decision rule (pre-registered, evaluated in this order — REJECT checked FIRST; all
band constants exact rationals; decision numbers are Arm A's exact Fractions only, at
the shipped cell T = 360 under the headline pins q = 1/20, d ~ {0..30}).**

1. **REJECT** ("the standing-liveness framing overstates what a 6-hourly point-probe
   sees — the net misses more than half of the pinned transient-outage mix, and/or
   the backlog's 'up to 6 hours' hard window fails more than one persistent fault in
   twenty once the workflow's own delay-or-drop caveat is priced; the honest doc line
   is a scoped one: 'catches faults that persist to the next fire, blind to most
   shorter blips'") iff `DET_mix(360) < 1/2` OR `WINDOW(360) > 1/20`.
2. **INVALID** (report, do not rule — controls misbehaving) iff the seed-20261350
   zero-noise identities fail in either arm, OR a monotonicity theorem gate fails
   (`DET(T, D)` non-decreasing in D at fixed T; `DET_mix(T)` non-increasing in T;
   `WINDOW(T)` non-decreasing in q under common random numbers — theorems under
   shared enumeration, so any violation is an implementation defect), OR Arm B
   breaches the agreement gate on any cell.
3. **APPROVE** ("the framing holds at the shipped cadence") iff
   `DET_mix(360) ≥ 3/4` AND `WINDOW(360) ≤ 1/100` AND the seed-20261352 stability leg
   reproduces the ruling.
4. **NULL** — anything else; three pre-registered axes: (i) **band-straddle** —
   `DET_mix(360) ∈ [1/2, 3/4)` and/or `WINDOW(360) ∈ (1/100, 1/20]` (works-partly;
   the measured pair IS the finding); (ii) **stability non-reproduction**; (iii)
   **sensitivity straddle** — a reporting-only world lands a primary conjunct on the
   other side of a band edge (the named axis is the finding; reporting legs never
   flip the decision).

**Liveness — expected landing DISCLOSED (closed-form decision arm; the P048–P052
norm: when the decision arm is exact, withholding a computable landing is the
dishonest move).** Drafting-time hand check (stdlib `fractions`, NON-authoritative —
the sim re-derives everything from the pinned constants and must not trust these
values): `DET_mix(360) = 123709/372000 ≈ 0.333` and
`WINDOW(360) = 22913/372000 ≈ 0.062` — BOTH REJECT conjuncts trip, so the honest
**expected landing is REJECT**. Per-cell exhibit: `DET(360, 5) = 19/1440 ≈ 1.3%`,
`DET(360, 30) = 19/240 ≈ 7.9%` (a half-hour outage is seen about one time in
thirteen), `DET(360, 60) = 19/120 ≈ 15.8%`, `DET(360, 180) = 19/40 = 47.5%`,
`DET(360, 360) = 6536/6975 ≈ 93.7%` — the net is a persistent-fault net, not a blip
net. Robustness the sharpening delivers: even with delivery PERFECT (q = 0, d ≡ 0)
`DET_mix(360) = 127/360 ≈ 0.353 < 1/2` — the transient-blindness conjunct is a
property of point-probing at the shipped cadence, NOT of the invented delivery noise;
while the WINDOW conjunct is delivery-driven (`WINDOW(360) = 0` exactly at q = 0,
d ≡ 0 — the "up to 6 hours" wording is TRUE precisely when GitHub's scheduler is
perfect, which is exactly the caveat the header itself disclaims). Falsifiability is
real, not theater: the T = 60 grid cell lands `DET_mix ≈ 0.685 ∈ [1/2, 3/4)` (the
NULL band) with `WINDOW ≈ 3.7×10⁻¹¹`, the q = 0 / d ~ {0..30} world lands
`WINDOW(360) ≈ 0.013 ∈ (1/100, 1/20]` (the NULL straddle), and the zero-noise world
lands the WINDOW conjunct on the APPROVE side — the pre-registered bands genuinely
discriminate, and the rule would rule differently at nearby pins.

**Reporting-only side pins (never gate the ruling).** (i) the full
`DET × (T, D)` table with the `DET_mix` and `WINDOW` columns and `runs/day = 1440/T`
cost column — the cadence menu a reader sizes against; (ii) `E[L]` per T × q (the
mean-latency view; zero-noise closed form `(T+1)/2` as its own sanity row); (iii) the
per-φ conditional `DET(360, D | φ)` at the shipped cell; (iv) every sensitivity world
named in the model; (v) the notification asymmetry carried as a quoted flag: a
DROPPED run sends no failed-workflow email — the silent-miss direction — and the
check is NOT required, so nothing gates on red (decidable by inspection, never
simulated).

**What a reader DOES differently on the verdict.**

- **APPROVE** → the "standing liveness verification" framing and the backlog's
  "up to 6 hours" window gain their measured basis, routed lane-side per Q-0260
  (this repo never edits websites files).
- **REJECT** → the framing gets an honest scope line (persistent-fault net, blind
  window quantified) and the "up to 6 hours" wording gets its measured violation rate
  under the workflow's own caveat; the priced cadence table gives the lane the
  detect-vs-runs/day menu if it ever retunes `17 */6` — and the already-captured
  scheduled browser-crawl bullet inherits the same table for ITS cadence choice.
- **NULL** → the named axis ships with its measured pair; the cheapest live probe is
  named below.

## Model basis — what is pinned vs a choice

- **The delivery noise (q, d) is INVENTED-but-pinned**, each with a reporting-only
  sensitivity pair. The workflow's own header commits the phenomenon ("a busy
  top-of-hour can delay or drop scheduled runs") and its mitigation (minute 17) but
  no magnitude; no fleet measurement exists. Direction stated: if minute-17 makes
  real drops far rarer than 1/20, the WINDOW conjunct weakens toward its q = 0 value
  (≈ 0.013, the NULL straddle) — but the DET_mix conjunct survives q = 0 entirely, so
  the expected REJECT does not ride the invented noise.
- **The transient-duration grid and mix are INVENTED-but-pinned**, disclosed, with
  short-/long-heavy sensitivity mixes. The repo commits no outage-duration data; it
  DOES commit one exemplar in-window miss (the 01:02Z-green / 03:46Z-red dashboard
  incident, quoted above) proving the class is real, not hypothetical.
- **The minute-17 phase cancels**: onset phase is uniform relative to the fire grid,
  so a fixed wall-clock offset shifts nothing (the cron-slot incident's lesson —
  fires are wall-clock slots — is CONSISTENT with this model, quoted above).
- **Detection ≠ notification**: a fire that executes and sees red turns the run red
  and emails; a DROPPED fire sends nothing. The sim prices detection; the
  notification asymmetry is carried as a reporting flag (inspection-decidable).
- **Curl-level blindness is out of scope**: the repo's own cold-browser bullet
  records regression classes this probe can never see at ANY cadence (rendering-only
  failures) — named as the source repo's own captured follow-up (the Playwright
  crawl), not smuggled into this head's metrics.
- **Independence of drops/delays across fires is an assumption**; the
  most-likely-to-flip alternative is CORRELATED scheduler congestion (a bad hour
  drops several fires). Direction stated: correlation fattens the WINDOW tail
  (REJECT-ward on that conjunct) and barely moves DET_mix; the wide-q leg brackets
  the scale.
- **Exact rationals throughout Arm A** — no float in the decision path; floats appear
  only in Arm B's empirical estimates and this file's `≈` annotations.
- **Cheapest live probe (pre-priced, on NULL or on demand):** the healthcheck
  workflow's Actions run history is PUBLIC committed evidence — pull the scheduled
  runs' timestamps, measure real inter-fire gaps and missing slots, and replace the
  invented (q, d) with measured values; one read, zero writes, no owner hardware.

## Relations — dedup sweep (verify-first, live this slice)

Tree-wide sweep at drafting HEAD `f6b1ff8` (ripgrep, kit excluded):
`rg -i -g '!bootstrap.py' -g '!.substrate' 'outage|downtime|detection.latency|inspection|probe.cadence|liveness|health.?check|dead.host|monitor' ideas/ control/outbox.md .sessions/`
returns no proposal or verdict that prices probe cadence, outage detection
probability, or a detection-latency window. The `liveness`/`healthcheck` hits are:
(a) `ideas/websites/scheduled-healthcheck-workflow-2026-07-10.md` — the harvested
LINK-INDEX of this head's own source doc (historical, shipped as websites #69); this
head does not re-propose the workflow, it prices the workflow's shipped cadence
constant and window claim; (b) `ideas/superbot/trigger-registry-liveness-sweep-…` —
a captured build idea (a sweep tool), no sim head, different repo; (c) incidental
prose ("liveness" as failsafe-aliveness in cards/orders). The seed sweep
`rg -oP '(?<![0-9])20261[0-9]{3}(?![0-9])'` (kit + `.substrate` excluded) plus the
range-notation companion over this tree at HEAD `f6b1ff8` AND the sim-lab working
copy READ-ONLY at `3d7ae2c` found max allocations 20261348 (idea-engine, P052) and
20261344 (sim-lab) — the larger numerals 20261542/20261664/20261833 are
Fraction-numerator digit substrings inside results.json-quoting outbox text, data not
seeds (the P046/P050/P051/P052 rule re-confirmed) — so 20261349–352 are clean, inside
the 8-digit band, no digit-boundary crossing.

**Nearest priors (disclosed, all distinct):**

- **P019 → V021 (same repo AND same backlog file — the disclosed second tap).** P019
  (round 1) harvested the backlog's "~3" low-water bullet and priced a REORDER POINT
  for never-idle lane backlogs (replenishment threshold, dry-wake economics). This
  head harvests the SHIPPED healthcheck cadence constant and prices DETECTION of an
  external down-state by a point-probe with unreliable delivery. Different bullet,
  different mechanism (inventory replenishment vs sampling/detection), different
  failure structure (dry backlog vs unseen outage), zero shared fixture. The second
  tap is disclosed, not hidden — the P049 precedent (curious-research's second tap)
  established that a rich source repo can be re-harvested honestly.
- **P012 → V014 (nearest method kin — cadence economics).** P012 priced ROUTINE/
  failsafe cadence for trigger CATCHING: every trigger WAITS until caught (nothing is
  ever missed; the costs are worker-turns and catch-latency, the constraint p95 ≤ 2h).
  This head's transients VANISH if unobserved — detection probability strictly < 1 IS
  the head — and the probe itself can silently fail to fire, a delivery-failure model
  P012's world has no analog of. Different objective (detection probability + hard-
  window violation vs cost per caught trigger), different world (external service
  outages vs owned trigger queue), zero shared fixture.
- **P029 → V031 (aliveness kin only).** Lease-renewal claim aliveness: INFERENCE from
  renewal-stamp presence in a ledger — no active probing, no cadence dial, no
  transient events. Method neighborhood only.
- **P045 → V056 (method kin only).** The same "price a shipped, hedged default on its
  named failure axes over a pre-registered grid" MOVE (staleness threshold: false-
  stale vs latency there; blind-window vs hard-window here), but its world is
  snapshot-age classification with no probe schedule, no delivery failure, no
  detection event. Method precedent, not overlap.

No prior proposal (P001–P052 re-scanned at HEAD), sim-lab verdict (V001–V063 ledger
scanned; V062/V063 in flight are the farm-faucet and coupon-collector heads, no
overlap), idea file, or session-card 💡 prices a probe-cadence/outage-detection
tradeoff or any inspection-schedule blind window.

## Probe report battery (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained knowledge probe over a
> pinned public repo, sim is report-only evidence, no spend/publish/irreversible
> surface — README § probe battery). Verify-first ran FIRST, live this slice: (a)
> **source verified at HEAD** — websites shallow-cloned read-only, HEAD
> `3076e9d1a092b81fd88a982405cb70af483f3931` ls-remote-confirmed; every harvested line
> quoted verbatim above with file + line numbers; the source repo's own control files
> carry no SIM-REQUEST to duplicate. (b) **dedup** — the tree-wide sweep quoted in
> `## Relations` returned zero domain hits; the four nearest priors are disclosed with
> their distinguishing mechanisms, including the P019 same-file second-tap
> distinction. (c) **kill test NOT triggered** — no prior proposal, verdict, or 💡
> prices probe cadence, detection probability, or an inspection blind window. (d)
> **feasibility + liveness arithmetic checked** — runtime bounded (Arm A is a few
> thousand lattice cells of exact-Fraction products per grid T; Arm B is one 200k
> loop + small legs; well under a minute, stdlib only); expected landing DISCLOSED
> with its exact drafting-time values (REJECT on both conjuncts at the headline pins)
> per the P048–P052 closed-form-arm norm, with the sensitivity and grid worlds shown
> to land in other bands so the rule genuinely discriminates.

**1. What is this really?** A pre-registered exact MEASUREMENT of a shipped scheduling
constant: does the websites healthcheck's 6-hourly point-probe (`17 */6 * * *`) earn
its committed "standing liveness verification" framing and the backlog's "up to 6
hours" hard window — computed as exact `Fraction` detection probabilities and
window-violation rates by full lattice enumeration (Arm A, the decision arm),
validated by a seeded common-random-numbers MC (Arm B), judged against bands fixed
before any code (REJECT `DET_mix < 1/2 OR WINDOW > 1/20` first, INVALID on misbehaving
controls, APPROVE `≥ 3/4 AND ≤ 1/100`, NULL with three named axes), byte-identical
across two process runs.

**2. What is the possibility space?** (i) Don't run it — the round-10 fleet-backlogs
slot goes unserved. (ii) Harvest a different repo — the remaining fully-untapped
candidates (trading-strategy is parked-and-graded-weekly; pokemon-mod-lab is DARK per
the reading path's own rule) are thinner than a shipped, load-bearing scheduler
constant with its own committed caveat and hard-window consumer; the second tap is
disclosed per the P049 precedent. (iii) A prose answer ("6 hours is a reasonable cron
cadence") — retells the folklore the workflow header already ships, measures nothing.
(iv) Measure the real Actions run history — the RIGHT eventual step for the (q, d)
pins and pre-priced as the live probe; it cannot answer the transient-detection
question (undetected outages leave no run record — that is the point). (v) This head:
hermetic, exact-arithmetic, pre-registered, with the repo's own quotes as the claim
authority. (vi) Over-scope (modeling GitHub's scheduler queue, Railway deploy
distributions, alert-fatigue economics, browser-level coverage) — named as
follow-ups, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~150-line stdlib file: an exact per-phase product enumerator parameterized by
(T, D-or-persistent, q, delay support) — reused for the headline, every sensitivity
world, and the zero-noise control — plus one seeded sampling loop. That single file
yields the ratify/scope-line verdict on the shipped cadence, the DET × (T, D) cadence
menu with its runs/day cost column, the WINDOW tail exhibit, and a reusable
point-probe blind-window pattern for every scheduled watcher the fleet arms (routine
failsafes, harvest freshness sweeps, the captured browser-crawl cadence choice).

**4. What breaks it? (assumptions made explicit)** (a) **The invented (q, d) and
duration mix** carry no measurement (disclosed; every one has a sensitivity pair; the
named live probe measures the delivery half directly, and the DET_mix conjunct is
shown to survive q = 0 entirely). (b) **Independence across fires** — correlated
congestion fattens the WINDOW tail; direction stated, wide-q leg brackets scale. (c)
**Band placement could cherry-pick** — all bands committed here BEFORE any code,
REJECT checked first, the expected landing DISCLOSED rather than hidden, and nearby
worlds shown to land in other bands so there is no room to retrofit. (d) **The
premise could silently fail** — a broken enumerator corrupts every cell; the
zero-noise identity control (exact closed forms, not tolerances) and three
monotonicity theorems rule INVALID before any ruling issues. (e) **Metric myopia** —
the ruling is on detection-and-window, the quantities the shipped texts claim;
notification fatigue, required-check policy, and browser-level coverage are out of
scope and named as flags/follow-ups, not smuggled in.

**5. What does it unlock?** The workflow header's framing becomes a measured basis or
an honest scope line plus a quantified blind window (routed lane-side per Q-0260);
the backlog's "up to 6 hours" wording gets its violation rate under the repo's own
caveat; the lane gains the detect-vs-cost cadence menu for `17 */6` and for the
captured browser-crawl's future cadence choice; and the fleet gains the point-probe
blind-window pattern — the sampling-side sibling of P012's catch-cadence economics —
for every scheduled watcher it arms.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment for the population claim: Arm A settles the ruling by exact
enumeration in under a second. For the delivery pins specifically, the named live
probe (read the public Actions run history, measure real gaps and missing slots)
decides the (q, d) question at one page-read of cost — pre-priced as the NULL/next
step, not a prerequisite.

**7. What would make this a mistake to run?** If the landing being disclosed made the
sim worthless — it does not: the value is the independent re-derivation, the MC
cross-check, the per-D exhibit (which the hand check says indicts the framing for
BLIPS while ratifying it for persistent faults — a scope line, not a demolition), the
delivery-vs-structure decomposition (which conjunct rides the invented noise and
which survives q = 0), and the cadence menu, with REJECT/APPROVE/NULL all reachable
at disclosed nearby pins. If the head duplicated P019 or P012 — the Relations section
shows the mechanisms are disjoint. If the sim were asked to validate the notification
asymmetry or the curl-level blindness — it is not: both are decidable by inspection
and carried as quoted flags, not gates.

**8. How will we know it worked?** A committed sim-lab report with: Arm A's exact
`DET × (T, D)` table, `DET_mix(T)`, `WINDOW(T)`, and `E[L]` columns as `Fraction`s
with float renderings plus the runs/day cost column; the verdict token (APPROVE /
REJECT / NULL, or INVALID) against the pre-registered bands; Arm B's agreement gate
outcome on every cell; the zero-noise control at its exact closed forms
(`MISS(360,180) = 1/2`, `WINDOW(360) = 0`, `WINDOW(720) = 359/720`); all three
monotonicity theorems passing; every sensitivity world's table; and a byte-identity
note (two Arm-A process runs identical). A clean run reproduces
`DET_mix(360) = 123709/372000` and `WINDOW(360) = 22913/372000` from scratch — or
DISAGREES and pins the drafter's arithmetic error, which the pre-registered rule then
rules on honestly.

**Recommendation: sim-ready**
