# Cluster anatomy — garbage measurements under one fixed greedy procedure

**Date:** 2026-11-23. **Objects (named):** the three rank-23
⟨3,3,3⟩ schemes Laderman (λ=1), Perminov's cn122, and Perminov's
cr58_cn122 ("T11"), all over ℚ. **Method (named in full):** core =
the scheme's unit terms; the non-unit terms are partitioned by
greedy agglomerative merging (clusters of size at most 3)
minimising total garbage, where the garbage of a cluster is the
number of off-support positions at which the cluster's term sum
is nonzero. The procedure is greedy, not optimal; the totals
below are outputs of this procedure — they are not invariants
of the schemes, not optimal partitions, and not comparable to
numbers produced by any other objective or method.

## The claim, at its approved wording

Under one fixed greedy procedure — core = the scheme's unit terms; the remaining terms merged agglomeratively into clusters of at most 3 so as to minimise the total number of off-support positions at which cluster sums are nonzero ('garbage'); the procedure is greedy, not optimal — the three rank-23 schemes measure as follows. Laderman: garbage falls from the all-singletons baseline 184 to 72, through four triples each carrying garbage 9 and six singletons each carrying garbage 6. Perminov's cn122: 422 to 136. Perminov's cr58_cn122 (T11): 390 to 148. In the Laderman and cn122 partitions, the clusters' on-support parts together with the core cover the tensor's 27 support positions with no overlap at all — every cancellation in those partitions is off-support; in T11 there are exactly 2 on-support overlaps. Two independent implementations of the procedure agree on every total and on the partitions themselves. These are measurements of the schemes under this procedure, not invariants: a different objective or an optimal partitioner could give different numbers. Whether the shared qualitative anatomy — a naive core, a few garbage-cancelling triples, a tail of near-clean singletons — is generic for sparse exact schemes is a hypothesis; no test of it has been run.

## Numbers

| scheme | core (unit terms) | non-unit terms | singletons baseline | greedy total |
|---|---|---|---|---|
| Laderman (λ=1) | 5 | 18 | 184 | **72** |
| Perminov cn122 | 3 | 20 | 422 | **136** |
| Perminov cr58_cn122 (T11) | 4 | 19 | 390 | **148** |

- Laderman's greedy history: 184 → 72 in 8 merges; the final
  partition is four triples (each garbage 9, support 13) and six
  singletons (each garbage 6, support 7). Laderman's file-order
  partition measures [20, 23, 20, 30, 16, 9], total 118, under
  the same garbage definition.
- cn122: 422 → 136 in 7 merges (triples at garbage 34 / 30 / 39,
  a pair at 4). T11: 390 → 148 in 6 merges (triples at garbage
  49 / 23 / 33).
- Support tiling: core plus clusters cover the 27 support
  positions with multiplicity 27 and **0 overlaps** for Laderman
  and cn122; multiplicity 29 and **exactly 2 overlaps** for T11.

## Method

- **Second path.** The Wave 32 gate re-implemented the procedure
  from the registered specification alone (`code/clusters_greedy.py`,
  written without opening the Wave 30 cluster code); the three
  schemes were first judged fresh VERIFIED 0/729 by `verify.py`.
  The re-implementation reproduced every baseline, every greedy
  total, every step of every greedy history, the Laderman
  file-order record, the exact final partitions, and all three
  support-tiling counts.
- **Specification note.** The registered specification leaves
  three points underdetermined (the tie-break's "resulting total
  cluster-support size", the referent of "lexicographic term
  indices", and the term-index convention for reporting); the
  gate's independent readings of all three reproduced the Wave 30
  partitions exactly after index conversion. That robustness is
  empirical — these three schemes, this reading — so the method
  is carried in full in the wording above, and any future scheme
  measured this way should have its tie-breaks pinned in advance.

## Scope

A measurement under one named algorithm on three named schemes.
The shared qualitative anatomy across the three schemes is
labelled a hypothesis in the approved wording; no test of it has
been run, and nothing here bears on rank 22.
