# The T11 point — Perminov's cr58_cn122, measured

**Date:** 2026-11-22. **Object:** one named third-party scheme.

## Provenance (mandatory)

The scheme is **Perminov's cr58_cn122**, a rank-23 scheme for
⟨3,3,3⟩ from his public database (arXiv:2512.21980), reprinted
by Karunaratne–Idamekorala (arXiv:2607.28676) and by the
boulder-swarm project (github.com/ForeverMJ/boulder-swarm),
where the campaign found it in Wave 24 and nicknamed it "T11".
**It is not a campaign discovery.** The campaign's contribution
is the set of measurements below. The scheme file is
`certificates/perminov_cr58_cn122_r23_Q.json` (VERIFIED 0/729
over ℚ by `code/verify.py`, fresh process; also verified over
F₂).

## The claim, at its approved wording

Perminov's cr58_cn122 is not equivalent to Laderman's scheme or
to Perminov's cn122: the per-slot factor-rank multisets —
invariants of the isotropy action — differ from both, under any
permutation of the slots. (Fresh profiles: Laderman {1:17, 2:4,
3:2} in every slot; cn122 U{1:19,2:4} V{1:14,2:9} W{1:16,2:7};
cr58_cn122 U{1:14,2:9} V{1:19,2:4} W{1:18,2:5}.) At this point
the Brent Jacobian over ℚ has kernel dimension **94**, exceeding
the trivial rescaling and isotropy tangents (**70**) by **24**
dimensions — the same excess as at cn122, in a different orbit.
No pair of its 23 terms merges over ℚ (**0 of 253** pairs have
a rank-1 sum), so it yields no rank-22 scheme by dropping two
terms and completing with one.

Notes on scope, per the claim gate:

- The excess is a kernel-minus-trivial-tangents count (Zariski
  tangent statement), not a claim about the local dimension of
  any moduli space.
- Bounded flip walks from this point and from cn122 visited
  disjoint state sets, but flip-component identity is formally
  undecided; the *proven* separation is the isotropy orbit,
  above.
- Perminov's own classification already assigns cr58_cn122 and
  cn122 different class labels, so their distinctness is
  implicit in the source; the invariant proof and the kernel
  and pair-merge numbers are the campaign's measurements, not
  found stated in the sources searched.

## Second path

Wave 28 re-pinned the kernel dimension with a from-scratch
Jacobian (`code/check_kernels_independent.py`): rank 527 at
each of the fresh primes 104729, 1299709, 15485863 gives
nullity ≤ 94; the stored 94-vector exact kernel basis was
annihilated exactly (J·v = 0, 0 failures) and has rank 94,
giving nullity ≥ 94. The trivial span 70 was independently
reproduced by the gate's own torus + orbit tangent
construction. The pair-merge exclusion was re-run fresh
(flattening-rank criterion over ℚ): 0 of 253.

## The four wrong=1 seeds

Dropping T11's four unit terms gives the basin's four rank-22
wrong=1 states (banked in the campaign record as
`boulder_T11_minus3.json`, `boulder_T11_minus14.json`,
`boulder_T11_minus15.json`, `boulder_T11_minus21.json`, with
wrong entries at (7,4,7), (3,1,4), (6,1,7) and (4,4,4)
respectively). They are states, not schemes, and are not shipped
as certificates. As of 2026-11-22 a validated solver kernel
carrying the free-4 {0,±1} repair instances on these four seeds
(16 exhaustive cases each) is staged in the campaign but has
not run; no repair verdict on this basin exists yet.
