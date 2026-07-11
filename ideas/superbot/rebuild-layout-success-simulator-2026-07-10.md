# Idea — the unified layout-success simulator (instruction-driven, deterministic + AI) — link index

> **State:** historical(built at superbot-next — D-0020, 2026-07-08: `sim/` shared runner + oracle registry + `check_sim_gate` CI gate; predates this 2026-07-10 harvest)
> **Class:** process · **Target:** `menno420/superbot-next`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-layout-success-simulator-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-layout-success-simulator-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-layout-success-simulator-2026-07-03.md)).

A unified layout-success simulator scoring any generated hub/menu layout by task success rate: given a natural instruction, does a user model (deterministic + AI) navigate to the correct node?

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/8214200aa0c00dda4156748617c9482dadc4277a/docs/ideas/rebuild-layout-success-simulator-2026-07-03.md@8214200 · fetched 2026-07-11T15:47:52Z
> *(pin annotation: superbot live HEAD S = `8214200aa0c00dda4156748617c9482dadc4277a` by `git ls-remote` 15:47:08Z — S has moved past the capture pin `fd638e3`; the canonical doc still exists at S, status still `ideas` — capture only. Premise verbatim: "One simulator that scores any generated hub/menu layout by **task success rate**"; user models "**Deterministic** — a reproducible heuristic user (semantic label-match + click model)" + "**AI-driven** — an LLM acting as a *naive* user"; metrics "**success** … **path length** (clicks), **wrong turns**"; the #1701 amendment §8 (Q-0235): "four sims in, distinct objective support, and a router eval corpus with independent provenance" — the Goodhart caution against one corpus tuning layouts AND validating the NL router. All four unification targets still exist at S (raw HTTP 200 each, 15:47Z: `tools/sim/help_menu_grouping_sim.py`, `role_menu_layout_sim.py`, `settings_order_sim.py`, `setup_wizard_sim.py`).)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/14e503769202e7ca38609c2063366d8db60bf2f0/docs/decisions.md@14e5037 · fetched 2026-07-11T15:47:52Z
> *(pin annotation: superbot-next live HEAD N = `14e503769202e7ca38609c2063366d8db60bf2f0` by `git ls-remote` 15:47:08Z. **D-0020 "Layer-V V-3: sim runner + oracles + check_sim_gate" · status: decided · date: 2026-07-08** — `sim/` built FRESH to design-spec §2.10: `sim/oracles/` = "the pluggable registry hosting the three NAMED oracles (canonical plan step 11: one shared runner, distinct oracles)" — **navigation** = "Q-0235 instruction-driven engine — deterministic label-match user, task-success-rate/ABSOLUTE-path-hops/wrong-turns, optional naive-user port advisory-only per §8 Q9, corpus minted from graph labels INDEPENDENT of the NL-router eval corpus per the #1701 Goodhart caution" — plus settings_grouping + dense_panel; `sim/run.py --space` = "deterministic records (winner, per-term breakdown, top-5 alternatives, input hashes, seed — bit-for-bit reproducible)"; `sim/apply.py` = "the SOLE machine [A]-writer" of `manifest/layout/<subsystem>.lock.json` with mandatory SimRef provenance; `tools/check_sim_gate.py` "added to ci.yml's green fleet (18th gate)". Provenance line names the prior art directly: "Q-0235 … superbot tools/sim/ (8) + tools/game_sim/ (2) … precedent fleet @7f7628e1". Consumption evidenced: D-0027 "the shipped hub already derived its layout from it"; D-0034 economy hub "layout = the shipped 3/4/1 row arrangement" as declared grammar; sim-gate is one of the six §6 named CI gates ("sim-gate=check_sim_gate", named-gates.yml entry); later band slices routinely close with "ZERO sim-gate/lock churn".)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/14e503769202e7ca38609c2063366d8db60bf2f0/control/status.md@14e5037 · fetched 2026-07-11T15:48:47Z
> *(pin annotation: superbot-next status updated 2026-07-11T15:45Z — ZERO occurrences of "layout" or "simulat" as open workstreams (grep 0/0 over the full file): the sim framework is settled machinery, not an open lane. One ledgered residual on the BUILT system, not on this idea: "NEW CHECKER GAP LEDGERED (@codex question comment 4947003427, final head `47d5cb8`): check_sim_gate does NOT flag VALUE drift on an existing [A] pin — the 3/2/2→3/3/1 reshape passed silently … values hand-amended + baseline regen".)*

> Single-pass battery (panel not escalated: docs/process surface, reversible, no
> security/data/spend/public blast radius — README § probe battery). The briefed
> mandatory verify-first — has any band already ported or consolidated the UX
> sims? — answered YES at N before the battery ran; the battery below prices
> what (if anything) remains.

**1. What is this really?**
A process idea (canonical superbot doc 2026-07-03, PR #1687 Q-0235, amended by
the #1701 final judgment §8) asking superbot-next to consolidate four bespoke
UX-layout sims into ONE instruction-driven layout-success simulator —
deterministic user model primary, AI naive-user for label ambiguity, distinct
objective support, and an NL-router eval corpus with independent provenance.
The verify-first read makes it a DONE idea: superbot-next built exactly this,
fresh to design-spec §2.10, via D-0020 on 2026-07-08 — **two days before this
repo harvested the capture** (2026-07-10). One shared runner + a pluggable
oracle registry IS the consolidation; the navigation oracle IS the
NL-instruction task-success scorer (task-success-rate / path-hops /
wrong-turns — the canonical doc's three metrics, verbatim in spirit and
nearly in name).

**2. What is the possibility space?**
As-built (runner + navigation/settings_grouping/dense_panel oracles + lock
writer + CI gate); the optional naive-user (AI) leg — DESIGNED IN as
"advisory-only per §8 Q9", not yet evidenced ported; wizard-flow objectives
(the `setup_wizard_sim` analog is not among the three named oracles, but
"spaces are REGISTERED by port bands" — the registry is open by design and
band slices add spaces as they land); the telemetry sidecar (seeded-empty by
design — "the sim never runs on invented data"); and checker hygiene on the
built system (the ledgered VALUE-drift gap in `check_sim_gate`, pin above).
Every branch of this space is in-lane follow-through at superbot-next, not a
new build.

**3. Most advanced capability reachable by the simplest implementation?**
Already reached, at the target, by the target: layout choices are
machine-scored, bit-for-bit reproducible, provenance-pinned, and CI-enforced
(sim-gate, one of the six §6 named gates). Nothing cheaper than what exists
could deliver more; the marginal simplest slices left (register a wizard
space when its band lands; port the naive-user advisory leg) are
band-sequenced lane work with their design already written down in §2.10/§8.

**4. What breaks it?**
Nothing left here to break — the idea's own "why now" (centralize BEFORE
layouts freeze, or pay retrofit cost per frozen surface) EXPIRED in the good
direction: hub/menu layouts froze THROUGH the simulator (D-0027/D-0034 —
locks derived from sim records), so the feared retrofit never accrued. What a
revival attempt would break: `sim/apply.py` is deliberately the SOLE
[A]-writer — a second layout-scoring build (here or at sim-lab) would fork
the lock-writing authority the design just unified. The one live crack is in
the BUILT system and is ledgered at N (check_sim_gate VALUE-drift gap, pin
above) — superbot-next's own checker hygiene, not this idea's remit.

**5. What does it unlock?**
Already unlocking: every band's layout freeze rides sim records instead of
taste (the ranking rationale's fear — "every band that freezes a layout
without a scorer raises retrofit cost" — is answered by construction); the
owner-proven value class (#1617 bespoke sim → owner picked Layout B →
shipped #1621, superbot live) is now institutional at the rebuild rather
than bespoke per surface. Marking this head historical also unblocks the
standing TOP-5: item 1 stops occupying the probe queue's top slot.

**6. What does it depend on?**
Going forward: nothing — D-0020 consumed the idea's dependency chain
(design-spec §2.10, Q-0235, the #1701 §8 amendment, the four bespoke sims as
named precedent @7f7628e1). The un-built remainders depend only on
superbot-next's own band sequencing (naive-user leg per §8 Q9; new spaces
per band registration; telemetry on real signal).

**7. Which lane should build it? (honest routing)**
Nobody — it is built, by the right lane, at the right layer. NOT sim-shaped
for sim-lab: the deterministic-vs-AI question this probe was briefed to
carry into a PROPOSAL 009 is already SETTLED BY DESIGN at the target
(deterministic label-match user is the primary engine; the naive-user AI leg
is "advisory-only per §8 Q9"), the Goodhart guardrail is encoded (corpus
"INDEPENDENT of the NL-router eval corpus per the #1701 Goodhart caution"),
and the framework's own records are bit-for-bit reproducible inside the
target's CI — an external sim-lab replay would re-derive what a required
green gate already enforces, and feeding the empty sim-lab queue does not
outrank that honesty (the guard outranks queue-feeding). NO outbox proposal.

**8. Smallest shippable slice?**
None here. The smallest TRUE remainder anywhere is superbot-next closing its
own ledgered `check_sim_gate` VALUE-drift gap (pin above) — one checker
amendment in the lane that owns the checker; flagged on this repo's heartbeat
as a manager-sweep note, not built from an idea-engine seat (Q-0260) and not
a simulation question.

**Recommendation: park** — built-at-target (superbot-next D-0020, 2026-07-08:
`sim/` shared runner + oracle registry + `check_sim_gate` CI gate): the
consolidation this idea asks for landed at the target two days before the
harvest, with the #1701 amendments (distinct oracles, independent corpus, AI
leg advisory-only) encoded as design; per the README's built precedent the
state advances to `historical(...)`, and nothing routes to sim-lab.
