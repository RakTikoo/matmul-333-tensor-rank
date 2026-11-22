#!/usr/bin/env python3
"""
fracsplit.py — Wave 8 FRACTIONS driver.

Reuses wave7/parity/paritysplit.py's instance builder and case
enumeration VERBATIM (imported, not reimplemented — so case indices
for the {0,+-1} Perminov free-4 instance are identical to Wave 7's
OUTCOMES.md), with three changes:

  1. Outcomes log to wave8/fractions/OUTCOMES.md (not Wave 7's).
  2. Extended coefficient sets: adds "q1" = quarters
     {0,+-1,+-1/2,+-1/4,+-3/4} (D=4) to termfree.COEFF_SETS before
     paritysplit imports it (same dict object).
  3. Coarse first split for the halves free-4: cases can be selected
     by the |product| multiset pattern of the covering vector
     (--pattern=a,b,c,d), implementing Wave 7's prescribed fix for
     the 213-case halves enumeration.

The per-case solve loop is paritysplit.py's, copied unchanged apart
from the log target: fresh z3 Solver per case, Or-of-equalities
domain constraints, the full 729 scaled-integer equations, plus the
case constraint prod_t(e) == v_t. On SAT: assemble with Fractions,
exact self-check 0/729 required before saving.

Exhaustiveness (inherited from paritysplit): for a wrong=1 seed with
wrong entry e, any solution's covering-product vector v (one entry
per freed term, prod_t(e) = U_t[e0]*V_t[e1]*W_t[e2]) sums to R[e];
the cases are ALL such vectors in P^free, pairwise disjoint, union =
whole instance. Grouping cases by |product| pattern is a partition
of that same case set — deciding every case of a pattern decides
that pattern; deciding every pattern decides the instance.

Usage:
  fracsplit.py <seed> <free_csv> <coeff_set> <cap_s> <out_path> <tag>
               [--list] [--list-patterns]
               [--cases i,j,...] [--pattern a,b,c,d] [--max-cases N]
"""
import itertools
import json
import sys
import time
from fractions import Fraction

import numpy as np

sys.path.insert(0, "wave7/parity")
import termfree  # noqa: E402

termfree.COEFF_SETS["q1"] = [Fraction(0), Fraction(1), Fraction(-1),
                             Fraction(1, 2), Fraction(-1, 2),
                             Fraction(1, 4), Fraction(-1, 4),
                             Fraction(3, 4), Fraction(-3, 4)]

import paritysplit as ps  # noqa: E402  (build_instance/enumerate_cases)
from termfree import target333, fmt  # noqa: E402

LOG = "wave8/fractions/OUTCOMES.md"


def logline(msg):
    line = f"- [{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def pattern_of(v):
    return tuple(sorted((abs(x) for x in v), reverse=True))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = [a for a in sys.argv[1:] if a.startswith("--")]
    seed_path, free_csv, cs_name = args[0], args[1], args[2]
    cap = int(args[3])
    out_path, tag = args[4], args[5]
    free = sorted(int(x) for x in free_csv.split(","))
    F, r, D, allowed, R, e, target_e = ps.build_instance(seed_path, free,
                                                         cs_name)
    P, cases = ps.enumerate_cases(free, allowed, target_e)
    logline(f"**{tag}**: seed={seed_path} free={free} coeff={cs_name} "
            f"D={D} allowed={allowed} P={P} wrong entry e={e} "
            f"R[e]={target_e} residual_nnz={int(np.count_nonzero(R))} "
            f"cases={len(cases)}**")
    if "--list" in opts:
        for i, v in enumerate(cases):
            print(f"  case {i}: [{ps.case_spec(free, v)}] "
                  f"pattern={pattern_of(v)}")
        return 0
    if "--list-patterns" in opts:
        groups = {}
        for i, v in enumerate(cases):
            groups.setdefault(pattern_of(v), []).append(i)
        for pat in sorted(groups, key=lambda p: (-max(p),
                                                 -sum(1 for x in p if x),
                                                 p)):
            idx = groups[pat]
            print(f"  pattern {pat}: {len(idx)} cases, indices "
                  f"{idx[0]}..{idx[-1]} -> {idx}")
        print(f"  total patterns={len(groups)} cases={len(cases)}")
        return 0
    sel = None
    for o in opts:
        if o.startswith("--cases="):
            sel = [int(x) for x in o.split("=")[1].split(",")]
        if o.startswith("--pattern="):
            pat = tuple(int(x) for x in o.split("=")[1].split(","))
            sel = [i for i, v in enumerate(cases) if pattern_of(v) == pat]
            logline(f"{tag}: pattern {pat} selects cases {sel}")
    max_cases = None
    for o in opts:
        if o.startswith("--max-cases="):
            max_cases = int(o.split("=")[1])
    todo = sel if sel is not None else list(range(len(cases)))
    if max_cases is not None:
        todo = todo[:max_cases]

    import z3
    for ci in todo:
        v = cases[ci]
        spec = ps.case_spec(free, v)
        U = {t: [z3.Int(f"U_{p}_{t}") for p in range(9)] for t in free}
        V = {t: [z3.Int(f"V_{q}_{t}") for q in range(9)] for t in free}
        W = {t: [z3.Int(f"W_{s}_{t}") for s in range(9)] for t in free}
        s = z3.Solver()
        s.set("timeout", cap * 1000)
        for M in (U, V, W):
            for t in free:
                for var in M[t]:
                    s.add(z3.Or([var == a for a in allowed]))
        for p in range(9):
            for q in range(9):
                for ss in range(9):
                    expr = 0
                    for t in free:
                        expr = expr + U[t][p] * V[t][q] * W[t][ss]
                    s.add(expr == int(R[p, q, ss]))
        for t, vt in zip(free, v):
            s.add(U[t][e[0]] * V[t][e[1]] * W[t][e[2]] == vt)
        t0 = time.time()
        res = s.check()
        dt = time.time() - t0
        ctag = f"{tag} case {ci}/{len(cases) - 1} [{spec}]"
        if res == z3.sat:
            m = s.model()
            outF = {name: [row[:] for row in F[name]]
                    for name in ("U", "V", "W")}
            for t in free:
                for p in range(9):
                    outF["U"][p][t] = Fraction(m[U[t][p]].as_long(), D)
                    outF["V"][p][t] = Fraction(m[V[t][p]].as_long(), D)
                    outF["W"][p][t] = Fraction(m[W[t][p]].as_long(), D)
            T = target333()
            wrong = sum(
                1 for p in range(9) for q in range(9) for ss in range(9)
                if sum(outF["U"][p][t] * outF["V"][q][t] * outF["W"][ss][t]
                       for t in range(r)) != T[p, q, ss])
            if wrong == 0:
                out = {"a": 3, "b": 3, "c": 3, "field": "Q",
                       "U": [[fmt(x) for x in row] for row in outF["U"]],
                       "V": [[fmt(x) for x in row] for row in outF["V"]],
                       "W": [[fmt(x) for x in row] for row in outF["W"]]}
                with open(out_path, "w") as f:
                    json.dump(out, f)
                logline(f"**{ctag}: SAT in {dt:.1f}s — assembled "
                        f"self-check 0/729, SAVED {out_path} — "
                        f"CANDIDATE RECORD, CLI-verify fresh**")
                return 0
            logline(f"{ctag}: SAT but self-check {wrong} wrong — "
                    f"ENCODING BUG, do not trust")
            return 2
        if res == z3.unsat:
            logline(f"{ctag}: UNSAT in {dt:.1f}s")
        else:
            logline(f"{ctag}: NO CONCLUSION (unknown at {cap}s cap, "
                    f"wall {dt:.1f}s)")
    logline(f"{tag}: case batch done ({len(todo)} of {len(cases)} cases "
            f"attempted)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
