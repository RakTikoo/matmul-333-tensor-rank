# The border line: a conversion equivalence, a missing explicit family, and a measured generic-point obstruction

**Date:** 2026-11-24. Negative results and instrument anatomy
for the border-rank route to ⟨3,3,3⟩ (border rank
15 ≤ R̲ ≤ 21: Landsberg–Ottaviani 2015 for the lower bound,
Schönhage 1981 for the upper). This record is grouped under
negative results; nothing in it is a construction.

## The claim, at its approved wording

"Three border-rank statements, all scoped. (1) The often-imagined shortcut does not exist: requiring a 21-term Laurent family to satisfy the tensor identity to *all* orders is exactly the statement R ≤ 21, and the 22-term version is exactly R ≤ 22; a single extra term can push the first defect one order higher only when that defect is itself rank 1, and killing all defects is the original problem. The border-plus-one route is equivalent in difficulty to exact rank. (2) Border rank 21 for ⟨3,3,3⟩ is proved in the literature only through Schönhage's asymptotic sum inequality — the saving lives in the limit over direct sums and tensor powers; no explicit 21-term Laurent family for the single tensor appears in any source we could access, and an earlier version of our own strategy document claimed otherwise and has been corrected. (3) Our numerical route to a border family failed its calibration, and we measured why: on Bini's border-10 family for ⟨3,2,2⟩ the search does show the genuine border signature (residual falling as a power law in the factor norms, exponent 3.58 against a predicted 3), and high-precision polishing drives the defect to 1.6e-76 — but the point it converges to is a *generic* point of a solution component with 106 genuine moduli (Jacobian nullity 126, of which only 20 are gauge), so its coordinates admit no low-degree algebraic description for exact reconstruction to find. The failure is genericity, not precision. The border line is parked, with three named revivals in our record (pattern-constrained solves, homotopy from Bini's rational point, α-theory certification)."

## The three statements, unpacked

**(1) Conversion equivalence (proved).** A border
decomposition is a Laurent-polynomial identity
T(ε) = T + O(ε^q) with 21 or 22 terms. Demanding the identity
hold to *all* orders collapses the Laurent family to an
ordinary decomposition: a 21-term all-orders identity is
exactly R ≤ 21, a 22-term one exactly R ≤ 22. The
"border-plus-one" idea — a border-21 family plus one
correcting term — buys exactly one order of vanishing, and
only when the first defect tensor is itself rank 1; killing
every defect is the original problem restated. The route is
equivalent in difficulty to exact rank, not a shortcut
around it.

**(2) The literature finding.** Schönhage's border-rank-21
bound is proved through the τ-theorem / asymptotic sum
inequality: border rank is subadditive under direct sums,
and the single-tensor bound is extracted from tensor powers.
The saving lives in the limit. No explicit 21-term Laurent
family for ⟨3,3,3⟩ alone was found in any accessible source
(the 1981 paper is paywalled; its disjoint-sum configuration
appears in no accessible secondary source we found). An
earlier version of the campaign's own strategy document
claimed such formulas were published; they are not, and the
document has been corrected.

**(3) The calibration anatomy.** The numerical route
(complex renormalised border-ALS at rank 21, exactified by
rational reconstruction) was gated on a calibration it then
failed: Bini's ⟨3,2,2⟩ border-10 family, which this
repository's machinery judges exactly. The search *does*
show the border signature (residual falling as a power law
in the factor norms; fitted exponent α = 3.58, R² = 0.991,
against the balanced-gauge prediction 3), and high-precision
Gauss–Newton polishing drives the defect to 1.6×10⁻⁷⁶ — but
the converged point is generic on a component with 106
genuine moduli (Jacobian nullity 126 = 20 gauge + 106
moduli), so its coordinates have no low-degree algebraic
description for PSLQ-style reconstruction to find, at any
precision. The failure is genericity, not precision. (The
calibration also caught two of our own errors, recorded in
the campaign record: a pair of pre-registered depth
thresholds that were mutually inconsistent by ~2 decades
under the fitted law, and a relation-finder embedding bug
caught by known-algebraic controls.) The line is parked;
the named revivals are pattern-constrained solves on a
small-field sub-locus, homotopy from Bini's rational point
along the component, and α-theory existence certification.
