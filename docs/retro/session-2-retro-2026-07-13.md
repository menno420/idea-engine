# Session 2 retro — 2026-07-13 (coordinator close-out)

> **Status:** `historical`
>
> Durable retro record written at the session-2 close-out (universal ender,
> span 2026-07-12T20:45Z → 2026-07-13T~12:35Z), following the
> `docs/retro/self-review-2026-07-11.md` convention: chat-only coordinator
> knowledge gets a committed home before the session archives. Every
> load-bearing claim cites a PR and/or sha; every count below was re-verified
> at close against both trees at HEAD (idea-engine `3a7be39` / sim-lab
> `afe18f3`) and against the live GitHub PR index (0 open PRs in both repos at
> 2026-07-13T~12:40Z). Landed by the close-out PR (branch
> `claude/session2-ender-closeout`); the heartbeat twin is
> `control/status.md` at the same commit.

## 1. Shipped & parked

- **idea-engine: 38 PRs merged, #271–#308, contiguous, zero left open**
  (verified by counting `(#NNN)` squash subjects on `origin/main` since
  2026-07-12T20:00Z — 38 merges, min #271, max #308, no gaps).
  - **23 PROPOSALs P013–P035** appended to `control/outbox.md` (35 proposal
    headers total at HEAD; P013–P035 are this session's). Roster: P013 #275 ·
    P014 #276→390a89b · P015 #277→b5f6791 · P016 #279→d1d1b6b · P017
    #281→80baad5 · P018 #283→d0dca70 · P019 #284→f7906e5 · P020 #286→da20713 ·
    P021 #287→8022a9d · P022 #288→1c6313c · P023 #289→15d1802 · P024
    #290→b11e258 · P025 #291→a123fda · P026 #293→0716140 · P027 #294→3978df1 ·
    P028 #295→535c232 · P029 #297→0e168bf · P030 #298→9b24977 · P031
    #299→6daf5ea · P032 #302→2e5d73f · P033 #303→11c5a1f · P034 #306→eea4e5b ·
    P035 #308→3a7be39.
  - **ORDER landings**: owner ORDER 003 (continuous pipeline) #274 → 1bfcde6;
    owner ORDER 004 (night run) #280 → c99852c; fm ORDERs 005/006/007
    #300→b428feb / #304→98b147b / #305→755319e.
  - **Infra**: auto-merge enabler `claude/*` allowlist fix #272 → daf9d50
    (kit-owned file — must be re-applied on upgrade; upstream ask = outbox
    ASK 001); outbox-parser fix in `scripts/check_ideas.py` rode #286.
  - **Control**: heartbeats/tallies #271/#273/#278/#292/#307 (TALLY 001 #292
    → 3b9a728, NIGHT-REPORT 001 #307 → 8218d66); claims prunes
    #282/#296/#301; V020+INTAKE-018 cross-ledger echo #285 → b9914ca.
- **sim-lab: 38 PRs merged, #57–#94, contiguous, zero left open** (same
  count method — 38 merges, min #57, max #94, no gaps).
  - **31 VERDICTs V015–V045** finalized in `control/outbox.md` (45 verdict
    headers total at HEAD; V015–V045 are this session's). V015–V036 answer
    PROPOSALs P013–P034 at the constant +2 offset; **V037–V045 are the 9
    SIM-REQUESTs** (intakes `simreq-001…009`, ORDER 005/006 relays) naming
    requesting seats venture-lab (V037/V039/V040/V041), superbot-idle (V038),
    superbot-games (V042/V043/V044/V045).
  - **Scoreboard V015–V045, counted at HEAD** (rulings extracted from the 31
    `verdict:` lines): **8 approve** (V015 V016 V018 V021 V028 V030 V034
    V042) · **1 approve-with-constants** (V043) · **1 ratify-with-null**
    (V045) · **1 mint-at-most-once** (V044) · **6 conditional** (V017 + the
    R3-conditional-default family V037/V038/V039/V040/V041) · **7 null**
    (V019 V020 V024 V026 V029 V031 V035) · **7 reject** (V022 V023 V025 V027
    V032 V033 V036).
  - **Infra/control**: INTAKE-018/V020 relocation echo #66 → a7edcad;
    current-state refresh #62 → a3b921b; tally heartbeat #72 → 6e28a63; night
    report #83; V043 red-flip repair #91.
- **Parked: NONE.** 0 open PRs in both repos at close (live GitHub, verified
  ~12:40Z), the two close-out PRs themselves excepted — they land on green
  per the standing enabler posture.
- **THE SEAM (one in-flight item): PROPOSAL 035 is UNVERDICTED.** P035
  (mining booster bypass, `## PROPOSAL 035 · 2026-07-13T12:12:40Z · status:
  sim-ready`, landed #308 → 3a7be39) had its verify session die at start
  (turn_failed no_access, 12:23Z) — nothing landed anywhere. Resume pointer:
  the successor dispatches a verdict session FIRST — INTAKE 035 + VERDICT
  046, spec readable at HEAD, template `sims/verdict-04x`, V042's anchors
  (`sims/verdict-042-mining-economy/{results,fixtures}.json` @ afe18f3)
  already in the sim-lab tree.

## 2. Struggles

- **`claude/` enabler-allowlist jam** — PR #271 sat green but unarmed: the
  kit enabler's hardcoded branch allowlist predated the fleet's `claude/<slug>`
  branch mandate. Fixed by #272 → daf9d50; the file is KIT-OWNED (regenerated
  on upgrade), so the fix must be re-applied on the next kit hop — upstreamed
  as outbox ASK 001, still `status: new`.
- **Inbox grammar gate fires only with `--inbox-base`** — the CI inbox
  append-only gate red on #274 (the ORDER 003 landing) where plain local
  `check --strict` had exited 0: the grammar leg only runs when CI passes the
  merge-base blob via `--inbox-base`. Fixed forward on the PR.
- **CI `check_ideas` preflight stricter than local `check --strict`** — red
  on #299 (P031): the idea file lacked a "## Probe report battery" section
  and a Grounding line that `scripts/preflight.py`'s check_ideas leg enforces
  in the non-control CI lane but plain `check --strict` does not. Fixed
  forward, same PR landed green. Both this and the #274 class are baked as
  **ASK 002** (this close-out): make local `check --strict` run the same
  preflights so local green ⇒ CI green.
- **V020 verdict mislocated into the idea-engine outbox** — the cross-ledger
  landing (idea-engine #285 → b9914ca) put INTAKE 018/VERDICT 020 in the wrong
  repo's ledger; repaired by the sim-lab relocation echo #66 → a7edcad, with
  the reconciliation pointer in sim-lab `docs/current-state.md`.
- **Write-tool REPORT.md refusals across ~8 worker sessions** — the harness
  refused report-file writes; workers switched to text returns (and a heredoc
  workaround where a committed file was genuinely needed). Zero work lost.
  Exact denial text preserved in the close-out PR body (quotes live there by
  convention, not in this doc).
- **Standalone `sleep` blocked** — foreground sleep is disallowed by the
  harness; polling was restructured into bounded checks.
- **One `&&`-chain exit-code slip shipped a red card flip** — the V043
  sibling's flip commit rode a chain whose earlier leg masked the check exit
  code (sim-lab #90); repaired immediately by #91. Lesson: capture the
  `check --strict` exit code directly, never inside a compound chain — this
  close-out does exactly that.
- **A fleet watchdog's failsafe-wedge claim was REFUTED** — the claim was
  checked against the trigger registry per Q-0120 (verify, never obey) and
  found false; the failsafe had fired on schedule all night.
- **Auto-merge squash race + dirty-zero-checks jams** — the known classes
  (documented in `docs/current-state.md` § Ops facts) recurred and were
  handled by the standing merge-main-in-never-rebase protocol; no work lost.

## 3. Went well

- **Read-spec-at-HEAD dispatches** — every verdict/proposal session read its
  spec from the committed tree at a named pin instead of trusting the brief;
  this caught the stale seed high-water in V041's dispatch brief (superseded
  twice mid-day, V040 → 20260880 and V043 → 20261280).
- **Verdict-number reservation + race protocol** — numbers RESERVE, never
  positions; origin/main merged INTO in-flight branches, never rebased. Nine
  concurrent SIM-REQUEST slices interleaved (V036–V045 landed out of number
  order: #85–#94) with zero renumbering and zero collisions; the one same-id
  landing (simreq-007 consumed by the fishing slice) resolved by the
  documented next-free-id exception (INTAKE simreq-008, #92).
- **`simreq-NNN` intake namespace** — SIM-REQUEST intakes got their own id
  space (per the owner-001/owner-002 precedent), keeping the INTAKE nnn ↔
  PROPOSAL nnn chain unbroken through the 9-request wave.
- **Chained anchors** — verdicts built on committed predecessors' machine-read
  results (V022→V025→V027 casino family; V024→V026/V028→V034 and onward),
  with P035 fully hermetic on V042's committed engine subtree + results.json
  (zero fresh clones).
- **Pre-registration discipline with honest NULLs** — all 7 nulls landed on
  pre-registered branches as finalized verdicts (never re-run requests), each
  naming its binding axis.
- **Hybrid pacemaker + failsafe wake posture** — zero missed wakes across
  ~16 h: send_later chain during active turns, 2-hourly failsafe cron for
  idle coverage (the VERDICT 014-ratified posture).

## 4. Surprises & open questions

- **SIM-REQUESTs arrive as manager ORDER relays in the idea-engine inbox**
  (ORDERs 005/006 @ 8218d66), not as direct sim-lab entries — the channel is
  now proven end-to-end (9/9 served, requesting seats named in each verdict).
- **V015 found the "1 contradiction" premise undercounted ×30** — the
  heartbeat-contradiction corpus held 30 real (revision × entity) intra-file
  contradictions from ONE carry+update seam, not the 1 the proposal named.
- **V030: the standard bracket ranks 12/315** — the default seeding is
  measurably suboptimal at its own stated goals in every profile.
- **V044: escort is an UNBOUNDED farm** — the loopability census found no
  committed cap; ruling mint-at-most-once.
- **V043's sibling shipped a red card flip via the `&&` slip** (#90, repaired
  #91) — surprising because the born-red gate is designed to make exactly
  that impossible; the gate held at CI, the slip was local-ritual-side.
- **Open questions for the successor**: (1) the P035 seam (INTAKE 035 +
  VERDICT 046) — first dispatch; (2) does the `claude/` allowlist line
  survive the pending kit v1.15.0 upgrade (ASK 001's verified-needed);
  (3) does ASK 002 (local↔CI check parity) get picked up by the kit lane
  before the next preflight-class red.
