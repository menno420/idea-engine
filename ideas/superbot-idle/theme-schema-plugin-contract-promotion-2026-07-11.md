# Theme-manifest schema promotion — carry v1's 12-pack evidence into the plugin-contract family when it is born

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-idle`
> **Grounding:** https://github.com/menno420/superbot-idle@f11c71a52d4d2adf88b2bf11f5d1134bad495be2 · fetched 2026-07-11T03:31Z (manifest row: behind)
> *(pin annotation: roster row @ fleet-manager `93d3a4d` records lane HEAD `97bfff2`; live HEAD `f11c71a` is 3 PRs ahead. The upstream absence is the LANE's own raw-probe evidence at the same pin, not this capture's assumption.)*
> **Sequence:** after superbot-next#ORDER-002 yields a published plugin/manifest contract — the promotion's arming event. At capture time the contract does NOT exist upstream: superbot-next publishes no plugin/manifest doc (`plugins.md` and `plugin-contract.md` both 404) and `superbot-plugin-hello` is an empty repo (lane PLUG-001 raw-probe evidence, `control/status.md` @ `f11c71a`).

## Problem

The directive decided (§4, re-affirmed §7 item 3, Q-0240 decide-and-flag): the
theme-manifest schema is **plugin-contract material** — drafted in the idle repo so the
games program never serializes behind the Builder, then **promoted into the contract
family later**. The draft half is done and over-delivered at lane HEAD: schema v1
frozen with a machine twin held field-for-field identical by tests, proven on 12
foreign packs across three catalog waves with ZERO schema pinches, and a gate whose
product property is "gate-green = safe to enable on a live server unreviewed"
(`docs/theme-schema.md` + `schema/theme.schema.json` + `tools/theme_gate.py` @
`f11c71a`). The promotion half has **no tracker anywhere**: the lane's QUEUE holds the
*adapter* on PLUG-001, not the schema promotion; the decided-and-flagged item lives
only as prose in a superbot planning doc. When the plugin contract is finally born,
nothing arms the promotion — the classic decided-and-flagged item that evaporates
between repos.

## Idea

This capture is that tracker, made greppable by the Sequence token above (one grep of
this tree surfaces every idea blocked on the same foreign order — README § Idea file
grammar). The promotion slice, when armed: schema v1 + theme-gate semantics + the
setup-code/provisioning contract move into the plugin-contract family **as one family**
— §4's "three versioned schemas, one discipline" (data API read · provisioning write ·
theme skin) — carrying the evidence trail (parity tests, 12 zero-pinch packs, exact
budget arithmetic, 150 cross-language vectors) as the draft's credentials. Promotion
should be adopt-with-evidence, not re-design: the contract family's theme chapter
already has a proven reference implementation, and re-drafting it upstream from scratch
would discard the only empirically-tested piece of the family.

## Grounding

- The decided split + promotion flag: superbot @ `41899e1` §4 ("the idle seat drafts v1
  in its own repo and flags it for promotion into the contract") and §7 item 3.
- Draft-half completeness: lane `docs/theme-schema.md`, `docs/current-state.md`
  § Stability baseline (schema v1, gate, 12 packs, parity tests) @ `f11c71a`.
- Upstream absence + the adapter-only hold: lane `control/status.md` § PLUG-001 and
  § QUEUE @ `f11c71a` (adapter evidence-blocked; schema promotion unmentioned).

**Why now:** both arming facts are fresh-verified this session (draft complete,
contract absent) and the capture costs one page; un-captured, the promotion duty gets
re-derived — or missed — whenever superbot-next's contract lands, by whoever happens
to notice.
