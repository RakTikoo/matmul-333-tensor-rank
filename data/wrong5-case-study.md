# Case study: the wrong=5 state over F3, and the exact closure of its neighbourhood

**Date:** 2026-11-24. One named near-miss state over F3 and
three exact closures around it. The state is shipped as
`data/wrong5-state.json` (sha256
2883c3c2b696f2c43da6d13219387b728d857d0d2598ef7108f2fd60dabae31c)
and is judged by the packaged mod-p checker:

```bash
python3 code/checkp.py 3 data/wrong5-state.json
# CHECKP FAIL wrong=5/729 rank=22 field=F3
# first_wrong=[(1,3,0,0,1), (3,2,5,0,1), (4,4,4,0,1), (6,0,6,0,1), (7,5,8,0,1)]
```

("FAIL" is the checker's word for "not an exact scheme": the
state has exactly 5 wrong entries of 729, each a support
entry reading 0 where the tensor wants 1.)

## The claim, at its approved wording

"Over F3, the closest near-miss our searches have produced is a 22-term state with exactly 5 wrong entries of 729 (GPU grammar annealing, 3.68×10¹² aggregate steps; harvested and re-judged exactly at home). All five defects are missing entries on the tensor's support — the one-signed flavour of Item 10. The state's local neighbourhood is now closed exactly, in three senses. (i) Weights: over all 3²² coefficient assignments the minimum wrong count is 5 — the annealer's weights were already optimal for its term shapes. (ii) Shapes: freeing the factors inside the state's own support template gives an unsatisfiable system, for an exact reason — the five defect entries are precisely the support entries no monomial of the template can reach; widening the supports by all cyclic shifts still leaves the entry (1,3,0) unreachable. (iii) Swaps: replacing any one term by any menu shape that covers (1,3,0) (136 such shapes; 35 swaps keep every support entry reachable) gives 35 systems, all unsatisfiable. So no single-term perturbation of this state is an F3 rank-22 scheme. This is a statement about one state's neighbourhood over F3; two-term swaps and swaps on widened supports are explicitly not covered, and nothing here is evidence about rank 22 over Q."

## How the closures were proved

- **Weights (i).** With the state's 22 rank-1 terms frozen,
  one scalar coefficient per term gives a 729 × 22 linear
  system over F3 of rank 22; it is inconsistent, and exact
  feasibility checks at wrong-budgets 1, 2, 3, 4 are all
  UNSAT — so 5 is the exact minimum over all 3²² coefficient
  assignments, and the annealer's all-ones weights were
  already optimal for these term shapes. (The campaign record
  also documents an instrument bug caught here — a backwards
  feasibility flag that briefly reported a false budget-1
  SAT; the mandatory model re-assembly check caught it, and
  the corrected run is the one reported.)
- **Shapes (ii).** Freeing each factor entry within its own
  support (74 unknowns) gives an unsatisfiable system, and
  the reason is exact: a term can only touch entry (p,q,s) if
  p, q, s lie in its three factor supports, and the five
  defect entries are precisely the support entries no term's
  support box contains — the state's 22 × 5 covering matrix
  against its own defects is all-zero. Widening every support
  by a cyclic shift (144 unknowns), and then by the full
  cyclic orbit (213 unknowns), still leaves the entry (1,3,0)
  with no covering monomial.
- **Swaps (iii).** Of the campaign's 1,081-shape support
  menu, 136 shapes cover (1,3,0), and exactly 2 cover all
  five defects. Replacing any one of the 22 terms by any
  covering shape gives 2,992 candidate systems; 35 keep every
  support entry reachable; all 35 are UNSAT (planted controls
  2/2 PASS). The swap-1 neighbourhood is closed at this
  scope; two-term swaps and swaps on widened supports are
  explicitly not covered.
