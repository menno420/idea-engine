# Session — fleet slice: auto-merge enabler arm-at-open race guard (skip while the in-diff card is in-progress)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~04:40Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Guard the auto-merge enabler against its arm-at-open race, per the V005 session's
recommendation: the enabler arms at `opened` and a green PR squash-merges in ~25s,
out-racing every multi-commit plan — PR #64 (opened 02:58:21Z, merged 02:58:45Z, 24s),
PR #80 (opened 04:22:22Z, merged 04:22:47Z, 25s — its close-out had to ride the
follow-up PR #81), same class as #62. The repo's own card convention already encodes
"more commits coming" machine-readably: a session card is ADDED born-red
(`**Status:** in-progress`, `.sessions/README.md`) as the FIRST commit and flipped
`complete` as the LAST. So the fix: the enabler SKIPS arming while the PR's in-diff
`.sessions/*.md` card still says `in-progress`; since it already re-runs on
`synchronize`, the close-out push that flips the card arms it then — "arm only once
the branch is FINAL" (README § Landing conventions), now structural instead of
manual discipline.

## What this session did

- **Claimed FIRST** as its own fast-lane PR #84 (merge `366ab2b`,
  `control/claims/fix-automerge-arm-race-guard.md`); claims dir re-read at HEAD after
  the merge — the scope-seam sibling's pair claims (PR #83: `ideas/product-forge` +
  `ideas/superbot-mineverse`) are disjoint from this fleet/workflow scope. Inbox
  re-read FIRST at origin/main HEAD (`a1b320a`, re-checked at `366ab2b`): ORDER 001
  is the only order and already `done=` (standing model-attribution rule — this
  card's `📊 Model:` line satisfies it for this wake too). Claim cleared in the
  close-out commit per convention.
- **The patch** (`.github/workflows/auto-merge-enabler.yml`, one new step `id: card`
  between the label re-read and the arm step): list the PR's changed files via the
  API; for every non-removed `.sessions/*.md` (README excluded), read the blob at
  the PR head SHA and parse its `**Status:**` badge; any `in-progress` card →
  `skip=1`, log why, exit GREEN without arming. The arm step now requires
  `steps.card.outputs.skip == '0'` alongside the existing conditions. The
  refuse-to-arm required-contexts guard and the sleep-15 fresh label re-read are
  UNTOUCHED; card-less PRs (claims, telemetry, heartbeats) arm at open exactly as
  before. Injection-safe per the PR #64 precedent: PR number + head SHA ride `env:`,
  card paths/contents are fetched and parsed inside Python only (argv-only
  subprocess, URL-quoted path) — no PR-controlled string ever splices into the
  script body. Fail-loud: an unreadable diff/blob fails the step (no arm) rather
  than guessing. KIT-OWNED file — this joins the Head-ref `--body` line in the
  re-apply-after-regen duty (in-file comment marks it; ledger = the extension notes
  on `ideas/fleet/branch-prefix-drift-tripwire-2026-07-11.md`).
- **RIDER — found red mid-slice, fixed to unjam the whole repo** (the exact PR #64
  precedent, next chapter): at ~04:41Z the wake preflight went red on
  `check_sections` (exit 1, `MISSING ideas/codetool-lab-fable5/` +
  `MISSING ideas/lane/`) — fleet-manager's roster flipped to machine generation #5
  at 04:28:10Z and added a SECOND table to the doc (the tool-verification sample,
  headed `| Lane (sample class) |`), and `roster_sections()` parsed every `|` line
  in the file: the second table's header reduced to phantom lane `lane`, and its
  `codetool-lab-fable5 (parked)` sample row carries no wind-down marker in-row.
  This slice's earlier green baseline rode the raw-CDN cache of gen #4 — the same
  cache-window trap as the manifest tombstone. Since the CI gate's non-control lane
  runs the same preflight with a live fetch, every non-control PR repo-wide reds
  from cache expiry onward (including this one). Bounded fix in
  `scripts/check_sections.py::roster_sections`: collect rows strictly between the
  exact `| Lane |` header and the first non-table line after it — later tables are
  never lane rows; fail-loud preserved (header-never-found / empty table still
  raises → exit 2; verified: live roster OK 13 sections, saved gen-5 copy OK,
  empty-roster copy exit 2).
- **Idea capture:** second extension note appended to
  `ideas/fleet/branch-prefix-drift-tripwire-2026-07-11.md` (the enabler
  host-customization ledger the workflow's own comments already point at) — probe
  report and state untouched, state stays `historical(#62)`.
- **Live-fire, both halves, on this very PR** (`pull_request` workflows run from the
  merge ref, so the enabler run on this PR already executes the patched guard —
  the PR #64 precedent): (a) opened READY with THIS card `in-progress` — the enabler
  must run and SKIP arming (`auto_merge` stays null); (b) the close-out push flips
  this card `complete` — the `synchronize` re-run must ARM, and the PR merges on
  green. Outcomes recorded below at close-out, not pre-written (honest-stamps rule).

## Live-fire outcomes (filled at close-out)

- Half (a) — skip while in-progress: PENDING at first push.
- Half (b) — arm on the card-flip synchronize: PENDING at first push.

**📊 Model:** fable-5 · high · fix payload (enabler guard step + arm condition,
idea-file extension note, claim add via PR #84 + clear, card, heartbeat; no new
idea file, no proposal — a deterministic workflow guard has no simulator question)

## 💡 Session idea

**The gate and the enabler now read the same card badge — converge the parse.**
Three surfaces now parse `.sessions/*.md` Status badges independently: the kit
engine (`_BADGE_RE` in `bootstrap.py`), the substrate-gate's diff-scoped card pick,
and now this guard's regex over the raw blob. The kit's grammar module
(`src/engine/grammar.py`, EAP §6.8) exists precisely so writer and enforcer cannot
drift — the enabler guard is a third consumer copy-parsing the badge. Kit-seam
candidate (cross-link shape, `ideas/substrate-kit/README.md`): the kit's adopt
template should ship the card-status guard natively in the enabler it plants (this
repo's step as the working reference), sourcing the badge regex from the one
grammar module — every adopter repo with born-red card conventions has this exact
race, and a host customization on a KIT-OWNED file is re-apply debt until upstream
absorbs it.

## ⟲ Previous-session review

The V005 fan-in pair (PR #80 + close-out PR #81, card
`.sessions/2026-07-11-verdict-005-superbot-fanin.md`) is this slice's origin
evidence, verified against the API rather than taken from the card: PR #80
created 04:22:22Z, merged 04:22:47Z by github-actions[bot] at its NOTE commit —
exactly the 25-second window its card describes; its close-out (heartbeat + card
flip + claim delete) rode PR #81 (merged 04:28:14Z) as a separate control-lane
follow-up. The card's own framing ("two races reconciled forward-only") was honest
about cost: an entire extra PR + reconcile pass per multi-commit session. Its
handoff listed ripest-next slices but not this guard — the coordinator's V005
review named it instead; the card convention (born-red first commit, flip-complete
last) that PR #80's session followed to the letter is precisely what makes the fix
machine-checkable, which is the nicest possible vindication of the convention.

## Handoff → next wake

From this PR's merge onward, a PR that ADDS/MODIFIES an `in-progress` session card
does NOT self-arm at open — push the close-out (card flipped `complete`) and the
`synchronize` re-run arms it; card-less PRs are unchanged. Re-apply duty grew by
one: after any adopt/upgrade regenerates the KIT-OWNED enabler, re-apply BOTH host
customizations (Head-ref `--body` provenance + this card-status guard) — the
in-file comments and the tripwire idea file's extension notes are the ledger. If a
session ever needs the old arm-at-open behavior on a carded PR, flip the card
`complete` before opening (or open card-less and add the card in the close-out) —
do NOT weaken the guard. Follow-up candidates: this card's 💡 (upstream the guard
into the kit's enabler template, badge regex from `grammar.py`); optionally treat
`drafted` cards (kit auto-drafts) as also not-final — deliberately NOT folded in
here (spec was `in-progress` exactly; a modified `drafted` card still holds the
required gate red, so the exposure is only the added-card advisory lane).
