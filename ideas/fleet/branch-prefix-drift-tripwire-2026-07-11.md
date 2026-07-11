# Branch-prefix drift tripwire — keep `automerge.branch_patterns` honest against merged reality

> **State:** park(built-here — scripts/preflight.py --branch-prefix-drift, shipped in this same PR)
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own preflight — built here, see report Q7)

**Origin:** the PR #55 session card 💡 (`.sessions/2026-07-11-wire-automerge-enabler.md`
§ 💡, "Branch-prefix drift tripwire — keep `branch_patterns` honest against reality").
That slice found the kit's default `automerge.branch_patterns: ["claude/*"]` matched
ZERO of this repo's real branch prefixes — the staged auto-merge enabler was a silent
no-op for a whole slice, invisible because nothing checks the config's patterns against
the branch names the repo actually merges. PR #55 fixed it by a one-time hand survey
(13 empirical prefixes from merged PRs #5–#54); this idea makes that survey a standing
wake-time advisory so the next pattern drift is caught at wake, not by archaeology.

**The idea:** a seventh, REPORT-ONLY `CHECKS` entry — `preflight.py
--branch-prefix-drift` (the `--gate-wiring`/`--open-work` self-invoke pattern) — that
derives the repo's real merged-branch prefixes from local `git log --merges` PR-merge
subjects ("Merge pull request #N from owner/branch" → first path segment + `/*`;
slashless names fall back to first hyphen token + `-*`, the `seed-*` precedent),
fnmatches each merged branch against `substrate.config.json::automerge.branch_patterns`,
and prints any RECURRING prefix (≥2 merged branches) that no configured pattern covers.
It NEVER affects the preflight exit code: an unmatched prefix means the enabler quietly
stopped arming that convention's PRs — information for the next config edit, not a
failure of the tree under test; even an unreadable config or a shallow clone prints a
"could not read / nothing to compare" line and still passes.

## Probe report (v0, 2026-07-11)

> **Sequence:** after PR #55 (the enabler wiring this tripwire guards went live there; probed the wake after its card's 💡 sized this exact slice)

**1. What is this really?**
The enabler's missing feedback loop. PR #54 staged the auto-merge enabler with a
default pattern that matched nothing; PR #55 wired it live and fixed the patterns by
hand survey — but the fix is a snapshot, and branch conventions drift (this repo grew
13 prefixes in one day of operation). This check is the survey PR #55 ran once, made
structural: config-vs-reality reconciliation at every wake, every pre-push, and (via
the PR #18 gate↔ritual convergence) every non-control CI run. It is the config-file
dual of the PR #36 gate-wiring tripwire: that one guards a kit-owned FILE against
silent regeneration loss; this one guards a kit-owned CONFIG KEY against silent
reality drift.

**2. What is the possibility space?**
- **Documentation only:** a "re-survey the patterns occasionally" ritual line —
  discipline-only, the exact class `scripts/preflight.py` exists to absorb.
- **Report-only advisory (this slice):** derive prefixes from local merge history,
  report recurring unmatched ones, classify nothing further, always exit 0.
- **Gating check:** rejected — pattern drift is a config-maintenance signal, not a
  defect in the tree under test; a PR that changed nothing must not go red because a
  sibling merged two branches of a new convention (the open-work advisory's
  hermeticity rule, honored by construction).
- **Auto-fix (write the missing pattern into the config):** rejected — the preflight
  is report-only by contract ("it never edits files"), and whether a recurring prefix
  is a convention to bless or a mistake to retire is a judgment call.
- **PR-API-backed survey (head refs of the last N merged PRs):** stronger data (sees
  squash merges), but network-dependent and seat-capability-variant (anonymous
  api.github.com 403s from this seat — PR #55 card) — the wrong dependency for a check
  that rides the hermetic preflight. Local `git log` is the floor that always works.
- **Kit-generic checker:** the enabler + config key are kit-planted, so the fleet-wide
  home is the kit's own `check` seam — cross-link routed to
  `ideas/substrate-kit/README.md` (this file), per the PR #29/#40 precedent; this
  slice is the working local reference implementation.

**3. What is the most advanced capability reachable by the simplest implementation?**
One `CHECKS` entry + one ~70-line stdlib function turns the enabler's worst failure
mode — silently disarmed, nothing red anywhere — into a named advisory line at every
wake, pre-push, and CI run, forever. Replay proof on real history: pointed at the
original `claude/*` default via the smoke-test seam, the check reports SIX recurring
unmatched prefixes (probe/* ×17 · slice/* ×6 · seed-* ×6 · groom/* ×4 · build/* ×3 ·
harvest/* ×3) — it would have caught the PR #54 no-op the first time any session ran
the preflight, one wake instead of one whole slice of archaeology.

**4. What breaks it?**
- **Squash-merge blindness (the honest one):** squash landings write `<title> (#N)`
  subjects with no branch name, and this repo's enabler squashes (`--auto --squash`) —
  so NEW conventions born after the enabler went live surface in `git log --merges`
  only via mid-flight sibling merges and any future merge-commit landings. The 46
  branch names recoverable today all predate-or-span the cutover, so the current
  baseline is rich; the survey thins as squash-only history accumulates, and the check
  degrades honestly ("no PR merge subjects … nothing to compare", still PASS). The
  PR-API leg that would fix this is deliberately out (Q2 hermeticity).
- **Prefix-key heuristic:** first `/` segment, else first `-` token — a future
  convention like `probe-deep-…` groups as `probe-*`, which is a correct pattern to
  suggest but not the only conceivable grouping. Advisory wording says "add the
  pattern OR retire the convention" — the human closes the loop.
- **Config moves:** if the kit renames `automerge.branch_patterns`, the check prints
  the skip line ("no automerge.branch_patterns list configured") forever — loud-ish,
  not red. Same accepted failure shape as the open-work sweep's remote-name drift.
- **Advisory fatigue:** a deliberately-unpatterned convention (e.g. an opt-out prefix
  someone WANTS un-armed) would print at every wake. Mitigation if it ever happens:
  bless it with a pattern anyway (arming is safe — merge stays gated on
  substrate-gate) or carry an ignore list; not built until the case exists.

**5. What does it unlock?**
The enabler stays trustworthy: "matching-prefix READY PRs self-arm" (PR #55's shipped
invariant) is now tripwired against the one config key it silently depends on. Frees
future sessions from re-running the PR #55 hand survey; gives the next
`bootstrap upgrade` a same-session detector if a kit regeneration ever resets the
patterns to a default (the gate-clobber class, config edition); and hands
substrate-kit a live reference implementation for the kit-seam twin (routed by
cross-link, not a proposal — no simulator question in a deterministic string
comparison).

**6. What does it depend on?**
`git` + python3 stdlib (both already required); local merge history (CI's checkout
uses `fetch-depth: 0`, so the gate lane sees the full survey; a shallow seat degrades
to the informational line); `substrate.config.json::automerge.branch_patterns`
(kit v1.8.0, live since PR #54/#55); `scripts/preflight.py` and its gate wiring
(PRs #16/#18, tripwired by #36). Nothing cross-lane, nothing unmerged, no open sim
question.

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It edits this repo's own preflight wrapper,
consumed only by this repo's sessions and gate (Q-0260). The fleet-generic home is the
kit's `check` seam (it plants both the enabler and the config key) — that routing is a
cross-link on `ideas/substrate-kit/README.md`, exactly like the open-work sweep's kit
leg; whether the kit ships it is that lane's call, with this file as the working
reference.

**8. What is the smallest shippable slice?**
One edit at `scripts/preflight.py::CHECKS` (seventh entry, `--branch-prefix-drift`
self-invoked per the `--gate-wiring`/`--open-work` pattern) + one
`check_branch_prefix_drift()` function: read `automerge.branch_patterns`; parse
`git log --merges -n 200 --pretty=%s` PR-merge subjects into branch names; fnmatch
each against the patterns; group the unmatched by prefix key; report groups of ≥2;
wrap every leg so ANY failure prints an advisory line instead of raising; `return 0`
unconditionally. Plus an optional `--config <path>` seam so a planted-violation smoke
test runs against a doctored config copy without touching the tree. Test = the live
run on this repo (46 merged branches, 13 patterns, 0 drift, 1 one-off below the bar)
plus the doctored-config replay (remove `probe/*` → DRIFT ×17 reported; feed the
original `claude/*` default → the 6-prefix report Q3 cites). Cheaper to build than to
route: it ships **in this same PR** per the README § probe-battery shortcut (the
blessed built-here deviation, same shape as #2/#11/#16/#22/#42).

**Recommendation: park(built-here — scripts/preflight.py --branch-prefix-drift, report-only merged-prefix vs automerge.branch_patterns drift advisory, shipped in this PR)** —
rationale: trivial repo-internal PROCESS tooling per the blessed same-PR shortcut — a
deterministic string comparison with no simulator question (proven by its own live run
plus the claude/* replay on real history), nothing routes to sim-lab, and the state
advances to `historical(<this PR>)` on merge.
