# Session — groom: superbot recheck vs live HEAD (honest re-pin of the 237-entry index)

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 ~09:59Z (worker slice, grooming lane)

## Scope

Groom `ideas/superbot/` against live superbot HEAD: run the full checker suite
(plain + `--bullet-drift`, `--emit-entries` if NEW, `--re-badge`, `--states`),
apply mechanical outcomes only (badge flips with canonical evidence, NEW/DELETED
index updates, pin bump 58040c6 → live), report-only on judgment-laden
divergences (PR #149 precedent). Claim landed first: `control/claims/
groom-superbot-recheck.md` via fast-lane PR #152 (merged 09:57:57Z, squash
`62541f7`); re-read `control/claims/` at HEAD after merge — no competing
superbot claim (websites-round-3 claims only a read-only superbot pin check).

## Findings

(to be filled at close-out: checker outputs, flips with evidence pins,
divergences report-only, ripe-probe shortlist)

**📊 Model:** fable-5

## 💡 Session idea

(to be filled at close-out)

## ⟲ Previous-session review

`.sessions/2026-07-11-superbot-mineverse-first-batch.md` (status `complete`) —
claims verified against this tree: all FIVE mineverse captures it shipped exist
and are indexed (`ideas/superbot-mineverse/`), the claim
`seed-superbot-mineverse-batch-1.md` is cleared from `control/claims/` at HEAD,
and its verification block matches the tree (296 idea files → grammar-clean at
its window). Its method note aged well and is adopted here: re-pin the upstream
repo at fetch time before writing a word — this slice re-runs `git ls-remote`
on menno420/superbot immediately before `--write-pins`, exactly the
verify-first-at-lane-HEAD prior that card carried forward. Its handoff flagged
the mining-projection single-source capture as expiry-aware; that head lives in
`ideas/superbot-mineverse/`, outside this slice's claim, so it is left for its
own lane but noted when weighing the ripe-probe shortlist below.

## Handoff → next wake

(to be filled at close-out)
