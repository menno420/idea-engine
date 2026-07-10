# Session — probe slice: capability pair, batched (battery v0 → sim-ready + parked(folded))

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Probe the batched same-space pair flagged by PR #26 —
`ideas/superbot/project-capability-self-awareness-2026-07-10.md` (fresh-harvested) +
`ideas/superbot/session-start-capability-self-probe-2026-07-10.md` (pre-existing) —
through battery v0 with the live-state check FIRST (the PR #25 lesson). Layout chosen:
ONE combined primary report on the self-awareness file + a pointer disposition (no
`## Probe report` heading, so no battery lint applies) on the sibling — the lint binds
the 8-question shape and single recommendation per `## Probe report` block, so the
combined layout is the one that avoids a duplicated battery while staying green.

## What this session did

**Timeliness verified live before probing** — superbot HEAD
`9624c5399f5b1a3da293c07ce930e8b0410d79e4` transport-verified via `git ls-remote
refs/heads/main` at 22:10Z (the PR #27/#29 recipe). Findings at `9624c53` + kit HEAD
`415c37e`:

- both canonical docs byte-identical at their harvest pins vs HEAD (equal sha256) —
  harvest faithful, pins kept;
- `bootstrap.py capabilities` is UNBUILT — kit HEAD is v1.7.1 and its `cli.py`
  subcommand table has no capability-shaped entry (vendored v1.7.0 here agrees);
- the LEDGER half already ships kit-side: `adopt` plants `CAPABILITIES.md.tmpl →
  docs/CAPABILITIES.md` (`src/engine/adopt.py:66`) + the OWNER-ACTION↔ledger xref
  advisory; fleet master ledger (fleet-manager `docs/capabilities.md`) is live with
  2026-07-10 entries; but this repo's own planted append log has ZERO entries —
  neither hand-maintenance nor probing has proven honesty yet;
- superbot itself has NO `docs/CAPABILITIES.md` and NO `bootstrap.py` at HEAD (raw
  404s) — `Target: superbot` is where the canonical DOCS live, not the build home;
- the owner's platform ask is OPEN: EAP wrap-up email is SEND-READY with the ask as
  §(d) item 2, window ends 2026-07-14, only the owner's Part 1 slot remains.

**Probe verdicts (they differ):**

- `project-capability-self-awareness` → **sim-ready**. The load-bearing find is the
  two-plane decomposition: a kit subprocess can probe transport walls but physically
  cannot reach MCP toolsets (model-invoked) — and the founding incident (sim-lab's
  coordinator/worker `create_trigger`/`send_later` split, OA-003) lives entirely in
  that unreachable plane. The genuine evidence question: capabilities are
  session-properties, the ledger is a repo-file — is probe-regenerated capability
  truth honest across seat types, or laundering (Q-0120 class, automated)?
  **PROPOSAL 005** appended (target sim-lab, whose own two seats are the canonical
  reproduction rig; `depends:` substrate-kit as providing lane).
- `session-start-capability-self-probe` → **park**, state `parked(folded — …)`: it IS
  the agent-plane half of the same surface; PROPOSAL 005's done-when names its
  checklist as the agent-plane battery, so a second battery/proposal would
  double-bill sim-lab for one question.

Routing: `ideas/substrate-kit/README.md` § Cross-links gained the pair's entry
(by-link, PR #17 rule — the kit owns the ledger template, the command home, and the
session-start carrier) + a MANAGER note on the heartbeat. Ride-along: one CI-notes
bullet in `control/README.md` — a PR in `mergeable_state: dirty` gets zero check runs,
so auto-merge jams silently; resolve the conflict to unjam.

Verified: `python3 scripts/preflight.py` all 4 checks green; `bootstrap.py check
--strict` green before push. Landing per README § Landing conventions: PR READY,
auto-merge armed only once the branch was final (claim deleted in the close-out
commit). One stamp lesson re-paid: PROPOSAL 005's heading was first written with a
~5-min-future time and corrected to real wall-clock pre-push (the PR #15 rule applies
to every stamp, not just heartbeats).

**📊 Model:** fable-5 · high · docs-only (probe report + pointer disposition + 2
section READMEs + outbox append + control/README bullet + card + heartbeat; no code)

## 💡 Session idea

Battery-lint blind spot: a `**Recommendation:**` line OUTSIDE any `## Probe report`
block is never shape-checked (`check_ideas.py` only scans blocks split on
`PROBE_HEADING_RE`), which this slice leaned on legitimately for the pointer
disposition — but the same hole lets a malformed or duplicate recommendation ride in
prose unlinted. A small pass could hold ANY `**Recommendation:` line file-wide to the
legal vocabulary (warn-first outside probe blocks). Anchors: `RECOMMENDATION_RE` /
`LEGAL_RECOMMENDATION_RE` in `scripts/check_ideas.py`.

## ⟲ Previous-session review

PR #29 (seat-boot harness probe; work `604e8c1`, close-out `7c9b961`, merge `698fd93`)
promised: battery v0 report ending park(routed) on the idea file, the first
`Cross-links` subsection in `ideas/substrate-kit/README.md`, a MANAGER relay note on
the heartbeat, claim cleared pre-merge — ALL verified on this tree: the probe report
parses (this slice's lint run covers it in the 270-file OK), the Cross-links section
exists (this slice appended to it), the heartbeat MANAGER note is present (preserved in
this slice's overwrite), and `claims/` carried only README.md at branch time
(`7c9b961` diffstat shows the -3 claim deletion). Its card's 💡 (cross-link state-echo
lint) is still unbuilt — and this slice GREW its target set: three new state echoes
(two superbot index lines + one kit cross-link line). Its capability recipe
(ls-remote for out-of-scope HEAD SHAs) was reused here verbatim and held. Friction
from its card: none hit. Standing unbuilt 💡s: `--emit-entries`, freshest-wins
one-liner, panel-cost consumption, cross-link state-echo lint, (new) file-wide
recommendation-vocabulary lint.

## Handoff → next wake

Inbox first, as always. PROPOSAL 005 now sits behind INTAKE 002 and PROPOSAL 004 in
sim-lab's queue — nothing to chase from here. Ripest per heartbeat: concept-pick
bringup-pack probe (Sequence-tied to the open pick window, decays like PR #25's head),
second-lane harvest, freshest-wins one-liner. Siblings in flight this window:
gba-homebrew probe + websites seed — re-read the bus and `claims/` before claiming;
expect `mergeable_state: dirty` on landing and use the new control/README bullet.
