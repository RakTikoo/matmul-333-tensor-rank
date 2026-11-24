# Walk anatomy — the terms-merging trips were cancellation artefacts

**Date:** 2026-11-23. **Object (named, finite):** the campaign's
own homotopy-walk data — the five predictor-corrector walks of
Wave 20 along exact moduli directions of the rank-23 fibre over
ℚ (Perminov's cn122, 3 directions; Laderman's scheme, 2
directions), run in float arithmetic on Kaggle (notebook
`matmul-walk`, version 3, 2026-11-23) and followed up exactly in
Wave 45. Quantities: signed vs unsigned pairwise term cosines,
pair-sum norms and rank-1 defects, term norms, fused-22 tensor
errors, and exact (over-ℚ) factor-column identities in the seed
schemes. This is a cautionary result about a monitoring
criterion; it makes no statement about rank 22 in either
direction.

## The claim, at its approved wording

"Our homotopy walks along the rank-23 fibre (Wave 20 machinery, run on Kaggle) tripped a 'terms merging' monitor — pairwise term cosine above 0.99 — in four of five directions. Exact follow-up shows the trips were an artefact of the monitor, which recorded the cosine's absolute value: the signed cosines are ≈ −0.99, so the pairs approach anti-parallelism (mutual cancellation), not parallelism (fusion). While the cosines climbed, the pairs' sums stayed bounded and their rank-1 defect stayed flat or grew (1.00→1.02 in the cleanest direction), the individual term norms inflated by an order of magnitude or more, and replacing a pair by its best rank-1 approximation leaves tensor errors of 1.02–9.42 against ‖T‖ = 5.20; rational reconstructions of the fused 22-term forms were rejected by exact verification on all 729 entries. The walk was sliding along the fibre's non-compact cancellation directions, where |cos| → 1 is automatic. A structural by-product, verified exactly over Q by an independent check: each of the three tripping Perminov pairs shares a factor column identically in the seed (terms 6 and 20 share their W column; terms 2 and 18 and terms 5 and 8 share their V columns) — the cancellation directions live on those shared-factor strata. (A complete scan finds seven shared-factor pairs in cn122 in total; the three above are the ones the walk tripped on. Laderman's scheme has no identical factor-column pair at all.) We have retired the |cos| trip criterion; a merge signal requires a pair-sum rank-1 defect → 0 at bounded term norms. Nothing in this episode bears on whether rank-22 schemes exist: these paths do not approach one, and no conclusion about the families' closures is drawn."

## Numbers

- **Trips:** the |cos| monitor (threshold 0.99) tripped in 4 of
  5 directions. The signed tensor cosines of the tripping pairs
  are ≈ −0.99 throughout: Perminov dir0 pair (6,20) −0.9921,
  dir1 pair (2,18) −0.9903, dir2 pair (5,8) −0.9916; Laderman
  dir1 pair (7,11) −0.9943. Laderman dir0 did not trip and shows
  the same anti-parallel drift in slow motion (−0.897 at step
  60). All three factor cosines of each tripping pair → 1 in
  absolute value — genuine three-factor alignment, with the
  wrong sign for fusion.
- **Pair sums stay bounded; defects do not fall.** For the
  cleanest direction (Perminov dir0), the pair-sum norm goes
  3.0000 → 1.7777 while its rank-1 defect stays flat
  (1.00 → 1.02); across the four trips the defect is flat or
  growing (1.00→1.02, 1.00→1.09, 1.41→1.57, 1.78→9.42). A
  genuine merge needs the defect → 0.
- **Term norms inflate.** The tripping pairs' term norms reach
  ≈14 / 19 / 18 / 141 (from ≈1–3 at the seeds); bystander
  anti-parallel pairs at the same endpoints reach norms of
  ≈220 and ≈2.8×10⁵, while the walked tensor stays exact to
  ≈10⁻¹¹. Perminov dir0's tail motion is ≥99% pure inflation:
  per-step pair-sum change ≈0.006 against per-step term change
  ≈5.03.
- **Fusion is O(1) away.** Replacing a tripping pair by its best
  rank-1 approximation leaves Frobenius errors 1.02 / 1.09 /
  1.57 / 9.42 against ‖T‖_F = 5.196 (660–709 of 729 entries off
  by more than 10⁻⁶). Bounded rational reconstructions of the
  two cleanest fused 22-term forms (denominator caps up to
  10⁴) were **rejected by exact verification on all 729
  entries** — rounding was never the obstacle.

## Second path (Wave-47 gate)

Fresh gate code re-derived, without opening Wave 45's analysis
scripts: (i) the three shared-factor identities exactly over ℚ
from the seed files — cn122 **W column 6 = W column 20; V
column 2 = V column 18; V column 5 = V column 8** — all true;
(ii) Laderman's pairs share no factor column — Laderman has
**no identical factor-column pair in any factor**; (iii) the
Perminov dir0 signed-cosine claim from the harvested walk
states: final pair (6,20) factor cosines +0.99471 / −0.99734 /
+1.000000, signed product −0.99207, term norms 14.05 / 14.14,
pair-sum norm 3.0000 → 1.7777 — agreement with Wave 45's record
to its recorded precision. A complete identical-column scan of
cn122 finds **seven** shared-factor pairs in total (V: (2,18),
(5,8), (6,11); W: (6,20), (8,14), (13,18), (17,19); U: none);
the three named in the claim are exactly the tripping pairs.
The defect trajectories, fusion errors and the two verify.py
rejections stand on Wave 45's own record, consistently with
the re-derived numbers.

## Standing consequence

The |cos| trip criterion is **retired**. Any future walk logs
signed cosines, pair-sum norms, rank-1 defects and term norms,
and a merge signal requires a pair-sum rank-1 defect → 0 at
bounded term norms. A gauge-fixed re-walk (inflation projected
out) is the registered decider for whether these families have
approachable boundaries at all; as of this record's date it
stood built and queued, not run.

## Extension (v1.4.0, 2026-11-24): the gauge-fixed re-walk ran — all five directions stall

The registered decider has now run. The gauge-fixed re-walk
(term-norm cap at 3× the seed maximum, a defect-monotone
exception, a trip defined as defect < 0.05 at bounded norms)
ran in all five registered directions from cn122 and
Laderman; every direction stalled — no trip under the
corrected criterion. Under the line's pre-registered rule,
the walk approach to rank reduction from these seeds is
closed. At its approved wording (claims.md Item 17):

"The walk line is closed. The gauge-fixed re-walk built after the Wave 45 artefact anatomy (term-norm cap at 3× the seed maximum, defect-monotone exception, a trip defined as defect < 0.05 at bounded norms) ran in all five registered directions; every direction stalled. Under the line's pre-registered rule, the walk approach to rank reduction from these seeds is closed. This complements the v1.3.0 walk-anatomy item: the earlier trips were cancellation artefacts, and the corrected instrument finds no genuine approach either."
