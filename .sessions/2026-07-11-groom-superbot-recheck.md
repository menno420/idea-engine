# Session — groom: superbot recheck vs live HEAD (honest re-pin of the 237-entry index)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~09:59–10:15Z (worker slice, grooming lane)

## Scope

Groom `ideas/superbot/` against live superbot HEAD: run the full checker suite
(plain + `--bullet-drift`, `--emit-entries` if NEW, `--re-badge`, `--states`),
apply mechanical outcomes only (badge flips with canonical evidence, NEW/DELETED
index updates, pin bump 58040c6 → live), report-only on judgment-laden
divergences (PR #149 precedent). Claim landed first: `control/claims/
groom-superbot-recheck.md` via fast-lane PR #152 (merged 09:57:57Z, squash
`62541f7`); re-read `control/claims/` at HEAD after merge — no competing
superbot claim (websites-round-3 claims only a read-only superbot pin check).

## Findings — the recheck came back clean (pin-bump-only)

All four checker passes ran green (exit 0) against live superbot HEAD:

- **Plain + `--bullet-drift`** (09:58Z): HEAD MOVED (docs unchanged) —
  superbot@main `e0fd8ef`, pin `58040c6`; 237 indexed · 237 live · 0 new ·
  0 unmarked · 0 deleted · 0 changed — "pin-bump-only (content-verified),
  sizes no harvest work".
- **`--emit-entries`**: not run — no NEW docs to emit.
- **`--re-badge`**: 0 re-badge candidates in the superbot section.
- **`--states`**: 0 state-drift in the superbot section.
- **Badge flips applied: 0. New indexed: 0. Deleted noted: 0.**
- **Divergences — report only: none in `ideas/superbot/`.** (The checker's
  two cross-section findings — websites `backlog.md` blob `f1d93e3` → `0897a6f`
  +101/-27 and the `open-pr-awareness-at-wake` parked→built state-drift — sit
  in `ideas/websites/`, inside the in-flight `harvest/websites-round-3` claim,
  and were deliberately NOT touched here.)

**Re-pin `58040c6` → `227c220`.** superbot HEAD moved TWICE during the slice
(`58040c6` → `e0fd8ef` at first check, → `227c220` at the pre-pin
`git ls-remote` re-verify). Reconciled per the write-pins rule: the checker had
content-verified `e0fd8ef` against the pin record; the `e0fd8ef` → `227c220`
delta was then blob-verified directly (blobless clone at `227c220`,
`git ls-tree` of `docs/ideas/` diffed against `.harvest-pin.json`: all 237
recorded blob shas identical; the only extra live file is the excluded index
`README.md`). README pinned @ `227c220`, then `--write-pins` re-recorded
`ideas/superbot/.harvest-pin.json` (harvest-pin/v1, 237 docs @ `227c220`).
Note: the same `--write-pins` run refused the websites section (README pin
`d862364` != live HEAD `f7f07e7`) — expected and correct, that re-pin belongs
to the websites-round-3 claim; the refusal wrote nothing there (overall exit 2
is that per-section refusal, superbot's record wrote clean).

## Ripe-probe shortlist (top 3 for future slices)

1. `games-theme-engine-website-first-2026-07-10.md` (captured @ `41899e1`) —
   the youngest canonical doc in the index, and the games program is the
   fleet's active wave right now (mineverse contract v1 + games-web phase-2 in
   flight): theme-engine/website-first provisioning choices expire once the
   game lanes freeze their own contracts.
2. `rebuild-websites-cutover-role-2026-07-10.md` (captured @ `fd638e3`) — the
   websites repo is the fastest mover observed this slice (HEAD moved twice
   mid-pass, backlog +101/-27 since its pin); the cutover-role decision should
   be probed before more websites build-out bakes in a de-facto answer.
3. `claude-code-projects-for-the-rebuild-2026-07-10.md` (captured @ `fd638e3`)
   — explicit before-event pressure: picking the rebuild's coordination
   surface only pays before the next rebuild wave spins up lanes, and the EAP
   program context it leans on is live this window.

## Verification (real runs, this tree)

`python3 scripts/check_harvest.py` suite: all passes exit 0 (superbot section
clean; cross-section websites findings report-only, out of claim).
`python3 bootstrap.py check --strict` + `python3 scripts/preflight.py` (all 10
PASS) run green immediately before push, after the heartbeat overwrite.
Telemetry residue: hook-born `.substrate/guard-fires.jsonl` appends left
uncommitted for the telemetry lane per the PR #32/#58/#62 precedent.

**📊 Model:** fable-5 · pin-bump grooming slice (README pin paragraph +
`.harvest-pin.json` + card + claim clear + heartbeat; no entry edits needed —
task-class: bounded index recheck)

## 💡 Session idea

**The checker should re-verify HEAD at pin-write time itself.** This slice hit
the pin-race twice in one pass (58040c6 → e0fd8ef → 227c220): the check ran at
one HEAD, the pin-write gate at another, and the reconcile (re-check + manual
blob diff at the new HEAD) had to be assembled by hand from parts the checker
already owns. A `--re-pin` mode that does ls-remote → blob-verify vs the
existing record → rewrite the README pin sha → write the record, atomically in
one invocation, would turn the raciest step of every grooming slice into one
mechanical command — and the refusal semantics already exist (`--write-pins`'s
"record away from the pin would lie" gate is exactly the right check, just run
one step too late).

## ⟲ Previous-session review

`.sessions/2026-07-11-superbot-mineverse-first-batch.md` (status `complete`) —
claims verified against this tree: all FIVE mineverse captures it shipped exist
and are indexed (`ideas/superbot-mineverse/`), the claim
`seed-superbot-mineverse-batch-1.md` is cleared from `control/claims/` at HEAD,
and its verification block matches the tree (296 idea files → grammar-clean at
its window). Its method note aged well and is adopted here: re-pin the upstream
repo at fetch time before writing a word — this slice re-ran `git ls-remote`
on menno420/superbot immediately before `--write-pins` and caught a second
HEAD move exactly there, vindicating the prior. Its handoff flagged the
mining-projection single-source capture as expiry-aware; that head lives in
`ideas/superbot-mineverse/`, outside this slice's claim, so it was left for
its own lane and weighed (not picked) for the shortlist above.

## Handoff → next wake

The superbot index is honest at `227c220` with a fresh pin record — the next
superbot slice should be a PROBE (shortlist above), not another groom; the
section's drift cost is now near-zero thanks to the blob record. The websites
section is the one carrying real drift (1 CHANGED +101/-27, 1 state-drift
parked→built) and an in-flight claim — check whether `harvest/websites-round-3`
cleared before routing anything there. Remaining-by-design sections stand at
10-of-13 complete (superbot, websites, fleet are the open three).
