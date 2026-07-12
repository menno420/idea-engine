# Session — single-pass probe: superbot-next known-risks-fix-coupling-checker-doctrine

> **Status:** `complete`

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + index re-badge + card; no code)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot-next/known-risks-fix-coupling-checker-doctrine-2026-07-12.md` —
the 2026-07-12 superbot-next harvest head from the tournament-entry race-fix
card (@ `80464ab`): generalize the just-proven #221→#223 pattern into standing
checker doctrine — every "suspected real bug" a checker surfaces lands as a
loud KNOWN_RISKS row whose deletion the stale-row guard couples to the fixing
PR. The dispatch's open question: does codifying an already-live,
self-enforcing pattern add anything — or is it terminal uncodified (a reject
being a fully successful outcome)?

Verify-first, live: N = superbot-next HEAD
`39bf226b98b48083f9b9d1b1cc8a644cd3dae9e3` (`git ls-remote`-resolved this
session, three commits past the harvest pin `80464ab` — #225/#226/#227; every
probe-relevant file byte-identical across the gap by `git diff --stat`).
Decisive findings:

- **The mechanism is live and its ONE lifecycle is complete**:
  `tools/check_money_race.py` @ N defines the two-ledger idiom (ALLOWLIST
  verified-safe with per-row justification; KNOWN_RISKS loud-not-red, stale
  row = RED); its ledger history is exactly 1 row — minted #221
  (enter_tournament_in_txn double-debit), deleted coupled-to-fix #223
  ("worked exactly as designed", the fix card's words), 0 drifted; the dict is
  now `{}` (line 118) with the cleared-row comment.
- **Self-enforcing ONLY where instantiated**: blobless-clone grep at N —
  `KNOWN_RISKS` hits exactly 1 of 23 `tools/check_*.py`; the sibling fences
  (check_egress, check_no_skip — the docstring's own cited "allowlist idiom"
  precedents) hold bare `ALLOWED_*` frozensets, no per-row justification, no
  stale-row guard. Adoption is convention-by-imitation.
- **Codified NOWHERE**: `docs/collaboration-model.md` @ N carries only the
  ORDER-010 @codex rule + "Friction → guard"; `docs/decisions.md` greps zero
  for known_risk/money_race/fix-coupl; lane inbox = ORDERs 001–013, no
  doctrine carrier; the routed band-binding/effect-arming doc slice has NOT
  landed — the shared carrier is still open.
- **The uncoupled disposition is alive as contrast**: the #194 prose-ledgered
  latent bug (`sb/domain/btd6/service.py:274-275`) is still live at N, file
  untouched since #144 — session-found and deliberately deferred, but it
  demonstrates prose rows carry no lifecycle guard.
- **A queued consumer exists**: the routed recapture-disposition warn-first
  checker slice (`ideas/superbot/golden-recapture-on-bugfix-2026-07-10.md`,
  parked routed at superbot-next) is a judgment-class checker mint this
  doctrine would bind — unlike PR #230's kit head, which parked on a
  no-queued-consumer trigger-misfire.

Verdict: **parked(routed — lane build-direct)** — NOT reject: the coupling
self-enforces per instance but adoption does not self-propagate as binding
(the lane's own ORDER-010 "ENCODE THE RULE DURABLY … survives inbox rotation"
diagnosis), and the value peak is one KNOWN_RISKS-disposition subsection
folded into the SAME `docs/collaboration-model.md` doc-only slice already
routed for band-binding + effect-arming — three sections, one lane PR/ORDER,
marginal cost ≈ a paragraph. Nothing sim-shaped (a doc encoding a proven
practice); no outbox proposal.

Dedup swept: `warn-first-checker-authoring-kit` (PR #230 probe — adjacent not
overlapping: authoring ergonomics at S vs finding lifecycle at N; its 23-checker
census reused as this probe's baseline); `band-binding-doctrine-encoding` +
`effect-arming-compensator-checklist` (same CARRIER, disjoint content — this
head rides their doc slice); `oracle-copy-punctuation-drift-sweep` (same source
card's other 💡, disjoint, sim-ready P011); `golden-recapture-on-bugfix` (the
queued consumer, not a duplicate); `lint-bundle` + superbot checker heads
(other repos/surfaces). No duplicate idea file.

Inbox read-only check (dispatch ask): `control/inbox.md` carries ORDERs 001
and 002 only — **no ORDER 003 or later** at branch time.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carried the `ideas/superbot-next/` collision flag per
the PR #222/#225/#226/#228 workflow convention.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/superbot-next/known-risks-fix-coupling-checker-doctrine-2026-07-12.md`
  (state flip captured→parked(routed — lane build-direct…) + probe report v0
  append), `ideas/superbot-next/README.md` (index bullet re-badge per the
  PR #192 card convention)
- sessions touched (1): `.sessions/2026-07-12-known-risks-checker-doctrine-probe.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY
  read of `control/inbox.md` for the ORDER-003 check)
- git: branch `probe/known-risks-checker-doctrine` off main `7fd857a`,
  born-red card first commit `f7b9e51`, probe+close-out commit follows;
  draft PR flipped ready per dispatch instructions — landed by the kit-owned
  auto-merge flow, never merged by this slice.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park routed, lane
  build-direct). The dispatch explicitly legitimized a
  reject("already self-enforcing"); the probe weighed it in Q4 and ruled it
  down on evidence, not caution: per-instance self-enforcement (the stale-row
  guard) is not fleet adoption (1/23), and the lane itself already ruled that
  unencoded conventions don't survive seat rotation (ORDER 010, executed for
  @codex). The graceful-degradation note: if the carrier slice lands first,
  the fold-in becomes a trivial same-doc follow-up — the routing cannot
  strand.
- Next session should know: the lane self-serve check for this head is one
  raw fetch — `docs/collaboration-model.md` at lane HEAD; a KNOWN_RISKS /
  finding-disposition subsection appearing there means verify-and-close. The
  routed slice's text spec lives in the probe's Q8 (disposition rule + the
  #223 ⟲ row-content lesson: oracle citation up front). The manager-sweep
  unit is now THREE sections riding one collaboration-model.md ORDER
  (band-binding + effect-arming + this).

## 💡 Session idea

The three superbot-next doctrine heads (band-binding, effect-arming, this)
were probed on three different days and each independently concluded "ride
the same `docs/collaboration-model.md` doc-only PR" — but nothing anywhere
aggregates routed-slice CARRIERS, so each probe re-derived the pairing by
grepping sibling state lines, and the manager's :30 sweep sees three separate
index bullets rather than one three-section lane ORDER. Cheap fix shape: a
section-README "routed carriers" rollup line (or an outbox-adjacent note)
that names the shared carrier once — turning N same-carrier parks into one
sweepable routing row the moment N≥2.

## ⟲ Previous-session review

PR #240 (registry-shrinkage probe): adopted wholesale — the live-HEAD-first
discipline (N moved again since #240's `af985c1`; the byte-identical
diff-stat over probe-relevant files is what let harvest citations carry), the
born-red-card collision flag under the dispatch boundary, and the
"verify the substance, rule on the substance" honesty rule. Improvement
carried: #240's report measured its claims (≈1165 refs) rather than asserting
them — this probe did the same for adoption breadth (1/23 by grep, lifecycle
counts 1/1/0 by ledger history) instead of accepting the source card's
"worked exactly as designed" as sufficient. Divergence, declared: #240 upheld
a head whose letter was wrong; this probe upheld a head whose letter was
right but whose REJECT framing (offered by the dispatch itself) was the trap
— the shared rule held in a third direction: the self-enforcement claim is
true per instance and false per fleet, and only the measured 1/23 split
settles which half rules.

## Handoff → next wake

Facts for the coordinator heartbeat (NOT written here — control/ is
coordinator-only): verdict parked(routed — lane build-direct, riding the
band-binding/effect-arming collaboration-model.md carrier — verified UNLANDED
at N `39bf226`); no outbox proposal; inbox still ORDERs 001–002 only, no
ORDER 003+; the superbot-next section index carries the re-badge. The routed
slice is manager-sweep material: ONE lane doc-only PR now carries three
sections; spec in this probe's Q8.
