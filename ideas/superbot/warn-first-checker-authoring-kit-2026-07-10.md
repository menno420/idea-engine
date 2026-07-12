# Idea — a warn-first-checker authoring kit (scaffold + shared AST/reachability lib) — link index

> **State:** parked(trigger-misfire — the fourth ledger's "third checker" trigger fired in letter, not substance: neither pending routing (#197 recapture seat at N, #211 class-4 rule at S) is an AST guard, so neither re-duplicates the plumbing this kit factors out; S's 4-member AST-guard family has no queued fifth and sits on the legacy side of the cutover — re-arm when a NEW AST-shaped guard is actually queued at S, or when N's 5-member AST subfamily mints a member that re-implements call-graph/receiver plumbing)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/warn-first-checker-authoring-kit-2026-07-06.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/warn-first-checker-authoring-kit-2026-07-06.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/warn-first-checker-authoring-kit-2026-07-06.md)).

After building two sibling warn-first AST guards in two sessions, extract the shared scaffold + AST/reachability lib so the third checker doesn't re-duplicate the same plumbing.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://github.com/menno420/superbot@1ecc21138fe0a1eb672d03b66bd319164c29d55f · fetched 2026-07-12
> *(pin annotation: S = superbot live HEAD by `git ls-remote` at probe time; tree
> scanned via the standing read-only blobless-clone recipe, files read via raw at
> the pinned SHA. Canonical idea doc byte-identical at S HEAD vs the `fd638e3`
> harvest pin — md5 match, capture fresh.)*
> **Grounding:** https://github.com/menno420/superbot-next@9b80444cfff82839fd70833e4645c51932f54184 · fetched 2026-07-12
> *(pin annotation: N = superbot-next live HEAD by `git ls-remote`; N moved past
> the #211 probe's pin `81b04bc` — the tools/ diff between the pins is exactly
> +`tools/check_money_race.py` (N PR #221, `71af879`): the fleet's NEWEST checker
> was minted standalone, without a kit, in the lane's own pattern.)*

> Single-pass battery (panel not escalated: process head, reversible park, no
> security/data/spend/public surface). TOP-5 #3 on the fourth ledger
> (`control/status.md` @ `42f9642`); the mint-time trigger claim ("third-checker
> trigger FIRED: PR #197 + PR #211 each mint a warn-first checker; probe before
> both re-duplicate plumbing") re-verified at live HEADs per the README battery's
> verify-first discipline — and found HALF-WRONG (corrections below).

**Verified census — every checker family this kit could touch, at live HEADs**

- **S @ `1ecc211`: 47 checker files** — 45 `scripts/check_*.py` +
  `tools/check_amendments.py` + `tools/web_ux/check_web_ux.py` (blobless-clone
  ls-tree). The kit's actual beneficiary family is the **4 warn-first AST
  guards**: `check_audit_seam.py`, `check_deferred_recovery.py`,
  `check_command_reachability.py`, `check_settings_reachability.py` — the
  duplicated plumbing the canonical doc names (`_callee_name` /
  `_receiver_tail` / `_direct_calls` / `_discord_mutation` / allowlist
  load+match / reachability fixpoint) stem-greps at 33/10/21/24 hits across the
  four. Shared plumbing conventions at S: per-checker
  `architecture_rules/*_exceptions.yml` allowlists (audit_seam,
  command_reachability, deferred_recovery, settings_reachability rows all
  exist), advisory CI via `continue-on-error: true` — 5 advisory steps in
  `.github/workflows/code-quality.yml` (:122 stale_claims, :137
  session_slug_unique, :147 amendments, :232 audit_seam, :244
  deferred_recovery) — the reachability pair runs as pytest ratchets
  (`tests/unit/invariants/test_command_reachability.py`,
  `test_settings_reachability.py`), and `check_plan_staleness.py` is warn-first
  NOT CI-wired (its own header: "always exit 0" default, `--strict` opt-in).
  **The kit itself does NOT exist**: no `scripts/lib/astguard.py`, no
  `scripts/new_checker.py` (`scripts/lib/` exists, holds only `owner_alert.py`;
  the scaffold precedent `scripts/new_subsystem.py` exists).
- **N @ `9b80444`: 23 `tools/check_*.py`**, 20 of them red-gating in the
  `set -e` fleet loop at `.github/workflows/ci.yml:46-61` (+ the
  `check_lockfile_fresh --regen` leg :76; `check_compat_frozen`,
  `check_parity_depth`, `check_rotation_due` run outside the loop). N's
  convention is the OPPOSITE of warn-first: hard-gating standalone stdlib
  checkers, no shared lib under `tools/`, no continue-on-error steps in ci.yml.
  Exactly **5 of 23 import `ast`** (`check_egress`, `check_money_race`,
  `check_config_usage`, `check_no_skip`, `check_symbol_shadowing`) — an AST
  subfamily exists but shows only shallow overlap with S's plumbing
  (`check_egress.py:55 _receiver_name` is the lone receiver-resolution twin;
  no call-graph/fixpoint duplication found).
- **idea-engine (this repo): 3 checkers + 1 runner** — `scripts/check_ideas.py`,
  `scripts/check_sections.py`, `scripts/check_harvest.py`, orchestrated by
  `scripts/preflight.py`; warn-first here means advisory WARN classes that never
  affect the exit code (check_ideas.py header). All regex-over-markdown, zero
  AST — **not subsumable** by this kit and not in its scope (the kit is S-path
  scoped: `scripts/lib/`, `code-quality.yml`, `architecture_rules/`).

**Trigger verification — both routings still PENDING, and neither is kit-shaped**

- **#211 half (class-4 `check_plan_staleness` slice at S): pending.**
  `scripts/check_plan_staleness.py` @ `1ecc211` is unchanged — 127 lines, its
  three original rules, zero `NN%`/percent/anchor rule hits; superbot
  `control/inbox.md` @ `1ecc211` carries only ORDER 001 + ORDER 002 (both
  `done`, neither about checkers) — the routing is unlanded AND unrouted.
  **Correction:** this slice does not MINT a checker — it adds a ~30-line regex
  rule to an existing text checker; zero AST, zero new scaffold dance.
- **#197 half (recapture checker seat at N): pending.** N `parity/parity.yml`
  @ `9b80444` has no `recapture:` section (grep: only `source:` :37 and prose
  hits); no recapture checker in `tools/`; N `control/inbox.md` @ `9b80444`
  carries ORDERs 001–013, none names recapture — unlanded AND unrouted.
  **Correction:** that seat is a yml row-shape validator copying N's own
  A-2/D-0005 ledger+checker pattern (23 in-repo exemplars), red-gating per N's
  fleet loop; zero AST, and it lives in the repo whose convention the kit does
  not target.

**1. What is this really?** A refactor-plus-scaffold head for ONE family: S's
   warn-first AST-guard family (4 members). Facet 1, `scripts/lib/astguard.py`:
   factor the collision-robust call-graph/receiver/mutation/allowlist plumbing
   the four guards each re-implement. Facet 2, `scripts/new_checker.py`: stamp
   the authoring dance (signal → triage → allowlist → gate-bites +
   `test_real_tree_is_clean` tests → advisory CI step → promote). For: any S
   session queued to write the NEXT AST guard — and the probe's finding is that
   no such session is queued.
**2. What is the possibility space?** (i) Do nothing — the 4 guards keep their
   duplicated-but-tested plumbing. (ii) Lib only (canonical doc's own "start
   with the lib" ordering) — one tested substrate, 4 thin signal definitions.
   (iii) Lib + scaffold — full kit as captured. (iv) Cross-repo kit — generalize
   for N's 5-member AST subfamily too; collides with N's opposite (red-gating,
   standalone) convention and with the cutover direction of travel. (v) Convention
   doc only — write the dance down (S CLAUDE.md § CodeGraph already carries the
   collision rule), zero code.
**3. What is the most advanced capability reachable by the simplest
   implementation?** The lib half alone, homed at existing `scripts/lib/`:
   import-qualified call resolution (the `self.X`-vs-`module.X` collision fix,
   already solved bespoke in `check_audit_seam`) + the reachability fixpoint +
   the `_discord_mutation` detector + allowlist load/match, with the four
   existing test files (`tests/unit/scripts/test_check_audit_seam.py`,
   `test_check_deferred_recovery.py`,
   `tests/unit/invariants/test_command_reachability.py`,
   `test_settings_reachability.py`) as the behavior-hold ratchet. Correct-once
   collision handling for every future S AST guard.
**4. What breaks it?** (a) The premise: the fired trigger mints ZERO new AST
   guards (corrections above) — the kit would ship to no queued consumer. (b)
   Family growth is over at S: the rubric checker backlog is consumed,
   carrier-less, or built at N (`rebuild-critical-review-checkers` probe @ N
   `81b04bc`), so the fifth AST guard has no named candidate. (c) Cutover decay:
   S is the legacy repo (rebuild complete, band-by-band live testing per N ORDER
   001); a refactor of 4 S-side checkers depreciates with the lane. (d)
   Refactor risk without payoff: touching 4 green guards to de-duplicate
   plumbing buys nothing user-visible and can only introduce drift the ratchets
   must catch. (e) Live counter-evidence: BOTH fleets grew their newest checker
   without a kit at ~1-file cost (N `check_money_race` @ `71af879`; this repo's
   lint-bundle heads, `ideas/fleet/lint-bundle-2026-07-11.md`).
**5. What does it unlock?** If a fifth S AST guard ever gets queued: authoring
   drops from ~1-session craft to ~1-hour fill-in (canonical doc's estimate),
   and the CodeGraph collision class is fixed once instead of per-checker. Also
   a template N could copy IF its AST subfamily starts duplicating call-graph
   plumbing (today it doesn't).
**6. What does it depend on?** (a) A queued AST-shaped consumer at S — ABSENT
   (the one pending S slice is a regex rule on an existing checker). (b) The 4
   guards' test ratchets as the refactor safety net — exist. (c)
   `scripts/lib/` as home — exists. (d) S staying worth investing in — decaying
   (cutover direction). (e) Nothing owner-shaped.
**7. Which lane should build it?** superbot (legacy lane), if ever — the family,
   the allowlist convention, the CI advisory pattern, and the scaffold precedent
   (`new_subsystem.py`) all live there. NOT superbot-next as captured: N's fleet
   is red-gating standalone by convention with no shared-lib pattern. NOT
   sim-lab: no numeric/deterministic question — the kit's payoff is authoring
   time on a family with no queued next member; judgment-only.
**8. What is the smallest shippable slice?** If the re-arm trigger fires:
   lib-only (facet 1) — `scripts/lib/astguard.py` extracting the shared
   primitives from `check_audit_seam.py` (the most complete donor, 33 plumbing
   hits), re-pointing the other three, all four existing test files green
   unchanged; scaffold deferred exactly as the canonical doc orders ("add the
   scaffold when a third checker is queued"). This-repo-side: this probe + park
   (nothing to build here, Q-0260).

**Recommendation: park** — trigger-misfire, corrected: the ledger's fired
"third checker" trigger names two pending routings (#197/#211) that are real
and still pending at live HEADs (S `1ecc211`, N `9b80444`) but NOT kit-shaped —
one is a regex rule added to an existing S text checker, the other a yml
row-shape validator at N under a red-gating convention with 23 in-repo
exemplars; neither re-duplicates the AST/reachability plumbing this kit factors
out, S's 4-member AST-guard family has no queued fifth member, and both fleets
just proved they grow non-AST checkers at ~1-file cost without a kit. Best
implementation found if re-armed: lib-only at S `scripts/lib/astguard.py`,
`check_audit_seam.py` as donor, existing ratchet tests as the hold. Re-arm
trigger (carried into the state line + index badge): a NEW AST-shaped guard
queued at S, or N's AST subfamily minting a member that re-implements
call-graph/receiver plumbing.
