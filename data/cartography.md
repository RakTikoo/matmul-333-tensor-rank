# Wrong-entry cartography — unit terms in the banked schemes are naive

**Date:** 2026-11-22. **Population (named, finite):** the rank-23
⟨3,3,3⟩ schemes this campaign holds — the Laderman λ-family (six
parametrisations of one skeleton), Perminov's cn122, and the
T11/T12/famA/famB family (Perminov's cr58_cn122 and its images) —
and the minus-one-term states banked from them, plus five sampled
Perminov flip-walk drop states. All quantities over ℚ.

## The claim, at its approved wording

In the rank-23 ⟨3,3,3⟩ schemes we hold (the Laderman λ-family,
Perminov's cn122, and the T11/T12 family), every unit term — a
term with a single nonzero entry in each factor — is a naive term
e_(i,j)⊗e_(j,k)⊗e_(i,k): **41 of 41, by direct census**.
Equivalently, all **46** banked rank-22 states that differ from a
scheme by one dropped term and exactly one wrong entry have that
entry on the 27-position support of the tensor, concentrated in
**8 orbits** of the entry-symmetry group ⟨Φ, A↔B duality⟩
covering **21 of 729 positions**; the concentration was
pre-registered in Wave 26 and held on a held-out family
(**5 of 5**).

We have not found this census or the orbit concentration stated
in the literature we searched (see `data/novelty-audit-2.md`);
the nearest prior observation is Blankline Research's "four
anchors" in Laderman's scheme alone (2026, not peer-reviewed).
This is anatomy of the known schemes, not evidence about rank
22: a rank-22 scheme need not contain any unit term.

## Census numbers

- Population: 157 banked state files; 48 files with exactly one
  wrong entry; **46 unique states** after removing two
  byte-identical duplicate pairs (identified by hash: a Wave-4
  anneal file = Laderman-minus-2; a Wave-5 anneal file =
  cn122-minus-6).
- **46/46 wrong entries lie on the 27-position support of T**,
  all have=0/want=1. (Null expectation for a uniform position:
  27/729 ≈ 3.7%.)
- 13 distinct wrong positions, in **8 orbits** of the group
  G = ⟨Φ, A↔B duality⟩ (|G| = 6, 138 orbits on the 729
  positions), the 8 orbits totalling 21 positions.
- Unit-term census of the 11 parent schemes: 41 unit terms
  (λ-family 5 each, cn122 3, T11 4, T12 4, famA/famB 0) —
  **every one naive**. (Blankline's four Laderman "anchors" are
  the pairwise-disjoint subset of Laderman's five.)
- Wave 26's Monte Carlo significance values: chi-square
  p < 10⁻⁵ in all pre-registered variants; holdout binomial
  p ≈ 2×10⁻⁸.

## Method

- **Pre-registration.** Wave 26 registered the population, the
  group, the statistic and the family-level holdout split
  *before* extracting any wrong-entry position
  (`wave26/wild/OUTCOMES.md` in the campaign record). The holdout
  split is by family — derivation families {λ-family, shear,
  cn122, T11+T12}, test family {Perminov flip-walk drops} — so
  the λ-family's shared skeleton cannot leak into the test half.
  All five held-out walk states are wrong=1 and land in the hit
  orbits.
- **Independent recount (second path).** Wave 28 re-derived
  every input from the raw JSONs with fresh code
  (`code/recount_cartography.py`, sharing no code with the
  Wave 26 pipeline): its own tensor-difference computation, its
  own rebuild of G from the two generators (both verified to fix
  T), and its own unit-term census. Agreement is exact on every
  count above. One limit: the Monte Carlo p-values are Wave 26's
  statistics — the gate re-derived every input to them exactly
  but did not re-run the Monte Carlo.

## Stated gap

The Heule–Kauers–Seidl database of 17,000+ rank-23 schemes was
**not** censused. This claim is scoped to the campaign bank
named above; a database-wide version is untested and would need
its own pass. A statement phrased in very different vocabulary
could also have been missed by the literature search
(`data/novelty-audit-2.md` lists the sources and gaps).
