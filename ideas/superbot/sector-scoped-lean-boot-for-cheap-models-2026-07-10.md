# Sector-scoped lean boot — make cheap models (Sonnet) usable by cutting the orientation tax — link index

> **State:** parked(routed — kit/fm seat-bootstrap design; behind fm model-allocation ruling)
> **Class:** process · **Target:** `menno420/superbot`
> **Sequence:** behind the fm model-allocation ruling (event form — no fm ORDER minted yet; the fm model-matrix census @ `5625e3b` is that ruling's INPUT, not the ruling)

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/sector-scoped-lean-boot-for-cheap-models-2026-06-19.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/sector-scoped-lean-boot-for-cheap-models-2026-06-19.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/sector-scoped-lean-boot-for-cheap-models-2026-06-19.md)).

Owner-directed: a sector-scoped lean boot so cheap models (Sonnet) are usable — the mandatory orientation fills Sonnet's context before it can do anything, wasting an entire weekly usage bucket.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/f76c2094217aa8ee35e4acb9b9bed8695fc7f223/docs/ideas/sector-scoped-lean-boot-for-cheap-models-2026-06-19.md@f76c209 · fetched 2026-07-11T15:12:14Z
> *(pin annotation: superbot live HEAD S = `f76c2094217aa8ee35e4acb9b9bed8695fc7f223` by `git ls-remote` 15:11:56Z — S has moved past the capture pin `fd638e3`; the canonical idea still exists at S, status still `ideas` — "owner-directed (2026-06-19, brainstorm). B1-priority for the next session." Premise lines verbatim: the mandatory boot "(CLAUDE.md + collaboration-model + current-state + journal + plan index + binding docs + CodeGraph) **fills Sonnet's context before it can do anything**, so it compacts on arrival"; "The orientation tax effectively costs an entire weekly bucket every week"; the foundation: 5 planning sectors "S1 bot · S2 btd6 · S3 ai-memory · S4 docs · S5 ops — Q-0137, `repo-sector-map.md`", partitioned "**explicitly to make the repo Sonnet-ready**"; the last mile: packs generated via the "**existing agent-context compiler** (`docs/agent/index.yml` → `docs/agent/generated/*.context.md`) … this is *wiring*, not new infrastructure".)*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/5625e3b4733524b8f34e6051946fbdb9d22e69b5/docs/findings/model-matrix-2026-07.md@5625e3b · fetched 2026-07-11T15:12:31Z
> *(pin annotation: fm live HEAD F = `5625e3b4733524b8f34e6051946fbdb9d22e69b5` by `git ls-remote` 15:11:56Z. The doc is an ATTRIBUTION CENSUS ("Fleet model matrix — 2026-07 (ORDER 010) … Family-level model names ONLY"), NOT an allocation ruling. Load-bearing lines verbatim: Project model config "is **not agent-visible anywhere** — no API, no trigger field, no env var observed"; "**Routine-fired sessions are not pinned to one family**: the same websites trigger produced a sonnet-5 session at 16:01Z and fable-5 sessions at 20:00Z"; CANNOT-establish head: "**Any Project's configured model** — not agent-visible on any surface probed". The briefed allocation-doc paths 404 at F, re-verified this probe 15:16:22Z: `docs/model-matrix.md` 404 · `docs/eap/model-matrix.md` 404 — no allocation document exists on any fetched fm surface.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/5625e3b4733524b8f34e6051946fbdb9d22e69b5/docs/roster.md@5625e3b · fetched 2026-07-11T15:12:32Z
> *(pin annotation: roster Generation #5 (generated-at 2026-07-11T04:28Z) @ F. The one place fleet seats WERE model-pinned by design is closed: all three codetool-lab-* rows (fable5 / opus4.8 / sonnet5) read STALE-BY-DESIGN, trigger **NONE**, "wind-down complete — ready for archive + fresh session".)*

> Single-pass battery (panel not escalated: docs/process surface, reversible, no
> security/data/spend/public blast radius — README § probe battery). sim-lab
> grounding not needed here (nothing sim-shaped survives Q7). Verify-first all
> live this probe (`git ls-remote` 15:11:56Z, pins above): the canonical premise
> is live at S; the fm model-allocation ruling is VERIFIED ABSENT at F (the
> matrix is a census, not a ruling; the two briefed ruling paths 404).

**1. What is this really?**
An owner-directed process idea (canonical superbot doc, 2026-06-19 brainstorm,
B1-priority banner still live at S) fusing TWO distinct things. (a) A boot-cost
problem: the mandatory orientation reading consumes a session's context/usage
bucket before any work happens — the canonical doc's own words: the boot "fills
Sonnet's context before it can do anything, so it compacts on arrival", and "the
orientation tax effectively costs an entire weekly bucket every week". (b) A
model-targeting premise: serve a leaner boot specifically to cheap-model (Sonnet)
seats, unlocking the near-unused separate Sonnet weekly bucket. Half (a) is a
measurable, model-agnostic cost problem; half (b) requires knowing which model a
session runs — and that is where it breaks (Q4).

**2. What is the possibility space?**
Sector-scoped orientation subsets (the canonical design: superbot's 5-sector
partition + per-sector lean packs via its existing agent-context compiler —
"wiring, not new infrastructure"); tiered/task-routed boot (orientation routers
already exist — this repo's own `docs/AGENT_ORIENTATION.md` is exactly a
task-specific reading router); kit-rendered per-seat boot profiles (orientation
surfaces are kit-generated fleet-wide); a measured boot-mass budget — a byte
census per mandatory boot path, published per lane; model-conditional boot
(structurally blocked today, Q4); and the non-design alternative: cap-side fixes
(bigger usage buckets), which is owner-side spend, not fleet design.

**3. Most advanced capability reachable by the simplest implementation?**
Make boot leanness a MEASURED, sector-scoped property. The orientation surfaces
already partition reading by task (superbot's sector map + context compiler;
this repo's orientation router); the simplest slice caps the mandatory path per
sector and publishes byte counts per boot path. Docs-only, zero new machinery —
and it benefits EVERY model family, not just cheap seats: a lean boot is worth
the same bytes to a fable-5 seat as to a sonnet-5 seat; only the bucket
economics differ. The model-conditioning half adds nothing reachable today on
top of this (Q4), so the simplest implementation IS the most advanced capability
actually available.

**4. What breaks it?**
The "for cheap models" half is structurally impossible agent-side TODAY. The fm
matrix pins (above): Project model config is "not agent-visible anywhere — no
API, no trigger field, no env var observed", and routine-fired sessions are not
pinned to one family (the same websites trigger produced a sonnet-5 session at
16:01Z and a fable-5 session at 20:00Z) — so no boot path can know at boot time
that it is serving a cheap model, and no trigger can pin one. A session can
self-report its family AFTER boot (the ORDER 001/Q-0262 card rule), which is
attribution, not conditioning. Also: no fm model-allocation ruling exists at F
(verified absent — the matrix is an attribution census; the briefed allocation
paths 404), so there is no target seat-set to design a cheap-model boot FOR; and
the codetool tri-model experiment — the one place seats WERE model-pinned by
design — is wound down per roster gen #5 (all three lanes STALE-BY-DESIGN,
trigger NONE).

**5. What does it unlock?**
Cheap seats become viable fleet-wide — the owner-felt problem is usage-bucket
economics (the near-unused Sonnet bucket vs the exhausted all-models bucket).
The orientation tax becomes real dollars post-EAP: the window wraps 2026-07-14,
so every byte of mandatory boot fires on PAID usage after that — this couples to
the post-EAP routine-posture decision already ⚑-bundled on this repo's heartbeat
(decision 4 of the ≤07-14 sitting). And a boot-mass census hands the fm
allocation decision its missing COST input: today the allocation question has an
attribution census but no per-lane price-of-orientation number.

**6. What does it depend on?**
The fm model-allocation ruling — VERIFIED ABSENT at F this probe (the census
header + the CANNOT-establish line pinned above; `docs/model-matrix.md` and
`docs/eap/model-matrix.md` both 404 at F). Kit render machinery — orientation
surfaces are kit-generated, so per-seat/per-sector boot profiles are a
substrate-kit rendering feature. And superbot's own boot surface at S: the
sector map (Q-0137) + the agent-context compiler the canonical doc names as the
already-built foundation.

**7. Which lane should build it? (honest routing)**
Split by ownership: substrate-kit owns fleet-wide boot rendering (per-sector /
per-seat packs are a kit render feature); superbot owns its own sector map and
context compiler (the canonical doc is B1-priority IN superbot's own backlog —
its lane builds its own lean packs); fleet-manager owns seat/model allocation
(the ruling this idea waits behind). NOT sim-shaped: boot mass is directly
countable on real repos — a byte census needs no simulation — and the
load-bearing unknown is an owner/fm allocation decision, not a simulatable
dynamic. So NO outbox proposal, and nothing for idea-engine to build.

**8. Smallest shippable slice?**
A per-lane byte census of the mandatory boot path — the orientation file sizes
along each repo's required reading order — published as a kit/fm finding. One
doc, no code, directly countable from public raw fetches. It turns "orientation
tax" from anecdote into a number, gives every lane a boot-mass budget baseline,
and hands the fm allocation decision its missing cost input (Q5) without waiting
for the ruling itself.

**Recommendation: park** — routed (kit/fm seat-bootstrap design): the
model-conditioning premise is structurally impossible agent-side today (fm
matrix pins — Project model config not agent-visible, fired sessions not
family-pinned); the sector-scoped remainder is kit/fm design work sequenced
behind the still-baking fm model-allocation ruling (verified absent at F); and
nothing here is sim-shaped — boot mass is directly measurable on real repos. NO
outbox proposal.
