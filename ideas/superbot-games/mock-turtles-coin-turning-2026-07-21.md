# Mock Turtles is an impartial coin-turning game (normal play, last to move wins) where a move turns over 1, 2, or 3 coins with the rightmost turned coin going Heads→Tails; the Sprague–Grundy value of a single heads-up coin at position n is the Mock-Turtle number g(n) = the unique ODIOUS member of {2n, 2n+1} (g(n)=2n if popcount(n) is odd, else 2n+1 — the odious numbers 1,2,4,7,8,11,13,14,16,… of OEIS A000069), and by the coin-turning decomposition the value of any position with heads at set S is the nim-sum ⊕ₙ∈S g(n), so the first player wins iff that nim-sum is nonzero (anchors: g(0)=1, g(1)=2, g(2)=4, g(3)=7, g(4)=8, g(5)=11, g(6)=13, g(7)=14, g(8)=16).

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem?oldid=1362556548@818faacdf5b5a059f160a8550c7b4c1acd5719a2 · fetched 2026-07-21

**Lane:** superbot-games · combinatorial game / Sprague–Grundy · coin-turning family
**Proposal:** 255 → Verdict 268 (+13 offset) — named by the `## PROPOSAL 255` block in `control/outbox.md`
**Verifier:** [`verify_255_mock_turtles.py`](verify_255_mock_turtles.py) · stdlib only (json, hashlib, math, random, fractions, itertools, argparse, sys) · SEED=20260717
**File sha256:** `b4df1b47239ca4b457ef9adbd410463ba932416ff91b1aaab6042922abb8834b`
**Digest:** `results_sha256 = 6b4b3775427d90daea848f4e4c3779ba35ba9e34dab9ee6c906cb6ed33c2f868`

## What this proposal does

Adds a superbot-games PROPOSAL establishing the **odious closed form** of **Mock Turtles**, an impartial **coin-turning game**. A row of coins occupies positions `n = 0,1,2,…`, each Heads (`H`) or Tails (`T`). A **move** turns over **1, 2, or 3** coins subject to the single constraint that the **rightmost (largest-index) coin turned must go from Heads to Tails** — this strictly lowers the largest head index every move, so play always terminates. Normal play: the player who cannot move loses.

The claim is the exact single-coin Grundy value and its consequence:

1. **Single-coin closed form.** The Sprague–Grundy value of a lone heads-up coin at position `n` is the **Mock-Turtle number** `g(n)` = the unique **odious** member of `{2n, 2n+1}` — where a number is *odious* iff its binary popcount is odd. Equivalently `g(n) = 2n` if `popcount(n)` is odd, else `g(n) = 2n+1`. These `g(n)` are exactly the **odious numbers** `1,2,4,7,8,11,13,14,16,…` (OEIS **A000069**) in increasing order — `g(n)` is the `n`-th odious number.
2. **Decomposition (XOR-sum).** By the coin-turning decomposition — a corollary of the Sprague–Grundy sum theorem, since every coin-turning position is the disjunctive sum of its single-heads coins — the Grundy value of ANY position with heads at set `S` is the **nim-sum** `⊕_{n∈S} g(n)`. The **first player wins iff this nim-sum ≠ 0**; the P-positions (second-player wins) are exactly those with nim-sum `0`.

The proposal ships a stdlib-only firsthand verifier that proves the claim by pitting an **independent from-scratch game oracle** — a memoized `mex`-DP over `frozenset` positions that knows nothing of the closed form — against the odious closed form, through **four gates each in its own direction** (an exact identity + decomposition sweep, a Monte-Carlo P-density agreement, an invariance/robustness leg, and a value-level falsifiability leg that rejects two naive foils), all wrapped in a reproducible `SEED=20260717` digest.

**Distinctness.** This is the **coin-turning family** (odious-number closed form), categorically distinct from every shipped game head: the subtraction game (**P219**, `g(n)=n mod 4`), Green Hackenbush = Nim / colon principle (**P247**), Wythoff (**P239**), Fibonacci-nim / Zeckendorf (**P243**). Its natural **foil** is **Turning Turtles** — the same game but turning only **1 OR 2** coins — whose single-coin value is the plain `g(n)=n` (ordinary Nim); allowing up to **three** coins is exactly what introduces the odious correction that separates Mock Turtles from Turning Turtles. `mock-turtle` / `coin-turning` / `odious` is **grep-0** across both repos.

## Method

Ground-truth engine first, closed form second, then the two are forced to agree.

**The game oracle (assumes no theorem).** A position is a `frozenset` of head positions. `moves(pos)` enumerates every legal move exactly once: for each head `h` (the rightmost turned coin, `H→T`) choose any `0/1/2` extra indices strictly below `h` to toggle, giving successor `pos △ ({h}∪extra)`. `grundy(pos)` is the memoized **mex** over the values of all successors, with `grundy(∅)=0`. This engine plays the game; it never references `g(n)`.

**The closed form.** `closed_g(n) = 2n if popcount(n) is odd else 2n+1`, cross-checked BOTH ways to equal "the unique odious member of `{2n,2n+1}`" (exactly one of the pair is odious, since `2n+1` flips the last bit of `2n`). A dedicated single-coin DP `single_coin_grundy(n)` — independent of `closed_g` — computes the lone-coin value by the `mex` recurrence over its successors (drop coin `n`, add any `0/1/2` coins below `n`, valued by the decomposition), reaching `n=255` where the exponential general oracle cannot.

**Determinism.** `SEED=20260717` (hardcoded); `random` is reseeded at the start of every sampling gate so gate order cannot perturb the payload; every float enters the payload via a fixed format string and every count as an int; the digest is the sha256 of the canonical-JSON results dict. Determinism is verified **three ways** — in-process double-run, a `--selfcheck` path, and a separate process re-invocation — all byte-identical.

## Exact reference

The from-scratch `mex`-DP oracle and the odious closed form agree on every single-coin anchor, and the decomposition holds over **all `2¹³` positions**:

| n | popcount(n) | odious? | g(n) = odious({2n, 2n+1}) | oracle grundy({n}) |
|---|---|---|---|---|
| 0 | 0 (even) | 2·0+1 = **1** | **1** | 1 |
| 1 | 1 (odd) | 2·1 = **2** | **2** | 2 |
| 2 | 1 (odd) | 2·2 = **4** | **4** | 4 |
| 3 | 2 (even) | 2·3+1 = **7** | **7** | 7 |
| 4 | 1 (odd) | 2·4 = **8** | **8** | 8 |
| 5 | 2 (even) | 2·5+1 = **11** | **11** | 11 |
| 6 | 2 (even) | 2·6+1 = **13** | **13** | 13 |
| 7 | 3 (odd) | 2·7 = **14** | **14** | 14 |
| 8 | 1 (odd) | 2·8 = **16** | **16** | 16 |

The sequence `(g(n))ₙ` equals the sorted odious numbers `1,2,4,7,8,11,13,14,16,…` (A000069) over the whole `n=0..255` range. Example composite position `{1,2,4,7}` has oracle Grundy value `g(1)⊕g(2)⊕g(4)⊕g(7) = 2⊕4⊕8⊕14 = 0` — a **P-position** (second-player win), confirmed by the general oracle directly.

## Four gates (each in its own direction)

- **G1 — EXACT (integer/XOR, zero tolerance).** (a) The single-coin DP `single_coin_grundy(n) == closed_g(n)` for **every `n=0..255`** — `single_coin_mismatches = 0`; the anchors are asserted; `closed_g` equals the odious member of `{2n,2n+1}` both ways; and `(g(n))ₙ` equals the sorted odious numbers. (b) **Decomposition:** the general from-scratch oracle over **all `2¹³ = 8192` positions** on `K=13` slots satisfies `grundy(pos) == ⊕ closed_g(heads)` — `decomp_mismatches = 0`. This validates the odious closed form AND the XOR-sum theorem firsthand. Exact → reported `z = "exact — z=n/a"`. **PASS.**
- **G2 — Monte-Carlo agreement (`|z| < 3`).** Enumerating all `2¹⁶` positions on `L=16` slots gives the exact P-density `p0 = 1/32` (the `g(0..15)` span a rank-5 space over GF(2) — they include the basis `1,2,4,8,16` — so `2¹⁶⁻⁵ = 2¹¹` of the `2¹⁶` positions have nim-sum 0). `N = 2,000,000` iid random positions (each coin Heads w.p. 1/2, seeded) give `p̂ = 0.0310335`, `z = −1.7597`, `|z| < 3` [Z_ACCEPT=3.0]. iid draws → plain iid SE is honest (no batch means). **PASS.**
- **G3 — invariance / robustness (0 discrepancies).** (a) **Disjoint-sum:** for `400` random pairs `A, B` on DISJOINT coordinate blocks, `grundy(A ∪ shift(B)) == grundy(A) ⊕ grundy(shift(B))` via the general oracle — `disjoint_discrepancies = 0` (note `g` depends on ABSOLUTE position, so the summand is `grundy(shift(B))`, not `grundy(B)`). (b) **Optimal-play robustness:** from `300` random first-player-WIN starts (nim-sum ≠ 0), a strategist that always moves to a nim-sum-0 successor beats a random opponent **every game** — `optimal_play_losses = 0`; and from nim-sum-0 starts **every** legal move leaves nim-sum ≠ 0 (the P-position property) — `pprop_violations = 0` over all moves of `400` P-positions. **PASS.**
- **G4 — falsifiability (value level, opposite polarity, reject at `|z| > 6`).** The general oracle's TRUE Grundy value (`== ⊕ closed_g`, cross-checked) is ground truth on `N = 2,000,000` iid positions (`L=13`). A foil "`g(n)=…`" is a claim about Grundy VALUES, so the fundamental falsification is the value-level disagreement. **Foil-A "g(n)=n"** (Mock Turtles = Turning Turtles = plain Nim) is rejected at `z_foil_A = 7832.71`; **Foil-B "g(n)=2n+1 for all n"** (drops the odious correction) is rejected at `z_foil_B = 1413.69`. Value witnesses: `{0}` (foil-A value 0 vs true 1) and `{1}` (foil-B value 3 vs true 2); single-coin `n=1`: true `g=2`, foil-A says `1`, foil-B says `3`. **PASS.**

  **Firsthand subtlety surfaced (disclosed honestly).** At the coarser **P-indicator (win/loss)** level, foil-A also fails (`p_disagree_A = 62318`, e.g. `{0}`: true N-position but foil-A predicts P), but **foil-B reproduces the true P-set EXACTLY** (`p_disagree_B = 0`). The reason is a popcount-parity identity: `⊕(head indices) = 0` forces `popcount` of the XOR to be `0` (even), hence an **even** number of odious-index heads, which is exactly the condition under which `⊕(2n+1)` and `⊕ closed_g` agree on being zero. So foil-B lands the P/N verdict *by luck* while getting the Grundy VALUES wrong — which is why the value level (what disjunctive-sum play actually needs) is the correct, and decisive, falsification.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = 6b4b3775427d90daea848f4e4c3779ba35ba9e34dab9ee6c906cb6ed33c2f868`. Deterministic three ways: in-process double-run, `--selfcheck` (`SELFCHECK: byte-identical`), and a separate re-invocation, all byte-identical. SEED = 20260717 (hardcoded). Verifier file sha256 `b4df1b47239ca4b457ef9adbd410463ba932416ff91b1aaab6042922abb8834b`.

## Grounding

Two pinned Wikipedia revisions (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match for both):

- **"Sprague–Grundy theorem"**, oldid 1362556548:
  `https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem?oldid=1362556548@818faacdf5b5a059f160a8550c7b4c1acd5719a2` (20199 bytes), fetched 2026-07-21. API `sha1 = 818faacdf5b5a059f160a8550c7b4c1acd5719a2`; self-computed `hashlib.sha1(rawwikitext)` — **match**.
- **"Odious number"**, oldid 1358277188:
  `https://en.wikipedia.org/wiki/Odious_number?oldid=1358277188@787af14a4c6ab7dfadc08d86f65be874f84f6093` (3802 bytes), fetched 2026-07-21. API `sha1 = 787af14a4c6ab7dfadc08d86f65be874f84f6093`; self-computed `hashlib.sha1(rawwikitext)` — **match**. (The article exists in its own right; it does **not** redirect to "Evil number".)

**Quoted** literally on the pinned revisions (grep count > 0 in the raw wikitext):
- *Odious number* — the **definition** "an odious number is a positive integer that has an odd number of 1s in its binary expansion"; the **exact sequence** "The first odious numbers are 1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28, 31, …" — literally the `g(n)` anchor values; the OEIS id "**A000069**"; "odd parity"; "Every power of two is odious".
- *Sprague–Grundy theorem* — "**mex** (minimum exclusion) … the smallest non-negative integer not equal to some `nᵢ`"; the **P-position criterion** "A position is a loss for the next player to move (i.e. a 𝒫-position) if and only if its Grundy value is zero"; the **sum theorem** "The Grundy value of the sum of a finite set of positions is just the **nim-sum** of the Grundy values of its summands"; "normal play condition (a player who cannot move loses)"; "impartial game".

**Derived firsthand** (grep count 0 on both pinned raw wikitexts — confirmed both directions): the **Mock-Turtles game rules** themselves (turn 1/2/3 coins, rightmost `H→T`) — no Wikipedia article for the Mock-Turtles / Turning-Turtles / coin-turning game exists, so the rules and the odious single-coin closed form are **DERIVED / firsthand** (source: Berlekamp–Conway–Guy, *Winning Ways for Your Mathematical Plays*, not Wikipedia-pinnable); the specific formula `g(n) = odious({2n, 2n+1}) = 2n if popcount(n) odd else 2n+1` (grep `2n`, `coin`, `turtle` = 0 on both pages); the identification `g(n) = ` the `n`-th odious number; the `mex`-DP game oracle; the coin-turning decomposition applied to THIS game; the exact `p0 = 1/32`; all z-values; the foil-B P-coincidence parity finding; SEED; and the results digest.

**Honest posture — disclosed seams.** (1) There is **no** Wikipedia article for the coin-turning "Mock Turtles" / "Turning Turtles" game (searched: "Mock Turtles (game)" and "Turning Turtles" are both absent; "Mock turtle" is a 25-byte redirect to an unrelated character), so the game rules and the odious closed form are **not Wikipedia-pinnable** and are cited as firsthand from *Winning Ways*, not oversold as sourced. (2) The Sprague–Grundy page writes "**nim-sum**" and "sum of a finite set of positions"; we relabel these as **XOR (⊕)** and **disjunctive sum** respectively (standard, disclosed). (3) The page states the P-criterion as "loss for the next player iff Grundy value zero"; our "first player wins iff nim-sum ≠ 0" is the contrapositive. (4) The Odious page lists the odious sequence and defines *odious*; that these are exactly the Mock-Turtle numbers `g(n)` is our derivation joining the two pinned facts. Nothing oversold: `mex`, the P-criterion, the nim-sum sum theorem, and the odious definition + sequence are QUOTED verbatim; the game, its single-coin odious formula, the oracle, every statistic, and the digest are the firsthand contribution.

## Probe report (v0, self-adversarial)

**1. What is this really?** The exact statement that Mock Turtles — turn 1/2/3 coins, rightmost `H→T`, normal play — has single-coin Sprague–Grundy value `g(n) = ` the odious member of `{2n, 2n+1}`, and every position's value is the XOR of its coins' `g`, so first player wins iff the nim-sum is nonzero. It is proved firsthand by an independent `mex`-DP oracle that plays the game, not by asserting the theorem: the oracle matches the closed form on **all `2¹³` positions** (G1b) and the single-coin DP matches it for `n=0..255` (G1a).

**2. Is it non-trivial / not a duplicate?** Yes. `mock-turtle` / `coin-turning` / `odious` is grep-0 across both repos. It is the coin-turning family, orthogonal to the subtraction game (P219, `g=n mod 4`), Green Hackenbush = Nim (P247), Wythoff (P239), and Fibonacci-nim (P243). Its foil Turning Turtles (`g=n`, plain Nim) is exactly the "turn 1 or 2 coins" restriction — allowing three coins is what makes the value odious rather than linear.

**3. How could the oracle be wrong, and what guards it?** A `mex`/memoization/move-generation bug could produce wrong Grundy values that happen to agree with a buggy closed form. Guarded by (i) the **exhaustive** `2¹³` decomposition sweep in G1b with 0 mismatches, where the two computations are genuinely independent (game oracle vs pure XOR of `closed_g`), and (ii) the disjoint-sum leg (G3a) checking additivity across coordinate blocks, and (iii) the optimal-play leg (G3b) where the closed-form strategy never loses a real game driven by the oracle's move set. A shared bug would have to corrupt all of these identically.

**4. Is the digest deterministic?** Yes. `build_results()` is a pure function of SEED and fixed params; `random` is reseeded at the start of every sampling gate; every float is a fixed format string, every count an int; no wall-clock / PID / unordered-set iteration enters the payload. In-process double-run, `--selfcheck`, and a separate re-invocation are byte-identical. `results_sha256 = 6b4b3775427d90daea848f4e4c3779ba35ba9e34dab9ee6c906cb6ed33c2f868`.

**5. What do the foils rule out?** G4 pre-registers two plausible-but-wrong Grundy-value rules and rejects both against the oracle's true values: Foil-A "`g=n`" (Turning Turtles / Nim) at `z = 7832.71` and Foil-B "`g=2n+1`" (no odious correction) at `z = 1413.69`. The honest, load-bearing subtlety: Foil-B reproduces the true **P-set** exactly (a popcount-parity coincidence, `p_disagree_B = 0`) yet gets the **values** wrong — so the falsification is done at the value level, which is what disjunctive-sum play requires, not at the coarser P/N level where Foil-B happens to be right.

**6. What are the limits?** The `mex`-DP oracle is exponential in the number of coins, so the exhaustive decomposition sweep is capped at `K=13` slots (`2¹³` positions) and the invariance/robustness legs at `L≤13`; the single-coin DP reaches `n=255` and the closed form scales freely. The exact identity (G1) carries the claim; G2 confirms the P-density on 16 slots, and the closed form remains valid well beyond the oracle's horizon.

**7. Who consumes it?** sim-lab, as the paired **VERDICT 268** (+13 offset) reproduction — a separate coordinator-driven slice that re-runs the verifier and checks the digest and the four gates.

**8. How will we know it worked?** Byte-identical digest reproduction: sim-lab VERDICT 268 re-runs `SEED=20260717` and obtains `results_sha256 = 6b4b3775427d90daea848f4e4c3779ba35ba9e34dab9ee6c906cb6ed33c2f868` (in-process double-run + `--selfcheck` + separate re-invocation byte-identical), with all four gates PASS each in its own direction and `all_gates_pass = true`, `first_failing_gate = null`, `decision = PASS`.

**Recommendation: sim-ready**
