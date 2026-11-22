# Wave 6 — FLIP-GRAPH agent report

**Mission:** implement a Perminov-style flip-graph random walk at rank 23
over {0,±1} from Laderman λ=1 and Perminov cn122, running the exact
rank-1 pair-collapse test at every visited state — one collapsible pair
anywhere = rank 22. Judge: `verify.py` CLI only, fresh processes.

**Headline: no rank-22 decomposition was found. Nothing is claimed.**
The yield is two exact structural results and one large bounded negative:

1. **Laderman is an isolated vertex of the two-term flip graph** — zero
   classic flips, zero near pairs, and zero general two-term rewrites
   across all 253 pairs (complete enumeration, see move set). Its "walk"
   has exactly one state: itself.
2. **Perminov walk: 100,459 steps, 34,604 distinct exact rank-23 states,
   25,416,380 pair tests — no collapsible pair anywhere.** The walk never
   dead-ended (0 restarts, classic flips always available, mean 19.4
   moves/state) and never needed the rewrite escape (0 rewrite steps).
3. **Closest approach to a collapse in the entire campaign:** the
   Perminov seed's own pair (13, 18), sharing its W factor, whose joint
   matrix S has exactly **1 nonzero 2×2 minor** — one minor away from
   rank 1. In 100k steps the walk never matched or beat that; the seed
   itself is the proximity champion (best-proximity state hash = seed
   hash).

---

## Move set (exactly what was implemented)

**Classic flips.** Two terms sharing a factor in one slot (up to sign)
have joint contribution f ⊗ S, S a 9×9 integer matrix of rank ≤ 2 in the
other two slots. A flip replaces them by any other pair of {0,±1}
rank-1 terms with the same joint contribution, i.e. any {0,±1}
decomposition S = x yᵀ + x′ y′ᵀ. Enumeration is exact and complete for
this move type: x, x′ must lie in col(S), y, y′ in row(S); the {0,±1}
vectors of a 2D rational subspace are enumerated via pivot pairs, and
for each candidate (x, x′) the partners (y, y′) are uniquely determined
by a 2×2 Fraction solve, then verified entrywise against S.

**General two-term rewrites (the brief's fallback).** For a pair with no
shared factor: any 2-term {0,±1} decomposition of the pair's joint
contribution P has its (V,W)-matrices in the pencil span{M₁, M₂} (row
space of the mode-0 flattening) and its U-factors in span{u₁, u₂}. So:
enumerate the rank-1 {0,±1} matrices in the pencil (span enumeration +
membership filtered mod 101, confirmed exactly over Q), then for each
independent pair of pencil members solve the 2×2 lift and keep it only
if both lifted U-factors are in {0,±1}. This is complete for two-term
rewrites of the pair. Every candidate rewrite is additionally checked
entrywise against P before acceptance.

**Pair-collapse test.** A pair's joint contribution has rank 1 over Q
iff the two terms' factors are proportional in ≥ 2 of the 3 slots
(flattening argument; for {0,±1} vectors proportional ⟺ equal up to
sign). This O(253·3·9) test ran at **every** visited state. It was
cross-validated against the literal test — all 2×2 minors of all three
flattenings vanish, computed as rank mod 101 (rigorous here: flattening
entries lie in {−2..2}, so every 2×2 minor has |value| ≤ 8 < 101 and
vanishes over Q iff it vanishes mod 101) — on both seeds (full 253
pairs, agreement, both empty, consistent with Wave 5's 759-pair result)
and on 66 sampled visited states during the walk (agreement every time).

**Proximity measure.** For pairs with exactly one proportional slot
("near pairs"), the contribution is f ⊗ S and collapse ⟺ S has rank 1;
proximity = number of nonzero 2×2 minors of S (0 would be a collapse).

## Validation evidence (all before the walks)

- Both seeds: internal exact integer check OK; CLI `VERIFIED` 0/729 in
  fresh processes.
- Fast vs literal pair test on both seeds: identical, zero collapsible
  pairs. Checker non-vacuity: a single perturbed entry makes the
  internal exact check fail.
- Flip round-trip: apply a flip at Perminov, its inverse is enumerated,
  applying it returns the seed state (hash-canonical under term order
  and per-term sign redistribution).
- 300-flip stability walk from Perminov: exactness asserted after every
  flip, pair test every step, no collapsible pair.
- Every rewrite returned by the general enumerator at the Perminov seed
  was applied and exactness-checked (there were none — see below).

## Results per seed

### Laderman λ=1 — ISOLATED (exact, complete at this point)

- Classic flips at seed: **0**. Near pairs (exactly one shared slot
  factor): **0** — no two Laderman terms share a factor in *any* slot.
- General two-term rewrites: **0 across all 253 pairs** (complete
  pencil enumeration per pair). So no two terms of Laderman can be
  rewritten as any other two {0,±1} terms at all: the point is a
  one-vertex component of the two-term flip graph. The Wave 4/5
  wrong=1 rigidity now has a graph-theoretic face: there is nowhere
  for a two-term move to go.
- Walk record: 1 state visited (itself), 253 pair tests, final state
  CLI `VERIFIED` (it is the seed). (`stats_laderman.json`.)

### Perminov cn122 — large bounded negative

- Seed mobility: 26 classic flips from 7 near pairs (shared-slot pairs
  per slot available); general rewrites on no-shared-factor pairs: **0**
  at the seed — all mobility is classic flips.
- Walk (rng 777, anti-backtracking, restarts only on dead-end):
  **100,459 steps in 750 s of walk time** (stopped by the agent at the
  750 s checkpoint to fit the wave budget; checkpointed stats are the
  record, `stats_perminov.json`), **34,604 distinct states**,
  **25,416,380 pair tests**, **0 collapsible pairs**, 0 restarts,
  0 rewrite steps (escape never triggered).
- Near pairs per state: mean 5.63, range 4–8 (seed: 7). Available flips
  per state: mean 19.4.
- Best proximity: **1 nonzero minor**, attained at the seed itself by
  pair (13, 18) sharing slot W (`bestprox_perminov.json` is the seed
  state). No visited state ever produced a near pair with 0 minors
  (that would be a collapse) or matched 1 with a different pair.
- Saturation: distinct-state growth flattened late in the walk (steps
  80k→96k added only ~1.7k new states), suggesting the walk was
  re-covering a component of order tens of thousands of states around
  Perminov — within that whole component, no pair ever collapses.
- Independent checks during the walk: **133 sampled states CLI-verified**
  (`VERIFIED`, fresh processes, every 750 steps) and **66 literal
  pair-test cross-checks** (every 1500 steps), all passing; the final
  checkpointed state was CLI-verified by hand after the stop:
  `VERIFIED` 0/729 (`final_cli_check.txt`).

### Drop states

25 drop states were logged and CLI-scored (the log cap), all from
states ≤ 6 steps from the Perminov seed and all dropping one of the
seed's own small-support terms (indices 6, 13, 18 → wrong = 1; 17, 19 →
wrong = 2). Honest assessment: **no wrong=1 drop with genuinely new
structure was found** — the logged drops are Perminov's known unit
terms persisting in nearby states, and the cap filled before any
deep-walk drop could be logged. These files (`drops/`) are near-miss
records only, duplicates in spirit of Wave 5's banked Perminov drops.

## Bottom line

- **Verified new decompositions: none. Rank 22 over Q was not found.**
  No file was written to `results/` by this agent.
- **Sound exact results:** (i) Laderman admits no two-term {0,±1}
  rewrite of any pair — it is isolated in the flip graph, so the
  Perminov method cannot even start there; (ii) at both seeds, no
  general two-term rewrite exists outside the classic shared-factor
  flips (Perminov) or at all (Laderman).
- **Bounded negative:** across 34,604 distinct rank-23 states in
  Perminov's flip component (100,459 visited states, 25.4M exact pair
  tests), no pair's joint contribution has rank 1 — pair collapse does
  not occur in this component, at least not in the explored region.
  The closest any pair comes is the seed's own (13, 18) at a single
  nonzero 2×2 minor.
- **Implication for the campaign:** if a collapsible rank-23 point
  exists, it is not within ~10⁵ two-term flips of Perminov, and
  Laderman's component is a dead end by construction. Remaining routes
  are the ones already queued: three-term rewrites (the flip graph's
  next move class — nothing here tests them), the undecided z3 free-4
  instances (W6-DeepExact), or a rank-23 scheme from a different
  construction altogether.

Artefacts: `flipgraph.py` (all code), `stats_laderman.json`,
`stats_perminov.json`, `bestprox_perminov.json` (= the seed state),
`current_perminov.json` (last checkpointed walk state, CLI-verified),
`sample_perminov.json`, `drops/` (25 CLI-scored near-miss drop states),
`final_cli_check.txt`, `walk_perminov.log`.
