# Kit upgrade — retire the fleet's oldest pin (v1.1.0 → v1.7.0)

> **State:** parked(overtaken-by-events — the lane executed the exact slice itself 14 minutes after this capture merged: v1.1.0 → v1.7.0 as its PR #38 (`0e713b9`, 2026-07-10T20:34:45Z, sequenced after the ORDER 008 holdout spend exactly as this capture prescribed), then kept going — v1.7.1 (its PR #44, `24649d7`) and v1.8.0 (its PR #51, `d0d789e`, HEAD at probe time); `substrate.config.json@d0d789e` reads `"kit_version": "1.8.0"`)
> **Class:** process · **Target:** `menno420/trading-strategy`
> **Grounding:** https://github.com/menno420/trading-strategy@d0d789ef7319fde6b9b416e72240a01fe3b79097 · fetched 2026-07-11T01:23:01Z (manifest row: behind)
> *(pin annotation: probe-time re-check pin — capture pin was `e713abb` (2026-07-10); manifest row @ superbot HEAD `10a7486` STILL reads "kit v1.1.0 (oldest pin)" (row update stamp 2026-07-10 16:21/16:24Z) while the lane tree at `d0d789e` carries kit_version 1.8.0 — three kit versions and a program phase behind; the lane's OWN heartbeat @ `d0d789e` also lags its tree by one version ("kit: substrate-kit v1.7.1 — upgraded … via PR #44" — lane PR #51's upgrade did not overwrite it); freshest wins: lane HEAD tree-scan)*
> **Sequence:** after trading-strategy ORDER 008 (P5 spend) — constraint MET by the lane itself: holdout spent 2026-07-10T16:47Z, the v1.1.0→v1.7.0 upgrade landed 20:34Z — around, not inside, the holdout session, exactly as the capture prescribed.

## Problem

The manifest flags the lane as running "**kit v1.1.0 (oldest pin)**" while the kit
shipped v1.7.0 gen-2 CLOSED — six MINOR versions of gate and checker fixes the lane
has never received. This is not cosmetic drift: the lane's own `control/status.md`
documents live process friction that newer-kit repos don't have (auto-merge arm
fails pending-side with the "unstable status" wall on every PR, reconfirmed on
PR #36, forcing agents to poll-and-REST-merge), and the v1.7.0-era planted
`substrate-gate.yml` carries the control-fast-lane and session-card gating fixes
that were learned live across the fleet after v1.1.0 was pinned. A parked-green lane
is the cheapest possible moment to take an upgrade — no research in flight to
destabilize.

## Idea

One bounded slice on the lane: `bootstrap.py upgrade` to the current dist, re-render,
run `check --strict` plus the full pytest suite (147 green at ORDER 007), land as one
READY PR, and bump the `kit:` self-report line in `control/status.md` in the same
session (the kit-line contract requires exactly that). Sequencing note: land it
**around, not inside,** the ORDER 008 holdout session — the binding P5 protocol
session should run on a tree whose gates weren't changed the same hour.

## Grounding

- Manifest trading-strategy row: "kit v1.1.0 (oldest pin)"; kit-lab row: "gen-2
  CLOSED handoff-ready at **v1.7.0**", write-all distribution scope per Q-0261.3
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane reality @ [`e713abb`](https://github.com/menno420/trading-strategy/tree/e713abb125766db2b1562980369a11290b8772b9):
  `control/status.md` health line (auto-merge "unstable status" wall on PR #36;
  147 tests as the upgrade's regression baseline) and ⚑ (c).
- Kit-line update-in-same-session rule: this repo's `control/README.md` § status
  format ("update it in the same session as every `bootstrap upgrade`").

**Why now:** the lane is parked green with one owner-gated order outstanding — the
last quiet window before post-holdout research restarts on top of whatever gates it
has.

## Probe report (v0, 2026-07-11)

*Probed 2026-07-11T01:23Z, single-pass per the README panel default (sim-lab VERDICT 002
— no ambiguity signal, no irreversible surface). Live-state recon FIRST per the
expiry-aware ordering rule ("why now" named a closing quiet window) and the
lane-self-served presumption the PR #49/#51 cards established — and it decided the
verdict in one read. Lane HEAD `d0d789e` (ls-remote 2026-07-11T01:23:01Z, re-confirmed
unchanged in the same stamped fetch); superbot HEAD `10a7486`; upgrade-commit history
from a read-only blobless clone.*

**Live state, with citations:**

- **The kit pin at lane HEAD** — `substrate.config.json@d0d789e` reads
  `"kit_version": "1.8.0"` (raw fetch 2026-07-11T01:23:01Z).
- **The capture's exact slice, executed by the lane** — lane commit `0e713b9`
  "kit: upgrade substrate-kit v1.1.0 → v1.7.0 (#38)", committed 2026-07-10T20:34:45Z —
  **14 minutes** after this capture merged (idea-engine PR #10, 2026-07-10T20:20:48Z).
- **Then two more** — `24649d7` "kit: upgrade substrate-kit v1.7.0 → v1.7.1 (#44)"
  (2026-07-10T22:14:55Z) and `d0d789e` "kit: upgrade substrate-kit v1.7.1 → v1.8.0
  (#51)" (2026-07-11T01:15:34Z — merged ~8 minutes before this probe's ls-remote; it IS
  the lane's HEAD).
- **Sequencing note honored** — holdout spent 2026-07-10T16:47Z (lane
  `control/status.md` @ `d0d789e`: run stamps 2026-07-10T1647Z); the upgrade landed
  20:34Z, around — not inside — the ORDER 008 session, exactly as the capture's own
  note prescribed.
- **Divergences (freshest-wins)** — manifest row @ superbot HEAD `10a7486` still reads
  "kit v1.1.0 (oldest pin)" (staleness datapoint 15, same row as datapoints 5–6 and 13);
  the lane's own heartbeat kit line @ `d0d789e` still reads "substrate-kit v1.7.1 …
  via PR #44" — one version behind its own tree (lane PR #51's diff has no
  `control/status.md` in it), a live kit-line-self-drift datapoint against the
  update-in-same-session contract this capture itself cited.

**1. What is this really?**
A correctly-diagnosed maintenance capture whose target lane ran the fix before the
probe could — the sharpest lane-self-served datapoint yet: 14 minutes from capture
merge to the lane's own v1.1.0→v1.7.0 upgrade commit (websites' PR #79 took ~19 min;
the R3 xsec self-serve took hours). Independent convergence, not wasted work: the
capture named the right lane, the right slice, and the right sequencing, and the lane
did precisely that.

**2. What is the possibility space?**
Post-self-serve, three residuals, none probe-worthy: (i) the lane's heartbeat kit line
lags its tree by one version (v1.7.1 line vs 1.8.0 config) — a one-line fix in the
lane's next heartbeat overwrite, self-correcting by its own contract; (ii) future kit
upgrades are now routine lane maintenance (three executed in ~5 hours proves the
muscle); (iii) the manifest row refresh — manager surface, already carried by the
staleness-datapoint series.

**3. What is the most advanced capability reachable by the simplest implementation?**
Already reached, by the lane, past the capture's target: it asked for v1.7.0 and the
lane sits at v1.8.0 — whose upgrade diff even ships `.substrate/ci/auto-merge-enabler.yml`,
aimed at the exact auto-merge "unstable status" friction (lane ⚑ (c)) the capture cited
as motivation (whether it clears that wall is unverified — not measured here).

**4. What breaks it?**
Broken by timing, twice over: the slice was executed 14 minutes after capture, and the
capture's target version was itself stale within hours (the lane went two MINOR
versions past it). A probe here can only record state. The capture's one premise that
never held at probe time: "kit v1.1.0 (oldest pin)" survives ONLY in the manifest row
(@ superbot `10a7486`) — a reader trusting it would prescribe an upgrade to a lane
three versions ahead of the prescription.

**5. What does it unlock?**
Nothing by acting — the trail is the product: third live lane-self-served datapoint
(two sections, both arrival paths, now spanning PRODUCT and PROCESS classes), and
datapoint 15 in the manifest-staleness series.

**6. What does it depend on?**
Consumed: it depended on the upgrade being un-executed; lane PR #38 consumed that
within the capture's own merge hour. The residual kit-line fixup depends only on the
lane's next session close-out.

**7. Which lane should build it?**
`menno420/trading-strategy` — and it already did (its PRs #38/#44/#51, all
merged-on-green with its 223-test suite). Nothing to route: no sim-lab question (a
completed upgrade proves itself), no providing ORDER, no owner action.

**8. What is the smallest shippable slice?**
For idea-engine: exactly this PR — state flip + probe report + section-index row, no
proposal. For the lane: the one-line heartbeat kit-line bump (v1.7.1 → v1.8.0) in its
next overwrite. For the manager: refresh the trading-strategy manifest row before any
manifest-driven routing touches this lane.

**Recommendation: park** — overtaken-by-events: the lane executed the capture's exact
slice itself (`0e713b9`, v1.1.0→v1.7.0, 14 min after capture merge, sequenced around
the holdout exactly as prescribed) and is now at v1.8.0 (`substrate.config.json@d0d789e`);
nothing remains to queue, route, or simulate.
