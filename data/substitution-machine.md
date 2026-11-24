# The substitution machine: a validated lower-bound instrument, and its measured reach

**Date:** 2026-11-24. A methods/validation record. The
substitution method (Bläser 2003) is the only known technique
that has raised the exact-rank floor for ⟨3,3,3⟩; Wang's
2026 automated form of it produced the current finite-field
bounds. We implemented the method, validated the instrument
end-to-end on a case with a known answer, and measured how
far our implementation gets on ⟨3,3,3⟩. Its bounds are
weaker than the published ones everywhere, and this record
is published as a validation item, not as a bound.

## The claim, at its approved wording

"We implemented the substitution method for tensor-rank lower bounds in the automated form of Wang (2026) and validated the instrument end-to-end: on ⟨2,2,2⟩ it reproduces Wang's 10 restriction orbits, certifies rank ≥ 7 over both F2 and F3, and its backtracking search then *completes* at target 8 with a negative — the sound answer, since the exact rank is 7. Run on ⟨3,3,3⟩, our implementation certifies rank ≥ 14 over F2 and ≥ 12 over F3. These bounds are **weaker than the published ones** — 19 over any field (Bläser 2003) and at least 21 over F2 (Wang; Yang et al., 2026) — and we publish them only as the instrument's measured reach, with the stall anatomy: our canonicalisation used the monomial subgroup, the restriction lattice grew to 3,389 orbits by dimension 3 (Wang's full-group treatment needs 496 in total), and the budget died before the strong leaves could fire. Closing the gap is a compiled full-group reimplementation, whose specification is in our record. The value of the item is a working, control-validated lower-bound machine whose certificates are checkable line by line — not a bound."

## Validation and stall anatomy

- **Control (⟨2,2,2⟩, exact rank 7).** The machine finds
  exactly 10 restriction orbits (Wang's count), certifies
  rank ≥ 7 over both F2 (1.8 s) and F3 (88 s), and its
  backtracking search then *completes* at target 8 with a
  negative — the sound answer. An instrument that overclaims
  would have "certified" 8; this one proves 7 and stops.
- **⟨3,3,3⟩ over F2: certified ≥ 14.** The bound comes from a
  dimension-2 restriction whose flattening bound of 9 is
  raised to 14 by the substitution bootstrap (all its
  dimension-1 children have exact bound 9; the pigeonhole
  closes targets 10–14 and completes at 15 as not-provable).
  242 states in the lattice carry bounds ≥ 12. The
  certificate is a per-state bound table with proof tags,
  checkable line by line.
- **⟨3,3,3⟩ over F3: certified ≥ 12,** by a targeted
  certificate on the same dimension-2 restriction (the full
  F3 lattice run timed out on canonicalisation cost — an
  engineering stall, recorded as such).
- **Why it stalls.** Canonicalisation used the monomial
  subgroup rather than Wang's full group, so the restriction
  lattice grew to 3,389 orbits by dimension 3 alone, against
  Wang's 496 orbits in total; the budget died in low
  dimensions before the strong Hopcroft–Kerr leaves
  (⟨2,2,3⟩ ≥ 11, ⟨2,3,3⟩ ≥ 15 over F2) could fire, and the
  top-orbit backtracking never ran. Closing the gap to the
  published bounds is a compiled full-group
  reimplementation, specified in the campaign record.

**The published bounds, for the same paragraph:** 19 over
any field (Bläser 2003); over F2, 20 (Wang 2026), then 21
(Wang; Yang et al., independently, 2026) — and the 2026 F2
endgame beyond 21 is summarised in the release notes'
literature section. Our 14 and 12 improve nothing.
