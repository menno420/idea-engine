# Session — fleet slice: branch-prefix drift tripwire (captured + probed + built same PR)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~02:28Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Consume the PR #55 card's 💡: nothing checks `substrate.config.json::automerge.branch_patterns`
against the branch names this repo actually merges, so pattern drift silently disarms
the auto-merge enabler (the original kit default `claude/*` matched ZERO real branches
and the staged enabler was a no-op for a whole slice — fixed by hand survey in PR #55).
Make that survey structural: capture the idea (`ideas/fleet/
branch-prefix-drift-tripwire-2026-07-11.md`), probe it through battery v0, and — per
the probe's park(built-here) verdict — build the advisory in this same PR per the
README § probe-battery shortcut.

## What this session did

- **Branched `build/branch-prefix-drift-tripwire`** from origin/main `dd9b1d0` (the
  PR #57 merge). Prefix `build/*` matches the live enabler patterns, so this PR is
  expected to self-arm at open. Inbox verified EMPTY at branch time (re-read at
  origin/main HEAD first, per the ritual).
- **Claim taken FIRST commit** (`control/claims/build-branch-prefix-drift-tripwire.md`,
  ideas/fleet section — `control/claims/` verified README-only at branch time), cleared
  in the close-out commit per the PR #42/#49 precedent.
- **Sibling PR #58 landed at setup time** (hook-born guard-fire telemetry residue,
  merge `1ecceae` — main moved between my hard-sync and my claim commit): merged
  origin/main forward-only per the README recipe. One near-collision on
  `.substrate/guard-fires.jsonl`: this seat's working tree carried TWO uncommitted
  hook-born lines (02:17/02:22Z, from a pre-slice session in this container) while
  PR #58 committed THREE different ones (02:14–02:16Z) — the local residue was stashed
  (not this slice's scope; the telemetry lane pattern owns those appends), the merge
  then applied clean. Open-work sweep at build time also showed sibling
  `groom/contract-grooming-round-4` in flight — scope disjoint (contract docs vs this
  slice's preflight/ideas surface); expect a status.md reconcile if it lands mid-flight.
- **Siblings PR #59 + #60/#61 landed MID-FLIGHT (pre-PR window, after this branch's
  first push):** PR #59 = the predicted contract grooming round 4 (merge `c182d2c`,
  README + control/README + heartbeat), #60/#61 = telemetry residue. Merged
  origin/main forward-only per the README recipe; ONE `control/status.md` conflict
  reconciled keeping both sides' facts — and round 4's heartbeat extension-key
  fold-in DECISION (mode:/BACKPRESSURE:/routine: folded into documented fields) is
  ADOPTED by the reconciled overwrite, this slice's routine facts layered into the
  folded ROUTINE note per the new grammar; PR #59's round facts preserved verbatim,
  this slice's fields win for its own work. Gates re-run green on the merged tree
  before re-push. Zero code overlap: round 4 never touched `scripts/preflight.py`
  or `ideas/fleet/` (its round card SKIPPED this exact head as "kit-generic script
  slice — not contract prose" — built here in parallel, no collision).
- **Captured + probed** `ideas/fleet/branch-prefix-drift-tripwire-2026-07-11.md`
  (origin: PR #55 card 💡; battery v0, single-pass per the panel default — an advisory
  never-red check, no irreversible surface). **Verdict: park(built-here —
  `scripts/preflight.py --branch-prefix-drift`, shipped in this PR)** — trivial
  repo-internal PROCESS tooling with no simulator question; same blessed deviation as
  #2/#11/#16/#22/#42. Honest Q4 finding: squash landings write `<title> (#N)` subjects
  with no branch name, and the enabler itself squashes — the survey's data source
  thins as squash-only history accumulates (46 branch names recoverable today; the
  check degrades to an informational line, never red). See this card's 💡.
- **Built the seventh CHECKS entry**: `check_branch_prefix_drift()` in
  `scripts/preflight.py` — parse local `git log --merges -n 200 --pretty=%s` PR-merge
  subjects into branch names (hermetic, no network; CI's gate checkout is
  `fetch-depth: 0` so the full survey runs there too), fnmatch each against
  `automerge.branch_patterns`, group the unmatched by prefix key (first `/` segment +
  `/*`; slashless → first `-` token + `-*`, the `seed-*` precedent), report groups of
  ≥2. ADVISORY ONLY: exit 0 unconditionally — findings, empty findings, unreadable
  config, missing key, shallow clone, dead git all PASS (the open-work check's
  hermeticity rule, mirrored structurally). An optional `--config <path>` seam exists
  solely so a planted-violation smoke test can run against a doctored config copy
  without touching the tree. Kit-seam routing recorded as a Cross-links row on
  `ideas/substrate-kit/README.md` (the kit plants both the enabler and the config
  key; this repo's entry is the working reference implementation).
- **Not touched:** no proposal (outbox stays at 5, all pulled — a deterministic
  string comparison has no simulator question), `README.md` untouched (the preflight
  check list lives in `scripts/preflight.py::CHECKS` + the wrapper's docstring, not
  the root README), no workflow/config changes.

### Live advisory run (real output, this tree)

```
$ python3 scripts/preflight.py --branch-prefix-drift
branch-prefix-drift: OK — every recurring merged-branch prefix matches a configured pattern (46 merged branches surveyed, 13 patterns, 1 one-off unmatched branch(es) below the recurrence bar)
branch-prefix-drift: OK — advisory sweep complete (report-only, never affects the exit)
exit=0
```

(The one unmatched one-off is `kit-upgrade-v1.7.1` — the PR #35-era pre-convention
branch; correctly below the ≥2 recurrence bar, correctly not reported. NO live drift:
the PR #55 hand survey still matches merged reality.)

### Planted-violation smoke test (real output, doctored config copies in scratchpad — tree untouched)

```
$ python3 scripts/preflight.py --branch-prefix-drift --config <scratch>/doctored-config.json   # probe/* removed, 12 patterns left
branch-prefix-drift: DRIFT (advisory) — 1 recurring merged-branch prefix(es) match NO automerge.branch_patterns entry (the enabler never arms on these — the PR #55 silent-no-op class; add the pattern or retire the convention):
branch-prefix-drift:   probe/*  ×17  (e.g. probe/trading-strategy-kit-upgrade-pin, probe/review-queue-row-auto-check, probe/cross-sectional-momentum-family …)
branch-prefix-drift: OK — advisory sweep complete (report-only, never affects the exit)
exit=0

$ python3 scripts/preflight.py --branch-prefix-drift --config <scratch>/claude-star-config.json   # the original PR #54 default, replayed
branch-prefix-drift: DRIFT (advisory) — 6 recurring merged-branch prefix(es) match NO automerge.branch_patterns entry (the enabler never arms on these — the PR #55 silent-no-op class; add the pattern or retire the convention):
branch-prefix-drift:   probe/*  ×17  (e.g. probe/trading-strategy-kit-upgrade-pin, probe/review-queue-row-auto-check, probe/cross-sectional-momentum-family …)
branch-prefix-drift:   slice/*  ×6  (e.g. slice/probe-open-pr-awareness, slice/preflight-gate-selfcheck, slice/gate-ritual-convergence …)
branch-prefix-drift:   seed-*  ×6  (e.g. seed-substrate-kit-ideas-2026-07-10, seed-gba-homebrew-ideas-2026-07-10, seed-pokemon-mod-lab-ideas-2026-07-10 …)
branch-prefix-drift:   groom/*  ×4  (e.g. groom/contract-round-3, groom/verdict-003-websites-note, groom/sim-verdicts-001-004 …)
branch-prefix-drift:   build/*  ×3  (e.g. build/open-work-preflight-sweep, build/optional-line-lint, build/harvest-freshness-checker)
branch-prefix-drift:   harvest/*  ×3  (e.g. harvest/superbot-reharvest-41899e1, harvest/websites-lane-backlog, harvest/superbot-reharvest-655e0fe)
branch-prefix-drift: OK — advisory sweep complete (report-only, never affects the exit)
exit=0

$ python3 scripts/preflight.py --branch-prefix-drift --config <scratch>/no-automerge-config.json   # {} — key absent
branch-prefix-drift: no automerge.branch_patterns list configured — nothing to compare (enabler not adopted?); advisory only, still PASS
exit=0

$ python3 scripts/preflight.py --branch-prefix-drift --config /nonexistent.json
branch-prefix-drift: could not read nonexistent.json ([Errno 2] No such file or directory: '/nonexistent.json') — advisory only, still PASS
exit=0
```

The `claude/*` replay is the retroactive proof: pointed at the original kit default on
this repo's REAL history, the tripwire reports all six recurring conventions the
enabler was silently ignoring — the PR #54→#55 no-op would have been caught the first
time any session ran the preflight.

### Local pre-push runs (real output)

```
$ python3 scripts/preflight.py
preflight: PASS — check_sections (exit 0)
preflight: PASS — check_ideas (exit 0)
preflight: PASS — check_ideas --outbox (exit 0)
preflight: PASS — bootstrap check --strict --status-only (exit 0)
gate-wiring: OK — .github/workflows/substrate-gate.yml non-control lane runs scripts/preflight.py
preflight: PASS — gate-wiring self-check (exit 0)
preflight: PASS — open-work advisory (report-only, never gates) (exit 0)
preflight: PASS — branch-prefix-drift advisory (report-only, never gates) (exit 0)
preflight: OK — all 7 checks green

$ python3 bootstrap.py check --strict
check: all checks passed.
```

(Both re-run green after the heartbeat overwrite, immediately before push — 284 idea
files conform including the new capture. This card is written before push per the
honest-stamps rule; no merge outcome is claimed here for this slice's own PR.)

**📊 Model:** fable-5 · built-here payload (idea file + probe, seventh CHECKS entry
~110 lines in scripts/preflight.py, fleet index row, substrate-kit cross-link, claim
add+clear, card, heartbeat; no proposal, no workflow/config changes)

## 💡 Session idea

**Squash landings should carry merge provenance — or the history-derived tripwire
starves.** This slice's Q4 blind spot, made precise: the enabler merges with
`gh pr merge --auto --squash`, and GitHub's default squash subject (`<title> (#N)`)
carries NO branch name — so every convention born AFTER the enabler cutover is
invisible to `git log --merges` and the drift survey thins toward "nothing to
compare" as pre-cutover history ages out. Kit-seam candidate (the enabler is
kit-planted — cross-link shape, `ideas/substrate-kit/README.md`): have the enabler's
arm step write the head ref into the squash commit body (one `--body`/subject
convention in the workflow it already owns), or have the kit's own drift check use
PR-API head refs where a token exists and fall back to subjects where not. One line
of provenance at merge time keeps every downstream history-derived check honest
forever; the alternative — each repo re-surveying via API — re-imports the
seat-capability variance this slice deliberately built below.

## ⟲ Previous-session review

PR #57 (apply-docs on repo-navigation-map + AGENT_ORIENTATION; merge `dd9b1d0`) —
claims verified against this tree and the GitHub API, all TRUE: both docs carry the
expanded kit-owned "Documentation root(s)" line (`docs/AGENT_ORIENTATION.md:24`,
`docs/repo-navigation-map.md` § Documentation roots) ✓; `.substrate/upgrade-report.md`
carries `## Applied (--apply-docs)` and no ⚠️ gate carve-out section — the
regeneration-not-append lossiness its card flagged is exactly what the file shows ✓;
NO fourth gate clobber: `git diff 935ebaa..HEAD -- .github/workflows/substrate-gate.yml`
EMPTY (the gate is still byte-identical to the PR #54 bytes, three re-applies later) ✓;
its card honestly claimed no merge outcome pre-push, and the outcome is now recorded
with evidence (API read 02:26Z): `merged: true`, `merged_by: github-actions[bot]`,
created 02:08:25Z → merged 02:13:55Z — the enabler's SECOND consecutive live-fire
(first `slice/*` @ #55, now `upgrade/*`), auto-merge is structural, not a one-off ✓.
One thing its card could not know: its OWN post-final hook residue became sibling
PR #58 (`1ecceae`, telemetry-only, 3 guard-fire lines, landed by the owner session per
the PR #32 precedent) — the same residue class this slice hit again locally and
stashed rather than committed; two occurrences in two sessions says the hook-append
vs clean-tree tension is a real recurring friction, not a one-off (left as an
observation, not a build — the telemetry lane owns the pattern).

## Handoff → next wake

Inbox first, as always (verified empty at `dd9b1d0`/`1ecceae` at branch time). The
preflight now has SEVEN checks; the drift tripwire runs at every wake, pre-push, and
non-control CI lane — if it ever prints DRIFT, the fix is one
`substrate.config.json::automerge.branch_patterns` edit (add the pattern or retire
the convention), never a red build. Live baseline at ship time: 0 drift, 46 merged
branches, 13 patterns. Still queued: grooming round 4 seeds
CONSUMED mid-flight by sibling PR #59 (its round card records the encodes + six
skips; the heartbeat ripest list is reconciled), this card's 💡 (squash merge
provenance → kit seam),
and the PR #57 card's 💡 (apply-docs report regeneration lossiness → kit seam). The
stash holds pre-slice guard-fire residue (`stash list` — telemetry lane pattern, PR
#32/#58 precedent) if a telemetry sweep wants it.
