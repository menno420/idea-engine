# Idea — `check_doc_cites.py`: validate source citations in analysis/design docs — link index

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/2c62a099973a2ee384af51e9a33074d9cd411002/.github/workflows/ci.yml@2c62a09 · fetched 2026-07-11
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/2c62a099973a2ee384af51e9a33074d9cd411002/tools/check_amendments.py@2c62a09 · fetched 2026-07-11
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/b2b7fe0ce02a2a68cc18eac5242ab160b7b4330f/docs/ideas/rebuild-design-cite-checker-2026-07-04.md@b2b7fe0 · fetched 2026-07-11
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/b2b7fe0ce02a2a68cc18eac5242ab160b7b4330f/scripts/check_plan_staleness.py@b2b7fe0 · fetched 2026-07-11

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-design-cite-checker-2026-07-04.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-design-cite-checker-2026-07-04.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-design-cite-checker-2026-07-04.md)).

Validate `path.py:NNN` source citations in analysis/design docs: one fabricated cite (a class that doesn't exist) propagated into the design work-list and cost a later session real correction effort.

## Probe report (v0, 2026-07-11)

**1. What is this really?** A ~100-line stdlib linter (`check_doc_cites.py`) mechanizing one proven failure class: fabricated or stale `path:line` source citations in analysis/design docs — the doc-side twin of the rubric's class-4 staleness rule. Verified live 2026-07-11: nothing checks these today in either repo — superbot-next's 22-checker `tools/` fleet and 19-checker red-gating ci.yml loop contain no cite rule; the nearest mechanisms are the kit's dead-relative-link check and `check_amendments.py`'s registry-scoped spec_ref resolution (external `superbot:` corpus roots advisory-skipped).

**2. What is the possibility space?** A rule ladder — (a) cited file exists; (b) plus line-range ≤ file length; (c) plus the cited identifier greps near the cited lines; (d) plus `as of <sha>` anchoring with re-validation at the pinned sha; (e) kit-portable fleet-wide run — crossed with three orthogonal axes: cite grammar (what regex counts as a cite), doc-tree scope, and warn vs red-gate.

**3. What is the most advanced capability reachable by the simplest implementation?** Rules (a)+(b)+(c)-lite in one stdlib regex pass over the doc tree: catches both the motivating fabrication (the nonexistent `WorkflowResult` cited at `disbot/core/contracts.py:48-52` per the canonical idea) and stale line drift — no AST, no config, no dependencies.

**4. What breaks it?** Line numbers drift on every edit, so a red-gating rule (b) on a fast-moving tree makes false reds and gets muted; `path:line`-shaped strings in fenced code blocks and cross-repo cites are false positives; and warn-first is where checkers stall (verified: superbot's `check_plan_staleness.py` is still "Warn-first: not wired into CI" and its class-4 extension remains unbuilt) — so the gating choice is load-bearing, not cosmetic.

**5. What does it unlock?** Design/analysis docs become trustable build inputs: the bug class that already cost a real correction session (a fabricated cite propagated into a design work-list) becomes CI-caught; together with class 4 it fences the whole "doc claims about code" surface; the checker is kit-portable to superbot and other lanes.

**6. What does it depend on?** Nothing new — python3 stdlib plus one line in superbot-next's existing ci.yml checker loop — and two spec decisions the real corpora should settle first: cite grammar and scope/gating.

**7. Which lane should build it?** superbot-next (the declared Target; its `tools/` fleet and ci.yml `set -e` loop are the natural one-file home). The superbot original stays canonical as spec; a superbot-side port is a later copy.

**8. What is the smallest shippable slice?** `tools/check_doc_cites.py` implementing the sim-selected grammar over the sim-selected scope, plus the one-word ci.yml loop addition — the same landing pattern as the class-11/12/13 checkers.

**Recommendation: sim-ready** — unlike TOP-5 item 3 (one named rule, nothing to sweep), this head has a real parameter space (grammar × scope × gating) and two live corpora; one sim pass measuring per-variant catch and false-positive rates settles the spec so the lane build ships red-gating on day one instead of joining the warn-first graveyard. PROPOSAL 010.

## Sim verdict (2026-07-12)

sim-lab **VERDICT 012 · finalized 2026-07-12T01:30:00Z · approve**
(= this repo's PROPOSAL 010 — sim-lab numbers by INTAKE order; sim-lab's own
V009 and V011 were owner-direct intakes, so PROPOSAL 010 → VERDICT 012).
Source pin — honest substitution: the verdict is parked, NOT yet landed in the
sim-lab outbox — [sim-lab `control/outbox.md` @ `b083581`](https://github.com/menno420/sim-lab/blob/b0835812faf7f5a6e4b190a9cc93a11280f099a4/control/outbox.md)
does not yet carry VERDICT 012; the evidence lives on sim-lab
[PR #44](https://github.com/menno420/sim-lab/pull/44) (final head `b083581`,
CI substrate-gate green, parked READY), and the paste-ready VERDICT 012 outbox
entry sits at the end of [`sims/verdict-012-doc-cite-checker-spec/REPORT.md` @ `b083581`](https://github.com/menno420/sim-lab/blob/b083581/sims/verdict-012-doc-cite-checker-spec/REPORT.md)
— that REPORT pin stands in for the usual outbox pin until the outbox landing,
pending PR #44 merge (coordinator step). Run: `python3
sims/verdict-012-doc-cite-checker-spec/cite_checker_sweep.py` — deterministic,
no RNG, 453 self-checks 0 failed, byte-identical re-runs; corpora fetch-on-run
pinned to superbot-next@`2c62a09` and superbot@`b2b7fe0`. The operative ruling
is the `recommendation:` field, quoted: grammar =
`(?<![\w/.-])((?:[\w.-]+/)*[\w.-]+\.(?:py|ts|tsx|yml|yaml)):(\d+)(?:-(\d+))?`
restricted to slash-containing paths, every segment contains a letter, no
`...`, fenced blocks skipped; scope = all tracked `*.md` minus a FOREIGN_ROOTS
config (superbot-next: disbot/, views/, cogs/, utils/, scripts/, ext/),
resolution exact-or-unique-suffix (ambiguous passes); gating = rule (a)
missing-file RED with inline waiver token, rule (b) WARN, rule (c) not
shipped; superbot port warn-first only. Build = single stdlib file + one
ci.yml loop word. Headline numbers at the chosen spec: superbot-next (124 md,
22 cite tokens) 0 rule-a and 0 rule-b flags — 0 FP across both scopes and
fence settings; superbot (1778 md, 5144 cite tokens) best cell 14 TC / 14 FP
rule-a (hence warn-first there), rule-b 24 TC / 21 FP (systematic ≤2-line
EOF-overshoot FP cluster), rule-c sampled 1 TC / 14 FP (~7% precision,
dropped); synthetic planted-corpus recall 1.0 in all 18 cells, frontier cell
P=1.0 R=1.0. Fabrication check: `disbot/core/contracts.py` verified ABSENT
from superbot @ `b2b7fe0` (real analogue
`disbot/services/lifecycle/contracts.py` exists); all 7 surviving cite
instances of the fabricated path are rule-a-flagged by all three grammars,
each survivor a deliberate correction note (e.g.
`docs/analysis/rebuild-discovery/foundations/design/shared-vocabulary.md:53`)
— hence the ruling's inline waiver token. Gate: PASS, EVIDENCE STRENGTH
moderate-strong (COMPARABLE — real checker logic on real pinned corpora,
snapshot-in-time + FOREIGN_ROOTS-circularity disclosed · UNCORRUPTED — 453
self-checks 0 failed, full sweep reported, no RNG · ROBUST — frontier variant
FP-minimal in every cell on both corpora/scopes; rule-c window and extension
set not swept · REPRODUCIBLE — one command, stdlib-only, byte-identical,
SHA-pinned inputs · LIMITS — 0 true catches exist on the target tree today,
so the red gate is proven non-noisy but not yet load-bearing; single-auditor
labels; rule (d) content-drift unmeasured). codex:
[PR #44 comment](https://github.com/menno420/sim-lab/pull/44#issuecomment-4949354456)
(one question — unique-suffix resolution's silent false-negative mode) ·
reply: pending (OA-002 Codex usage-capped). State stays `sim-ready`,
forward-only and untouched — this note, not a new state, is the canonical
verdict marker.
