# Session — probe slice: seat-boot verification harness (battery v0 → park(routed))

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Probe `ideas/superbot/seat-boot-verification-harness-2026-07-10.md` (harvested in PR #26)
through battery v0, with a live-state timeliness check FIRST (the PR #25 lesson: a probe
against a stale window wastes the slice). Ship as one merged-on-green PR.

## What this session did

**Timeliness verified live before probing** — superbot HEAD `afbaea73cda998d0f31994efdd4cf959b2f38505`
obtained transport-verified via `git ls-remote refs/heads/main` (recipe note: the MCP is
walled to this repo and anonymous api.github.com 403s through the proxy, but `git
ls-remote` against the public clone URL works — the cheap out-of-scope HEAD-SHA source).
Findings at `afbaea7`:

- the runbook §5 boot-verification log (`docs/planning/round3-dispatch-runbook-2026-07-10.md`)
  now carries **7** hand-composed rows — the repetition the idea observed at 4 grew by 3
  since harvest (Simulator, Trading, Builder rows added);
- `scripts/check_seat.py` is unbuilt (raw 404 + a superbot `scripts/` tree listing);
- the canonical idea doc is **byte-identical** at harvest pin `655e0fe` and HEAD
  `afbaea7` (equal sha256) — the harvest gist is still faithful;
- the fleet manifest @ `afbaea7` shows all 3 games lanes (games-plugins, pokemon-mod-lab,
  gba-homebrew) seat-unbooted with pending self-arm ORDERs — the ≥3 incoming boots
  (Q-0259 r.5) are still ahead. Window open, probe proceeded.

**Probe verdict: `park`** (state → `parked(routed — …)`): no simulator question — a
deterministic transport-checking harness is proven by one golden replay against a
recorded §5 row, not reproduced simulation — and the build, though real and timely,
belongs to lanes this repo does not write. Q7 split: **substrate-kit owns the parsing
core** (it owns the heartbeat grammar; the decisive Q4 risk is a second parser copy
silently rotting — the drift class its own `kit-line-self-drift` / `host-checkers-one-gate`
captures already track), **superbot hosts the thin operator wrapper** (registry-dump
match + §5 row emission, per the canonical doc), **fleet-manager is the standing
co-consumer** (sweeps + ORDER 009 roster convergence). Routing shipped: `Cross-links`
subsection added to `ideas/substrate-kit/README.md` (by-link, PR #17 rule) + a MANAGER
relay note on the heartbeat. **No outbox proposal** (earn-rate bar upheld: nothing for
sim-lab here).

Verified: `python3 scripts/preflight.py` all 4 checks green; `bootstrap.py check
--strict` green before push. Landing per README § Landing conventions: PR READY,
auto-merge armed only once the branch was final (claim deleted in the close-out commit).

**📊 Model:** fable-5 · high · docs-only (probe report + 2 section READMEs + card +
heartbeat; no code)

## 💡 Session idea

Cross-link state-echo lint: this slice's `ideas/substrate-kit/README.md` cross-link line
echoes the linked idea's state (`parked(routed)`), and the superbot index line does too —
state echoes in OTHER files are exactly the annotation class that rots when a state
advances later. `check_ideas.py` already parses every idea's state line; a small pass
could verify that any `— <state> ·` annotation on an index/cross-link line matches the
linked file's actual current state (warn-first). Anchors: `first_state()` +
`lint_file()` in `scripts/check_ideas.py`; test target: a mismatched index line under
`ideas/`.

## ⟲ Previous-session review

PR #26 (drift re-harvest; commits `6f38749` work + `7602fca` close-out, merge `fdf1a5a`)
promised 2 upstream docs link-indexed @ `655e0fe` with Grounding+fetch-time lines, the
UNMARKED entry reformatted, and the pin bumped — all verified on this tree: both files
present and grammar-clean (this slice probed one of them), pin line parses (PR #22's
`check_harvest.py` PIN_RE shape), claim file deleted before merge (`7602fca` diffstat).
Its card's probe-ready note on this very idea predicted "from here it probes to an
outbox proposal / manager relay, not a local build" — half right, confirmed on the
relay half: manager relay yes, but NO sim proposal (the probe found no simulator
question; the outbox earn-rate bar held). Its byte-level harvest fidelity was
independently confirmed here (canonical doc sha256 identical at `655e0fe` vs `afbaea7`).
Friction from its card: none hit. Standing unbuilt 💡s: `--emit-entries`, optional-line
lint coverage, freshest-wins one-liner, panel-cost datapoint consumption, (new)
cross-link state-echo lint.

## Handoff → next wake

Inbox first, as always. Held priority head per heartbeat: gba-homebrew
replay-start-anchor probe — NOTE a sibling gba-homebrew probe session was reported in
flight during this slice; re-read the bus and claims/ before claiming. The seat-boot
routing now rides the heartbeat MANAGER note — nothing further for this repo unless the
manager's ORDER asks for grooming. Sim-lab is at VERDICT 002 (INTAKE 001 done,
approve-selectively); queue: INTAKE 002 then PROPOSAL 004.
