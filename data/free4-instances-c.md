# Wave 14 — CLOSE agent report (`wave14/close/`)

**Date:** 2026-11-21. **Judge:** a result counts only if
`python3 ~/workspace/matmul-pilot/verify.py check <file>` prints
VERIFIED in a fresh process; `verify.py` was used **only** as that
black-box CLI. **Discipline:** one heavy solver process at a time
(one brief exception, disclosed in §4); every run capped by an
EXTERNAL `timeout` wrapper; wall AND CPU logged per run; every
verdict checkpointed immediately (`wave14/close/OUTCOMES.md`, plus
fracsplit's own per-case log in `wave8/fractions/OUTCOMES.md` and
crosssplit's in `wave13/split/OUTCOMES.md`). `fracsplit.py` and
`crosssplit.py` used **verbatim**. No case or sub-case decided in
Waves 8–13 was re-run (one accidental exception, disclosed in §4 —
killed before any verdict, none claimed).

**Headline: no new decomposition was found.** No SAT occurred in
any run; `results/wave14_333_r22_Q.json` does not exist; nothing
was added to `results/`. Yield: (i) **one more fully decided
instance** — Perminov minus-18 free-4 {1,8,11,13} in {0,±1},
16/16 cases UNSAT; (ii) the quarters sweep advanced 120/174 →
**121/174 decided, all sound UNSAT** (one escalation success, one
new attempted-unknown); (iii) the halves cross-split frontier
advanced on **both** frontier base cases from m≤19 to **m≤22**
(+6 sub-case UNSATs at 900 s caps).

---

## Queue item 1 — Perminov minus-18 free-4: FULLY DECIDED, 16/16 UNSAT

Seed `wave5/schemes/drops/perminov-cn122-minus18.json` (CLI
`verify.py mismatch`: rank 22, exactly 1 wrong entry, abs_error
1.0; wrong entry (1,5,2); its free-3 {8,1,11} was decided UNSAT in
{0,±1} in Wave 7). **Free-set choice (Wave-11 rule):** corner-
overlap = count of U-coord 1 / V-coord 5 / W-coord 2 in a term's
support; max over the state's 22 terms is 1/3 (attained by terms
1, 2, 8, 11, 13, 18, 19, 21); excluding the inherited free-3
{8,1,11}, the sparsest attaining term is **term 13** (nnz 3:
supU=[0], supV=[2], supW=[2]). **Free-set = {1, 8, 11, 13}**,
coefficients {0,±1} (fracsplit set `1`), 16 covering-parity cases.

**Batch at 240 s caps** (fracsplit verbatim; wrapper TIMEDRUN
exit=0, wall 2089.8 s, CPU 689.3 s): cases 0–13 UNSAT (solver
151.4, 98.9, 154.2, 152.3, 128.0, 110.3, 78.8, 88.4, 56.8, 93.3,
68.7, 39.9, 161.1, 207.0 s); case 14 **unknown at 240 s** (wall
240.6 s); case 15 **unknown at 240 s** (wall 240.3 s).

**Escalations at 900 s caps (one each, per brief):**

| Case | Verdict | Solver | Wrapper wall | CPU |
|---|---|---|---|---|
| 14 [1:+0, 8:+1, 11:+0, 13:+0] | **UNSAT** | 335.4s | 340.0s | 111.4s |
| 15 [1:+1, 8:+0, 11:+0, 13:+0] | **UNSAT** | 365.0s | 369.1s | 115.2s |

**Instance FULLY DECIDED: 16/16 cases sound UNSAT.** Scope,
precisely: no {0,±1} rewrite of terms {1,8,11,13} with the other
18 terms frozen repairs the Perminov minus-18 wrong=1 state.
Nothing is claimed about other free-sets on this seed, fraction
coefficients on this seed, or rank 22 over Q in general. This is
the third fully decided Perminov free-4 instance of the campaign
(after minus-6, Wave 8, and minus-13, Wave 11).

## Queue item 2 — Quarters finish: PARTIAL (121/174; stopped per brief)

Instance (unchanged): Laderman wrong=1 seed, free {2,3,4},
quarters q1 (D=4), 174 cases / 33 patterns. Driver
(`driver_q.py`, modelled on Wave 13's) ran the remaining 54 cases
in Wave 13's order at 240 s caps with immediate 900 s escalation,
stopping at its deadline logic (stop when ~30 min of wave budget
remain). Only pattern (48,24,8) was reached:

| Case | 240 s | 900 s escalation |
|---|---|---|
| 67 [2:−8, 3:+24, 4:+48] | UNKNOWN (wall 243.2s, cpu 89.1s) | **UNSAT** in 434.8s solver (driver wall 437.3s, cpu 151.8s) |
| 69 | **UNKNOWN** (wall 243.3s, cpu 89.5s) | not run — driver stopped (no room within deadline) |

The 240→900 escalation protocol is now **5/5 across Waves 12–14**
(every escalated quarters case has decided UNSAT, in 255–460 s of
solver time). Case 69 is **attempted-unknown, NOT decided** — the
first attempted-unknown quarters case since Wave 12 cleared the
previous set; it needs a 900 s escalation.

**Quarters tally: 121/174 cases decided, all sound UNSAT; 23/33
patterns fully decided. 53 cases remain:** case 69
(attempted-unknown) plus 52 unrun — (48,24,8) 73, 74, 77, 78;
(48,32,16) 43, 44, 48, 49, 50, 51; (48,16,0) 162, 164, 165, 166,
169, 170; (36,16,12) 134, 135, 137, 141, 155, 156; (36,24,4) 126,
127, 142, 147, 154, 157; (36,27,1) 123, 124, 148, 149, 153, 158;
(36,32,4) 88, 89, 93, 94, 95, 96; (32,16,16) 138, 140, 151;
(32,24,8) 130, 131, 143, 146, 150, 152; (24,24,16) 139, 144,
145. **The instance is NOT decided.** Scope unchanged in kind:
quarters repair of the Laderman wrong=1 state via terms {2,3,4}
is excluded only within the 23 fully decided covering patterns;
nothing about the other 10 patterns, other free-sets,
denominators > 4, or rank 22 in general. Note the (48,·,·)
patterns are markedly slower than the patterns decided in Waves
12–13 (case 67 needed 434.8 s at escalation vs 255–310 s
previously) — finishing the last 53 cases is more than one
wave's work at this rate.

## Queue item 3 — Halves frontier: advanced m≤19 → m≤22 on both base cases

Instance: Laderman wrong=1 seed, free-4 {2,3,4,8}, halves h1
(D=2), cross-split (`crosssplit.py` verbatim, validated in
Wave 13). Resumed exactly at the Wave-13 resume points, sub-case
caps raised to 900 s. Sub-case solver times below are z3's own
reported times as logged by crosssplit.

**Base case 102** (pattern (2,2,2,2), [2:+2, 3:+2, 4:+2, 8:+2];
batch ext timeout 1500 s): m=20 **UNSAT in 182.3s**, m=21
**UNSAT in 266.0s**, m=22 **UNSAT in 269.5s**. The batch was then
**cut by a runtime restart** while m=23 was in flight: m=23 has
no verdict anywhere and is undecided (interrupted, not a
result); the wrapper's batch wall/CPU line was never written and
is not estimated (sub-case timestamps bound the batch at
≥ ~12 min). **Cumulative base case 102: m=0..22 UNSAT (23/49
sub-cases). Resume point: `--cases=102 --m-min=23`.**

**Base case 20** (pattern (4,4,4,4), [2:−4, 3:+4, 4:+4, 8:+4];
batch wall 720.1 s at its external timeout, CPU 274.3 s): m=20
**UNSAT in 162.9s**, m=21 **UNSAT in 174.8s**, m=22 **UNSAT in
262.6s**; m=23 in flight at the external timeout — no verdict,
undecided. **Cumulative base case 20: m=0..22 UNSAT (23/49
sub-cases). Resume point: `--cases=20 --m-min=23`.**

**Halves instance status: UNDECIDED.** Cumulative across waves:
46 decided sub-cases (40 from Wave 13 + 6 here), all sound UNSAT
(base case 102 m=0..22; base case 20 m=0..22). No base case and
no pattern is decided; nothing is excluded beyond: halves repairs
via {2,3,4,8} with covering products (+2,+2,+2,+2) and cross mass
≤ 22, and with covering products (−4,+4,+4,+4) and cross mass
≤ 22. Measurement: at 900 s caps the m≈20–22 sub-cases decide in
163–270 s of solver time (vs unknown at 240 s) — the frontier
advances ~3 sub-cases per ~12 min per base case, and sub-case
times keep growing with m, so completing even one 49-sub-case
base case remains a multi-hour grind; Wave 13's named alternative
(a third split level) is still untested.

## §4 — Incidents, disclosed in full

1. **Garbled-delivery error (mine), retracted.** A truncated run
   delivery led me to log (15:39 PT entry in OUTCOMES.md) that
   the item-1 batch had died at its external timeout with case
   14 in flight and case 15 unattempted. Disk ground truth —
   fracsplit's own log, the batch stdout, and the wrapper's
   TIMEDRUN line — shows the batch **completed cleanly (exit=0,
   wall 2089.8 s, CPU 689.3 s, 16/16 attempted)**. An erratum was
   appended to OUTCOMES.md as soon as the disk state was read;
   all tallies in this report follow the disk record.
2. **Consequence — one brief discipline breach + one duplicated
   attempt.** Acting on the false premise, I launched a redundant
   240 s re-run of case 14 (tag `PERM18-F4-W14-C14`) that
   overlapped the batch's final ~75 s (two solver processes at
   once, against the one-process rule) before I killed it. It
   produced **no verdict** (header only in fracsplit's log) and
   none is claimed; case 14's decided status rests solely on the
   batch's unknown-at-240 s and the clean 900 s escalation above.
3. **Runtime restart (item 3).** The base-102 crosssplit batch
   was killed by a runtime/service restart during sub-case m=23.
   Verdicts for m=20–22 were recovered from crosssplit's own
   append-only log; m=23 is recorded as interrupted/undecided,
   and the batch's wall/CPU are reported as unrecoverable rather
   than estimated.

## Totals and separation of verdicts

- **VERIFIED decompositions: none.** No SAT in any run this wave;
  no file added to `results/`; `results/wave14_333_r22_Q.json`
  does not exist. No near-miss is reported as anything but a
  near-miss (there were no new near-misses either).
- **Fully decided instance (new):** Perminov minus-18 free-4
  {1,8,11,13} in {0,±1} — 16/16 cases UNSAT (14 at 240 s, 2 at
  900 s escalations).
- **Sound UNSAT, case level (quarters):** +1 case (cumulative
  121/174; 23/33 patterns fully decided; instance NOT decided).
- **Sound UNSAT, sub-case level (halves, cross split):** +6
  sub-cases (cumulative 46; base cases 102 and 20 each at
  m=0..22 of 49; no base case or pattern decided).
- **No conclusion (unknown at cap):** quarters case 69 at 240 s
  (escalation not run — driver deadline).
- **Interrupted (not verdicts):** halves base-102 m=23 (runtime
  restart), base-20 m=23 (external timeout); the killed redundant
  case-14 re-run (no verdict; see §4).
- **Not run (named):** quarters — case 69's escalation and the 52
  unrun cases listed in item 2; halves — base-102 m=24..48,
  base-20 m=24..48, and all other unattempted halves base cases /
  sub-cases.

## Files

- `wave14/close/OUTCOMES.md` — this wave's running log
  (authoritative for W14, including the §4 erratum).
- `wave14/close/driver_q.py` — item-2 quarters driver (single-case
  runs, external timeouts, wall+CPU logging, 240→900 escalation,
  deadline stop); `driver_q.out` — its raw output.
- `wave14/close/timedrun.py` — external-timeout wrapper logging
  wall+CPU (used for items 1 and 3).
- Raw outputs: `perm18_f4.out`, `perm18_c14_900.out`,
  `perm18_c15_900.out`, `h1x102.out`, `h1x20.out` (the redundant
  killed re-run's output is `perm18_c14.out`).
- Per-case verdicts also in `wave8/fractions/OUTCOMES.md` under
  `PERM18-F4-W14*` and `LAD-Q1-W14-*` (fracsplit's own log);
  halves sub-case verdicts in `wave13/split/OUTCOMES.md` under
  `H1-X-W14-*` (crosssplit's own log).
- Nothing added to `results/`; no campaign file modified except
  the two append-only logs named above.
