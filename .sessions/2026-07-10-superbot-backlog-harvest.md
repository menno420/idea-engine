# Session — harvest slice: superbot docs/ideas/ backlog indexed by link into ideas/superbot/

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator under
> continuous-chaining mode; fifth shipped slice of the repo)

## What this session did

Harvested `menno420/superbot` → `docs/ideas/` (the canonical backlog) into
`ideas/superbot/` **by link** per README § Idea file grammar. Enumerated the backlog at
superbot HEAD pinned to `fd638e3c0693687a62093aa6bd75954e238fa58d` (via `git ls-remote` +
a read-only sparse clone — the GitHub REST API is session-scoped to idea-engine and
returned "not enabled for this session" for superbot; the public raw path and git
transport both work). 233 docs indexed (everything except the already-indexed
`idea-probe-brainstorm-simulator-2026-07-10.md`): each entry carries a state line
(`captured` ×190, or the canonical doc's recorded outcome mirrored — `historical(...)`
×41, `parked(...)` ×2), class + target, pinned blob+raw links @ `fd638e3`, and a
one-paragraph gist in this session's own words. Nothing copied — superbot's `docs/ideas/`
stays canonical (Q-0264.8). Section README index updated (all 234 entries listed).

Backlog size note: 233 docs is well past the "very large" line; links are cheap, so
everything was indexed in one pass rather than splitting the slice.

Ripest probe candidates spotted while gisting (for the next probe slices):

- `explore-hub-federated-world-2026-07-10.md` — one design decision homes four gated
  game lanes; owner-directed framing already captured.
- `wild-encounters-activity-spawning-2026-07-10.md` — owner already decided BUILD FIRST
  (superbot Q-0186); probing it produces an outbox proposal with a decided consumer.
- `kit-seed-command-fleet-repo-bootstrap-2026-07-10.md` — sim-lab + three games repos are
  imminent consumers; the ~10-step birth sequence is twice-proven and mechanical.

Preflight: `python3 scripts/check_sections.py` and `python3 bootstrap.py check --strict`
run green before push (see heartbeat). Landing per README § Landing conventions: PR READY,
no review wait, auto-merge armed only once the branch was final (claim deleted in the
final commit per `claims/README.md`).

- **📊 Model:** fable-5 · high · docs-only (233 link-index files + section README +
  control ceremony)

## 💡 Session idea

**Harvest freshness checker** — this index is pinned to superbot `fd638e3`; superbot's
backlog keeps growing (three docs in the enumeration were born the same day). A tiny
checker diffing superbot `docs/ideas/` @ HEAD against `ideas/superbot/` entry canonical
links (same slug-mapping rule as this slice's generator) would turn "is the harvest
current?" from a re-enumeration into a one-command answer — same shape as
`scripts/check_sections.py`, candidate `park(built-here)` slice.

## ⟲ Previous-session review

The contract-grooming card (`.sessions/2026-07-10-contract-grooming.md`) handed off
exactly this slice as the strongest standing candidate ("harvest superbot's docs/ideas/
backlog into ideas/superbot/ by link"); consumed as written — README § Idea file grammar's
link-indexing rule held with zero ambiguity, and the section README's promised reference
index absorbed the 233 lines without a format change. Friction from prior cards: none.
Standing 💡s still unbuilt: wake-preflight wiring; probe-report lint; (new) harvest
freshness checker.

## Handoff → next wake

PROPOSALS 001 + 002 still await sim-lab's pull. The superbot section is now fully
enumerated — probe slices can pick straight from the index (top candidates above) instead
of re-reading superbot. Normal loop: inbox first, then probe the ripest candidate or build
a standing 💡.
