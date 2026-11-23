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

## Extension (2026-11-23): unequal cardinalities, bank-wide

**Set (named, finite):** the enlarged campaign bank — 62 files
reducing to **60 distinct verified ⟨3,3,3⟩ schemes** (46
distinct rank-23 schemes, plus ranks 24 ×2, 25, 26, 27).
**Test:** all subset sums of sizes 1–4 (679,539, exact over ℚ),
compared across adjacent cardinalities (2,1), (3,2), (4,3),
within and across schemes — the shape a rank-reducing term
transplant would need at unequal sizes. Measured in Wave 41;
gated in Wave 47.

### The extension claim, at its approved wording

"We extended the cross-scheme transplant census to unequal cardinalities across the whole enlarged bank: all subset sums of sizes 1–4 over the 60 distinct verified ⟨3,3,3⟩ schemes we hold (679,539 sums, exact), compared between adjacent cardinalities (2,1), (3,2), (4,3), within and across schemes. The only exact equalities anywhere are 277 hits between the rank-25 scheme we ourselves constructed by splitting one term of the rank-24 metaflip scheme in Wave 22 and that parent scheme — the split's own undoing, with counts 1, 23, 253 = C(23, k−2) exactly, whose assembled candidate is the parent scheme itself. There is no genuine cross-scheme subset-sum swap at any cardinality ≤ 4 in this pool; together with the earlier equal-cardinality censuses (depth ≤ 4 over the core 8 schemes), the transplant line is closed at all cardinalities ≤ 4 for the schemes we hold. Two independent exact computations agree on every hit and every count. Depth-5 comparisons were not run; nothing here is a statement about schemes outside the bank."

### Second path

The Wave-47 gate re-derived the hit census by a different
route (all entries scaled to integers by one global LCM,
subset sums as dense integer arrays, candidates from a sha256
index with every candidate confirmed by exact array equality —
no modular digest) on a 21-scheme sub-pool (a seeded random 20
of the 60, plus metaflip-24): 244,410 subset sums produced
**exactly 277 hits, all in the split group, counts 1 / 23 / 253
= C(23, k−2), zero genuine** — identical to the full-pool
census, because every hit in the pool involves only split-25
and metaflip-24 and both were in the sub-pool. The spot check
therefore re-derives the complete hit census, not a sample of
it; it does not re-derive the 679,539-sum total over the full
pool, and depth-5 comparisons were not run by either path.
