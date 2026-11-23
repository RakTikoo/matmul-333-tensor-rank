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

## Item 4 — cartography: unit terms are naive

**Claim.** "In the rank-23 ⟨3,3,3⟩ schemes we hold (the Laderman
λ-family, Perminov's cn122, and the T11/T12 family), every unit
term — a term with a single nonzero entry in each factor — is a
naive term e_(i,j)⊗e_(j,k)⊗e_(i,k): 41 of 41, by direct census.
Equivalently, all 46 banked rank-22 states that differ from a
scheme by one dropped term and exactly one wrong entry have that
entry on the 27-position support of the tensor, concentrated in
8 orbits of the entry-symmetry group ⟨Φ, A↔B duality⟩ covering
21 of 729 positions; the concentration was pre-registered in
Wave 26 and held on a held-out family (5 of 5). We have not
found this census or the orbit concentration stated in the
literature we searched (see `data/novelty-audit-2.md`); the
nearest prior observation is Blankline Research's 'four anchors'
in Laderman's scheme alone (2026, not peer-reviewed). This is
anatomy of the known schemes, not evidence about rank 22: a
rank-22 scheme need not contain any unit term."

**Evidence.** Two independent computations agree: the Wave-26
pipeline (population, statistic and holdout split registered
before any position was extracted) and the Wave-28 gate's
from-scratch recount (`code/recount_cartography.py`), which
re-derived every count exactly — 157 files, 46 unique wrong=1
states, 46/46 wrong entries on the support, 8 hit orbits
totalling 21 positions, 41/41 unit terms naive. The Monte Carlo
p-values (p < 10⁻⁵; holdout p ≈ 2×10⁻⁸) are Wave 26's; the gate
re-derived every input to them but did not re-run the Monte
Carlo. Full record in `data/cartography.md`.

**Scope.** The named bank only. The Heule–Kauers–Seidl database
of 17,000+ schemes was not censused.

**Would overclaim:** "every known rank-23 scheme…" without
naming the bank; "first/novel discovery that fast schemes
contain naive terms"; any phrasing suggesting the pattern bears
on the existence of rank 22.

## Item 5 — the T11 point (Perminov's cr58_cn122)

**Claim.** "Perminov's cr58_cn122 (a rank-23 scheme for ⟨3,3,3⟩
from his public database, reprinted by Karunaratne–Idamekorala
and by the boulder-swarm project) is not equivalent to
Laderman's scheme or to Perminov's cn122: the per-slot
factor-rank multisets — invariants of the isotropy action —
differ from both, under any permutation of the slots. At this
point the Brent Jacobian over ℚ has kernel dimension 94,
exceeding the trivial rescaling and isotropy tangents (70) by
24 dimensions — the same excess as at cn122, in a different
orbit. No pair of its 23 terms merges over ℚ (0 of 253 pairs
have a rank-1 sum), so it yields no rank-22 scheme by dropping
two terms and completing with one."

**Provenance (never dropped).** The scheme is Perminov's, not a
campaign discovery; the campaign found it in a third-party
repository and measured it. Its distinctness from cn122 is
implicit in Perminov's own class labels; the invariant proof
and the kernel and pair-merge numbers are the campaign's
measurements. Scheme: `certificates/perminov_cr58_cn122_r23_Q.json`;
full record in `data/t11-basin.md`.

**Evidence.** Two independent paths agree: the Wave-24/25
computations, and the Wave-28 gate's from-scratch Jacobian at
fresh primes (`code/check_kernels_independent.py`) re-pinning
the nullity two-sided, its own tangent construction reproducing
the trivial span 70, and a fresh drop-2 test (0 of 253).

**Scope.** The excess is a kernel-minus-trivial-tangents count
(the Headline scope rule applies). Bounded flip walks from this
point visited state sets disjoint from cn122's, but
flip-component identity is formally undecided; the proven
separation is the isotropy orbit.

**Would overclaim:** "a new scheme / a new basin discovered by
the campaign"; "the flip-graph component of T11 is disjoint
from cn122's" as a proven statement; "local dimension of the
moduli space" for the excess 24.

## Item 6 — ladder points at ranks 24 and 26

**Claim.** "At the two genuine rank-24 schemes we measured (a
Perminov meta-flip-graph scheme and a downward projection of a
⟨3,3,4⟩ scheme, both from the solven-eu catalog), the Brent
Jacobian over ℚ has kernel dimension 102 and 111, exceeding the
trivial tangents (72) by 30 and 39 dimensions. At the campaign's
own rank-26 block construction the kernel dimension is 187,
exceeding the trivial tangents — 73 at this point, not the
generic 78, because the torus and orbit tangents overlap in 5
dimensions there — by 114. All values are exact over ℚ, pinned
from both sides. Together with the rank-23 values (Laderman
excess 6; cn122 and cr58_cn122 excess 24) they show no monotone
behaviour in the rank: within-rank spread is as large as any
between-rank difference, so these numbers constrain nothing
about rank 22."

**Evidence.** Two independent paths agree: the Wave-22
computations and the Wave-28 gate's from-scratch Jacobian at
fresh primes (`code/check_kernels_independent.py`) — ranks
agreeing at each point, stored kernel bases annihilated exactly
(0 failures in 494 vector checks), trivial spans independently
reproduced (72, 72, 73). Full record in `data/ladder.md`,
including the rank-25 split row used as calibration only
(artificial kernel identified and removed exactly; net excess
30, equal to its parent's).

**Scope.** Pointwise measurements at the named schemes. The
trivial span is measured at each point, never assumed.

**Would overclaim:** any "thinning toward rank 22" narrative;
"moduli space dimension" phrasing; borrowing these pointwise
numbers to support claims about other ranks or about rank-22
(non)existence.

## Item 7 — cross-family transplants

**Claim.** "Among the eight rank-23 schemes in our bank (the
Laderman λ-family, Perminov's cn122, and Perminov's
cr58_cn122), exact comparison over ℚ finds the three families
share almost no raw material: of 184 rank-1 terms only 158 are
distinct, but the single term shared across families is one
naive unit term (at (1,0,1)); and no pair of terms from one
family sums to a pair from another (1,974 distinct pair sums,
no genuine cross-family collision). In this bounded sense —
these eight schemes, transplants of depth at most 2, over ℚ —
the families cannot be hybridised by swapping one or two terms.
We have not found this term-sharing census stated in the
literature we searched; the neighbouring published notions are
de Groote equivalence classes and flip-graph components."

**Evidence.** Two independent computations agree exactly on
every number (the Wave-26 census and the Wave-28 gate's fresh
canonicalisation). Full record in `data/transplants.md`.

**Scope.** These eight schemes, depth ≤ 2, over ℚ. Rank-24
schemes excluded; the Heule–Kauers–Seidl database not censused.

**Would overclaim:** "the basins are disconnected" without the
depth/schemes/ring bounds; any implication for depth ≥ 3 or for
flip-graph connectivity in general.

## Item 8 — Blankline audit

**Claim.** "Blankline Research's January 2026 report (Zenodo
18443297) makes two checkable claims. The first — that the
compound term with u={3,5,6,8}, v={1,2,7,8} cannot route its
products consistently — is correct in its stated single-term
scope; we verified the witness rows directly. The second — that
its '1+2+19' structure has minimum residual √6, identical for
all 2^16 sign patterns — does not hold for the part of the claim
that can be reconstructed from the publication: two independent
exact computations give a minimum residual² of 7 (not 6) for the
compound term T1, with the residual taking five distinct values
across sign patterns, so it is not sign-invariant either. The
full 22-term claim cannot be decided from the publication,
because the supports of the remaining terms are never given.
Neither result moves any bound on the rank of ⟨3,3,3⟩."

**Evidence.** Two independent exact computations (campaign
Wave 24; the Wave-28 gate's independent derivation from the
PDF) agree exactly, including the five-value residual set
{7, 29/4, 15/2, 31/4, 8}. Full record in
`data/blankline-audit.md`.

**Scope.** An audit of one named, non-peer-reviewed source.
Its Theorem 8 is untouched by this audit.

**Would overclaim:** "Blankline's barriers are refuted" as a
wholesale statement (claim (i) is confirmed; their Theorem 8 is
untouched); "the 1+2+19 structure is impossible" (only its
printed numbers fail, on the reconstructible core).

## Standing scope rules for everything above

- Every UNSAT comes from an encoding validated by a control (the
  same terms freed on a known-good scheme returns SAT and the
  candidate verifies exactly). Timeouts are recorded as
  "no conclusion" and appear in no claim.
- Every field is named: a statement over {0,±1}, quarter-integers,
  F₂, or ℚ says nothing about the others.
