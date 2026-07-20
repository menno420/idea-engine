# Nim / Sprague–Grundy: the nim-sum zero criterion and the Sub({1..k}) Grundy closed form

> **Status:** `sim-ready` — PROPOSAL 219 (round-52 GAME slot) → VERDICT 232 (+13 offset)
>
> Verifier: `ideas/superbot-games/sprague-grundy-nim-sum-2026-07-20.py` (byte-identical copy in sim-lab `sims/verdict-232-sprague-grundy-nim-sum/sprague_grundy_nim_sum.py`).
> results_sha256 = `e50e461d105e4984f6f562def0eba3f527ef4030512f9cf75294ddd6709002b7`

## Head

In an impartial combinatorial game, a disjunctive-sum position is a **loss for the player to move** (a *P-position*) **iff the XOR ("nim-sum") of its component Grundy values is zero** — the Sprague–Grundy theorem. Two exactly-true corollaries carry the claim:

- **Nim P-density.** For `d`-heap Nim with heaps drawn uniformly from a binary range `{0,…,2^b−1}`, the nim-sum is uniform on the group, so the exact P-position density is `1/2^b`. For `d=3`, `b=3` (heaps in `{0,…,7}`) that is exactly `1/8`.
- **Subtraction-game Grundy closed form.** For the single-heap subtraction game `Sub({1,…,k})`, the Grundy value has the closed form `G(n) = n mod (k+1)`, and the Grundy value of a disjunctive sum of heaps equals the XOR (nim-sum) of the per-heap Grundy values.

## Why it matters (fleet framing)

Independent impartial sub-tasks compose by nim-sum, not by totals: whether the player-to-move is in a losing balance is decided by the XOR of component Grundy values, not the sum of heap sizes. A "parity of the total" heuristic — the intuitive but wrong belief that whoever faces an even token-count loses — is exactly the naive trap the falsifiability gate kills at 300+ sigma. The correct invariant is XOR-to-zero.

## Exact core identities (proved firsthand by the verifier)

- `Sub({1,2,3})`: `G(n) = n mod 4` for all `n ∈ [0,256]` — 0 mismatches (mex recurrence vs closed form).
- Disjunctive sum of two `Sub({1,2,3})` heaps: `G_sum(a,b) = G(a) ⊕ G(b)` for all `(a,b) ∈ [0,40]²` — 0 mismatches, `G_sum` computed by mex over the joint move set.
- Exhaustive Nim P-density over `{0,…,7}³`: exactly `Fraction(1,8)` (64 of 512 triples have nim-sum zero).

## Gate battery (SEED=20260717, deterministic; each direction stated)

| Gate | Kind | Direction / PASS rule | Result |
|---|---|---|---|
| G1 | MC significance | MC 3-heap P-density agrees with exact `1/8`, `|z| < 3` | z=1.446904 ✅ |
| G2 | Exact (Fraction) | exhaustive density `== Fraction(1,8)`, count `== 64` | equal ✅ |
| G3 | Exact-Grundy | `G(n) == n mod 4`, `n∈[0,256]`, 0 mismatch | 0 ✅ |
| G4 | Sprague–Grundy sum | `G_sum == G(a)⊕G(b)`, `(a,b)∈[0,40]²`, 0 mismatch | 0 ✅ |
| G5 | Robustness | `G(n)==n mod (k+1)`, `k∈{2,3,4,5}`, 0 mismatch | 0 ✅ |
| G6 | Falsifiability | naive total-parity (density `1/2`) REJECTED, `|z|>3` | z=−334.45 ✅ |

All six PASS; `all_pass=true`, `first_failing_gate=null`. Each gate is checked in its own direction: exact-equality gates require zero error, the MC gate requires agreement inside 3σ, and the falsifiability gate requires the wrong model to be rejected far outside 3σ.

## Determinism & digest

`build_results()` is a pure function of `SEED` and the fixed params (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture). `main()` runs it twice and asserts the canonical JSON forms are byte-identical; a separate re-invocation reproduces the same digest. Full 64-hex:

```
results_sha256: e50e461d105e4984f6f562def0eba3f527ef4030512f9cf75294ddd6709002b7
```

## Grounding & scope

The nim-sum (XOR) winning criterion is grounded in the English Wikipedia article "Nim" at pinned revision `https://en.wikipedia.org/w/index.php?title=Nim&oldid=1362772636`@`750a8fd6ead1d0b082596aab4f84d9d4bd49da78` (rev 2026-07-06T02:51:13Z), which states verbatim: "In a normal nim game, the player making the first move has a winning strategy if and only if the nim-sum of the sizes of the heaps is not zero" — equivalently, a position is a loss for the player to move iff the nim-sum (bitwise XOR) of the heap sizes is zero. The disjunctive-sum rule — that the Grundy value of a sum of positions is the nim-sum (XOR) of the summands' Grundy values, a position is a P-position iff its Grundy value is zero, and Grundy values are defined via the mex (minimum excludant) — is grounded in the "Sprague–Grundy theorem" article at pinned revision `https://en.wikipedia.org/w/index.php?title=Sprague%E2%80%93Grundy_theorem&oldid=1362556548`@`818faacdf5b5a059f160a8550c7b4c1acd5719a2` (rev 2026-07-04T19:24:32Z). For both revisions the `action=raw` wikitext bytes hash to exactly the MediaWiki-reported rev sha1.

**Scope caveat (verified by grep of the pinned wikitext):** these external sources establish the XOR/nim-sum criteria and the mex-based Grundy framework, but neither states the closed-form subtraction-game identity `G(n) = n mod (k+1)` as an equation. The Nim article's "subtraction game" section gives only the outcome condition `n ≡ 0 (mod k+1)` (win/loss), not an explicit Grundy-value formula, and the Sprague–Grundy article does not treat bounded subtraction games at all. The closed-form Grundy identity `G(n) = n mod (k+1)`, the disjunctive-sum reproduction, and the digest are therefore established FIRSTHAND by the verifier, not taken from Wikipedia.

## Reproduce

```
python3 ideas/superbot-games/sprague-grundy-nim-sum-2026-07-20.py
```

Exit 0 iff all gates pass; prints the results dict and `results_sha256:`.
