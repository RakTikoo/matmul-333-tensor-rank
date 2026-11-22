# Claims, at their strongest honest wordings

Every claim below is given in the strongest wording the evidence
supports, with its scope. The "would overclaim" lines are part of the
record: they mark wording we deliberately do not use. Novelty
statements mean "not found in the sources searched", with the search
documented in `data/novelty-audit.md`.

## Headline — Jacobian kernel dimensions at Laderman and Perminov

**Claim.** For the Brent Jacobian J (729 × 621) of the ⟨3,3,3⟩
rank-23 system: dim ker J = 76 over ℚ at Laderman's scheme and 94
over ℚ at Perminov's cn122. The trivial tangent spaces — the
46-dimensional rescaling torus and the 26-dimensional isotropy-orbit
tangent space — span 70 dimensions at each point (overlap 2). Hence
the Jacobian kernel exceeds the trivial (rescaling + isotropy)
tangents by 6 dimensions at Laderman and by 24 at Perminov.

**Evidence.** Two independent implementations agree
(`code/moduli_exact.py`, `code/rigor_check.py`). The pinning
argument: rank of J modulo several primes gives dim ker J over ℚ
≤ the claimed value (rank can only drop mod p), and the exhibited
exact rational kernel bases (`certificates/kernel_*.npz`, every
vector verified J·v = 0 over ℤ) give ≥. The trivial-part accounting
was rebuilt independently, including the correct isotropy action
(inverse-transposes on contracted wires; the naive inverse action
fails exactly the 18 off-diagonal Lie directions).

**Scope.** These are Zariski tangent (Jacobian kernel) dimensions.
Calling 6/24 "local dimensions of the moduli space" would
additionally assume smoothness of the fibre at those points; we
claim the tangent statement, and note the consistency of Perminov's
24 with Heule–Kauers–Seidl's ≥17-dimensional family, and that
Laderman's 6 excludes it from a smooth 17-dimensional part.

**Would overclaim:** "the moduli space has dimension 24 at
Perminov" (unproven smoothness); "Laderman is isolated" (a 6-dim
excess is not isolation).

## Item 1 — covering-parity case split

**Claim.** "We decide term-repair instances for rank-23 ⟨3,3,3⟩
schemes by an exhaustive case split derived from the state's single
wrong entry — cases indexed by which freed terms cover that entry
and the sign pattern of their products there — reducing each
instance to independent SAT/SMT sub-instances. Term-freeing with a
frozen remainder follows Heule–Kauers–Seidl's streamlining; the
covering/sign split itself, and its use to *prove* repair instances
unsatisfiable, we have not found in the literature we searched. In
our runs it decided in minutes instances that resisted hours of
unsplit solving."

**Would overclaim:** "a new case-splitting method for SAT" (case
decomposition is cube-and-conquer's home ground); "the first
exhaustive treatment of term completion" without the "in the
sources searched" qualifier and the streamlining credit.

## Item 2(a) — pair merges

**Claim.** "Applying the standard merge test (Heule–Kauers–Seidl
§8; Kauers–Moosbauer Def. 2) exactly over ℚ, we verified that no
pair of terms merges in Laderman's scheme (λ=1, and hence λ=2 by
rescaling) or in Perminov's cn122 — 759 pairs. For cn122 we have
not found this stated elsewhere."

**Would overclaim:** "we discovered that Laderman's scheme admits
no merging pair" (the check, and a negative outcome over a large
scheme collection, are published; Laderman is a re-verification).

## Item 2(b) — flip component and triples

**Claim.** "Laderman's scheme is an isolated vertex of the flip
graph (Kauers–Moosbauer, arXiv:2212.01175); we confirmed this
independently over {0,±1}. We enumerated the full {0,±1} flip
component of Perminov's cn122 (34,604 states) and tested every term
pair at every state (25.4M tests): no collapsible pair. Across
~75k visited rank-23 states we also ran all 1,771 triples per state
through a rank-≤2 flattening filter (~133M tests): no 3-to-2
collapse. We have not found either census in the literature
searched; Kauers–Moosbauer's Z₂ component census (64,061 vertices)
is the closest published analogue and covers different components
over a different field."

**Would overclaim:** presenting Laderman's isolation as a campaign
discovery; "the flip component of cn122" without the {0,±1} scope;
"no rank-22 scheme is reachable" (the census excludes pair/triple
collapses at visited states of one component, nothing more).

## Item 2(c) — fully decided free-4 instances

**Claim.** "Five frozen-rest repair instances on wrong=1 states of
Laderman and Perminov were decided completely (16/16 exhaustive
cases UNSAT each) over {0,±1}. We have not found published
equivalents."

**Scope (never dropped):** with the stated terms freed, the rest
frozen, over {0,±1}.

**Would overclaim:** "Perminov's scheme cannot be repaired";
"these neighbourhoods contain no rank-22 scheme."

## Item 2(d) — quarters, completely decided

**Claim.** "For Laderman's wrong=1 state with terms {2,3,4} freed
over quarter-integers {0, ±1, ±1/2, ±1/4, ±3/4}, all 174
exhaustive cases are decided, all UNSAT (33 of 33 sign patterns
complete), as of 2026-11-22; the instance is fully decided."
(The audit-time figure was 121/174 and the v1.0.0 figure 166/174;
the completion is evidenced in
`data/quarters-status-2026-11-22.md`.)

**Scope (never dropped):** with terms {2,3,4} freed, the rest
frozen, over the stated coefficient set, on this seed.

**Would overclaim:** "Laderman cannot be repaired" without the
scope — other free-sets and coefficient sets are separate
instances.

## Item 3 — nullity at generic numerical points

**Claim.** "At the generic real rank-23 solutions produced by
numerical optimisation, we measured the CP Jacobian nullity to be
exactly 2r = 46 — the scaling torus and nothing else — so those
points are locally isolated modulo scaling, and quantisation from
generic starts has no local direction to follow. This does not
conflict with Heule–Kauers–Seidl's ≥17-dimensional family: that
family passes through special, structured schemes, while the
numerical points lie on a different, minimal-dimension stratum of
the same variety. We have not found this measurement, or the
diagnosis drawn from it, in the literature searched."

**Would overclaim:** "rank-23 decompositions are isolated" (false
globally); "the solution set has dimension 46"; "rational points
cannot be reached numerically" without the "from generic starts /
by local attraction" scope.

## Standing scope rules for everything above

- Every UNSAT comes from an encoding validated by a control (the
  same terms freed on a known-good scheme returns SAT and the
  candidate verifies exactly). Timeouts are recorded as
  "no conclusion" and appear in no claim.
- Every field is named: a statement over {0,±1}, quarter-integers,
  F₂, or ℚ says nothing about the others.
