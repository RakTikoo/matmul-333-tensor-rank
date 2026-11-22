"""Wave 20 Item 1: exact Jacobian nullity at Laderman / Perminov + generic control.

J: 729 x 621, params [U;V;W] each flattened (t,i)->t*9+i (bridge.py convention).
J is an INTEGER matrix for both schemes (all entries in Z), so:
  rank mod p <= rank over Q  =>  nullity mod p >= nullity over Q.
Lower bound on nullity over Q: explicit exact null vectors (torus + isotropy
orbit tangent), verified by exact integer multiplication J v = 0.
"""
import json, sys
import numpy as np
from fractions import Fraction

ROOT = '/home/hatch/workspace/matmul-pilot/'

def load_scheme(path):
    d = json.load(open(path))
    U = np.array([[int(Fraction(x)) for x in row] for row in d['U']], dtype=np.int64)
    V = np.array([[int(Fraction(x)) for x in row] for row in d['V']], dtype=np.int64)
    W = np.array([[int(Fraction(x)) for x in row] for row in d['W']], dtype=np.int64)
    return U, V, W

def jacobian_int(U, V, W):
    r = U.shape[1]
    I9 = np.eye(9, dtype=np.int64)
    JU = np.einsum('pi,qt,st->pqsit', I9, V, W).transpose(0, 1, 2, 4, 3)
    JV = np.einsum('pt,qi,st->pqsit', U, I9, W).transpose(0, 1, 2, 4, 3)
    JW = np.einsum('pt,qt,si->pqsit', U, V, I9).transpose(0, 1, 2, 4, 3)
    return np.concatenate([JU.reshape(729, 9*r), JV.reshape(729, 9*r),
                           JW.reshape(729, 9*r)], axis=1).astype(np.int64)

def jacobian_float(U, V, W):
    r = U.shape[1]
    I9 = np.eye(9)
    JU = np.einsum('pi,qt,st->pqsit', I9, V, W).transpose(0, 1, 2, 4, 3)
    JV = np.einsum('pt,qi,st->pqsit', U, I9, W).transpose(0, 1, 2, 4, 3)
    JW = np.einsum('pt,qt,si->pqsit', U, V, I9).transpose(0, 1, 2, 4, 3)
    return np.concatenate([JU.reshape(729, 9*r), JV.reshape(729, 9*r),
                           JW.reshape(729, 9*r)], axis=1)

def rank_mod(A, p):
    A = (A % p).astype(np.int64)
    m, n = A.shape
    rank = 0
    for col in range(n):
        piv = -1
        for i in range(rank, m):
            if A[i, col] != 0:
                piv = i; break
        if piv < 0:
            continue
        if piv != rank:
            A[[rank, piv]] = A[[piv, rank]]
        inv = pow(int(A[rank, col]), -1, p)
        A[rank] = (A[rank] * inv) % p
        below = A[rank+1:, col].copy()
        nz = below != 0
        if nz.any():
            idx = np.where(nz)[0] + rank + 1
            A[idx] = (A[idx] - np.outer(below[nz], A[rank])) % p
        rank += 1
        if rank == m:
            break
    return rank

def torus_vectors(U, V, W):
    """46 exact kernel vectors: per term t, (u_t in U) - (w_t in W), (v_t in V) - (w_t in W)."""
    r = U.shape[1]; n = 27*r
    vecs = []
    for t in range(r):
        for blk, M in ((0, U), (1, V)):
            v = np.zeros(n, dtype=np.int64)
            v[blk*9*r + t*9: blk*9*r + t*9 + 9] = M[:, t]
            v[2*9*r + t*9: 2*9*r + t*9 + 9] = -W[:, t]
            vecs.append(v)
    return np.array(vecs).T  # 621 x 46

def orbit_vectors(U, V, W):
    """27 vectors: infinitesimal isotropy action of (X,Y,Z) in gl3^3.
    Isotropy triple on the factor spaces: (g (x) h, h^{-T} (x) k, g^{-T} (x) k^{-T})
    (inverse-transposes on the contracted wires). Lie form, column reshaped
    M[a,b]=col[a*3+b], slot actions P (first slot) -> P M, Q (second) -> M Q^T:
    dU = X M + M Y^T ; dV = -Y^T N + N Z^T ; dW = -X^T P - P Z."""
    r = U.shape[1]; n = 27*r
    def act(M, A, B):  # returns (A (x) I + I (x) B) applied to each column of M
        out = np.zeros_like(M)
        for t in range(M.shape[1]):
            Mt = M[:, t].reshape(3, 3)
            out[:, t] = (A @ Mt + Mt @ B.T).ravel()
        return out
    vecs = []
    Z3 = np.zeros((3, 3), dtype=np.int64)
    for which in range(3):          # 0: X nonzero, 1: Y nonzero, 2: Z nonzero
        for a in range(3):
            for b in range(3):
                E = np.zeros((3, 3), dtype=np.int64); E[a, b] = 1
                X = E if which == 0 else Z3
                Y = E if which == 1 else Z3
                Z = E if which == 2 else Z3
                v = np.zeros(n, dtype=np.int64)
                v[0:9*r] = act(U, X, Y).T.ravel()
                v[9*r:18*r] = act(V, -Y.T, Z).T.ravel()
                v[18*r:27*r] = act(W, -X.T, -Z.T).T.ravel()
                vecs.append(v)
    return np.array(vecs).T  # 621 x 27

PRIMES = [1000003, 1000033, 1000037]

def analyse(name, path):
    U, V, W = load_scheme(path)
    r = U.shape[1]
    print(f'=== {name}: r={r}, entries range U[{U.min()},{U.max()}] nnz={np.count_nonzero(U)+np.count_nonzero(V)+np.count_nonzero(W)}')
    J = jacobian_int(U, V, W)
    print('  J shape', J.shape, 'J entries in', (J.min(), J.max()))
    out = {'scheme': name, 'r': r}
    # exact kernel vectors
    Tv = torus_vectors(U, V, W)
    Ov = orbit_vectors(U, V, W)
    assert np.abs(J @ Tv).max() == 0, 'torus vector NOT in kernel!'
    jov = np.abs(J @ Ov).max()
    print(f'  torus: 46 vecs, max|J v| = 0 (exact). orbit: 27 vecs, max|J v| = {jov} (exact int)')
    out['orbit_max_resid'] = int(jov)
    for p in PRIMES:
        rkT = rank_mod(Tv, p); rkO = rank_mod(Ov, p)
        rkTO = rank_mod(np.concatenate([Tv, Ov], axis=1), p)
        rkJ = rank_mod(J, p)
        print(f'  p={p}: rank(torus)={rkT} rank(orbit)={rkO} rank(torus+orbit)={rkTO} '
              f'rank(J)={rkJ} nullity(J) mod p = {621-rkJ}')
        out[f'p{p}'] = {'rank_torus': rkT, 'rank_orbit': rkO, 'rank_span': rkTO,
                        'rank_J': rkJ, 'nullity_J': 621-rkJ}
    # float SVD
    Jf = jacobian_float(U.astype(float), V.astype(float), W.astype(float))
    s = np.linalg.svd(Jf, compute_uv=False)
    for tol in (1e-8, 1e-10, 1e-12):
        print(f'  float SVD nullity @ rel tol {tol:g}: {int((s < tol*s[0]).sum())}')
    print('  smallest 12 singular values:', ['%.2e' % x for x in s[-12:]])
    out['svals_tail'] = [float(x) for x in s[-12:]]
    return out

results = []
results.append(analyse('Laderman', ROOT + 'results/wave4_333_r23_Q_laderman.json'))
results.append(analyse('Perminov-cn122', ROOT + 'results/wave5_333_r23_Q_perminov-cn122.json'))

# generic control: wave3 float ALS point, same code path
d = np.load(ROOT + 'wave3/bridge/best_r23.npz')
Jf = jacobian_float(d['U'], d['V'], d['W'])
s = np.linalg.svd(Jf, compute_uv=False)
print('=== generic ALS control (wave3 best_r23, residual 2.5e-4):')
for tol in (1e-8, 1e-10, 1e-12):
    print(f'  float SVD nullity @ rel tol {tol:g}: {int((s < tol*s[0]).sum())}')
print('  smallest 12 singular values:', ['%.2e' % x for x in s[-12:]])
results.append({'scheme': 'generic-ALS-control', 'svals_tail': [float(x) for x in s[-12:]]})

json.dump(results, open(ROOT + 'wave20/homotopy/item1_numbers.json', 'w'), indent=1)
print('saved item1_numbers.json')
