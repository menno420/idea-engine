# Session — games-theme-engine directive probe (the harvest-deferred head comes back armed and finds itself consumed)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~10:22Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

ONE probe: `ideas/superbot/games-theme-engine-website-first-2026-07-10.md` — the
owner-shaped games directive harvested at PR #38 with an explicit ripeness deferral
("probeable once the idle seat exists and pre-registers economy params"). Both arming
facts have since happened AND been consumed (superbot-idle exists; its pre-registered
economy got VERDICT 006), so the battery's honest job was residue assessment: per-§
consumed / frozen / still-open, at live HEADs, with a fan-in ledger. Section claimed
first — `control/claims/probe-games-theme-engine.md`, first commit on this branch (the
early in-flight signal; claims dir empty of competitors at claim time and re-checked at
push). ORDER 002 (fleet self-review) deliberately NOT absorbed — a sibling session
executes it; this slice only reconciles its status.md landing at heartbeat time.

## Grounding pins (every load-bearing claim; ls-remote batch 2026-07-11T10:22:09Z)

- **superbot** live HEAD `c77ee0d` — canonical doc byte-identical `41899e1` → `c77ee0d`
  (raw-fetched both pins, diffed clean this probe); game-state feed NOT at three
  candidate paths (404 ×3 @ `c77ee0d`; not measured beyond candidates).
- **superbot-idle** live HEAD `1e2c9f6` (depth-1 clone): 12 theme packs incl.
  `egg-farm.yaml`, `schema/theme.schema.json`, `tools/theme_gate.py`,
  `docs/provisioning.md` (SETUP-CODE FORMAT v1, `binding`, 150 vectors); heartbeat
  updated 10:11:04Z still lists "economy tuning (SIM-001)" as blocker — the
  VERDICT 006 lift is NOT yet consumed by the lane.
- **superbot-next** live HEAD `8b55d95` — **the probe's find**:
  `docs/game-plugin-contract.md` (D-0056, `binding`) returns 200 at `8b55d95` AND at
  historical pins `4a32f61` + `4c8c5b0`, so the sibling promotion head's "all
  contract-doc paths 404" grounding (4-path list) was a path-keyed false negative;
  ORDER 002 still `status: new` in `control/inbox.md` @ `8b55d95`;
  `superbot-plugin-hello` ls-remote returns zero refs (raw README 404) — the un-park
  condition's doc-fetchable disjunct reads SATISFIED, the ORDER-002-done disjunct not.
- **superbot-games** HEAD `e62818a` (status raw-fetched): theme-leaks R2 cleared,
  audit 19✅·9⚠️·2❌, fishing shipped (44+20 tests of 257), orders 001+002 done.
- **superbot-mineverse** live HEAD `2f2d33a` (depth-1 clone): clone-grep for
  theme/setup-code/provisioning surface EMPTY — the lane consumed the web↔bot
  contract-family discipline, not the theme seam.
- **websites** live HEAD `f0e7710` (depth-1 clone): zero selector/gallery/encoder
  surface; `superbot-idle` only as a fleet-registry row (`app/config.py:251`).
- **fleet-manager** live HEAD `3150f0e`: `docs/roster.md` gen #5 (04:28Z, first
  machine generation) + `docs/proposals/games-program-mapping-conformed-2026-07-10.md`
  (the four manager details all filled: API split · Seat-B contract home + promotion ·
  `superbot-idle` name · selector LAST).
- **sim-lab** VERDICT 006 = PROPOSAL 006, approve, finalized 05:09:53Z — cited from
  the in-tree Sim verdict note on
  `ideas/superbot-idle/idle-economy-sim-kernel-2026-07-11.md` @ its outbox pin
  `d89303e`, never re-derived.

## The probe (verdict: park — routed)

State flip `captured` → `parked(routed — …)` + probe report v0 appended with a per-§
verify-first ledger: §1 seam CONSUMED (Seat B built, Seat A adopting), §2 CONSUMED and
exceeded (12 packs vs "2–3"), §3 write path FROZEN (setup-code v1 binding) / consumer
STILL OPEN but sequenced-last by design, §4 DECIDED + arming HALF-FIRED (the D-0056
find above), §5 CONSUMED (both seats live, first shippables shipped), §6 sim-lab
CONSUMED (V006) / websites OPEN (same §3 surface) / intake OPEN-standing, §7 all four
flags executed or tracked. No outbox entry (nothing sim-ready — the one evidence
question the doc ever carried is already verdicted). Index echoes re-badged in BOTH
READMEs that carry the entry (`ideas/superbot/README.md` + the cross-link in
`ideas/superbot-idle/README.md` — the check_ideas STATE-ECHO warning driven to zero
for this entry, both directions).

## Honesty-guard drop record

- **Un-parking the sibling promotion head** (`theme-schema-plugin-contract-promotion`)
  on the half-fired arming event — NOT done: it lives in the superbot-idle section
  (outside this claim), and its own un-park prescription is a MANAGER relay, not a
  state edit; flagged on the heartbeat notes for the sweep instead.
- **A Seat-A world-themes pre-capture** — NOT captured: the lane's theme audit
  (9⚠️·2❌ remaining) is mid-flight lane roadmap; capturing now would race its own
  self-serve (README self-serve prior, four datapoints).

## Verification (real runs, this tree)

```
$ python3 scripts/check_ideas.py
check_ideas: OK — 301 idea files conform to the README grammar (3 warning(s), advisory)
$ python3 scripts/preflight.py
preflight: OK — all 10 checks green
```

Full `python3 scripts/preflight.py` + `python3 bootstrap.py check --strict` rerun green
immediately before push (after the heartbeat overwrite, reconciled against any sibling
ORDER-002 landing). No merge outcome claimed for this slice's own PR — the number is
stamped by follow-up per the #72 precedent.

**📊 Model:** fable-5 · probe slice (1 probe report + state flip + 2 index re-badges +
card + claim add/clear + heartbeat; no scripts, no workflows, no outbox entry —
task-class: bounded single-head probe)

## 💡 Session idea

**An un-park condition should ship with its own probe command.** The promotion head's
park was event-keyed (correctly!) yet still went stale-blind, because CHECKING the
event meant re-deriving which paths to fetch — and the checker inherited the capture's
4-path list, missing `docs/game-plugin-contract.md` even though a manager doc had cited
that exact path a day earlier. If a `parked(awaiting-arming-event)` reason carried one
paste-ready verification command (here: `curl -s -o /dev/null -w '%{http_code}' <raw
contract-doc URL>` per candidate home, plus the ORDER-done grep), any wake could probe
the event in seconds and the false-negative class would need to survive a byte-level
command review instead of a prose path list. Cheap retrofit-never grammar bless, same
family as the Sequence token.

## ⟲ Previous-session review

PR #155 (groom: superbot recheck, pin `58040c6` → `227c220`, claim #152) — claims
verified against this tree and live HEADs: the claim file is deleted (claims dir held
only README.md at this slice's claim time), the section index carries the `227c220`
pin banner with the recheck's "0 flips, 0 new, 0 deleted" finding, and this probe
independently extended its central claim one HEAD further — the canonical games doc is
byte-identical from the harvest pin `41899e1` all the way to live `c77ee0d`, so the
groom's 0-content-drift verdict still holds past its own pin. Its method adopted here:
verify content at the pin, then re-verify at whatever HEAD is live at fetch time,
never assume the briefing's pin survived dispatch (it hadn't: briefing said ~227c220+,
live was `c77ee0d`).

## Handoff → next wake

Ripest head this probe plants: the **§4 promotion relay** — the theme-schema promotion
park's arming condition half-fired (contract doc live at superbot-next `8b55d95` since
at least `4a32f61`/2026-07-10); it is on this slice's heartbeat notes for the manager
sweep, and if the sweep doesn't collect it within a wake or two, a fan-in slice should
relay it explicitly. Watch superbot-idle for the VERDICT-006 tuning PR (heartbeat @
10:11:04Z had not consumed the lift; when it does, the two sim guardrails must ride the
PR — the verdict text names them). The websites selector stays sequenced-last by
design: do NOT capture a "websites should build the gallery" head; the read-contract
head (`theme-catalog-gallery-read-contract`, parked build-direct) is the correct next
domino and belongs to the lane. ORDER 002 self-review: sibling-owned; verify its
status.md section landed and was preserved verbatim by this slice's heartbeat
reconcile.
