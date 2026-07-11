# Idea — mechanize the critical-review rubric (the checker backlog) — link index

> **State:** parked(routed — superbot lane build: the class-4 un-anchored-`NN%` staleness-extension one-file slice; every other backlog item is built at N, human-by-design, owner-gated, or carrier-less; probe 2026-07-11)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot@050ba693d507af5b74a8d7348c7c6b612a8b6ad7 · fetched 2026-07-11
> **Grounding:** https://github.com/menno420/superbot-next@81b04bcbbf80dedac0fa26a9295138cea092f513 · fetched 2026-07-11
> *(pin annotation: S pinned via `git ls-remote` + raw per-file reads; N pinned as a blobless-clone HEAD, ls-remote-confirmed — both fresh at probe time, ~19:15Z)*

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-critical-review-checkers-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-critical-review-checkers-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-critical-review-checkers-2026-07-03.md)).

Mechanize the critical-review rubric: several of its ten finding-classes are checkable, so the review isn't purely manual — the 'enforce, don't exhort' arm of the rubric.

## Probe report (v0, 2026-07-11)

> Single-pass full battery (TOP-5 item 3; panel not escalated — process head, reversible
> park, no security/data/spend/public surface). Verify-first read at invocation sites,
> not doc claims: N pinned by blobless clone @ `81b04bc` (ls-remote-confirmed), S pinned
> by ls-remote @ `050ba69` with raw per-file reads. Canonical idea doc byte-identical at
> S HEAD vs the `fd638e3` harvest pin (md5 match) — the capture is fresh; the TREE around
> it is not (corrections below).

**Verified ledger — what actually exists at N HEAD `81b04bc`, per rubric class**
(the ten classes: superbot `docs/planning/rebuild-critical-review-rubric-2026-07-03.md`
@ `050ba69`, mechanization roadmap section; the three v2 classes: N
`docs/planning/rubric-v2-classes-11-12-13.md`, header status `binding — ADOPTED`):

- **Classes 11/12/13 — BUILT and CI-WIRED** (D-0014 mechanics, D-0033 lens adoption):
  `tools/check_cost_posture.py` + `tools/check_metric_cardinality.py` (11),
  `tools/check_data_lifecycle.py` + `sb/kernel/privacy/erasure.py` (12),
  `tools/check_egress.py` (13 — a real `ast`-walking fence, `BANNED_METHODS` covers
  send/reply AND the A-5 raw state mutations: edit/delete/ban/kick/add_roles/…).
  All red-gating in `.github/workflows/ci.yml:50-56` — an 18-checker CI fleet
  (22 `tools/check_*.py` exist; 18 in the CI loop + the lockfile `--regen` leg :75).
- **Class 10 (naming/collision) — BUILT by construction** as designed: K1 namespace
  registry + `tools/check_namespace.py` + `tools/check_symbol_shadowing.py` (CI-wired).
- **Class 9 (UX/lifecycle contract) — the nav golden EXISTS**:
  `tests/unit/navigation_golden/test_navigation_completeness.py` (the A-3 golden inside
  D-0020). Which residual half remains is the SEPARATE TOP-5 mint-time exclusion on
  `rebuild-navigation-completeness-check-2026-07-10.md` — not consumed here.
- **Class 8 (verification hole) — mechanized in a STRONGER form than the ask**:
  `tools/check_verified_live.py` (the V-5 signed-registry gate, Q-0244 evidence rules) +
  the parity discipline (`parity/parity.yml`, `tools/check_parity_depth.py`, the A-16
  door) — every ported feature has a golden oracle, every live feature a signed row.
- **The audit-coverage AST arm (the doc's 2026-07-05 addendum) — SUBSTANTIALLY CLOSED**:
  hole (b) raw-Discord-state-mutation fence is `check_egress.py` (above; the doc's
  "even that one is PENDING (RC-21/Q-D26)" is STALE — RC-21 landed at S11);
  hole (a) mis-declared effect is covered at arm time by `check_atomic_db_only`
  (`sb/kernel/workflow/compile.py:118` — source-token scan of every DB leg of every
  armed scheduler/repair/compensation handler for banned I/O), plus the K7
  `audit_completeness` compile fence. Residual: no UNIVERSAL per-leaf
  effect-vs-writes AST verifier exists as a standalone tool — but the current-bot twin
  shipped (superbot `scripts/check_audit_seam.py`, see the sibling index entry
  `audit-seam-coverage-checker-2026-07-10.md`, historical since 2026-07-06).
- **Classes 1/3/5 — NOT built, and carrier-less**: `SubsystemManifest`
  (`sb/spec/manifest.py:23-33`) declares NO `depends_on` and no risk field (the only
  `depends_on` at N is a SettingSpec ordering field, `sb/spec/settings.py:147`), so
  dep-order (1) and thin-step-vs-risk (3) checkers have nothing declared to read —
  the roadmap's own scope note ("mechanizable against the new repo's declared
  manifests") is still waiting on the carrier. Class 1's premise is additionally
  MOOTED: the S-row build order fully executed (the rebuild is complete and in
  band-by-band live-testing per the lane's own ORDER 001 + testing ledger); residual
  dep-order value shifts to the plugin era (D-0056 hash-pinned joint compilation
  already fences that seam). Class 5 (fragmentation) has only the ADJACENT
  `check_symbol_shadowing.py` (symbol identity, not concept-cluster duplication).
- **Classes 2/6/7 — human by design**, per the roadmap; the rubric is their enforcement.
- **Class 4 (stale/un-anchored claim) — the ONE named-now slice, still UNBUILT at S**:
  `scripts/check_plan_staleness.py` @ `050ba69` carries exactly its three original
  rules (shipped-marker / recon-band / idea-shipped; 127 lines, warn-first, not
  CI-wired) — NO un-anchored-`NN%` rule (grep for `NN%`/percent/anchor: zero rule
  hits). The exact class that misled two sessions remains uncaught.
- **Lens self-application is FENCED BY DESIGN**: Q-0233 froze the rubric as
  owner-directed, "never self-applied" (N rubric-v2 doc header, verbatim) — so
  "mechanize the review pass itself" is not a buildable checker, it is an owner gate.

**Honesty corrections** (stale claims contradicted by this verification):
(1) this repo's TOP-5 framing "enforcement still manual" is OVERBROAD — enforcement of
every mechanized class is CI-wired red at N (`ci.yml:50-56`); what stays manual is the
review PASS (deliberately, Q-0233) and the un-mechanized classes named above.
(2) The canonical doc's audit-coverage addendum understates N: the state-mutation
egress fence is live, not pending (D-0014). (3) The doc's "In the rebuild" checker
list is two-thirds consumed: verification-hole and UX-contract shipped in stronger
forms (verified_live registry + parity door; nav golden), leaving only the
carrier-less 1/3/5.

### The battery

**1. What is this really?** A link-indexed checker BACKLOG, not one checker: mechanize
   the mechanizable classes of superbot's ten-class critical-review rubric (Q-0233,
   PR #1685) — the "enforce, don't exhort" arm — split at capture into a now-arm
   (class-4 staleness extension on the current repo) and a rebuild-arm (manifest-fed
   checkers for classes 1/3/5/8/9 + the audit-coverage AST addendum).
**2. What is the possibility space?** From a one-regex warn-first extension (class 4)
   up to a full review-tooling suite: topological `depends_on` checks, section-depth-
   vs-declared-risk lint, concept-cluster duplication heuristics, done-definition/
   oracle presence assertion, nav goldens, effect-vs-writes AST — and, past the fence,
   a report generator that walks the ten classes per subsystem manifest (owner-gated:
   the lens is never self-applied).
**3. Most advanced capability by the simplest implementation?** The class-4
   un-anchored-`NN%` rule: one more mechanical rule in the existing 127-line
   `check_plan_staleness.py` (flag a plan/ideas-badged doc stating `NN%`/"complete"
   about a fast-moving component with no `as of #PR`/commit anchor) — kills the exact
   class that misled two sessions in one week (the substrate-kit "45–55%" vs ~90–95%
   incident), ~30 warn-first lines.
**4. What breaks it?** (a) Building rubric checkers where no declared carrier exists —
   classes 1/3 read manifest fields (`depends_on`, risk) that N does not declare;
   heuristics over prose are the low-signal trap the roadmap's own scope note names.
   (b) Self-applying the lens — fenced by Q-0233. (c) Class 1's premise decay: build
   order already executed. (d) Duplicate enforcement: re-building at S what N already
   fences (the build-twice-at-cutover cost).
**5. What does it unlock?** The stale-%-claim class dies at the source (every future
   plan/idea doc); plugin-era manifests (D-0056) inherit compile-fence review for
   free; human review attention concentrates on the judgment classes (2/6/7) — the
   rubric's stated goal.
**6. What does it depend on?** S `scripts/check_plan_staleness.py` (exists, warn-first,
   3 rules @ `050ba69`); N's checker fleet + CI (exists, 18 wired); a
   `depends_on`/risk manifest carrier for classes 1/3 (does NOT exist — the real
   blocker for the rebuild-arm residue); Q-0233's owner gate for anything that runs
   the lens itself.
**7. Which lane should build it?** superbot (legacy lane) for the class-4 extension —
   the canonical doc itself routes it "a small current-repo checker PR (any session
   can pick it up)"; superbot-next owns everything else and has already built it,
   deferred it by design, or lacks the declared carrier.
**8. Smallest shippable slice?** One superbot PR: add rule 4 to
   `check_plan_staleness.py` — flag `plan`/`ideas`-badged docs whose body states an
   un-anchored `NN%` or "complete" claim (no `as of #PR`/`@<sha>` within the same
   paragraph), warn-first with the Q-0105 delete-if-noisy header, plus tests riding
   the file's existing shape.

**Recommendation: park** — routed (superbot lane build: the class-4 staleness-extension
one-file slice; the rest of the backlog is built at N `81b04bc`, human-by-design,
owner-gated by Q-0233, or waiting on a manifest carrier that does not exist — nothing
here has a parameter space or corpus for sim-lab to settle, so no proposal).
