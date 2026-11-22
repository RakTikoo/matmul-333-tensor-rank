# Wave 11 — GRIND agent report (`wave11/grind/`)

**Date:** 2026-11-21. **Judge:** a result counts only if
`python3 ~/workspace/matmul-pilot/verify.py check <file>` prints
VERIFIED in a fresh process; `verify.py` was used **only** as that
black-box CLI. **Discipline held:** exactly one heavy solver process
at a time; every run capped by an EXTERNAL `timeout` wrapper
(`run_one.py`, logs wall + child CPU per run); every verdict
checkpointed immediately (per-case in `wave8/fractions/OUTCOMES.md`
by fracsplit's own logging, per-run in `wave11/grind/OUTCOMES.md`).
`wave8/fractions/fracsplit.py` was used **verbatim** for all
parity-split work (encoder control-validated in Waves 8–10: controls
SAT + fresh-process CLI VERIFIED at {0,±1}, halves and quarters).
No case already decided in Waves 8–10 was re-run.

**Headline: no new decomposition was found.** No SAT occurred in any
run; `results/wave11_333_r22_Q.json` does not exist; nothing was
added to `results/`. Yield: (i) Queue 1 completed — all 7
attempted-unknown quarters cases decided UNSAT at 900 s caps, closing
3 more patterns; (ii) a **fresh instance fully decided**: Perminov
minus-13 free-4 {3,11,13,17} in {0,±1}, 16/16 cases UNSAT;
(iii) the halves free-4 instance resisted every 240 s attempt again
(14/213 attempted cumulatively, 0 decided).

---

## Queue 1 — Quarters unknowns at 900 s: COMPLETE, 7/7 UNSAT

Instance (unchanged): Laderman wrong=1 seed
`wave4/laderman/anneal_best_r22.json`, free {2,3,4}, quarters q1
(D=4), wrong entry (8,8,8), 174 covering-parity cases / 33 patterns.
The 7 cases that were attempted-unknown at 240 s in Waves 8–10 were
re-run singly at a 900 s z3 cap (external timeout 1140 s):

| Case | Pattern | Spec | Verdict | Solver | Wall | CPU |
|---|---|---|---|---|---|---|
| 55 | (64,12,12) | [2:−12, 3:+64, 4:+12] | UNSAT | 231.2s | 233.0s | 138.2s |
| 57 | (64,12,12) | [2:+12, 3:+64, 4:−12] | UNSAT | 237.0s | 238.6s | 109.4s |
| 58 | (64,12,12) | [2:+64, 3:−12, 4:+12] | UNSAT | 286.4s | 288.9s | 170.9s |
| 59 | (64,12,12) | [2:+64, 3:+12, 4:−12] | UNSAT | 259.5s | 260.6s | 187.2s |
| 16 | (48,48,32) | [2:−32, 3:+48, 4:+48] | UNSAT | 329.0s | 330.2s | 250.5s |
| 20 | (48,48,32) | [2:+48, 3:−32, 4:+48] | UNSAT | 457.9s | 459.3s | 319.8s |
| 68 | (36,36,8) | [2:−8, 3:+36, 4:+36] | UNSAT | 416.0s | 417.8s | 259.9s |

All seven decided well inside the 900 s cap (232–458 s). Patterns
(64,12,12), (48,48,32) and (36,36,8) are thereby **fully decided**.

## Queue 2 — Quarters sweep continuation: PARTIAL (stopped at the ~55-min-remaining boundary, per brief)

One batch: pattern (64,16,16) remaining cases 46, 47, 52, 53 at
240 s caps (external bound 780 s, exit 124 — batch wall 780.0s,
CPU 456.7s):

- case 46 [2:+16, 3:−16, 4:+64]: **NO CONCLUSION** (unknown at 240 s)
- case 47 [2:+16, 3:+64, 4:−16]: **NO CONCLUSION** (unknown at 240 s)
- case 52 [2:+64, 3:−16, 4:+16]: **UNSAT in 225.0s**
- case 53: in flight at the external kill — **no verdict, undecided,
  nothing claimed**.

### Quarters instance — updated tally

**69/174 cases decided, all sound UNSAT** (61 inherited + 8 this
wave); **14/33 patterns fully decided**: (64,0,0), (64,64,64),
(32,32,0), (48,8,8), (64,1,1), (64,2,2), (64,3,3), (64,4,4),
(64,6,6), (64,8,8), (64,9,9) [W8–W10] + (64,12,12), (48,48,32),
(36,36,8) [W11]. **105 cases remain undecided**: (64,16,16) cases
46, 47 (attempted-unknown at 240 s), 53 (unrun); all of (64,18,18),
(64,24,24), (64,27,27), (64,32,32), (64,36,36), (64,48,48),
(48,12,4), (48,18,2), (48,24,8), (48,32,16), (48,16,0), (36,16,12),
(36,24,4), (36,27,1), (36,32,4), (32,16,16), (32,24,8),
(24,24,16) — unrun. The instance is **NOT decided**.

**Scope, precisely:** excluded is any quarters repair of the
Laderman wrong=1 state by rewriting terms {2,3,4} (other 19 terms
frozen) whose (8,8,8) covering-product vector lies in one of the 14
fully decided patterns. Nothing is excluded about the other 19
patterns, other free-sets, denominators > 4, or rank 22 over Q in
general. The {2,3,4} triple remains closed in {0,±1} (Wave 4) and
in halves (Wave 5); in quarters it is now closed for 14 of 33
covering patterns, and every case ever attempted in quarters is
decided except (64,16,16) cases 46/47.

## Queue 3 — Halves free-4 small patterns: PARTIAL, 0 decided

Instance: Laderman wrong=1 seed, free {2,3,4,8}, halves h1 (D=2),
213 cases / 15 patterns. All runs at 240 s caps:

- Pattern (2,2,2,2) — its single case 102 [2:+2, 3:+2, 4:+2, 8:+2]:
  **NO CONCLUSION** (unknown at 240 s; wall 241.5s, CPU 131.8s).
  The pattern is therefore NOT decided.
- Pattern (4,4,4,4) — cases 20, 34, 37: **NO CONCLUSION** each
  (unknown at 240 s; batch wall 780.1s under a 780 s external bound,
  CPU 302.6s); case 38 was in flight at the kill — **no verdict,
  undecided**. Pattern NOT decided.
- Patterns (4,4,1,1) and (4,4,2,2): **not run** — remaining wall
  time was prioritised to Queue 4 (a documented choice, made
  because 14 consecutive halves attempts across Waves 8–11 have now
  all returned unknown at 240 s, while Queue 4's instance class had
  a track record of deciding).

**Halves tally: 14/213 cases attempted cumulatively (Waves 8, 10,
11), 0 decided; no pattern fully decided; the instance is
UNDECIDED and nothing is excluded about it.** This wave confirms
Wave 8's diagnosis at two more patterns: 240 s caps do not decide
halves free-4 cases of any |product| pattern tried; the named
escalations remain ≥900 s caps (case 209's 900 s attempt was
restart-destroyed in Wave 10 and has still never completed) or the
index-8-cross split within patterns.

## Queue 4 — Fresh Perminov free-4 instance: COMPLETE, FULLY DECIDED UNSAT

Seed: `wave5/schemes/drops/perminov-cn122-minus13.json` (Perminov
cn122 minus term 13; wrong entry (0,2,2), R[e]=1, residual nnz 18).
Free-set: **{3, 11, 13, 17}** — the Wave-7 free-3 {3,11,13} (already
UNSAT, 6/6) plus term 17, chosen by support overlap with the wrong
entry's box: no remaining term reaches (0,2,2) (that is why the
entry is wrong); corner-overlap (count of U-row 0 / V-row 2 /
W-row 2 present in the term's support) maxes at 1/3, and term 17
attains it with the smallest support in the scheme (nnz 3:
supU=[1], supV=[5], supW=[2]). Coefficients {0,±1} (fracsplit set
"1"), covering-parity split = 16 cases, run in enumeration order at
240 s caps (batch wall 1389.3s, CPU 626.3s):

- Cases 0–11 (pattern (1,1,1,0)): UNSAT in 37.9–85.0 s each.
- Cases 12–15 (single-cover (1,0,0,0)): UNSAT in 119.4–231.1 s each.
- **16/16 UNSAT — the instance is DECIDED.**

**Scope, precisely:** with the other 18 terms of the Perminov
minus-13 state frozen, no rewrite of terms {3,11,13,17} with
coefficients in {0,±1} repairs the (0,2,2) entry — i.e. this
free-4 neighbourhood of that wrong=1 state contains no rank-22
{0,±1} completion. Nothing is claimed about other free-sets on
this seed, halves/quarters coefficients on this seed, other
wrong=1 states, or rank 22 over Q in general. (Integer-coefficient
rank 22 is in any case excluded by the 2026 F2 preprint cascade;
this exclusion is a local-rigidity datum in the same style as
Waves 4–8, not a step toward a global bound.)

## Totals and separation of verdicts

- **VERIFIED decompositions: none.** No SAT in any run; no file
  added to `results/`; `results/wave11_333_r22_Q.json` does not
  exist. No near-miss is reported as anything but a near-miss.
- **Sound UNSAT, instance fully decided (new):** Perminov minus-13
  free-4 {3,11,13,17} {0,±1} — 16/16 cases.
- **Sound UNSAT, case-level (quarters):** 8 new cases (cumulative
  69/174; 14/33 patterns fully decided; instance NOT decided).
- **No conclusion (unknown at cap):** quarters cases 46, 47 at
  240 s; halves cases 102, 20, 34, 37 at 240 s.
- **Interrupted / no verdict (not results):** quarters case 53 and
  halves case 38, both in flight when their batch's external bound
  fired; both remain undecided.
- **Not run (named):** quarters — case 53 and the 18 unrun patterns
  listed above (105 undecided cases total in the instance);
  halves — patterns (4,4,1,1), (4,4,2,2) and all other unattempted
  cases (199 of 213 never attempted; 14 attempted, 0 decided).

## Files

- `wave11/grind/OUTCOMES.md` — this wave's running log
  (authoritative for W11; includes the Queue-4 free-term choice
  computation).
- `wave11/grind/run_one.py` — timed single-run wrapper (external
  timeout, wall + child-CPU logging).
- Per-case verdicts: `wave8/fractions/OUTCOMES.md` under tags
  `LAD-Q1-W11-*`, `LAD-H1-W11-*`, `PERM13-F4-W11` (fracsplit's own
  append-only log).
- Nothing added to `results/`; no campaign file modified except
  the append-only `wave8/fractions/OUTCOMES.md`.
