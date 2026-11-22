"""RIGOR agent, Wave 21: adversarial re-check of the Wave-20 nullity claim.

Independent implementation: J built from scheme files with explicit
loops (no import of the homotopy agent's code); rank mod p by numpy
Gaussian elimination; kernel artefacts checked by exact integer
sparse matvec; trivial bases built from the Lie-action formulas
derived in REPORT.md (inverse-transposes on contracted wires).
Variable order: [U; V; W], each block term-major (t,i) -> t*9+i,
row order (a,b,c) -> a*81+b*9+c.  J[(a,b,c), U(t,i)] = d(a,i) V[b,t] W[c,t],
J[(a,b,c), V(t,i)] = d(b,i) U[a,t] W[c,t], J[(a,b,c), W(t,i)] = d(c,i) U[a,t] V[b,t].
"""
import json, sys, time
import numpy as np
from fractions import Fraction

ROOT = '/home/hatch/workspace/matmul-pilot/'
LAD = ROOT + 'results/wave4_333_r23_Q_laderman.json'
PERM = ROOT + 'results/wave5_333_r23_Q_perminov-cn122.json'

def load_scheme(path):
    d = json.load(open(path))
    U = np.array([[int(Fraction(x)) for x in row] for row in d['U']], dtype=np.int64)
    V = np.array([[int(Fraction(x)) for x in row] for row in d['V']], dtype=np.int64)
    W = np.array([[int(Fraction(x)) for x in row] for row in d['W']], dtype=np.int64)
    assert U.shape == V.shape == W.shape == (9, 23)
    return U, V, W

def build_J(U, V, W):
    """Dense int64 J (729 x 621), built by explicit loops."""
    r = 23
    J = np.zeros((729, 621), dtype=np.int64)
    for a in range(9):
        for b in range(9):
            for c in range(9):
                row = a * 81 + b * 9 + c
                for t in range(r):
                    uv = int(V[b, t]) * int(W[c, t])
                    if uv:
                        J[row, t * 9 + a] += uv
                    uw = int(U[a, t]) * int(W[c, t])
                    if uw:
                        J[row, 207 + t * 9 + b] += uw
                    uv2 = int(U[a, t]) * int(V[b, t])
                    if uv2:
                        J[row, 414 + t * 9 + c] += uv2
    return J

def sparse_rows(J):
    rows = []
    for i in range(J.shape[0]):
        nz = [(int(j), int(J[i, j])) for j in np.nonzero(J[i])[0]]
        rows.append(nz)
    return rows

def is_prime(n):
    if n < 2: return False
    small = [2,3,5,7,11,13,17,19,23,29,31,37]
    for q in small:
        if n % q == 0: return n == q
    d = n - 1; s = 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in [2, 7, 61]:  # deterministic for n < 2^32
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else:
            return False
    return True

def rank_mod(A, p):
    """Rank of integer matrix A over F_p (numpy elimination, exact)."""
    M = np.array(A, dtype=np.int64) % p
    nrows, ncols = M.shape
    rank = 0
    for col in range(ncols):
        if rank >= nrows: break
        piv = -1
        for i in range(rank, nrows):
            if M[i, col] != 0:
                piv = i; break
        if piv < 0: continue
        if piv != rank:
            M[[rank, piv]] = M[[piv, rank]]
        inv = pow(int(M[rank, col]), -1, p)
        if inv != 1:
            M[rank] = (M[rank] * inv) % p
        if rank + 1 < nrows:
            fac = M[rank + 1:, col].copy()
            nz = fac != 0
            if nz.any():
                sub = M[rank + 1:, col:]
                sub[nz] = (sub[nz] - np.outer(fac[nz], M[rank, col:])) % p
        rank += 1
    return rank

def torus_basis(U, V, W):
    vecs = []
    for t in range(23):
        v1 = np.zeros(621, dtype=np.int64)
        v1[t*9:t*9+9] = U[:, t]
        v1[207+t*9:207+t*9+9] = -V[:, t]
        vecs.append(v1)
        v2 = np.zeros(621, dtype=np.int64)
        v2[t*9:t*9+9] = U[:, t]
        v2[414+t*9:414+t*9+9] = -W[:, t]
        vecs.append(v2)
    return np.array(vecs).T  # 621 x 46

def orbit_basis(U, V, W, corrected=True):
    """27 Lie directions (X,Y,Z) each = E_pq. Tangent formulas (corrected):
    du = X A + A Y^T ; dv = -Y^T B + B Z^T ; dw = -X^T C - C Z.
    Naive (wrong) version: dv = -Y B + B Z^T ; dw = -X C - C Z^T.
    A,B,C are the 3x3 reshapes of the factor columns (row-major)."""
    vecs = []
    for which in range(3):          # 0:X, 1:Y, 2:Z
        for p in range(3):
            for q in range(3):
                E = np.zeros((3, 3), dtype=np.int64); E[p, q] = 1
                X = E if which == 0 else np.zeros((3, 3), dtype=np.int64)
                Y = E if which == 1 else np.zeros((3, 3), dtype=np.int64)
                Z = E if which == 2 else np.zeros((3, 3), dtype=np.int64)
                v = np.zeros(621, dtype=np.int64)
                for t in range(23):
                    A = U[:, t].reshape(3, 3); B = V[:, t].reshape(3, 3); C = W[:, t].reshape(3, 3)
                    du = X @ A + A @ Y.T
                    if corrected:
                        dv = -Y.T @ B + B @ Z.T
                        dw = -X.T @ C - C @ Z
                    else:
                        dv = -Y @ B + B @ Z.T
                        dw = -X @ C - C @ Z.T
                    v[t*9:t*9+9] = du.reshape(-1)
                    v[207+t*9:207+t*9+9] = dv.reshape(-1)
                    v[414+t*9:414+t*9+9] = dw.reshape(-1)
                vecs.append(v)
    return np.array(vecs).T  # 621 x 27

def matvec_int(rows, v):
    """Exact integer J.v via sparse rows; v a list/array of Python ints."""
    out = []
    for nz in rows:
        s = 0
        for j, val in nz:
            if v[j]:
                s += val * int(v[j])
        out.append(s)
    return out

def load_kernel(name):
    z = np.load(ROOT + f'wave20/homotopy/kernel_{name}.npz', allow_pickle=True)
    arr = z['vecs']  # (n, 621) strings
    vecs = [[int(x) for x in row] for row in arr]
    return vecs

def main():
    t0 = time.time()
    log = open(ROOT + 'wave21/rigor/OUTCOMES.md', 'w')
    def say(s):
        print(s, flush=True); log.write(s + '\n'); log.flush()
    say('# Wave 21 (rigor) — OUTCOMES (checkpointed as tests land)\n')
    primes = [999983, 999979, 999961, 10000019, 10000079]
    say('Primes (all NOT in agent set {1000003,1000033,1000037}): ' +
        ', '.join(f'{p} prime={is_prime(p)}' for p in primes))
    assert all(is_prime(p) for p in primes)
    schemes = [('laderman', LAD, 76), ('perminov', PERM, 94)]
    for name, path, claim in schemes:
        U, V, W = load_scheme(path)
        say(f'\n## {name}: claim nullity_Q = {claim}')
        J = build_J(U, V, W)
        say(f'J built: shape {J.shape}, entries in {sorted(set(J.reshape(-1).tolist()))}, nnz={int((J!=0).sum())}')
        rows = sparse_rows(J)
        # Test 2: independent rank at 5 fresh primes
        for p in primes:
            t = time.time()
            r = rank_mod(J, p)
            nul = 621 - r
            verdict = 'OK' if nul >= claim else '*** CLAIM FALSE ***'
            say(f'  rank mod {p}: rank={r} nullity={nul} (claim {claim}) {verdict} [{time.time()-t:.1f}s]')
            if nul < claim:
                say('  STOP: nullity below claim at a fresh prime.'); return
        # Test 3: kernel artefacts
        vecs = load_kernel(name)
        say(f'  kernel artefact: {len(vecs)} vectors, each length {len(vecs[0])} (claim {claim})')
        bad = 0
        for i, v in enumerate(vecs):
            mv = matvec_int(rows, v)
            if any(x != 0 for x in mv):
                bad += 1
                say(f'    vector {i}: J.v != 0 (max|.|={max(abs(x) for x in mv)})')
        say(f'  J.v = 0 exact over Z: {len(vecs)-bad}/{len(vecs)} pass')
        # independence mod 2 fresh primes
        B = np.array(vecs, dtype=np.int64)  # n x 621
        for p in [999983, 999979]:
            rk = rank_mod(B, p)
            say(f'  basis rank mod {p}: {rk} (expect {len(vecs)}) {"OK" if rk == len(vecs) else "*** FAIL ***"}')
        # Test 4: trivial bases
        T = torus_basis(U, V, W)
        O = orbit_basis(U, V, W, corrected=True)
        On = orbit_basis(U, V, W, corrected=False)
        def rank_of(M, p=999983):
            return rank_mod(M.T, p)  # M is 621 x k; rank of columns
        say(f'  torus dim mod 999983: {rank_of(T)} (expect 46)')
        say(f'  orbit dim mod 999983: {rank_of(O)} (expect 26)')
        say(f'  span(torus+orbit) dim: {rank_of(np.concatenate([T, O], axis=1))} (expect 70)')
        # every trivial vector in ker J exactly
        for nm, M in [('torus', T), ('orbit-corrected', O), ('orbit-naive', On)]:
            badt = 0
            for i in range(M.shape[1]):
                mv = matvec_int(rows, [int(x) for x in M[:, i]])
                if any(x != 0 for x in mv): badt += 1
            say(f'  J.v=0 exact: {nm}: {M.shape[1]-badt}/{M.shape[1]} pass')
        # agent kernel contains trivial span?
        KB = np.array(vecs, dtype=np.int64).T  # 621 x n
        comb = np.concatenate([T, O, KB], axis=1)
        rk = rank_of(comb)
        say(f'  rank(span[trivial + agent kernel]) mod 999983: {rk} (expect {claim} if trivial subset of kernel)')
        say(f'  -> genuine moduli = {claim} - 70 = {claim-70} (if trivial span is 70 and inside kernel)')
    say(f'\nTotal wall: {time.time()-t0:.0f}s')

if __name__ == '__main__':
    main()
