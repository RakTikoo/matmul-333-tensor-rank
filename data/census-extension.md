# Census extension — the universal form does not extend beyond the original bank

**Date:** 2026-11-23. **Population (named, finite):** every other
verified ⟨3,3,3⟩ scheme on the campaign disk beyond the original
11 bank files of `data/cartography.md`: **48 further files, 40
distinct schemes** (up to tensor-identical term multisets), each
re-verified exactly over ℚ. All quantities over ℚ: unit terms
(exactly one nonzero in each factor column), and whether each unit
term's single position lies on the 27-position support of T
("naive") or off it.

## The claim, at its approved wording

We extended the Wave 26/28 unit-term census to every other verified ⟨3,3,3⟩ scheme on our disk: 48 further files, 40 distinct schemes, each re-verified exactly over Q. Of the 50 unit terms in those 40 schemes, 49 are naive — and one is not. The exception is term 0 of the rank-24 scheme obtained by downward projection of a ⟨3,3,4⟩ scheme (solven-eu catalogue): its factors are e₅, −e₈, e₄, so its single entry sits at position (5,8,4), where the matrix-multiplication tensor is zero. The universal statement 'every unit term in every verified scheme is naive' therefore does not extend beyond the original bank. What survives is narrower: every unit term in every rank-23 scheme in the extended census is naive (the published 41-of-41 statement about the original 11 bank schemes is untouched), and the single counterexample is at rank 24, in a scheme of a different construction type. Two independent exact computations agree on every count. Unit-term-ness is a property of a scheme's presentation, not of its orbit: the 30 de Groote transforms of Laderman in the census carry no unit terms at all. This is anatomy of the schemes we hold, not evidence about rank 22.

## Census numbers

- Per file: **210 unit terms, 209 naive, 1 off-support** across
  the 48 held-out files.
- Per distinct scheme: **50 unit terms, 49 naive, 1 off-support**
  across the 40 distinct schemes. (Duplicate groups: the naive
  rank-27 scheme in 2 files; the lensC rank-26 tensor in 8 files.)
- The counterexample, verified directly from its file: term 0 of
  the rank-24 projection scheme has U column = +1 at row 5 only,
  V column = −1 at row 8 only, W column = +1 at row 4 only — a
  unit term — and its term tensor has exactly one nonzero entry,
  −1 at flat position 481 = (5,8,4) = ((1,2),(2,2),(1,1)), where
  T = 0.
- The 30 shear/dense de Groote transform files (ladT00–ladT29)
  carry **zero unit terms each**.

## Method

- **Population.** The held-out list is the Wave 30 enumeration:
  every verified-over-ℚ ⟨3,3,3⟩ scheme object on the campaign
  disk that was neither one of the original 11 bank files nor a
  tensor-identical duplicate of one. T12 is classified among the
  original 11 in that enumeration — it was not held out.
- **Independent recount (second path).** The Wave 32 gate
  re-derived every count with fresh code
  (`code/recount_census_extension.py`, sharing no code with the
  Wave 30 census or with the Wave 28 recount): each of the 48
  files was re-judged two ways — the gate's own exact Fraction
  recomputation (0 wrong of 729 for every file) and a
  fresh-process `verify.py check` run (48/48 VERIFIED) — and the
  census was recomputed from the tensor definition. Agreement is
  exact on every count above, in both countings.

## Stated gap

The Heule–Kauers–Seidl database of 17,000+ rank-23 schemes was
**not** censused — by this campaign or, so far as the sources
searched show, by anyone. This claim is scoped to the 48 files /
40 distinct schemes named above; schemes not on this disk are
likewise outside the population. No version of this census,
positive or negative, extends to that database.
