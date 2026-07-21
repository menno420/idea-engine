# Vickrey–Clarke–Groves (Clarke-pivot) mechanism, multi-unit single-demand: k identical units auctioned to n unit-demand bidders (valuations v₁≥…≥vₙ) — the efficient allocation gives the units to the k highest-value bidders, and each winner's Clarke-pivot payment = the externality it imposes on others = W₋ᵢ(without i) − W₋ᵢ(with i) equals, for EVERY winner, the SAME uniform price = the (k+1)-th highest valuation (the highest LOSING bid), so truthful reporting is a dominant strategy and expected revenue = k·E[V₍ₖ₊₁₎:ₙ] — on n=5, k=2, v=(10,8,6,4,2) the winners are {10,8}, the uniform price is 6, revenue is 12, and the naive "uniform price = the lowest WINNING bid (k-th highest = 2nd-highest)" foil is rejected on the random-profile sample at |z|≈378.9

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · mechanism design / auction theory / VCG–Clarke pivot
**Proposal:** 250 → Verdict 263 (+13 offset)
**Verifier:** [`verify_250_vcg_clarke_pivot.py`](verify_250_vcg_clarke_pivot.py) · stdlib only (json, hashlib, math, random, fractions) · SEED=20260717
**Digest:** `results_sha256 = 7b0758bc85433ed89f640bbe47aba2a4dd63bf337ab9b3a0a19c6a4497319f2b`

## What this proposal does

Adds a fleet PROPOSAL establishing the **exact externality-payment identity** of the **Vickrey–Clarke–Groves (Clarke-pivot) mechanism** in its **multi-unit single-demand** instance. `k` identical units are auctioned to `n` bidders who each want **at most one** unit, with valuations `v₁ ≥ v₂ ≥ … ≥ vₙ`. Then

1. the **efficient allocation** gives the `k` units to the `k` highest-value bidders (welfare `W = v₁ + … + v_k`);
2. the **Clarke-pivot payment** of each winner `i` equals the **externality** it imposes on the others,

        p_i = W₋ᵢ(efficient allocation WITHOUT agent i) − W₋ᵢ(efficient allocation WITH agent i),

   and this collapses — for **every** winner — to the **same uniform price** equal to the **(k+1)-th highest valuation** (= the highest **losing** bid);
3. **truthful reporting is a dominant strategy** (a winner's payment is independent of its own report as long as it stays a winner);
4. **expected revenue** = `k · E[V₍ₖ₊₁₎:ₙ]` (`k` times the expected `(k+1)`-th highest order statistic).

**Headline instance (n=5, k=2, v=(10,8,6,4,2)):** winners `{10, 8}`, uniform price `= 3rd-highest = 6`, revenue `= k·price = 12`. The pivot for the 10-bidder is `14 − 8 = 6` (others' best without it, `{8,6,4,2}` top-2 `= 14`, minus others' welfare with it, `8`); for the 8-bidder it is `16 − 10 = 6` (others without it `{10,6,4,2}` top-2 `= 16`, minus others' welfare with it, `10`). **Fleet framing:** a coordinator awards `k` identical execution slots to `n` unit-demand agents; the VCG price each winner pays is the marginal welfare loss its win imposes on the rest, which for identical slots + unit demand is one uniform clearing price — the highest bid that did **not** clear. The proposal ships a stdlib-only firsthand verifier that (i) computes the allocation and each winner's pivot payment **exactly** as the externality and matches it to the closed-form `(k+1)`-th order statistic (zero mismatches), (ii) confirms `k·E[V₍ₖ₊₁₎:ₙ]` against a Monte-Carlo profile sample, (iii) shows the payment is **invariant** to a winner's own report (DSIC) and **equivariant** under agent relabelling, and (iv) **falsifies** the plausible-but-wrong "uniform price = lowest **winning** bid" belief.

**Distinctness.** This is the **multi-unit generalization** of single-item Vickrey second-price (sim-lab V212 / the `vickrey-truthful-dominance` card): the pivot price is the **(k+1)**-th (not 2nd) order statistic, and the content is the **externality-payment identity**. At `k = 1` it recovers single-item second-price exactly (price = 2nd-highest). `VCG` / `clarke` / `groves` / `pivot mechanism` is **grep-0** across both repos; orthogonal to single-item Vickrey (V212), revenue-equivalence (P235), and the power-index / airport-Shapley heads (P203/P231).

## Method

Exact rational arithmetic first, Monte-Carlo second.

**Mechanism (exact, over `fractions.Fraction`).** Agents are `(agent_id, value)` pairs. The efficient allocation sorts by `(−value, agent_id)` (deterministic tie-break: lower id wins) and takes the top `k`; `W = welfare_topk(all values, k)` is the sum of the top `k`. For a winner `i`, the Clarke-pivot payment is computed as the **externality directly**:

- `W₋ᵢ(without i) = welfare_topk(values of all agents except i, k)` — the best the others can do when `i` is gone;
- `W₋ᵢ(with i) = W − vᵢ` — the others' welfare in the efficient allocation with `i` present (total welfare minus `i`'s own value);
- `pᵢ = W₋ᵢ(without i) − W₋ᵢ(with i)`.

Because `i` is a winner, removing it lets the `(k+1)`-th-ranked bidder rise into the last slot, so `W₋ᵢ(without i) = W − vᵢ + v₍ₖ₊₁₎` and therefore `pᵢ = v₍ₖ₊₁₎` for **every** winner — one uniform price, the highest losing bid. The verifier does **not** assume this: it computes `pᵢ` from the two welfare terms and independently asserts `pᵢ == v₍ₖ₊₁₎` (the closed-form `(k+1)`-th order statistic). Their exact agreement is the teeth.

**Monte-Carlo (iid profiles).** Draw `N = 200 000` iid profiles of `n = 5` values, each iid Discrete-Uniform`{1..6}`, `k = 2`; revenue per profile `= 2 · (3rd highest)`. The exact target `E[revenue] = k · E[V₍ₖ₊₁₎:ₙ]` is computed by **full enumeration of all 6⁵ = 7776 profiles** with `Fraction` (no order-statistic formula — bulletproof). The whole-sample sum and sum-of-squares are accumulated in **exact integer arithmetic** (revenue is an integer), so the sample mean and variance are exact rationals and only the final `√`/division touch float. iid profiles are **not autocorrelated**, so the plain iid SE is honest — **no** batch-means/thinning (that is only for autocorrelated sample-path estimators like queues / Markov chains); this is stated in the verifier docstring.

## Exact reference

Headline instance `n=5, k=2, v=(10,8,6,4,2)`, all quantities exact over `Fraction`:

| winner value | W₋ᵢ(without i) | W₋ᵢ(with i) | pivot payment = externality | = (k+1)-th highest? |
|---|---|---|---|---|
| **10** | 14 (`{8,6,4,2}` top-2) | 8 | **14 − 8 = 6** | ✓ (3rd = 6) |
| **8**  | 16 (`{10,6,4,2}` top-2) | 10 | **16 − 10 = 6** | ✓ (3rd = 6) |

Uniform price **6**, revenue **k·6 = 12**. Companion instances (all 0 mismatches):

| instance | k | winners | uniform price | revenue | note |
|---|---|---|---|---|---|
| v=(10,8,6,4,2) | 2 | {10,8} | 6 (3rd) | 12 | headline |
| v=(10,8,8,4,2) | 2 | {10, 8@id1} | 8 (3rd) | 16 | **tie** exercises `(−value, id)` tie-break |
| v=(10,8,6,4,2) | 1 | {10} | 8 (2nd) | 8 | **recovers single-item second-price** |
| v=(10,8,6,4,2) | 3 | {10,8,6} | 4 (4th) | 12 | k=3 |

## Four gates (each in its own direction)

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** On the fixed instance plus the tie, `k=1`, and `k=3` companions, compute the efficient allocation and each winner's Clarke-pivot payment **exactly** as the externality `W₋ᵢ(without i) − W₋ᵢ(with i)`, and assert (a) each winner's payment equals that externality exactly, and (b) all winners pay the **same** price `= (k+1)`-th highest valuation. **total_mismatches = 0.** Headline verified: winners `{10,8}`, uniform price `6`, revenue `12`, pivots `14−8=6` and `16−10=6`; `k=1` recovers second-price (price `8`); `k=3` price `4`, revenue `12`. `z` is not applicable and is reported `null` / `"exact"`.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** `N = 200 000` iid profiles (`n=5` iid U`{1..6}`, `k=2`), revenue `= 2·(3rd highest)`. Exact target by full `6⁵`-enumeration: `E[revenue] = k·E[V₍₃₎:₅] = 7` exactly (`E[3rd highest] = 7/2`, by symmetry of U`{1..6}`). Sample mean `700641/100000 ≈ 7.006410`; **z = 1.2193 < 3** [Z_ACCEPT = 3.0]. iid profiles are **not** autocorrelated, so the plain iid SE is honest (no batch means).
- **G3 — invariance (exact, 0 mismatches).** (a) **DSIC / own-report invariance:** vary the winner at index 1 (value 8) over its **whole winning range** — every integer report `b ∈ {7,…,30}` keeps it a winner — and assert the payment is unchanged: the only distinct payment observed is `6` (the highest losing bid), `mismatches = 0`. (b) **Equivariance:** apply the fixed non-trivial relabel `σ = [2,0,3,1,4]`; the winner set `{0,1}` maps to `{0,2}` and the payment vector permutes accordingly, `mismatches = 0`. Both exact via `Fraction`. **total_mismatches = 0.**
- **G4 — falsifiability (reject at large `|z|`, on the SAME G2 sample).** The pre-registered naive foil "the uniform price is the lowest **WINNING** bid" (the `k`-th highest = 2nd-highest for `k=2`), i.e. predicted `E[revenue] = k·E[V₍₂₎:₅] = 5831/648 ≈ 8.998457`. On the same TRUE-revenue sample, `z_foil = (sample_mean_true − exact_mean_foil)/(sample_std/√N) = −378.9138`, **|z_foil| = 378.9138 > 6** [Z_REJECT = 6.0]. The teeth: charge the highest **losing** bid (correct) vs the lowest **winning** bid (wrong) — the classic multi-unit-auction confusion.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = 7b0758bc85433ed89f640bbe47aba2a4dd63bf337ab9b3a0a19c6a4497319f2b`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant). Verifier file sha256 `8319b3192f3dc823939084b02105c37cdcb43bde6cede81e7fffabdab59ebf4e`.

## Grounding

Two pinned Wikipedia revisions (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match on both):

- **"Vickrey–Clarke–Groves auction"**, oldid 1311466659:
  `https://en.wikipedia.org/w/index.php?title=Vickrey–Clarke–Groves_auction&oldid=1311466659@1d816a80feb3bcc457f4cab2b999ddfd15f75681` (14374 bytes), fetched 2026-07-21.
- **"Vickrey auction"**, oldid 1338833083:
  `https://en.wikipedia.org/w/index.php?title=Vickrey_auction&oldid=1338833083@398d2e4148cc7ee83f1343f720f6e243926bb895` (12916 bytes), fetched 2026-07-21.

**Quoted** literally on the pinned revisions (grep count > 0):
- The **externality-payment definition** — VCG page: "it charges each individual **the harm they cause to other bidders**" (grep `harm` = 4), stated as a formula in words, "(sum of bids … *excluding the participant under consideration*) − (what other *winning* bidders have bid …)", and as math `V^{M}_{N∖{bᵢ}} − V^{M∖{tⱼ}}_{N∖{bᵢ}}` = "the **social cost** of their winning … incurred by the rest of the agents". Vickrey page: "each bidder pays the '**opportunity cost**' that their presence introduces … the total bids of all the other bidders that would have won if the first bidder had not bid, minus the total bids of all the other actual winning bidders."
- The **uniform-price / highest-losing-bid** identity and the **unit-demand** condition — Vickrey page: "all winning bidders pay the amount of the **highest non-winning bid** … known as a **uniform price auction**. The uniform-price auction does not, however, result in bidders bidding their true valuations … **unless each bidder has demand for only a single unit**."
- **Dominant-strategy truthfulness** — VCG page: "making truthful reporting a weakly-**dominant strategy**" (grep `dominant strategy` = 1; `truthful` = 6; `incentive compatib` = 2).
- The names **Clarke** (grep 6), **Groves** (grep 6), **Vickrey** (grep 8); the **multi-unit generalization** framing — VCG: "It is a **generalization of a Vickrey auction for multiple items**"; Vickrey: "**multiunit auction**", "**second-price**".

**Derived** firsthand (grep count 0 on both pinned raw wikitexts): the specific instance `n=5, k=2, v=(10,8,6,4,2)` and its adjacency of values (grep 0 for `10,8,6,4,2`); the exact integer pivot values, uniform price 6, revenue 12; the **`(k+1)`-th-order-statistic** characterization of the uniform price and `revenue = k·E[V₍ₖ₊₁₎:ₙ]` (the words "order statistic" and "(k+1)" are grep 0 on both — the pages say "highest non-winning bid" in words); the tie / `k=1` / `k=3` companions; the DSIC own-report invariance sweep and the relabel equivariance leg; the Monte-Carlo profile sample; every z-value; the lowest-winning-bid foil; SEED 20260717; and the results digest.

**Honest posture — disclosed seams.** (1) The **word "pivot" is grep 0 on both revisions**, and the **word "externality" is grep 0 on the VCG page** — the pages carry the *concept* under "harm" / "marginal harm" / "social cost" / "opportunity cost", and the "Clarke pivot" phrase itself is my label for the standard construction, not literally on the page. (2) The VCG page's externality **formula** and its worked "apples" example are stated for the **general combinatorial** setting (items `tⱼ`, item-sets `M`, and a multi-demand example), not the unit-demand uniform-price reduction; the specialization to `k` identical units + unit demand where the general formula **collapses to one uniform `(k+1)`-th-highest price** is quoted-supported *on the Vickrey-auction page* ("highest non-winning bid … truthful … unless each bidder has demand for only a single unit") and worked firsthand here into the exact rational instance + order-statistic revenue law. Nothing oversold as novel: VCG / Clarke-pivot and the uniform-price auction are textbook (Vickrey 1961; Clarke 1971; Groves 1973), cited as such; the exact instance, the two-route pivot=externality check, the DSIC + equivariance legs, the MC agreement, the lowest-winning-bid falsification, and every z-value + the digest are the firsthand contribution.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes the efficient allocation and each winner's Clarke-pivot payment entirely in `fractions.Fraction` as the externality `W₋ᵢ(without i) − W₋ᵢ(with i)`, and independently asserts that value equals the closed-form `(k+1)`-th highest valuation — two genuinely distinct routes (a difference of two `welfare_topk` sums vs a single order statistic) that agree with **total_mismatches = 0** across the headline, a tie instance, `k=1`, and `k=3`. The headline `{10,8}`, price `6`, revenue `12`, pivots `14−8=6` and `16−10=6` are exact integers, not fits.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The exact identity (G1) is fixed before any RNG is touched. The Monte-Carlo gate (G2) only *confirms* the revenue law `k·E[V₍ₖ₊₁₎:ₙ]`, whose target is computed by **exact full enumeration** of all `6⁵` profiles (no sampling), and even the sample mean/variance are accumulated in exact integer arithmetic. Its `z = 1.2193` lands well inside the accept band.

**3. What is the most plausible wrong belief this could be confused with?** That the uniform clearing price is the **lowest winning** bid (the `k`-th highest) rather than the **highest losing** bid (the `(k+1)`-th) — pre-registered as G4 and refuted on the same sample at `|z_foil| = 378.9`. A secondary confusion — that this is "just" single-item Vickrey — is addressed by the `k=1` companion (which *does* recover 2nd-price) alongside `k=2,3` (price = `(k+1)`-th), and by the equivariance / tie-break legs.

**4. Is the verifier deterministic and self-checking?** Yes. A single `random.Random(20260717)` is seeded once and consumed in a fixed order by the MC gate only; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). Rationals serialize via `str(Fraction)` as `"num/den"`, integer counts as ints, every z-value via a fixed `f"{z:.4f}"` string. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 7b0758bc85433ed89f640bbe47aba2a4dd63bf337ab9b3a0a19c6a4497319f2b`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, with the seams disclosed. The externality-payment definition, the dominant-strategy truthfulness, the Clarke/Groves/Vickrey naming, and the multi-unit generalization are QUOTED on the VCG page; the uniform-price = highest-non-winning-bid identity *and* the unit-demand truthfulness condition are QUOTED on the Vickrey page. Disclosed: the word "pivot" is grep 0 on both and "externality" is grep 0 on the VCG page (the concept appears as "harm"/"opportunity cost"/"social cost"); the VCG page's formula is stated for the general combinatorial case, and the unit-demand uniform-price collapse leans on the Vickrey page plus firsthand derivation. The exact instance, the `(k+1)`-order-statistic revenue law, every z-value, and the digest are DERIVED.

**6. Does it scale / is it robust?** The mechanism code is general — `welfare_topk`, `efficient_winners`, and `clarke_payments` take an arbitrary agent list and `k`, with a deterministic `(−value, id)` tie-break. G1 exercises `k ∈ {1,2,3}` and a tie; G3 relabels the agents and re-solves, reproducing `σ(outcome)` exactly (`mismatches = 0`), so the result is a property of the valuation profile, not of a hard-coded index order. The `(k+1)`-th-highest price is read off directly and matches the externality on every winner.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong belief ("price = lowest winning bid = k-th highest") and refutes it on the same evidence at `|z| = 378.9`, while G2 shows the same sample agrees with the true `k·E[V₍ₖ₊₁₎:ₙ]` at `z = 1.22`. Charging the `k`-th instead of the `(k+1)`-th highest, or an off-by-one in the winner set, would break the exact G1 identity or push a G2 z past the band.

**8. Any residual risk before ruling?** The Monte-Carlo leg is an **iid** profile estimator (not an autocorrelated sample path), so the plain iid SE is the honest one and batch means are deliberately *not* used — stated explicitly in the docstring; the exact identity (G1) is what carries the claim and is RNG-free with two independent routes (externality subtraction + closed-form order statistic). The VCG / Clarke-pivot construction and the uniform-price auction are textbook (Vickrey 1961; Clarke 1971; Groves 1973; the two pinned pages) and cited as such; the exact instance, the DSIC + equivariance legs, the MC agreement, the lowest-winning-bid falsification, and every z-value + the digest are the firsthand contribution. The paired sim-lab VERDICT 263 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
