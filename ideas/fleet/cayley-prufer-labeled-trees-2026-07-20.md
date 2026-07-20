# Cayley's formula via the Prüfer bijection: the number of labeled trees on `{1..n}` is exactly `n^(n-2)`

> **State:** sim-ready
> **Status:** `sim-ready` — PROPOSAL 224 (round-53 UNRELATED slot) → VERDICT 237 (+13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Cayley%27s_formula&oldid=1293533452@910071d1648b9817de6852fa2d98e1e6b260e94a · fetched 2026-07-20T18:34:00Z
>
> Verifier (merged firsthand in sim-lab): `sims/verdict-237-cayley-prufer/cayley-prufer.py` (sim-lab PR #318). Paired verdict: VERDICT 237 (offset +13).
> results_sha256 = `7e8dbff568cf62ab3e15ebdc1d9a7e893f024d10f4bd39b1630cbc444317ad1b`

## Head

**Cayley's formula.** The number of labeled trees on the vertex set `{1, 2, …, n}` is **EXACTLY**

```
T(n) = n^(n-2)   for n >= 2.
```

The claim is not "there are roughly exponentially many trees" but the exact integer count, proven **bijectively** by the **Prüfer sequence** — the cleanest of the many proofs (Borchardt 1860; Cayley 1889; Prüfer 1918):

- **Encode.** Given a labeled tree on `{1..n}`, repeatedly delete the smallest-labeled leaf and record the label of its unique neighbor; stop when two vertices remain. This yields a string of length `n − 2` over the alphabet `{1..n}` — the tree's Prüfer sequence.
- **Decode.** Given any string in `{1..n}^(n-2)`, the neighbor-multiset reconstruction inverts the encode step and returns a unique tree.
- Encode and decode are mutual inverses, so trees on `{1..n}` are in **bijection** with `{1..n}^(n-2)`. Hence `T(n) = |{1..n}^(n-2)| = n^(n-2)`.

A vertex `v` appears in the Prüfer sequence exactly `deg(v) − 1` times (each non-final deletion of a neighbor records `v` once, and `v` keeps one edge to the end), which turns the bijection into a probability engine. For a **uniformly random labeled tree** on `{1..n}` (equivalently, a uniformly random Prüfer string, each of the `n − 2` positions i.i.d. uniform on `{1..n}`):

```
E[deg(v)]         = 2 − 2/n
P(specific edge {i,j} present) = 2/n
P(v is a leaf)    = ((n − 1)/n)^(n-2).
```

`E[deg(v)] = 2 − 2/n` is forced (a tree has `n − 1` edges, so the degree sum is `2(n − 1)`, split by symmetry over `n` vertices). `P(edge {i,j}) = 2/n` follows because the `n − 1` edges are spread symmetrically over the `C(n,2)` possible pairs: `(n−1)/(n(n−1)/2) = 2/n`. `P(v is a leaf) = ((n−1)/n)^(n-2)` because `v` is a leaf iff it is *absent* from the length-`(n−2)` Prüfer string.

## Why it matters (fleet framing)

Counting the labeled configurations of a connected acyclic structure is a **closed-form integer, not an estimate**. Any place a fleet reasons about spanning structures over `n` labeled things — the number of distinct ways to wire `n` lanes into a single connected acyclic dependency tree, the number of spanning trees a fully-connected `n`-node coordination graph admits (`K_n` has exactly `n^(n-2)` spanning trees, the same count) — is governed by `n^(n-2)`, and the *shape* statistics of a random such wiring are pinned by the Prüfer encoding, not left to intuition. Two design traps fall out. First, the plausible-but-wrong belief that a "specific edge" in a random tree is a coin flip (`P = 1/2`) is exactly wrong — it is `2/n`, which the falsifiability gate kills at 298σ. Second, confusing "edge present" with "vertex is this particular endpoint" (`P = 1/n`) is a near-miss a designer might write down; it is rejected at 134σ. The correct edge rate is `2/n` because each of the `n − 1` tree edges is one of `C(n,2)` symmetric candidates.

## Exact core identities (proved firsthand by the verifier)

- **Cayley identity (EQUALITY, brute union-find count):** exhaustively enumerating every labeled tree on `{1..n}` (edge-subsets of `K_n` that are connected and acyclic, tested by union-find) yields `T(n) = n^(n-2)` exactly for `n = 2..6`:
  - `n=2 → 1 = 2^0`, `n=3 → 3 = 3^1`, `n=4 → 16 = 4^2`, `n=5 → 125 = 5^3`, `n=6 → 1296 = 6^4`.
- **Bijection roundtrip (EQUALITY):** at `n = 5`, all `125` enumerated trees encode to a Prüfer string and decode back to the identical tree (roundtrip fixed-point), and the `125` resulting strings are all `5^3 = 125` sequences with **no collision** — a genuine bijection, not a lossy hash.
- **Exact consequences (EQUALITY, `fractions.Fraction`) at `n = 5`:** `P(edge {1,2}) = 2/5`, mean `deg(1) = 8/5`, `P(1 is a leaf) = 64/125` — each an exact reduced rational, never a float.

## Gate battery (SEED=20260717, Z_GATE=3.0, deterministic; each direction stated)

| Gate | Kind | Direction / PASS rule | Result |
|---|---|---|---|
| G1 | Exact Cayley identity (EQUALITY, brute union-find) | `T(n)` counted exhaustively `== n^(n-2)` for `n=2..6` | `1,3,16,125,1296` exact ✅ |
| G2 | Exact bijection roundtrip (EQUALITY) | all `125` trees at `n=5` roundtrip; `125` Prüfer strings = all `5^3` distinct (no collision) | 0 mismatch, 0 collision ✅ |
| G3 | Exact consequences (EQUALITY, `Fraction`) | `n=5`: `P(edge{1,2})==2/5`, mean `deg(1)==8/5`, leaf prob `==64/125` | exact equal ✅ |
| G4 | MC agreement (AGREEMENT, `|z| < 3`) | `n=12` random Prüfer sample: edge-rate and mean-degree match theory | `z_edge=−0.35`, `z_deg=0.809` ✅ |
| G5 | Robustness (EQUALITY + AGREEMENT) | identity `n=2..8` all match; edge-prob MC at `n=6/10/20` all `|z|<3` | all match, all `|z|<3` ✅ |
| G6 | Falsifiability (REJECTION) | counts uniquely `≠ n^(n-1)/(n-1)!/2^(n-1)`; naive `P=1/2` and `P=1/n` rejected | `z=−298.4`, `z=+134.4` REJECTED ✅ |

All six PASS; `all_pass=true`, `first_failing_gate=null`. Each gate is checked **in its own direction**: the exact-integer and exact-`Fraction` gates require zero error, the Monte-Carlo agreement gates require the sampled statistic to sit inside 3σ of the theoretical value, and the falsifiability gate requires the wrong models to be rejected far *outside* the band (edge-rate `2/n` vs the naive coin-flip `1/2` and the endpoint-confusion `1/n`).

## Determinism & digest

`build_results()` is a pure function of `SEED=20260717` and the fixed configuration grid (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture). `main()` runs it twice and asserts the canonical JSON forms are byte-identical; a separate re-invocation reproduces the same digest. Full 64-hex:

```
results_sha256: 7e8dbff568cf62ab3e15ebdc1d9a7e893f024d10f4bd39b1630cbc444317ad1b
```

## Grounding & scope

Cayley's formula and the Prüfer-sequence proof are grounded in the English Wikipedia article **"Cayley's formula"** at pinned revision `https://en.wikipedia.org/w/index.php?title=Cayley%27s_formula&oldid=1293533452`@`910071d1648b9817de6852fa2d98e1e6b260e94a` (rev 2025-06-02T06:55:49Z). The `action=raw` wikitext bytes (4632 bytes) hash to exactly the MediaWiki-reported rev sha1 (`sha1sum` of the fetched bytes = `910071d1648b9817de6852fa2d98e1e6b260e94a`, MATCH the API `rvprop=sha1`).

**Scope caveat (verified by grep of the pinned wikitext).** The pinned revision DOES state, verbatim (QUOTED): "for every positive integer `n`, the number of trees on `n` labeled vertices is `n^{n-2}`", it shows the `n=2,3,4` census `2^{2-2}=1`, `3^{3-2}=3`, `4^{4-2}=16`, it names the **Prüfer sequence** as a proof method, notes the formula "equivalently counts the spanning trees of a complete graph", and credits Borchardt (1860) / Cayley (1889). It does **NOT** state the uniform-random-tree consequences: the strings `2/n`, `2-2/n`, and the leaf probability `((n-1)/n)^(n-2)` do **not** appear on the page (grep: 0 hits for `2/n`; no edge-probability, expected-degree, or leaf-probability passage). Those three consequences are therefore **DERIVED** firsthand from the Prüfer encoding and machine-checked by the verifier — not quoted from Wikipedia. The core identity `n^(n-2)` is **quoted**; the random-tree statistics are **derived**. Neither oversold nor undersold.

## Reproduce

```
python3 sims/verdict-237-cayley-prufer/cayley-prufer.py   # (in sim-lab)
```

Exit 0 iff all six gates pass; prints the results dict and `results_sha256:`. The verifier is stdlib-only (`itertools`, `random`, `json`, `hashlib`, `math`, `fractions`) and already merged in sim-lab (PR #318, VERDICT 237); an in-process double-run and a separate re-invocation are byte-identical.

## Probe report (v0, 2026-07-20)

**1. Is `n^(n-2)` a coincidence of small `n`, or the real closed form?** Real. G1 counts labeled trees *exhaustively* by union-find over edge-subsets of `K_n` for `n = 2..6` and gets `1, 3, 16, 125, 1296` — five *different* values, each landing on `n^(n-2)` with zero slack. A formula fitted to one `n` would miss the others; this one does not. G5 extends the exact identity to `n = 8`. The count is the exponential integer, not a small-`n` artifact.

**2. Is the "proof" an actual bijection, or a lossy encoding that merely has the right cardinality?** A genuine bijection. G2 does not just count — it roundtrips: every one of the `125` trees at `n = 5` encodes to a Prüfer string and *decodes back to the identical tree* (fixed point), and the `125` strings are checked to be `5^3` **distinct** with no collision. A lossy hash with the right output count would fail either the roundtrip or the no-collision leg; both hold.

**3. Are the random-tree consequences the right stochastic reading, or decoration?** They are exact identities, corroborated stochastically. G3 computes `P(edge{1,2})`, `E[deg(1)]`, and leaf probability as exact `fractions.Fraction` at `n = 5` (`2/5`, `8/5`, `64/125`); G4 then samples uniform Prüfer strings at `n = 12` and confirms the edge-rate and mean-degree estimators agree within 3σ (`z_edge=−0.35`, `z_deg=0.809`). The exact `Fraction` gates are the proof; the MC leg is independent corroboration that would diverge if the closed forms were wrong.

**4. Is the falsified alternative actually the naive one someone would pick?** Yes — deliberately two of them. `P(edge)=1/2` is the "is this pair connected? coin flip" reflex; `P(edge)=1/n` is the "vertex `v` is this specific endpoint" confusion. G6 rejects the coin-flip at `z=−298.4` and the `1/n` near-miss at `z=+134.4`. Both are genuine traps a designer might write down, not straw men — the true rate is `2/n`.

**5. Does the result rely on any hidden float or ordering assumption?** No. The counts are exact integers (union-find over enumerated edge-subsets), the consequences are exact `fractions.Fraction`, and the bijection is order-canonical (encode always deletes the *smallest-labeled* leaf, decode consumes the string left-to-right). G5's robustness leg re-checks the identity across `n = 2..8` and the edge-probability MC across `n = 6/10/20`, so the result is not a fixed-`n` or fixed-seed fluke.

**6. Are the falsifiability gates real teeth or trivially satisfied?** Real. G6 is a *rejection* gate in the opposite direction to the agreement gate G4 — it also checks that the true tree count is uniquely `≠ n^(n-1)/(n-1)!/2^(n-1)` (a plausible over-counting formula), and rejects both naive edge probabilities at `|z| > 100`. A verifier that reproduced only a wrong model would (correctly) fail G6.

**7. Is `all_pass` gameable by a single degenerate parameter?** No. The six gates test distinct directions: an exact brute-count identity, an exact bijection roundtrip + no-collision, three exact-`Fraction` consequences, two Monte-Carlo agreement statistics, a multi-`n` robustness sweep, and a two-pronged falsifiability rejection. No single degenerate `n` or seed satisfies all six; a verdict session reproduces the exact 64-hex digest to confirm every constant.

**8. How will a verdict session know it reproduced the head?** It re-runs the stdlib verifier under `SEED=20260717`, and confirms `all_pass=true`, `first_failing_gate=null`, the exact counts `{1,3,16,125,1296}`, the `n=5` bijection roundtrip with no collision, the exact consequences `{2/5, 8/5, 64/125}`, the four gate z-scores (`−0.35`, `0.809`, `−298.4`, `+134.4`), and results-dict sha256 `7e8dbff568cf62ab3e15ebdc1d9a7e893f024d10f4bd39b1630cbc444317ad1b` byte-for-byte (in-process double-run and separate-process run byte-identical). Any gate fail or digest mismatch is a REJECT. This paired verifier already merged as sim-lab PR #318 (VERDICT 237).

## One-line design fix

When you count the ways to wire `n` labeled things into a single connected acyclic structure, the answer is exactly `n^(n-2)` (not an estimate), and the shape of a *random* such wiring is pinned by the Prüfer encoding — a specific edge appears with probability `2/n` (not `1/2`, not `1/n`) and expected degree is `2 − 2/n` — so read those constants off the bijection, do not guess them.

**Recommendation: sim-ready**
