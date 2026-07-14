# Ideas Lab seat — EAP close-out project audit (2026-07-14)

> **Status:** `audit`
>
> FINISHED — this doc ships complete, not in-progress (the badge token is
> `audit` because the docs badge grammar allows only
> archive/audit/binding/historical/ideas/living-ledger/owner-guidance/plan/reference —
> `complete` is a session-card status, rejected by the `[badge]` checker).
> The seat's definitive EAP audit, ordered by the owner as inbox ORDER 011
> (`control/inbox.md`, landed verbatim 2026-07-14): what this project used,
> what it couldn't use, where it lost time, what it fixed, what still hurts.
> Covers BOTH repos of the Ideas Lab seat — [menno420/idea-engine](../../README.md)
> (ideation) and menno420/sim-lab (verdicts). Every finding carries a
> disposition: **FLEET-FIX** (we can improve it ourselves), **ANTHROPIC**
> (candidate ask for the final feedback email), or **ACCEPTED** (inherent
> cost). Numbers are MEASURED (git log, exhaustive PR/workflow-run listings
> via GitHub MCP, ledger greps) — never estimated; "not measured" is stated
> where true.

**Measurement basis.** Local clones unshallowed and pinned at measurement
time: idea-engine @ `4399b6d`, sim-lab @ `03b81fc`; GitHub listings snapshot
2026-07-14T08:39–08:54Z (both PR lists paginated to exhaustion, contiguous
#1..#N; workflow runs deduped by id, run_number contiguous 1..N). A sibling
worker was live during measurement: idea-engine PR #412 (created 08:42:16Z)
is included; 2 sim-lab workflow runs and 2 branches created after ~08:52Z
are not (§11). GitHub MCP reads can be ~25 min stale.

**Prior art & delta.** This repo pair already carries retrospectives and an
external audit; this doc cites and DELTAs them instead of restating:
`docs/retro/self-review-2026-07-11.md` (ORDER 002, window 07-10→07-11: the
dirty-zero-checks jam genealogy, arm-at-open race + fix #86, kit-regen
clobbers, stop-hook treadmill, the 3 venture-lab terminal denials, proxy
walls) · `docs/retro/session-2-retro-2026-07-13.md` (session 2: the claude/
enabler jam #271/#272, local-vs-CI gate divergence #274/#299, Write-tool
REPORT refusals, the P035 seam) · `docs/audits/2026-07-13-fleet-cleanup-audit.md`
(both repos, external pass: CI health 22/30 with all 8 fails = designed
born-red holds; outbox past the 256 KB read wall; review-queue.md never used
across 115 sim-lab PRs) · sim-lab `docs/retro/self-review-2026-07-11.md` +
`docs/retro/archive-ready-2026-07-11.md` (OA-002/003/004 verbatim, SQUASH
race) · sim-lab `docs/CAPABILITIES.md` walls fence (folded per ORDER 007,
sim-lab PR #136 → `b10ffce`). New here and nowhere else: the measured PR/CI
corpus (§1, §4), the full denial-quote inventory with dispositions (§3), the
guard-fires quantification (§7), the scheduling forensics roll-up (§5), and
the ranked asks (§9–§10).

## 1. Identity & scale

**Seat:** Ideas Lab — one coordinator + dispatched worker sessions, operating
two repos: **idea-engine** (fleet ideation lab: `ideas/<section>/` for 13
lanes, `control/` coordination bus, no product code) and **sim-lab**
(reproduced-evidence verdicts on idea-engine PROPOSALs + fleet SIM-REQUESTs).
Pipeline: idea-engine proposes → sim-lab verdicts → fleet-manager routes.

**Active window:** 2026-07-10T17:50:16Z (idea-engine first commit `df64aab`)
→ 2026-07-14 ≈ **3.6 days**.

| Measured total | idea-engine | sim-lab | combined |
|---|---|---|---|
| Session cards (`.sessions/`) | 209 | 79 | 288 |
| PRs opened | 412 | 133 | **545** |
| PRs merged | 410 | 133 | **543** |
| PRs closed-unmerged | 2 (#85, #361) | 0 | 2 |
| PRs open at snapshot | 0 | 0 | 0 |
| Commits on main | 638 | 134 | **772** |
| Heartbeat commits (`control/status.md`) | 175 | 36 | 211 |
| Backlog: PROPOSALs / VERDICTs | 62 (P001–P062, all sim-ready) | 72 (V001–V072, all finalized) | 61 of 62 proposals verdicted |
| Unverdicted backlog at snapshot | — | — | **1** (P062 → V073, in flight, §11) |

Throughput ≈ 17.7 proposals/day in, ~20.6 verdicts/day out (verdicts exceed
proposals because 9 fleet SIM-REQUESTs + 2 owner asks rode the verdict lane);
steady-state pipeline lag ≈ 1 proposal. Verdict ruling split (parsed from all
72 `verdict:` lines): 23 approve · 20 reject · 12 null · 7 needs-more-evidence
· 6 conditional · 4 other (incl. V067 `invalid` — a registered gate that
honestly lost its own pre-committed coin flip).

## 2. Tooling used

| Tool / surface | How used | Verdict | Citation |
|---|---|---|---|
| Bash + local git | All measurement, ledger appends, byte-faithful rollovers | **reliable** | 772 commits; rollover verified by sha256 reconstruction (sim-lab PR #134) |
| GitHub MCP (PR/actions/branch tools) | THE GitHub path (direct `api.github.com` is proxy-walled) — 545-PR + 1,500-run exhaustive listings, PR opens, PR close-with-reason | **reliable** (with ~25 min read staleness + hard repo-scoping, §3) | gh metric snapshot 08:39–08:54Z; `docs/CAPABILITIES.md` walls |
| auto-merge enabler (Actions, `GITHUB_TOKEN`) | Merge-on-green for every PR post-install | **reliable** | ie 455 runs / 0 failures; sl 175 runs / 0 failures (§4) |
| `bootstrap.py check --strict` (substrate-kit) | Pre-push gate + CI substrate-gate on every PR | **reliable at CI, flaky locally** — local legs diverge from CI (§7 false-greens) | ASKs 002/003, accepted kit-side per fm ORDER 010 (`control/inbox.md`) |
| claude-code-remote MCP (triggers, `send_later`, `add_repo`, `send_message`) | Wake chain (pacemaker + failsafe cron), worker dispatch, lane-repo clones | **flaky** — self-bound: excellent; fresh-session cron: broken (§5) | `docs/ROUTINES.md`; zero missed wakes ~16 h (session-2 retro) |
| Write/Edit tools | All file authoring | **painful on one pattern** — REPORT-style filenames refused (§3) | sim-lab V038→V067 cards, ~10 reproductions |
| python3 stdlib sims | All 72 verdicts (hermetic, exact-arithmetic, twin evaluators) | **reliable** | sim-lab `sims/` — 72 subtrees, count parity with ledger |
| `raw.githubusercontent.com` + `git ls-remote` | Cross-repo reads/SHA-pins where MCP is out-of-scope | **reliable** | fm convention doc read at fm main (STEP 0, 2026-07-14); CAPABILITIES append log 2026-07-11 |
| Codex review bot (@codex) | External verdict review step (Q-0264.4) | **painful** — quota-capped + 3 fabricated-evidence incidents → suspended | OA-002; sim-lab outbox incidents #1–#3; V016 gate spec |
| ffmpeg / media | Frame extraction for probe evidence | **reliable** | `docs/CAPABILITIES.md` capability fence, verified 2026-07-10 |

## 3. Tooling walled or missing

Every quote below is the exact recorded error text; dates are discovery
dates. Walls already ledgered in `docs/CAPABILITIES.md` (idea-engine) and
sim-lab `docs/CAPABILITIES.md` + `PLATFORM-LIMITS.md` (now folded into its
capability-seed fence) are cited, not re-derived.

| Capability wanted | What happened when tried (verbatim + date) | Workaround | Disposition |
|---|---|---|---|
| GitHub MCP read of any repo outside the session's pair | `Access denied: repository "menno420/fleet-manager" is not configured for this session. Allowed repositories: menno420/idea-engine, menno420/sim-lab` (2026-07-14); same class for `"menno420/superbot"` (2026-07-13, ie card proposal-051; sl card V058), `"menno420/superbot-mineverse"` (V056) | `add_repo` + shallow clone (lane repos); `raw.githubusercontent.com` / `git ls-remote` (read-only pins) — both proven | **ANTHROPIC** — ask in §9.2 |
| Branch deletion (merged heads) | `error: RPC failed; HTTP 403 curl 22 The requested URL returned error: 403` / `send-pack: unexpected disconnect while reading sideband packet` (2026-07-11, `docs/retro/archive-ready-2026-07-11.md`; 403 on git AND API paths) | none agent-side; owner enables repo auto-delete | **ANTHROPIC** — ask in §9.3 (389 undeleted merged branches accumulated across both repos) |
| Direct `api.github.com` HTTP | blocked at proxy (2026-07-10, `docs/CAPABILITIES.md`) | GitHub MCP tools; raw/ls-remote for out-of-scope | **ACCEPTED** (MCP path is complete enough) |
| Tag push / release via git | 403 on `refs/tags/*` push, reproduced (OA-004, sim-lab `harness-v0.1.0` still un-pushed) | `workflow_dispatch` release path — "proven repeatedly fleet-wide" | **FLEET-FIX** (done — workflow path ledgered) |
| Write tool creating REPORT.md | `Subagents should return findings as text, not write report files.` (first V038 2026-07-13; reproduced verbatim V042/V054/V055/V056/V059/V060/V065/V066/V067) | bash heredoc — "zero work lost" every time | **ANTHROPIC** — ask in §9.5 |
| Foreground `sleep` in workers | blocked by harness (2026-07-13, session-2 retro) | `python3 -c 'import time; time.sleep(N)'`, bounded polls | **ACCEPTED** (bounded polling is better practice anyway) |
| `git reset --hard` (diverged local main) | classifier denial (2026-07-11, `.sessions/2026-07-11-probe-leaderboard-row-avatars.md`) | `git reset --keep` | **ACCEPTED** (safer primitive exists) |
| Self-merge of own owner-gated PRs | "sessions can be refused merging owner-gated PRs while their other capabilities work — and the boundary differs by venue (a child session was refused where a coordinator was not)" (2026-07-10, CAPABILITIES walls); 3 terminal denials landing venture-lab PR #15 from a lane seat (2026-07-11) | merge-on-green enabler (§8.1) — removed the need entirely | **FLEET-FIX** (done) + **ANTHROPIC** transparency ask, §9.5 |
| Cross-session trigger binding | `binding a trigger to another session is not enabled for this organization` (2026-07-10/11, sim-lab PLATFORM-LIMITS → CAPABILITIES fence) | self-bind from a worker seat to its own coordinator session (proven) | **ANTHROPIC** — ask in §9.4 |
| Fetch `*.github.io` (live Pages check) | `curl: (56) CONNECT tunnel failed, response 403` ×2 (2026-07-11T09:10Z, CAPABILITIES append log) | verify Pages from committed surfaces / target repo's own CI | **ACCEPTED** |
| GitHub `releases/download/` assets | 403 through proxy (2026-07-10 kit-upgrade card; re-confirmed 07-11) | git clone the source instead | **ACCEPTED** |
| Workflow retrigger on `GITHUB_TOKEN` pushes | checks never report (anti-recursion; evidence PR #138 card, 2026-07-11) | explicit re-dispatch or PAT/App token | **ACCEPTED** (GitHub platform design, not harness) |
| Codex external review | bot replies `reached usage limits` on every verdict PR (OA-002); separately 3 fabricated-evidence incidents (verbatim forensics in sim-lab `control/outbox.md` lines 163ff) | step suspended @ `dedc12e`; V016 measured authenticity gate (3/3 catch, 0/24 false alarms) ready if re-enabled | **ACCEPTED** (third-party quota; owner-click) — the fabrication *gate* is FLEET-FIX, done |
| Env/Project creation, console knobs (model class, branch-push, auto-fix) | owner-click only (CAPABILITIES walls, 2026-07-11; routine *arming* is NOT a wall — `create_trigger` proven agent-side) | six-field OWNER-ACTION asks, never wait silently | **ACCEPTED** |
| Stable denial semantics across sessions | P050's venture-lab source read denied once 2026-07-13 (quoted verbatim in claim + outbox per no-laundering rule), the SAME read succeeded 2026-07-14 (P054 card: walls "need re-probing at every session boundary") | re-probe at session boundary; record scope/TTL | **FLEET-FIX** (ledger grammar: add scope/TTL field) + ANTHROPIC transparency ask, §9.5 |

## 4. Merge & landing friction

All numbers measured over the full corpus (543 merged PRs, 592 + 278
substrate-gate runs, 455 + 175 enabler runs).

| Metric | idea-engine | sim-lab |
|---|---|---|
| Time-to-land (created→merged): median | **0.5 min** | **0.5 min** |
| p90 / mean | 4.5 min / 2.8 min | 18.8 min / 9.2 min |
| Worst | 8.58 h (#364 — deliberate overnight owner-sweep park) | 8.37 h (#116 — same audit-night park) |
| PRs needing >1 CI round (distinct head SHAs) | 76 of 401 branches (19%) | 40 of 133 (30%) |
| Red→green sequences on a branch | 42 | 15 (largely DESIGNED born-red holds, §7) |
| Enabler runs: success / skipped / **failed** | 396 / 59 / **0** | 173 / 2 / **0** |
| Green-but-unarmed stalls >30 min | **0** (max gap 8.2 min, #253) | **0** (max gap 7.1 min, #44) |
| Merged by github-actions[bot] (auto) | 313 (76.3%) | 83 (62.4%) |
| Merged under owner identity (owner-click dependency) | 97 — #1–#54 all pre-enabler, then tapering; only ONE after 07-12T14:26Z (#396) | 50 — #1–#50, i.e. every PR until the enabler landed via #50; **zero** after |
| Classifier denials on merge-path actions | 3 (venture-lab PR #15: REST self-merge + auto-merge ARM refused from a child seat, terminal; landing required a coordinator-seat merge under the owner's genuine turn — `.sessions/2026-07-11-venture-lab-self-landable-probe.md`; full verbatim text not preserved in-repo, §11) | 0 recorded |
| Abandoned branches (PR closed-unmerged) | 2 (`fix/session-log-2026-07-11` #85, `claude/verdict-060-…` #361, closed with cited reason 2026-07-14) | 0 |
| Merged-but-undeleted branches (hygiene, not abandonment) | 304 | 85 |

Recurring causes, dispositioned:

| Cause | Evidence | Disposition |
|---|---|---|
| Arm-at-open race (auto-merge squashes ~25 s after open, breaking multi-commit plans) | PRs #62/#64/#80 (merged in 24–25 s); heartbeat stamps exiled to follow-up PRs #198/#201/#206/#212 | **FLEET-FIX (done)** — PR #86 `521aebf`: enabler skips arming while the in-diff card is in-progress |
| Already-clean PRs never arm (enabler event coverage gap) | PR #209 sat green ~4 min, needed manual squash (`docs/current-state.md` § Ops facts) | **FLEET-FIX** — add a periodic sweep event to the enabler (unshipped; small) |
| Allowlist drift vs branch-naming mandate | PR #271 green + `mergeable_state: clean`, all 3 enabler runs SKIPPED (kit allowlist predated `claude/` mandate); silent-no-op class also caught at sl #50 install (empirical prefix survey) | **FLEET-FIX (done)** — #272 `daf9d50`; upstreamed as ASK 001, ACCEPTED kit-side (fm ORDER 010) |
| Dirty-PR zero-check-runs jam | first PR #33, recurrences #38 + 3 more (self-review retro) | **FLEET-FIX (done)** — doctrine in `control/README.md` § CI notes |
| SQUASH race splitting sim PR from trailing heartbeat commit | sl #38/#39, #40/#41 ("not harmful, forward-only, but noisy" — sl self-review) | **ACCEPTED** — forward-only follow-ups are cheap |
| Born-red hold = 1 extra push + 1 extra CI cycle per session PR | ~all 288 session PRs; 100% of sampled gate failures were this hold (audit doc 07-13) | **ACCEPTED** (designed; §7) |
| GraphQL auto-merge intermittently rate-limited | sl PLATFORM-LIMITS (V003/V009/V011 era) | **FLEET-FIX (done)** — REST merge-on-green proven fallback, then enabler |

## 5. Scheduling & wake friction

Doctrine home: `docs/ROUTINES.md` (idea-engine) — all incident-backed.

| Issue | Evidence | Disposition |
|---|---|---|
| Fresh-session-per-fire cron delivery failed | **0-for-2** vs 100% on self-bound crons/one-shot chains (2026-07-12 forensics, `docs/ROUTINES.md:17-24`) | **ANTHROPIC** — §9.4 |
| Trigger registry surfaced a different environment id than recorded at arm time | load-bearing suspect in the delivery failure (`docs/ROUTINES.md:25-29`) | **ANTHROPIC** — §9.4 |
| Triggers vanish with no tombstone | a "verified live" trigger gone within hours, unfired (`docs/ROUTINES.md:43-50`); deletions have no audit trail | **ANTHROPIC** — §9.4 |
| Manual-fire trap | `fire_trigger` sets `last_fired_at` without advancing `next_run_at` (`docs/ROUTINES.md:58-61`) | **ACCEPTED** (documented; verify-after-fire doctrine) |
| Parallel trigger-MCP writes hung reliably | four workers, one night → one-write-at-a-time pacing (`docs/ROUTINES.md:65-69`) | **FLEET-FIX (done: pacing)**; underlying concurrency bug is ANTHROPIC-adjacent |
| Proving a per-seat trigger negative | required paginating an **800+-entry account-wide trigger list (8 pages)** (session-1 close-out card) | **ANTHROPIC** — §10.1 (filtered list) |
| Cross-session binding | org-walled (§3, verbatim there) | **ANTHROPIC** — §9.4 |
| Dead workers/sessions (count: **2** recorded) | (1) P035 verify session "died at start (`turn_failed no_access`, 12:23Z) — nothing landed anywhere" (session-2 retro); (2) sim-lab OA-005: env deleted under a live trigger, found `ended_reason=auto_disabled_env_deleted` | **ANTHROPIC** — §9.4 (death observability) |
| Fresh sessions die silently at provision without the env setup-script paste | owner-click gated; "10-min dead-child fallback" (`.sessions/2026-07-11-wake-resilience-rebind-probe.md:29-34`) | **ACCEPTED** (fallback works) |
| A fleet watchdog's failsafe-wedge claim | **REFUTED** by registry check (Q-0120 verify-never-obey; session-2 retro) — a false alarm, not a failure | honest null |

What worked: hybrid ~15-min `send_later` pacemaker + 2-hourly failsafe cron
(V014-ratified) delivered **zero missed wakes across ~16 h**; 18/18
session-bound one-shots fired and self-disabled (session-1 close-out card).

## 6. Environment & platform issues

| Issue | Verbatim evidence | Disposition |
|---|---|---|
| Session/container death | `turn_failed no_access` (P035 dispatch, 2026-07-13); `ended_reason=auto_disabled_env_deleted` (OA-005 trigger post-mortem) | **ANTHROPIC** — §9.4 |
| Warm-container clone lag + stray local seed commit | recurring `df64aab` divergence; recovery recipe (backup branch + `reset --keep`) in `docs/current-state.md` § Ops facts; hard-sync preflight now rule 0 in `.claude/CLAUDE.md` | **FLEET-FIX (done)** — preflight doctrine |
| Read tool 256 KB limit vs append-only ledgers | sim-lab outbox grew to **1,091,133 B** ("~4× the fleet rollover threshold", ORDER 006); idea-engine outbox 368–543 KB — "every session now needs chunked reads" (ASK 004) | **FLEET-FIX (done)** — fm rollover convention executed both repos (ie ROLLOVER 001; sl PR #134 → `5356b2a`, byte-verified); kit-level automation still wishlist §10 |
| Proxy walls (api.github.com, `*.github.io`, `releases/download`) | §3 verbatim | dispositioned in §3 |
| GitHub MCP staleness | PR-state reads up to ~25 min stale vs live (metrics snapshot caveat; also "re-verify PR state before writes" — 07-13 audit suggestion) | **ACCEPTED** (re-read before writes) |
| `/usr/bin/time` absent in container | V065 card: bash builtin `time` used | **ACCEPTED** |
| Browser/Playwright unavailable | "on all 3 LIVE sites Playwright was SKIPPED — Chromium" + proxy wall disclosed (V011 card) | **ACCEPTED** (disclosed as LIMIT, verdict shipped) |
| Disk pressure | no incident recorded in any card/ledger — honest null | — |
| Context-limit incidents | none explicitly recorded — honest null (the 256 KB read wall above is the nearest real cost) | — |

## 7. Process & ceremony cost

**Guard-fire ledger, quantified** (idea-engine `.substrate/guard-fires.jsonl`,
443 entries over 4 days): `stance` 382 (advisory, zero blocked actions) ·
`stop-advisory` 46 · `session-log` 9 (blocking) · `reachable` 3 (blocking) ·
`owner-action-fields` 2 · `claims-stale` 1. **96.6% of all guard fires were
advisory stance/stop noise; 12 blocking fires in 4 days.**

| Ritual | Paid for itself? | Evidence |
|---|---|---|
| Born-red session card (red hold until flip) | **YES, at a price** — held at CI when the local ritual slipped (session-2 retro); price = 1 extra push + CI cycle × ~288 session PRs, and a misleading raw stat ("~27% CI failure rate… is in fact a designed, self-healing hold pattern" — 07-13 audit) | ACCEPTED by design; annotation wish §10.5 |
| ⟲ previous-session review (288/288 cards) | **YES** — caught the Q-id mislabel, the masked `claude/` allowlist gap, scoping gaps; functioned as the incident-propagation channel for the mtime corridor (V049 predict → V051 reproduce → V062 bite) | keep |
| Verbatim-quote / no-laundering discipline | **YES** — caught a wrong-ruling near-miss ("only the verbatim-quote discipline caught it", self-review retro); made this audit's §3 possible | keep |
| Claims protocol (one file per claim) | **YES** — 9 concurrent slices, zero collisions; measured ~98% → 0% conflict vs shared-append (claims README) | keep |
| Carve-out tripwires (gate-wiring, branch-prefix) | **YES** — caught kit-regen clobbers the 4th/5th time (#120/#125) | keep |
| Stance guard | **NO — pure tax**: 382 advisory fires, zero blocks | FLEET-FIX: tune or disable the stance heuristic |
| Stop-hook telemetry flush | **NO — was tax**: "13 one-line flush merges #58→#100 in ~3.5h" | FLEET-FIX (done) — exemption PR #108 |
| Heartbeat cadence | mixed: 175 heartbeat commits = **27% of all idea-engine commits**; arm-at-open squash forced stamp follow-up PRs; but heartbeats were the recon backbone for every audit incl. this one | ACCEPTED, with §10.2 (machine-readable seam line) |
| tracked `.substrate/guard-fires.jsonl` | **NO — conflict machine**: dirtied by every local check; first real merge conflict V053; V066 dirt rescue | FLEET-FIX: shard per session or untrack (parked recipe, V051 💡) |
| Verdict-card fixture duplication / registration prose | tax at the margin: "~40 lines of single-block registration prose… no single sentence independently citable" (V056 ⟲); "friction was self-imposed prose length" (V070) | FLEET-FIX: session-type-aware card skeleton (parked) |

**Checker false-greens/false-positives caught (all real, all disclosed):**
mtime-newest false-green corridor (ASK 003; predicted V049 → reproduced live
V051 → **bit** V062 and V067 — CI stayed correct because the kit gate keys on
the diff-touched card) · local-green-CI-red ×2 (inbox leg needs
`--inbox-base` #274; CI `check_ideas` stricter #299 → ASK 002) ·
`check_gate_wiring` proven false-green class, caught by the lint bundle's
added leg (`GREEN (false-green confirmed)` fixture) · `&&`-chain masking an
exit code shipped one red card flip (sl #90/#91) · grep-fingerprint
verify-first returning false MOOT on mutated premises ("verify the invariant,
not the artifact") · `check_sections.py` broken mid-session by fm roster
regen, fixed forward same-session `a52a704` → ASK 005. ASKs 001–003 are
ACCEPTED kit-side (fm ORDER 010) — the local/CI convergence fix is in flight
upstream.

## 8. What we fixed ourselves

1. **Merge-on-green enabler, both repos** — ie `.github/workflows/auto-merge-enabler.yml` (wired + allowlist #55 `5b8fca7`, provenance stamping #64 `d218550`); sl mirrored with an empirical prefix survey of PR heads #1–#49 (PR #50 → `e11ed40`). Result: 396 bot merges, **0 enabler failures**, zero agent merge calls post-install.
2. **Arm-at-open race guard** — skip arming while the in-diff card is in-progress; live-fired on itself (PR #86 `521aebf`).
3. **`claude/` allowlist fix + upstream** — #272 `daf9d50`, then ASK 001 accepted into the kit template (fm ORDER 010).
4. **Stop-hook telemetry exemption** — ended the flush treadmill (PR #108 `b53c01f` + `scripts/patch-stop-hook-git-check.sh`).
5. **Claims protocol** — one-file-per-claim, structurally conflict-free; enabled 9-way concurrency with zero collisions (`control/claims/README.md`).
6. **Outbox rollovers, byte-verified** — ie ROLLOVER 001 (P001–P057 → dated archive); sl 1,091,133 B → 41,974 B with sha256 reconstruction proof (PR #134 → `5356b2a`).
7. **Sim harness v0.1 + hardening conventions** — `harness/simharness.py`; fixtures-before-runner, twin independently-written evaluators, pre-registered REJECT-first rules, seed high-water registry (sl archive-ready retro; V046+ cards).
8. **External-review authenticity gate (measured)** — V016's 270-cell sweep: catches 3/3 recorded @codex fabrications at 0/24 false alarms (sl `control/outbox.md` VERDICT 016).
9. **Repo checkers + lint bundle** — `scripts/check_sections.py`/`check_ideas.py`/`check_harvest.py`/`preflight.py` incl. the false-green-catching leg (`.sessions/2026-07-11-lint-bundle-build.md`).
10. **Walls ledger discipline + capability-seed fence fold** — venue-tagged walls with exact error text, discovery rule, scope/TTL lesson; sl fence restored + 6 lane walls folded, seat digest renders non-empty (ORDER 007, sl PR #136 → `b10ffce`).

## 9. Top 5 remaining pains (ranked)

1. **Local gate ≠ CI gate** (mtime false-green corridor + missing legs) — bit
   real sessions 4× (V051/V062/V067, #274/#299). **FLEET-FIX (in flight
   upstream)**: ASKs 001–003 ACCEPTED kit-side per fm ORDER 010; evidence
   standard = next kit-upgrade PR converges local `check --strict` with CI.
2. **GitHub MCP hard repo-scoping** — every cross-repo read (fleet-manager
   conventions, lane sources for harvests) hits `Access denied: repository
   "…" is not configured for this session`; workarounds exist but cost a
   probe + fallback every time. **ANTHROPIC — exact ask:** *"Allow GitHub MCP
   read-only operations (get_file_contents, list_commits, search) on all
   repos the installed GitHub App can already see, keeping write scoping
   session-pinned — or add a session-config knob to extend the read
   allowlist. Verbatim wall: `Access denied: repository
   "menno420/fleet-manager" is not configured for this session. Allowed
   repositories: menno420/idea-engine, menno420/sim-lab`."*
3. **Branch deletion 403 on every path** — 389 merged-but-undeleted branches
   accumulated in 3.6 days across two repos. **ANTHROPIC — exact ask:**
   *"Permit agents to delete the head branch of a PR that is already merged
   (narrowest safe scope), or surface GitHub's 'automatically delete head
   branches' repo setting as an agent-visible/owner-one-click action.
   Verbatim wall: `error: RPC failed; HTTP 403 curl 22 The requested URL
   returned error: 403` on `git push origin :branch` and the API path."*
4. **Scheduling opacity** — fresh-session cron 0-for-2, triggers vanishing
   without tombstones, registry env-id mismatch, silent session deaths
   (`turn_failed no_access`, `auto_disabled_env_deleted`), cross-session
   binding org-walled. **ANTHROPIC — exact ask:** *"Give Routines an audit
   trail (creation/fire/disable/delete events with reasons, queryable), make
   fresh-session-per-fire failures observable instead of silent, expose
   `ended_reason` at delete time, and enable cross-session trigger binding
   org-wide or say why not. Verbatim wall: `binding a trigger to another
   session is not enabled for this organization`."*
5. **Policy-boundary opacity** (classifier + tool policy) — merge refusals
   differ by venue/session-kind with no queryable rule; `Subagents should
   return findings as text, not write report files.` fired ~10× against
   coordinator-ordered report files; one source-read denial proved transient
   (P050 vs P054) with no way to know its TTL. **ANTHROPIC — exact ask:**
   *"Publish (or expose via API) the effective policy for a session: which
   merge/write actions its kind is allowed, and make tool-policy refusals
   carry a stable reason code + scope (session/org/permanent) so agents can
   ledger walls with a TTL instead of re-probing. Verbatim examples:
   `Subagents should return findings as text, not write report files.`; a
   child session refused a REST merge where a coordinator was not."*

## 10. Wishlist

Ranked; deduped against §3/§9 (MCP scoping, branch deletion, the scheduling
audit trail, and policy transparency are already asked there, not repeated).

1. **Filtered trigger listing** — a `session_grouping_id`-filtered
   `list_triggers` "would turn an 8-page enumeration into one call" (proving
   one seat-negative required paging 800+ account-wide triggers).
2. **Machine-readable session handoff** — "give the ender a 'seam manifest'
   line-format the successor can machine-read" instead of parsing prose
   heartbeats (session2-ender card).
3. **Kit: first-class append-only ledger rotation** — the outbox wall was hit
   independently by BOTH repos and the 07-13 auditor called it fleet-generic;
   the fm convention now exists — automate it in the kit (threshold check +
   roll script), don't re-execute it by hand per seat.
4. **Denial-ledger TTL/scope grammar** — walls entries carry scope + verified
   dates; add an explicit re-probe horizon so transient denials (P050→P054)
   don't ossify into imagined permanent walls.
5. **CI-status annotation for designed holds** — let a workflow mark a
   failing run "designed hold" so born-red reds stop reading as CI failures
   to external reviewers/tooling (the 07-13 audit had to explain the ~27%
   "failure" rate in prose).
6. **Read tool: chunked/streaming reads past 256 KB** — append-only ledgers
   are a legitimate repo pattern; today every big-file read needs manual
   offset arithmetic.
7. **Enabler-allowlist conformance check** — "so doctrine and automation
   can't drift apart silently" (the PR #271 jam would have been caught at
   #54/#55 already).

## 11. Honest gaps

- **V073 (P062) verdict state at live HEAD: IN FLIGHT, not interfered with.**
  sim-lab PR #135 ("VERDICT 073: P062 owner-queue attention-order
  simulation", branch `claude/verdict-073-owner-queue-attention-order`, head
  `673d133`, base `5356b2a`) was OPEN at 2026-07-14T09:01Z — created
  08:50:52Z, born-red discipline per its body; builder claim landed
  idea-engine PR #412 → main `b8173be` (08:42Z). Its outcome is outside this
  audit's window by design.
- **STEP 0 parked items: none.** PR #361 closed-with-reason (cited comment,
  2026-07-14); sim-lab ORDER 006 done (PR #134 → `5356b2a`, outbox 41,974 B
  < 200 KB, byte-verified); ORDER 007 done (PR #136 → `b10ffce`, fence
  non-empty, digest renders). Nothing long-running was left un-parked.
- **Owner-click vs PAT indistinguishable**: the 147 owner-identity merges
  could be UI clicks or PAT-armed auto-merge; no available data separates
  them (enabler token is `ROUTINE_PAT || GITHUB_TOKEN`; ROUTINE_PAT never
  set, so post-enabler bot attribution implies GITHUB_TOKEN — pre-enabler
  merges remain ambiguous in principle, though #1–#54/#1–#50 predate any
  automation).
- **Conflicted-branch state not measured** — determining merge-conflict
  status of 389 stale branches would require attempting each merge; no
  closed-unmerged PR cites conflicts in metadata.
- **idea-engine worker Write-refusal verbatim text lost** — the ~8
  idea-engine worker refusals' exact text lives only in a close-out PR body
  ("exact denial text preserved in the close-out PR body", session-2 retro);
  only sim-lab preserved it in-repo (§3 quotes the sim-lab text).
- **Lost time in minutes: not measured anywhere** — no card quantifies
  minutes lost to any wall; the ledgers record incidents and "zero work
  lost" qualitatively only.
- **Venture-lab merge-path denials verbatim text not in-repo** — the 3
  terminal denials are ledgered as facts + paraphrase, not exact text
  (`.sessions/2026-07-11-venture-lab-self-landable-probe.md`).
- **Live-sibling measurement holes** — 2 sim-lab workflow runs (gate 278→280,
  enabler 175→177 during pagination) and branches/PRs created after ~08:54Z
  are not in the metrics dataset; GitHub MCP reads may be ~25 min stale.
- **WAKE-DEAD / ENV-DEAD markers: 0 hits** in either repo (working trees +
  all 175 idea-engine status.md historical versions) — those marker classes
  were never used by this seat; honest null, not an absence of deaths (the 2
  known deaths are ledgered under other vocabulary, §5).
- **Per-PR `merged_by` for all 543 merged PRs**: not individually queried;
  measured via push-event run actors (bot merges trigger no push run),
  validated 5/5 against direct spot-reads.
