# Session — substrate-kit host-checkers-one-gate probe (the section's LAST captured head — section complete)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~08:37Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The `ideas/substrate-kit/` section carried ONE remaining captured head:
`host-checkers-one-gate-2026-07-10.md` (an `extra_checks` seam in
`substrate.config.json` so host checkers run under the kit's one `check --strict`
gate). This slice probes it, single-pass battery v0, closing the section. Section
claimed first — `control/claims/probe-substrate-kit-host-checkers-one-gate.md`
landed on main via fast-lane PR #140 (merged 08:35:31Z by the enabler) before any
build work; the only sibling claim at HEAD is
`probe-superbot-next-four-heads.md` (PR #139) — a disjoint section, no collision.

## Verify-first (both sides of the seam)

- **substrate-kit live HEAD `489e763`** (blobless clone 08:30Z; HEAD committed
  08:28:59Z — the kit moved DURING the read window, `be72c09` → `489e763`; the
  delta is the v1.10.1 payload `0499625` (gate tail-1 multi-card shadowing fix +
  doctrine emphasis normalization) + its release claim, disjoint from any
  host-checker surface). Newest tag **v1.10.0 — no v1.10.1 tag yet, no v1.11.0**;
  `[Unreleased]` carries only the tail-1 payload.
- **No `extra_checks` seam** at HEAD — and the near-named `_extra_check_findings`
  (`src/engine/cli.py:606`; dist `bootstrap.py:12932`) is a FALSE FRIEND: an
  internal helper running the kit's own non-doc checkers, zero host-command
  execution in `cmd_check`. The config schema is CLOSED (`Config.from_dict` drops
  unknown keys — the `kit_version` field comment says so verbatim).
- **Layer correction (the probe's sharpest finding):** the captured
  `cmd_check`-subprocess mechanism collides with the kit's §3.2 no-shell-out
  check invariant (`check_setup_script.py:38` "Pure stdlib, no ``subprocess``
  (§3.2)"; `adopt.py:690` "the engine never shells out (§3.2)") — the routed
  build is the gate GENERATOR seam instead: a host-owned config key
  (`gate_host_checks`-shaped) that `live_ci_workflow` (`adopt.py:1615`, already
  parameterized by `interpreter_for_checks`) renders as named non-control-lane
  steps, so regen re-derives the wiring and upgrades cannot drop it.
- **Host-side premise mutated, gap intact:** the capture's "session-ritual-only
  preflight" is history (PR #18 wired it into the KIT-OWNED gate), but the wiring
  is a five-times-caught re-apply treadmill (#35/#54/#55 + the v1.9.0/v1.10.0
  hops), and `scripts/check_harvest.py` (569 lines) is wired NOWHERE — the
  residual "silently falls back to session discipline" class, live.
- **Kit-side corroboration:** the kit's own backlog head
  `docs/ideas/adopt-plants-pytest-gate-step-2026-07-10.md` @ `489e763` (origin:
  superbot-games #16's tests-blind gate) is the template-layer twin — it
  collapses into one default entry of the generalized key.

## Verdict

`host-checkers-one-gate` → **parked(routed — substrate-kit lane build,
layer-corrected)**: gap evidenced from both sides, mechanism moved from
`cmd_check` to the gate generator; JOINS the kit fan-in bundle as its **SIXTH
head**, consolidating with the enabler-guard head's already-routed
"gate-preflight config seam" item (same landing zone — build once). No outbox
proposal (nothing sim-shaped — a generated workflow step is proven by its own
red/green, the #114 precedent). **SECTION MILESTONE: substrate-kit 6/6
probed-or-routed — the SEVENTH complete section** (after superbot-games /
trading-strategy / superbot-mineverse @ #107 / venture-lab @ #110 /
superbot-idle @ #116 / pokemon-mod-lab @ #137).

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` (all 8 checks) + `python3 bootstrap.py check
--strict` run green immediately before push, after the heartbeat overwrite; a
pre-push `git fetch origin main` reconciles any mid-flight sibling forward-only
per the README recipe (the superbot-next four-heads probe is in flight, claim
PR #139). This slice also commits the session's own `.substrate/reflections.json`
mine (`bootstrap reflect --mine`, R-0036) on the slice branch, keeping the claim
PR control-only.

**📊 Model:** fable-5 · medium · single-head probe slice (1 probe report + state
flip + section index + card + claim clear + heartbeat; no scripts, no workflows,
no proposal — task-class: bounded section-closing battery pass)

## 💡 Session idea

**A grep-hygiene lesson worth a capture: symbol-boundary false friends in
verify-first sweeps.** This probe's first evidence pass ran
`rg "extra_checks|plugin|hook_checks|host_checks|custom_checks"` over the kit
and returned ZERO hits — yet `_extra_check_findings` sits in `cmd_check` at the
exact line the probe cares about, invisible because the plural `extra_checks`
never substring-matches `extra_check_findings`. Only reading `cmd_check`'s body
caught it, and the symbol turned out to be a false friend that a hasty probe
could have cited as "the seam already exists" (verdict-flipping in the WRONG
direction). Verify-first sweeps should grep the STEM (`extra_check`,
`host_check`) never the exact key, and treat any near-named hit as
read-the-body-required — one line in the probe-battery reachability discipline
(README § The probe battery) would encode it.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-substrate-kit-heartbeat-behind-pair-probe.md`
(the #138 batched probe — this slice's direct predecessor on the same section).
Its claims verified against the tree and the live kit: (1) both its heads are
badged `parked(routed)` with probe parentheticals in
`ideas/substrate-kit/README.md` (verified in this slice's own index edit); (2)
its claim file is GONE from `control/claims/` (deleted at close per convention —
only README + the #139 sibling + this slice's claim existed at HEAD); (3) its
kit pin aged exactly as its handoff predicted: it flagged "a v1.10.1 payload
claim is in flight at `be72c09` … any next hop should re-verify the parks at the
new HEAD" — this slice re-verified at `489e763` and the in-flight claim had
indeed become the merged payload `0499625`, still disjoint from all bundle
heads; (4) its handoff named this exact slice ("the ripest next slice is the
host-checkers-one-gate probe — probing it closes the section") and the fan-in
count it left (FIVE routed heads) is what this slice consolidates to SIX. Its
method notes were adopted: claim fast-laned before any build byte (#140),
verify-first at the LIVE kit HEAD (which had moved again — the re-read is what
makes the pin honest), and its 💡 (the GITHUB_TOKEN no-retrigger gotcha as a
capability-ledger-worthy fact) is still un-landed — carried below as open
follow-up rather than re-derived.

## Handoff → next wake

The substrate-kit section is CLOSED (6/6 probed-or-routed, the seventh complete
section) — no captured heads remain anywhere in `ideas/substrate-kit/`. The
kit-lane fan-in bundle now stands at SIX routed heads (carveout-needles-config +
enabler-card-status-guard-upstream(sharpened) + kit-line-self-drift +
parallel-session-heartbeat-reconcile + behind-stall-auto-updater(sharpened) +
host-checkers-one-gate(layer-corrected)) plus the pokemon ruling-sync kernel
rider — one manager ORDER carries the whole bundle, and the bundle note now
flags the intra-bundle consolidation (this head + the enabler-guard head share
the gate-preflight landing zone; build ONCE). Watch the kit release cadence: the
v1.10.1 payload is merged but untagged at `489e763` — when v1.10.1 (or later)
ships, the next idea-engine upgrade hop re-fights the two known regen
clobbers (gate wake-preflight step + enabler anchors) one more time; the bundle
landing would make that hop the last hand-carried one. Open follow-ups worth a
future capture: the #138 card's 💡 (GITHUB_TOKEN no-retrigger → this repo's
docs/CAPABILITIES.md) and this card's 💡 (stem-grep discipline). The
superbot-next four-heads probe (claim #139) was in flight this session — expect
its heartbeat facts to need a forward reconcile if it lands first.
