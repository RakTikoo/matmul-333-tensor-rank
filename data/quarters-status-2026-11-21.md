# HARVEST — Actions run #2 "quarters-unrun" (matmul-compute)

- **Run:** https://github.com/RakTikoo/matmul-compute/actions/runs/44991896386 — RakTikoo/matmul-compute, workflow "compute", commit 815d677 on main, manually triggered 2026-11-21 22:01 PT.
- **Run outcome:** Completed — Success. All 47 jobs succeeded (1 setup job, 5s, + 46 matrix jobs). Total run duration shown on the run page: **15m 55s** (jobs ran in parallel). 47 warnings, all Node.js 20 deprecation notices, no failures.
- **Batch:** the 46 never-attempted cases of the quarters free-3 {2,3,4} instance (coeff q1, D=4) on the Laderman wrong=1 seed, 900s cap each (`compute-repo/batches/quarters-unrun.json`).
- **Harvested:** 2026-11-21 ~23:02 PT. All 46 artifacts (`verdict-quarters-unrun-qNNN`) downloaded individually from the run page (no download-all button in this UI) and unzipped under `compute-harvest/run2/raw/<artifact>/` (each contains `out/qNNN.log` + the job's `wave8/fractions/OUTCOMES.md`). **46/46 cases accounted for; none missing.** No `out/qNNN.json` candidate file exists in any artifact.

## Headline

- **45 UNSAT, 1 NO CONCLUSION, 0 SAT.**
- The one undecided case is **Q140** (pattern (32,16,16)): `NO CONCLUSION (unknown at 900s cap, wall 900.0s)` — evidence line from `raw/verdict-quarters-unrun-q140/out/q140.log`: "Q140 case 140/173 [2:+16,3:+32,4:+16]: NO CONCLUSION (unknown at 900s cap, wall 900.0s)".
- **No SAT occurred** — no candidate rank-22 decomposition in this batch; nothing to verify.
- **New instance tally: 166/174 cases decided, all UNSAT** (was 121/174; +45).
- **Patterns fully decided: 30/33** (was 23/33; +7 — see pattern table).
- Still open (8 cases): 43, 44 (pattern (48,32,16), attempted-unknown locally), 69, 73, 74, 77, 78 (pattern (48,24,8), attempted-unknown locally), and 140 (pattern (32,16,16), unknown at 900s on the runner).
- **Runner time:** sum of per-job wall times from the log start/end timestamps = 3,685s ≈ **61.4 runner-minutes** (solver time alone 3,672.3s ≈ 61.2 min; per-job overhead is seconds). Against the 2,000 Linux min/month Free-plan pool, this batch cost roughly 61 minutes plus the 28s smoke run.

## Per-case results

| Case | Pattern | Covering vector [2,3,4] | Verdict | Solver time |
|---|---|---|---|---|
| Q48 | (48, 32, 16) | [2:+32, 3:-16, 4:+48] | UNSAT | 282.3s |
| Q49 | (48, 32, 16) | [2:+32, 3:+48, 4:-16] | UNSAT | 254.2s |
| Q50 | (48, 32, 16) | [2:+48, 3:-16, 4:+32] | UNSAT | 183.5s |
| Q51 | (48, 32, 16) | [2:+48, 3:+32, 4:-16] | UNSAT | 359.8s |
| Q88 | (36, 32, 4) | [2:-4, 3:+32, 4:+36] | UNSAT | 28.8s |
| Q89 | (36, 32, 4) | [2:-4, 3:+36, 4:+32] | UNSAT | 20.0s |
| Q93 | (36, 32, 4) | [2:+32, 3:-4, 4:+36] | UNSAT | 24.2s |
| Q94 | (36, 32, 4) | [2:+32, 3:+36, 4:-4] | UNSAT | 37.5s |
| Q95 | (36, 32, 4) | [2:+36, 3:-4, 4:+32] | UNSAT | 118.0s |
| Q96 | (36, 32, 4) | [2:+36, 3:+32, 4:-4] | UNSAT | 20.7s |
| Q123 | (36, 27, 1) | [2:+1, 3:+27, 4:+36] | UNSAT | 1.7s |
| Q124 | (36, 27, 1) | [2:+1, 3:+36, 4:+27] | UNSAT | 1.5s |
| Q126 | (36, 24, 4) | [2:+4, 3:+24, 4:+36] | UNSAT | 2.0s |
| Q127 | (36, 24, 4) | [2:+4, 3:+36, 4:+24] | UNSAT | 1.7s |
| Q130 | (32, 24, 8) | [2:+8, 3:+24, 4:+32] | UNSAT | 1.1s |
| Q131 | (32, 24, 8) | [2:+8, 3:+32, 4:+24] | UNSAT | 21.7s |
| Q134 | (36, 16, 12) | [2:+12, 3:+16, 4:+36] | UNSAT | 1.9s |
| Q135 | (36, 16, 12) | [2:+12, 3:+36, 4:+16] | UNSAT | 16.2s |
| Q137 | (36, 16, 12) | [2:+16, 3:+12, 4:+36] | UNSAT | 1.9s |
| Q138 | (32, 16, 16) | [2:+16, 3:+16, 4:+32] | UNSAT | 2.0s |
| Q139 | (24, 24, 16) | [2:+16, 3:+24, 4:+24] | UNSAT | 9.4s |
| Q140 | (32, 16, 16) | [2:+16, 3:+32, 4:+16] | NO CONCLUSION | 900.0s cap (unknown) |
| Q141 | (36, 16, 12) | [2:+16, 3:+36, 4:+12] | UNSAT | 218.8s |
| Q142 | (36, 24, 4) | [2:+24, 3:+4, 4:+36] | UNSAT | 56.2s |
| Q143 | (32, 24, 8) | [2:+24, 3:+8, 4:+32] | UNSAT | 286.9s |
| Q144 | (24, 24, 16) | [2:+24, 3:+16, 4:+24] | UNSAT | 21.2s |
| Q145 | (24, 24, 16) | [2:+24, 3:+24, 4:+16] | UNSAT | 66.9s |
| Q146 | (32, 24, 8) | [2:+24, 3:+32, 4:+8] | UNSAT | 1.9s |
| Q147 | (36, 24, 4) | [2:+24, 3:+36, 4:+4] | UNSAT | 86.7s |
| Q148 | (36, 27, 1) | [2:+27, 3:+1, 4:+36] | UNSAT | 1.6s |
| Q149 | (36, 27, 1) | [2:+27, 3:+36, 4:+1] | UNSAT | 8.2s |
| Q150 | (32, 24, 8) | [2:+32, 3:+8, 4:+24] | UNSAT | 8.3s |
| Q151 | (32, 16, 16) | [2:+32, 3:+16, 4:+16] | UNSAT | 1.3s |
| Q152 | (32, 24, 8) | [2:+32, 3:+24, 4:+8] | UNSAT | 8.6s |
| Q153 | (36, 27, 1) | [2:+36, 3:+1, 4:+27] | UNSAT | 1.9s |
| Q154 | (36, 24, 4) | [2:+36, 3:+4, 4:+24] | UNSAT | 70.5s |
| Q155 | (36, 16, 12) | [2:+36, 3:+12, 4:+16] | UNSAT | 392.8s |
| Q156 | (36, 16, 12) | [2:+36, 3:+16, 4:+12] | UNSAT | 75.0s |
| Q157 | (36, 24, 4) | [2:+36, 3:+24, 4:+4] | UNSAT | 67.7s |
| Q158 | (36, 27, 1) | [2:+36, 3:+27, 4:+1] | UNSAT | 1.2s |
| Q162 | (48, 16, 0) | [2:+0, 3:+16, 4:+48] | UNSAT | 0.8s |
| Q164 | (48, 16, 0) | [2:+0, 3:+48, 4:+16] | UNSAT | 0.7s |
| Q165 | (48, 16, 0) | [2:+16, 3:+0, 4:+48] | UNSAT | 0.9s |
| Q166 | (48, 16, 0) | [2:+16, 3:+48, 4:+0] | UNSAT | 1.2s |
| Q169 | (48, 16, 0) | [2:+48, 3:+0, 4:+16] | UNSAT | 1.6s |
| Q170 | (48, 16, 0) | [2:+48, 3:+16, 4:+0] | UNSAT | 1.3s |

## Pattern tally

| Pattern | Cases in this batch | Batch result | Pattern status after harvest |
|---|---|---|---|
| (48, 32, 16) | Q48, Q49, Q50, Q51 | 4 UNSAT | NOT fully decided — cases 43, 44 still open (attempted-unknown locally) |
| (36, 32, 4) | Q88, Q89, Q93, Q94, Q95, Q96 | 6 UNSAT | **Fully decided** (all 6 cases now UNSAT) |
| (36, 27, 1) | Q123, Q124, Q148, Q149, Q153, Q158 | 6 UNSAT | **Fully decided** (all 6 cases now UNSAT) |
| (36, 24, 4) | Q126, Q127, Q142, Q147, Q154, Q157 | 6 UNSAT | **Fully decided** (all 6 cases now UNSAT) |
| (32, 24, 8) | Q130, Q131, Q143, Q146, Q150, Q152 | 6 UNSAT | **Fully decided** (all 6 cases now UNSAT) |
| (36, 16, 12) | Q134, Q135, Q137, Q141, Q155, Q156 | 6 UNSAT | **Fully decided** (all 6 cases now UNSAT) |
| (32, 16, 16) | Q138, Q140, Q151 | 2 UNSAT, 1 no conclusion | NOT fully decided — Q140 unknown at 900s (Q138, Q151 UNSAT) |
| (24, 24, 16) | Q139, Q144, Q145 | 3 UNSAT | **Fully decided** (all 3 cases now UNSAT) |
| (48, 16, 0) | Q162, Q164, Q165, Q166, Q169, Q170 | 6 UNSAT | **Fully decided** (all 6 cases now UNSAT) |

Case→pattern map per `wave15/five/REPORT.md` §2, cross-checked against each log's covering vector (pattern = sorted absolute values of the vector). Pattern case-counts: (48,32,16) has 6 cases total (43, 44, 48–51); (32,16,16) and (24,24,16) have 3 each; the other six patterns above have 6 each — for those six plus (48,16,0), the cases in this batch were the pattern's only undecided cases, so an all-UNSAT batch completes the pattern.

## Notes

- Verdict parsing was word-boundary safe (the Wave 12 "SAT in" ⊂ "UNSAT in" parser bug does not apply); every verdict above was read from the case's own `fracsplit` log line.
- Runner speed note: cases that took minutes of wall time on this VM decided in seconds–minutes on the dedicated runners (e.g. Q155 UNSAT in 392.8s solver time at full CPU; most small patterns in <10s). Q140 is the batch's one genuinely hard case at the 900s cap.
- No new workflow runs were dispatched during this harvest. The canonical `wave8/fractions/OUTCOMES.md` was not edited; these verdicts live only here.
