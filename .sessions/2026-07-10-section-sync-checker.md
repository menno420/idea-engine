# Session — fleet slice: section-sync-checker captured + probed + BUILT (PR #2)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 ~19:xxZ (worker slice, pre-scoped by the seed card
> `.sessions/2026-07-10-seed.md` §💡; second PR of the repo)

## What this session did

- Claimed `ideas/fleet/` (`claims/probe-fleet-section-sync-checker.md`, flat filename per
  PR #1's guard recipe; cleared at close per `claims/README.md`).
- **Captured + probed (battery v0):** the seed card's idea — manifest-derived section
  sync checker → `ideas/fleet/section-sync-checker-2026-07-10.md`, grounded in a live
  fetch of superbot `docs/eap/fleet-manifest.md` (public raw). Verdict: **park**, with a
  flagged build-here deviation — the four battery labels have no "build directly in this
  repo" outcome; nothing routes to sim-lab (no PROPOSAL appended), the slice was cheaper
  to build than to route, and the state advances to `historical(#2)` on merge (idea
  grammar permits).
- **Built the slice in the same PR:** `scripts/check_sections.py` — stdlib-only,
  report-only, exit 1 on drift, `--manifest FILE` for offline runs, fail-loud (exit 2)
  on unparseable manifest. First entry in `scripts/`.
- Section index updated (`ideas/fleet/README.md`).
- Landing per README § Landing conventions: PR #2 READY (never draft), no review wait,
  merge-on-green; auto-merge/branch-protection evidence recorded in `control/status.md`
  (this session's last content step) + the PR timeline.

### Smoke run (real output, this tree)

```
$ python3 scripts/check_sections.py --manifest <saved-manifest-copy>
check_sections: OK — 10 sections in sync with the manifest
(exit 0)

$ python3 scripts/check_sections.py          # live fetch of the raw manifest URL
check_sections: OK — 10 sections in sync with the manifest
(exit 0)

$ python3 scripts/check_sections.py --manifest <copy> --ideas-dir <tree with websites/ removed, made-up-lane/ added>
MISSING section: ideas/websites/ (active lane in manifest, no directory)
ORPHAN section:  ideas/made-up-lane/ (no active lane row in manifest)
check_sections: DRIFT — 1 missing, 1 orphan
(exit 1)
```

- **📊 Model:** fable-5 · high · docs + one stdlib script

## 💡 Session idea

**Wake-preflight wiring** — now that `scripts/check_sections.py` exists, add a one-line
preflight to the routine-wake ritual (a `notes:` convention or a `bootstrap.py check`
seam): run the checker at every wake so a new/closed lane row is spotted the wake it
appears, not when someone rereads the manifest. Guard recipe: call site =
`scripts/check_sections.py::main` (exit 1 = drift), consume from the per-session ritual
in `control/README.md`; test = the synthetic drift run in this card's smoke block.

## ⟲ Previous-session review

The first-probe card (`.sessions/2026-07-10-first-probe.md`) handed off exactly this slice
("the seed card's section-sync-checker idea as a first `ideas/fleet/` capture") and its
claims-filename guard recipe (flatten `/` to `-`) was consumed as written — zero
re-derivation. One friction found downstream of IT: the battery's four labels don't cover
"build directly in this repo", which this session hit on its first repo-internal PROCESS
idea. Guard recipe: one README line in § The probe battery ("repo-internal tooling whose
smallest slice is trivial may close park(built-here) → historical(PR)") — prose-only fix,
no code anchor; left for a future wake rather than widening this slice.

## Handoff → next wake

Nothing to babysit: no outbox proposal (build-here verdict), claim cleared, checker on
main once #2 merges. Next wake: normal loop — inbox first, then a probe from the superbot
backlog index, or wire the checker into the wake preflight (💡 above), or the
probe-report lint (first-probe card's 💡).
