"""Exact rational nullspace of J at Laderman / Perminov via mod-p RREF + CRT
+ rational reconstruction, every vector verified by exact integer J v = 0.
Success => nullity over Q is EXACT (upper bound: rank mod p; lower bound:
exhibited independent exact kernel vectors)."""
import json
import numpy as np
from fractions import Fraction
import sys
sys.path.insert(0, '/home/hatch/workspace/matmul-pilot/wave20/homotopy')
src = open('/home/hatch/workspace/matmul-pilot/wave20/homotopy/item1.py').read()
exec(src.split('PRIMES =')[0])  # defs only: load_scheme, jacobian_int, rank_mod, ...

PRIMES = [1000003, 1000033, 1000037]

def rref_nullspace_mod(J, p):
    """Return (pivot_cols, N) with N a 621 x nullity int64 matrix mod p:
    RREF basis (free variables form an identity block)."""
    A = (J % p).astype(np.int64)
    m, n = A.shape
    pivots = []
    row = 0
    for col in range(n):
        piv = -1
        for i in range(row, m):
            if A[i, col] != 0:
                piv = i; break
        if piv < 0:
            continue
        if piv != row:
            A[[row, piv]] = A[[piv, row]]
        inv = pow(int(A[row, col]), -1, p)
        A[row] = (A[row] * inv) % p
        # eliminate this column from ALL other rows (full RREF)
        fac = A[:, col].copy(); fac[row] = 0
        nz = np.where(fac != 0)[0]
        if len(nz):
            A[nz] = (A[nz] - np.outer(fac[nz], A[row])) % p
        pivots.append(col)
        row += 1
        if row == m:
            break
    free = [c for c in range(n) if c not in set(pivots)]
    N = np.zeros((n, len(free)), dtype=np.int64)
    for j, f in enumerate(free):
        N[f, j] = 1
        for i, pc in enumerate(pivots):
            N[pc, j] = (-A[i, f]) % p
    return pivots, N

def rat_reconstruct(x, M, bound):
    """Find a/b with b>0, |a|<=bound, b<=bound, a = b*x (mod M). None if fail."""
    # extended Euclid on (M, x)
    r0, r1 = M, x % M
    s0, s1 = 0, 1  # coefficient of x
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    a, b = r1, s1
    if b < 0:
        a, b = -a, -b
    if b == 0 or b > bound or abs(a) > bound:
        return None
    if (b * (x % M) - a) % M != 0:
        return None
    return Fraction(a, b)

def process(name, path):
    U, V, W = load_scheme(ROOT + path)
    J = jacobian_int(U, V, W)
    n = J.shape[1]
    bases = []
    piv0 = None
    for p in PRIMES:
        piv, N = rref_nullspace_mod(J, p)
        if piv0 is None:
            piv0 = piv
        assert piv == piv0, f'pivot sets differ at p={p}'
        bases.append(N)
        print(f'{name} p={p}: nullity mod p = {N.shape[1]}')
    nullity = bases[0].shape[1]
    M = 1
    for p in PRIMES:
        M *= p
    # CRT per entry
    vecs = []
    ok_entries = 0; tot_entries = 0
    for j in range(nullity):
        col = []
        good = True
        for i in range(n):
            tot_entries += 1
            residues = [int(bases[k][i, j]) for k in range(3)]
            # Garner / direct CRT (primes pairwise coprime)
            x = residues[0]
            mcur = PRIMES[0]
            for k in (1, 2):
                t = ((residues[k] - x) * pow(mcur, -1, PRIMES[k])) % PRIMES[k]
                x += mcur * t
                mcur *= PRIMES[k]
            if x == 0:
                col.append(Fraction(0)); ok_entries += 1; continue
            fr = None
            for bound in (10**6, 10**7, 10**8):
                fr = rat_reconstruct(x, M, bound)
                if fr is not None:
                    break
            if fr is None:
                good = False
                col.append(None)
            else:
                col.append(fr); ok_entries += 1
        vecs.append((col, good))
    print(f'{name}: entries reconstructed {ok_entries}/{tot_entries}')
    # verify exactly over Z (clear denominators, big-int dot)
    Jo = J.astype(object)
    verified = []
    for col, good in vecs:
        if not good:
            continue
        den = 1
        for fr in col:
            den = den * fr.denominator // np.gcd(den, fr.denominator)
        vint = np.array([int(fr * den) for fr in col], dtype=object)
        if all(v == 0 for v in Jo @ vint):
            verified.append(vint)
    print(f'{name}: vectors verified J v = 0 over Z exactly: {len(verified)}/{nullity}')
    if verified:
        Vm = np.array([[int(x) for x in v] for v in verified], dtype=np.int64) \
            if all(abs(int(x)) < 2**62 for v in verified for x in v) else None
        rankv = rank_mod(np.array(verified, dtype=object).astype(np.int64), PRIMES[0]) \
            if Vm is not None else None
        print(f'{name}: rank of verified set mod {PRIMES[0]} = {rankv}')
        np.savez(ROOT + f'wave20/homotopy/kernel_{name}.npz',
                 vecs=np.array([[str(x) for x in v] for v in verified]))
        return {'scheme': name, 'nullity_modp': nullity,
                'verified_exact': len(verified), 'rank_verified': rankv}
    return {'scheme': name, 'nullity_modp': nullity, 'verified_exact': 0}

out = []
out.append(process('laderman', 'results/wave4_333_r23_Q_laderman.json'))
out.append(process('perminov', 'results/wave5_333_r23_Q_perminov-cn122.json'))
json.dump(out, open(ROOT + 'wave20/homotopy/nullspace_exact.json', 'w'), indent=1)
print(out)
