# Wave 7 — TRIPLES agent report

**Mission:** find a triple of terms in a rank-23 ⟨3,3,3⟩ scheme over Q whose
joint contribution tensor has rank ≤ 2 — replacing it by 2 terms gives
rank 22. Judge: `verify.py` CLI only, fresh processes.

**Headline: no rank-22 decomposition was found. Nothing is claimed.**
The filter passed **zero** triples everywhere it was run — and it was run
on **all 1771 triples of ~75,000 distinct exact rank-23 states** (≈133
million triple tests counting the two walks' overlap). No completion was
ever triggered on a real candidate, because none existed. This is a large
bounded negative: within Perminov's flip component and every banked
rank-23 scheme, **no three terms' joint contribution has all flattening
ranks ≤ 2**, hence none has tensor rank ≤ 2.

---

## The filter (exact, and stronger than the brief required)

For a triple with factors (u_t, v_t, w_t), the mode-0 flattening is
A·Bᵀ with A = [u₁ u₂ u₃] (9×3) and B = [v₁⊗w₁, v₂⊗w₂, v₃⊗w₃] (81×3).
rank(ABᵀ) ≤ 2 iff rank A ≤ 2 or rank B ≤ 2 (if both are 3, Bᵀ is
surjective and A injective, so rank(ABᵀ) = 3). Three vectors have rank
≤ 2 iff their Gram determinant is 0, and the Kronecker Gram factorises:
Gram(v⊗w) = Gram(v) ∘ Gram(w) (Hadamard). So with G_u, G_v, G_w the 3×3
Gram matrices of the triple's factors, all six determinants are small
exact integers:

- mode-0 flattening ≤ 2 ⟺ det G_u = 0 or det(G_v∘G_w) = 0
- mode-1 flattening ≤ 2 ⟺ det G_v = 0 or det(G_u∘G_w) = 0
- mode-2 flattening ≤ 2 ⟺ det G_w = 0 or det(G_u∘G_v) = 0

This made the filter ~free (vectorised numpy int64, no rounding), so
instead of sampling triples at sampled states, **every triple was tested
at every distinct state visited**. The Gram filter was validated against
literal Fraction flattening ranks on 300 random Perminov triples:
300/300 agreement.

## Validation (before any searching)

- Seeds internally exact; Perminov CLI `VERIFIED` fresh process.
- **Synthetic planted triple:** Perminov term 0 split into two terms
  (W factor split across two terms) → 24-term exact scheme; the triple
  {split-1, split-2, term 1} has contribution rank ≤ 2 by construction.
  Filter: **passed** (literal flattening ranks [2,2,2]).
  Completion pipeline: the pencil/Jennrich solver decomposed it exactly
  over Q, the assembled file was CLI-`VERIFIED` (rank 23 from the
  24-term parent — machinery proof only, moved out of `results/` to
  `synthetic_assembled_r23.json`). The full detect → complete →
  assemble → CLI path works end-to-end.
- Completion machinery (for candidates, none occurred): pencil/Jennrich
  exact decomposition over Q (rank-1 members of the slice pencil via
  rational roots of 2×2-minor quadratics, with the conjugate-pair
  obstruction detected), then z3 over {0,±1} (120 s), then z3 halves
  (scaled ×8, factors in {0,±1,±2}, 120 s).

## Coverage and results

| sweep | states | triples tested | filter passes |
|---|---|---|---|
| Perminov seed (all triples) | 1 | 1,771 | **0** |
| Laderman λ=1 seed (all triples) | 1 | 1,771 | **0** |
| W6 final walk state (all triples) | 1 | 1,771 | **0** |
| λ-family λ∈{−1,2,1/2,−2,3} + 30 GL copies of Laderman | 35 | 61,985 | **0** |
| Walk 1: Perminov seed, rng 31337, ~600 s | 37,799 distinct | 66,942,029 | **0** |
| Walk 2: W6 final state, rng 777777, 420 s | 37,184 distinct | 65,852,864 | **0** |

- Walk mechanics: Wave 6's exact flip enumeration reused verbatim;
  exactness asserted after every move; only first-visit states swept.
  Walk 1 was stopped at ~600 s on clear saturation (distinct-state
  growth: +26,740 states in the first 270 s, +571 in the next 300 s);
  its last checkpointed state was CLI-`VERIFIED` by hand afterwards.
  Walk 2 ran its full 420 s; final state CLI-`VERIFIED`. The two walks'
  nfail histograms are nearly identical (nfail=1 counts 128,097 vs
  126,124), i.e. both covered essentially the same ~38k-state component
  Perminov's flips reach — consistent with Wave 6's saturation estimate.
- The banked wrong=1 drop states' parent schemes are Perminov and
  Laderman themselves, so triples involving the unit terms in those
  parents are covered by the seed sweeps above (Perminov unit terms
  {6,13,18}, Laderman {2,19,20,21,22}).

## Proximity (how close triples come)

Proximity = number of flattening modes with rank 3 (nfail; 0 = pass),
tie-broken by the number of nonzero Gram determinants (ndet, 0–6).

- **Best anywhere: nfail = 1, ndet = 4** (both walks; e.g. state
  `569d452f305016a7` in walk 1). Triples failing exactly one mode are
  not rare (126–128k per walk) but none ever failed zero.
- At the Perminov seed only 4 triples have nfail = 1, all tiny-support:
  (2,13,18) support 7, failing mode 0 only, dets (1,0,0,5,5,1) — note
  det G_u = 1, a single unit away from passing that mode; (5,8,14)
  support 8, mode 0; (6,11,15) support 13, mode 2; (6,11,20)
  support 17, mode 0. A failed mode means that flattening has rank
  exactly 3, so these triples' contributions provably have rank ≥ 3 —
  they are near in determinant space only, not collapsible.
- Laderman is farther: best nfail = 2 (48 triples), min ndet = 5.
- All 35 λ/GL variants share best (nfail 2, ndet 5) at triple (0,3,6):
  independently confirmed not a bug — the isotropy action applies one
  fixed invertible map per slot, so per-slot linear dependence is
  orbit-invariant; Laderman's terms 0,3,6 have dependent W factors
  (literal flattening ranks [3,3,2] in the dense copies), and that is
  the only vanishing determinant in those triples.

## Bottom line

- **Verified new decompositions: none. Rank 22 over Q was not found.**
  No file was written to `results/` by this agent (the one CLI-verified
  file produced during validation was the synthetic machinery proof and
  was moved into this directory).
- **Sound bounded negative:** across ~75k distinct exact rank-23 states
  of Perminov's flip component (two independent walks), all 38 banked
  rank-23 schemes (Laderman family, Perminov, 30 GL copies, W6 end
  state), and ≈133M exact triple tests, **no triple has all flattening
  ranks ≤ 2** — so no three-term collapse to 2 terms exists anywhere in
  that space. Combined with Wave 6 (no pair collapse in the same
  component), Perminov's component is closed under both two-term and
  three-term rewrites of this form.
- **Where rank-2 triples could still hide:** only outside the sampled
  space — rank-23 points not reachable by {0,±1} flips from Perminov
  (Laderman's component is a single vertex and was fully tested at the
  seed: 0 passes), schemes with fraction coefficients not in the
  Laderman λ-orbit, or genuinely different constructions. A rank-22
  decomposition, if it exists, does not arise from collapsing a triple
  inside any rank-23 point this campaign has reached.

Artefacts: `triples.py` (filter, pencil/z3 completion, walks),
`seeds_summary.json`, `extras_summary.json` (35 schemes),
`stats_walk_perminov_31337.json`, `stats_walk_w6current_777777.json`,
`current_walk_perminov_31337.json` (CLI-verified), `walk1.log`,
`walk2.log`, `synthetic_assembled_r23.json` (validation only).
`candidates.jsonl` was never created — there were no candidates.
