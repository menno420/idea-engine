# Session — single-pass probe: superbot channel-deployed-component-menu primitive

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot/channel-deployed-component-menu-primitive-2026-07-10.md` —
the ONE-primitive claim (build-in-panel → post-to-channel → persist
message_id → re-attach on restart) said to unlock role menus + starboard +
polls as thin consumers. The briefed question was the STALENESS check:
pin `fd638e3` (canonical doc 2026-06-21) vs live superbot HEAD — is the
primitive still unbuilt?

Verify-first, live, tree-scanned: superbot HEAD S resolved by
`git ls-remote` 02:00:30Z = `1ecc21138fe0a1eb672d03b66bd319164c29d55f`
(the SAME S the #228/#232 probes measured; canonical doc byte-identical
`fd638e3`→S, md5 match), inspected via a depth-1 clone at S;
superbot-next HEAD N = `af985c17def5ff2478103cb363ebb150cb583a97`
(moved past the #232 probe's `cc59a6e`; decisions.md re-read fresh).
The decisive facts: (a) the NAMED primitive is ABSENT — stem-matched
`rg "deploy_component|deployed_message|component_message"` over the S
tree = zero hits; (b) but the LIFECYCLE shipped consumer-private: role
menus carry the full claimed shape as their own code
(`RoleMenuView(PersistentView)` role_menu_view.py:232; builder post +
persist `set_menu_location` role_menu_builder.py:382 +
`add_view(view, message_id=…)` :383/:911/:952; boot re-attach
`reattach_role_menus` role_menu_view.py:447-483, docstring "Mirrors
``message_anchor_manager.restore_anchors``…", wired bot1.py:343-345;
plan header "PR 2 MERGED (#1219)"); (c) starboard shipped
reaction-based — raw-reaction listeners starboard_cog.py:39/:46, own
`starboard_message_id` rows utils/db/starboard.py:81-96, NO components,
no view to re-bind; (d) polls: legacy `!poll` utility_cog.py:298 only,
AG-15 suggestion box unbuilt; (e) rebuild side at N `af985c1`: D-0040
ported the role family into N's own grammar (`role_menus`+options
stores, `role.hub` panel), D-0062 re-routed `!rolemenu` at
`PanelRef("role.hub")`, starboard + utility named not-yet-ported —
a generic seam at N would be minted in N's grammar, not this helper.

Verdict: **parked(mooted-in-part)** — the extraction the doc justified
at consumer #1 lost its window (PR 2 merged without it; consumer #2
arrived component-less), so per the doc's own second-copy rule it waits
for a second channel-deployed component consumer at S. Today's
fourth-mint pattern held again: part-built — the LIFECYCLE shipped, the
ABSTRACTION did not. Nothing sim-shaped (refactor-economics judgment,
no numeric parameter space); NO outbox proposal, outbox tail unchanged.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this born-red
first commit carries the `ideas/superbot/` collision flag per the PR
#222/#225/#226/#228/#232 workflow convention.

## Close-out

**Evidence (hand-written):**

- ideas touched (2): `ideas/superbot/channel-deployed-component-menu-primitive-2026-07-10.md`
  (state flip captured→parked(mooted-in-part…) + probe report append),
  `ideas/superbot/README.md` (index bullet re-badge, built-half/open-half
  split per the PR #189 card duty + re-open trigger per PR #192)
- sessions touched (1): `.sessions/2026-07-12-channel-deployed-component-menu-probe.md`
- code touched: none · control touched: none (dispatch boundary)
- git: branch `probe/channel-deployed-component-menu` off main `485b45e`,
  born-red card first commit `5b8e1fe`, probe+close-out commit follows;
  draft PR flipped ready on green per dispatch instructions.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park, mooted-in-part).
  One pricing call, declared: this was NOT filed as reject — the premise
  (one seam beats three hand-rolls) stays true in principle, but its
  trigger condition regressed from "second consumer on the backlog" to
  "second consumer actually landing", so the head parks on the doc's own
  extract-at-second-copy rule with role menus named as the refactor donor.
- Next session should know: S now carries THREE sibling re-attach paths —
  `restore_anchors` (per-user panel anchors, bot1.py:339),
  `reattach_role_menus` (public role menus, bot1.py:343-345), and any
  future consumer would be the third copy that justifies extraction.
  The fun-and-ease (§B1 starboard) and superbot-vision (AG-15 polls)
  probes should carry this report's consumer findings instead of
  re-scanning.

## 💡 Session idea

A link-index whose canonical doc names its consumers should get a
per-consumer build-status line at HARVEST time, not probe time: this
probe's entire verdict reduced to three lookups (consumer #1 built?
#2 built? #3 built?) that a harvest slice could have stamped as a badge
in seconds with the tree already open — the "extract at consumer #N"
idea class moots by consumers shipping, and a consumer-status badge
turns its staleness check into a scan.

## ⟲ Previous-session review

PR #232 (visual-card-engine-vision probe): adopted — (a) its same-S carry
discipline paid again: S had NOT moved (`1ecc211` still HEAD at this
session's 02:00Z ls-remote), so the #228/#232 S-pin carried and only N
needed a fresh read (it HAD moved, `cc59a6e`→`af985c1` — the freshest-wins
rule from README applied); (b) the born-red-card collision flag (no claim
file under the dispatch boundary) used verbatim; (c) its md5 byte-identity
check on the canonical doc reused (`03240bc6…` both pins). Deviation from
its shape, declared: this card was hand-written from the first commit —
the #225/#226/#232 cards all report the kit auto-draft close-out firing
against a wrong diff base, so no auto-draft was relied on here.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) ·
  docs-only probe slice (one probe append + state flip + index re-badge +
  card; no code)

## Handoff → next wake

Re-open triggers on future superbot re-pins: a NEW
`bot.add_view(..., message_id=...)` call-site family outside
`disbot/views/roles/` (second consumer landed → extraction justified), a
components-based starboard/poll module appearing, or
`deploy_component_message` appearing anywhere (lane self-served → flip
toward historical). Guard recipe:
`git ls-remote https://github.com/menno420/superbot.git HEAD`, then
`rg -n "add_view\(.*message_id" disbot/ | grep -v views/roles` and
`rg -in "deploy_component|deployed_message"` at the new SHA; test target
`python3 scripts/preflight.py` here.
