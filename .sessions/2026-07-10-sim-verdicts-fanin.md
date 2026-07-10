# Session — sim-lab VERDICT 001–004 fan-in grooming (README panel default + idea-file verdict notes)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Applied the consequences of sim-lab's four finalized verdicts to this repo's own
surfaces. All four read raw at pinned sim-lab HEAD
`8713f261c99634156dd6facda03e396b888a9e8a` (ls-remote 23:24Z, `control/outbox.md`);
the sim-lab↔proposal numbering is crossed and recorded here to prevent a future
mis-cite: **sim-lab VERDICT 001 = our PROPOSAL 003** (wild-encounters),
**VERDICT 002 = PROPOSAL 001** (panel-vs-single-pass), **VERDICT 003 = PROPOSAL 002**
(OAuth trust gate), **VERDICT 004 = PROPOSAL 004** (explore-hub XP split).

- **VERDICT 002 (approve — selectively)** → README § The probe battery: the panel-mode
  sentence upgraded from "only for big or contested ideas" to the ruling's concrete
  escalation rule (single-pass default; panel only on repeat-disagreement OR
  irreversible/high-blast-radius surface; always-on rejected), citing the measured
  4.00×/3.05×/1.61× costs and this repo's live datapoint (PR #23's panel run ≈127k lens
  tokens). Matching `## Sim verdict` note on
  `ideas/superbot/idea-probe-brainstorm-simulator-2026-07-10.md`.
- **VERDICT 001 (needs-more-evidence)** → `## Sim verdict` note on
  `ideas/superbot/wild-encounters-activity-spawning-2026-07-10.md`: settled defaults
  threshold=24/debounce=30s/cooldown=900s + guardrails; reward values provisional
  pending the named telemetry.
- **VERDICT 004 (needs-more-evidence)** → `## Sim verdict` note on
  `ideas/superbot/explore-hub-federated-world-2026-07-10.md`: phi=0 rate-only mechanism
  is the INVARIANT; magnitude (t≈0.10, e≈0.20–0.35, BOOST_CAP≈0.25) provisional pending
  PR-2 telemetry; owner-reserved questions untouched.
- **VERDICT 003 (needs-more-evidence, buildable-with-named-changes)** → **DEFERRED**:
  its idea file lives under `ideas/websites/` and a sibling session holds that claim
  this window — no edit made; the ruling (six §5 controls settled as the spike's
  reference set; HOLE-1 stale guild membership + HOLE-2 guilds over-read to fix; §4
  read-only API UNBUILT+UNROUTED = hard blocker; phases 1–2 wait on nothing) is
  recorded in the heartbeat notes for the manager, and the idea-file note is the
  first item for whichever session next holds the websites claim.

State badges untouched everywhere: the idea grammar has no post-verdict state
(`sim-ready → historical(<PR>)` is a BUILD-time move and post-verdict routing is the
manager's), so all three touched ideas stay `sim-ready` with the verdict recorded
note-only. Claimed `claims/groom-sim-verdicts-001-004.md` first (superbot section +
README § probe battery; explicitly NOT websites), deleted in the final push. Preflight
(5 checks) + `python3 bootstrap.py check --strict` green before push; landed per
README § Landing conventions (PR READY, merge-on-green).

**📊 Model:** fable-5 · high · docs-only (README + 3 idea-file appends + heartbeat + card; no code)

## 💡 Session idea

The idea grammar has **no state for "verdict returned"**: a sim-ready idea whose verdict
is finalized reads identically to one still waiting, so the only signal is a prose
`## Sim verdict` section this session had to invent. Candidate grooming-round-3 line:
either bless `## Sim verdict` as an optional forward-only section (lintable byte-form,
like Grounding/Sequence), or extend the state vocabulary with a
`verdict(<needs-more-evidence|approve|reject> @ <sha>)` badge — without it,
`check_ideas --outbox` cannot distinguish "awaiting sim-lab" from "awaiting manager
routing", which is exactly the queue the manager sweeps.

## ⟲ Previous-session review

The encounter-contract probe (PR #39) handed off a clean tree and an honest card: its
23:09Z four-of-five verdict read (heartbeat BACKPRESSURE line) checked out exactly
against this session's own 23:24Z raw read at `8713f26` — same four rulings, no drift —
and its warning that "sim-lab is moving fast; re-verify at write time, don't copy
forward" was followed here (fresh ls-remote pin rather than reusing its `bc6e0fe`).
Its handoff correctly scoped VERDICT 003/004 fan-out as MANAGER work while flagging the
§4 read-only-API blocker for the fan-in note — this session is the repo-local half of
that fan-out (own README + own idea files), not the manager's routing half. One
inherited claim honored: the websites sibling it named in flight still holds
`ideas/websites/`, so the VERDICT 003 note was deferred rather than raced. Friction
recipes inherited and confirmed again: ls-remote + raw reads for sim-lab (tenth
consumer of the recipe), GitHub MCP for this repo's PR ops only.

## Handoff → next wake

Inbox first. The deferred item is the ripest small slice: append the VERDICT 003
`## Sim verdict` note to `ideas/websites/superbot-site-stats-data-story-2026-07-10.md`
once the websites claim clears (ruling summarized above and in the heartbeat — cite
sim-lab `control/outbox.md` @ `8713f26`). Outbox: 5 proposals, four verdict-ed and now
fanned into the tree; only PROPOSAL 005's verdict pending. Then the standing ripest
list (websites-backlog probe heads, check_harvest output-refinement bundle) — and the
💡 above is a natural rider on grooming round 3.
