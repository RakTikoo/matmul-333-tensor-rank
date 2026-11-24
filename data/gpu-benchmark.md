# GPU evaluator benchmark: 172.9M steps/s, exact-agreement gated

**Date:** 2026-11-24. A benchmark of the campaign's own F3
annealing evaluator (the instrument behind the wrong=5 state
of `data/wrong5-case-study.md`) on named hardware against two
named CPU baselines. The GPU proposes states; every exact
judgement in this repository was made on CPU by the exact
layer (`verify.py` / `checkp.py`).

## The claim, at its approved wording

"Our F3 annealing evaluator, ported to an RTX 4070 laptop GPU (CuPy), sustains 172.9 million steps per second on the rank-22-over-F3 annealing workload — about 25× the same machine's compiled CPU annealer and about 1,800× this project's VM CPU baseline. Before any campaign run, the GPU evaluator's wrong-counts were checked against the exact home evaluator on a 16-state battery (16/16 agreement, the home evaluator itself cross-checked against the exact mod-3 judge), and full- assembly recount audits ran clean over ~65 billion cumulative steps. All exact verification remained on CPU throughout: the GPU proposes states; only the exact layer judges them."

## Numbers

| evaluator | hardware | throughput |
|---|---|---|
| GPU (CuPy) | RTX 4070 Laptop GPU | 172.9M steps/s (32.30B steps / 186.8 s) |
| CPU annealer (gcc -O2) | same laptop | 6.90M steps/s |
| CPU baseline | this project's VM | ~96k steps/s |

Ratios: ≈25.1× against the same machine's CPU annealer;
≈1,800× against the VM baseline. Both clear the
pre-registered ≥10× porting rule. Agreement controls: the
GPU evaluator's wrong-counts matched the exact home
evaluator on a 16-state battery, 16/16 (the home evaluator
itself cross-checked against `checkp.py`); full-assembly
recount audits ran clean over ~65 billion cumulative steps;
deliberately left on CPU: all SMT solving and all
verification.
