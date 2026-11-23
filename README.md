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

## Verify it yourself

```bash
python3 code/verify.py check certificates/laderman_r23_Q.json      # VERIFIED, 0/729 over Q
python3 code/verify.py check certificates/perminov_cn122_r23_Q.json # VERIFIED, 0/729 over Q
python3 code/verify.py check certificates/perminov_cr58_cn122_r23_Q.json # VERIFIED, 0/729 over Q
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

`verify.py` uses exact rational arithmetic (`fractions.Fraction`);
floats are rejected. All three scheme files are **literature
schemes**, included as the objects of study, not as campaign
results.

## What this is not

- No rank-22 (or lower) decomposition over any field is claimed.
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
- `code/` — the exact verifier, the case-split drivers, both kernel
  computations, the independent rigor check, and the Wave-28 and
  Wave-32 second-path checkers.
- `certificates/` — the three literature schemes, the exact kernel
  bases, and the rigor run log.
- `data/` — the novelty audits, the flip-component census, the
  triple-sweep and decided-instance reports, the quarters status,
  and the v1.1.0 records (cartography, the T11 point, the ladder,
  transplants, the Blankline audit), and the v1.2.0 records (the
  census extension and the cluster anatomy).

## License

MIT (code and text). The three scheme files are the work of
Laderman (1976) and Perminov (2025) and are redistributed for
verification.

## Author

RakTikoo — an independent computational campaign, November 2026.
