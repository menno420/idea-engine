# Story bubble-texts as a committed content feed — owner voice grows without a code session

> **State:** parked(build-direct — first-commit content/code-separation constraint on the P002 phase-1 story page, not an independent build surface; fold "narrative lives in ONE committed content file (chapter texts + speaker-attributed bubble asides, stable chapter-ID anchors), rendered honest-empty, page code never embeds prose" into the phase-1 story-page ORDER when the manager routes it — deviation upheld, see probe report)
> **Class:** product · **Target:** `menno420/websites`
> **Sequence:** before websites builds P002 phase-1 story page commit #1 — the narrative-feed shape is decided at that page's first commit; the lane's revealed default is narrative hardcoded in code (`review/story.py` @ `8f97654`)
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/698fd93869f8a05200f26fde45bbd71596323e6a/ideas/websites/superbot-site-stats-data-story-2026-07-10.md@698fd93 · fetched 2026-07-10T22:08Z
> **Grounding:** https://github.com/menno420/websites@0cd08d2da1580fffff1595a6f4119b6d98a8b4b3 · fetched 2026-07-10T22:08Z (manifest row: behind)
> *(pin annotation: lane HEAD via `git ls-remote`; the manifest websites row @ superbot `9624c53` still records close-out #58/`d493792` 13:57Z + kit v1.6.0 while the lane heartbeat @ `0cd08d2` reads #75 @ 21:58Z + kit v1.7.1 — staleness datapoint #8, relayed on the heartbeat)*

## Problem

The one part of the story page (PROPOSAL 002 phase 1) that agents cannot
generate is the part the owner asked for by name: "bubble texts etc., to really
bring the reader into the story" (idea §1) — the voice-of-the-owner /
voice-of-the-agent asides (§2). Hardcode that narrative in page templates and
every new owner aside costs a websites code session; the owner is the program's
scarcest resource, and the probe's Q4 already flags scrollytelling as "an
unbounded design sink" — content/code coupling is half of that sink. The
original idea itself reached this repo as a chat aside relayed by the dispatch
copilot; the story's future asides will arrive exactly the same way.

## Idea

Separate the narrative from the page: one committed content file (small
schema — chapter texts, bubble asides with a `speaker: owner|agent` attribution
and an anchor to a scroll position or graph moment) that the story page renders.
A new owner aside is then a one-line content commit — landable by ANY session or
relayed straight from owner chat by the copilot, no template work, no design
decisions reopened. This is not a new pattern for the lane, it is its own
doctrine applied to prose: committed generated/authored artifacts, rendered
live, "never fake data" (`dashboard/data_source.py`), honest empty states when a
chapter has no asides yet. The story page becomes append-cheap for the two
voices that matter while its code stays frozen.

**Why now:** cheapest decided before the story skeleton (the probe's smallest
shippable slice, routable now) hardcodes its first chapter — and the lane's
proven 4-hourly wake + continuous send_later chain means content commits get
picked up and deployed with no human in the render loop.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://github.com/menno420/websites@8f9765483a7df57ce426e7d11d200f10b5495ed7 · fetched 2026-07-12T01:12Z
> *(pin annotation: live lane HEAD by `git ls-remote refs/heads/main` this probe,
> then blobless-cloned and tree-scanned this session — BYTE-IDENTICAL to the HEAD
> the pulse-feed probe (PR #222) cloned 2026-07-11T23:57Z and the explorer-facets
> probe (PR #225) pinned 2026-07-12T00:33Z, so the lane has not moved across all
> three P002-family probes; every #222/#225 whole-tree finding carries over to
> this exact commit and was independently re-checked here where load-bearing.)*
> **Sequence:** before websites builds P002 phase-1 story page commit #1 — the
> narrative-feed shape is decided at that page's first commit

> Single-pass battery (panel not escalated: docs/design-constraint surface,
> reversible, no security/data/spend/public blast radius — README § probe
> battery). This probe is ALSO the flagged review of the fourth ledger's TOP-5 #5
> DEVIATION from the Q-0259 "websites below superbot" weighting (coordinator flag
> (a) on the fourth mint): each deviation pin is re-verified below and the
> recommendation carries an explicit deviation ruling.

*Timeliness verified live FIRST (the PR #25 lesson). At websites HEAD `8f97654`
(re-resolved by `ls-remote` 2026-07-12T01:12Z, blobless clone + full-tree scan
this session): the P002 phase-1 story page is UNBUILT — the only story-shaped
files in the tree are the review service's (`review/story.py`,
`review/gen_snapshot.py`), a different page for a different audience — and
UNROUTED: `control/inbox.md` carries ORDERs 001–011 with ZERO matches for
story/bubble/narrative/scrolly, despite VERDICT 003's explicit "phases 1–2 … do
NOT wait" (sim-lab `control/outbox.md` @ `8713f26`, recorded in the parent idea's
Sim verdict section). NEW measured datapoint, decisive for this capture:
`review/story.py`'s own module docstring declares "Curated narrative — the
process/successes/problems record … lives here" — the lane's ONE shipped
story-shaped page hardcodes its entire narrative (owner/agent explainer rows,
Q&A prose, chapter copy) inside the Python module. The lane's revealed default
for narrative is code-coupled prose; without a folded constraint, the story
page's first commit does the same to chapter 1 and every future owner aside
costs a code session.*

**1. What is this really?**
A first-commit CONTENT/CODE-SEPARATION constraint on the P002 phase-1 story
page, not an independent build item — and, stated explicitly: the THIRD RIDER of
the same PROPOSAL 002 routing family, after
[`fleet-program-pulse-feed-2026-07-10.md`](fleet-program-pulse-feed-2026-07-10.md)
(phase-1 rider, the page's generated-NUMBERS half, PR #222) and
[`contract-driven-explorer-facets-2026-07-10.md`](contract-driven-explorer-facets-2026-07-10.md)
(phase-2 rider, PR #225). This file is the phase-1 page's NARRATIVE half: the
one part of the story page agents cannot generate — the owner's "bubble texts"
(§1 of the parent capture, the owner's own words) — moved out of page code into
one committed content file (chapter texts + asides with `speaker: owner|agent` +
a stable anchor), so a new owner aside is a one-line content commit relayable
straight from owner chat by the dispatch copilot. Who it is for: the owner (his
voice grows without a code session — he is the program's scarcest resource), the
websites lane (story-page code freezes after commit 1), and the copilot relay
path the original idea itself arrived through.

**2. What is the possibility space?**
- **Where narrative lives:** hardcoded in templates/module (the lane's revealed
  default — `review/story.py` @ `8f97654` does exactly this, measured above) →
  ONE committed content file with a small schema (chapters + speaker-attributed
  asides + anchors; the capture's ask) → per-chapter content files (more files,
  same doctrine — a rendering detail, not a fork) → a CMS/admin surface
  (rejected: new service + auth surface, against VERDICT 003's zero-auth phase-1
  clearing and the lane's committed-feed doctrine).
- **Anchor semantics:** scroll positions (rejected: page-redesign-fragile) →
  graph moments (fragile the same way) → stable chapter IDs the page defines
  once (the survivable floor; an aside anchored to a missing ID renders in the
  chapter's honest-empty aside rail, never dropped silently).
- **Voice integrity:** `speaker: owner` entries must be RELAYED owner words, not
  agent-authored owner voice — the "never fake data" doctrine
  (`dashboard/data_source.py` @ `8f97654`) applied to prose; agent asides carry
  `speaker: agent` honestly.

**3. What is the most advanced capability reachable by the simplest implementation?**
One committed content file (JSON/YAML: `chapters[{id, text, asides[{speaker,
text, anchor}]}]`) plus one render loop in the story page and an honest-empty
state per chapter — the same committed-artifact shape the lane renders
everywhere already. That alone buys the advanced capability: the story page's
narrative becomes append-cheap for the two voices that matter, landable by ANY
session or relayed from owner chat with zero template work and zero design
decisions reopened, while the page code stays frozen. The lane's proven
4-hourly wake + continuous chain (measured self-serve latencies: ~19 min /
14 min per the README's #49/#51/#53 cards) then deploys content commits with no
human in the render loop. Measured caveat, not guessed: WHICH moments deserve
asides is judgment the schema cannot encode — the file makes asides cheap, not
automatic.

**4. What breaks it?**
- **Sequencing (decisive):** the constraint is worthless the day after the story
  page hardcodes chapter 1. Two same-class datapoints say the lane WILL default
  that way at pace: the pulse-feed window half-closed on an unpredicted page
  between capture and probe (PR #222), and `review/story.py` already shipped
  narrative-in-module once. The Sequence pin above is the guard; the phase-1
  ORDER is the only carrier that reaches the lane in time.
- **Deviation-evidence audit (the TOP-5 #5 flag, each pin re-verified):**
  (a) window class half-closes at lane pace — SOUND: PR #222's probe report read
  this session, plus the independent `review/story.py` narrative-in-code
  datapoint measured above; (b) VERDICT 003 cleared phases 1–2 and routing still
  absent — SOUND: verdict text at sim-lab `control/outbox.md` @ `8713f26` (via
  the parent's Sim verdict section), inbox re-greped LIVE this probe at
  `8f97654` (11 ORDERs, zero story-shaped); (c) narrative-feed shape decided at
  the page's first commit — SOUND: the page does not exist in the tree, so its
  first commit has not happened; the window is verifiably still OPEN.
- **Anchor drift:** asides anchored to page structure dangle when the
  scrollytelling design iterates — stable chapter IDs + honest-empty fallback is
  the floor; anything fancier re-couples content to code.
- **Fake owner voice:** an agent writing `speaker: owner` prose is the BUG-0022
  silent-desync class applied to trust in the page itself; the relay-only rule
  (Q2) is the guard.

**5. What does it unlock?**
The story page's narrative grows at chat pace instead of code-session pace —
the owner's voice becomes an append-only committed feed exactly like the lane's
data. The copilot relay path (owner chat → one-line content commit) closes the
loop the original idea itself traveled. And the phase-1 ORDER becomes symmetric:
the pulse-feed rider covers the page's generated numbers, this rider covers its
authored prose — one committed-artifact doctrine for both halves, page code
frozen after commit 1.

**6. What does it depend on?**
- The manager routing PROPOSAL 002 phase 1 to websites (VERDICT 003 cleared it
  explicitly; verified still unrouted at websites `control/inbox.md` @ `8f97654`
  this probe) — the constraint's only carrier, same as both sibling riders.
- NOT a dependency: auth, databases, the read-only API, the fm ORDER 012/013
  contract fan-in, any new service — one static content file + a render loop.
  Zero owner clicks; the owner's asides are the PAYLOAD, not a gate.
- Cost, priced honestly: as a folded constraint, ~zero — one instruction line in
  the phase-1 ORDER plus the content file being the FIRST implementation instead
  of an extraction refactor later; this probe itself was docs-only (one
  `ls-remote`, one blobless clone, three greps).

**7. Which lane should build it — and what does it displace or duplicate?**
**websites** implements it (inside the phase-1 ORDER); **nobody** builds
anything from THIS file — it is a constraint rider, and explicitly the third
one on the same P002 routing. Dedup findings, named (repo-wide
`rg -il 'story|bubble|narrative|feed'` over `ideas/`, kit machinery excluded,
this session):
- SAME PAGE, OTHER HALF: [`fleet-program-pulse-feed-2026-07-10.md`](fleet-program-pulse-feed-2026-07-10.md)
  — parked(build-direct) riding the SAME phase-1 routing (PR #222); it is the
  page's generated-numbers half, this is the authored-prose half. Not a
  duplicate — disjoint payloads, same carrier — but the manager should fold BOTH
  riders into ONE phase-1 ORDER line-pair rather than two separate instructions.
- SAME SHAPE, OTHER PHASE: [`contract-driven-explorer-facets-2026-07-10.md`](contract-driven-explorer-facets-2026-07-10.md)
  — parked(build-direct), the phase-2 twin of this ride-the-routing move
  (PR #225); its "columns+search from v1 today" split has no analog here (this
  constraint is whole from day one).
- PARENT: [`superbot-site-stats-data-story-2026-07-10.md`](superbot-site-stats-data-story-2026-07-10.md)
  (PROPOSAL 002) — §1's "bubble texts" is the owner's own phrase this capture
  extracts; its probe Q4 already flags scrollytelling as "an unbounded design
  sink", of which content/code coupling is half.
- DOCTRINE-RELATED ONLY: [`public-leaderboards-committed-feed-2026-07-10.md`](public-leaderboards-committed-feed-2026-07-10.md)
  (committed-feed doctrine on game data) and the websites lane backlog
  ([`lane-backlog-2026-07-10.md`](lane-backlog-2026-07-10.md) — greped: zero
  story/bubble/narrative bullets, no lane-side overlap).
- No other narrative-content-file or bubble-text mechanism exists anywhere in
  `ideas/` (grep above); the review service's hardcoded narrative is the
  ANTI-instance, not a duplicate.

**8. What is the smallest shippable slice?**
No independent slice ships from this file. The deliverable is ONE instruction
folded into the manager's phase-1 story-page ORDER when it routes (paired with
the pulse-feed rider's exporter line): "the story page's narrative — chapter
texts and bubble asides — lives in ONE committed content file (schema:
chapters + asides with `speaker: owner|agent` and a stable chapter-ID anchor),
rendered with honest-empty states; page code never embeds prose; `speaker:
owner` entries are relayed owner words only; a new aside must land as a
content-only commit, proven by a fixture test." If phase 1 somehow builds
before the ORDER carries this, the constraint dies and the extraction refactor
becomes lane-priced follow-up work — that is the reversibility the deviation
flag named.

**Recommendation: park** — build-direct, as a first-commit content/code
separation constraint folded into the P002 phase-1 story-page ORDER: no
simulator question exists (rendering a committed content file is deterministic
and trivially demonstrable — judgment/routing only, the PR #222/#225 precedent),
the first-commit window is verified still open (no story page at websites
`8f97654`, phase 1 unrouted, inbox re-greped live), and the best implementation
found is the Q8 fold-in — one committed narrative file with speaker-attributed,
chapter-anchored asides, honest-empty states, relay-only owner voice — paired
with the pulse-feed rider in the same ORDER. **Deviation upheld**: all three
TOP-5 #5 evidence pins re-verified sound this probe — (a) two same-class
datapoints of the window closing at lane pace (PR #222 + `review/story.py`'s
hardcoded narrative), (b) VERDICT 003 clearance with routing still absent at
live `8f97654`, (c) the page's first commit not yet made — and the probe's
output had to exist BEFORE the routing lands, which can be any wake; yes, this
is the third rider of the same routing (Q7, stated), and with it the P002
fold-in family is CLOSED — no fourth rider candidate exists in the section.

## Groom (2026-07-12 story-window re-check)

> **Grounding:** https://github.com/menno420/websites@d67eaaddc6b6c6a4fb53bb633849e3a05b1b6e8c · fetched 2026-07-12T16:21Z
> *(pin annotation: grooming re-verification, NOT a re-probe — dispatched after
> the lane's 2026-07-12 ORDER 017 burst (39 commits `8f97654` → `d67eaad`, HEAD
> committed 16:06Z) landed story work; `review/story.py` read IN FULL at
> `d67eaad` (769 lines, blob `b35ad65`) and diffed locally against `8f97654`
> (505 lines), `50dd661` (ORDER 017 A, websites PR #175, +116) and `d7721bb`
> (ORDER 017 C homepage rebuild, websites PR #180, +156); `control/inbox.md`
> read in full at `d67eaad` (ORDERs 001–020); full `git ls-tree -r` stem scan
> for story/scrolly/narrat/bubble/chapter. HEAD moved once more DURING the
> re-check — `3bfdf18`, websites #187, `app/`-only by `--stat`, orthogonal —
> so the pin stays at the dispatched head.)*

**VERDICT: window OPEN — the ORDER 017 story work was orthogonal to this
rider's carrier.** The burst refreshed and rebuilt the REVIEW service (inbox
ORDER 017 @ `d67eaad`: "Refresh and upgrade the public program-review site
(review-production-f027)… the Anthropic Claude Code team is reviewing it this
week") — the probe's named ANTI-instance, "a different page for a different
audience". The P002 phase-1 story page's first commit has still not happened:

- **Page still UNBUILT:** the only story-shaped file in the whole `d67eaad`
  tree remains `review/story.py` (full-tree stem scan above); no
  scrollytelling page, no chapter/bubble file, no content-file seam for
  narrative anywhere. (`review/data/questions.json` + `load_questions` are the
  Q&A ledger and pre-existed at `8f97654` — data, not chapter narrative.)
- **Routing still ABSENT:** inbox @ `d67eaad` grew ORDERs 012–020 today; zero
  are P002/story-page-shaped (greps: `scrolly|bubble|narrative` = 1 hit,
  "reviewer narrative" inside ORDER 017 A's source list; `story` hits are the
  review site's "scale story"/"story in brief"). The literal token "P002"
  appears nowhere in the websites tree — the phase naming is this repo's, so
  its absence is expected and carries no signal either way.
- **First-commit shape NOT decided:** there is still room for the content-feed
  mechanism to be the story page's commit #1; nothing built today constrains
  it.

**The constraint got MORE necessary, not less:** all +272 gross new
`review/story.py` lines are hardcoded module literals (the 07-12 incident
`PROBLEMS` entry with its evidence URLs, `START_HERE` cards,
`GENERATIONS_TILE`, `site_map`, `EVIDENCE_LINKS`) — the revealed
narrative-in-code default's third and largest same-class datapoint, landed at
burst pace under an owner deadline. Two NEW window threats, measured: (1)
websites ORDER 016 @ `d67eaad` ("find all website related plans across the
multiple repos and execute all the important ones") is a lane-initiated path
that could surface PROPOSAL 002 and start the story page WITHOUT the
manager-routed phase-1 ORDER this rider waits on; (2) the lane's new
auto-merge-enabler (websites #167, `f14aeaa` — green `claude/*` PRs land
themselves) plus today's measured burst pace means any story-shaped start
closes the window in hours.

**Manager-flag status (the standing "fold BOTH riders into ONE ORDER on the
phase-1 carrier" flag): AMEND.** Replacement text, verbatim: "Fold BOTH
riders — the pulse-feed exporter line (parameterize `review/gen_snapshot.py`'s
walk + the fleet rollup) and the story-bubble narrative line (ONE committed
content file, `speaker: owner|agent`, stable chapter-ID anchors, honest-empty
render, page code never embeds prose) — into ONE ORDER on the P002 phase-1
story-page routing, unchanged in substance; AND, new tripwire: websites
ORDER 016 can surface P002 and start the story page lane-side without that
routing — if the lane self-starts story-page work under ORDER 016 (or any
order), inject both rider lines into that work item immediately; with the
lane's auto-merge-enabler live (websites #167), the fold-in is hours-scale
time-sensitive from the first story-shaped commit."

State unchanged: `parked(build-direct)` stands, Sequence pin stands (no
re-badge; groom precedent PR #244).
