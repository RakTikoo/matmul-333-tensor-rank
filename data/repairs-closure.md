# Decided repair fronts: the repairs closure (1,843/1,843) and the new-basins front (336/336)

**Date:** 2026-11-24. Two free-4 repair fronts over ℚ, decided
completely by the control-validated generalised parity-split
machinery (the Wave 42 generalised driver; the covering-parity
split itself is claims.md Item 1). In both fronts the move is
the same: four terms of a banked near-miss state are freed with
coefficients in {0, ±1}, the remaining terms frozen; the
instance splits into exhaustive covering-parity cases, and each
case UNSAT excludes only that case's covering vector on that
seed. Every run carried the encoder's control gate (a
known-good scheme with the same terms freed returns SAT and
verifies), and the control artefacts were re-judged at home in
fresh `verify.py` processes.

## Item 15 — the repairs closure: 1,843/1,843 UNSAT

**The claim, at its approved wording**

"The repair front is decided at its registered scope. For each of seven banked near-miss states — six 22-term wrong=2 states from rank-23 parents and the one off-support wrong=1 state (proj-24 minus term 0) — we enumerated every covering-parity case of the free-4 repair move (four terms freed, coefficients in {0, ±1}, the other terms frozen, over Q): 1,843 cases in total. All 1,843 are UNSAT, with the encoder's control gate passed in the same run and its control artefacts re-verified exactly at home. No rank-22 scheme is reachable by this repair move from any of these seven states, and the off-support state has no free-4 {0,±1} repair to a new rank-23 scheme either. The closure is scoped to this move, this free-set size, and this coefficient set; other repair settings are separate fronts."

The seven states: six 22-term wrong=2 states obtained from
rank-23 parents (304 covering cases each) and the one
off-support wrong=1 state (proj-24 minus term 0; 19 cases) —
1,843 cases in total, all UNSAT, 7/7 instances decided, no SAT
and no undecided case anywhere in the front. A SAT on the
wrong=2 instances would have assembled a rank-22 scheme over
ℚ; a SAT on the off-support instance would have assembled a
new rank-23 scheme. Neither exists at this scope.

## Item 16 — the new-basins front: 336/336 UNSAT

**The claim, at its approved wording**

"The new-basins free-4 front is fully decided. The 21 wrong=1 states obtained in Wave 39 from nine orbit-distinct catalogue schemes generated 336 free-4 {0,±1} repair cases over Q; all 336 are UNSAT (21/21 instances decided, controls passed). No rank-22 scheme is reachable by this repair move from any of these 21 states."

The 21 wrong=1 states came from nine schemes of the
solven-eu catalogue that the campaign proved pairwise
orbit-distinct (a genuinely separate set of basins from the
classical schemes), 16 covering cases per state. All 336 cases
are UNSAT, 21/21 instances decided, controls passed in the
same run.

## The two fronts together

The fronts may be summed only as "2,179 decided repair cases
across the two fronts" (1,843 + 336), each front named. Both
closures are scoped to the free-4 {0,±1} repair move on the
named states; other free-set sizes, other coefficient sets and
other states are separate fronts (the partial ones are in
`data/partial-fronts.md`).
