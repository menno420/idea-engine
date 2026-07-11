# Session — probe: wager-flow-map (TOP-5 item 5) — verdict park(routed), no proposal; TOP-5 fully consumed

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~17:30Z (worker slice, coordinator-dispatched)

## Scope

The handoff's named ripest work: probe standing TOP-5 item 5,
`ideas/superbot/wager-flow-map-2026-07-10.md` (the generated game coin-path
tracer), the LAST unconsumed TOP-5 head. Claim landed first via fast-lane PR
#191 (claim file `control/claims/probe-wager-flow-map.md`, branch
`probe/wager-flow-map-claim` per the workprefix+`-claim` convention;
auto-merged in 26s, main `719cc7f`; claims dir re-read at HEAD post-merge —
sole claim — then DELETED at this close-out). Work shipped on branch
`probe/wager-flow-map` (PR number stamped post-open per the never-guess rule /
#181 recipe).

## What this session did

- **Inbox FIRST**: read at wake (origin/main HEAD `ad251c1`, claim later moved
  it to `719cc7f`) — still exactly ORDER 001 (standing per-session rule,
  re-satisfied by this card's 📊 Model line) + ORDER 002 (done by #158,
  Self-review preserved verbatim on the heartbeat). No new orders.
- **Live pin moved MID-SESSION and the probe caught it**: recon ls-remote
  earlier today read superbot HEAD `448584e`; the pre-work re-check (ls-remote
  17:23Z) read `2c7d2de770fee76008b4561ef8165f1d97d78a52`. Every load-bearing
  claim was RE-verified at `2c7d2de` rather than carried from recon:
  - **Nothing is built anywhere** (the #186 invocation-wiring 💡 applied as
    idea-exists-is-not-idea-built): `scripts/wager_flow_map.py`,
    `scripts/coin_flow_map.py`, `scripts/economy_map.py`,
    `docs/economy/coin-flow-map.md`, `docs/wager-flow-map.md` all 404 at S;
    superbot `scripts/` census (~130 files, recon @ `448584e`) has zero
    wager/coin/money/economy/flow/map filenames; superbot-next
    `tools/check_settle_once.py` 404 at its main `e81bc9e`.
  - **Canonical doc byte-identical** at `448584e` and `2c7d2de` (diff clean);
    Grounding pinned at the newer sha, fetched 17:24:25Z.
  - **The seam is alive, the doc's path is not**:
    `disbot/services/game_wager_workflow.py` → 200 at S while the canonical
    doc says `services/` — the doc is one directory move behind its own tree,
    live evidence FOR generated maps over hand-maintained ones.
  - **The faucets have NOT landed**: no encounters cog (`cogs/encounters.py`
    and `disbot/cogs/encounters.py` both 404), zero encounter/loot-faucet hits
    in `docs/current-state.md` @ `2c7d2de` — so the map's cheapest moment
    (before V001/V008 faucet builds mint coins on untraced paths) is still
    open. Encoded as the idea file's `> **Sequence:**` line.
- **Verdict: park(routed)** — state advanced captured → `parked(routed — …)`;
  index bullet re-badged; probe appended forward-only, nothing rewritten.
  **NO PROPOSAL 010**: a tracer is deterministic — build it, run it, read the
  output; no parameter space, no design fork (the canonical doc already chose
  read-only/offline/disposable-guard) — and the one sim-shaped question on
  these coin paths is already PROPOSAL 009's. Honesty guard over
  queue-feeding, the #180/#183/#189 precedent.
- **PROPOSAL 009 state pinned honestly**: PENDING — sim-lab @ its live HEAD
  `e559a37` has not intaken it (its control/status.md 15:16:50Z says "no
  PROPOSAL 009+"; its own VERDICT 009 is an unrelated OWNER-DIRECT
  superbot-next sim). Co-consumable evidence noted in the report preamble:
  the six-instance double-settlement corpus lives on the same coin paths the
  map traces — distinct questions, neither blocks the other, a landed map
  cheapens 009's catch-matrix reconstruction.
- **Heartbeat overwritten LAST**: TOP-5 item 5 marked probed→parked(routed)
  this slice, NO proposal; **TOP-5 now fully consumed (items 1-5)** — re-rank
  due next groom; all preserved blocks carried verbatim (the FOUR-decision
  ≤07-14 ⚑ sitting bundle, the ORDER 002 Self-review section, all standing
  manager sweep flags, outbox-tail=009).
- Claim file deleted at close-out; guard-fires residue rides this PR per
  precedent (#180/#183/#186/#189 carried the same class).

**📊 Model:** fable-5 · probe slice (one idea-file append + state flip + index
re-badge + card + heartbeat + claim clear; NO outbox append, no product code,
no lane-file writes, Q-0260)

## 💡 Session idea

**A canonical doc that names its own trigger should surface it in the badge.**
This idea's canonical doc has carried its routing all along — "build it the
next time a wager/economy path is touched" — and the whole probe verdict
(park, sequenced before the faucets) was latent in that one clause the day
V001 green-lit the first new wager/economy touch. The index badge said only
`captured`. Grooming seed, the exact complement of the #189 card's
name-which-half rule: when a harvest captures an idea whose canonical text
names a trigger event ("build when X", "next time Y"), carry the trigger into
the index badge — then ripeness re-ranking becomes a scan for fired triggers
instead of a re-read of 300 canonical docs.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-probe-audited-score-scaffold.md`
(status `complete`; shipped #189 + heartbeat stamp #190, its claim rode #188 —
the arm-at-open recipe followed again by this slice's claim #191). Spot-checked
against the tree at `719cc7f`: its probe report exists as promised
(audited-score idea file — state `parked(routed — …)` line 3, exactly one
`**Recommendation: park**` line closing the report after Q8); its claim file
is gone from `control/claims/` (only README + this slice's claim were present
post-claim-merge); the status.md heartbeat carries TOP-5 item 4 =
parked(routed) + the NEW RankProvider parity-guard sweep flag, and the
preserved ⚑/Self-review blocks verbatim; the index line 34 re-badge matches
the file state. Its handoff's ripeness call — "item 5 (wager-flow-map) is the
ripest next probe" — VERIFIED against the heartbeat's own TOP-5 ledger (items
1-2 historical, 3 sim-ready+009, 4 parked at #189): item 5 was indeed the last
unconsumed head, confirmed ripest; this slice consumed it. Its 💡
(name-which-half badges) fed this card's complementary 💡. No reconciliation
debt handed to this slice.

## Handoff → next wake

Inbox first, as always. **The standing TOP-5 is now FULLY CONSUMED**: 1
historical (#180), 2 historical (#183), 3 sim-ready + PROPOSAL 009 pending
sim-lab intake (record the verdict via the `## Sim verdict` note grammar when
it lands; numbering by sim-lab INTAKE order, not guaranteed 009), 4
parked(routed) (#189), 5 parked(routed) this slice. **Ripest next slice:
groom/re-rank — mint the next TOP-5** from the remaining superbot heads +
fleet/websites backlog (per Q-0259 websites ranks below superbot), folding in
the six queued 💡 one-liners (README fan-in parse-rule #178, target-lane
ledger-check #180, folio/tree-beats-current-state #183, invocation-wiring
#186, name-which-half #189, and this card's trigger-in-the-badge rule).
Standing watches unchanged (theme-schema half-fired; superbot-idle V006
guardrails; #161 adoption-record sweep; #174 contract-shape attach flag;
effect-arming third-dependent note; check_sim_gate VALUE-drift note). Manager
sweep flags to keep carrying: the NEW map-before-faucets sequencing flag (this
slice), RankProvider parity-guard (#189), Rule 6 registry-roots (#186) — the
latter three are all superbot-lane one-file slices a single routed ORDER could
bundle.
