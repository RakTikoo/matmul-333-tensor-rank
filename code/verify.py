#!/usr/bin/env python3
"""
verify.py — Exact verifier for matrix-multiplication tensor decompositions.

A decomposition of format <a,b,c> with rank r is three matrices:
  U : (a*b) x r   coefficients over the entries of A (a x b), row-major
  V : (b*c) x r   coefficients over the entries of B (b x c), row-major
  W : (a*c) x r   coefficients over the entries of C (a x c), row-major

It is correct iff for every (p, q, s):
  sum_t U[p][t] * V[q][t] * W[s][t] == T[p][q][s]
where T is the matmul tensor:
  p = (i, j)  indexes A[i][j]
  q = (j2, k) indexes B[j2][k]
  s = (i2, k2) indexes C[i2][k2]
  T = 1 iff j == j2 and i == i2 and k == k2, else 0.

Verification is EXACT: over Q using fractions.Fraction, over F2 using ints mod 2.
No floating point anywhere in the decision path.

Result file format (JSON):
  {"a":2,"b":2,"c":2,"field":"Q","U":[[...],...],"V":[[...],...],"W":[[...],...]}
Entries may be ints, or strings "p/q" for rationals (Q only). Rank r = number of columns.

CLI:
  python3 verify.py check <file.json>     -> prints VERIFIED / REJECTED, exit 0/1
  python3 verify.py selftest              -> runs the paranoid self-test suite
  python3 verify.py mismatch <file.json>  -> prints mismatch stats (for search lenses)
"""
import json
import sys
from fractions import Fraction


# ---------- core ----------

def target_entry(a, b, c, p, q, s):
    """Matmul tensor entry T[p][q][s] in {0,1}."""
    i, j = divmod(p, b)
    j2, k = divmod(q, c)
    i2, k2 = divmod(s, c)
    return 1 if (j == j2 and i == i2 and k == k2) else 0


def _parse_entry(x, field):
    if field == "F2":
        if isinstance(x, str):
            x = int(x)
        return int(x) % 2
    # Q
    if isinstance(x, str):
        return Fraction(x)
    if isinstance(x, float):
        raise ValueError("float entries are forbidden in exact verification")
    return Fraction(x)


def load_decomposition(path):
    with open(path) as f:
        d = json.load(f)
    return d


def normalize(d):
    """Return (a,b,c,field,U,V,W) with entries as Fraction (Q) or int 0/1 (F2).
    Raises ValueError on any shape/format problem."""
    a, b, c = int(d["a"]), int(d["b"]), int(d["c"])
    field = d.get("field", "Q")
    if field not in ("Q", "F2"):
        raise ValueError(f"unknown field {field!r}")
    raw = {}
    for name, rows_expected in (("U", a * b), ("V", b * c), ("W", a * c)):
        M = d[name]
        if len(M) != rows_expected:
            raise ValueError(f"{name} has {len(M)} rows, expected {rows_expected}")
        raw[name] = M
    r = len(raw["U"][0]) if raw["U"] else 0
    if r == 0:
        raise ValueError("rank 0 decomposition")
    out = {}
    for name in ("U", "V", "W"):
        M = raw[name]
        parsed = []
        for row in M:
            if len(row) != r:
                raise ValueError(f"{name} rows have inconsistent lengths")
            parsed.append([_parse_entry(x, field) for x in row])
        out[name] = parsed
    return a, b, c, field, out["U"], out["V"], out["W"]


def mismatch_stats(a, b, c, field, U, V, W):
    """Return (num_wrong_entries, total_entries, sum_abs_error_as_float).
    num_wrong_entries == 0  <=>  decomposition is exactly correct.
    For F2, errors are counted mod 2. For Q, exact Fraction comparison."""
    na, nb, nc = a * b, b * c, a * c
    r = len(U[0])
    wrong = 0
    total = na * nb * nc
    abs_err = 0.0
    for p in range(na):
        for q in range(nb):
            # partial sums over s handled inside; compute column products once
            for s in range(nc):
                acc = 0 if field == "F2" else Fraction(0)
                for t in range(r):
                    acc += U[p][t] * V[q][t] * W[s][t]
                if field == "F2":
                    acc %= 2
                tgt = target_entry(a, b, c, p, q, s)
                if acc != tgt:
                    wrong += 1
                    try:
                        abs_err += abs(float(acc) - tgt)
                    except Exception:
                        abs_err += 1.0
    return wrong, total, abs_err


def verify_dict(d):
    """Return (ok: bool, info: dict). Never raises for bad decompositions;
    raises only via normalize errors which are caught and reported as reject."""
    try:
        a, b, c, field, U, V, W = normalize(d)
    except Exception as e:
        return False, {"error": f"format: {e}"}
    wrong, total, abs_err = mismatch_stats(a, b, c, field, U, V, W)
    r = len(U[0])
    return wrong == 0, {
        "format": f"<{a},{b},{c}>", "field": field, "rank": r,
        "wrong_entries": wrong, "total_entries": total, "abs_error": abs_err,
    }


def verify_file(path):
    return verify_dict(load_decomposition(path))


# ---------- known decompositions (for self-tests and Lens C seeds) ----------

def naive(a, b, c):
    """Naive decomposition, rank a*b*c."""
    na, nb, nc = a * b, b * c, a * c
    terms = []
    for i in range(a):
        for j in range(b):
            for k in range(c):
                terms.append(((i * b + j), (j * c + k), (i * c + k)))
    r = len(terms)
    U = [[0] * r for _ in range(na)]
    V = [[0] * r for _ in range(nb)]
    W = [[0] * r for _ in range(nc)]
    for t, (p, q, s) in enumerate(terms):
        U[p][t] = 1
        V[q][t] = 1
        W[s][t] = 1
    return {"a": a, "b": b, "c": c, "field": "Q", "U": U, "V": V, "W": W}


def strassen():
    """Strassen's rank-7 decomposition of <2,2,2> over Z (works over any ring).
    Entry order row-major: [11, 12, 21, 22] for each of A, B, C."""
    # columns:        M1        M2         M3          M4          M5         M6          M7
    U = [
        [1, 0, 1, 0, 1, -1, 0],   # a11
        [0, 0, 0, 0, 1, 0, 1],    # a12
        [0, 1, 0, 0, 0, 1, 0],    # a21
        [1, 1, 0, 1, 0, 0, -1],   # a22
    ]
    V = [
        [1, 1, 0, -1, 0, 1, 0],   # b11
        [0, 0, 1, 0, 0, 1, 0],    # b12
        [0, 0, 0, 1, 0, 0, 1],    # b21
        [1, 0, -1, 0, 1, 0, 1],   # b22
    ]
    W = [
        [1, 0, 0, 1, -1, 0, 1],   # c11
        [0, 0, 1, 0, 1, 0, 0],    # c12
        [0, 1, 0, 1, 0, 0, 0],    # c21
        [1, -1, 1, 0, 0, 1, 0],   # c22
    ]
    return {"a": 2, "b": 2, "c": 2, "field": "Q", "U": U, "V": V, "W": W}


def strassen_squared():
    """Rank-49 decomposition of <4,4,4> by applying Strassen recursively
    (Kronecker product of the <2,2,2> scheme with itself). Built by composing
    the bilinear algorithm: treat 4x4 as 2x2 blocks of 2x2 matrices.
    Constructed directly at the tensor level via block substitution:
    each outer Strassen term combines 2x2 blocks; each block product is itself
    a <2,2,2> product done by Strassen. Implemented by explicit composition
    of the two bilinear maps on indices."""
    S = strassen()
    # Outer level: A,B,C are 2x2 blocks; block (I,J) of A is a 2x2 matrix.
    # Global index: A entry (i,j), i,j in 0..3. Block I=i//2, i_in=i%2 etc.
    # Outer term t uses block-combinations Uo[.][t] etc.; inner term u expands
    # each block product. The composed coefficient for A entry (i,j) in term
    # (t,u) is Uo[blockA][t] * Ui[inA][u] where the inner A-factor of the block
    # product (X*Y) uses X = the A-block combination, Y = the B-block combination.
    Uo, Vo, Wo = S["U"], S["V"], S["W"]
    na = 16
    U = [[0] * 49 for _ in range(na)]
    V = [[0] * 49 for _ in range(na)]
    W = [[0] * 49 for _ in range(na)]
    col = 0
    for t in range(7):
        for u in range(7):
            for i in range(4):
                for j in range(4):
                    I, ii = divmod(i, 2)
                    J, jj = divmod(j, 2)
                    blk = I * 2 + J
                    inn = ii * 2 + jj
                    U[i * 4 + j][col] = Uo[blk][t] * Uo[inn][u]
                    # B entry (j,k): block (J,K), inner (jj,kk)
                    # handled in V loop below via same col
            for j in range(4):
                for k in range(4):
                    J, jj = divmod(j, 2)
                    K, kk = divmod(k, 2)
                    blk = J * 2 + K
                    inn = jj * 2 + kk
                    V[j * 4 + k][col] = Vo[blk][t] * Vo[inn][u]
            for i in range(4):
                for k in range(4):
                    I, ii = divmod(i, 2)
                    K, kk = divmod(k, 2)
                    blk = I * 2 + K
                    inn = ii * 2 + kk
                    W[i * 4 + k][col] = Wo[blk][t] * Wo[inn][u]
            col += 1
    return {"a": 4, "b": 4, "c": 4, "field": "Q", "U": U, "V": V, "W": W}


# ---------- self-tests ----------

def _copy(d):
    return json.loads(json.dumps(d))


def selftest():
    import random
    failures = []

    def expect(name, d, want):
        ok, info = verify_dict(d)
        status = "ok" if ok == want else "FAIL"
        if ok != want:
            failures.append((name, want, ok, info))
        print(f"  [{status}] {name}: verified={ok} (want {want}) {info}")

    print("== accepts: known-good decompositions ==")
    expect("naive <2,2,2> rank 8 over Q", naive(2, 2, 2), True)
    expect("naive <3,3,3> rank 27 over Q", naive(3, 3, 3), True)
    expect("naive <2,2,3> rank 12 over Q", naive(2, 2, 3), True)
    expect("Strassen <2,2,2> rank 7 over Q", strassen(), True)
    s2 = _copy(strassen()); s2["field"] = "F2"
    s2 = {**s2, "U": [[x % 2 for x in row] for row in s2["U"]],
          "V": [[x % 2 for x in row] for row in s2["V"]],
          "W": [[x % 2 for x in row] for row in s2["W"]]}
    expect("Strassen <2,2,2> rank 7 reduced mod 2 over F2", s2, True)
    n2 = _copy(naive(3, 3, 3)); n2["field"] = "F2"
    expect("naive <3,3,3> rank 27 over F2", n2, True)
    expect("Strassen-squared <4,4,4> rank 49 over Q", strassen_squared(), True)

    print("== accepts: fractional coefficients (halves) ==")
    # Split Strassen term 0 into two half-weight copies -> rank 8, still exact.
    d = _copy(strassen())
    for name in ("U", "V", "W"):
        for row in d[name]:
            row.append(row[0])
    for row in d["W"]:
        half = str(Fraction(row[0], 2))
        row[0] = half
        row[7] = half
    expect("Strassen with term split into halves, rank 8 over Q", d, True)

    print("== rejects: EVERY single-entry perturbation of Strassen ==")
    base = strassen()
    n_pert = 0
    bad = 0
    for name in ("U", "V", "W"):
        for p in range(len(base[name])):
            for t in range(7):
                for delta in (1, -1):
                    d = _copy(base)
                    d[name][p][t] += delta
                    ok, _ = verify_dict(d)
                    n_pert += 1
                    if ok:
                        bad += 1
                        failures.append((f"perturb {name}[{p}][{t}]+={delta}", False, True, {}))
    print(f"  [{'ok' if bad == 0 else 'FAIL'}] {n_pert} single-entry perturbations, {bad} wrongly accepted")

    print("== rejects: random decompositions ==")
    rng = random.Random(20261120)
    n_rand = 0
    bad = 0
    for (a, b, c, r) in [(2, 2, 2, 7), (2, 2, 2, 8), (3, 3, 3, 23), (2, 2, 3, 11), (2, 2, 2, 6)]:
        for trial in range(6):
            d = {"a": a, "b": b, "c": c, "field": "Q",
                 "U": [[rng.choice((-1, 0, 1)) for _ in range(r)] for _ in range(a * b)],
                 "V": [[rng.choice((-1, 0, 1)) for _ in range(r)] for _ in range(b * c)],
                 "W": [[rng.choice((-1, 0, 1)) for _ in range(r)] for _ in range(a * c)]}
            ok, _ = verify_dict(d)
            n_rand += 1
            if ok:
                bad += 1
                failures.append((f"random <{a},{b},{c}> r={r} trial {trial}", False, True, {}))
    print(f"  [{'ok' if bad == 0 else 'FAIL'}] {n_rand} random decompositions, {bad} wrongly accepted")

    print("== rejects: structural problems ==")
    d = _copy(strassen()); d["U"] = d["U"][:3]
    expect("Strassen with a U row deleted", d, False)
    d = _copy(strassen()); d["a"] = 3
    expect("Strassen mislabelled as <3,2,2>", d, False)
    d = _copy(naive(2, 2, 2)); d["U"][0][0] = 0.5
    expect("float entry (forbidden)", d, False)
    d = _copy(strassen())
    d["U"], d["V"] = d["V"], d["U"]  # swapping A/B factors breaks noncommutative identity in general position? (symmetric format - may still pass; informational only)
    ok_swap, info_swap = verify_dict(d)
    print(f"  [info] Strassen with U/V swapped: verified={ok_swap} (format is symmetric under A<->B with transpose; not a required reject)")

    print()
    if failures:
        print(f"SELFTEST FAILED: {len(failures)} failure(s)")
        for f in failures[:10]:
            print("  ", f)
        return 1
    print("SELFTEST PASSED: all accepts accepted, all required rejects rejected.")
    return 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "selftest":
        return selftest()
    if len(argv) >= 3 and argv[1] in ("check", "mismatch"):
        ok, info = verify_file(argv[2])
        if argv[1] == "check":
            print(("VERIFIED " if ok else "REJECTED ") + json.dumps(info))
            return 0 if ok else 1
        print(json.dumps(info))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
