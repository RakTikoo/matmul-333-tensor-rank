# The ladder — exact kernel dimensions at ranks 23–26

**Date:** 2026-11-22. Pointwise exact Jacobian-kernel dimensions
over ℚ at named ⟨3,3,3⟩ schemes, measured with one machinery and
each re-pinned by an independent second path. "Excess" means:
the Jacobian kernel dimension minus the dimension of the
trivial (rescaling + isotropy) tangents **as measured at that
point** — the trivial span is point-dependent and is never
assumed from a formula.

## The table

| rank | point | dim ker J | trivial span (measured) | excess |
|---|---|---|---|---|
| 23 | Laderman (1976) | 76 | 70 | **6** |
| 23 | Perminov cn122 | 94 | 70 | **24** |
| 23 | Perminov cr58_cn122 ("T11") | 94 | 70 | **24** |
| 24 | metaflip (Perminov meta-flip-graph, solven-eu catalog) | 102 | 72 | **30** |
| 24 | projection (downward projection of a ⟨3,3,4⟩ scheme, solven-eu catalog) | 111 | 72 | **39** |
| 25 | split of metaflip-24 — CONSTRUCTED-DEGENERATE, calibration only | 129 | 74 | 55 raw = 25 split + 30 inherited; **net 30** |
| 26 | lensC block construction (this campaign's own) | 187 | **73** | **114** |

Every scheme in the table passed `code/verify.py check` in a
fresh process (0/729 wrong over ℚ) before measurement. The two
rank-24 schemes are literature schemes taken from the solven-eu
matmulcatalog's published data; no genuine noncommutative
rank-25 scheme was found in either catalogue searched, so the
rank-25 row is a deliberate term split of the metaflip scheme,
included only as a calibration: its artificial kernel (25
dimensions from the split) is identified and removed exactly,
its net excess equals its parent's (30), and its kernel closes
with nothing left over (74 trivial + 25 split + 30 lifted parent
vectors = 129). It is kept out of any trend reading.

At lensC the trivial span is **73, not the formula value 78**:
the torus has 52 dimensions there and the orbit tangent 26, but
they overlap in 5 dimensions, not the generic 2 — extra
block-wise rescalings sit in both. The excess 114 is against
the measured 73.

## The claim, at its approved wording

At the two genuine rank-24 schemes we measured (a Perminov
meta-flip-graph scheme and a downward projection of a ⟨3,3,4⟩
scheme, both from the solven-eu catalog), the Brent Jacobian
over ℚ has kernel dimension 102 and 111, exceeding the trivial
tangents (72) by 30 and 39 dimensions. At the campaign's own
rank-26 block construction the kernel dimension is 187,
exceeding the trivial tangents — 73 at this point, not the
generic 78, because the torus and orbit tangents overlap in 5
dimensions there — by 114. All values are exact over ℚ, pinned
from both sides. Together with the rank-23 values (Laderman
excess 6; cn122 and cr58_cn122 excess 24) they show **no
monotone behaviour in the rank: within-rank spread is as large
as any between-rank difference, so these numbers constrain
nothing about rank 22.**

## Second path

Wave 28 recomputed all three new points with a from-scratch
Jacobian (`code/check_kernels_independent.py`): ranks at the
fresh primes 104729, 1299709, 15485863 agree at each point
(546 / 537 / 515, giving the nullity upper bounds 102 / 111 /
187); the stored kernel bases (102 / 111 / 187 vectors) were
annihilated exactly, 0 failures in 494 vector checks, each of
full rank. Trivial spans were independently reproduced by the
gate's own tangent construction: 72, 72, and 73 at lensC —
including the overlap anomaly.
