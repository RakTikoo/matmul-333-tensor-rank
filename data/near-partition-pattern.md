# The near-partition pattern: support shapes carry a learnable signature of near-exactness (a labelled speculative bet)

**Date:** 2026-11-24. This item was run as a labelled
speculative bet: train a classifier to distinguish the
support shapes of near-exact term sets from random shapes,
read off the pattern, and exact-test its best proposals.
The pattern validated; the proposals did not. Both halves
are the claim.

## The claim, at its approved wording

"Support shapes carry a learnable signature of near-exactness. On a corpus of 7,255 support templates (drop-one supports of our banked exact rank-23 schemes as positives-by-proxy; random menu subsets and fake-scheme drops as negatives), a random forest separates the classes perfectly on a scheme-held-out split (AUC 1.0000), where a reachability-only baseline is at chance (0.5320). The signature: near-exact shapes are sparse near-partitions of the target — about 91% of the entries that must be hit are covered exactly once, overlap between terms is minimal, and almost no coverage is wasted on entries that must stay zero; symmetry/orbit features carry no signal. We state the limit in the same place: the signature is necessary-looking, not sufficient. The model's ten best-scoring new proposals, all passing full reachability, were exact-tested — all ten are provably empty. The pattern's use is as a pre-filter for future template enumerations; it is not a construction, and the positives are proxies (supports of rank-23 schemes minus a term), since no exact rank-22 template exists to train on."

## Numbers

- **Corpus.** 7,255 support templates with 35 exact features
  each: 2,255 positives-by-proxy (drop-one supports of 98
  unique banked exact rank-23 schemes, plus the wrong=5
  support of `data/wrong5-case-study.md`, train-only) against
  5,000 negatives (2,500 random menu 22-subsets; 2,500
  drop-one supports of random fake schemes).
- **Separation.** Random forest, group-split holdout by
  scheme (1,779 rows): AUC 1.0000, against a reachability-only
  baseline at 0.5320 (random menu shapes already cover
  91–96% of support entries, so reachability alone
  distinguishes nothing). The pre-registered rule (learned
  part valid iff it beats the baseline by ≥ 0.02) passes.
- **The signature.** Near-exact shapes are sparse
  near-partitions: ~7.0 nonzero entries per support triple
  against 12.0 for negatives; 91% of the entries that must be
  hit are covered exactly once (negatives 21%); mean coverage
  of entries that must stay zero is 0.37 (negatives 2.20);
  mean pairwise term overlap 1.83 (negatives 5.36). Top
  features: zero-entry coverage mean, exactly-once coverage
  fraction, overlap mean, triple-nnz mean. Symmetry/orbit
  features carry no signal (importances ≤ 0.00014). The
  signature is the statistical shadow of the one-signedness
  phenomenon of `data/one-signedness.md`: real schemes work
  with almost no cancellation, and their supports show it
  before any coefficient is chosen. (Recorded caveat: part of
  the separation rides on sparsity, since the negatives
  inherit menu density; the coverage-economy features are
  per-template normalised and carry independent signal.)
- **The limit.** 12,000 mutants of known-good supports →
  1,279 passed full reachability → the 10 best by model
  score (all scoring 1.0000, profiles inside the positive
  envelope, 146–172 template unknowns each) were exact-tested
  over F3: **10/10 UNSAT** (0.7–16.6 s each). Exactness lives
  below support level, in coefficient arithmetic the
  support-only model cannot see. The pattern's use is as a
  pre-filter for future template enumerations.
