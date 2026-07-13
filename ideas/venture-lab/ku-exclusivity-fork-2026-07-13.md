# KU exclusivity fork — the publishing plan's "KDP Select: Yes" default vs its own royalty/page-read arithmetic

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 6, BOOKS half on the slot's own half-alternation; rounds 1–5 were P018
> books → V020 null, P022 trading → V024 null, P026 trading → V028 approve, P030
> books → V032 reject, P034 trading → V036 reject) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane
> build; enrollment stays an explicit OWNER action on every outcome, the lane's
> hard rail inherited verbatim)
> **Grounding:** https://github.com/menno420/idea-engine@2b43de296e15c64b3b04f6380d88f97c5f2936e6 · fetched 2026-07-13T15:50:00Z
> (this repo's own tree at backfill HEAD — the pin under which the P038 outbox
> block was re-read verbatim; the target document itself is pinned inside that
> block at venture-lab `79a1987`)

**Origin + provenance (backfill, disclosed):** PROPOSAL 038 was drafted as a
control-only fast-lane slice (PR #317, merged at main HEAD `2b43de2`) whose
block disclosed "no local idea file is committed — the P037 precedent, a
disclosed deviation from the P017–P036 idea-file convention". That deviation
left `scripts/check_ideas.py --outbox` RED at main (LINK: "PROPOSAL 038:
`idea:` carries no menno420/idea-engine ideas/ link") — a latent gate any next
non-control PR would inherit. This file backfills the convention: the **full
probe/summary/question/done-when text rides the P038 block in
`control/outbox.md` verbatim and stays the source of truth**; this doc
condenses it so the outbox↔ideas link contract holds. A correction `idea:`
line inside the P038 block links here.

## The idea (condensed from the P038 block)

The venture-lab publishing plan's §4 OWNER-ACTION row **"KDP Select: Yes"**
(docs/publishing/PUBLISHING-PLAN.md @ `79a1987`) is a convention-based default
recommended for the Tier-1 adult novellas on an uncited directional claim
(novellas "earn best in KU via page-reads") — never measured, and load-bearing
asymmetrically: Select is 90-day EXCLUSIVITY, so a wrong "Yes" forecloses wide
distribution while a wrong "No" merely forgoes page-read income, one owner
click from execution. The head prices the default against the plan's OWN
verified constants (the 70%-royalty band $2.99–$9.99 with per-MB delivery fee,
else 35%; measured word counts 27,865 / 36,434) via a per-reader-contact
buy-vs-borrow mixture: ARM KU(p) vs ARM WIDE(p) at the SAME price per cell —
the exclusivity fork isolated from the pricing fork — over 288 decision cells
(2 titles × borrow-to-sale b ∈ {1/2, 1, 2, 4} × read-through rt ∈ {7/20, 3/5,
17/20} × KENP rate ∈ {$0.0035, $0.0045, $0.0055} × price ∈ {$0.99, $2.99,
$4.99, $6.99}), in BOTH an exact closed-form Fraction arm (all 288 cells, zero
sampling error) and a seeded MC replication arm (seeds 20261289–92, new
registry high-water 20261292). Pre-registered, REJECT checked FIRST (KU-win
share W < 2/5 → strike the blanket "Yes" from the recommendation posture;
drafting arithmetic disclosed in the block: W = 101/288 ≈ 0.351 overall,
4/72 at the plan's own $4.99 tier — REJECT is the expected landing), APPROVE
(W ≥ 4/5 overall AND ≥ 4/5 at the $4.99 tier → ratify the default with its
evidence row), else NULL (conditional enroll-rule via the per-axis win shares
and the b* crossover map + the named 90-day one-title KDP dashboard live
probe).

## Probe report (v0, 2026-07-13 — backfill condensation)

> The probe rode the P038 outbox block itself (the fast-lane deviation, stated
> there); this section condenses it into the battery form so the idea grammar
> holds. Every claim below is sourced from the block @ `2b43de2`.

**1. What is this really?** A pre-registered measurement of an unmeasured,
asymmetric, one-click-from-execution default: does KU enrollment (90-day
exclusivity) actually beat going wide under the plan's own verified royalty
constants and a swept borrow/read-through/rate/price grid — per reader-contact,
royalty mechanics only, discoverability out of scope by construction.

**2. What is the possibility space?** Execute the "Yes" unmeasured (the status
quo — the costly error the REJECT-first ordering protects against); flip to a
blanket "No" equally unmeasured; wait 90 days for live data on an enrolled
title (the NULL branch's probe — but the model brackets the space before any
lock-in click); or this head: isolate the enrollment fork from the pricing
fork and price it exactly, with the conditional rule as the citable landing.

**3. Most advanced capability from the simplest implementation?** One stdlib
sim + fixture JSON: 288 closed-form cells (exact Fractions from the plan's own
royalty-band identities) cross-gated against a seeded MC arm — a per-title
crossover table (the smallest b at which KU wins, per rt/rate/price) that
turns an ideological fork into a lookup.

**4. What breaks it?** γ (borrowers who buy anyway when wide) and κ (buyer
cannibalization under KU) are invented, pinned, the disclosed weakest joints —
zero titles published, no fleet datapoint on borrow-vs-buy behavior; the
sweeps bracket scale, not shape. Reader-contacts are held EQUAL across arms
(KU visibility boost and wide multi-store reach BOTH out of scope). The KENP
rate is Amazon-set and monthly-varying (the grid brackets the cited range).
Single-title single-term statics. All stated in the block's done-when
boundaries.

**5. What does it unlock?** The enrollment row that sits UPSTREAM of every
already-landed pricing verdict (V037/V039/V040/V041 priced points under an
assumed enrollment state); on REJECT, per-title enrollment gated on the
crossover table before any exclusivity click; on NULL, the named zero-tooling
live probe (90 days of KDP dashboard orders vs KENP page-reads on ONE enrolled
title → the real b and per-borrow income).

**6. What does it depend on?** Nothing at verdict time — fully hermetic, every
fixture a pinned constant committed with the sim, the plan's §4/§6 rows quoted
verbatim @ venture-lab `79a1987`. Consumers: venture-lab owns the plan
(routing is the manager's per Q-0260 — this repo never edits venture-lab
files); enrollment/publishing stays an explicit OWNER action on every outcome.

**7. Which lane should build it?** sim-lab (method provider — the hermetic
dual-arm pre-registered discipline is the PROPOSAL 017–037 committed
precedent); the verdict consumer is venture-lab via the manager sweep +
OWNER-QUEUE. Dedup ran at drafting (block @ `2b43de2`): no proposal P001–P037
and no verdict V001–V047 touches KU exclusivity, KDP-Select enrollment,
royalty-band structure as a decision variable, or page-read economics; nearest
neighbors (the V037/V039/V040/V041 pricing verdicts by lane, P018/V020 +
P030/V032 by slot) are disjoint on decision variable and model, argued
line-by-line in the block.

**8. What is the smallest shippable slice?** The committed stdlib sim + fixture
JSON reproducing the full {KU, WIDE, Δ, Δrel, MC SE, win flag} × 288-cell table
byte-identically per the block's done-when — already fully specified there;
this file adds no scope.

**Recommendation: sim-ready** — the proposal is already on the sim-lab pull
surface as PROPOSAL 038 (outbox @ `2b43de2`, drafted via PR #317); this
backfill restores the idea-file convention behind it so the outbox↔ideas LINK
gate holds. State advances to `historical(…)` on the verdict's arrival per the
forward-only rule.
