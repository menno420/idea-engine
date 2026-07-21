# In Green Hackenbush every rooted forest's Sprague–Grundy value is given exactly by the colon principle, so a bamboo forest of stalk-lengths (a₁,…,aₖ) has value a₁⊕…⊕aₖ and is a first-player win iff that nim-sum is nonzero — Green Hackenbush is Nim (anchor: (3,5,7) has value 3⊕5⊕7 = 1, a first-player win; the branching Y-tree {0-1,1-2,1-3} also has value 1).

> **State:** sim-ready
> **Status:** sim-ready
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Hackenbush&oldid=1360289482@1a8d4f063a7890b389c959e4b675791d2bc15754 · fetched 2026-07-21

**Lane:** superbot-games · combinatorial game / Sprague–Grundy
**Proposal:** 247 → Verdict 260 (+13 offset)
**Verifier:** [`verify_247_green_hackenbush_nim.py`](verify_247_green_hackenbush_nim.py) · stdlib only (json, hashlib, math, random, fractions, itertools) · SEED=20260717
**File sha256:** `da7f11191025addd748d29a49d22eb9173bd05ab8775bf8458a62e65b31b639b`
**Digest:** `results_sha256 = f1967eac6a0158fb4b1546facd309355577f251033067167296f6b921903c0b9`

## What this proposal does

Adds a superbot-games PROPOSAL establishing that **Green Hackenbush is Nim**: in the impartial (all-edges-green) game every rooted forest's Sprague–Grundy value is given **exactly** by the **colon principle**, so a bamboo forest of stalk-lengths `(a₁,…,aₖ)` has value `a₁⊕…⊕aₖ` and is a first-player win iff that nim-sum is nonzero. The proposal ships a stdlib-only firsthand verifier that proves the claim by pitting an **independent ground-truth mex-DP game engine** (which knows nothing of the closed form) against the **colon-principle closed form**, through **four gates each in its own direction** — an exact identity sweep, a Monte-Carlo P-density agreement, an invariance/robustness leg, and a falsifiability leg that rejects plausible naive foils — all wrapped in a reproducible SEED=20260717 digest. Fills a confirmed gap: green-hackenbush / colon-principle is grep-0 across both repos and orthogonal to the named prior game heads — Sprague–Grundy nim-sum (P219), Fibonacci nim / Zeckendorf (P243), Wythoff (P239), Banzhaf voting power (P203) — this is the colon-principle reduction of Green Hackenbush to Nim, not a take-away/pursuit/power object.

## Method

Ground-truth engine first, closed form second, then the two are forced to agree. (1) The **game engine** `grundy(edges)` computes the Sprague–Grundy value by memoized **mex-DP** over `frozenset` positions: each move removes one edge, after which `ground_component` prunes every edge no longer connected to the ground (disconnected edges fall), and the value of a position is the **mex** of the values of its successors under normal play — the engine assumes no theorem, it plays the game. (2) The **closed form** `colon_value` evaluates the colon-principle recursion `sub(v, parent) = XOR over children c of (1 + sub(c, v))`, with the whole forest's value taken as the XOR over the ground's neighbours `r` of `(1 + sub(r, 0))`. (3) Determinism: SEED=20260717 (hardcoded), all floats rounded to 10 decimals before hashing, and the digest is the sha256 of the canonical-JSON results dict; determinism is verified **three ways** — an in-process double-run via `--selfcheck`, a separate re-invocation, both byte-identical.

## Exact reference

The colon-principle closed form and the independent mex-DP engine agree on every anchor position:

| position | colon value | grundy (mex-DP) |
|---|---|---|
| bamboo (3,5,7) | 3⊕5⊕7 = 1 | 1 |
| Y-tree {0-1, 1-2, 1-3} | 1 | 1 |
| explicit tree {0-1,1-2,2-3,1-4,4-5,2-6} | 4 | 4 |

## Four gates (each in its own direction)

- **G1 — EXACT identity (integer/XOR arithmetic).** `colon_value == grundy` over an exhaustive enumeration of all rooted trees `≤ 7` edges plus a random battery of larger trees/forests. Result: **800 positions checked, 0 mismatches, max 34 edges**. PASS.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** The exact P-position density over the bamboo model (`k = 3` stalks, each length uniform in `{1..8}`, 512 forests) is **`p0 = 21/256 = 42/512 ≈ 0.08203`**, computed by solving all 512 with the game engine; `N = 200000` i.i.d. samples classified by the game engine give `p̂ = 0.08248` (16496 hits), **`z = 0.731`**. PASS.
- **G3 — invariance / robustness (two sub-checks).** (a) relabel/child-order invariance over 200 random trees — both engines unchanged, **0 discrepancies**; (b) optimal-play robustness — an optimal player (move to a value-0 successor) never loses across **360 games** vs a random opponent, **0 losses**. PASS.
- **G4 — falsifiability (reject plausible naive foils).** On the same model the sample's true P-density is rejected against Foil A "sum-parity" (P iff `a₁+a₂+a₃` even, `q = 1/2`) at **`z = −373.4`** and Foil B "sum-mod-3" (P iff sum `≡ 0 mod 3`, `q = 85/256`) at **`z = −237.0`**, while agreeing with the correct XOR rule at `z = 0.731`. PASS.

## Grounding

Pinned Wikipedia **"Hackenbush"** oldid **1360289482** @ raw-wikitext sha1 **1a8d4f063a7890b389c959e4b675791d2bc15754** (API `revisions.sha1` == self-computed `sha1sum`, 9955 bytes, fetched 2026-07-21).

- **Quoted** (grep count > 0 in the raw wikitext): "colon principle" (×4); "Green Hackenbush" (×4); "bamboo" stalks (×1); "nim sum" (×2); "Sprague"/"Grundy" (×2); and the near-verbatim colon-principle wording *"when branches come together at a vertex, one may replace the branches by a non-branching stalk of length equal to their nim sum"* — plus *"the game directly becomes Nim and can be directly analyzed as such."*
- **Derived firsthand** (grep count 0): "XOR" / "exclusive or" (0); the literal phrase "equivalent to Nim" (0) and hyphenated "nim-sum" (0); the numeric formulas — a stalk of `n` edges is a Nim heap of size `n`, and a forest's value is the XOR of its stalk lengths — are our derivation. The mex-DP ground-truth engine, all four gate statistics, the z-values, the exact P-density 21/256, and the results digest are the firsthand contribution.
- **Honest posture / relabeling disclosed:** the article develops the colon principle under an "impartial version" heading (lines 41–44) while naming the green variant separately (line 18, "This is also called Green Hackenbush"); joining the two — that the *Green* variant IS that impartial colon-principle game — is our inference, not a single sourced sentence. The "edges disconnected from the ground fall" cutting rule is standard Hackenbush, not restated in those lines. "nim sum" appears with a space, not a hyphen.

## Probe report (v0, self-adversarial)

**1. What is this really?** The exact statement that the impartial (all-green) Hackenbush game reduces to Nim via the colon principle: every rooted forest's Sprague–Grundy value equals the colon-principle value `sub(v,parent) = XOR over children c of (1 + sub(c,v))`, forest value = XOR over ground-neighbours, so a bamboo forest `(a₁,…,aₖ)` has value `a₁⊕…⊕aₖ` and is a first-player win iff the nim-sum is nonzero. It is proved firsthand by an independent mex-DP engine that plays the game, not by asserting the theorem.

**2. Is it non-trivial / not a duplicate?** Yes. green-hackenbush / colon-principle is grep-0 across both repos. It is distinct from the named prior game heads — Sprague–Grundy nim-sum (P219, the abstract disjunctive-sum theorem), Fibonacci nim / Zeckendorf (P243, a take-away game), Wythoff (P239, a two-pile pursuit game), and Banzhaf voting power (P203, a power index): those are abstract-sum / take-away / pursuit / power objects; this is the concrete colon-principle reduction of a specific topological game (Green Hackenbush) to Nim.

**3. How could the engine be wrong, and what guards it?** The mex-DP engine could mis-handle the ground-fall pruning, memoization, or the mex, silently producing wrong Grundy values that happen to agree with a buggy closed form. This is guarded by the **exhaustive** enumeration of all rooted trees `≤ 7` edges in G1 — 800 positions, 0 mismatches, max 34 edges — where the two computations are genuinely independent (one is a game oracle, the other pure XOR arithmetic); a shared bug would have to corrupt both in exactly the same way across every position, which the exhaustive sweep plus the anchor table (3,5,7)→1, Y-tree→1, explicit tree→4 rules out.

**4. Is the digest deterministic?** Yes. SEED=20260717 is a hardcoded constant, all floats are rounded to 10 decimals before hashing, and the digest is the sha256 of the canonical-JSON results dict. Determinism is confirmed three ways: an in-process double-run via `--selfcheck`, a separate process re-invocation, both byte-identical. `results_sha256 = f1967eac6a0158fb4b1546facd309355577f251033067167296f6b921903c0b9`.

**5. What do the foils rule out?** G4 pre-registers two plausible-but-wrong classification rules and rejects both on the same sample: Foil A "sum-parity" (P iff `a₁+a₂+a₃` even) at `z = −373.4` and Foil B "sum-mod-3" (P iff sum ≡ 0 mod 3) at `z = −237.0`, while the correct XOR rule agrees at `z = 0.731`. This shows the P-density is carried specifically by the nim-sum structure, not by any coarse arithmetic-sum statistic that a casual observer might guess.

**6. What are the limits?** The mex-DP engine is exponential in the number of edges, so the random battery of trees/forests is capped at ~14 edges (the exhaustive sweep runs to ≤7 edges, the random battery reaches 34 edges on tractable shapes) — while `colon_value` scales freely to any size. The exact identity is what carries the claim; the Monte-Carlo leg confirms the density on the bamboo model, and the closed form remains valid well beyond the horizon the game oracle can reach.

**7. Who consumes it?** sim-lab, as the paired VERDICT 260 (+13 offset) reproduction — a separate coordinator-driven slice that re-runs the verifier and checks the digest and the four gates.

**8. How will we know it worked?** Byte-identical digest reproduction: sim-lab VERDICT 260 re-runs SEED=20260717 and obtains `results_sha256 = f1967eac6a0158fb4b1546facd309355577f251033067167296f6b921903c0b9` (in-process double-run via `--selfcheck` + separate re-invocation byte-identical), with all four gates PASS each in its own direction and `all_pass = true, first_failing_gate = null, decision = PASS`.

**Recommendation: sim-ready**
