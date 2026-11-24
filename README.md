# The 3×3 matrix multiplication tensor: verified findings around rank 23

Computational findings on the rank of the ⟨3,3,3⟩ matrix multiplication
tensor, obtained by an exact-methods campaign in November 2026. The rank
over ℚ is known to satisfy 19 ≤ R ≤ 23 (Bläser 2003; Laderman 1976).
**This repository claims no new decomposition and no rank-22 scheme.**
What it contains is a set of exact, machine-checkable measurements and
exclusions around the two best-known rank-23 schemes — Laderman's
(arXiv-era catalogue: Sedoglavic's FMM collection) and Perminov's cn122
(arXiv:2512.21980) — each shipped with the certificates and code needed
to re-verify it independently. Version 1.1.0 adds measurements at a
third rank-23 scheme (Perminov's cr58_cn122) and at ranks 24 and 26, a
census of the banked schemes' unit terms, a bounded cross-family
transplant census, and an exact audit of two claims in a January 2026
report (findings 6–10 below). Version 1.2.0 adds an extension of
the unit-term census to every other verified scheme on the campaign
disk — where the universal form of the census finding does not
extend, with a single rank-24 counterexample — and a cluster
anatomy of the three rank-23 schemes under one fixed greedy
procedure (findings 11–12 below).
Version 1.3.0 adds a census of the complete
Heule–Kauers–Seidl repository of rank-23 schemes — every unit
term in all 17,376 schemes is naive, closing the gap left open
in finding 11 — a cautionary anatomy of the campaign's homotopy
walks, the bank-wide closure of the transplant census at all
cardinalities ≤ 4, and a single-drop delta table across ranks
23–26 (findings 13–16 below).
Version 1.4.0 adds the decided repair fronts and the partial
fronts around them, the exact ruler geometry at Perminov's
scheme and the one grip-gain scheme on its lines, a calibrated
3-adic lifting bridge from F3 to ℚ, a one-signedness census of
11,777 near-miss states, two exact exclusions of symmetric
ansätze and a feasibility verdict on a third, the border-rank
line's negative anatomy, a case study closing the
neighbourhood of the closest F3 near-miss our searches have
produced, a census of the symmetry groups that could organise
a rank-22 scheme over F3, a validated substitution-method
instrument, a learned pattern in support shapes, and a GPU
evaluator benchmark (findings 17–36 below). It also records a
literature development due to others: over F2 the rank is now
determined to be exactly 23 (see "What this is not"), so the
open fields for rank 22 are ℚ and F3.

## Headline result: exact Jacobian kernel dimensions at the two schemes

For the Brent system of a rank-23 decomposition (729 equations, 621
factor entries), we computed the Jacobian kernel **exactly over ℚ** at
both schemes, by two independent implementations that agree:

| point | dim ker J | trivial tangents | excess |
|---|---|---|---|
| Laderman (1976) | 76 | 70 | **6** |
| Perminov cn122 (2025) | 94 | 70 | **24** |

The trivial tangents at any exact decomposition are the 46-dimensional
rescaling torus plus the 26-dimensional tangent space of the isotropy
orbit (27 Lie parameters, 1-dimensional action kernel), overlapping in
2 dimensions: 46 + 26 − 2 = 70. The excess — the kernel dimension
beyond all trivial tangents — is **6 at Laderman and 24 at Perminov**.

Consequences, stated at exactly the strength proved:

- Perminov's excess of 24 is consistent with Perminov lying on the
  ≥17-dimensional family of rank-23 schemes whose existence
  Heule–Kauers–Seidl established (ISSAC 2019 / JSC 2021).
- Laderman's excess of 6 is below 17, so Laderman does not lie on a
  smooth 17-dimensional part of that family: the variety is stratified
  and local dimension is point-dependent.
- This reconciles the published ≥17 with the nullity of exactly
  2r = 46 measured at generic numerical rank-23 points (see
  `claims.md`, Item 3): those points decompose a perturbed tensor,
  whose stabiliser is trivial.

Certificates: `certificates/kernel_laderman.npz` and
`certificates/kernel_perminov.npz` contain exact rational kernel bases;
every vector satisfies J·v = 0 over ℤ, checkable in minutes.
Two independent computations: `code/moduli_exact.py` (mod-p rank +
CRT/rational reconstruction) and `code/rigor_check.py` (a from-scratch
adversarial re-implementation: fresh primes, exact integer matvecs,
independent construction of the trivial tangent spaces, Bareiss exact
ranks). Their agreement is the result's evidence.

## Other findings (precise wordings and scopes in `claims.md`)

1. **A covering-parity case split** for deciding term-repair instances:
   an exhaustive split derived from a wrong=1 state's single wrong
   entry, indexed by which freed terms cover that entry and the sign
   pattern of their products there. It decided in minutes instances
   that resisted hours of unsplit SMT solving. Term-freeing itself
   follows Heule–Kauers–Seidl's streamlining; the split and its use as
   an unsatisfiability proof we have not found in the literature
   searched (audit in `data/novelty-audit.md`).
2. **Five completely decided repair instances** (16/16 exhaustive
   cases UNSAT each, coefficients in {0,±1}, stated terms freed, rest
   frozen) on wrong=1 states of Laderman and Perminov.
3. **A census of Perminov's {0,±1} flip component**: 34,604 states,
   every term pair tested at every state (25.4M tests), no collapsible
   pair; and ~133M triple tests through a rank-≤2 flattening filter
   across ~75k visited rank-23 states, no 3-to-2 collapse. (Laderman's
   flip-graph isolation is published by Kauers–Moosbauer,
   arXiv:2212.01175; we confirm it independently and claim nothing for
   it.)
4. **Pair-merge exclusions over all of ℚ**: the standard merge test
   applied exactly shows no pair of terms merges in Laderman (λ=1,
   hence λ=2) or in Perminov cn122 — 759 pairs. For cn122 we have not
   found this stated elsewhere.
5. **A completely decided quarters exclusion**: for Laderman's
   wrong=1 state with terms {2,3,4} freed over quarter-integers
   {0, ±1, ±1/2, ±1/4, ±3/4}, all 174 exhaustive cases are decided,
   all UNSAT (33 of 33 sign patterns complete), as of 2026-11-22.
   The instance is **fully decided** — no quarters completion of
   the freed triple exists. Full record in
   `data/quarters-status-2026-11-22.md`.
6. **A census of unit terms (wrong-entry cartography)**: in the
   rank-23 schemes we hold (the Laderman λ-family, Perminov's
   cn122, and the T11/T12 family), every unit term is a naive term
   e_(i,j)⊗e_(j,k)⊗e_(i,k) — 41 of 41 by direct census.
   Equivalently, all 46 banked rank-22 states that differ from a
   scheme by one dropped term and exactly one wrong entry have
   that entry on the 27-position support of the tensor,
   concentrated in 8 orbits of the entry-symmetry group covering
   21 of 729 positions; the concentration was pre-registered and
   held on a held-out family (5 of 5). We have not found this
   census in the literature searched (audit in
   `data/novelty-audit-2.md`); it is anatomy of the known schemes,
   not evidence about rank 22. Full record in
   `data/cartography.md`.
7. **A third measured rank-23 point**: Perminov's cr58_cn122 — a
   third-party scheme from his public database, reprinted by
   Karunaratne–Idamekorala and by the boulder-swarm project, not
   a campaign discovery — is not equivalent to Laderman's scheme
   or to cn122 (the per-slot factor-rank multisets, invariants
   of the isotropy action, differ from both). Its Jacobian kernel
   is 94, exceeding the trivial tangents (70) by 24 — the same
   excess as at cn122, in a different orbit — and no pair of its
   terms merges over ℚ (0 of 253 pairs). Full record in
   `data/t11-basin.md`; the scheme is in `certificates/`.
8. **Kernel dimensions at ranks 24 and 26 (the ladder)**: at two
   genuine rank-24 literature schemes the kernel dimensions are
   102 and 111 (excesses 30 and 39 over the measured trivial
   span 72); at our own rank-26 block construction the kernel is
   187, exceeding the trivial tangents — 73 at this point, not
   the generic 78 — by 114. Together with the rank-23 values
   these show no monotone behaviour in the rank: within-rank
   spread is as large as any between-rank difference, so they
   constrain nothing about rank 22. Full record in
   `data/ladder.md`.
9. **A bounded cross-family transplant census**: among the eight
   banked rank-23 schemes, the three families share almost no
   raw material — the single term shared across families is one
   naive unit term (at (1,0,1)) — and no pair of terms from one
   family sums to a pair from another (1,974 distinct pair sums,
   no genuine cross-family collision). In this bounded sense
   (eight schemes, transplants of depth at most 2, over ℚ) the
   families cannot be hybridised by swapping one or two terms.
   Full record in `data/transplants.md`.
10. **An exact audit of a January 2026 report**: Blankline
    Research's report (Zenodo 18443297) makes two checkable
    claims. The first (a routing inconsistency) is correct in
    its stated single-term scope. The second (a "1+2+19"
    structure with minimum residual √6, identical for all 2^16
    sign patterns) does not hold for the part that can be
    reconstructed from the publication: two independent exact
    computations give a minimum residual² of 7, not 6, and the
    residual is not sign-invariant; the full claim cannot be
    decided from the publication. Neither result moves any bound
    on the rank of ⟨3,3,3⟩. Full record in
    `data/blankline-audit.md`.
11. **A census extension, and where the census finding stops**:
    extending the unit-term census of finding 6 to every other
    verified ⟨3,3,3⟩ scheme on the campaign disk (48 further
    files, 40 distinct schemes, each re-verified exactly over ℚ)
    gives 50 unit terms, of which 49 are naive — and one is not.
    The exception is term 0 of the rank-24 scheme obtained by
    downward projection of a ⟨3,3,4⟩ scheme (solven-eu catalogue):
    its factors are e₅, −e₈, e₄, so its single entry sits at
    position (5,8,4), where the matrix-multiplication tensor is
    zero. The universal statement therefore does not extend
    beyond the original bank; what survives is narrower — every
    unit term in every rank-23 scheme in the extended census is
    naive, and the published 41-of-41 statement about the
    original 11 bank schemes is untouched. Two independent exact
    computations agree on every count. The
    Heule–Kauers–Seidl database of 17,000+ schemes was not
    censused. Full record in `data/census-extension.md`.
12. **A cluster anatomy under one fixed greedy procedure**: with
    the core taken as a scheme's unit terms and the remaining
    terms merged agglomeratively into clusters of at most 3 so
    as to minimise the total number of off-support positions at
    which cluster sums are nonzero ("garbage") — a greedy
    procedure, not an optimal one — total garbage falls from the
    all-singletons baselines 184 to 72 at Laderman, 422 to 136
    at Perminov's cn122, and 390 to 148 at Perminov's
    cr58_cn122. In the Laderman and cn122 partitions the
    clusters' on-support parts together with the core cover the
    tensor's 27 support positions with no overlap at all; in
    cr58_cn122 there are exactly 2 on-support overlaps. Two
    independent implementations agree on every total and on the
    partitions themselves. These are measurements under this
    procedure, not invariants of the schemes; whether the shared
    qualitative anatomy is generic for sparse exact schemes is a
    hypothesis, untested. Full record in
    `data/cluster-anatomy.md`.

13. **The unit-term census at database scale**: censusing the
    complete Heule–Kauers–Seidl repository of ⟨3,3,3⟩ rank-23
    schemes as distributed (17,376 schemes, all with entries in
    {−1, 0, 1}) gives 1,882 unit terms — and every one of them
    is naive, its entry on the tensor's 27-position support; no
    off-support unit term exists in this population. Three
    independent computations agree on every count, one of them
    verifying all 17,376 schemes exactly. This closes the gap
    stated in finding 11, for this population: within rank 23,
    every unit term in every scheme population we have censused
    is naive. The statement is about these named populations,
    not a theorem about all rank-23 schemes over ℚ, and it is
    not evidence about rank 22. Full record in
    `data/hks-census.md`.
14. **A cautionary anatomy of the homotopy walks**: walks along
    the rank-23 fibre tripped a "terms merging" monitor
    (pairwise term cosine above 0.99) in four of five
    directions — but the monitor recorded the cosine's absolute
    value, and the signed cosines are ≈ −0.99: the pairs were
    approaching cancellation, not fusion, while their sums
    stayed bounded, their rank-1 defect stayed flat or grew,
    and their term norms inflated by an order of magnitude or
    more. Fused 22-term reconstructions were rejected by exact
    verification on all 729 entries. A structural by-product:
    each of the three tripping Perminov pairs shares a factor
    column identically in the seed (a complete scan finds seven
    such pairs in cn122 in total; Laderman's scheme has none).
    The |cos| trip criterion is retired. Nothing in this
    episode bears on whether rank-22 schemes exist. Full record
    in `data/walk-anatomy.md`.
15. **The transplant census closed at all cardinalities ≤ 4,
    bank-wide**: extending finding 9's census to unequal
    cardinalities across the enlarged bank — all subset sums of
    sizes 1–4 over the 60 distinct verified schemes (679,539
    sums, exact), compared between adjacent cardinalities
    within and across schemes — the only exact equalities
    anywhere are the 277 hits between our constructed rank-25
    split and its rank-24 parent, the split's own undoing. No
    genuine cross-scheme swap exists at any cardinality ≤ 4 in
    this pool; depth-5 comparisons were not run. Full record in
    `data/transplants.md`.
16. **A single-drop delta table across ranks 23–26**: for six
    verified schemes spanning ranks 23–26, the full single-drop
    battery shows a wrong=1 neighbour in exactly the schemes
    that have a unit term (Laderman 5, cn122 3, proj-24 1,
    lensC-26 19) and in none that do not (metaflip-24 and the
    rank-25 split, closest drops 2 wrong) — the near-miss
    structure does not soften gradually down the ranks. Every
    wrong=1 state in the table is the standard flavour (have 0 /
    want 1 on the support) except one: proj-24's unique unit
    term sits off-support, so its drop state has an extra entry
    to cancel (have +1 / want 0). Full record in
    `data/delta-table.md`.
17. **The repair front is decided at its registered scope**:
    for seven banked near-miss states (six 22-term wrong=2
    states from rank-23 parents, and the off-support wrong=1
    state from proj-24), every covering-parity case of the
    free-4 repair move (four terms freed, coefficients in
    {0,±1}, the rest frozen, over ℚ) was enumerated — 1,843
    cases, all UNSAT, controls passed and re-verified at home.
    No rank-22 scheme is reachable by this move from any of
    these states. Full record in `data/repairs-closure.md`.
18. **The new-basins free-4 front is fully decided**: the 21
    wrong=1 states obtained from nine orbit-distinct catalogue
    schemes generated 336 free-4 {0,±1} repair cases over ℚ;
    all 336 are UNSAT (21/21 instances decided). Full record
    in `data/repairs-closure.md`.
19. **The walk line is closed**: the gauge-fixed re-walk built
    after finding 14's anatomy ran in all five registered
    directions and stalled in every one, under its
    pre-registered rule. Full record in
    `data/walk-anatomy.md`.
20. **The hinge free-4 front, partial**: of the 3,072 repair
    cases derived from the 192 hinge wrong=1 states of the
    Wave 48 construction, 631 have been decided, all UNSAT
    (39 of 192 instances fully, one partially); 2,441 cases
    are not yet attempted and no front-level conclusion is
    drawn. Full record in `data/partial-fronts.md`.
21. **The proj24-family free-4 front, partial**: of the 1,140
    repair cases derived from the 60 drop states of the shear
    families on the exact rank-24 parents proj24 and
    metaflip24, 943 have been decided, all UNSAT; 197 are not
    yet attempted. A repair here would assemble an exact
    rank-23 scheme, not a rank-22 one — the front tests ladder
    connectivity. Full record in `data/partial-fronts.md`.
22. **The shear-family free-4 front, partial, with a lost
    run**: of the 14,016 cases derived from the 876 wrong=1
    states of the Wave 56 shear families, 414 have been
    decided, all UNSAT, in the kernel covering the Kauers,
    cn97 and c88 parents. The companion kernel's run (the
    cn119 and cn120 instances, 8,256 cases) was lost when its
    interactive session ended before harvest; its partial
    verdicts are unrecoverable and are counted nowhere. A
    committed re-run is queued. Full record in
    `data/partial-fronts.md`.
23. **Rulers at cn122 — no rank drop on the lines or the flat
    planes**: at Perminov's cn122 (Jacobian nullity 94), the
    exact straight lines in the rank-23 variety through the
    point number exactly 21 within the searched scope; 114 of
    the 153 two-planes spanned by pairs of the flat basis
    rulers are themselves entirely flat; no term vanishes and
    no two terms merge anywhere on the 21 lines or in any of
    the 134 flat planes (for all 596 tested plane/pair
    combinations the merge ideal is the unit ideal — no merge
    even over ℂ). Random directions are never rulers (0 of
    3,000 at each parent). Full record in
    `data/rulers-and-gg611.md`.
24. **gg611, the unique grip-gain scheme**: exactly one point
    on the 21 ruler lines strictly increases the
    identical-factor pair count — the t = 1 point of one shear
    line, with 8 pairs. The scheme is banked, verified exactly
    (rank 23 over ℚ), and shipped as `data/gg611_r23_Q.json`;
    its shear family gives 96 exact variants and 150 new
    wrong=1 states, from which 2,400 free-4 cases are staged.
    Full record in `data/rulers-and-gg611.md`.
25. **A calibrated Hensel bridge from F3 to ℚ**: 3-adic
    lifting of finite-field decompositions is published prior
    art (Khoruzhii–Gelß–Pokutta, ISSAC 2026); our
    implementation of the bridge is calibrated — cn122 and
    Laderman, reduced mod 3, lift to Z/3⁴² and reconstruct
    entry-identically, verifying over ℚ — and it converts
    genuinely new finite-field points: a solver-found
    F3-native rank-7 decomposition of ⟨2,2,2⟩ lifts to a
    verified rank-7 scheme over ℚ not entry-identical to
    Strassen's. Any future non-singular F3 rank-22 point
    would lift the same way; the bridge finds nothing by
    itself. Full record in `data/hensel-bridge.md`.
26. **One-signedness, without exception in the pools
    censused**: across all 11,777 on-support wrong=1 states
    the campaign has banked (1,282 of the 22-term class,
    10,495 of the 25-term class), the residual is a single
    missing support entry (+E_e) in 11,777 of 11,777 cases;
    and unit terms across the bank and the complete
    Heule–Kauers–Seidl population number 2,010 positive
    against exactly 1 negative — the off-support proj-24 term,
    whose drop state is the campaign's only −E_e state. A
    census of named pools, not a theorem; its force is that
    opposite-sign state surgery is starved by it. Full record
    in `data/one-signedness.md`.
27. **The Γ39 Singer ansatz over F3 is excluded exactly**:
    for the order-39 group generated by a Singer cycle and
    Frobenius, every sum of whole orbits of rank-1 tensors
    lands in a fixed 17-dimensional subspace of the
    31-dimensional fixed space, and the multiplication tensor
    is not in it — no Γ39-equivariant rank-22 decomposition
    over F3 exists, for any orbit partition. The obstruction
    is a modular norm gap (3 divides the group order);
    parameter counting alone would not have excluded the
    ansatz. Full record in `data/symmetric-ansatze.md`.
28. **Involution pairing is excluded by counting**: an
    involution leaves 365 independent equations on the
    729-entry tensor space, while every pairing pattern of 22
    terms supplies at most 286 effective unknowns — short by
    at least 79 in all cases, over ℚ and F3 alike. Full
    record in `data/symmetric-ansatze.md`.
29. **The C13-only Singer ansatz survives its paper tests**:
    its fixed terms are exactly triples of GF(27) elements;
    the system has 88 effective unknowns against 93 equations
    — the nearest-to-square full rank-22 ansatz we have
    measured — and, unlike the Γ39 case, there is no norm
    gap. A discrete count of its image falls short (log₃
    80.46 against 93), so a solution would require the tensor
    to be special beyond linear reachability. A solver run on
    the system is in flight and undecided; nothing here is
    evidence that a C13-equivariant scheme exists. Full
    record in `data/symmetric-ansatze.md`.
30. **The lensC pipeline**: our own rank-26 scheme lensC
    carries 51 identical-factor pairs, the most in our bank;
    its 612 exact shear variants yield 10,495 distinct 25-term
    wrong=1 states and 10,495 derived free-4 instances
    (167,920 cases). A repair of one of these states would be
    an exact rank-25 scheme — the ladder's first rung — not a
    rank-22 candidate; a 1,792-case selection is kernelled
    and the family is staged, not decided. Full record in
    `data/lensc-pipeline.md`.
31. **The border line, in three scoped statements**: (1)
    requiring a 21-term Laurent family to satisfy the tensor
    identity to all orders is exactly R ≤ 21 (and the 22-term
    version exactly R ≤ 22) — the border-plus-one route is
    equivalent in difficulty to exact rank; (2) border rank
    21 is proved in the literature only through Schönhage's
    asymptotic sum inequality, and no explicit 21-term
    Laurent family for the single tensor appears in any
    source we could access; (3) our numerical border-ALS
    route failed its calibration on Bini's ⟨3,2,2⟩ family for
    a measured reason — the point it converges to is generic
    on a component with 106 genuine moduli, so its
    coordinates admit no low-degree algebraic description.
    The failure is genericity, not precision; the line is
    parked with three named revivals. Full record in
    `data/border-line.md`.
32. **The wrong=5 state over F3, and its closed
    neighbourhood**: the closest near-miss our searches have
    produced over F3 is a 22-term state with exactly 5 wrong
    entries of 729 (all five missing support entries). Its
    local neighbourhood is now closed exactly in three
    senses: over all coefficient assignments the minimum
    wrong count is 5; its own support template is
    unsatisfiable, the five defects being precisely the
    support entries no monomial of the template can reach
    (and the entry (1,3,0) stays unreachable under all cyclic
    widenings); and all 35 reachability-passing one-term swap
    systems are unsatisfiable. The state is shipped as
    `data/wrong5-state.json`. Full record in
    `data/wrong5-case-study.md`.
33. **A census of the symmetry groups over F3**: passing
    every candidate group action through a parameter count
    and the orbit-sum reachability test leaves exactly three
    survivors, whose specifications we publish — the
    octahedral group S4 acting by conjugation (31 equations;
    the closest-to-balanced symmetric ansatz we have
    measured), a translation action of C3×C3 with the only
    positive margin found (+9 effective unknowns), and a
    second translation type short by 1. Two candidate groups
    cannot act at all: exhaustive search over GL(3,3) shows
    D13 and Q12 are not realisable over F3. The census does
    not cover mixed conjugation × leg-permutation actions
    beyond the previously studied S3, and a survivor is a
    specification, not evidence a scheme exists. Full record
    in `data/symmetry-census.md`.
34. **A substitution-method instrument, validated**: our
    implementation of Wang's automated substitution method
    reproduces his 10 restriction orbits on ⟨2,2,2⟩,
    certifies rank ≥ 7 over F2 and F3, and completes
    negatively at target 8 — the sound answer. On ⟨3,3,3⟩ it
    certifies ≥ 14 over F2 and ≥ 12 over F3 — weaker than the
    published bounds (19 over any field, Bläser 2003; at
    least 21 over F2, Wang and Yang et al. 2026), published
    only as the instrument's measured reach, with its stall
    anatomy (a 3,389-orbit lattice against Wang's 496). Full
    record in `data/substitution-machine.md`.
35. **A learned near-partition pattern (a labelled
    speculative bet)**: on 7,255 support templates, a random
    forest separates the drop-one supports of banked exact
    rank-23 schemes from random shapes perfectly on a
    scheme-held-out split (AUC 1.0000, against a
    reachability-only baseline at 0.5320): near-exact shapes
    are sparse near-partitions of the target, with ~91% of
    support entries covered exactly once and almost no wasted
    coverage; symmetry features carry no signal. The pattern
    is necessary-looking, not sufficient — the model's ten
    best new proposals were exact-tested and all ten are
    provably empty. Its use is as a pre-filter for future
    template enumerations. Full record in
    `data/near-partition-pattern.md`.
36. **A GPU evaluator benchmark**: our F3 annealing
    evaluator, ported to an RTX 4070 laptop GPU, sustains
    172.9 million steps per second — about 25× the same
    machine's compiled CPU annealer and about 1,800× this
    project's VM CPU baseline — after exact-agreement gating
    against the home evaluator (16/16 states) and clean
    recount audits over ~65 billion steps. All exact
    verification remained on CPU throughout. Full record in
    `data/gpu-benchmark.md`.

## Verify it yourself

```bash
python3 code/verify.py check certificates/laderman_r23_Q.json      # VERIFIED, 0/729 over Q
python3 code/verify.py check certificates/perminov_cn122_r23_Q.json # VERIFIED, 0/729 over Q
python3 code/verify.py check certificates/perminov_cr58_cn122_r23_Q.json # VERIFIED, 0/729 over Q
python3 code/verify.py check data/gg611_r23_Q.json          # VERIFIED, 0/729 over Q (finding 24)
python3 code/checkp.py 3 data/wrong5-state.json             # wrong=5/729 over F3 — the near-miss of finding 32, not a scheme
python3 code/check_kernels.py  # pins dim ker J = 76 / 94 from both sides (needs numpy)
```

`code/check_kernels.py` is the packaged, self-contained
re-verification of the headline numbers. `code/moduli_exact.py`,
`code/moduli_float.py` and `code/rigor_check.py` are the original
campaign scripts, archived as run for provenance — they reference
the campaign's internal file layout and are not the packaged entry
point. `code/recount_cartography.py` and
`code/check_kernels_independent.py` are the Wave-28 claim gate's
independent second-path checkers for the v1.1.0 findings (a
from-scratch recount of the cartography census, and a from-scratch
Jacobian re-pinning of the newer kernel dimensions); they likewise
reference the campaign's internal file layout.
`code/recount_census_extension.py` and `code/clusters_greedy.py`
are the Wave-32 claim gate's independent second-path checkers for
the v1.2.0 findings (a from-scratch recount of the census
extension, and a from-scratch re-implementation of the greedy
cluster procedure); they likewise reference the campaign's
internal file layout.
`code/recount_hks_census.py` is the home recount behind
finding 13 — the second of the three independent computations
of the Heule–Kauers–Seidl population census (the Wave-47 claim
gate's product-route derivation is the third) — and likewise
references the campaign's internal file layout (it reads the
locally held copy of the distribution archive).
`code/checkp.py` is the exact mod-p judge (pure integer
arithmetic reduced mod p) behind the finite-field artefacts —
the wrong=5 state of finding 32 — packaged as run.

`verify.py` uses exact rational arithmetic (`fractions.Fraction`);
floats are rejected. All three scheme files are **literature
schemes**, included as the objects of study, not as campaign
results.

## What this is not

- No rank-22 (or lower) decomposition is claimed by this work.
  Over ℚ and over F3, whether rank 22 is achievable remains
  open. Over F2 it is now known not to be: the rank over F2 is
  exactly 23 — lower bounds of 20 (Wang 2026), 21 (Wang; Yang
  et al., 2026) and 22 (Rudich–Rousseau 2026), and the
  determination R_{F2}(⟨3,3,3⟩) = 23 by Tomar
  (arXiv:2610.11823), with Laderman's algorithm (whose
  coefficients are 0 and ±1, so it works over any ring)
  supplying the upper bound. All of the 2026 sources are
  preprints, the top links carrying machine-checked (Lean)
  certificates; the determination is others' work, not this
  repository's, and we re-verified only the upper bound
  in-house (our banked Laderman scheme passes the mod-2 judge
  at p = 2).
- Timeouts in the underlying campaign were recorded as "no
  conclusion", never as impossibility; every UNSAT above comes from a
  control-validated encoding (a known-good scheme with the same terms
  freed returns SAT and verifies).
- Novelty statements are of the form "not found in the sources
  searched", with the searches documented in `data/novelty-audit.md`
  and `data/novelty-audit-2.md` — they are not proofs of priority.

## Layout

- `claims.md` — every claim at its strongest honest wording, with its
  scope and the wording that would overclaim it.
- `code/` — the exact verifier, the mod-p judge (`checkp.py`), the
  case-split drivers, both kernel computations, the independent
  rigor check, and the Wave-28, Wave-32 and Wave-47 second-path
  checkers.
- `certificates/` — the three literature schemes, the exact kernel
  bases, and the rigor run log.
- `data/` — the novelty audits, the flip-component census, the
  triple-sweep and decided-instance reports, the quarters status,
  and the v1.1.0 records (cartography, the T11 point, the ladder,
  transplants, the Blankline audit), and the v1.2.0 records (the
  census extension and the cluster anatomy), and the v1.3.0
  records (the HKS population census, the walk anatomy, the
  transplant closure extension, and the delta table), and the
  v1.4.0 records (the repairs closure and new-basins front, the
  partial fronts, the walk-line closure extension, the rulers
  and gg611 with its scheme file, the Hensel bridge, the
  one-signedness censuses, the symmetric ansätze, the lensC
  pipeline, the border line, the wrong=5 case study with its
  state file, the symmetry census, the substitution machine,
  the near-partition pattern, and the GPU benchmark).

## License

MIT (code and text). The three scheme files are the work of
Laderman (1976) and Perminov (2025) and are redistributed for
verification.

## Author

RakTikoo — an independent computational campaign, November 2026.
