# Session — pinned-feed-contract-for-dashboard-json probe: parked(routed), the read-only-API fan-in

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

The heartbeat's STANDING SHORTLIST item 2: full v0 battery on
`ideas/superbot/pinned-feed-contract-for-dashboard-json-2026-07-10.md` (single-pass —
docs/contract-pattern surface, no blast radius; VERDICT 002 default). Verify-first
grounding all live at probe time (~12:47–12:50Z): superbot HEAD S = `e1090db`
(ls-remote 12:47:33Z), canonical doc @ S byte-identical to the harvest pin `fd638e3`;
the LIVE `dashboard/data/dashboard.json` @ S carries THIRTEEN families with only 2
contracted — including three (`reviews`, `bot_changelog`, `telemetry`) the canonical
idea's own remaining-list doesn't name; `console.json` families exactly match its
contract; NO `mining_snapshot` feed exists anywhere probed (404s at `data/`,
`dashboard/data/`, `botsite/data/`) — the games feed needs a NEW producer.

**Recommendation: park** — routed: the pattern is the fleet's DECIDED read-only-API
transport (fm ORDER 012: "superbot lane, contracted committed-JSON feed per #1920's
actual pattern … NOT a live service"; ORDER 013 confirms the split; both @ fm HEAD
`7b46bd1`), with four consumers converging (websites dashboard, botsite console,
games-web phase-2 per VERDICT 007 change #2, websites stats/explorer). The build =
superbot lane INSIDE the fm ORDER 012/013 providing ORDER — which is decided but
verified UNROUTED at superbot's inbox @ `e1090db` (12:48:02Z; inbox holds exactly
ORDER 001 done + ORDER 002 new), apparently owner-held pending the founding-package
review (fm ORDER 012 ⚑ OWNER-REVIEW). NO outbox proposal: no genuine sim question
survives — VERDICT 007 already routes the one measurable axis (presentation value)
to a phase-2 A/B; the rest is deterministic contract engineering. The probe's Q8
contract-shape line (born-contracted `mining_snapshot.v1` + one-family-one-bump +
the 3 unlisted live families) attaches to the providing-ORDER relay via the
heartbeat's manager-sweep line. State advanced captured → parked(routed — …), index
bullet re-badged to the exact echo.

**Honesty note (pin supersession, not error):** prior session surfaces cited the
unrouted-inbox fact at older pins — PROPOSAL 007's `depends:` reads "@ `58040c6`",
the #167-era heartbeat reads "@ `e1090db` carries only its ORDER 001" — both
pre-date ORDER 002's append. The "unrouted" claim itself RE-VERIFIES TRUE this
slice at the same SHA `e1090db`, which now also carries ORDER 002 (2026-07-11T10:01Z,
fleet-wide self-review relay, status: new). Supersession, not error.

**Rider shipped:** one bullet in `control/claims/README.md` § idea-engine specifics
documenting the claim-branch naming convention — work branch + `-claim` suffix,
never a `claim/` prefix (#166's prefix was a one-off; every other claim rode its
work prefix). Closes the #167 heartbeat's "NEW small flag".

Claim ritual honored: `control/claims/probe-pinned-feed-contract.md` fast-laned as
PR #170 (merged fb7be40, the branch-cut base), deleted in this close-out.
`.substrate/` reflect residue (reflections.json R-0044 + guard-fires.jsonl) rides
this PR per repo precedent. Also observed live: sim-lab INTAKE 008
(mining-grid-encounters, from PROPOSAL 008 @ `68f4574`) went in-progress at
12:45:17Z @ sim-lab HEAD `a05ee3c` — the V008 fan-in is arming. Heartbeat
overwritten LAST; preflight + `bootstrap.py check --strict` green before push;
landed per README § Landing conventions (PR READY, merge-on-green).

**📊 Model:** fable-5 · docs-only (one idea-file probe append + index re-badge +
claims-README rider + card + heartbeat; no code)

## 💡 Session idea

The two LIVE contract semantics are undoctrined: `console_data_contract.json` is
TOTAL-whitelist (every family contracted, unknown = fail) while
`dashboard_data_contract.json` is SLICE (only `contracted_families` pinned, the
other 11 free to drift). Nothing anywhere says WHEN each applies — a one-line fleet
doctrine ("new feeds are born total-whitelist; legacy feeds grow slice-wise toward
total, flipping semantics at full coverage" or whatever the manager rules) would
make every future feed contract mechanical instead of a per-PR judgment call.
Attach to the same fm ORDER 012/013 providing-ORDER relay as the born-contracted
line — same relay, zero extra routing cost.

## ⟲ Previous-session review

The V007 fan-in card (`.sessions/2026-07-11-verdict-007-fanin.md`) spot-checked
against the tree: its `## Sim verdict (2026-07-11)` note exists where claimed
(`ideas/product-forge/games-web-concept-evidence-pass-2026-07-11.md:129`); its claim
file (`control/claims/fix-verdict-007-fanin.md`) is gone from `control/claims/` —
deleted at close per convention (only README.md + this slice's own claim there at
my wake). Its handoff aged honestly: it named the claim-branch-convention doc fix
as "best next slice NOW" and item 2 (this probe) + item 4 as ripe — this slice
consumed BOTH the doc fix (rider) and item 2, so the handoff's ranking was
load-bearing, not decorative. No reconciliation debt handed forward.

## Handoff → next wake

Ripest NOW: **usage-limit-aware-routines** (shortlist item 4) — HARD EXPIRY
2026-07-14 (EAP wrap-up send window; PROPOSAL 005 depends) — probe before the 13th.
Armed behind it: the PROPOSAL 008 verdict fan-in when sim-lab finalizes V008 —
INTAKE 008 went in-progress at 12:45:17Z (@ `a05ee3c`), so the verdict may land
within hours. The claim-branch rider is DONE this slice — drop it from ripe lists.
Manager-side watches unchanged (theme-schema promotion half-armed; superbot-idle
tuning PR must carry V006's two guardrails; adoption-record retirement sweep) plus
the NEW one: when the fm ORDER 012/013 providing ORDER routes, attach this probe's
contract-shape line + the dual-semantics doctrine candidate (💡 above).
