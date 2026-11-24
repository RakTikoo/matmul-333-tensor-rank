# Partial free-4 fronts: hinge (631/3,072), proj24-family (943/1,140), shear family (414 decided, one run lost)

**Date:** 2026-11-24. Three free-4 {0,±1} repair fronts over ℚ
(same move and scoping as `data/repairs-closure.md`) whose
solver runs completed on their time budgets with part of each
queue unattempted. Decided fractions are stated with their
denominators and their not-attempted counts; no front-level
conclusion is drawn from any of them. All decided cases are
UNSAT; no SAT occurred anywhere in this release's fronts.

## Item 18 — the hinge front: 631 of 3,072 decided

**The claim, at its approved wording**

"Of the 3,072 free-4 {0,±1} repair cases derived from the 192 hinge wrong=1 states of Wave 48, 631 have been decided — all UNSAT (39 of 192 instances fully decided, one further instance partially). The remaining 2,441 cases are not yet attempted; this front is partial, and no front-level conclusion is drawn from it."

The 192 states came from the hinge construction of Wave 48:
84 exact rank-23 schemes built by re-factorising the seven
shared-factor pairs of Perminov's cn122, each contributing
wrong=1 drop states. The completed run decided instances
I000–I038 completely and I039 partially (7 of its 16 cases).

## Item 19 — the proj24-family front: 943 of 1,140 decided

**The claim, at its approved wording**

"Of the 1,140 free-4 {0,±1} repair cases derived from the 60 wrong=1 drop states of the Wave 55 shear families (on the exact rank-24 parents proj24 and metaflip24), 943 have been decided — all UNSAT (49 of 60 instances fully decided, one partially). The remaining 197 cases are not yet attempted; the front is partial. A repair here would have assembled an exact rank-23 scheme, not a rank-22 one; the front's value is ladder connectivity (Wave 66), and the wording must keep that scope."

The parents are exact rank-24 schemes (proj24 with six
identical-factor pairs, metaflip24 with one), so these
instances test repair to an exact rank-23 scheme — the ladder
question of whether the rank-24 level connects downward — not
rank 22. The completed run decided 49 of 60 instances
completely and one partially (12 of 19 cases).

## Item 20 — the shear-family front: 414 decided of 5,760 in the surviving record; one run lost

**The claim, at its approved wording**

"Of the 14,016 free-4 {0,±1} repair cases derived from the 876 wrong=1 states of Wave 56, 414 have been decided — all UNSAT (25 of the 360 instances in the completed kernel, covering the Kauers, cn97 and c88 parents). The companion kernel's run (the cn119 and cn120 instances, 8,256 cases) was lost when its interactive session ended before the results could be harvested; the partial verdicts observed during that session are unrecoverable and are **not** counted anywhere in this release. A committed re-run is queued. The shear-family front is therefore mostly undecided: 5,346 cases in the completed kernel were not attempted, and the lost kernel's 8,256 cases stand wholly undecided."

The 876 states came from the shear families of five verified
rank-23 parents (Kauers, cn119, cn120, cn97, c88 — 468 exact
shear variants, 876 distinct wrong=1 drop states). The queue
was split into two kernels by parent. The Kauers/cn97/c88
kernel completed on budget with 414 cases decided and 5,346
not attempted. The cn119/cn120 kernel was launched through an
interactive session rather than a committed run; the session
ended before its results could be harvested, the partial
verdicts seen during the session (about 45 cases) are
unrecoverable, and they are counted nowhere in this release.
A committed re-run of those 8,256 cases is queued.
