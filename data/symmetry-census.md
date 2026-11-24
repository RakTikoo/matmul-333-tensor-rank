# The symmetry census over F3: three survivors, the kills, and two groups that cannot act

**Date:** 2026-11-24. A census of candidate group actions
for equivariant rank-22 ansätze over F3: conjugation-isotropy
actions in GL(3,3), the index-translation family, and the
previously covered leg-permuting S3. Every candidate passed
through two exact filters — **F1**, a parameter count
(effective unknowns vs independent equations, per orbit
partition of 22), and **F2**, reachability (T must lie in the
span of the group's orbit sums; this is the norm-gap test of
`data/symmetric-ansatze.md`). The census pipeline was
validated by reproducing the earlier waves' numbers exactly
(the Γ39 kill, the involution count 365, the C13 counts).
Survivors are specifications for solver systems, not
existence results.

## The claim, at its approved wording

"We censused the group actions that could organise a rank-22 decomposition over F3, passing each through two exact filters — a parameter count (unknowns vs independent equations, per orbit partition of 22) and a reachability test (the tensor must lie in the span of the group's orbit sums; this is the test that kills ansätze whose group order is divisible by 3). Of the conjugation-type actions in GL(3,3) and the translation family, exactly three survive both filters, and we publish their specifications: the octahedral group S4 acting by conjugation (31 independent equations; best partition short by 3 effective unknowns, and by 2.26 in the discrete count — the closest-to-balanced symmetric ansatz we have measured); a translation action of C3×C3 (type P1) whose best partition has 9 *more* effective unknowns than equations, the only positive-margin symmetric instance we have found; and a second translation type (P2) short by 1. Two candidate groups cannot act at all: exhaustive search over all 11,232 elements of GL(3,3) shows no element inverts the Singer cycle (so the dihedral group D13 is not realisable over F3), and no element satisfies the dicyclic relations (Q12 likewise). Two further candidates (A4; permutation S3×C2) survive only under a raw parameter count and are excluded under the effective count, which we argue is the correct convention for their action type; both counts are in our record. The census does not cover mixed conjugation × leg-permutation actions beyond the previously studied S3, and a survivor is a specification for a solver system, not evidence that a scheme exists — the S4 and translation systems are being built; the S3 and C13 systems (Items 13 and the Wave 60 design) are already in flight. Symmetric-exclusion results for other groups over ℂ are in the literature (Burichenko)."

## Census table (summary; both counts and full partition data are in the campaign record)

| action | order | indep. equations | verdict |
|---|---|---|---|
| Coordinate S3 (leg-permuting) | 6 | 138 | covered — solver run in flight |
| Singer C13 | 13 | 93 | covered — solver run in flight (see `data/symmetric-ansatze.md`, Item 27) |
| Singer C26; C13×C2 | 26 | 93 | collapse to the C13 row (centre acts trivially) |
| Singer C2 ⟨−I⟩ | 2 | 729 | killed — degenerate (action trivial) |
| Γ39 = C13 ⋊ Frobenius | 39 | 31 | killed by F2 (norm gap; orbit sums span 17 of 31) |
| **Octahedral S4 (conjugation)** | 24 | 31 | **SURVIVOR** — 76/103 partitions pass both filters; best −3 effective; discrete shortfall 2.26 |
| **Translation C3×C3, type P1** {(a,b,0)} | 9 | 81 | **SURVIVOR** — best +9 effective (only positive margin found); discrete shortfall 5.46 |
| **Translation C3×C3, type P2** {(a,−a,c)} | 9 | 81 | **SURVIVOR** — best −1 effective; discrete shortfall 6.51 |
| Translation C3×C3, types P3/P4 | 9 | 81 | killed by F1 (best margin −23) |
| Translation C3³ (full) | 27 | 27 | killed by F2 (all 13,689 partitions pass F1; every orbit-sum span ≤ 9-dimensional per species, T in none) |
| A4 (tetrahedral) | 12 | 61 | killed by F1 under the effective count (−11; raw count +5 — both counts recorded; see below) |
| Permutation S3×C2 | 12 | 122 | killed by F1 under the effective count (−27; raw +7) |
| C3 conjugation, class J3(1) | 3 | 243 | killed by F1 (−61) |
| C3 conjugation, class J2(1)⊕[1] | 3 | 275 | killed by F2 (orbit-sum spans 125/211 exclude T — a pure order-3 norm gap) |
| Klein V4 | 4 | — | killed in earlier waves (the encoded shape cannot express the control) |
| Involution pairing | 2 | 365 | killed by F1 (see `data/symmetric-ansatze.md`, Item 26) |
| **D13 (dihedral)** | 26 | — | **not realisable over F3** — exhaustive over all 11,232 elements of GL(3,3): the Singer normaliser (order 78) achieves conjugation powers exactly {1, 3, 9}; zero elements invert the Singer cycle; all 144 C13 subgroups are conjugate |
| **Q12 (dicyclic)** | 12 | — | **not realisable over F3** — for all 2,600 order-6 elements r, the Sylvester space {s : s r = r⁻¹ s} contains no invertible s with s² = r³ generating order 12 |

**The counting-convention note (part of the claim).** For
actions that do not permute the legs, the fixed locus of a
term is a cone under the scaling torus, so the *effective*
count (raw − 2 per orbit) is the geometrically correct one;
A4 and permutation S3×C2 pass F1 only under the raw count
and are excluded under the effective count. Both counts are
preserved in the campaign record so the judgement call stays
auditable. For leg-permuting actions (the S3 row), stabilisers
rigidify the scaling and the raw count is the correct one.

**Completeness caveat (part of the claim).** The census
covers conjugation-isotropy actions, the translation family,
and the leg-permuting S3. Mixed conjugation × leg-permutation
actions beyond that S3 are not covered, and unnamed solvable
subgroups of GL(3,3) were not separately censused (the
SL(2,3) and GL(2,3) images factor through the A4 and S4 rows).
