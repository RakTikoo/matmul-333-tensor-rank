# Cross-family transplants — a bounded term-sharing census

**Date:** 2026-11-22. **Set (named, finite):** the eight
verified rank-23 ⟨3,3,3⟩ schemes in the campaign bank — the
Laderman λ-family (λ ∈ {1, −1, 2, 1/2, −2, 3}, one skeleton in
six parametrisations), Perminov's cn122, and Perminov's
cr58_cn122 ("T11"). **Test:** exact equality over ℚ of single
rank-1 terms and of pair sums of rank-1 terms between schemes
of different families — transplants of depth at most 2.

## The claim, at its approved wording

Among the eight rank-23 schemes in our bank (the Laderman
λ-family, Perminov's cn122, and Perminov's cr58_cn122), exact
comparison over ℚ finds the three families share almost no raw
material: of 184 rank-1 terms only 158 are distinct, but the
single term shared across families is one naive unit term (at
(1,0,1)); and no pair of terms from one family sums to a pair
from another (1,974 distinct pair sums, no genuine cross-family
collision). In this bounded sense — these eight schemes,
transplants of depth at most 2, over ℚ — the families cannot
be hybridised by swapping one or two terms. We have not found
this term-sharing census stated in the literature we searched;
the neighbouring published notions are de Groote equivalence
classes and flip-graph components (see
`data/novelty-audit-2.md`).

## Numbers

- 184 terms across the 8 schemes; **158 distinct** as exact
  rank-1 tensors (canonical primitive-integer 729-vectors).
- Term tensors shared across families: **exactly 1** — the
  naive unit term at (i,j,k) = (1,0,1): Laderman term 20 =
  cr58_cn122 term 14, also shared by all λ parametrisations.
  cn122 shares no term with either other family.
- **1,974 distinct pair sums**; 10 cross-scheme pair-sum
  collisions, all within the λ-family (restatements of its
  shared skeleton); **genuine cross-family pair-sum hits: 0**;
  within-scheme duplicate pair sums: 0.
- All 8 schemes were re-judged fresh (VERIFIED 0/729 over ℚ)
  before testing.

## Second path and bounds

Wave 28 recomputed the census with fresh canonicalisation code
(campaign record: `wave28/gate/c2c4_check.py`), sharing no code
with the Wave 26 pipeline; every number above agrees exactly.

This is **not** a statement about all rank-23 schemes, about
transplants of depth ≥ 3, or about flip-graph connectivity in
general. Rank-24 schemes were excluded (rank bookkeeping
differs). The Heule–Kauers–Seidl database was not censused.
