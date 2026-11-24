# The Hensel bridge: calibration over ℚ via 3-adic lifting, and one native F3 point converted

**Date:** 2026-11-24. A methods calibration. Hensel lifting of
finite-field decompositions to ℤ/ℚ is published prior art —
Khoruzhii–Gelß–Pokutta (ISSAC 2026, arXiv:2511.10786)
discover schemes over F2/F3 and Hensel-lift them to schemes
over ℤ/ℚ, and Moosbauer–Poole's symmetric flip graphs lift F2
solutions to ℤ. This record claims no part of the method; it
calibrates *our* implementation of it and demonstrates, on a
small format, that the implementation converts genuinely new
finite-field points and not only reductions of known schemes.

## The claim, at its approved wording

"We built and calibrated a 3-adic (Hensel) lifting bridge from F3 decompositions to Q, in the spirit of the lifting steps used in recent flip-graph work (Khoruzhii–Gelß–Pokutta, ISSAC 2026): a non-singular F3 point of a decomposition system is Newton-lifted to Z/3⁴² and its coordinates are rationally reconstructed. Calibration: Perminov's cn122 and Laderman's scheme, reduced mod 3, lift and reconstruct **entry-identically**, and both reconstructions verify exactly over Q; the Jacobian ranks mod 3 reproduce the known over-Q nullities (94 and 76). The bridge also converts genuinely new finite-field points, not only reductions of known schemes: a solver-found F3-native rank-7 decomposition of ⟨2,2,2⟩, differing from Strassen's scheme mod 3 in 13 entries, lifts to a verified rank-7 scheme over Q that is not entry-identical to Strassen's. The bridge changes the value of our F3 searches — any future non-singular F3 rank-22 point would lift the same way — but it finds nothing by itself, and non-singularity of a hypothetical F3 point would have to be checked when one exists."

## Calibration record

- **Controls.** Perminov's cn122 and Laderman's scheme,
  reduced mod 3, Newton-lifted to Z/3⁴² and rationally
  reconstructed: both reconstructions are entry-identical to
  the originals and verify exactly over ℚ in fresh processes.
  The Jacobian ranks mod 3 at the reduced points (nullities 94
  and 76) reproduce the over-ℚ values of the headline result —
  the singularity check the bridge depends on is itself
  calibrated.
- **Native conversion.** A rank-7 decomposition of ⟨2,2,2⟩
  over F3 found by the solver natively over F3 (not the
  reduction of Strassen's scheme; it differs from Strassen
  mod 3 in 13 entries) lifts and reconstructs to a rank-7
  scheme over ℚ that verifies exactly and is not
  entry-identical to Strassen's. Rank 7 for ⟨2,2,2⟩ has been
  known since 1969; the artefact's value is solely as proof
  that the bridge converts native points.
- **The condition.** Lifting requires the F3 point to be
  non-singular (its Jacobian of full expected rank mod 3).
  The bridge therefore changes what an F3 rank-22 *find*
  would be worth — it would be lifted and judged over ℚ the
  same way — but it produces no find by itself, and whether a
  hypothetical F3 point is non-singular can only be checked
  when one exists.
