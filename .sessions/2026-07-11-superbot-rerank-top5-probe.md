# Session — probe: superbot backlog re-rank (top-5 by decay) + mining-grid-encounters battery v0

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~12:05Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope — the slice plan

The superbot #155 ripe shortlist is fully consumed (SECTION LEDGER on the prior
heartbeat: zero remainders). This slice re-ranks the remaining `captured` superbot
backlog into a fresh standing TOP-5 by decay (owner rulings pending > live build waves >
contracts about to freeze), runs the full battery v0 on the #1 pick, and routes the
verdict. Claim ritual honored: `control/claims/probe-superbot-rerank-top5.md` fast-laned
FIRST as PR #166 (merged `20749db` — substrate-gate green in ~6s, control-only
short-circuit; REST squash after the enabler SKIPPED on `claim/*`), claims dir re-read at
HEAD post-merge (README.md + this claim only). Claim file deleted in this close-out.

## Live grounding (all reads this session, ls-remote-pinned ~12:05Z)

- superbot HEAD `e1090dbcfdf63ffd955399dc2325b9ad1a2f8c8d` — 43rd Q-0107 pass (band
  #1980) records the band as "entirely docs/tooling, zero `disbot/` runtime";
  `docs/current-state.md` has ZERO "encounter" occurrences (build unstarted); inbox
  carries ORDER 001 done (#1977) + ORDER 002 (self-review) `new`.
- fleet-manager HEAD `7b46bd1577b247e41b8ab0458333e6175bbfcb7a` — roster gen #5
  (04:28Z): superbot-next band-5 COMPLETE via #111 (merge `569beea`); superbot-games
  theme-leaks R2 cleared (nouns → swappable DATA tables); superbot-idle STEADY-STATE
  HOLD; superbot-mineverse "deepening well is dry"; 32 enabled triggers; codetool-lab
  tri-model seats STALE-BY-DESIGN. (Roster = the lane registry since 2026-07-11; the
  superbot fleet-manifest is a tombstone.)
- sim-lab HEAD `015e28e6f0c89ffcbd40d5b1375bcc636c0b1e13` — heartbeat 09:56:46Z:
  **PROPOSAL 007 pulled AND finalized as VERDICT 007 — needs-more-evidence / ruling
  REDIRECT** (games-web character-sheet v1.0.1 is hand-authored fiction, not a
  projection of mineverse's real `mining_snapshot.v1`; self-authored phase-2 API
  conflicts with the fm ORDER 012/013 committed-JSON feed). "INTAKE 001–007 all
  finalized as VERDICT 001–007; queue EMPTY at this wake" — so the pull happened
  BEFORE the 11:00Z wake, verdict shipped as sim-lab PRs #25–#27.

## The standing TOP-5 (captured superbot heads, ranked by decay)

1. **`mining-grid-encounters-2026-07-10.md`** — owner ruling already LIVE (Q-0198
   banner @ `e1090db`: build greenlit loot-first, "depth/chance/cooldown … sim-tunable
   at build time" — and no sim has run); sister trigger's defaults sim-pinned by
   VERDICT 001; the shared encounter-resolution engine freezes at whichever build lands
   first. **Probed this slice → sim-ready → PROPOSAL 008.**
2. **`pinned-feed-contract-for-dashboard-json-2026-07-10.md`** — read-only-API fan-in
   converging: fm ORDER 012/013 transport decided (committed-JSON feed), VERDICT 007
   REDIRECT demands projections of real data (sim-lab status @ `015e28e`), PROPOSAL 002's
   stats phase waits on the same surface; the feed-contract shape freezes when the
   providing superbot ORDER lands (verified still unrouted at superbot inbox @
   `e1090db`).
3. **`channel-role-scoped-authority-gap-2026-07-10.md`** — rebuild wave at pace:
   superbot-next band-5 COMPLETE (#111/`569beea`, roster @ `7b46bd1`); the gap names
   BOTH the live bot and the frozen rebuild design — every band that lands raises the
   authority-model retrofit cost.
4. **`usage-limit-aware-routines-2026-07-10.md`** — hard expiry: the EAP wrap-up email
   send window ends 2026-07-14 (control/outbox.md PROPOSAL 005 `depends:`); 32 enabled
   triggers make usage limits a live operational fact (roster @ `7b46bd1`) — a probed
   platform-ask only rides the email if it exists before the send.
5. **`sector-scoped-lean-boot-for-cheap-models-2026-07-10.md`** — fm model-matrix
   findings (fm `docs/findings/model-matrix-2026-07.md`, relayed fleet-wide as this
   repo's inbox ORDER 001) are steering family allocation now; the codetool-lab
   tri-model comparison seats are wound down (roster STALE-BY-DESIGN rows) —
   orientation-tax evidence loses leverage as allocations bake in.

## What this session did

- **Re-ranked the captured superbot backlog** (index scan of `ideas/superbot/README.md`;
  ~190 heads still `captured`) against the four live signals the wake brief named: games
  completion wave (lane repos, roster rows), rebuild pace (superbot-next band-5),
  encounter engine post-VERDICT-001 (defaults pinned, build unstarted), read-only-API
  fan-in (ORDER 012/013 + VERDICT 007). Output: the standing TOP-5 above, mirrored on
  the heartbeat notes.
- **Probed #1** — full battery v0 appended to
  `ideas/superbot/mining-grid-encounters-2026-07-10.md` (single-pass; panel not
  escalated — reversible game surface, VERDICT 002 default). Verify-first: canonical doc
  re-read at live HEAD (Q-0198 banner live, status `ideas`), current-state grep zero
  "encounter" (premise live, build unstarted). Verdict: **sim-ready** — the one open
  dependency is the parameter set Q-0198 explicitly left "sim-tunable at build time".
  State advanced captured → sim-ready in BOTH the file state line and the index-row echo
  (exact echo, the #163/#165 discipline).
- **PROPOSAL 008 appended** to `control/outbox.md` (kit ORDER grammar, sim-ready,
  target sim-lab): the depth/chance/cooldown sweep across roamer/deep-runner/fastmine
  traces, loot-faucet vs `mine_here` earn rate, grinder-vs-honest ratio; done-when
  mirrors VERDICT 001's unsettled-half form and restates its no-live-baseline caveat.
- **Verified sim-lab pulled 007**: evidence block above — pulled and VERDICTED (REDIRECT)
  by 09:56:46Z, queue empty. The VERDICT 007 fan-in (a `## Sim verdict` note on
  `ideas/product-forge/games-web-concept-evidence-pass-2026-07-11.md`) is deliberately
  NOT done here — product-forge section, outside this slice's superbot claim; named in
  the handoff as the ripest next slice.

**📊 Model:** fable-5 · one probe append + state/badge advance + PROPOSAL 008 + card +
heartbeat + claim clear; no lane-file writes (Q-0260), no workflow edits.

## 💡 Session idea

**`claim/*` is a recurring merged prefix that matches NO `automerge.branch_patterns`
entry — the #55 card's drift-tripwire idea now has a live datapoint.** PR #166 (this
slice's claim) merged from `claim/probe-superbot-rerank-top5`; the enabler job SKIPPED
(job-level `if` — no `startsWith` clause for `claim/`), so every claim fast-lane rides
REST-merge fallback instead of self-arming. Two fixes, both cheap: add `claim/*` to
`substrate.config.json::automerge.branch_patterns` + re-run `adopt --wire-enforcement`
(one slice), and/or build the #55 card's prefix-drift advisory (derive recurring merged
prefixes from `git log --merges`, warn on pattern misses) so the next new prefix is
caught at wake time instead of by survey.

## ⟲ Previous-session review

Assigned review target — the wire-automerge-enabler card
(`.sessions/2026-07-11-wire-automerge-enabler.md`, ~PR #55): its live-fire promise
verifies on today's tree AND today's traffic: `.github/workflows/auto-merge-enabler.yml`
is live with the 13 surveyed patterns, and ~100 PRs later the mechanism still ran on this
slice's PR #166 (job present, correctly SKIPPED on the unsurveyed `claim/*` prefix — see
💡; `probe/*` IS patterned, so THIS PR is a fresh live-fire datapoint). Its card's 💡
(branch-prefix drift tripwire) is now evidence-backed rather than hypothetical. Honest
delta: its "empirically complete" 13-prefix survey aged exactly as its own tripwire idea
predicted — new prefixes (`claim/*`) entered the convention after the survey froze.
Also verified (actual newest card, `2026-07-11-emit-exact-state-echo.md` / #165): its
writer-side exact-echo fix is honored by this slice's own hand-advance (state line +
index echo minted identically), and `check_ideas` stayed at the 3 deliberate SIM-VERDICT
legacy advisories on this tree.

## Outcomes

Verdict: **sim-ready** (one recommendation, battery Q1–Q8 complete) — routed as
PROPOSAL 008. Landed per README § Landing conventions (PR READY, never draft; auto-merge
on green; forward-merge on sibling collision). Claim file deleted in this close-out.

## Handoff → next wake

- **VERDICT 007 fan-in is the ripest next slice**: append the `## Sim verdict` section to
  `ideas/product-forge/games-web-concept-evidence-pass-2026-07-11.md` (REDIRECT, cite
  sim-lab outbox @ HEAD + the VERDICT n = PROPOSAL m cross), and mirror the redirect on
  the heartbeat for the manager's :30 sweep — the seam ruling (#87 A/B/C) now has its
  missing value axis.
- The standing TOP-5 above replaces the consumed #155 shortlist; items 2–5 are the probe
  queue in decay order. Item 4 (usage-limit-aware-routines) EXPIRES 2026-07-14 with the
  EAP send window — probe it before the 13th.
- PROPOSAL 008 awaits the sim-lab pull (its failsafe wakes 2-hourly; queue was empty at
  09:56Z, so 008 is next intake).
- This card's 💡 (`claim/*` pattern gap) is a one-line config fix + optional advisory.
