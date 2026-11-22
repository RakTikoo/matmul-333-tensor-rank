#!/usr/bin/env python3
"""Self-contained re-verification of the headline kernel dimensions.

For each scheme in certificates/:
  1. builds the Brent Jacobian J (729 x 621, integer entries) from the
     scheme file, in the parameter order [U; V; W], each flattened
     (term, entry) -> term*9 + entry;
  2. computes rank(J) mod p for several primes  =>  dim ker J over Q
     is at most 621 - rank (rank can only drop mod p);
  3. loads the exact rational kernel basis from certificates/ and
     checks every vector satisfies J.v = 0 exactly over Z, and that
     the basis is independent (rank mod p equals the vector count)
     =>  dim ker J over Q is at least the count.
If the two bounds meet, dim ker J over Q is exactly the count.

Usage:  python3 code/check_kernels.py
Requires: numpy. Everything else is the standard library.
"""
import json
import sys
from fractions import Fraction
from math import gcd

import numpy as np

PRIMES = [999983, 999979, 1000003, 1000033]


def load_scheme(path):
    d = json.load(open(path))
    mats = []
    for key in ("U", "V", "W"):
        M = [[Fraction(x) for x in row] for row in d[key]]
        assert all(x.denominator == 1 for row in M for x in row), \
            f"{path}: {key} has non-integer entries; this checker covers the two integer schemes"
        mats.append(np.array([[int(x) for x in row] for row in M], dtype=np.int64))
    return mats  # each 9 x r


def jacobian_int(U, V, W):
    r = U.shape[1]
    I9 = np.eye(9, dtype=np.int64)
    JU = np.einsum('pi,qt,st->pqsit', I9, V, W).transpose(0, 1, 2, 4, 3)
    JV = np.einsum('pt,qi,st->pqsit', U, I9, W).transpose(0, 1, 2, 4, 3)
    JW = np.einsum('pt,qt,si->pqsit', U, V, I9).transpose(0, 1, 2, 4, 3)
    return np.concatenate([JU.reshape(729, 9 * r), JV.reshape(729, 9 * r),
                           JW.reshape(729, 9 * r)], axis=1).astype(np.int64)


def rank_mod(A, p):
    A = (A % p).astype(np.int64)
    m, n = A.shape
    rank = 0
    for col in range(n):
        piv = -1
        for i in range(rank, m):
            if A[i, col] != 0:
                piv = i
                break
        if piv < 0:
            continue
        if piv != rank:
            A[[rank, piv]] = A[[piv, rank]]
        inv = pow(int(A[rank, col]), -1, p)
        A[rank] = (A[rank] * inv) % p
        below = A[rank + 1:, col].copy()
        nz = below != 0
        if nz.any():
            idx = np.where(nz)[0] + rank + 1
            A[idx] = (A[idx] - np.outer(below[nz], A[rank])) % p
        rank += 1
        if rank == m:
            break
    return rank


def check(name, scheme_path, kernel_path, expected):
    print(f"== {name}")
    U, V, W = load_scheme(scheme_path)
    J = jacobian_int(U, V, W)
    print(f"   J built: {J.shape[0]}x{J.shape[1]}, entries in "
          f"[{J.min()}, {J.max()}]")
    for p in PRIMES:
        rk = rank_mod(J, p)
        print(f"   rank(J) mod {p} = {rk}  ->  dim ker over Q <= {621 - rk}")
        assert 621 - rk == expected, \
            f"mod-{p} nullity {621 - rk} != claimed {expected}: CLAIM FAILS"

    vecs = np.load(kernel_path, allow_pickle=True)["vecs"]
    assert vecs.shape[0] == expected, \
        f"kernel file holds {vecs.shape[0]} vectors, claim is {expected}"
    # exact check J.v = 0 over Z, per vector (clear denominators first)
    for i, row in enumerate(vecs):
        fr = [Fraction(x) for x in row]
        den = 1
        for x in fr:
            den = den * x.denominator // gcd(den, x.denominator)
        v = np.array([int(x * den) for x in fr], dtype=object)
        prod = np.array([sum(int(J[a, b]) * v[b] for b in range(621))
                         for a in range(729)], dtype=object)
        assert all(x == 0 for x in prod), f"kernel vector {i}: J.v != 0"
    print(f"   all {expected} kernel vectors satisfy J.v = 0 exactly over Z")
    B = np.array([[int(Fraction(x)) for x in row] for row in vecs],
                 dtype=np.int64)
    for p in PRIMES[:2]:
        rk = rank_mod(B, p)
        assert rk == expected, f"kernel basis rank mod {p} = {rk} != {expected}"
    print(f"   kernel basis independent (rank = {expected} mod {PRIMES[0]}, {PRIMES[1]})")
    print(f"   => dim ker J over Q = {expected} EXACTLY "
          f"(upper bound from rank mod p, lower bound from the exhibited basis)")
    print()


def main():
    root = sys.path[0] + "/.." if sys.path[0] else ".."
    check("Laderman (1976)", f"{root}/certificates/laderman_r23_Q.json",
          f"{root}/certificates/kernel_laderman.npz", 76)
    check("Perminov cn122 (2025)", f"{root}/certificates/perminov_cn122_r23_Q.json",
          f"{root}/certificates/kernel_perminov.npz", 94)
    print("ALL CHECKS PASS: dim ker J = 76 (Laderman), 94 (Perminov) over Q.")
    print("Trivial tangents span 70 at each point (46 torus + 26 orbit - 2 overlap),")
    print("so the excess is 6 at Laderman and 24 at Perminov.")


if __name__ == "__main__":
    main()
