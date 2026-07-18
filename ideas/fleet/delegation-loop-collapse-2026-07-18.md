# Delegation loop collapse — liquid democracy concentrates power and loses votes

> **State:** sim-ready
> **Class:** FLEET-domain (round-24 opener) · multi-agent governance — liquid-democracy random mapping (Flajolet–Odlyzko 1990) · PROPOSAL 105
> **Target:** sim-lab (VERDICT 118, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@6648ae1 · fetched 2026-07-18T00:29:25Z
> **Source basis:** P. Flajolet & A. M. Odlyzko, "Random Mapping Statistics," EUROCRYPT '89 / Lecture Notes in Computer Science 434 (1990) 329–354 — cyclic-node count ~√(πN/2), giant-component fraction ~0.7582N (standard random-mapping theory; no external repo fetched).
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/delegation_loop_collapse.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 c3e5e6c1…d49ea6 (see Verify below).

## Domain
FLEET — multi-agent governance / coordination economics. Distinct from prior fleet slots (winner's-curse auction P101, Braess routing P092): transitive proxy voting ("liquid democracy") modelled as a random mapping.

## The mechanism
N agents, each delegates its vote to one uniformly-random peer (delegating to self = voting directly). Follow the delegation chains: every chain ends in a cycle; the cyclic agents are the effective deciders, and each weakly-connected component is one voting bloc whose weight = the agents funneling into it.

## The trap (counterintuitive)
Uniform random delegation "feels" egalitarian — no agent is favored, so influence should stay spread out. It does not. The delegation graph is a **random mapping**, and its classical statistics (Flajolet & Odlyzko, 1990) bite:

- **Electorate collapse.** Only cyclic nodes decide; their count is ~√(πN/2) = O(√N). For N=4096 that is ~80 agents — under 2% — deciding for all.
- **Power concentration.** One accidental component (the giant) holds a Θ(N) share of all voting weight (asymptotic constant ≈ 0.758).
- **Hidden oligarchy.** The clique that controls that bloc — the cycle at its core — is only O(√N) agents, under 5% of the population.

One-hop, individually-rational, uniformly-random delegation silently hands ≥30% of all voting weight to a sub-5% clique while shrinking the real electorate below 10%. No preferential attachment, no coordination, no malice — pure graph structure.

## Gates (each ≥3σ from threshold; SEED=20260717, N=4096, 400 trials)
| gate | statistic | claim |
|---|---|---|
| G1 electorate collapse | mean(cyclic/N) | ≤ 0.10 |
| G2 power concentration | mean(largest bloc/N) | ≥ 0.30 |
| G3 controlling clique | mean(core cycle/N) | ≤ 0.05 |

## Verify
```
python3 ideas/fleet/delegation_loop_collapse.py   # exit 0; prints canonical results + sha256
```
Deterministic: pinned seed, canonical `json.dumps(sort_keys, separators)` → sha256 reproduces byte-for-byte on a double run. Expected results-dict sha256 disclosed in the outbox block after the dry run.

## Fleet relevance
Any fleet mechanism that lets agents route decisions/tasks/trust to "whoever seems best" one hop away inherits this collapse: escalation chains, trust delegation, proxy approvals. Mitigation for sim-lab to explore: cap chain depth or forbid cycles (bounded delegation) and measure electorate/concentration recovery.

## Model basis (declared model-dependence — the P024 discipline)
The collapse depends on structural assumptions: (a) one uniformly-random out-edge per agent (self allowed) with no preferential attachment, so the delegation graph is exactly a uniform random mapping f:[N]→[N]; (b) one-hop delegation resolved transitively by chain-following (each chain terminates in a cycle); (c) N large enough for the random-mapping asymptotics to govern (finite-N corrections are O(1/√N) in the means and vanish in the gates via the standard-error margin). Under bounded delegation (capped chain depth or forbidden cycles), skewed target-choice (preferential attachment), or multi-hop weighted schemes the quantitative constants shift — but the qualitative collapse (O(√N) deciders, one Θ(N) bloc, O(√N) controlling clique) is robust for any uniform one-hop random-mapping delegation. The claim is scoped: under uniform one-hop random delegation on N=4096 agents, the effective electorate, largest voting bloc, and controlling core cycle land at the pinned constants, mechanism-explained, not asserted as a universal law.

## Dedup
Distinct from prior fleet slots: winner's-curse task auction (P101, auction/valuation economics) and Braess selfish-routing (P092, congestion/equilibrium). This is a random-mapping governance mechanism — transitive proxy voting, not pricing or routing. No prior idea models liquid democracy as a functional graph.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A random-mapping claim: N=4096 agents each delegate to one uniformly-random peer (self = voting directly), so the delegation graph is a uniform random mapping. Only cyclic nodes decide, and their count is ~√(πN/2)=O(√N) (electorate collapse); one weakly-connected bloc captures a Θ(N) share of all voting weight (~0.758N); and the core cycle controlling that bloc is only O(√N) agents (hidden oligarchy). Uniform one-hop delegation concentrates ≥30% of the vote into a sub-5% clique while shrinking the electorate below 10%.
**2. What would make it false?** If a simulation showed the cyclic-node fraction staying near 1 (the electorate does NOT collapse), or the largest bloc holding only a vanishing share of weight (no concentration), or the controlling core cycle being Θ(N) rather than O(√N). Any of G1/G2/G3 failing at its threshold → REJECT.
**3. Simplest version that still bites?** SEED=20260717, N=4096, 400 independent trials; each trial draws a uniform functional graph f:[N]→[N]; one O(N) pass extracts the cyclic nodes (G1), the largest weakly-connected bloc (G2), and that bloc's core cycle length (G3); compare the trial means to 0.10 / 0.30 / 0.05.
**4. What is the counterintuitive core?** Uniform random delegation "feels" egalitarian — no agent is favored — so intuition expects ~N independent deciders and no concentration. But a random mapping's cyclic core is only O(√N) (~2% here) and one accidental giant component swallows ~75% of all voting weight, controlled by a sub-5% clique. No preferential attachment, no coordination, no malice — the concentration is pure graph structure.
**5. Where could I be fooling myself?** Finite-N: the asymptotic constants (√(πN/2)/N=0.0196, giant fraction 0.7582) are large-N limits; at N=4096 the measured means (0.0197, 0.748) already match them. The largest-bloc distribution is heavy-tailed with high per-trial variance, so the gate correctly tests the ESTIMATED MEAN via its standard error (se=std/√400), not the per-trial spread — the 45.8σ G2 margin is on the mean estimate, the honest quantity.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 mean_cyclic_frac=0.01967 (se 0.000495) z=162.43σ (≤0.10); G2 mean_largest_bloc_frac=0.748063 (se 0.009785) z=45.79σ (≥0.30); G3 mean_core_cycle_frac=0.010834 (se 0.000419) z=93.49σ (≤0.05) — all clear the ≥3σ bar; exit 0; results-dict sha256 c3e5e6c1…d49ea6.
**7. What decision does it change?** Any fleet mechanism that routes decisions/tasks/trust one hop to "whoever seems best" — escalation chains, proxy approvals, trust delegation — inherits this collapse. Do not assume uniform one-hop delegation spreads influence; cap chain depth or forbid cycles (bounded delegation) and measure electorate/concentration recovery before trusting a delegated-authority design.
**8. How will we know it worked?** The committed stdlib verifier reproduces mean_cyclic/N ≤0.10, mean_largest_bloc/N ≥0.30, and mean_core_cycle/N ≤0.05, each ≥3σ on the standard-error margin, with the results-dict sha256 matching c3e5e6c15bee39165e3ccfb3967135c06df2ccfd60af7d727b918cda47d49ea6.

**Recommendation: sim-ready**
