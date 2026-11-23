# Independent second-path checker (HKS census harvest, 2026-11-23).
# recount_hks_census.py — the home re-judgement of the
# Heule-Kauers-Seidl population census (data/hks-census.md):
# re-derives every census tally from the locally held copy of
# the distribution archive and verifies all 17,376 schemes
# exactly, without importing the Kaggle kernel's parser (the
# only kernel data read is its bank file list, as data). It
# references the campaign's internal file layout; the packaged
# entry point for the headline kernel numbers is
# check_kernels.py.

#!/usr/bin/env python3
"""
census_home.py — INDEPENDENT home re-judgement of the HKS population census.

Written fresh for this harvest (2026-11-23). It does NOT import or read
the parser inside kaggle/hks_kernel.py. The only data taken from the
kernel file is the BANK_HASHES_JSON literal (the campaign bank's file
list), extracted as data. Canonical term-multiset equality follows the
notion fixed by wave32/gate/recount_g1.py: a term is canonicalised to
its primitive integer 729-vector (denominators cleared, gcd divided
out, sign fixed by first nonzero entry positive); two schemes are the
same iff their sorted tuples of canonical terms agree. For the
{0,+/-1} population the primitive vector is computed sparsely (its
nonzero entries with flat indices p*81+q*9+s) — exactly equal as a
mathematical object to the dense primitive vector.

.tab reading (diagnosed on the classics, this script's own test):
each file is 23 blocks of 3 rows; each row holds three 3x3 groups
(U, V, W-displayed) separated by '|'. U and V 9-vectors are the
row-major flattenings (index 3a+b). The W group is stored transposed
(rows k, cols i): W[s] with s = 3i+k equals D[k][i]. Validation: all
four classics verify 0/729 under this reading and exactly 36/729
under the direct reading.

Target tensor: T[p][q][s] = 1 iff p=(i,j), q=(j2,k), s=(i2,k2) with
j==j2, i==i2, k==k2. A unit term has exactly one nonzero in each
factor column; it is NAIVE iff T at its position is 1.

Every one of the 17,376 schemes is verified EXACTLY here (integer
arithmetic, sparse accumulation over all 729 entries) — full
coverage, superseding the kernel's (a) all-carriers + (b) 300-sample
+ (c) degenerate verification split.
"""
import hashlib
import json
import re
import sys
import tarfile
import time
from fractions import Fraction
from math import gcd

TGZ = ("/home/hatch/workspace/browser_downloads/sess-186047132/"
       "browser-download-20261123T202245.059142541Z-4-schemes.tgz")
ROOT = "/home/hatch/workspace/matmul-pilot"
KERNEL = ROOT + "/kaggle/hks_kernel.py"
OUT = ROOT + "/compute-harvest/kaggle-hks/census_home_results.json"

TARGET = [0] * 729
for _p in range(9):
    _i, _j = divmod(_p, 3)
    for _q in range(9):
        _j2, _k = divmod(_q, 3)
        if _j != _j2:
            continue
        for _s in range(9):
            _i2, _k2 = divmod(_s, 3)
            if _i == _i2 and _k == _k2:
                TARGET[_p * 81 + _q * 9 + _s] = 1


def parse_tab(text):
    """Return list of 23 terms; each term = (U3, V3, D) 3x3 int lists."""
    rows = []
    for line in text.splitlines():
        if "|" in line:
            vals = [int(x) for x in line.replace("|", " ").split()]
            if len(vals) != 9:
                raise ValueError("row with %d values" % len(vals))
            rows.append(vals)
    if len(rows) % 3 != 0:
        raise ValueError("%d data rows" % len(rows))
    terms = []
    for b in range(0, len(rows), 3):
        trip = rows[b:b + 3]
        mats = []
        for g in range(3):
            mats.append([[trip[r][3 * g + c] for c in range(3)]
                         for r in range(3)])
        terms.append(tuple(mats))
    return terms


def sparse_cols(term):
    """(suppU, suppV, suppW): lists of (index, value), W transposed."""
    U3, V3, D = term
    su = [(3 * a + b, U3[a][b]) for a in range(3) for b in range(3)
          if U3[a][b] != 0]
    sv = [(3 * a + b, V3[a][b]) for a in range(3) for b in range(3)
          if V3[a][b] != 0]
    sw = [(3 * a + b, D[b][a]) for a in range(3) for b in range(3)
          if D[b][a] != 0]  # s = 3a+b = 3i+k takes D[k][i] = D[b][a]
    return su, sv, sw


def term_key_and_entries(su, sv, sw):
    """Sparse primitive term key + the RAW (flat, value) entry list.

    The key is sign-normalised (first nonzero entry positive); the
    raw entries keep the term's true signs and are what the exact
    verification accumulates. (First version of this script wrongly
    accumulated the normalised entries — caught because the classics
    then failed verification while the orientation test passed.)"""
    raw = []
    for (p, u) in su:
        for (q, v) in sv:
            uv = u * v
            base = p * 81 + q * 9
            for (s, w) in sw:
                raw.append((base + s, uv * w))
    key_entries = sorted(raw)
    if key_entries and key_entries[0][1] < 0:
        key_entries = [(f, -val) for (f, val) in key_entries]
    return tuple(key_entries), raw


def digest_of(multiset_key):
    return hashlib.sha256(repr(multiset_key).encode()).hexdigest()


def bank_term_key(U, V, W, t, r):
    """Primitive sparse key of term t of a campaign JSON scheme
    (Fraction entries), recount_g1 notion."""
    sup = []
    for M in (U, V, W):
        sup.append([(row, M[row][t]) for row in range(9) if M[row][t] != 0])
    su, sv, sw = sup
    entries = []
    for (p, u) in su:
        for (q, v) in sv:
            for (s, w) in sw:
                entries.append((p * 81 + q * 9 + s, u * v * w))
    if not entries:
        return ()
    L = 1
    for _, x in entries:
        L = L * x.denominator // gcd(L, x.denominator)
    ints = [(f, int(x * L)) for (f, x) in entries]
    g = 0
    for _, val in ints:
        g = gcd(g, abs(val))
    if g > 1:
        ints = [(f, val // g) for (f, val) in ints]
    ints.sort()
    if ints[0][1] < 0:
        ints = [(f, -val) for (f, val) in ints]
    return tuple(ints)


def main():
    t0 = time.time()
    n_files = 0
    parse_failures = []
    rank_hist = {}
    tot_unit = tot_naive = 0
    off_list = []
    carriers = 0
    carriers_ge5 = []
    degenerate = 0
    verify_failures = []
    classic_wrong = {}
    key_members = {}   # digest -> [member names]
    key_full = {}      # digest -> multiset key (for duplicate confirm)

    tf = tarfile.open(TGZ, "r:gz")
    for member in tf:
        if not member.name.endswith(".tab"):
            continue
        n_files += 1
        try:
            text = tf.extractfile(member).read().decode()
            terms = parse_tab(text)
            cols = [sparse_cols(t) for t in terms]
        except Exception as e:  # noqa: BLE001 - tally, don't die
            parse_failures.append((member.name, str(e)[:100]))
            continue
        rank_hist[len(terms)] = rank_hist.get(len(terms), 0) + 1

        acc = [0] * 729
        term_keys = []
        n_unit = 0
        is_degenerate = False
        for (su, sv, sw) in cols:
            if not su or not sv or not sw:
                is_degenerate = True
            key, entries = term_key_and_entries(su, sv, sw)
            term_keys.append(key)
            for (f, val) in entries:
                acc[f] += val
            if len(su) == 1 and len(sv) == 1 and len(sw) == 1:
                n_unit += 1
                p, q, s = su[0][0], sv[0][0], sw[0][0]
                if TARGET[p * 81 + q * 9 + s] == 1:
                    tot_naive += 1
                else:
                    off_list.append((member.name, p, q, s))
        tot_unit += n_unit
        if n_unit >= 1:
            carriers += 1
        if n_unit >= 5:
            carriers_ge5.append((member.name, n_unit))
        if is_degenerate:
            degenerate += 1

        wrong = sum(1 for a, b in zip(acc, TARGET) if a != b)
        if "/classic/" in member.name:
            classic_wrong[member.name] = wrong
        if wrong != 0:
            verify_failures.append((member.name, wrong))

        mk = tuple(sorted(term_keys))
        d = digest_of(mk)
        key_members.setdefault(d, []).append(member.name)
        key_full[d] = mk
        if n_files % 4000 == 0:
            print("... %d files, %.0fs" % (n_files, time.time() - t0),
                  flush=True)

    dup_groups = {d: v for d, v in key_members.items() if len(v) > 1}

    # ---- bank comparison (bank file list read as DATA from kernel) ----
    src = open(KERNEL).read()
    m = re.search(r"BANK_HASHES_JSON = r'''(.*?)'''", src, re.S)
    bank_map = json.loads(m.group(1))
    bank_files = sorted({f for files in bank_map.values() for f in files})
    bank_digests = {}
    bank_missing = []
    for f in bank_files:
        try:
            d = json.load(open(ROOT + "/" + f))
        except Exception as e:  # noqa: BLE001
            bank_missing.append((f, str(e)[:80]))
            continue
        U, V, W = d["U"], d["V"], d["W"]
        r = len(U[0])
        def conv(M):
            return [[Fraction(x) if isinstance(x, str) else Fraction(x)
                     for x in row] for row in M]
        U, V, W = conv(U), conv(V), conv(W)
        mk = tuple(sorted(bank_term_key(U, V, W, t, r) for t in range(r)))
        bank_digests.setdefault(digest_of(mk), []).append(f)
    inter = set(bank_digests) & set(key_members)

    results = {
        "files_tab": n_files,
        "parse_failures": parse_failures,
        "rank_hist": rank_hist,
        "unit_terms_total": tot_unit,
        "unit_naive": tot_naive,
        "unit_off_support": len(off_list),
        "off_list": off_list,
        "carriers_ge1": carriers,
        "carriers_ge5_count": len(carriers_ge5),
        "carriers_ge5": carriers_ge5,
        "degenerate_schemes": degenerate,
        "exact_verify_failures": verify_failures,
        "classic_wrong": classic_wrong,
        "distinct_multisets": len(key_members),
        "duplicate_groups": {d: v for d, v in dup_groups.items()},
        "bank_hashes_in_kernel_data": len(bank_map),
        "bank_files_listed": len(bank_files),
        "bank_files_missing": bank_missing,
        "bank_distinct_multisets_home": len(bank_digests),
        "bank_population_intersection": sorted(inter),
        "elapsed_s": round(time.time() - t0, 1),
    }
    json.dump(results, open(OUT, "w"), indent=1)
    print(json.dumps({k: (v if not isinstance(v, list) or len(str(v)) < 300
                           else str(v)[:300])
                      for k, v in results.items()}, indent=1)[:3000])
    print("wrote", OUT)


if __name__ == "__main__":
    main()
