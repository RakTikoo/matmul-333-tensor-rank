# Independent second-path checker (Wave 32 claim gate).
# clusters_greedy.py — a from-scratch re-implementation of the
# registered greedy cluster procedure (data/cluster-anatomy.md),
# written from the specification alone: reproduces the baselines,
# greedy totals, greedy histories, final partitions and
# support-tiling counts for Laderman, Perminov cn122 and Perminov
# cr58_cn122. It references the campaign's internal file layout;
# the packaged entry point for the headline kernel numbers is
# check_kernels.py.

#!/usr/bin/env python3
"""
clusters_g2.py — Wave 32 GATE, second path for claim G2 (Wave 30 Item B).
Provenance: Wave 32 gate agent, 2026-11-23. Judge status: exact Fraction
arithmetic here; the three schemes are also judged fresh by verify.py
CLI before measurement (run separately, logged in GATE.md).

Re-implemented from the SPECIFICATION in wave30/wild/OUTCOMES.md only.
wave30/wild/itemB_clusters.py was NOT read. The specification used:

  - Term tensor: the exact 729-vector u(x)v(x)w over Q.
    supp(T): the 27 naive positions.
  - garbage(C) = #{positions not in supp(T) : (sum of term tensors
    in C) is nonzero there}.
  - Core = the scheme's unit terms. Cluster material = non-unit terms.
  - Greedy agglomerative partitioning of the non-unit terms: start
    from singletons; repeatedly merge the pair of clusters whose
    union has size <= 3 and whose merge most reduces total garbage
    sum_C garbage(C); tie-break by smaller resulting total
    cluster-support size, then lexicographic term indices. Stop
    when no admissible merge reduces total garbage.
  - Also: all-singletons baseline; Laderman file-order partition
    (consecutive triples of the non-unit terms, in file order).

SPECIFICATION AMBIGUITY NOTES (gate findings, also in GATE.md):
  (a) "total cluster-support size" is not defined in the spec. Read
      here as: sum over all clusters, after the candidate merge, of
      the number of nonzero positions of the cluster sum (on- and
      off-support together).
  (b) "lexicographic term indices" does not say indices of what.
      Read here as: the sorted tuple of term indices of the merged
      union, then the pair of cluster tuples. Term indices are
      indices into the non-unit term list in file order.
  (c) The spec does not fix an enumeration order for candidate
      pairs; with the tie-break chain above the choice is
      deterministic in this implementation, but a different
      reasonable reading of (a)/(b) could in principle select a
      different merge at a tied step. The gate therefore checks
      whether the TOTALS and OVERLAP COUNTS reproduce; the exact
      partition is also compared and reported.

Sparse representation: each term tensor is a dict
{flat_position: Fraction} of its nonzero entries.
"""
import json
from fractions import Fraction

ROOT = "/home/hatch/workspace/matmul-pilot"
SCHEMES = [
    ("Laderman lam=1", "results/wave4_333_r23_Q_laderman.json"),
    ("Perminov cn122", "results/wave5_333_r23_Q_perminov-cn122.json"),
    ("T11 (cr58_cn122)", "wave25/t11/wave25_333_r23_Q_T11.json"),
]


def parse(x):
    return Fraction(x) if isinstance(x, str) else Fraction(x)


def target_positions():
    supp = set()
    for i in range(3):
        for j in range(3):
            for k in range(3):
                supp.add(((i * 3 + j) * 81) + ((j * 3 + k) * 9)
                         + (i * 3 + k))
    return supp


SUPP = target_positions()
assert len(SUPP) == 27


def term_dicts(path):
    d = json.load(open(path))
    U = [[parse(x) for x in row] for row in d["U"]]
    V = [[parse(x) for x in row] for row in d["V"]]
    W = [[parse(x) for x in row] for row in d["W"]]
    r = len(U[0])
    terms = []
    is_unit = []
    for t in range(r):
        td = {}
        for p in range(9):
            if U[p][t] == 0:
                continue
            for q in range(9):
                if V[q][t] == 0:
                    continue
                for s in range(9):
                    v = U[p][t] * V[q][t] * W[s][t]
                    if v != 0:
                        td[p * 81 + q * 9 + s] = v
        terms.append(td)
        is_unit.append(all(
            sum(1 for row in range(9) if M[row][t] != 0) == 1
            for M in (U, V, W)))
    return terms, is_unit


def cluster_sum(members, terms):
    acc = {}
    for t in members:
        for pos, v in terms[t].items():
            acc[pos] = acc.get(pos, Fraction(0)) + v
    return {pos: v for pos, v in acc.items() if v != 0}


def garbage(csum):
    return sum(1 for pos in csum if pos not in SUPP)


def greedy(nonunit_terms):
    """nonunit_terms: list of term dicts, indexed 0..n-1 locally."""
    clusters = [(i,) for i in range(len(nonunit_terms))]
    sums = {c: nonunit_terms[c[0]] for c in clusters}

    def total_garbage(cls):
        return sum(garbage(sums[c]) for c in cls)

    history = [total_garbage(clusters)]
    while True:
        cur = history[-1]
        best = None  # (new_total_garbage, new_total_support, union, i, j)
        for a in range(len(clusters)):
            for b in range(a + 1, len(clusters)):
                union = tuple(sorted(clusters[a] + clusters[b]))
                if len(union) > 3:
                    continue
                usum = cluster_sum(union, nonunit_terms)
                new_total = (cur - garbage(sums[clusters[a]])
                             - garbage(sums[clusters[b]])
                             + garbage(usum))
                if new_total >= cur:
                    continue
                rest_support = sum(len(sums[c]) for idx, c
                                   in enumerate(clusters)
                                   if idx not in (a, b))
                key = (new_total, rest_support + len(usum), union,
                       clusters[a], clusters[b])
                if best is None or key < best[0]:
                    best = (key, a, b, union, usum)
        if best is None:
            break
        _, a, b, union, usum = best
        clusters = [c for idx, c in enumerate(clusters)
                    if idx not in (a, b)] + [union]
        sums = {c: (usum if c == union else sums[c]) for c in clusters}
        history.append(total_garbage(clusters))
    out = []
    for c in sorted(clusters):
        cs = sums[c]
        out.append({"terms": list(c), "size": len(c),
                    "garbage": garbage(cs), "support": len(cs)})
    return out, history


def main():
    results = []
    for name, rel in SCHEMES:
        terms, is_unit = term_dicts(ROOT + "/" + rel)
        core_idx = [t for t in range(len(terms)) if is_unit[t]]
        nonunit_idx = [t for t in range(len(terms)) if not is_unit[t]]
        nonunit_terms = [terms[t] for t in nonunit_idx]
        baseline = sum(garbage(td) for td in nonunit_terms)
        clusters, history = greedy(nonunit_terms)
        total = sum(c["garbage"] for c in clusters)

        entry = {"scheme": name, "rank": len(terms),
                 "core_unit_terms": len(core_idx),
                 "nonunit_terms": len(nonunit_idx),
                 "baseline_singletons_garbage": baseline,
                 "greedy_total_garbage": total,
                 "greedy_history": history,
                 "clusters": clusters}

        if name.startswith("Laderman"):
            fo = []
            for a in range(0, len(nonunit_terms), 3):
                grp = nonunit_terms[a:a + 3]
                acc = {}
                for td in grp:
                    for pos, v in td.items():
                        acc[pos] = acc.get(pos, Fraction(0)) + v
                acc = {p: v for p, v in acc.items() if v != 0}
                fo.append(garbage(acc))
            entry["fileorder_clusters_of_3_garbage"] = fo
            entry["fileorder_total_garbage"] = sum(fo)

        # support tiling: parts = core terms (individually) + clusters
        parts = [terms[t] for t in core_idx]
        for c in clusters:
            parts.append(cluster_sum(c["terms"], nonunit_terms))
        mult = 0
        covered = set()
        for part in parts:
            on = {pos for pos in part if pos in SUPP}
            mult += len(on)
            covered |= on
        entry["tiling"] = {
            "on_support_count_with_multiplicity": mult,
            "distinct_on_support_covered": len(covered),
            "on_support_overlaps": mult - len(covered),
            "covers_all_27": len(covered) == 27}
        results.append(entry)
        print(json.dumps(entry, indent=1))

    json.dump(results,
              open(ROOT + "/wave32/gate/clusters_g2_results.json", "w"),
              indent=1)
    print("wrote wave32/gate/clusters_g2_results.json")


if __name__ == "__main__":
    main()
