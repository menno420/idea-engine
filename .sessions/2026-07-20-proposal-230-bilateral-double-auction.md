# Session — PROPOSAL 230 (bilateral double auction → VERDICT 243)

> **Status:** `complete`
> Born-red HOLD: this card lands `in-progress` on the first commit to hold the PR red through the substrate-gate, and flips to `complete` as the deliberate last commit once the idea doc, verifier, outbox block, and claim are in place and the paired sim-lab reproduction is verified green. Merge is by native squash auto-merge on all-green.

## 💡 Session idea
Round-56 VENTURE slot. PROPOSAL 230: the Chatterjee–Samuelson k=1/2 bilateral double auction with buyer value v and seller cost c iid Uniform[0,1] has the linear Bayes–Nash equilibrium b(v)=2v/3+1/12, s(c)=2c/3+1/4; because the offers are parallel, trade happens exactly when v−c≥1/4; expected realized gains are exactly 9/64 versus first-best 1/6 (efficiency 27/32, deadweight 5/192) — a closed-form signature of Myerson–Satterthwaite impossibility. Paired reproduction mirror in sim-lab under sims/verdict-243-bilateral-double-auction/ (offset +13); the canonical independent ruling is a separate coordinator-driven VERDICT 243 slice.

## ⟲ Previous-session review
P228 (UNRELATED, random-walk no-return → VERDICT 241) landed. Rotation advances to the VENTURE slot at P230 (P229 is a sibling's in-flight slot; ledger union-resolved). This slice does not touch control/status.md (coordinator-owned) and does not author a VERDICT block or advance the verdict high-water; proposal high-water advances P228 → P230.

## 🫀 Heartbeat
Verifier ideas/venture-lab/bilateral-double-auction.py verified green before flip: exit 0, all four gates PASS, results_sha256 5052053d3a6cb6fb1419afe0846f4f339d3537057d6ee5fbeb8a86e9b9ea42c3 byte-identical across in-process double-run + separate re-invocation (SEED=20260717, stdlib-only, Python 3.11.15). G1 EXACT Fraction integration delta=1/4 realized=9/64 first_best=1/6 efficiency=27/32 deadweight=5/192 trade_prob=9/32. G2 MC N=200000 z_gains=−0.123561 (p̂=0.140558) z_trade=−0.258615 (p̂=0.28099), both |z|<3. G3 buyer+seller grid best-response argmax == closed form at all four probes AND a second exact route (difference density f_D(d)=1−d) reproduces 9/64. G4 efficient rule agrees with 1/6 (z=−0.308089) while equilibrium gains reject the naive-efficient 1/6 at z=−47.919492 (>6). Grounding pins Wikipedia "Double auction" oldid 1346190881 sha1 ffbd1f23d644439cf57dfe7be48fc39990d9b68a. A byte-identical copy is carried in the paired sim-lab reproduction PR (branch claude/verdict-243-bilateral-double-auction); the canonical independent ruling is a separate coordinator-driven VERDICT 243 slice.

> **📊 Model:** Claude Opus · high · proposal-authoring / VENTURE slot

## Decisions made
- Chose the Chatterjee–Samuelson linear double-auction equilibrium — bilateral two-sided trade, distinct from P226 (Myerson optimal reserve, one-sided) and P222 (revenue equivalence).
- Best-response probe points restricted to v>1/4 and c<3/4 so the equilibrium offer trades with positive probability and the grid argmax is a unique interior maximum (outside that range every non-trading offer ties at zero payoff).
- Kept G1/G3 non-tautological via exact rational polynomial integration plus an independent difference-density route, both landing on 9/64.
- Grounding pinned to the Double auction revision (carries linear-equilibrium existence under a uniform prior + the MS impossibility incl. the k=1 corollary); every specific number is honestly labelled derived.
- Did not author a VERDICT block or advance the verdict high-water, and did not touch control/status.md, per the ledger-convention refinement — the canonical VERDICT 243 ruling is a dedicated slice.

## Next session should know
- Rotation next cycles to the GAME slot (P231/P232 depending on the sibling union).
- The paired sim-lab reproduction mirror lands the byte-identical verifier under sims/verdict-243-bilateral-double-auction/; the canonical independent VERDICT 243 ruling is still pending its dedicated coordinator-driven slice (as is the V241 mirror — union-resolve the verdict ledger there).
- No edits were made to control/status.md.
