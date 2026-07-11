# Session — fleet slice: substrate-kit self-upgrade v1.9.0 → v1.10.0

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~07:15Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Move the vendored kit v1.9.0 → v1.10.0 (released upstream the same day as v1.9.0 —
the exact hop the #120 card's handoff named ripest) and COLLECT the three items the
v1.9.0 slice deferred to this hop: (a) `upgrade --apply-docs` for `.claude/CLAUDE.md`
(v1.9.0's apply-docs dropped the report carve-out section — fixed in v1.10.0),
(b) the `.sessions/README.md` model-attribution doctrine append (v1.9.0 only planted
it into FRESH READMEs — v1.10.0's upgrade appends retroactively), (c) the enabler
re-apply tripwire from the #120 card's 💡 (the carve-out scan is step-granular and
blind to the in-step `--body` edit — manual diff was the only catch). Standing
re-apply duty on BOTH kit-owned workflows as on every hop.

## What this session did

- **Claimed FIRST** as fast-lane PR #122 (control-only, squash `8c536c6` — the
  enabler arming a card-less `upgrade/*` claim as designed). Claims dir re-read at
  HEAD after the merge: no competing claim on the kit surface (sibling claims
  `fix/verdict-006-fanin` + the two harvest re-pin claims all cleared with their
  PRs; #124's verdict-registry claim is a different surface). Inbox re-read FIRST
  at branch time: ORDER 001 (model-attribution standing rule) is the only order,
  already `done=` — this card's `📊 Model:` line satisfies it for this wake too.
  Claim file deleted in this PR per convention.
- **Fetched the v1.10.0 dist via the raw tag path** (the PR #35 wall unchanged —
  `releases/download/` assets and `dist/bootstrap.py.sha256`/`release.json`
  raw-404 at the tag). `substrate-kit@v1.10.0:dist/bootstrap.py`: header v1.10.0,
  self-reported `--version` 1.10.0, 659891 bytes, sha256
  `ba69fc5cf21619cc85e4c733ebe3d9eda8803e678f810fcc39b94d60c2f3b5a4` —
  **byte-identical to BOTH the kit repo's own `main:dist/bootstrap.py` AND
  fleet-manager's vendored copy at its HEAD** (raw fetches this session; the
  first v1.10.0-wave adopter as cross-repo provenance in place of the walled
  release.json, the PR #54 recipe — websites + gba-homebrew still carry the
  v1.9.0 bytes `5518108…`, matching this repo's pre-upgrade dist exactly).
- **Ran the documented flow:** `python3 bootstrap.py.new upgrade`. Result: kept
  5 consumer-edited/host docs (`control/*` ×3, `control/claims/README.md`,
  `project.index.json`), `.ignore`/`.gitattributes` kept (search-hygiene entries
  already present), **`.sessions/README.md` MERGED — the model-attribution
  doctrine appended by the upgrade itself** (deferred item (b) collected
  structurally: retroactive plant under a provenance marker
  `<!-- substrate-kit: model-attribution doctrine … -->`, host content
  byte-preserved, family-level-names-only text exactly as the ORDER 012 doctrine
  prescribes), staged `.substrate/` artifacts regenerated, `kit_version` 1.10.0
  recorded in `substrate.config.json` + `.substrate/state.json`, state schema v1
  (no migration — release marker `breaking=false state_migration=false`).
  `.claude/CLAUDE.md` classified template-improved (the v1.9.0 search-hygiene
  note) → collected via `--apply-docs`, see below.
- **The predicted clobber happened a FIFTH time, detected a fifth time — on BOTH
  workflows:**
  - `substrate-gate.yml`: regen dropped the PR #18 `wake preflight` step; carve-out
    banked the pre-regen gate at `.substrate/backup/substrate-gate.pre-regen-4e09d80d.yml`.
    The v1.10.0 gate template GENUINELY changed (the born-red card-only loophole
    fix: an ADDED in-progress card is now an explicit `session-card-hold` red until
    it flips complete — this PR live-fires that fix, see below — plus
    `--simulate-added-card` on the gate-regen branch), so a verbatim HEAD-restore
    was NOT possible: the step was **RE-APPLIED verbatim into the new template**
    between `setup-python` and the session-card gate step, anchors intact.
    Post-re-apply diff vs HEAD: the ONLY deltas are v1.10.0's own (hold semantics
    + simulation — both tighten-only). Workflow name AND job id `substrate-gate`
    byte-unchanged — the required-check context renamed nothing. PR #36 tripwire
    green (fifth consecutive catch of the class).
  - `auto-merge-enabler.yml`: regen dropped the PR #86 card-status guard step
    (named by the carve-out scan) AND the `Head-ref:` `--body` provenance
    customization (NOT named — step-blind, exactly as on the v1.9.0 hop; the
    manual-diff duty caught it again, for the LAST time — see deferred item (c)).
    Pre-regen bank dedup'd to the existing
    `.substrate/backup/auto-merge-enabler.pre-regen-78295b76.yml` (hash-identical).
    The v1.10.0 enabler template is byte-UNCHANGED vs v1.9.0 (staged copy diff
    empty; live regen identical to the staged copy), so restored via
    `git checkout HEAD -- .github/workflows/auto-merge-enabler.yml` — ships
    **byte-identical to HEAD, both customizations intact** (the #56/#120 recipe;
    `git diff HEAD` on the file is empty).
  - Config survived regen untouched: `automerge.branch_patterns` (all 13
    empirically-observed prefixes), `automerge.required_context: substrate-gate`,
    `claims_dir: control/claims` — verified by direct JSON read post-upgrade.
- **Deferred item (a) collected — `upgrade --apply-docs`:** applied
  `.claude/CLAUDE.md` (template@new, hash re-recorded in state.json): the ONE
  kit-owned addition is the `## Kit machinery — search hygiene` section (exclude
  `bootstrap.py` + `.substrate/` from repo-wide searches); no host content
  deleted. **The v1.10.0 carve-out re-emit fix VERIFIED live:** the rewritten
  `.substrate/upgrade-report.md` KEEPS its `## ⚠️ Gate carve-outs` section with
  all 4 hits marked `[carried from the previous upgrade report]`, a fresh
  `## Carve-out scan` (ran post-restore: 0 found on both workflows), and the new
  `## Applied (--apply-docs)` section — the exact section the v1.9.0 bug dropped
  (websites hand-restored theirs; nothing to hand-restore here).
- **Deferred item (c) collected — enabler-anchor tripwire,**
  `scripts/preflight.py --enabler-anchors` (eighth CHECKS entry, the #120 card's
  💡 consumed): asserts BOTH host anchors live in the kit-owned enabler — the
  card-guard consult `steps.card.outputs.skip == '0'` in the arm-step `if`, and
  `--body "Head-ref: $HEAD_REF"` in the arm command. **REPORT-ONLY (advisory,
  exit 0 unconditionally) on first landing — a deliberate decision:** a
  brand-new check should OBSERVE before it blocks; if the needle bytes or the
  scan are miscalibrated, an advisory misreport costs one log line while a red
  would jam every PR through the gate-wired preflight (the gate runs this
  wrapper). Promotion condition recorded here: flip `check_enabler_anchors` to
  return 1 on missing anchors after the advisory survives one real
  adopt/upgrade regen cycle without a false report (the next kit hop is the
  natural promotion moment). Both directions smoke-proven this session: OK on
  the live file; a doctored copy with both anchors stripped reports
  `DRIFT (advisory) — 2 of 2 … MISSING` and still exits 0.
- **Three version artifacts in sync at v1.10.0** (the #114-probed drift class,
  third consecutive same-day in-sync upgrade):
  1. vendored dist header: `bootstrap.py` line 1 → `v1.10.0` (self-reported
     `--version`: 1.10.0)
  2. config pin: `substrate.config.json` → `"kit_version": "1.10.0"`
  3. heartbeat `kit:` line: `control/status.md` → `kit: v1.10.0 · check: green ·
     engaged: yes` (updated in this PR's final heartbeat commit — same session as
     the upgrade, per the control/README rule)
- **This PR live-fires the v1.10.0 born-red fix on itself:** the PR touches the
  gate workflow, so its ADDED card takes the FULL locked door — the born-red
  first commit held the gate red (`session-card-hold` locally reproduced:
  `check --strict` printed the designed-hold banner) until this close-out flips
  the card `complete`; the enabler's card guard skipped arming on the same
  signal and arms on the flip's `synchronize`.
- **Siblings landed mid-flight** (#123 harvest re-pin + #124 verdict-registry
  claim, exactly the in-flight work the claim-time sweep showed): merged
  origin/main forward-only per the README recipe; one conflict —
  `.substrate/guard-fires.jsonl`, both sides append-only telemetry — resolved as
  an order-preserving line union (200 lines, JSONL re-validated), no facts lost
  either side. Their status.md is the base this slice's heartbeat overwrites.

### Local pre-push runs (real output)

```
$ python3 bootstrap.py --version
substrate-kit 1.10.0

$ python3 bootstrap.py check --strict
check: all checks passed.

$ python3 scripts/preflight.py
preflight: PASS — check_sections (exit 0)
preflight: PASS — check_ideas (exit 0)
preflight: PASS — check_ideas --outbox (exit 0)
preflight: PASS — bootstrap check --strict --status-only (exit 0)
gate-wiring: OK — .github/workflows/substrate-gate.yml non-control lane runs scripts/preflight.py
preflight: PASS — gate-wiring self-check (exit 0)
preflight: PASS — open-work advisory (report-only, never gates) (exit 0)
preflight: PASS — branch-prefix-drift advisory (report-only, never gates) (exit 0)
enabler-anchors: OK — both host customization anchors present in .github/workflows/auto-merge-enabler.yml (card-status guard + Head-ref --body provenance)
preflight: PASS — enabler-anchors advisory (report-only, never gates) (exit 0)
preflight: OK — all 8 checks green
```

(The `gate-wiring: OK` line is the PR #36 tripwire proving the wake-preflight
re-apply landed on the regenerated v1.10.0 gate — fifth consecutive upgrade it has
caught the class; the `enabler-anchors: OK` line is its brand-new enabler sibling
on its first live run. Both runs re-executed green after the heartbeat overwrite,
immediately before push. The locked-door card gate simulated locally too:
`check --strict --require-session-log --session-log` on this card → exit 0 once
complete.)

**📊 Model:** fable-5 · high · kit payload (vendored dist + config/state + staged
artifacts + gate regen/re-apply + enabler verbatim-restore + apply-docs CLAUDE.md +
README doctrine append + preflight eighth check; no idea-tree changes, no proposal —
kit surface only)

## 💡 Session idea

**Promote the enabler-anchor advisory to gating — and seed the byte-needle pattern
upstream.** This hop closed the last manual-diff duty with a tripwire, but
report-only: the promotion condition (one clean regen cycle) is recorded above, and
the next kit hop should flip `check_enabler_anchors` to red-on-missing exactly as
`--gate-wiring` already is — at that point EVERY host customization on both
kit-owned workflows is machine-checked and upgrade slices lose their scariest
manual step. Kit-seam half: the kit's carve-out scan itself could adopt the
byte-needle idea — let a host declare `carveout_needles` in `substrate.config.json`
(file → list of literal strings) and have the scan report a dropped needle even
when it lives INSIDE a kit-owned step, closing the step-blindness class for every
adopter instead of one repo's preflight (cross-link candidate:
`ideas/substrate-kit/README.md`; the upstream card-guard absorption seed
`seed-enabler-card-guard-upstream` is still open and this composes with it).

## ⟲ Previous-session review

PR #121 (`fix/verdict-006-fanin`, squash `d90f9c5`) promised, and this tree
verifies: the `## Sim verdict (2026-07-11)` note on
`ideas/superbot-idle/idle-economy-sim-kernel-2026-07-11.md` present with the
verbatim `recommendation:` quote and the V006=P006 numbering cross ✓; state line
untouched (`sim-ready`, forward-only) ✓; its claim `fix-verdict-006-fanin.md`
cleared (gone at this slice's claim-time re-read) ✓; the six-cross lineage
(V001=P003 … V006=P006) recorded ✓. Its card's honest format note — V006 carries
no `ruling:` field so the note quotes `recommendation:` verbatim instead — is the
right instinct generalized by its own 💡 (verdict-entry field-set pin on the
registry idea, still queued). Its handoff named this hop indirectly ("ripest next
slices: the #119 harvest (in flight …)") and the harvest DID land mid-flight as
#123, forward-merged here exactly per the README recipe it relied on. One delta
its card could not know: its "deferred-verdict queue EMPTY" milestone held for
less than two hours of tree-time before this slice re-verified it at claim time —
the fan-in cadence is now fast enough that queue-empty is a steady state, not a
milestone, which strengthens its 💡's case for a registry over per-card lineage
lists.

## Handoff → next wake

Inbox first, as always. Kit line now v1.10.0 — all three artifacts in sync (dist
header · config pin · heartbeat `kit:` line). The re-apply duty CHANGES SHAPE from
this hop on: gate wake-preflight step (tripwire-covered, `--gate-wiring`) + enabler
card guard AND Head-ref `--body` line (NOW tripwire-covered too —
`--enabler-anchors`, advisory this first cycle; PROMOTE to gating next kit hop per
this card's 💡, then the manual-diff duty is fully retired). v1.10.0 features live:
added in-progress cards are an explicit `session-card-hold` (born-red PRs hold red
until the card flips — this PR proved it on itself), `--simulate-added-card` runs
on gate-regen PRs, apply-docs is safe again. Deferred-items queue from the v1.9.0
hop: EMPTY (3/3 collected here). Queued elsewhere: the #124 sibling's
verdict-registry probe (in flight), the superbot-idle parked heads' un-park events,
`upgrade/apply-docs-v180` remote branch (stale — predates this hop's apply-docs;
prune-candidate at ~72h per the claims convention).
