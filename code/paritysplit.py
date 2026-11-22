#!/usr/bin/env python3
"""
paritysplit.py — Wave 7 PARITY-SWEEP: generalised covering-parity case
split for term-freeing instances on wrong=1 seeds (scales Wave 6's
wave6/deepexact/casesplit.py from one hardcoded instance to any
seed / free-set / coefficient set in {"1", "h1"}).

Method. Freeze all seed terms except `free`; the freed terms must
reproduce the residual R = D^3*T - sum(frozen) in the scaled-integer
encoding of termfree.py (D = lcm of seed and coefficient denominators;
freed entries range over the finite set A = {D*s : s in coeff_set}).
Let e be the seed's unique wrong entry (have 0 / want 1, asserted).
In ANY solution of the full instance, the e-equation reads

    sum_{t in free} U_t[e0]*V_t[e1]*W_t[e2] = R[e]        (scaled ints)

where each summand (a "covering product") lies in the finite set
P = {a*b*c : a,b,c in A}. Hence the vector of covering products is one
of the finitely many vectors v in P^free with sum(v) = R[e]. The cases
are exactly those vectors: pairwise disjoint (a solution's product
vector is unique) and exhaustive (every solution has one). Each case
adds the constraints prod_t(e) == v_t to the full 729-equation
instance and is decided by a fresh z3 Solver. UNSAT on every case =
sound UNSAT of the whole instance (for this free-set + coefficient
set, rest frozen). Any case left unrun or unknown leaves the instance
UNDECIDED — reported as such, never as UNSAT.

For coeff "1" (A={0,+-1}, P={-1,0,1}) and R[e]=+1 this reproduces
Wave 6's split exactly: free-4 -> 16 cases (4 single-cover "A", 12
triple-cover "B"); free-3 -> 6 cases. For coeff "h1" (D=2,
A={0,+-1,+-2}, P={0,+-1,+-2,+-4,+-8}) and R[e]=8 the enumeration is
by construction (all vectors in P^free summing to 8).

Usage:
  paritysplit.py <seed> <free_csv> <coeff_set> <cap_s> <out_path>
                 <tag> [--list] [--cases i,j,...] [--max-cases N]
Cases run most-pinned first (more covering terms, then larger total
|product| — Wave 6 evidence: triple-cover cases decided fastest).
Every case outcome is appended to OUTCOMES.md immediately.
On SAT: assemble, exact Fraction self-check, save to <out_path>.
verify.py is NOT imported; the caller CLI-verifies any saved file.
"""
import itertools
import json
import sys
import time
from fractions import Fraction
from math import gcd

import numpy as np

sys.path.insert(0, "wave7/parity")
from termfree import COEFF_SETS, lcm, target333, fmt  # noqa: E402

LOG = "wave7/parity/OUTCOMES.md"


def logline(msg):
    line = f"- [{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def build_instance(seed_path, free, cs_name):
    """Return (F, r, D, allowed, R, e, target_e) in scaled integers."""
    S = COEFF_SETS[cs_name]
    d = json.load(open(seed_path))
    assert (d["a"], d["b"], d["c"]) == (3, 3, 3)
    F = {name: [[Fraction(x) if isinstance(x, str) else Fraction(x)
                 for x in row] for row in d[name]]
         for name in ("U", "V", "W")}
    r = len(F["U"][0])
    D = 1
    for name in ("U", "V", "W"):
        for row in F[name]:
            for x in row:
                D = lcm(D, x.denominator)
    for s in S:
        D = lcm(D, s.denominator)
    A = {name: np.array([[int(D * x) for x in row] for row in F[name]],
                        dtype=np.int64) for name in ("U", "V", "W")}
    # the seed's own wrong entries (unscaled check on the seed itself)
    T = target333()
    seedT = np.einsum("pt,qt,st->pqs", A["U"], A["V"], A["W"])
    diff = (D ** 3) * T - seedT
    wrong = np.argwhere(diff != 0)
    assert len(wrong) == 1, f"seed must have exactly 1 wrong entry, got {len(wrong)}"
    e = tuple(int(x) for x in wrong[0])
    assert int(diff[e]) == D ** 3, f"expected have-0/want-1 at e, delta={int(diff[e])}"
    frozen = [t for t in range(r) if t not in free]
    R = (D ** 3) * T - np.einsum("pt,qt,st->pqs", A["U"][:, frozen],
                                 A["V"][:, frozen], A["W"][:, frozen])
    allowed = sorted(int(D * s) for s in S)
    return F, r, D, allowed, R, e, int(R[e])


def enumerate_cases(free, allowed, target_e):
    P = sorted({a * b * c for a in allowed for b in allowed
                for c in allowed})
    cases = [v for v in itertools.product(P, repeat=len(free))
             if sum(v) == target_e]
    # most-pinned first: more covering terms, then larger sum |v|
    cases.sort(key=lambda v: (-sum(1 for x in v if x != 0),
                              -sum(abs(x) for x in v)))
    return P, cases


def case_spec(free, v):
    return ",".join(f"{t}:{x:+d}" for t, x in zip(free, v))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = [a for a in sys.argv[1:] if a.startswith("--")]
    seed_path, free_csv, cs_name = args[0], args[1], args[2]
    cap = int(args[3])
    out_path, tag = args[4], args[5]
    free = sorted(int(x) for x in free_csv.split(","))
    F, r, D, allowed, R, e, target_e = build_instance(seed_path, free,
                                                      cs_name)
    P, cases = enumerate_cases(free, allowed, target_e)
    logline(f"**{tag}**: seed={seed_path} free={free} coeff={cs_name} "
            f"D={D} allowed={allowed} P={P} wrong entry e={e} "
            f"R[e]={target_e} residual_nnz={int(np.count_nonzero(R))} "
            f"cases={len(cases)}**")
    if "--list" in opts:
        for i, v in enumerate(cases):
            print(f"  case {i}: [{case_spec(free, v)}]")
        return 0
    sel = None
    for o in opts:
        if o.startswith("--cases="):
            sel = [int(x) for x in o.split("=")[1].split(",")]
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
        spec = case_spec(free, v)
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
