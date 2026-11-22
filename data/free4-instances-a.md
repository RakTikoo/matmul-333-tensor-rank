# Wave 6 — DEEP-EXACT report (`wave6/deepexact/`)

**Date:** 2026-11-21. **Agent:** deep-exact, Wave 6. **Judge:** a result
counts only if `python3 ~/workspace/matmul-pilot/verify.py check <file>`
prints VERIFIED in a fresh process; `verify.py` was used **only** as
that black-box CLI (never imported — all tensor arithmetic below is
this agent's own code, cross-checked against the CLI's mismatch
counts).

**Headline: no new decomposition was found** — no file was added to
`results/` by this agent (`results/wave6_333_r22_Q.json` and
`results/wave6_333_r24_Q.json` do not exist). **Main yield: the
campaign's sharpest undecided instance is now DECIDED.** The free-4
{2,3,4,8} {0,±1} term-freeing instance on the Laderman wrong=1 rank-22
state — unknown to a single z3 run at 600s (Wave 4) and at the full
1800s cap (Wave 5) — is **soundly UNSAT**, proved by an exhaustive
16-case decomposition: every case decided, total solver time ~26 min.
Plus queue outcomes on the Perminov wrong=1 state and the r24 seed
(below).

---

## Pre-flight validation (before any solver output was trusted)

1. **Seed score reproduced** (CLI `mismatch`, fresh process): Laderman
   wrong=1 seed (`wave4/laderman/anneal_best_r22.json`) 1/729 wrong,
   abs_error 1.0 — exactly as handed over.
2. **Encoder control.** Freeing terms (0,1) of Lens C's verified
   rank-26 scheme with {0,±1} via this session's copy of `termfree.py`:
   **SAT in 1.0s**, assembled file self-checks 0/729, fresh-process CLI
   prints `VERIFIED {... "rank": 26, "wrong_entries": 0, ...}`
   (`wave6/deepexact/control_r26.json` — a control artefact, **not** a
   new result). The case-split solver (`casesplit.py`) uses the
   identical encoding core (same residual construction, same
   Or-of-equalities domain constraints, same 729 cubic equations), so
   every UNSAT below inherits this validation.
3. **Instance anatomy re-derived** (`prep.py`, own arithmetic): the
   seed is Laderman's rank-23 **minus term 2** (the unit term
   e₈⊗e₈⊗e₈, all entries +1) — confirmed entrywise against
   `results/wave4_333_r23_Q_laderman.json`. Its only wrong entry is
   (8,8,8): have 0, want 1. The freed seed terms {2,3,4,8} are Laderman
   [3],[4],[5],[9] — four "line" terms, each with one dense factor
   supported on {0,2,4,5,6,7,8} and two unit factors. The residual
   R = T − (frozen 18 terms) has nnz 29 and R[8,8,8] = +1 (asserted in
   code). Residual entries with an 8-coordinate, all +1: (2,8,2),
   (5,8,5), (7,5,8), (8,7,7), (8,8,8).

## Main target — case-split of free-4 {2,3,4,8}, {0,±1}: DECIDED UNSAT

**The split.** In any solution of the raw instance, the (8,8,8)
equation reads

  Σ_{t ∈ {2,3,4,8}} U_t[8]·V_t[8]·W_t[8] = R[8,8,8] = +1,

where each summand lies in {−1, 0, +1} (entries are in {0,±1}). Call a
term **covering** if its summand is nonzero. The number k of covering
terms must make a sum of k values of ±1 equal +1, so **k is odd**:
k = 1 (the single summand is +1) or k = 3 (signs +, +, −). k ∈ {0, 2, 4}
is arithmetically impossible. This gives 16 pairwise-disjoint cases
whose union is the whole instance:

- **A⟨t⟩** (4 cases): exactly term t covers, with product +1; each
  other freed term misses (8,8,8) (at least one of its U[8], V[8],
  W[8] is 0).
- **B⟨e⟩n⟨n⟩** (12 cases): term e does not cover; of the remaining
  three, term n has product −1 and the other two have product +1.

**Index-8-line refinement (defined, not needed).** The brief's
level-2 split was implemented (`casesplit.py --cross m`): with the
index-8 cross C = {2,5,6,7,8} (row 2 ∪ column 2 of the 3×3 grid; a
covering term has 8 ∈ supp of all three factors), split by the total
off-centre cross mass m = Σ over covering terms and factors of
|supp(F_t) ∩ {2,5,6,7}|, sparsest first. **It was never needed** —
every level-1 case decided inside its cap, so no case required the
pattern refinement. (The A-case UNSATs therefore already exclude all
cross patterns for single-cover solutions, and likewise for B.)

**Results** (z3, one fresh solver per case; caps 300s for A, 240s
for B; all outcomes logged per-case in `OUTCOMES.md` as they landed):

| Case | Covering structure | Outcome |
|---|---|---|
| A2 | only seed term 2, product +1 | **UNSAT 115.5s** |
| A3 | only seed term 3, product +1 | **UNSAT 115.5s** |
| A4 | only seed term 4, product +1 | **UNSAT 246.3s** |
| A8 | only seed term 8, product +1 | **UNSAT 176.2s** |
| B2n3 | 3,4,8 cover; term 3 negative | **UNSAT 50.9s** |
| B2n4 | 3,4,8 cover; term 4 negative | **UNSAT 57.0s** |
| B2n8 | 3,4,8 cover; term 8 negative | **UNSAT 61.6s** |
| B3n2 | 2,4,8 cover; term 2 negative | **UNSAT 43.2s** |
| B3n4 | 2,4,8 cover; term 4 negative | **UNSAT 45.8s** |
| B3n8 | 2,4,8 cover; term 8 negative | **UNSAT 53.3s** |
| B4n2 | 2,3,8 cover; term 2 negative | **UNSAT 51.5s** |
| B4n3 | 2,3,8 cover; term 3 negative | **UNSAT 49.7s** |
| B4n8 | 2,3,8 cover; term 8 negative | **UNSAT 53.3s** |
| B8n2 | 2,3,4 cover; term 2 negative | **UNSAT 31.0s** |
| B8n3 | 2,3,4 cover; term 3 negative | **UNSAT 37.8s** |
| B8n4 | 2,3,4 cover; term 4 negative | **UNSAT 33.5s** |

**Conclusion (auditable):** with the other 18 Laderman terms frozen,
no rewrite of seed terms {2,3,4,8} with {0,±1} coefficients completes
the wrong=1 state to an exact rank-22 decomposition. This closes the
instance left undecided by Waves 4–5. Scope, stated precisely: this is
a statement about **this free-set and this coefficient set only**. It
does not exclude other free-4 sets on this seed, free-5+ rewrites,
{0,±1} rewrites that also move terms outside {2,3,4,8}, halves or
wider coefficients on this set (the {2,3,4} triple in halves is
already closed by Wave 5; this 4-set in halves is untested), or rank
22 over Q in general. The wrong=1 state remains a near-miss, **not** a
result.

Why the split worked where the raw run stalled: the raw instance's
difficulty concentrates in the (8,8,8) covering structure — fixing
which terms cover (and their signs) removes the symmetric thrash
between covering configurations; the triple-cover cases, with nine
factor entries pinned nonzero, decided in under ~62s each.

## Queue item 2 — Perminov wrong=1 state (wrong entry (5,8,5))

Seed `wave5/schemes/drops/anneal_best_r22.json` (Perminov minus term
6). Wave 5 closed free-2 and two free-3 sets in {0,±1}. This wave, via
`termfree.py` (same control-validated encoder):

| Instance | Domain | Outcome |
|---|---|---|
| free-3 {14,3,2} (one toucher per factor), cap 600s | {0,±1/2,±1} | **UNSAT in 325.5s** — fractions route through this triple closed |
| free-3 {20,10,19} (one toucher per factor), cap 600s | {0,±1/2,±1} | **UNSAT in 334.6s** — fractions route through this triple closed |
| free-4 {14,3,2,21} (touchers + box-84 dense term 21; residual nnz 91), cap 600s | {0,±1} | **NO CONCLUSION** — z3 unknown in 600.2s. Next escalation: the covering-parity case-split of §1 applied to wrong entry (5,8,5) |

The Perminov basin now mirrors Laderman's: locally rigid against all
tested 2- and 3-term rewrites in {0,±1} (Wave 5) **and** in halves
(this wave), with its first free-4 attempt undecided.

## Queue item 3 — r24 seed, free {0,1,5,23}

`wave3/bridge/discrete_r24c.json` (21/729 wrong), free-set {0,1,5,23}
(dead slots 0,1 + single-entry live terms 5,23), {0,±1}, cap 900s —
the ready instance preserved since Wave 4:

| Instance | Outcome |
|---|---|
| free-4 {0,1,5,23}, cap 900s | **NO CONCLUSION** — z3 unknown in 900.2s (timeout; the run's wall time overran the cap under this VM's CPU throttling, so the outcome landed after this report's first draft — final state confirmed from `r24_f4_01523.log`, no file saved). Consistent with the Wave 3 (300s) and Wave 4 (1200s) free-4 timeouts on this seed. |

## Files

- `termfree.py` (copied unchanged from `wave5/exact/`),
  `casesplit.py` (case-split solver with the exhaustiveness argument
  in its docstring), `prep.py` (instance anatomy), `OUTCOMES.md`
  (running per-instance log), `control_r26.json` (CLI-VERIFIED control
  artefact).
- Logs: `perm_f3h_14_3_2.log`, `perm_f3h_20_10_19.log`,
  `perm_f4_14_3_2_21.log`, `r24_f4_01523.log`.
- Nothing added to `results/`; campaign files untouched.

## Suggested next steps (for the coordinator)

1. The Laderman wrong=1 basin is now closed against ≤4-term {0,±1}
   rewrites of the line-term neighbourhood (free-2/3 in Waves 4–5,
   free-4 {2,3,4,8} here). Remaining levers on this seed: a *different*
   free-4 set mixing line + dense terms in {0,±1} (e.g. {2,3,5,10}),
   free-5 sets, or this same 4-set in halves — each attackable with
   the same covering case-split (the parity argument is
   coefficient-set independent for any domain symmetric under negation
   with values in {0,±1} scaled; for halves the summands lie in
   {0,±1/8,±1/4,±1/2,±1}·… — the split needs re-derivation there).
2. The case-split technique itself is the transferable win: any future
   undecided free-k instance on a wrong=1 seed splits by the wrong
   entry's covering parity. First application: the Perminov free-4
   {14,3,2,21} instance left undecided above (split on wrong entry
   (5,8,5)); then the other wrong=1 drop states (33 banked in
   `wave5/schemes/drops/`).
3. The r24 seed's free-4 instances have now timed out at 300s,
   900s and 1200s across three waves — apply the covering-style
   decomposition there too (its residual is 23 unit entries, so the
   split variable is which freed terms cover each missing entry),
   or move to a different free-set on that seed.
