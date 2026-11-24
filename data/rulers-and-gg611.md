# Rulers at cn122: 21 exact lines, 114 flat planes, no rank drop — and the one grip-gain scheme gg611

**Date:** 2026-11-24. Exact geometry over ℚ of the rank-23
variety at one named point: Perminov's cn122, whose Jacobian
kernel has dimension 94 (excess 24 over the trivial span 70;
see the headline result). A *ruler* is a straight line through
cn122 lying entirely in the rank-23 variety — equivalently a
kernel direction of the Jacobian along which the quadratic
obstruction also vanishes. All computations are exact
(rational arithmetic); sampled points on the lines were
verified with `verify.py`.

## Item 21 — the ruler census

**The claim, at its approved wording**

"At Perminov's rank-23 scheme cn122 (Jacobian nullity 94 over Q, excess 24 over the trivial span), we computed the exact straight lines in the rank-23 variety through the point. Within the searched scope — all directions in two-dimensional coordinate planes of the kernel basis, plus the shear lines — there are exactly 21 ruler directions; 114 of the 153 two-planes spanned by pairs of the 18 flat basis rulers are themselves entirely flat. Along all 21 lines there is no term-zero event and no two-term proportionality event at any rational parameter: no rank drop occurs anywhere on them (42 sampled schemes on the lines were verified exactly). Extending the scan to the flat planes: no term vanishes anywhere in any of the 134 flat planes, and for all 596 tested (plane, term-pair) combinations the simultaneous proportionality ideal is the unit ideal, so no two terms merge at any point of those planes, even over ℂ. Random directions are never rulers (0 of 3,000 sampled at cn122; 0 of 3,000 at Laderman, which has no shear lines at all). Scopes: directions supported on three or more kernel basis vectors outside the flat planes are not excluded, and the plane merge scan covers the restricted pair set stated in our record."

How the 21 directions arise: the kernel basis at cn122
contains 18 *flat singles* — directions flat to second order
on their own (14 of them are the shear lines of cn122's seven
identical-factor pairs, counted with multiplicity of
construction) — and 3 further *isolated pair directions* flat
only in combination. Two-planes spanned by pairs of flat
singles: 114 of 153 are flat in every direction. On the flat
planes, no term vanishes anywhere, and the simultaneous
proportionality (merge) test was run for all 596 tested
(plane, term-pair) combinations: in every case the ideal of
3-slot minors has Gröbner basis [1], so no two terms merge at
any point of those planes, even over ℂ. Random directions are
rulers with frequency 0 in 3,000 samples at cn122 and 0 in
3,000 at Laderman.

## Item 22 — gg611, the unique grip-gain point

**The claim, at its approved wording**

"Exactly one point on the 21 ruler lines through cn122 strictly increases the identical-factor pair count: the t = 1 point of one shear line, with 8 pairs — cn122's seven plus a (6,15) pair in the first factor that cn122 itself does not have. That scheme (gg611) is banked and verified exactly (rank 23 over Q). Its shear family gives 96 exact variants (93 new to our bank) and 150 new 22-term wrong=1 states, from which 2,400 free-4 repair cases are derived and staged. The other three candidate points on the lines are pair swaps at count 7, not gains — we record this correction of Wave 57's preliminary reading in the same place."

"Grip" is the count of identical-factor pairs (two terms
sharing a factor column in one slot). Scanning all 21 ruler
lines for points where the grip strictly increases found
exactly one: t = 1 on the shear line of the (6,11) pair in the
V slot, where a new identical pair (6,15) appears in the U
slot, taking the count from 7 to 8. (Three other candidate
points first read as gains are pair swaps at count 7; the
correction is recorded here as in the campaign record.) The
scheme is shipped as `data/gg611_r23_Q.json` and verifies
exactly:

```bash
python3 code/verify.py check data/gg611_r23_Q.json   # VERIFIED, rank 23, 0/729 over Q
```

Its shear family (96 exact variants, 93 new to the campaign
bank) yields 150 new 22-term wrong=1 states and 2,400 derived
free-4 repair cases, staged for a solver run that is queued,
not yet run.
