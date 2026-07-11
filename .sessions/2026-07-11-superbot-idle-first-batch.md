# Session — superbot-idle slice: first grounded idea batch (3 captures)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

- Claimed `ideas/superbot-idle/`
  (`control/claims/seed-superbot-idle-first-batch.md`, flat filename per
  control/claims/README; taken first commit, cleared in this branch's close-out
  commit per the section-claim precedent).
- **Ground truth first — the lane is BORN and deep in volume phase**, which
  reshaped the whole batch: `menno420/superbot-idle` @ HEAD `f11c71a` (ls-remote
  2026-07-11T03:31:35Z + blobless clone at the pin) — 45 merged PRs, 827 tests,
  12 theme packs, schema v1 frozen with md↔json parity, SETUP-CODE FORMAT v1 +
  150 cross-language vectors, render layer, SAVE FORMAT v1, economy design v1
  with pre-registered targets T1–T10 and the executable SIM-001 request; lane
  phase "STEADY-STATE HOLD" pending SIM-001/PLUG-001/orders. The roster row @
  fleet-manager `93d3a4d` (gen #4, 01:58Z — raw-fetched at the ls-remote-pinned
  SHA) records lane HEAD `97bfff2` 01:49Z: row is BEHIND live HEAD by 3 PRs
  (#43–#45) — recorded as the pin annotation on every capture.
- **Generated the section's first batch — 3 captures**, all state `captured`, one
  page each, blessed Grounding + Sequence lines (honesty guard: 3 well-grounded
  beat 5 speculative on a lane this fast; five candidates dropped, below):
  - `idle-economy-sim-kernel` (product) — the §6 head, MANDATED for this batch,
    and its arming condition turned out already MET: the lane pre-registered
    economy params (PRs #9+#12+#13) and wrote SIM-001 to be executable without
    follow-up questions, but it sits "awaiting manager relay" while sim-lab idles
    on an EMPTY queue (VERDICTs 001–005 finalized @ `f70fbea`, ls-remote
    03:37:05Z). The head: probe → likely sim-ready → outbox proposal RELAYING
    SIM-001's own spec (idea-engine's outbox is the surface sim-lab pulls
    directly, Q-0264; the lane cannot write it, Q-0260). Verify-first duty
    written into the capture: re-check sim-lab's intake at probe time.
  - `theme-catalog-gallery-read-contract` (product) — §3's gallery ("rendered
    from the committed theme packs") has a contract-complete WRITE path
    (setup codes, websites = named encoder) and NO read surface; a committed
    regenerate-or-red catalog index (the lane's proven vector-file discipline)
    published BEFORE the first gallery render. Consumer-side verified: websites
    @ `d4ed380` (ls-remote 03:34:07Z, clone-grep) carries zero
    idle/setup-code/gallery work.
  - `theme-schema-plugin-contract-promotion` (product) — the §4/§7 item-3
    decided-and-flagged promotion has NO tracker anywhere (lane PLUG-001 holds
    the adapter, not the promotion); the capture IS the tracker, armed by the
    blessed token form `after superbot-next#ORDER-002` so one grep surfaces it
    when the foreign order moves.
- **Dropped as too thin or duplicative (recorded, not padded):**
  - theme-concept intake batch (§6 "perfect INTAKE material") — the lane
    self-serves 3-pack catalog waves in-session with zero schema pinches and its
    own roadmap rules more packs "merge-on-gate-green filler, not risk
    reduction"; concept supply is not its constraint.
  - setup-code v2 bound ruling — the lane's own deferred-BY-DESIGN queue item,
    deferred to the PR that defines v2; capturing restates lane state.
  - plugin adapter — evidence-blocked upstream and already ⚑'d by the lane
    (PLUG-001, six-field); no idea-engine head unblocks a missing upstream doc.
  - generator purchase path (T10) — new engine surface the lane deliberately
    HOLDS (steady-state phase line) with the target already pre-registered;
    natural sequencing is after the SIM-001 verdict anyway.
  - websites-side selector/gallery UI head — real, but belongs in
    `ideas/websites/` (disjoint-section claims); the gallery-read-contract
    capture names websites as consumer; flagged as follow-up, not force-fit.
- Section README index updated (3 rows; Cross-links subsection kept intact).
- **Grounding fetched this session (public raw + git transport, Q-0260):**
  superbot-idle @ `f11c71a` (ls-remote + blobless clone: status, inbox — empty,
  current-state, economy-v1, provisioning, theme-schema, tree scan);
  fleet-manager roster @ `93d3a4d` (ls-remote-pinned raw fetch); sim-lab
  heartbeat @ HEAD `f70fbea`; websites @ `d4ed380` (clone-grep); canonical
  games-theme-engine doc re-read at its standing harvest pin, superbot
  `41899e1` (raw fetch at the pinned SHA — content matches the local link
  index's account).
- **NO outbox entries** — captures only; the sim-kernel head routes through a
  probe first (and must verify the manager's relay hasn't landed by then).
- Landing per README § Landing conventions: branch `seed-superbot-idle-first-batch`
  (seed-* automerge pattern), PR READY, merge-on-green;
  `python3 bootstrap.py check --strict` green before push; heartbeat overwrite as
  the deliberate LAST step.

- **📊 Model:** fable-5 · docs-only (3 captures + index + control + session ceremony)

## 💡 Session idea

**A "lane-velocity prior" field for section stubs** — this batch was scoped
expecting a pre-birth or newborn lane ("probeable once the idle seat exists") and
found 45 merged PRs; the roster row's HEAD pin was already 3 PRs stale at ~90
minutes old. For lanes in declared volume phase, the roster row could carry (or a
capture ritual could compute) a PRs-per-day velocity, so capture authors size the
verify-first budget to the lane's actual speed — a fast lane makes "not yet built"
claims perishable in hours, which changes what is honest to capture at all.

## ⟲ Previous-session review

The PR #68 card (sections re-point REMAINDER) handed off exactly this slice: the
superbot-idle Cross-links entry it shipped ends "the head arms when the lane
pre-registers economy params, watch its heartbeat" — this session watched, and
the condition was ALREADY MET (the lane pre-registered in its PR #12, before the
cross-link even merged). Consumed directly from that card and its heartbeat: the
roster-as-registry re-point (used for the roster row fetch at a pinned SHA), the
ls-remote-then-raw pin recipe, and the claims arbitration lesson (claim first
commit, re-read at HEAD before building — no collision this time; sibling
product-forge seed slice was in flight but on a disjoint section). Friction: none
new — anonymous `api.github.com` stayed unused per the CAPABILITIES wall; every
SHA came from the git transport.

## Handoff → next wake

The ripest head in this section is `idle-economy-sim-kernel` and it is
time-sensitive in BOTH directions: sim-lab idles while the lane is blocked (probe
soon), and the manager's relay may land first (verify sim-lab intake + lane QUEUE
at live HEADs before the battery). superbot-mineverse is now the last stub-empty
roster section. The websites-side selector/gallery head is flagged for whoever
next works `ideas/websites/`. Nothing to babysit.
