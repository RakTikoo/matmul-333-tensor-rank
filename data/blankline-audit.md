# Audit of two claims in Blankline Research's January 2026 report

**Date:** 2026-11-22. **Source audited:** Blankline Research,
"Computational Barriers to Rank-22 Decomposition of the 3×3
Matrix Multiplication Tensor", Zenodo record 18443297
(Jan 2026, not peer-reviewed) — its Theorem 5 and its
Theorems 6–7. Both claims were decided by exact rational
arithmetic over ℚ, twice, by independent computations.

## The audit, at its approved wording

Blankline Research's January 2026 report (Zenodo 18443297)
makes two checkable claims. The first — that the compound term
with u={3,5,6,8}, v={1,2,7,8} cannot route its products
consistently — is correct in its stated single-term scope; we
verified the witness rows directly. The second — that its
"1+2+19" structure has minimum residual √6, identical for all
2^16 sign patterns — does not hold for the part of the claim
that can be reconstructed from the publication: two
independent exact computations give a minimum residual² of 7
(not 6) for the compound term T1, with the residual taking five
distinct values across sign patterns, so it is not
sign-invariant either. The full 22-term claim cannot be decided
from the publication, because the supports of the remaining
terms are never given. **Neither result moves any bound on the
rank of ⟨3,3,3⟩.**

## Details

**Claim (i) — routing inconsistency (their Theorem 5):
CONFIRMED in scope.** Under the report's own indexing, the
target rows force contradictory values on one factor: T[3][1][·]
is supported exactly at c=4 and T[3][2][·] exactly at c=5,
forcing w₄=1, w₅=0 and w₅=1, w₄=0 respectively; the Farkas
certificate is eq(3,1,4) − eq(3,2,4) ≡ 0·w = 1. The full system
the term induces on its touched rows (144 equations, 9
unknowns) has rank(A)=9 < rank([A|T])=10 — inconsistent over ℚ
— and the contradiction survives all 256 factorable sign
patterns on (u,v). Scope: the argument treats the term in
isolation (cancellation by other terms is what it excludes), so
it is a fact about this support pattern, not a barrier to rank
22. (A parenthetical in the report — "(729 equations, 198
variables)" — does not describe this system; 198 = 22×9 belongs
to its §5 system.)

**Claim (ii) — "1+2+19" minimum residual √6, sign-invariant
(their Theorems 6–7): decidable core REFUTED; full claim
UNDECIDABLE-FROM-PUBLICATION.** What can be rebuilt exactly is
the structure's core, the compound term T1 (its coverage does
check out: 16 output pairs, 8 useful + 8 garbage, all four of
the report's "anchor" products covered). Exact rational least
squares over T1's 144 touched rows gives minimum residual² =
**7** (residual √7 ≈ 2.646), not 6; over all 2^16 per-pair sign
patterns the exact minimum residual² takes the five distinct
values **{7, 29/4, 15/2, 31/4, 8}** — not sign-invariant, and
√6 occurs for no pattern. (Against all 729 rows the residual²
is ≥ 19.) The full 22-term claim cannot be rebuilt: the (u,v)
supports of the remaining terms T2–T22 are never printed, the
2^16 sign space is never defined for the full system, and no
system or norm for §5 is ever stated.

**Proportionality note.** The report's Theorem 8 (single-term
elimination from Laderman with coefficients in {−3,…,3} is
impossible) is a scoped statement that this campaign's stronger
exclusions exceed but do not contradict; nothing in this audit
touches it. "Blankline's barriers are refuted" as a wholesale
statement would overclaim: claim (i) is confirmed, and only the
printed numbers of claim (ii) fail, on the reconstructible core.

## Deciding artefacts

Campaign Wave 24 (`s2_blankline.py`, exact rational arithmetic
from the published PDF) and the Wave 28 gate
(`c5_spotcheck.py`, an independent derivation from the PDF:
closed-form least squares per output index). The two
computations agree exactly, including the five-value residual
set.
