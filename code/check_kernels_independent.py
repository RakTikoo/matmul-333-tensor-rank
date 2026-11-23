# Independent second-path checker (Wave 28 claim gate).
# check_kernels_independent.py — a from-scratch Brent-Jacobian
# construction that re-pins the kernel dimensions of claims C2/C3
# (Perminov cr58_cn122, the two rank-24 schemes, the rank-26 block
# construction) from both sides at fresh primes, and independently
# rebuilds the trivial tangent spans. Shares no code with
# moduli_exact.py or rigor_check.py. It references the campaign's
# internal file layout; the packaged entry point is check_kernels.py.

#!/usr/bin/env python3
"""Wave 28 GATE — independent nullity check for claims C2/C3.

Fresh code. Builds the Brent Jacobian J of <3,3,3> at a scheme point with
explicit loops, in the gate's own variable order (slot, term, entry).
Pins nullity_Q(J) two-sided:
  upper: rank of J mod p at three fresh primes (not used by Waves 20-22
         or by the Wave-21 rigor pass);
  lower: the kernel bases stored by the original waves are checked
         against THIS J (J.v = 0 exactly, integer arithmetic) and their
         rank mod p is computed -- after identifying the stored vectors'
         coordinate order by testing candidate permutations (the
         annihilation test itself adjudicates).
Also independently builds the torus tangents and the isotropy-orbit
tangents (Lie action of (g x h, h^-T x k, g^-T x k^-T)) and measures
their span mod p, as a second path for the trivial-span figures.
"""
import json, sys
import numpy as np
from fractions import Fraction
from pathlib import Path

ROOT = Path.home() / "workspace" / "matmul-pilot"
PRIMES = [104729, 1299709, 15485863]   # the 10_000th, 100_000th, 1_000_000th primes

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1 if i == 2 else 2
    return True

assert all(is_prime(p) for p in PRIMES)

def load(path):
    d = json.loads(Path(path).read_text())
    def conv(M):
        out = []
        for row in M:
            r = []
            for x in row:
                f = Fraction(str(x))
                assert f.denominator == 1, f"non-integer entry {x} in {path}"
                r.append(int(f))
            out.append(r)
        return out
    return conv(d["U"]), conv(d["V"]), conv(d["W"])

def check_scheme(U, V, W):
    """Own exact reconstruction: sum of outer products == T ?"""
    r = len(U[0])
    bad = 0
    for p in range(9):
        for q in range(9):
            for s in range(9):
                acc = sum(U[p][t] * V[q][t] * W[s][t] for t in range(r))
                i, j = divmod(p, 3)
                j2, k = divmod(q, 3)
                i2, k2 = divmod(s, 3)
                want = 1 if (j == j2 and i == i2 and k == k2) else 0
                if acc != want:
                    bad += 1
    return bad

def build_J(U, V, W):
    """Dense integer Jacobian, rows (p,q,s) lexicographic,
    cols (slot, term, entry) lexicographic. Explicit loops."""
    r = len(U[0])
    n = 27 * r
    J = np.zeros((729, n), dtype=np.int64)
    def col(slot, t, a):
        return slot * (9 * r) + t * 9 + a
    for p in range(9):
        for q in range(9):
            for s in range(9):
                row = p * 81 + q * 9 + s
                for t in range(r):
                    J[row, col(0, t, p)] += V[q][t] * W[s][t]
                    J[row, col(1, t, q)] += U[p][t] * W[s][t]
                    J[row, col(2, t, s)] += U[p][t] * V[q][t]
    return J

def rank_mod(A, p):
    A = (A.astype(np.int64) % p).copy()
    rows, cols = A.shape
    rank = 0
    r0 = 0
    for c in range(cols):
        piv = -1
        for i in range(r0, rows):
            if A[i, c] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        if piv != r0:
            A[[r0, piv]] = A[[piv, r0]]
        inv = pow(int(A[r0, c]) % p, -1, p)
        A[r0] = (A[r0] * inv) % p
        # eliminate below only (rank computation)
        below = A[r0 + 1:]
        factors = below[:, c].copy()
        nz = factors != 0
        if nz.any():
            below[nz] = (below[nz] - factors[nz][:, None] * A[r0][None, :]) % p
        rank += 1
        r0 += 1
        if r0 == rows:
            break
    return rank

def orderings(r):
    def o1(s, t, a): return s * (9 * r) + t * 9 + a
    def o2(s, t, a): return s * (9 * r) + a * r + t
    def o3(s, t, a): return t * 27 + s * 9 + a
    def o4(s, t, a): return t * 27 + a * 3 + s
    def o5(s, t, a): return a * (3 * r) + s * r + t
    def o6(s, t, a): return a * (3 * r) + t * 3 + s
    return {"o1": o1, "o2": o2, "o3": o3, "o4": o4, "o5": o5, "o6": o6}

def perm_for(order_fn, r):
    """perm[my_col] = position of that variable in the stored vector order."""
    perm = np.empty(27 * r, dtype=int)
    for s in range(3):
        for t in range(r):
            for a in range(9):
                mine = s * (9 * r) + t * 9 + a
                perm[mine] = order_fn(s, t, a)
    return perm

def mat3(vec9):
    return [[vec9[3 * i + j] for j in range(3)] for i in range(3)]

def matmul(A, B):
    return [[sum(A[i][x] * B[x][j] for x in range(3)) for j in range(3)] for i in range(3)]

def transpose(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]

def add(A, B, s=1):
    return [[A[i][j] + s * B[i][j] for j in range(3)] for i in range(3)]

def tangents(U, V, W):
    """Torus + orbit tangent vectors in my (slot, term, entry) order, as
    integer vectors (scheme entries are integers)."""
    r = len(U[0])
    n = 27 * r
    def col(slot, t, a):
        return slot * (9 * r) + t * 9 + a
    vecs = []
    # torus: per term, the 2-dim scaling-tangent space
    # {(a*u, b*v, c*w) : a+b+c = 0}, basis (u,-v,0) and (u,0,-w)
    for t in range(r):
        for s2 in (1, 2):
            v = np.zeros(n, dtype=np.int64)
            for a in range(9):
                v[col(0, t, a)] = U[a][t]
                v[col(s2, t, a)] = -(U, V, W)[s2][a][t]
            vecs.append(v)
    torus_count = len(vecs)
    # orbit: Lie action of (g x h, h^-T x k, g^-T x k^-T);
    # X = Lie(g) [i-index], Y = Lie(h) [j-index], Z = Lie(k) [k-index]
    #   u' = X u + u Y^T ;  v' = -Y^T v + v Z^T ;  w' = -X^T w - w Z
    basis = []
    for which in range(3):
        for a in range(3):
            for b in range(3):
                E = [[1 if (i == a and j == b) else 0 for j in range(3)] for i in range(3)]
                trip = [[[0]*3 for _ in range(3)] for _ in range(3)]
                trip[which] = E
                basis.append(tuple(trip))
    for (X, Y, Z) in basis:
        v = np.zeros(n, dtype=np.int64)
        Xt, Yt = transpose(X), transpose(Y)
        for t in range(r):
            u = mat3([U[a][t] for a in range(9)])
            w_ = mat3([W[a][t] for a in range(9)])
            vv = mat3([V[a][t] for a in range(9)])
            du = add(matmul(X, u), matmul(u, Yt))
            dv = add(matmul(vv, transpose(Z)), matmul(Yt, vv), s=-1) if False else \
                 [[-matmul(Yt, vv)[i][j] + matmul(vv, transpose(Z))[i][j] for j in range(3)] for i in range(3)]
            dw = [[-matmul(Xt, w_)[i][j] - matmul(w_, Z)[i][j] for j in range(3)] for i in range(3)]
            for slot, M in enumerate((du, dv, dw)):
                for i in range(3):
                    for j in range(3):
                        v[col(slot, t, 3 * i + j)] = M[i][j]
        vecs.append(v)
    return vecs, torus_count

POINTS = [
    ("T11", "wave25/t11/wave25_333_r23_Q_T11.json", "wave25/t11/kernel_T11.npz", 94, 70),
    ("metaflip24", "wave22/ladder/wave22_333_r24_Q_metaflip.json", "wave22/ladder/kernel_metaflip24.npz", 102, 72),
    ("proj24", "wave22/ladder/wave22_333_r24_Q_proj.json", "wave22/ladder/kernel_proj24.npz", 111, 72),
    ("lensC26", "results/lensC_333_r26_Q.json", "wave22/ladder/kernel_lensC26.npz", 187, 73),
]

results = {}
for name, scheme_rel, npz_rel, claimed_null, claimed_span in POINTS:
    print(f"\n===== {name} =====")
    U, V, W = load(ROOT / scheme_rel)
    r = len(U[0])
    n = 27 * r
    bad = check_scheme(U, V, W)
    print(f"r={r}, vars={n}, own reconstruction wrong entries: {bad}")
    J = build_J(U, V, W)
    ranks = {}
    for p in PRIMES:
        ranks[p] = rank_mod(J, p)
    nulls = {p: n - ranks[p] for p in PRIMES}
    print(f"rank(J) mod p: {ranks} -> nullity upper bounds: {nulls}")

    # --- kernel basis check ---
    d = np.load(ROOT / npz_rel, allow_pickle=True)
    vecs = d["vecs"]
    k = vecs.shape[0]
    print(f"stored basis: {k} vectors of length {vecs.shape[1]} (claimed nullity {claimed_null})")
    Bfrac = [[Fraction(str(x)) for x in row] for row in vecs]
    assert all(f.denominator == 1 for row in Bfrac for f in row), "fractional basis entries!"
    Bstored = np.array([[int(f) for f in row] for row in Bfrac], dtype=np.int64)
    chosen = None
    for oname, ofn in orderings(r).items():
        perm = perm_for(ofn, r)
        Bmine = Bstored[:, perm]           # columns reordered into my order
        ok = all(not (J @ Bmine[i]).any() for i in range(min(3, k)))
        print(f"  ordering {oname}: first-3 annihilation: {ok}")
        if ok:
            chosen = (oname, Bmine)
            break
    if chosen is None:
        print("  !! no candidate ordering annihilates -- basis check FAILED")
        results[name] = {"error": "ordering not found"}
        continue
    oname, Bmine = chosen
    badvecs = sum(0 if not (J @ Bmine[i]).any() else 1 for i in range(k))
    brank = rank_mod(Bmine, PRIMES[0])
    print(f"  ordering identified: {oname}; vectors failing J.v=0: {badvecs}/{k}; basis rank mod {PRIMES[0]}: {brank}")
    pinned = (len(set(nulls.values())) == 1 and nulls[PRIMES[0]] == k == brank and badvecs == 0)
    print(f"  nullity pinned at {k}: {pinned} (claimed {claimed_null})")

    # --- trivial span second path ---
    tvecs, tc = tangents(U, V, W)
    Tmat = np.array(tvecs, dtype=np.int64)
    tan_bad = sum(0 if not (J @ Tmat[i]).any() else 1 for i in range(len(tvecs)))
    span = rank_mod(Tmat, PRIMES[0])
    torus_span = rank_mod(Tmat[:tc], PRIMES[0])
    orbit_span = rank_mod(Tmat[tc:], PRIMES[0])
    print(f"  tangents: {len(tvecs)} built ({tc} torus + {len(tvecs)-tc} orbit); failing J.v=0: {tan_bad}")
    print(f"  span mod {PRIMES[0]}: torus {torus_span}, orbit {orbit_span}, combined {span} (claimed trivial span {claimed_span})")
    results[name] = {
        "r": r, "scheme_wrong": bad, "rank_mod": {str(p): ranks[p] for p in PRIMES},
        "nullity_upper": {str(p): nulls[p] for p in PRIMES},
        "basis_k": k, "ordering": oname, "basis_bad": badvecs, "basis_rank": brank,
        "pinned": pinned, "claimed_nullity": claimed_null,
        "tangent_bad": tan_bad, "torus_span": torus_span, "orbit_span": orbit_span,
        "span": span, "claimed_span": claimed_span,
    }

(ROOT / "wave28/gate/nullity_results.json").write_text(json.dumps(results, indent=1))
print("\nwrote wave28/gate/nullity_results.json")
