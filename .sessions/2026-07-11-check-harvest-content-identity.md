# Session — build slice: check_harvest content identity (blob shas + --bullet-drift)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator;
> deferred from contract grooming round 4 as "build slice, not prose")

## What this session did

Extended `scripts/check_harvest.py` (stdlib-only, wake-time-only — CI hermeticity
untouched, the script still joins no preflight/CI and the default run's network
legs are unchanged) with CONTENT identity, closing the lived gap the PR #49 probe
hit: the checker's `HEAD MOVED (docs unchanged)` verdict was filename-set-only, so
the websites backlog's 47/31-line content change was invisible and the PR #52
re-pin rider had to be hand-sized by a clone-level diff.

Three legs, one file (`scripts/check_harvest.py`):

- **CHANGED finding class** — same filename, different blob sha, reported
  distinctly from NEW/DELETED and counted as harvest work (a content-moved
  section can no longer report `docs unchanged`). Live side is free: both
  listing sources already carry blob shas (contents-API `sha` field; `ls-tree`
  object column — `live_docs()` now returns a name→sha map).
- **`--write-pins` → `ideas/<section>/.harvest-pin.json`** — records the per-doc
  blob-sha map AT the pin, run by the harvester in the same session that
  (re-)pins the README; refuses (exit 2) when README pin ≠ live HEAD. The one
  deliberate write mode; the check stays report-only. Backward compatible: no
  record / unparseable record / stale record (pin mismatch) all degrade to the
  old filename-set behavior with a printed note naming the blindness — never a
  crash, never an implied content-freshness.
- **`--bullet-drift`** — pin→HEAD content-delta sizing: one blobless clone per
  moved section fetches the pin commit, `git diff --numstat/--name-status`
  yields per-doc `+N/-M` line deltas (promisor lazy-fetches only changed
  blobs); M-rows feed CHANGED, A/D rows annotate NEW/DELETED with sizes. Works
  without a pin record — sizes re-pin riders (the lane-backlog case) by data.
  Flag-gated OFF by default. Exit codes unchanged: 0 = ran (drift or clean),
  2 = could not run.

Extension note appended to `ideas/fleet/harvest-freshness-checker-2026-07-10.md`
per the #47 lineage precedent (probe report and `historical(#22)` state
untouched) — this builds the middle rung of the probe's own Q2 depth axis
("per-doc content drift via blob shas").

## Verification evidence (live + smoke, verbatim summaries)

**LIVE RUN, default flags, both registered lanes** (2026-07-11, exit 0 —
behavior preserved + the new degrade note):

```
section ideas/superbot/README.md ← menno420/superbot/docs/ideas @ main
  (no pin record .harvest-pin.json — content identity untracked for this section: …)
  HEAD MOVED (docs unchanged): menno420/superbot@main is b0e9ab2 (…), harvest pin is 41899e1
    — pin-bump-only (filename set only — content drift invisible without a pin record
    or --bullet-drift), sizes no harvest work
  summary: 237 indexed · 237 live upstream · 0 new · 0 unmarked · 0 deleted · 0 changed · HEAD moved (docs unchanged)
section ideas/websites/README.md ← menno420/websites/docs/ideas @ main
  (no pin record …)  HEAD MOVED (docs unchanged): … 7da9fbf …, harvest pin is 8c19e93 …
  summary: 5 indexed · 5 live upstream · 0 new · 0 unmarked · 0 deleted · 0 changed · HEAD moved (docs unchanged)
check_harvest: OK — no harvest work across 2 harvested section(s); 2 section(s) HEAD-moved-only (pin-bump, no work)
```

**LIVE RUN, `--bullet-drift`, both lanes** (exit 0) — found REAL drift the old
checker called `docs unchanged`:

```
section ideas/superbot/README.md … HEAD MOVED: b0e9ab2, pin 41899e1
  CHANGED upstream doc (same name, content moved since pin): docs/ideas/fleet-manifest-freshness-checker-2026-07-10.md — +6/-1 lines
  CHANGED upstream doc (same name, content moved since pin): docs/ideas/reconcile-fleet-runtime-digest-2026-07-10.md — +7/-4 lines
  summary: 237 indexed · 237 live upstream · 0 new · 0 unmarked · 0 deleted · 2 changed · HEAD moved
section ideas/websites/README.md … HEAD MOVED: 7da9fbf, pin 8c19e93
  CHANGED upstream doc (same name, content moved since pin): docs/ideas/activity-per-repo-filter-2026-07-09.md — +4/-4 lines
  CHANGED upstream doc (same name, content moved since pin): docs/ideas/backlog.md — +117/-54 lines
  CHANGED upstream doc (same name, content moved since pin): docs/ideas/open-pr-awareness-at-wake-2026-07-10.md — +5/-5 lines
  summary: 5 indexed · 5 live upstream · 0 new · 0 unmarked · 0 deleted · 3 changed · HEAD moved
check_harvest: DRIFT — 7 finding(s) across 2 section(s) (report-only; sizes the next re-harvest slice)
```

Per the slice contract, NO harvest performed here — the drift is captured as
sized next-harvest lines on the heartbeat (websites backlog `+117/-54` lines
since pin `8c19e93` is the headline; the PR #52 re-pin had already consumed the
47/31 the PR #49 probe saw, so this is NEW drift accrued since `8c19e93`).

**SMOKE, planted content change** (record leg, zero extra network): a
`.harvest-pin.json` for websites at README pin `8c19e93` with live blob shas
except `backlog.md` altered to `000…0` →
`CHANGED upstream doc (same name, content moved since pin): docs/ideas/backlog.md — blob 0000000 → e8aeed5`,
summary `… 1 changed · HEAD moved`, exit 0. Fixture deleted after the run.

**SMOKE, degrade paths**: stale record (record pin ≠ README pin) → `STALE record
ignored; degrading to filename-set behavior` note + old behavior, exit 0.
`--write-pins` with pins behind HEAD → per-section refusal (`README pin 41899e1
!= live HEAD b0e9ab2 — a record taken away from the pin would lie …`), exit 2.
`--write-pins --re-badge` combo → refused, exit 2. Unknown arg → usage, exit 2.
`write_pin_record`→`load_pin_record` round-trip exercised directly (record
written under a temp dir, loaded map byte-equal), pass.

Preflight: `python3 scripts/preflight.py` ALL SEVEN checks green +
`python3 bootstrap.py check --strict` exit 0 on the final tree before push.

**📊 Model:** fable-5 · one code file (scripts/check_harvest.py) + idea-file
extension note + card + heartbeat; claim fast-laned first as its own PR and
deleted in this PR.

## 💡 Session idea

The pin record and `--bullet-drift` are two answers to the same question ("what
was true AT the pin?") with opposite cost shapes: the record is O(0) network at
check time but must be written at pin time and can go stale; the git-derived
diff is always honest (git IS the pin-time truth) but costs a clone per moved
section. A future slice could collapse them: `--bullet-drift` could WRITE the
missing pin record as a byproduct whenever README pin == a tree it already
fetched — retrofitting content tracking onto old pins for free, no separate
`--write-pins` sitting needed.

## ⟲ Previous-session review

PR #110 (venture-lab self-landable-merge-path probe, the latest merged card):
adopted from it — claim→re-read→build (claim fast-laned as its own control-only
PR first, claims dir re-read at HEAD after merge; two disjoint sibling probe
claims live: substrate-kit kit-line-self-drift + superbot-idle theme heads),
card complete BEFORE push so the enabler arms at open, and the `📊 Model:`
line per inbox ORDER 001 (re-read FIRST this session; still the only order,
already done). Its handoff named probe surfaces as ripest; this session was
instead a coordinator-dispatched BUILD slice (the grooming-round-4 deferral),
which the handoff couldn't have predicted — no chain break, different queue.
Its staged-vs-live 💡 (check BOTH `.substrate/ci/` and `.github/workflows/`)
wasn't load-bearing here but its verify-first habit was: the live run re-measured
the websites drift fresh rather than trusting the PR #49 number (47/31 then,
+117/-54 now — the number had already moved again).

## Handoff → next wake

The next websites/superbot re-harvest session should: (1) re-pin the README,
(2) run `check_harvest.py --write-pins` in that SAME session — first records
born at a pin, CHANGED goes zero-extra-network from then on. Sized queue for it:
websites backlog `+117/-54` since `8c19e93` + 2 small websites docs (+4/-4,
+5/-5); superbot 2 docs (+6/-1, +7/-4) since `41899e1`. Watch: the two sibling
probe claims (substrate-kit, superbot-idle) were in flight at this session's
dispatch — expect their heartbeat reconciles.
