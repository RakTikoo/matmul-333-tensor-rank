# Quarters instance — FINAL status, 2026-11-22

**Instance.** Laderman's rank-22 wrong=1 state (Laderman's rank-23
scheme over ℚ with one term dropped; the remaining state has
exactly one wrong tensor entry), with terms {2,3,4} freed over the
quarter-integer coefficient set {0, ±1, ±1/2, ±1/4, ±3/4} (scaled
integers, D=4), all other terms frozen. The exhaustive split has
174 cases in 33 sign patterns (covering vectors at the wrong
entry, per the fracsplit driver).

**Final tally: 174/174 cases decided, all UNSAT. 33/33 patterns
complete. The instance is FULLY DECIDED** — no completion of the
freed triple {2,3,4} over quarter-integers exists.

## How the last cases closed

- Cases 43, 44 (pattern (48,32,16)) and 73, 74, 77, 78 (pattern
  (48,24,8)): UNSAT at 900s caps on dedicated runners (solver
  times 89.8–400.3s).
- Case 69 (pattern (48,24,8)): decided via the cross-split —
  sub-cases m=0..36 all UNSAT (m=0..27 locally, m=28..36 on
  runners).
- Case 140 (pattern (32,16,16)): decided via the cross-split —
  all 37 sub-cases m=0..36 UNSAT on runners.

## History

- Audit time (2026-11-21): 121/174 decided.
- v1.0.0 of this repository (2026-11-21): 166/174, instance open
  (snapshot preserved in `quarters-status-2026-11-21.md`).
- 2026-11-22: 174/174 — decided. This file supersedes the
  earlier status for the current tally; the earlier file remains
  as the dated record of the partial state.

All encodings were control-validated (a known-good scheme with
the same terms freed returns SAT and verifies). No SAT occurred
in any case; no candidate decomposition exists from this
instance.
