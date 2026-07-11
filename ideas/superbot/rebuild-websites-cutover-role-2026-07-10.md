# Idea — the off-Discord websites: rebuild disposition, cutover role, and staying current — link index

> **State:** parked(routed — the rebuild disposition the doc asked for is CONSUMED by practice at the websites lane (both sites rebuilt + dark-launched, producer question resolved read-only); the residual cutover-role call is an owner architecture decision, now ripe, tracked click-level on websites' own owner surface (docs/owner/OWNER-ACTIONS.md rows 1/4/6 @ 92c3dc6) and bundled as ONE structured-choice sitting on this slice's heartbeat ⚑ — probe report below)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/c77ee0d662aeaff892623c445297c5f2952de34d/docs/ideas/rebuild-websites-cutover-role-2026-07-03.md@c77ee0d · fetched 2026-07-11T10:41Z
> *(pin annotation: probe-time re-fetch at live superbot HEAD — byte-identical to the harvest pin `fd638e3` (sha256 `4e75226…` both, diffed this probe), so the canonical link below stays valid unchanged.)*

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-websites-cutover-role-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-websites-cutover-role-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-websites-cutover-role-2026-07-03.md)).

The public bot site and dev dashboard are fed by a producer that AST-parses the OLD repo; nothing dispositions them at cutover, so both sites would silently die. Owner-originated: define the websites' rebuild disposition and cutover role.

## Probe report (v0, 2026-07-11)

*Single-pass battery per the README panel default (sim-lab VERDICT 002): the head is a
disposition/routing question with no irreversible surface reachable from this repo (the
irreversible bits — DNS, service retirement — are owner-gated on another lane's rails),
and the verify-first sweep did not disagree with itself. Every load-bearing claim below
was fetched live this probe (2026-07-11 ~10:35–10:45Z): superbot HEAD `c77ee0d`
(canonical doc byte-identical from the harvest pin `fd638e3`, sha256-diffed), websites
HEAD `92c3dc6` (depth-1 clone + its 10:28Z heartbeat), superbot-next HEAD `dc32367`
(blobless clone + its 10:25Z heartbeat), fleet-manager roster gen #5 @ `3150f0e`
(websites row live/fresh).*

### Verify-first ledger — what practice already answered vs what is genuinely open

| Canonical item (superbot doc @ `c77ee0d`) | Status | Where it lives now (live-pin citation) |
|---|---|---|
| Rebuild disposition ("nothing dispositions the sites; both silently die at cutover") | **CONSUMED** | The websites repo IS the disposition: kickoff step 3 plan (websites PR #4 `f7d3def`), then both sites REBUILT + dark-launched — botsite PR #7 (Railway service `4314f839…`), dashboard PR #8 (D-0009, public per D-0011) — per `docs/current-state.md` + `docs/botsite.md` + `docs/dashboard.md` @ `92c3dc6`. The judgment-gap premise (§4 #4) no longer holds: the sites no longer die at cutover, their replacements are deployed and verified (heartbeat 10:28Z: all three services `/version` == main `1ff77e4`, wait_deploy CONVERGED). |
| Open fork 1 — interim producer (old repo vs new repo vs both) | **CONSUMED** | Resolved as rework-plan Q7 (recommendation taken): consume superbot's committed artifacts (`site.json` / `dashboard.json` / `console.json`) over raw, read-only, never rebuild the export tooling — `botsite/data_source.py` + `dashboard/data_source.py` @ `92c3dc6` read `superbot@main`; the console feed rides a pinned versioned cross-repo contract (superbot PR #1884, v1) with an honest schema-drift banner. Old repo stays the producer while the old bot is production — exactly the doc's "old = live bot" arm. |
| Open fork 2 — hosting + update cadence | **CONSUMED** | Own Railway project `superbot-websites` (3 services), deploy = merge-to-main auto, deploy-state DRIFT cell on the board (lane ORDER 001), healthcheck cron, 180s TTL feed cache; 22 work slices landed 2026-07-11 alone (#64→#118, heartbeat 10:28Z). |
| Open fork 3 — progress-dashboard scope, public vs owner-only | **MOSTLY CONSUMED** | Control-plane oversight board shipped and made public (owner verbatim "Yes drop the auth", D-0011 path; readiness board + fleet status + journal/decision browsing) — the §4 #16 owner-visual-artifact gap has a live surface. A rebuild-progress-specific view (Stage-2 rows walked etc.) was not found in the websites tree (doc grep only — not measured deeper); superbot-next's own parity ratchet/report job carries that job lane-side (26/49 ported, 168/168 goldens @ `8b55d95`, its heartbeat 10:25Z). |
| **The cutover-role call itself** (which site keeps which role, DNS, old-site retirement, control-panel home) | **OPEN — owner, unruled** | Tracked click-level on the LANE's own owner surface @ `92c3dc6`: `docs/owner/OWNER-ACTIONS.md` 🟡 row 1 (plan Q4, control home — "Do not port without an owner call"), row 4 (Q6 domains — "Deferred to cutover"), row 6 (OLD-site cutover/retirement — "Gated: needs your go"); `docs/question-router.md` Q6 "(unanswered — deferred to cutover)". The plan's migration order marks steps 3 and 5 "(owner go)". Not on the lane's heartbeat ⚑ (which carries only the Postgres + PAT asks). |
| Producer repoint at the NEW repo's manifest | **OPEN — sequenced to the BOT cutover, target exists** | superbot-next already commits the declared surface the doc wanted (`manifest.snapshot.json` + `manifest/layout/*.lock.json` @ `dc32367`), but no websites-side consumer reads it yet and the bot rebuild is mid-parity (26/49 subsystems @ its 10:25Z heartbeat) — the repoint keys to the BOT cutover (D-3/CUT-3), a later, separable event. |

**1. What is this really?**
An owner-originated 2026-07-03 gap-capture whose build half FINISHED without it: the
"sites have no rebuild disposition" premise was consumed by the websites lane (repo +
plan + both rebuilt sites, ledger above), and what survives is exactly one thing — the
cutover-role CALL: go/no-go on retiring superbot's two live site services, where bot
control lives (websites / superbot / superbot-next), and domains. That call is an owner
architecture/preference decision the lane has deliberately queued ("Gated: needs your
go"), not an open engineering question.

**2. What is the possibility space?**
Dispositions only, since the design work is done and the decision is owner-reserved:
(a) park(routed) with a structured-choice fan-in ask — bundles the lane's three open
rows into one paste-ready sitting; (b) leave captured — invites a future battery to
re-derive this ledger and re-ask an owner-reserved question (the stale-grounding trap);
(c) sim-ready — needs a reproduced-evidence question: none survives (see Q7); (d)
needs-more-grooming — nothing ungroomed: the lane's plan enumerated the seven forks and
the owner surface tracks the open ones; (e) reject — wrong: the residual call is real,
ripe, and costs dual-maintenance while unmade. Collapses to (a).

**3. What is the most advanced capability reachable by the simplest implementation?**
One ⚑ heartbeat entry that converts three scattered owner-surface table rows (websites
OWNER-ACTIONS rows 1/4/6) into ONE recommendation-first structured choice the owner can
answer with a single pasted line — plus the separability finding no surface records yet:
SITE cutover and BOT cutover are independent events (the new sites mirror the old bot's
data, which stays correct while the old bot IS production; the producer repoint keys to
the bot cutover and its manifest target already exists committed at `dc32367`), so the
site-cutover go needs zero waiting on the 26/49 parity march.

**4. What breaks it?**
- **The premise inversion going unnoticed** — the idea says "the call should precede
  more build-out", but build-out already reached the dark-launch line BY DESIGN
  (rollback before DNS is "free — do nothing", plan § rollback), so anyone reading the
  captured head as urgent-blocking would misroute effort; the honest framing is
  ripe-not-blocking, and the cost of delay is dual-maintenance plus de-facto answers
  baking in (the lane's backlog is already down to 4 buildables, heartbeat 10:28Z).
- **Bundling errors** — folding plan Q4 (control home) into the same sitting risks the
  owner deferring the whole bundle because ONE member is hard; mitigated by making the
  recommendation's Q4 arm "rule the home, defer the wiring" (the stub is credential-free
  by construction, dashboard.md § control panel).
- **Ledger rot** — websites moved HEAD twice during this probe's window alone; mitigated
  because every open item is tracked on surfaces with their own freshness discipline
  (the lane's OWNER-ACTIONS doc is a living list; this file's ledger cites pins).

**5. What does it unlock?**
The owner's one reply unlocks: plan steps 3/5 (retire superbot's `dashboard/` +
`botsite/` services — the last dual-running surfaces of the old repo's web story), the
Q4 control-panel wiring path (a separate service, wherever ruled), domain assignment,
and — for this tree — closing the superbot section's #155 shortlist item 2 without a
future re-probe.

**6. What does it depend on?**
Nothing buildable — a routing park has no build dependencies. The ask's freshness
depends on the reads above staying true: websites `92c3dc6` (clone + heartbeat 10:28Z),
superbot `c77ee0d` (doc byte-identical from `fd638e3`), superbot-next `dc32367`
(manifest surface present; parity 26/49 self-reported at 10:25Z), fm roster gen #5 @
`3150f0e` (no layer disagreed this probe — freshest-wins never needed). The producer
repoint additionally depends on a future superbot-next artifact/feed contract twin —
NOT asked for now (bot cutover is the arming event; capturing it today would race the
lane's own CUT-3 planning).

**7. Which lane should build it?**
No lane builds — the OWNER decides; that is the whole residue. On the ruling: websites
executes the site-side steps (it owns both replacements and the plan's cutover order),
superbot retires its two services, superbot-next inherits the control home if ruled
there and, at bot cutover, the producer contract. Not sim-lab: no reproduced-evidence
question survives — retirement timing, control home, and domains are
preference/architecture calls with reversibility already engineered (dark-launch +
deferred DNS), and simulation cannot settle a preference (the Q-0263.2 route is a
structured-choice ask, recommendation first).

**8. What is the smallest shippable slice?**
This PR: this report + the state flip + the section-README re-badge + the heartbeat ⚑
fan-in entry (six-field OWNER-ACTION bundling websites OWNER-ACTIONS rows 6/4/1 into one
paste-ready structured choice, recommendation first — the canonical rows STAY on the
lane's surface; the ⚑ is the fan-in, per the fewer-clearer-asks hygiene). Explicitly NOT
in the slice: any outbox entry (nothing sim-ready), any websites-lane file write
(Q-0260), and any producer-repoint pre-capture (bot-cutover-armed, see Q6).

**Recommendation: park** — routed: the doc's rebuild-disposition ask is consumed at
websites `92c3dc6` (both sites rebuilt, dark-launched, deploy-verified; producer
resolved read-only per plan Q7), and the one survivor — the cutover-role call — is an
owner architecture decision already queued owner-side ("Gated: needs your go",
OWNER-ACTIONS row 6), so nothing is simulable; the ⚑ on this slice's heartbeat hands the
owner the call as one structured choice with Option A (site-cutover go now, control home
= superbot-next wire-later, producer repoint at bot cutover) recommended.
