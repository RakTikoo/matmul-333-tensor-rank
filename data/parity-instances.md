# Wave 7 — PARITY-SWEEP report (`wave7/parity/`)

**Date:** 2026-11-21. **Agent:** parity-sweep, Wave 7. **Judge:** a
result counts only if `python3 ~/workspace/matmul-pilot/verify.py
check <file>` prints VERIFIED in a fresh process; `verify.py` was used
**only** as that black-box CLI (never imported — all tensor arithmetic
below is this agent's own code, cross-checked against the CLI's
mismatch counts).

**Headline: no new decomposition was found** — no SAT case occurred in
93 decided cases, and `results/wave7_333_r22_Q.json` does not exist.
**Yield: three term-freeing instances DECIDED soundly UNSAT** (one
Laderman free-4 set never tried before, and both remaining Perminov
wrong=1 drops at free-3), **plus 60 further case-level UNSATs** across
five more instances that remain formally undecided only because a
handful of cases hit their caps or were not reached inside the wall
budget. The covering-parity split again decided in ~1–2 minutes per
case what raw z3 left unknown at 600–1800s in earlier waves.

---

## Method (generalised from Wave 6) and exhaustiveness

`paritysplit.py` generalises `wave6/deepexact/casesplit.py` to any
seed / free-set / coefficient set in {`1`, `h1`}, reusing
`wave5/exact/termfree.py`'s scaled-integer encoding verbatim (D = lcm
of seed and coefficient denominators; freed entries range over the
finite set A; residual R = D³·T − Σ frozen).

**Split.** Let e be the seed's unique wrong entry (have 0 / want 1;
asserted in code for every instance). In any solution of the full
instance, the e-equation reads Σ_{t∈free} U_t[e₀]·V_t[e₁]·W_t[e₂] =
R[e], where each summand lies in the finite product set P = {a·b·c :
a,b,c ∈ A}. The cases are **all** vectors v ∈ P^free with Σv = R[e],
each case adding the constraints prod_t(e) = v_t to the full
729-equation instance:

- **Disjoint:** a solution's covering-product vector is a single
  well-defined vector, so it satisfies exactly one case's constraints.
- **Exhaustive:** every solution has some covering-product vector,
  which by the e-equation sums to R[e], hence is one of the enumerated
  cases. UNSAT on all cases ⇒ sound UNSAT of the instance (this
  free-set + coefficient set, rest frozen — nothing more is claimed).

For {0,±1} (P = {−1,0,1}, R[e] = +1) this reproduces Wave 6's split
exactly: free-4 → 16 cases (12 triple-cover with signs (+,+,−), 4
single-cover (+1)); free-3 → 6 cases. Cases were run most-pinned first
(triple-cover before single-cover — Wave 6's evidence that they decide
fastest). For halves {0,±1/2,±1} (D = 2, A = {0,±1,±2}, P =
{0,±1,±2,±4,±8}, R[e] = 8) the enumeration gives **213 cases** for a
free-4 set — by construction exhaustive, but see item 4 below.

## Pre-flight validation (before any solver output was trusted)

1. **Seed scores reproduced** (CLI `mismatch`, fresh processes): all
   four seeds 1/729 wrong, abs_error 1.0 — exactly as handed over.
2. **Anatomy re-derived** (`prep.py`, own arithmetic): Perminov
   minus-6 seed = Perminov parent minus term 6, wrong entry (5,8,5);
   minus-13: wrong entry **(0,2,2)**, touchers U{13,16} V{3,19}
   W{11,17}; minus-18: wrong entry **(1,5,2)**, touchers U{8,18}
   V{1,2,19,21} W{11,13}; Laderman seed wrong entry (8,8,8), as known.
3. **Encoder controls.** (a) `termfree.py` free-(0,1) on Lens C's
   verified rank-26, {0,±1}: SAT 1.1s, fresh-process CLI **VERIFIED**
   (`control_r26.json`, control artefact). (b) Parity-split controls
   on a padded Laderman seed (verified rank-23 with term 2 zeroed;
   CLI mismatch 1/729): free-{2} has exactly 1 case [2:+1] → **SAT**,
   assembled file CLI **VERIFIED** (restores Laderman — control
   artefact, `control_padded_f1.json`); free-{2,3} → **SAT** in case
   [2:+0,3:+1], CLI **VERIFIED** (`control_padded_f2.json`). The split
   constraints therefore admit genuine solutions, and the shared
   encoding core is the control-validated one. (An earlier free-{2}
   attempt on the *unpadded* wrong=1 seed returned UNSAT in 0.1s; that
   is mathematically correct there — one rank-1 term cannot equal a
   line-term box plus the disjoint unit entry — and is what prompted
   the padded-seed control design.)
4. **Enumeration cross-check:** `--list` on Wave 6's instance
   (Laderman {2,3,4,8}, {0,±1}) enumerates exactly Wave 6's 16 cases.

---

## Queue item 1 — Perminov wrong=1, free-4 {14,3,2,21}, {0,±1}

Seed `wave5/schemes/drops/anneal_best_r22.json`, e = (5,8,5), residual
nnz 91. (Raw z3 was unknown at 600s in Wave 6.) 16 cases:

- Triple-cover (12 cases, cap 150s): **all UNSAT**, 20.0–59.9s each.
- Single-cover (4 cases, cap 240s): case [21:+1] **UNSAT 88.3s**,
  case [14:+1] **UNSAT 119.5s**; case [3:+1] **NO CONCLUSION**
  (unknown at 240s); case [2:+1] **NO CONCLUSION** (unknown at 240s).

**Instance status: UNDECIDED** — 14/16 cases soundly UNSAT; the two
single-cover cases where the covering term is a W-toucher (term 2) or
a V-toucher (term 3) resisted the 240s cap. Next escalation: retry
those two cases at ≥600s, or add Wave 6's level-2 cross split.

## Queue item 2 — Laderman wrong=1, free-4 sets, {0,±1}

Seed `wave4/laderman/anneal_best_r22.json`, e = (8,8,8), residual
nnz 29 (31 for the mixed set). Line terms {2,3,4,8,9,13}.

| Instance | Triple-cover (12) | Single-cover (4) | Status |
|---|---|---|---|
| {2,3,4,9} (cap 150/240s) | 12 UNSAT, 25.4–47.1s | 4 UNSAT, 118.1–155.6s | **DECIDED UNSAT (16/16)** |
| {2,8,9,13} (cap 100s) | 12 UNSAT, 20.0–42.2s | not run | undecided (12/16) |
| {3,4,9,13} (cap 100s) | 12 UNSAT, 22.0–72.4s | not run | undecided (12/16) |
| {2,3,8,9} (cap 100s) | 11 UNSAT, 30.1–99.7s; case 9 [9:−1 pattern] NO CONCLUSION at 100s | not run | undecided (11/16) |
| mixed {2,3,4,5} (cap 100s) | 11 UNSAT, 61.0–91.6s; case 3 NO CONCLUSION at 100s | not run | undecided (11/16) |

The mixed set {2,3,4,5} (3 line + dense seed-5, Laderman term [6])
was chosen by contributor analysis in `prep.py`: its dense term's
contribution box overlaps the line triple's union box in 9 entries —
the maximum over all 20 (3-line + 1-dense) candidates — with the
smallest residual (nnz 31).

**Net for item 2:** one more Laderman free-4 set fully closed
({2,3,4,9}); together with Wave 6's {2,3,4,8}, the two most natural
line-term free-4 sets around (8,8,8) are now decided. The remaining
sets' triple-cover halves are all (but two cases) excluded; their
single-cover cases were not reached inside the budget.

## Queue item 3 — Perminov minus-13 and minus-18, free-3 {0,±1}

One toucher per factor, parity split (6 cases each, cap 120s):

| Instance | Cases | Status |
|---|---|---|
| minus-13, free {13,3,11}, e=(0,2,2), nnz 18 | 6 UNSAT, 0.8–1.8s each | **DECIDED UNSAT (6/6)** |
| minus-18, free {8,1,11}, e=(1,5,2), nnz 41 | 6 UNSAT, 0.8–1.8s each | **DECIDED UNSAT (6/6)** |

Both remaining Perminov wrong=1 drops are now closed against
one-toucher-per-factor free-3 rewrites in {0,±1} (mirroring Wave 5's
free-2/3 closures on the minus-6 state). The follow-on free-4 on each
was **not attempted** — the wall budget was consumed by item 2's
41-minute four-set batch under CPU contention.

## Queue item 4 — Laderman {2,3,4,8} in halves — NOT RUN

The split was derived and enumerated: D = 2, scaled products in
{0,±1,±2,±4,±8} must sum to R[e] = 8, giving **213 disjoint,
exhaustive cases** (`paritysplit.py … h1 --list`). No case was solved:
unlike the {0,±1} split (16 cases), 213 cases × ~1–2 min is a
multi-hour run, so the method does **not** "stay cheap" in halves at
free-4 without a further split level (e.g. splitting first on the
multiset of |products|, or on a second entry's parity). Recorded as
the named next step, not attempted.

---

## Totals and separation of verdicts

- **VERIFIED decompositions: none.** No file added to `results/`.
- **Sound UNSAT (complete instances, encoder control-validated, split
  exhaustive as proved above):** Laderman free-4 {2,3,4,9} {0,±1}
  (16/16 cases, ~15.3 solver-min); Perminov minus-13 free-3 {13,3,11}
  {0,±1} (6/6, ~8s); Perminov minus-18 free-3 {8,1,11} {0,±1} (6/6,
  ~7s). Scope of each: that free-set and coefficient set only, all
  other terms frozen.
- **Case-level UNSATs in undecided instances:** Perminov minus-6
  free-4 {14,3,2,21}: 14/16. Laderman {2,8,9,13}: 12/16;
  {3,4,9,13}: 12/16; {2,3,8,9}: 11/16; mixed {2,3,4,5}: 11/16.
- **No conclusion:** Perminov minus-6 cases [3:+1] and [2:+1]
  (unknown at 240s); Laderman {2,3,8,9} case 9 and mixed {2,3,4,5}
  case 3 (unknown at 100s); all single-cover cases of the last four
  Laderman sets (not run); Perminov minus-13/18 free-4 (not run);
  halves free-4 (enumerated only, 213 cases).
- **Case tally:** 93 cases decided (88 sweep UNSAT + 2 control SAT +
  3 control-side lines), 4 unknown at cap, all logged per-case in
  `OUTCOMES.md` as they finished. Total solver time ≈ 95 min across
  ~100 min wall (VM CPU contention from parallel campaigns inflated
  the last batch).

## Files

- `paritysplit.py` (generalised split solver; exhaustiveness argument
  in its docstring), `prep.py` (anatomies + mixed-set scoring),
  `termfree.py` (copied unchanged from `wave5/exact/`),
  `OUTCOMES.md` (running per-case log — the authoritative record).
- Controls (artefacts, **not** results): `control_r26.json`,
  `control_padded_seed.json`, `control_padded_f1.json`,
  `control_padded_f2.json`.
- Nothing added to `results/`; campaign files untouched.

## Suggested next steps (for the coordinator)

1. Finish the near-closed instances first — they are each ≤4 cases
   from decided: Perminov minus-6 cases [3:+1]/[2:+1] at ≥600s (or
   with the level-2 cross split); the 16 single-cover cases of the
   four Laderman sets at ~240s each (≈35–65 solver-min total based on
   this wave's single-cover timings); the two 100s-cap unknowns at
   240s.
2. Perminov minus-13/18 free-4 (toucher sets + one extra toucher)
   via the same split — free-3 fell in seconds, so these are the
   cheapest undecided instances left in the Perminov basins.
3. Halves free-4 needs a coarser first split level before the
   213-case enumeration is practical: split on the |product| multiset
   pattern (few dozen patterns), then on assignments within a
   pattern.
