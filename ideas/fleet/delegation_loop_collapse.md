# Delegation loop collapse — liquid democracy concentrates power and loses votes

> **Status:** `sim-ready` · PROPOSAL 105 · round-24 fleet slot · verifier: `delegation_loop_collapse.py`

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
