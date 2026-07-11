# Self-review 2026-07-11 (ORDER 002) — durable retro record

> **Status:** `historical`
>
> Moved VERBATIM from the foot of `control/status.md` at the 2026-07-11 wrap-up
> close-out (owner-directed: the coordinator chat is being archived, so chat-only
> and heartbeat-foot content gets a durable home). Original section shipped by
> PR #158 (branch orders/self-review-2026-07-11) per inbox ORDER 002; nothing
> below this banner has been edited.

## Self-review 2026-07-11 (ORDER 002)

> Window: 2026-07-10T20:00Z → 2026-07-11T~10:30Z. Owner-requested fleet-wide self-review, relayed
> as inbox ORDER 002 (P1). Claim rode fast-lane PR #156 (merged 0c70f33); shipped this slice
> (branch orders/self-review-2026-07-11). Every load-bearing claim cited (PR + sha or file:line).

### 1. What went wrong

- **PR #85 stale coordinator session-log PR** — closed UNMERGED by menno420 at 2026-07-11T05:26:11Z
  ("Closing as superseded/collided — content verified duplicative of main … coordinator hygiene");
  head branch fix/session-log-2026-07-11 STILL exists on origin (branch-delete is a ledgered 403
  wall, docs/CAPABILITIES.md:51). The staleness was flagged live on
  .sessions/2026-07-11-snapshot-parity-audit-probe.md:58-63, but the close itself is recorded ONLY
  on GitHub — no session card or status line carries it. Gap named here.
- **Dirty-PR zero-check-runs auto-merge jams (recurring class)** — FIRST documented on
  .sessions/2026-07-10-capability-pair-probe.md:56-58, which landed as PR #33 (merge cd7251e;
  the folklore that says "#29" is wrong — #29 is merge commit 698fd93, a different PR).
  Recurrences: PR #38 (.sessions/2026-07-10-superbot-theme-engine-reharvest.md:56-58),
  .sessions/2026-07-10-sim-verdicts-fanin.md:79-80, .sessions/2026-07-11-verdict-registry-probe.md:131,
  .sessions/2026-07-11-ci-parity-guard-probe.md:75. Doctrine now standing in control/README.md § CI notes.
- **Auto-merge enabler arm-at-open race broke multi-commit plans** — #62, #64 (opened→merged in
  24s), #80 (25s; its close-out exiled to follow-up #81). Fixed by PR #86 (521aebf, merged
  2026-07-11T04:48:59Z), which live-fired on itself — sat OPEN while mergeable_state clean
  (.sessions/2026-07-11-automerge-arm-race-guard.md:83-86).
- **Kit regen clobbered host workflow customizations on consecutive upgrades** — FOURTH time at
  #120 (v1.9.0, f417a1f) and FIFTH at #125 (v1.10.0, b11fe68); on BOTH hops the PR #36 tripwire
  caught the gate clobber and the manual-diff duty caught the enabler clobber
  (.sessions/2026-07-11-kit-upgrade-v1.9.0.md:50-66, .sessions/2026-07-11-kit-upgrade-v1.10.0.md:51-74).
  Routed upstream via .sessions/2026-07-11-substrate-kit-clobber-family-probe.md.
- **Stop-hook telemetry flush treadmill** — 13 one-line flush merges #58→#100 in ~3.5h; ended by
  PR #108 (b53c01f, nag exemption for kit state anchors) plus final residue flush #109 (1abc3bb).
  NOTE: #93 (466ccdd) was the separate fill-token seam fix, NOT the treadmill fix — an earlier
  briefing paired "#93/#108" wrongly; corrected here.
- **Q-id mislabel near-miss** — PR #134 (454a1db): NO pokemon entry exists under Q-0266 in fm
  surfaces ("Q-0266" is the fm-side label on the Emerald/Option-A decide-and-flag); this lane's
  own session read landed on the WRONG ruling and only the verbatim-quote discipline caught it
  (.sessions/2026-07-11-pokemon-verify-park-pair.md:43-46 and 99-101). Recorded in both park
  notes, unresolved (fm's ledger to fix).
- **Non-monotonic heartbeat `updated:` stamps** — historical instance (21:40Z/22:25Z stamps on
  20:31Z/20:44Z commits) quoted at ideas/substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md:101-103;
  the #138 wake planted the advisory tripwire (.sessions/2026-07-11-substrate-kit-heartbeat-behind-pair-probe.md:61-65).
- **Permission/classifier denials** — THREE terminal denials attempting to land venture-lab PR #15
  from a lane seat (.sessions/2026-07-11-venture-lab-self-landable-probe.md:21-27, surfaced by this
  repo's PR #110); child-session-refused-where-a-coordinator-wasn't is ledgered at docs/CAPABILITIES.md:56-59.
- **Proxy walls** — api.github.com anonymous 403 (docs/CAPABILITIES.md:53); *.github.io blocked
  (docs/CAPABILITIES.md:70, ledgered via #147); GITHUB_TOKEN pushes never retrigger workflows
  (docs/CAPABILITIES.md:71, ledgered via #144). The GitHub release-asset `releases/download/` 403
  is CARD-ONLY (.sessions/2026-07-10-kit-upgrade-v1.7.1.md:15-17, re-confirmed
  .sessions/2026-07-11-kit-upgrade-v1.8.0.md:20) and NOT yet in the CAPABILITIES append-log — gap
  named; promotion suggested on this slice's card 💡.
- **Honesty line** — one briefed went-wrong candidate did NOT verify: no invented-SHA near-miss
  exists on the #76 wake (exhaustive grep negative across .sessions/, control/, docs/ and full git
  history); recorded as not-found rather than repeated.

### 2. Owner attention (click-level)

- **The one sitting by 2026-07-14 carries THREE decisions** (bundled — standing detail on the ⚑
  line above): (a) Lumen Drift itch.io go/no-go + publish clicks (full OWNER-ACTION entry already
  on this heartbeat's ⚑ line, from #97); (b) pokemon playtest verdicts (fm docs/owner-queue.md
  item 3, from #131); (c) the gba concept pick (the lane's own heartbeat ⚑, from #148/#150). The
  same sitting will likely GENERATE the first share ask (egress-doctrine probe, PR #137) — no
  separate click needed yet.
- **Venture-lab repo settings, owner-only, ~1 minute**: turn ON "Allow auto-merge" and mark
  substrate-gate as a required check (from PR #110,
  .sessions/2026-07-11-venture-lab-self-landable-probe.md:29-34; unverified from any agent seat —
  the three terminal denials above prove the wall).
- **Standing decide-and-flag open to veto**: the Q-0266 Emerald-QoL+ framing used in the pokemon
  parks (#134/#131 cards — fm gen-#4 note reads "owner can override").

### 3. Health

147 distinct PRs merged in the window (98 squash #55–#155 + 49 merge-commit; the only
close-unmerged ever is #85); 10 of 13 sections fully probed-or-parked; 7 proposals shipped, 6
verdicted + 1 awaiting verdict (PROPOSAL 007); next: living-backlog grooming + probe-by-expiry on
the remaining superbot/websites/fleet heads.
