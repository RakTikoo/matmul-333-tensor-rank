# Census of the Heule–Kauers–Seidl repository — every unit term is naive

**Date:** 2026-11-23. **Population (named, finite):** the complete
Heule–Kauers–Seidl distribution of ⟨3,3,3⟩ rank-23 schemes (JKU
Linz repository, as distributed 2020-08-06; bulk archive
`schemes.tgz`, 43,134,227 bytes): **17,376 schemes, every one with
entries in {−1, 0, 1}**. Quantities: unit terms (a term whose
tensor has exactly one nonzero entry), and whether that entry
lies on the 27-position support of T ("naive") or off it. This
census closes the gap stated in `data/census-extension.md`,
where the Heule–Kauers–Seidl database was named as not censused.

## The claim, at its approved wording

"We censused the complete Heule–Kauers–Seidl repository of ⟨3,3,3⟩ rank-23 schemes as distributed (17,376 schemes, all with entries in {−1, 0, 1}). Across the whole population there are 1,882 unit terms — terms whose tensor has a single nonzero entry — and every one of them is naive: its entry sits on the 27-position support of the matrix-multiplication tensor. No off-support unit term exists in this population. Three independent computations agree on every count (a SAT-solver-hosted kernel run, and two differently-structured home recounts, one of which also verified all 17,376 schemes exactly, with zero wrong entries). This extends our earlier bank censuses (41 of 41 unit terms naive across the 11 original bank schemes; 49 of 50 across 40 further schemes, the single exception being a rank-24 scheme): within rank 23, every unit term in every scheme population we have censused is naive. The statement is about these named populations — it is not a theorem about all rank-23 schemes over Q, and it is not evidence about rank 22: a rank-22 scheme need not contain any unit term."

## Census numbers

- **17,376 schemes parsed, 0 parse failures**; the token set seen
  across the whole population is exactly {−1, 0, 1}.
- **Unit terms: 1,882 in total — naive 1,882, off-support 0.**
- **1,708 schemes carry at least one unit term**; 0 schemes are
  degenerate.
- **17,375 distinct term-multisets** among the 17,376 files: the
  single duplicate pair (`i91w197c347f-000.tab` /
  `i91w197c347f-001.tab`, in pattern directory
  `25x2+44x+3y6+4y5+8y4+8y3+z33+z31+z30`) is a pair of
  **byte-identical files** in the distribution, carrying 0 unit
  terms — the population's only multiplicity is a literal
  duplicate file.
- Comparison with the campaign bank: the bank's 53 files give
  exactly **51 distinct term-multisets, and the intersection with
  the population is empty** — no population scheme matches a
  banked scheme as a term multiset.
- The classic Laderman scheme in the population is its **only
  scheme with ≥5 unit terms** (exactly 5, all naive); the other
  three classics (Courtois–Bard–Hulme, Oh–Kim–Moon, Smirnov)
  carry no unit terms.

## Method — three independent computations

- **Path 1 (the census run).** A kernel run on Kaggle
  (notebook `matmul-hks`, 2026-11-23) downloaded the archive
  in-kernel (both size and member-count guards passed), parsed
  all 17,376 `.tab` files, and verified exactly: all 1,708
  unit-carrying schemes (0 failed) and a seeded random sample
  of 300 zero-unit schemes (0 failed). The run's output bundle
  could not be transferred home (93.81 MB, browser downloads
  interrupted), so no number below rests on it alone.
- **Path 2 (home recount).** `code/recount_hks_census.py`,
  written fresh for the harvest, re-derived the entire census
  from the locally held copy of the same archive (byte-size
  identical, 43,134,227 bytes) and verified **all 17,376
  schemes exactly — 0 wrong entries anywhere**. Every tally
  above matches Path 1 exactly.
- **Path 3 (claim-gate derivation).** The Wave-47 gate's
  differently-structured recount decided unit-ness by the
  product route (each term's full sparse product multiplied
  out) instead of from the factor columns, reproduced the
  headline tallies over the full population, and verified a
  1,000-file slice scheme-by-scheme (1,000/1,000 exact; 197
  unit terms, all naive).
- The three paths share only the archive bytes and the `.tab`
  format facts (23 blocks × 3 rows, `|` separators, W stored
  transposed) — each path re-diagnosed the format by its own
  verification leg (0/729 under the transposed reading vs
  exactly 36/729 under the direct reading, for the classics).
  No code, parser, or counting method is shared between any
  two paths.

## Scope

The statement is about this named population as distributed on
2020-08-06; a later repository revision would be a different
population. Schemes with entries outside {−1, 0, 1} and
schemes outside this repository are covered only by the earlier
bank censuses (`data/cartography.md`,
`data/census-extension.md`), not by this one. The single known
off-support unit term anywhere in the campaign's censuses
remains the rank-24 counterexample of
`data/census-extension.md`; nothing here is a theorem about all
rank-23 schemes over ℚ, and nothing here is evidence about
rank 22.
