# The bundle over a floorless PWYW — does the committed Ship-It triple ($49 + $19-suggested vs $59, "saves $9") price a discount, or a $10 strategic surcharge decided by one unset owner field?

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 15, PRODUCTS half on the slot's own half-alternation read from the
> actual sequence: P018 books (r1) → P022/P026 trading (r2/r3) → P030 books
> (r4) → P034 trading (r5) → P038 books (r6) → P042 products (r7) → P046 books
> (r8) → P050 products (r9) → P054 books (r10) → P058 products (r11) → P062
> books (r12) → P066 products (r13) → P070 books (r14), so r15 = products due;
> round 15 opened at fleet backlogs with P073 (#437), so the venture slot is
> next per ORDER 004 rule 3.)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/venture-lab@520bdfca71ca4f119808d1098cd4ecf7fc6e6732 · fetched 2026-07-15T10:13:36Z
> (FIRSTHAND pin, public shallow clone read this session — the P058/P062/P066
> precedent; every venture-lab sentence quoted below was read directly at this
> pin. Companion READ-ONLY dedup pin: menno420/sim-lab @
> 23708552a730d61fbe7fce82610ac0afc54484e2, fetched 2026-07-15T10:17:34Z — the
> V040 gap-register sentence quoted below was read there. The sim itself is
> fully hermetic: zero repo/network reads at verdict time, every fixture
> constructed in-sim from the pinned constants in this file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation ("fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains") — round
15 opened at the fleet-backlogs slot (PROPOSAL 073, PR #437), so this slice
serves the VENTURE slot, products half. The harvested object is the committed
catalog's own three-price lattice plus the ONE field it leaves unset:

- **The kit (fixed):** "**$49** (one-time, lifetime updates to the v0.x
  line)." — `candidates/membership-kit/LISTING.md:46`.
- **The pack (PWYW, floor unset):** "**Pay-what-you-want, $19 suggested**
  (one-time, free updates to the v0.x line)." —
  `candidates/template-packs/LISTING.md:61`. The queued ⚑D publish click
  commits the openness itself: "**WHAT:** price set ($19 pay-what-you-want
  suggested (default); **minimum owner's choice**)." —
  `docs/publishing/OWNER-QUEUE.md:162`.
- **The bundle (fixed) + the committed claim:** "**$59** for the bundle —
  versus **$68** bought separately ($49 kit + $19 suggested for the pack).
  The $9 discount is a modest, honest nudge…" —
  `candidates/BUNDLE-LISTING.md:56-58`; FAQ, verbatim: "Yes — each is sold
  separately (kit $49, pack $19 PWYW). The bundle is only for people who
  want both; **it saves $9 and one checkout**." (`BUNDLE-LISTING.md:73-74`).
- **The lane's own coherence guard (verbatim):** "The bundle price is FIXED
  even though the pack alone is PWYW — inheriting PWYW would let the bundle
  undercut the $49 kit alone, which is incoherent pricing." —
  `docs/publishing/vetting/bundle-starter.md` §3.
- **The served anchor ruling this head chains to:** "$59 one-time fixed
  RATIFIED — ORDER 010 / V040 … **$64 is PARKED-WITH-BAR** behind one named
  retention measurement — ≥ 50589/54944 ≈ 0.9207. **Never price at $68**" —
  `bundle-starter.md` §3. And V040's OWN gap register, read at sim-lab
  `2370855`, fixtures `pinned_constants/pwyw_minimum_unpinned`: "the PWYW
  minimum is an owner choice with **NO committed value (gap G2)**".
- **The committed fee schedule:** "flat **10% platform fee + $0.50 per
  transaction** … payment processing (~2.9% + $0.30) … roughly **~12.9% +
  $0.80 per sale**" — `candidates/photo-packs/MARKET-PLAN.md:17-19`, which
  V040 committed as the affine reading net(P) = 0.871·P − 0.80.

Every price in the triple has been priced — V040 ratified the $59 anchor,
V039/V041 priced the PWYW-vs-fixed mode question for their products — but
nobody has priced what the FLOOR does to the lattice the three committed
prices form together. The bundle is still HARD-GATED behind the ⚑B/⚑D
component clicks (`bundle-starter.md` header), and the floor is a field the
owner sets DURING ⚑D — so this is the exact moment the knob is still free,
the same cheap-moment structure P073 found in the unbuilt executor. This
head builds nothing in venture-lab and never edits its files (routing is the
manager's per Q-0260); it prices the floor's effect on the committed lattice
and hands the lane a pre-registered ruling whose repair is literally one
field on one queued click (or one clarifying phrase in committed copy).

## The idea (reasoned to its fuller form — Q-0254 duty)

**The harvested structure, stated back.** A buyer who wants BOTH products
has two purchase paths: the bundle at p = 59, or two separate checkouts at
49 + w, where w is whatever they choose to pay for the PWYW pack, subject
only to w ≥ f — and f, the floor, is the one number in the system with no
committed value. The committed copy evaluates the separate path at the
SUGGESTED w = 19 ("saves $9"). The lattice evaluates it at the ACHIEVABLE
w = f. The falsifiable core: **on exact path arithmetic at the committed
triple (a, s, p) = (49, 19, 59), how far apart are the advertised and the
achievable readings as a function of f — exactly — and is there any floor
value at which the committed copy, the lane's own no-undercut guard, and a
live PWYW knob are simultaneously satisfiable?** Two-sided: if the
committed constants admit a coherent floor region compatible with the copy,
the triple is VINDICATED with the exact region as the finding (the APPROVE
branch is genuinely live — the f grid contains cells where it fires).

**The model (fixed, fully pinned — every constant a decision of this file,
none left to the implementer; all quantities exact rationals).**

- **Prices.** Kit a = 49 (fixed). Pack: PWYW with suggested s = 19 and
  floor f — grid **f ∈ {0, 1, 3, 5, 10, 15, 19}** with decision cell
  **f = 0** (the floorless default: the committed listing and the queued
  click name no minimum; 0 is the reading in which "minimum owner's choice"
  ships untouched). Grid notes: 1 = the mirror knife-edge cell (below), 3 =
  the photo-packs family's ONE committed floor (`OWNER-QUEUE.md:84` "floor
  $3" — the sibling product whose floor IS pinned), 19 = s (the
  PWYW-degenerate world). Bundle p ∈ **{59, 64, 68}** — V040's committed
  anchor family (59 ratified, 64 parked, 68 banned) — decision anchor
  **p = 59**.
- **Buyer paths (a both-buyer).** BUNDLE: one checkout, pay p. SEPARATE:
  two checkouts, pay a + max(w, f) where w is the buyer's intended pack
  payment. STRATEGIC buyer: w = f (pays the floor). Types are exogenous;
  nothing here models demand size (V040's territory) or conversion (its
  G1).
- **Core exact quantities.** Advertised saving σ_adv = (a + s) − p;
  achievable saving σ_ach(f) = (a + f) − p (sign-free); strategic premium
  π(f) = (p − a − f)⁺; buyer-type indifference w\* = p − a (bundle weakly
  cheaper iff w ≥ w\*); coherence window (the lane's own guard, formalized):
  p is lattice-coherent iff **a ≤ p ≤ a + f** (never undercuts the kit
  alone; never charges a strategic premium); floor threshold f\*(p) = p − a.
- **Fee layer (T3 only, seller side).** The committed affine schedule
  net(P) = (871/1000)·P − 4/5 per transaction, exactly V040's committed
  reading of `MARKET-PLAN.md:17-19`; seller path delta Δ(f) = net(p) −
  [net(a) + net(f)] = α(p − a − f)·(−1)… stated precisely: bundle-minus-
  separate seller net = α·(p − a − f) + β with α = 871/1000, β = 4/5.

**Three structure theorems (hand-provable, riding as gates F2).**

1. **BASIS GAP.** σ_adv − σ_ach(f) = s − f EXACTLY, for every a and every
   p (both cancel). The committed copy's number and the lattice's number
   differ by exactly the floor-to-suggested gap: at f = 0 the "$9 saving"
   overstates the achievable by $19 = s exactly — the achievable saving is
   **−$10** (the bundle costs a strategic both-buyer $10 MORE than their
   achievable separate path). Falsifiable: any lattice where the gap
   depends on a or p kills the theorem.
2. **COHERENCE WINDOW.** Coherent iff p ∈ [a, a + f], so f\*(p) = p − a
   with unit slope — every $1 of bundle premium above the kit price must be
   backed by $1 of committed floor. The committed family maps
   **{59, 64, 68} → f\* = {10, 15, 19}**: the ratified $59 needs a floor
   STRICTLY above half the suggested price (10 > 19/2, ratio exactly
   20/19); the parked $64 needs f ≥ 15; and the banned $68 needs
   **f\* = 19 = s exactly** — a margin-0 contact: the banned anchor coheres
   only when the floor equals the suggested price, i.e. only when the PWYW
   knob is dead ink. (An independent lattice re-derivation of V040's
   "never $68", which V040 reached via the $0-discount rationale.) At
   f = 0 the window is the single point {49}: NO bundle price can offer a
   strict achievable discount over a floorless PWYW component — a strict
   achievable discount of $d requires f ≥ (p − a) + d, so the committed
   "$9" needs f = 19 = s, PWYW extinct.
3. **FEE INVARIANT.** Under ANY affine per-transaction schedule
   net(P) = αP − β (α ∈ (0,1), β ≥ 0): bundle-minus-strategic-separate
   seller net = α·(p − a − f) + β, so at the decision cell the seller nets
   exactly **+$9.51** (= 871/100 + 4/5 per both-buyer routed to the bundle)
   while that buyer pays **$10** over their achievable path — for every
   f < 10 the seller's gain and the buyer's loss are simultaneously strict,
   and the "modest, honest nudge" copy sits exactly on that fork. The ONLY
   f-independent genuine saving anywhere in the system is β = $0.80 — the
   saved second fixed fee — and it accrues to the SELLER: "saves $9 and one
   checkout" prices the checkout at $0.80, to the other party. The f = s
   cell reproduces V040's committed nudge cost exactly: Δ(19) = −7039/1000
   = −$7.039 (external anchor).

Plus the **f = 1 MIRROR KNIFE-EDGE** as a named census cell: at a $1 floor
the strategic premium is exactly $9 — the surcharge equals the advertised
saving in magnitude, the copy's own number reflected across the lattice.

**Decision rule (pre-registered, evaluated in this order; decision cell =
(a, s, p, f) = (49, 19, 59, 0); all quantities seedless exact rationals).**

- **REJECT** ("the committed triple is coherent only on the vs-suggested
  reading; on the achievable lattice the floorless default turns the
  advertised $9 discount into a $10 strategic surcharge, and one committed
  field repairs it"): **R1** at the decision cell p ∉ [a, a + f] (the
  lane's own no-undercut guard formalized excludes the committed price) AND
  σ_ach(0) ≤ −(p − a) with σ_adv = 9 exactly reproducing the committed copy
  number (the same triple carries a +$9 advertised and a −$10 achievable
  saving simultaneously); AND **R2** the anchor-family lattice holds:
  f\*({59, 64, 68}) = {10, 15, 19} with f\*(68) = s EXACTLY (margin-0,
  registered) and f\*(59) > s/2 strictly (ratio 20/19); AND **R3** the
  repair thresholds are exact: f = 10 restores weak coherence with
  achievable saving exactly 0, strict achievable saving $d requires
  f ≥ 10 + d, and the committed "$9" on the achievable basis requires
  f = 19 = s — so a live PWYW knob and the committed copy are jointly
  satisfiable ONLY on a stated vs-suggested basis. Checked FIRST because
  the costly direction ships silently: the ⚑D click is queued for one
  sitting, "minimum owner's choice" defaults to floorless in every
  storefront flow, and the bundle listing's committed sentence becomes
  checkable-false against the lattice the moment both listings are live —
  in front of buyers, where "manufactured discount" is precisely the
  accusation the copy's own anti-fake-anchor stance disclaims.
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate
  failing (below).
- **APPROVE** ("the committed triple coheres as shipped"): at the decision
  cell p ∈ [a, a + f] AND σ_ach ≥ 0 — mutually exclusive with R1 by
  arithmetic; fires on the f grid at every cell f ≥ 10, so the branch is
  live: if the drafter misread and the packet DOES commit a floor ≥ 10
  (or the ⚑D click ships one), the pinned constant moves and APPROVE
  fires as re-run-with-the-measured-f.
- **NULL** (anything else — pre-registered axes, each a finalized citable
  finding): basis-reading fork (if the committed "saves $9" is read as
  vs-suggested-prices it is TRUE as stated — the finding is then the exact
  basis-gap table s − f with the repair being one clarifying phrase, and
  the ruling names the reading rather than forcing one); floor-granularity
  convention (a storefront minimum-price quantum — e.g. integer dollars or
  a platform minimum — shifts f\* by less than one quantum: pre-checked
  non-flipping on the committed integer thresholds, disclosed); a theorem
  failure without gate failure (the drafter's lattice algebra is wrong —
  the corrected law is the finding); twin-arm disagreement surviving the
  INVALID diagnosis.

**Arms.** **Arm A** (DECISION arm, seedless): exact-Fraction closed forms
over the full grid (7 floors × 3 anchors + perturbed-a/p control worlds for
T1's independence claim + degeneracy rows), byte-identical across process
runs. **Arm B** (twin, seedless, INDEPENDENTLY-WRITTEN): literal
integer-cent enumeration — path costs by direct min() over enumerated w,
w\* by upward scan, window membership by scanning candidate bundle prices,
the basis gap by direct subtraction — must reproduce every Arm-A number
EXACTLY. **Arm R** (seeded, REPORTING-ONLY): buyer-type draws at the
decision cell under two pinned pmfs — FLOOR-HEAVY {w=0: 3/5, w=10: 1/5,
w=19: 1/5} and SUGGESTED-ANCHORED {w=19: 3/5, w=10: 1/5, w=0: 1/5} —
50,000 episodes on random.Random(20261660) and 20,000 on
random.Random(20261661) (one uniform per episode, counts counted and
asserted), presentation shuffle 20261662, aux 20261663 NEVER read.
Reported beside the exact expectations (bundle-take 2/5 and 4/5; exact
mean outlays 53 and 57); no statistical gate rides Arm R.

**Gates (INVALID if any fails).**

- **F1 model identities + external anchors:** σ_adv = 9 reproduces the
  committed copy number exactly; the committed fee reading reproduces
  V040's committed net table EXACTLY — net(49) = 41879/1000, net(59) =
  50589/1000, net(64) = 54944/1000, net(68) = 58428/1000, the
  "+$0.80" both-separate-at-suggested row net(68) − [net(49) + net(19)] =
  4/5, and the retention bar net(59)/net(64) = 50589/54944 verbatim —
  five independent contacts between this head's arithmetic and a FINALIZED
  sibling verdict's committed numerals; w\* = f\* identity (buyer
  indifference and coherence threshold coincide at p − a).
- **F2 the three structure theorems** (statements above, checked on exact
  arithmetic across the FULL grid including perturbed-a and perturbed-p
  control worlds for T1's independence, not just the decision cell).
- **F3 census anchors:** the full f-grid table at p = 59 verbatim —
  (f: coherent, σ_ach, π, gap, Δ) = (0: no, −10, 10, 19, 951/100),
  (1: no, −9, 9, 18, 8639/1000), (3: no, −7, 7, 16, 6897/1000),
  (5: no, −5, 5, 14, 1031/200), (10: yes, 0, 0, 9, 4/5),
  (15: yes, 5, 0, 4, −711/200), (19: yes, 9, 0, 0, −7039/1000);
  the f\* table {59→10, 64→15, 68→19}; the mirror cell π(1) = 9 = σ_adv;
  Δ(0) = 951/100; the strict-discount law f(d) = 10 + d at d ∈ {1, 9}.
- **F4 hand world:** (a, s, p) = (3, 2, 4), f = 0: w\* = 1, f\* = 1,
  gap = 2 = s, window = {3} (empty of discounts), π = 1 — all by pencil;
  Arm B's cent-scan must land w\* = 100 cents.
- **F5 degeneracies:** f = s → PWYW degenerate-fixed, gap 0, triple
  coherent, σ_ach = σ_adv = 9 (the world the committed copy implicitly
  assumes); p = a → pack-free-with-kit, coherent at EVERY f with π = 0
  (the lane's own guard sentence as arithmetic — the only coherent price
  at f = 0); p = a + s = 68 → f\* = s (the banned-anchor contact).
- **F6 battery:** Arm B exact-equal on every number; twin
  independently-written decision evaluators agree on the token; Arm-R
  draw-count sentinels counted and asserted; aux seed 20261663 never read
  (constructor registry); stdout + results.json byte-identical across two
  process runs; CPython minor pinned.

**GATE POWER, computed at registration for a correct implementation (the
V065/V067 lesson, applied):** the sim is FULLY DETERMINISTIC — every
decision clause and every F-gate is an exact-rational identity, structural
assertion, or byte comparison; the only seeded arm is reporting-only with
NO statistical gate (its sole gates are the draw-count sentinel and exact
reproducibility, pass probability 1 for a correct implementation). JOINT
pass probability across all gates for a correct implementation = 1 EXACTLY
(the P059–P073 no-stochastic-gate precedent). Decision separation is
noise-free exact arithmetic; the registered knife-edges are disclosed as
such — f\*(68) = s is a TRUE margin-0 contact (the thesis, not an
accident), f\*(59)/(s/2) = 20/19 and π(0)/σ_adv = 10/9 are the two thin
strict clauses, both exact, and the f = 1 mirror cell is a registered
equality (π = σ_adv = 9).

**Expected landing DISCLOSED per the P048–P073 closed-form-arm norm
(drafting script `draft_p074.py` ran this session, ALL PASS exit 0; the sim
re-derives from scratch and must not trust these):** REJECT on all three
conjuncts — R1: at f = 0 the window is {49} ∌ 59, σ_adv = +9 and σ_ach =
−10 simultaneously; R2: f\* = {10, 15, 19} with the 68→19 = s margin-0
contact and 10 > 9.5 at ratio 20/19; R3: f = 10 → σ_ach = 0 exactly,
f(d = 9) = 19 = s. Falsifiability real on every clause — **every f ≥ 10
grid cell lands the APPROVE clauses** (the committed triple is one owner
field away from coherent, which is exactly the repair); the basis-reading
NULL axis is genuinely live (on the vs-suggested reading the copy is TRUE
and the verdict ships the gap table, not a scolding); and the T1
independence claim dies on any world where the gap moves with a or p
(checked on perturbed controls). Reporting sharpenings run live: the
seller/buyer fork at f = 0 is +$9.51 vs −$10 per both-buyer (the committed
schedule's α, β applied once each); the only f-invariant saving is the
seller's $0.80 second-fee; and the f = 3 cell — the floor value the
SIBLING product actually committed — still leaves the triple incoherent
with a $7 premium: the family's one pinned floor would not save this
lattice, so the repair genuinely needs a NEW committed value, not a copied
one.

**Consequence, pre-registered** (routing the manager's per Q-0260 — this
repo never edits venture-lab files, nothing here builds, publishes, or
spends; APPLICATION GUARD, two conditions: (1) the verdict conditions on
the committed triple and copy @ 520bdfc — a re-priced component, an amended
FAQ sentence, or a committed floor value means re-run at the new constants,
not reuse; (2) it conditions on the floor being genuinely open at ⚑D-click
time — if the owner has already set a minimum on the live storefront, that
measured f decides by table lookup, no re-run):

- **REJECT** → paste-ready structured choice, recommendation first per
  Q-0263.2 — **(a, recommended: one field + one phrase, zero new
  artifacts)** set the pack's Gumroad minimum to **$10** in the queued ⚑D
  price row (`OWNER-QUEUE.md:162` — the row already says "minimum owner's
  choice"; this makes the choice) AND add the two words "at suggested
  prices" to the bundle FAQ's "$9" sentence — the floor makes the lattice
  weakly coherent (σ_ach = 0, no strategic premium, kit never undercut)
  and the phrase makes the committed claim exactly true on its stated
  basis; **(b)** floor at $19 = suggested (PWYW becomes de-facto fixed —
  the copy becomes true on BOTH bases, at the cost of the PWYW knob's
  entire point; V041's mode analysis then applies unchanged); **(c)**
  keep the floorless PWYW and re-cut the bundle to $49 ("pack free with
  bundle") — the one coherent price at f = 0, a real repricing decision
  that V040's frontier machinery already prices. An owner/lane intent
  call, never ruled by fiat here.
- **APPROVE** → the committed triple gains a measured coherence basis and
  the f-table ships as the ⚑D click's reading aid.
- **NULL** → the named axis ships with the exact tables plus the free
  probe (the lattice functions re-run on any measured floor at zero
  marginal cost).

**Boundaries (stated in the verdict):** the strategic-buyer boundary (the
lattice prices PATHS, not psychology — real PWYW buyers overpay floors
routinely, which is exactly why the ruling's REJECT clause is about the
committed COPY's checkable truth and the coherence guard, never a claim
that every buyer arbitrages; the Arm-R pmfs bracket both worlds and are
reporting-only); the demand boundary (no conversion, no market size — V040
G1 territory, untouched: this head prices the lattice per both-buyer,
V040 priced the anchor per retention frontier); the platform boundary
(Gumroad minimum-price quanta and any "$0.99 minimum for paid products"
rule are named follow-ups; the thresholds are integers so a sub-dollar
quantum cannot flip them, pre-checked); the copy-reading boundary (the
vs-suggested reading is a genuinely available honest reading — it is the
NULL axis, not a defeated strawman). Honest-null explicit: every NULL axis
is a finalized, citable finding with its exact numbers, never a re-run
request.

## Relations (adjacent heads — deliberately links, not duplication)

- Nearest by WORLD: **V040 (Ship-It bundle anchor)** — the SAME committed
  triple, the orthogonal knob, and this head's provenance: V040 priced the
  ANCHOR p ∈ {59, 64, 68} per committed both-buyer at the SUGGESTED $19,
  and its own gap register names this head's knob verbatim — G2, "the PWYW
  minimum is an owner choice with NO committed value", disclosed-with-
  direction and priced nowhere. This head holds the anchor FIXED at V040's
  ratified $59 and prices the FLOOR — serving a finalized verdict's own
  registered gap with a different decision object, exactly the P066→V061
  precedent shape. Five of V040's committed numerals ride as external
  anchor gates (F1), and T2 re-derives its "$68 ban" by an independent
  route — deliberate cross-verification, not duplication.
- **V039 (photo-packs)** — the family's other bundle math: a SAME-product
  two-pack priced by SELLER-net dominance (net(b) ≥ 2·net(5)) with a
  COMMITTED floor ($3 — `OWNER-QUEUE.md:84`); no cross-product lattice, no
  open floor knob. Its committed $3 appears here as a grid cell — and the
  drafting run shows $3 would NOT save this lattice ($7 premium remains),
  which is why the repair needs a new committed value. **V041 (cookbook
  $19-vs-PWYW)** — single-product PWYW MODE choice with min-0 taker
  mechanics and the $3.20 fee-floor crossing; no second product, no bundle,
  no path arithmetic. **V037 (serial pricing)** — different product family
  entirely.
- Products-half priors: **P042 → V053** (channel token allocation — no
  price lattice), **P050 → V061** (kill-clock dial), **P058 → V069**
  (rubric weight jitter — the instrument-audit kin by move; different
  instrument, zero shared fixtures), **P066 → V079** (kill-clock anchor /
  exposure truncation — the served-gap PRECEDENT this head reuses as a
  move, on a different verdict's different gap).
- Method kin disclosed: **P073** (rate-tier degeneracy) is the nearest
  BY MOVE — both audit committed constant-pairs sitting exactly on a
  degeneracy surface with margin-0 contacts registered as the thesis. The
  mechanics share nothing: windowed admission maxima over disciplines
  there; buyer-path dominance and coherence windows over a price lattice
  here. Also the P059–P073 fully-deterministic no-stochastic-gate shape
  (exact decision arm + independently-written twin + reporting-only seeded
  traces) is the inherited battery; the coherence-window formalization of
  the lane's own prose guard, the basis-gap invariance theorem, and the
  external-anchor gate row (a finalized sibling verdict's committed
  numerals as F1 contacts) are this head's own additions.
- No proposal P001–P073 and no verdict V001–V086 (ledger swept READ-ONLY at
  sim-lab `2370855` this session: V085/V086 newest in flight per the
  coordinator relay) prices a cross-product dominance lattice, a PWYW
  floor, purchase-path arbitrage, or advertised-vs-achievable claim
  arithmetic — the pipeline's first price-lattice head.

## Model basis (declared model-dependence — the P024 discipline)

The decision layer is model-FREE window/path arithmetic on committed
constants: T1/T2 and every REJECT clause are exact statements about the
prices themselves (what a buyer CAN pay, what the copy claims, what the
lane's own guard demands) — no demand model, no behavior model. The only
model content is (i) the affine fee reading of the committed schedule
(V040's own committed reading, reproduced to five external anchors — and T3
is proved for ALL affine α, β, so fee imprecision moves nothing), and (ii)
the Arm-R buyer-type pmfs, which are invented-but-pinned, REPORTING-ONLY,
and bracket the floor-heavy and suggested-anchored worlds. The named live
measurement is free: the storefront's own analytics will eventually hand
the owner a real PWYW payment distribution, at which point the committed
lattice functions re-run on measured w at zero marginal cost.

## Probe report (v0, 2026-07-15)

**1. What is this really?** A pre-registered audit of the committed
catalog's three-price lattice at its one uncommitted degree of freedom: the
PWYW floor. The committed bundle copy claims a $9 saving measured against a
price nobody is required to pay; the lattice measures against the price
everybody is ALLOWED to pay, and the two readings differ by exactly s − f —
$19 at the floorless default — flipping the advertised discount into a $10
strategic surcharge, with the repair already sitting inside the lane's own
queued click.

**2. What is the possibility space?** (i) Don't run it — the ⚑D click
ships (one sitting, batched), the storefront default is floorless, and the
live catalog then contains a checkable-false committed sentence next to an
anti-fake-anchor stance; the failure is silent because every individual
price was separately ratified. (ii) Wait for live PWYW data — the right
distribution eventually, but the floor is set AT the click, before any
data exists; the lattice question is decidable now on committed constants
alone. (iii) A prose answer ("obviously set a minimum") — measures
nothing: not the threshold (10, not obvious), not the anchor-family map
({10, 15, 19} with the banned anchor's margin-0 contact), not the fact
that the sibling's committed $3 floor would NOT suffice. (iv) This head:
hermetic, exact-arithmetic, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file + one fixture JSON yields: the full
exact lattice surface (coherence, achievable saving, premium, basis gap,
seller delta per floor × anchor), three hand-provable theorems as gates,
five external-anchor contacts against a finalized sibling verdict, and a
transferable pattern — ADVERTISED-VS-ACHIEVABLE CLAIM ARITHMETIC — that
audits every fleet surface where a committed claim is evaluated at a
reference value while the system leaves the reference free (suggested
prices, default configs cited as guarantees, "up to" claims over
uncommitted parameters).

**4. What breaks it? (assumptions made explicit)** (a) The strategic-buyer
reading — real buyers may never arbitrage; disclosed as the boundary, and
the REJECT clause deliberately rides the COPY's checkable truth and the
lane's OWN coherence guard, not a behavioral prediction. (b) The
basis-reading fork — "saves $9" vs suggested is an honest reading; it is
a pre-registered NULL axis that ships the gap table instead of a ruling.
(c) Platform floor quanta — could shift thresholds by sub-dollar amounts;
integer thresholds pre-checked non-flipping, named follow-up. (d) The fee
reading — T3 is proved for all affine schedules, so only a NON-affine real
schedule (e.g. percentage caps) could move the seller-side numbers;
decision clauses never ride the fee layer. None is hidden; each is a
boundary, a NULL axis, or a named follow-up.

**5. What does it unlock?** The ⚑D click gains its missing number: the
floor field goes from "owner's choice" (unpriced) to a chosen value with
an exact consequence table. The bundle listing's committed sentence
becomes exactly true on a stated basis before it is ever public. V040's
gap register G2 closes with a citation. And the fleet gains the
advertised-vs-achievable audit pattern — the products half's fifth head
(P042 where to build, P050 when to stop, P058 whether the scorer is
robust, P066 when the stopwatch starts — this one: whether the price the
copy cites is a price anyone must pay).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at verdict time (fully hermetic; every fixture in this file). The
cheapest kill at drafting was reading the queued click row firsthand — if
`OWNER-QUEUE.md:162` had committed a minimum ≥ $10, this head dies in one
sentence; it commits "minimum owner's choice" instead, and V040's G2
independently records the absence. The cheapest confirm after the verdict:
the owner sets the floor at ⚑D time and the committed table gives the
lattice state by lookup.

**7. Which lane should build it — and what does it displace or interact
with?** sim-lab builds the verdict (the standing pipeline); venture-lab is
the CONSUMER via the manager's routing (Q-0260). It displaces nothing —
V040's anchor ruling stands (this head USES it: the anchor is held at the
ratified $59, and the parked/banned anchors get their floor requirements
priced as a bonus row); V039/V041's mode rulings stand; P062's owner-queue
machinery composes (the repair is one field inside an already-sequenced
click).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib sim file (Arm A exact lattice closed forms + Arm B
independently-written integer-cent enumeration + Arm R reporting traces),
one fixtures.json (every constant in this file copied verbatim),
results.json + stdout byte-stable across two runs, the pre-registered rule
applied in the registered order. Feasibility: the full grid is 7 floors ×
3 anchors plus control worlds and two 50k/20k reporting traces — seconds,
pure CPython, no dependencies.

**Recommendation: sim-ready** — every constant pinned here, the decision
rule registered REJECT-first before any code, every registered numeral
PRODUCED by the drafting script this session (`draft_p074.py`, ALL PASS,
exit 0 — the V080 live-verify rule and the V084 NO-DERIVED-LITERALS lesson
honored by construction), zero stochastic gates (joint pass probability 1
exactly for a correct implementation — the P059–P073 precedent), seeds
20261660–663 strictly above the verified in-tree high-water 20261653
(P073/V086's registered set) with the gap 20261654–659 disclosed as the
in-flight buffer, fully hermetic at verdict time; the honest next step is
the sim itself.
