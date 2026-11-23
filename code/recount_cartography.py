# Independent second-path checker (Wave 28 claim gate).
# recount_cartography.py — a from-scratch recount of the wrong-entry
# cartography census (data/cartography.md): recomputes every banked
# wrong=1 state's tensor difference from the raw scheme JSONs, rebuilds
# the entry-symmetry group, and re-derives the orbit census and the
# unit-term census without sharing code with the original pipeline.
# It references the campaign's internal file layout; the packaged
# entry point for the headline kernel numbers is check_kernels.py.

#!/usr/bin/env python3
"""Wave 28 GATE — independent recount for claim C1 (wrong-entry cartography).

Fresh code written for the gate. Does NOT import verify.py or any wave26
code. Recomputes, from the raw JSON artefacts:
  * for every banked rank-22 state file in the registered population,
    the exact tensor difference S - T over Q and its wrong entries;
  * the census numbers (files, wrong=1 files, unique states);
  * the symmetry group G = <Phi, A<->B duality> on the 729 positions,
    its orbits, and where the wrong entries land;
  * a direct census of unit terms in the parent rank-23 schemes.
"""
import json, hashlib, itertools, sys
from fractions import Fraction
from pathlib import Path

ROOT = Path.home() / "workspace" / "matmul-pilot"

def F(x):
    return Fraction(str(x))

def load(path):
    d = json.loads(Path(path).read_text())
    U = [[F(x) for x in row] for row in d["U"]]
    V = [[F(x) for x in row] for row in d["V"]]
    W = [[F(x) for x in row] for row in d["W"]]
    return U, V, W

def target():
    T = {}
    for i in range(3):
        for j in range(3):
            for k in range(3):
                T[(3*i+j, 3*j+k, 3*i+k)] = Fraction(1)
    return T

def diff_entries(U, V, W):
    """Return dict {(p,q,s): value} of S - T restricted to nonzeros."""
    r = len(U[0])
    T = target()
    out = {}
    for p in range(9):
        for q in range(9):
            for s in range(9):
                acc = Fraction(0)
                for t in range(r):
                    a = U[p][t]
                    if a:
                        b = V[q][t]
                        if b:
                            c = W[s][t]
                            if c:
                                acc += a*b*c
                want = T.get((p, q, s), Fraction(0))
                if acc != want:
                    out[(p, q, s)] = (acc, want)
    return out

# ---------- population (Wave 26 registered census) ----------
pop = []
for d in ["wave5/schemes/drops", "wave24/fringe-tests/drops", "wave6/flipgraph/drops"]:
    pop += sorted((ROOT / d).glob("*.json"))
pop.append(ROOT / "wave4/laderman/anneal_best_r22.json")
print(f"population files: {len(pop)}")

wrong1 = []          # (path, wrongpos, have, want)
census = []
for path in pop:
    U, V, W = load(path)
    d = diff_entries(U, V, W)
    census.append((str(path.relative_to(ROOT)), len(d)))
    if len(d) == 1:
        (pos, (have, want)), = d.items()
        raw = Path(path).read_bytes()
        wrong1.append({
            "path": str(path.relative_to(ROOT)),
            "pos": pos, "have": str(have), "want": str(want),
            "sha": hashlib.sha256(raw).hexdigest(),
            # semantic fingerprint: sorted multiset of term tensors is overkill;
            # use the full ordered factor content as canonical bytes of Fractions
            "sem": hashlib.sha256(
                json.dumps([[str(x) for x in row] for M in (U, V, W) for row in M]).encode()
            ).hexdigest(),
        })

print(f"files with exactly 1 wrong entry: {len(wrong1)}")
by_sha = {}
for w in wrong1:
    by_sha.setdefault(w["sha"], []).append(w["path"])
print(f"unique by file bytes: {len(by_sha)}")
by_sem = {}
for w in wrong1:
    by_sem.setdefault(w["sem"], []).append(w["path"])
print(f"unique by factor content: {len(by_sem)}")
dupes = {k: v for k, v in by_sha.items() if len(v) > 1}
print(f"byte-identical duplicate groups: {len(dupes)} -> {list(dupes.values())}")

uniq = list({w["sha"]: w for w in wrong1}.values())
positions = [w["pos"] for w in uniq]
T = target()
onsupport = sum(1 for p in positions if p in T)
print(f"unique wrong=1 states: {len(uniq)}")
print(f"wrong entries on the 27-position support of T: {onsupport}/{len(positions)}")
print(f"all have=0/want=1: {all(w['have']=='0' and w['want']=='1' for w in uniq)}")
distinct_pos = sorted(set(positions))
print(f"distinct wrong positions: {len(distinct_pos)} -> {distinct_pos}")

# ---------- group G on positions ----------
def tau(x):  # transpose on a 9-index (3x3 row-major)
    return 3*(x % 3) + x//3

def phi(pos):
    p, q, s = pos
    return (tau(s), p, tau(q))

def swap(pos):
    p, q, s = pos
    return (tau(q), tau(p), tau(s))

# verify generators fix T (as position permutations preserving T's values)
allpos = [(p, q, s) for p in range(9) for q in range(9) for s in range(9)]
for g, name in [(phi, "phi"), (swap, "swap")]:
    ok = all((g(pos) in T) == (pos in T) for pos in allpos)
    print(f"generator {name} fixes T support: {ok}")

def compose(f, g):
    return lambda pos: f(g(pos))

# group closure (as tuples of images over a fixed ordering of positions)
def key(f):
    return tuple(f(pos) for pos in allpos)
G = {key(lambda pos: pos): (lambda pos: pos)}
frontier = [phi, swap]
funcs = {(lambda pos: pos): None}
# BFS on functions via key set
seen = {key(lambda pos: pos)}
elems = [lambda pos: pos]
queue = [lambda pos: pos]
while queue:
    f = queue.pop()
    for g in (phi, swap):
        for h in (compose(f, g), compose(g, f)):
            k = key(h)
            if k not in seen:
                seen.add(k); elems.append(h); queue.append(h)
print(f"|G| = {len(elems)}")

# orbits
remaining = set(allpos)
orbits = []
while remaining:
    p0 = next(iter(remaining))
    orb = {f(p0) for f in elems}
    orbits.append(orb)
    remaining -= orb
print(f"number of G-orbits on 729 positions: {len(orbits)}")

hit = [orb for orb in orbits if orb & set(distinct_pos)]
print(f"orbits containing a wrong position: {len(hit)}")
print(f"total positions in hit orbits: {sum(len(o) for o in hit)}")
for o in sorted(hit, key=lambda o: (len(o), sorted(o))):
    inside = sorted(set(o) & set(distinct_pos))
    print(f"  orbit size {len(o)}: wrong positions {inside}")

# ---------- direct unit-term census on parent schemes ----------
print("\n--- unit terms in parent rank-23 schemes (direct census) ---")
parents = [
    "results/wave4_333_r23_Q_laderman.json",
    "results/wave5_333_r23_Q_laderman-lam-neg1.json",
    "results/wave5_333_r23_Q_laderman-lam2.json",
    "results/wave5_333_r23_Q_laderman-lam-half.json",
    "results/wave5_333_r23_Q_laderman-lam-neg2.json",
    "results/wave5_333_r23_Q_laderman-lam3.json",
    "results/wave5_333_r23_Q_perminov-cn122.json",
    "wave25/t11/wave25_333_r23_Q_T11.json",
    "wave24/fringe-tests/schemes/boulder_T12_Q.json",
    "wave24/fringe-tests/schemes/boulder_famA_Q.json",
    "wave24/fringe-tests/schemes/boulder_famB_Q.json",
]
import os
for rel in parents:
    path = ROOT / rel
    if not path.exists():
        print(f"  MISSING: {rel}")
        continue
    U, V, W = load(path)
    r = len(U[0])
    units = []
    for t in range(r):
        cols = []
        ok = True
        for M in (U, V, W):
            nz = [(i, M[i][t]) for i in range(9) if M[i][t] != 0]
            if len(nz) != 1:
                ok = False; break
            cols.append(nz[0])
        if ok:
            pos = (cols[0][0], cols[1][0], cols[2][0])
            units.append((t, pos, pos in T))
    off = [u for u in units if not u[2]]
    print(f"  {rel}: {len(units)} unit terms, on-support {len(units)-len(off)}, OFF-support {len(off)} {off if off else ''}")

json_out = {
    "population": len(pop),
    "wrong1_files": len(wrong1),
    "unique_by_bytes": len(by_sha),
    "unique_by_content": len(by_sem),
    "on_support": onsupport,
    "distinct_positions": [list(p) for p in distinct_pos],
    "group_order": len(elems),
    "orbits_total": len(orbits),
    "hit_orbits": len(hit),
    "hit_orbit_positions": sum(len(o) for o in hit),
    "census": census,
}
(ROOT / "wave28/gate/recount_c1_results.json").write_text(json.dumps(json_out, indent=1))
print("\nwrote wave28/gate/recount_c1_results.json")
