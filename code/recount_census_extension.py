# Independent second-path checker (Wave 32 claim gate).
# recount_census_extension.py — a from-scratch recount of the census
# extension (data/census-extension.md): re-judges every held-out
# scheme file exactly over Q and re-derives the unit-term census
# (per file and per distinct scheme) without sharing code with the
# Wave 30 census or the Wave 28 recount. It references the
# campaign's internal file layout; the packaged entry point for
# the headline kernel numbers is check_kernels.py.

#!/usr/bin/env python3
"""
recount_g1.py — Wave 32 GATE, second path for claim G1 (Wave 30 Item A).
Provenance: Wave 32 gate agent, 2026-11-23. Judge status: this script's
own exact recomputation plus fresh-process verify.py CLI runs.

Fresh code, written for this gate. It shares NO code with
wave30/wild/itemA_census.py (not read) and none with
wave28/gate/recount_c1.py. Inputs: the scheme JSON files on disk and
the held-out file list taken from the Wave 30 record
(wave30/wild/itemA_results.json, records with class "held-out-new").

Method (from the tensor definition only):
  T[p][q][s] = 1 iff, with p=(i,j), q=(j2,k), s=(i2,k2) row-major,
  j==j2 and i==i2 and k==k2; else 0.
  A scheme is exact iff sum_t U[p][t] V[q][t] W[s][t] == T[p][q][s]
  at all 729 positions, in exact Fraction arithmetic (recomputed
  here independently; verify.py CLI is also run fresh per file).
  A term is a UNIT term iff each of its three factor columns has
  exactly one nonzero entry. Its position is the triple of nonzero
  row indices. It is NAIVE iff T at that position is 1.
  Distinct schemes: two files are the same scheme iff their
  multisets of rank-1 term tensors agree, each term tensor
  canonicalised to a primitive integer 729-vector (common
  denominator cleared, gcd divided out, sign fixed by first
  nonzero entry positive).
"""
import json
import subprocess
import sys
from fractions import Fraction
from math import gcd

ROOT = "/home/hatch/workspace/matmul-pilot"


def parse(x):
    if isinstance(x, str):
        return Fraction(x)
    return Fraction(x)


def load(path):
    d = json.load(open(path))
    U = [[parse(x) for x in row] for row in d["U"]]
    V = [[parse(x) for x in row] for row in d["V"]]
    W = [[parse(x) for x in row] for row in d["W"]]
    return d, U, V, W


def target(p, q, s):
    i, j = divmod(p, 3)
    j2, k = divmod(q, 3)
    i2, k2 = divmod(s, 3)
    return 1 if (j == j2 and i == i2 and k == k2) else 0


def wrong_count(U, V, W, r):
    wrong = 0
    for p in range(9):
        for q in range(9):
            for s in range(9):
                tot = sum(U[p][t] * V[q][t] * W[s][t] for t in range(r))
                if tot != target(p, q, s):
                    wrong += 1
    return wrong


def term_tensor(U, V, W, t):
    return tuple(U[p][t] * V[q][t] * W[s][t]
                 for p in range(9) for q in range(9) for s in range(9))


def primitive(vec):
    L = 1
    for x in vec:
        dn = x.denominator
        L = L * dn // gcd(L, dn)
    ints = [int(x * L) for x in vec]
    g = 0
    for v in ints:
        g = gcd(g, abs(v))
    if g > 1:
        ints = [v // g for v in ints]
    for v in ints:
        if v != 0:
            if v < 0:
                ints = [-w for w in ints]
            break
    return tuple(ints)


def unit_terms(U, V, W, r):
    out = []
    for t in range(r):
        pos = []
        ok = True
        for M in (U, V, W):
            nz = [row for row in range(9) if M[row][t] != 0]
            if len(nz) != 1:
                ok = False
                break
            pos.append(nz[0])
        if ok:
            out.append((t, tuple(pos)))
    return out


def main():
    rec = json.load(open(ROOT + "/wave30/wild/itemA_results.json"))
    held = [r["file"] for r in rec["records"]
            if r.get("class") == "held-out-new"]
    print("held-out files from wave30 record:", len(held))

    per_file = []
    failures = []
    groups = {}
    for f in held:
        path = ROOT + "/" + f
        d, U, V, W = load(path)
        r = len(U[0])
        wc = wrong_count(U, V, W, r)
        cp = subprocess.run(
            [sys.executable, ROOT + "/verify.py", "check", path],
            capture_output=True, text=True)
        cli_ok = cp.stdout.startswith("VERIFIED")
        if (not cli_ok) or wc != 0:
            failures.append((f, wc, cp.stdout.strip()[:80]))
        uts = unit_terms(U, V, W, r)
        naive = sum(1 for _, pos in uts if target(*pos) == 1)
        off = [(t, pos) for t, pos in uts if target(*pos) != 1]
        canon = tuple(sorted(primitive(term_tensor(U, V, W, t))
                             for t in range(r)))
        groups.setdefault(canon, []).append(f)
        per_file.append({"file": f, "rank": r, "wrong_own": wc,
                         "cli_verified": cli_ok,
                         "unit_terms": len(uts), "naive": naive,
                         "off_support": [{"term": t, "pos": list(pos)}
                                         for t, pos in off]})

    print("files failing own exact check or CLI:", failures)
    tot_u = sum(x["unit_terms"] for x in per_file)
    tot_n = sum(x["naive"] for x in per_file)
    print("PER FILE: %d files, unit=%d, naive=%d, off=%d"
          % (len(per_file), tot_u, tot_n, tot_u - tot_n))

    by_file = {x["file"]: x for x in per_file}
    du = dn = 0
    dup_groups = []
    for canon, files in groups.items():
        rep = by_file[files[0]]
        du += rep["unit_terms"]
        dn += rep["naive"]
        if len(files) > 1:
            dup_groups.append(files)
    print("DISTINCT schemes: %d, unit=%d, naive=%d, off=%d"
          % (len(groups), du, dn, du - dn))
    print("duplicate groups within held-out (%d):" % len(dup_groups))
    for g in dup_groups:
        print("   ", g)

    pf = "wave22/ladder/wave22_333_r24_Q_proj.json"
    d, U, V, W = load(ROOT + "/" + pf)
    r = len(U[0])
    print("\nCOUNTEREXAMPLE %s: rank=%d, wrong_own=%d"
          % (pf, r, wrong_count(U, V, W, r)))
    for name, M in (("U", U), ("V", V), ("W", W)):
        col = [(row, str(M[row][0])) for row in range(9) if M[row][0] != 0]
        print("  term0 %s column nonzeros: %s" % (name, col))
    tt = term_tensor(U, V, W, 0)
    nz = [(idx, str(v)) for idx, v in enumerate(tt) if v != 0]
    print("  term0 tensor nonzeros (flat p*81+q*9+s):", nz)
    print("  position (5,8,4): flat=%d, T[5][8][4]=%d"
          % (5 * 81 + 8 * 9 + 4, target(5, 8, 4)))
    print("  decode: p=5=(1,2), q=8=(2,2), s=4=(1,1)")

    trans = [x for x in per_file if "ladT" in x["file"]]
    print("\nTRANSFORMS: %d ladT files, unit-term counts seen: %s"
          % (len(trans), sorted(set(x["unit_terms"] for x in trans))))

    json.dump({"per_file": per_file,
               "distinct_schemes": len(groups),
               "per_file_totals": [tot_u, tot_n],
               "distinct_totals": [du, dn]},
              open(ROOT + "/wave32/gate/recount_g1_results.json", "w"),
              indent=1)
    print("\nwrote wave32/gate/recount_g1_results.json")


if __name__ == "__main__":
    main()
