#!/usr/bin/env python3
"""
termfree.py — Wave 3 exact term-freeing completion (generalised).

Usage: termfree.py <seed.json> <free_csv> <coeff_set> <cap_s> <out_path> [tag]
  coeff_set: "1"  -> freed coefficients in {0,+-1}
             "2"  -> freed coefficients in {0,+-1,+-2}
             "h1" -> freed coefficients in {0,+-1/2,+-1}

Method: freeze all seed terms except the freed ones; freed terms must
exactly reproduce the residual R = T - sum(frozen) over Q. All arithmetic
is done over the integers by scaling with D = lcm of the denominators of
the seed entries and of the coefficient set: entries become D*x, the
target becomes D^3 * T, and each freed variable is constrained to the
finite set {D*s : s in coeff_set} via Or-of-equalities. z3 decides.
SAT -> assemble, self-check exactly with Fractions, save JSON to
out_path. UNSAT is a statement about THIS free-set + coefficient set
only. unknown/timeout = NO CONCLUSION.

verify.py is NOT imported — the caller checks any saved file with the
verify.py CLI in a fresh process (the only judge that counts).
"""
import json
import sys
import time
from fractions import Fraction
from math import gcd

import numpy as np

COEFF_SETS = {
    "1": [Fraction(0), Fraction(1), Fraction(-1)],
    "2": [Fraction(0), Fraction(1), Fraction(-1), Fraction(2), Fraction(-2)],
    "h1": [Fraction(0), Fraction(1), Fraction(-1),
           Fraction(1, 2), Fraction(-1, 2)],
}


def lcm(a, b):
    return a * b // gcd(a, b)


def target333():
    T = np.zeros((9, 9, 9), dtype=np.int64)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                T[3 * i + j, 3 * j + k, 3 * i + k] = 1
    return T


def fmt(x: Fraction):
    return int(x) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main():
    seed_path, free_csv, cs_name = sys.argv[1], sys.argv[2], sys.argv[3]
    cap = int(sys.argv[4])
    out_path = sys.argv[5]
    tag = sys.argv[6] if len(sys.argv) > 6 else "termfree"
    import z3

    free = sorted(int(x) for x in free_csv.split(","))
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
    frozen = [t for t in range(r) if t not in free]
    R = (D ** 3) * target333() - np.einsum(
        "pt,qt,st->pqs", A["U"][:, frozen], A["V"][:, frozen],
        A["W"][:, frozen])
    allowed = sorted(int(D * s) for s in S)
    print(f"[{tag}] seed={seed_path} rank={r} free={free} "
          f"coeff_set={cs_name} allowed(scaled)={allowed} D={D} cap={cap}s "
          f"residual range [{R.min()},{R.max()}], nnz "
          f"{int(np.count_nonzero(R))}", flush=True)

    U = {t: [z3.Int(f"U_{p}_{t}") for p in range(9)] for t in free}
    Vv = {t: [z3.Int(f"V_{q}_{t}") for q in range(9)] for t in free}
    W = {t: [z3.Int(f"W_{s}_{t}") for s in range(9)] for t in free}
    s = z3.Solver()
    s.set("timeout", cap * 1000)
    for M in (U, Vv, W):
        for t in free:
            for v in M[t]:
                s.add(z3.Or([v == a for a in allowed]))
    for p in range(9):
        for q in range(9):
            for ss in range(9):
                expr = 0
                for t in free:
                    expr = expr + U[t][p] * Vv[t][q] * W[t][ss]
                s.add(expr == int(R[p, q, ss]))
    t0 = time.time()
    res = s.check()
    dt = time.time() - t0
    print(f"[{tag}] z3 -> {res} in {dt:.1f}s", flush=True)
    if res == z3.sat:
        m = s.model()
        outF = {name: [row[:] for row in F[name]] for name in ("U", "V", "W")}
        for t in free:
            for p in range(9):
                outF["U"][p][t] = Fraction(m[U[t][p]].as_long(), D)
                outF["V"][p][t] = Fraction(m[Vv[t][p]].as_long(), D)
                outF["W"][p][t] = Fraction(m[W[t][p]].as_long(), D)
        # Exact self-check with Fractions.
        T = target333()
        wrong = 0
        for p in range(9):
            for q in range(9):
                for ss in range(9):
                    v = sum(outF["U"][p][t] * outF["V"][q][t] *
                            outF["W"][ss][t] for t in range(r))
                    if v != T[p, q, ss]:
                        wrong += 1
        print(f"[{tag}] assembled self-check: {wrong} wrong of 729",
              flush=True)
        if wrong == 0:
            out = {"a": 3, "b": 3, "c": 3, "field": "Q",
                   "U": [[fmt(x) for x in row] for row in outF["U"]],
                   "V": [[fmt(x) for x in row] for row in outF["V"]],
                   "W": [[fmt(x) for x in row] for row in outF["W"]]}
            with open(out_path, "w") as f:
                json.dump(out, f)
            print(f"[{tag}] SAVED {out_path} (caller must CLI-verify)",
                  flush=True)
            return 0
        print(f"[{tag}] SAT model failed self-check — ENCODING BUG, "
              "do not trust", flush=True)
        return 2
    if res == z3.unsat:
        print(f"[{tag}] z3 UNSAT: free-set {free} with coefficients "
              f"{cs_name} cannot complete this seed (statement about "
              "this free-set only)", flush=True)
        return 3
    print(f"[{tag}] NO CONCLUSION (timeout/unknown)", flush=True)
    return 4


if __name__ == "__main__":
    sys.exit(main())
