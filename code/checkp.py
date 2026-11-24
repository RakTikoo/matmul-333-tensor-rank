# checkp.py — exact mod-p judge for matmul tensor decompositions.
# Packaged copy of the campaign checker (wave20/primes/checkp.py),
# archived as run; used to judge the F3 near-miss state in
# data/wrong5-state.json (see data/wrong5-case-study.md).
#
#!/usr/bin/env python3
"""checkp.py — exact mod-p checker for matmul tensor decompositions
(field-parametric generalisation of wave17/prime/check3.py).

Same file format and tensor convention as the campaign's verify.py:
  {"a","b","c","field","U","V","W"} with U:(a*b)x r, V:(b*c)x r,
  W:(a*c)x r, entries int or "p/q" strings. Target T[p][q][s] = 1 iff,
  with p=(i,j), q=(j2,k), s=(i2,k2) row-major, j==j2 and i==i2 and
  k==k2.

All arithmetic is pure Python integer arithmetic reduced mod P.
A fraction a/b is reduced mod P as a * b^{-1} (mod P); b must not be
divisible by P.

Usage: checkp.py <prime> <file.json>
Prints one line: CHECKP PASS wrong=0/<n> ... or CHECKP FAIL wrong=<k>/<n> ...
Exit code 0 iff PASS.
"""
import json, sys
from fractions import Fraction


def main():
    P = int(sys.argv[1])
    path = sys.argv[2]

    def residue(x):
        if isinstance(x, str):
            f = Fraction(x)
        elif isinstance(x, int):
            f = Fraction(x)
        else:
            raise ValueError(f"non-exact entry {x!r} (floats forbidden)")
        num, den = f.numerator, f.denominator
        dm = den % P
        if dm == 0:
            raise ValueError(f"denominator divisible by {P} in entry {x!r}")
        return (num % P) * pow(dm, -1, P) % P

    with open(path) as fh:
        d = json.load(fh)
    a, b, c = d["a"], d["b"], d["c"]
    U = [[residue(x) for x in row] for row in d["U"]]
    V = [[residue(x) for x in row] for row in d["V"]]
    W = [[residue(x) for x in row] for row in d["W"]]
    r = len(U[0])
    assert len(U) == a * b and len(V) == b * c and len(W) == a * c, "bad shapes"
    assert all(len(row) == r for row in U + V + W), "ragged matrices"

    def target(p, q, s):
        i, j = divmod(p, b)
        j2, k = divmod(q, c)
        i2, k2 = divmod(s, c)
        return 1 if (j == j2 and i == i2 and k == k2) else 0

    wrong = 0
    first = []
    total = (a * b) * (b * c) * (a * c)
    for p in range(a * b):
        for q in range(b * c):
            for s in range(a * c):
                acc = 0
                for t in range(r):
                    acc += U[p][t] * V[q][t] * W[s][t]
                if acc % P != target(p, q, s):
                    wrong += 1
                    if len(first) < 5:
                        first.append((p, q, s, acc % P, target(p, q, s)))
    if wrong == 0:
        print(f"CHECKP PASS wrong=0/{total} rank={r} field=F{P} file={path}")
        return 0
    print(f"CHECKP FAIL wrong={wrong}/{total} rank={r} field=F{P} first_wrong={first} file={path}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
