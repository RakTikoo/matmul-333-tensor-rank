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

## Item 9 — census extension: the universal form does not extend beyond the original bank

**Claim.** "We extended the Wave 26/28 unit-term census to every other verified ⟨3,3,3⟩ scheme on our disk: 48 further files, 40 distinct schemes, each re-verified exactly over Q. Of the 50 unit terms in those 40 schemes, 49 are naive — and one is not. The exception is term 0 of the rank-24 scheme obtained by downward projection of a ⟨3,3,4⟩ scheme (solven-eu catalogue): its factors are e₅, −e₈, e₄, so its single entry sits at position (5,8,4), where the matrix-multiplication tensor is zero. The universal statement 'every unit term in every verified scheme is naive' therefore does not extend beyond the original bank. What survives is narrower: every unit term in every rank-23 scheme in the extended census is naive (the published 41-of-41 statement about the original 11 bank schemes is untouched), and the single counterexample is at rank 24, in a scheme of a different construction type. Two independent exact computations agree on every count. Unit-term-ness is a property of a scheme's presentation, not of its orbit: the 30 de Groote transforms of Laderman in the census carry no unit terms at all. This is anatomy of the schemes we hold, not evidence about rank 22."

**Evidence.** Two independent exact computations agree on every
count: the Wave-30 census and the Wave-32 gate's from-scratch
recount (`code/recount_census_extension.py`), which re-judged
each of the 48 files two ways — its own exact Fraction
recomputation (0 wrong of 729 for every file) and a fresh-process
`verify.py check` run (48/48 VERIFIED) — and recomputed the
census from the tensor definition in both countings (per file:
210 unit terms, 209 naive, 1 off-support; per distinct scheme:
50, 49, 1). The counterexample was inspected directly from its
file. Full record in `data/census-extension.md`.

**Scope.** The named population only: the 48 held-out files /
40 distinct schemes on the campaign disk. The
Heule–Kauers–Seidl database of 17,000+ schemes was not censused,
and schemes not on this disk are outside the population.

**Would overclaim:** "every known rank-23 scheme…" without
naming the census population; "the pattern fails at rank 24" as
a general statement about rank-24 schemes (exactly one rank-24
scheme in the census carries a unit term at all); any
implication for the HKS database or for rank-22 existence.

## Item 10 — cluster anatomy under the registered greedy method

**Claim.** "Under one fixed greedy procedure — core = the scheme's unit terms; the remaining terms merged agglomeratively into clusters of at most 3 so as to minimise the total number of off-support positions at which cluster sums are nonzero ('garbage'); the procedure is greedy, not optimal — the three rank-23 schemes measure as follows. Laderman: garbage falls from the all-singletons baseline 184 to 72, through four triples each carrying garbage 9 and six singletons each carrying garbage 6. Perminov's cn122: 422 to 136. Perminov's cr58_cn122 (T11): 390 to 148. In the Laderman and cn122 partitions, the clusters' on-support parts together with the core cover the tensor's 27 support positions with no overlap at all — every cancellation in those partitions is off-support; in T11 there are exactly 2 on-support overlaps. Two independent implementations of the procedure agree on every total and on the partitions themselves. These are measurements of the schemes under this procedure, not invariants: a different objective or an optimal partitioner could give different numbers. Whether the shared qualitative anatomy — a naive core, a few garbage-cancelling triples, a tail of near-clean singletons — is generic for sparse exact schemes is a hypothesis; no test of it has been run."

**Evidence.** Two independent implementations of the procedure
agree on every total and on the partitions themselves: the
Wave-30 measurement and the Wave-32 gate's re-implementation
from the registered specification alone
(`code/clusters_greedy.py`), which reproduced the baselines
(184 / 422 / 390), the greedy totals (72 / 136 / 148), every
step of every greedy history, the Laderman file-order record
([20, 23, 20, 30, 16, 9], total 118), the exact final
partitions, and all three support-tiling counts (0 overlaps for
Laderman and cn122; exactly 2 for T11). Full record in
`data/cluster-anatomy.md`.

**Scope.** A measurement under one named algorithm on three
named schemes. The totals are outputs of the procedure — not
invariants of the schemes, not optimal partitions, and not
comparable to numbers produced by any other objective or method.
The specification's three underdetermined points (tie-break
reading, lexicographic referent, term-index convention) are
recorded in `data/cluster-anatomy.md`; the agreement above is
under the gate's independent readings of them.

**Would overclaim:** the bare totals ("Laderman's garbage is
72") without the method; "the schemes decompose into clusters"
as a structural theorem; the cross-basin anatomy as anything but
a labelled hypothesis; any implication for rank 22.

## Item 11 — the HKS census: every unit term in the Linz population is naive

**Claim.** ""We censused the complete Heule–Kauers–Seidl repository of ⟨3,3,3⟩ rank-23 schemes as distributed (17,376 schemes, all with entries in {−1, 0, 1}). Across the whole population there are 1,882 unit terms — terms whose tensor has a single nonzero entry — and every one of them is naive: its entry sits on the 27-position support of the matrix-multiplication tensor. No off-support unit term exists in this population. Three independent computations agree on every count (a SAT-solver-hosted kernel run, and two differently-structured home recounts, one of which also verified all 17,376 schemes exactly, with zero wrong entries). This extends our earlier bank censuses (41 of 41 unit terms naive across the 11 original bank schemes; 49 of 50 across 40 further schemes, the single exception being a rank-24 scheme): within rank 23, every unit term in every scheme population we have censused is naive. The statement is about these named populations — it is not a theorem about all rank-23 schemes over Q, and it is not evidence about rank 22: a rank-22 scheme need not contain any unit term.""

**Evidence.** Three independent computations agree on every
count: the Kaggle kernel census (in-kernel download and parse;
all 1,708 unit-carrying schemes and a seeded 300-sample of
zero-unit schemes verified exactly, 0 failed); the home recount
(`code/recount_hks_census.py`), which re-derived the census
from the locally held archive and verified **all 17,376 schemes
exactly, 0 wrong entries anywhere**; and the Wave-47 gate's
product-route derivation, which reproduced the headline tallies
over the full population and verified a 1,000-file slice
scheme-by-scheme (1,000/1,000 exact). The three paths share
only the archive bytes and the `.tab` format facts, each
re-diagnosed by its own verification leg; no code is shared.
Full record in `data/hks-census.md`.

**Scope.** The Heule–Kauers–Seidl population as distributed
2020-08-06, entries in {−1, 0, 1} — not all rank-23 schemes
over ℚ. This item closes the gap carried in the Scope lines of
Items 4 and 9 ("the Heule–Kauers–Seidl database was not
censused") for this population; schemes with entries outside
{−1, 0, 1} and schemes outside the repository remain covered
only by the earlier bank censuses (Items 4 and 9).

**Would overclaim:** "every known rank-23 scheme…" without
naming the population; "unit terms are always naive" as a
universal (the rank-24 counterexample of Item 9 stands, one
term in one scheme); any suggestion that the HKS authors state
or endorse this census (the population is theirs, the census is
ours); any implication for rank-22 existence.

## Item 12 — walk anatomy: the terms-merging trips were cancellation artefacts

**Claim.** ""Our homotopy walks along the rank-23 fibre (Wave 20 machinery, run on Kaggle) tripped a 'terms merging' monitor — pairwise term cosine above 0.99 — in four of five directions. Exact follow-up shows the trips were an artefact of the monitor, which recorded the cosine's absolute value: the signed cosines are ≈ −0.99, so the pairs approach anti-parallelism (mutual cancellation), not parallelism (fusion). While the cosines climbed, the pairs' sums stayed bounded and their rank-1 defect stayed flat or grew (1.00→1.02 in the cleanest direction), the individual term norms inflated by an order of magnitude or more, and replacing a pair by its best rank-1 approximation leaves tensor errors of 1.02–9.42 against ‖T‖ = 5.20; rational reconstructions of the fused 22-term forms were rejected by exact verification on all 729 entries. The walk was sliding along the fibre's non-compact cancellation directions, where |cos| → 1 is automatic. A structural by-product, verified exactly over Q by an independent check: each of the three tripping Perminov pairs shares a factor column identically in the seed (terms 6 and 20 share their W column; terms 2 and 18 and terms 5 and 8 share their V columns) — the cancellation directions live on those shared-factor strata. (A complete scan finds seven shared-factor pairs in cn122 in total; the three above are the ones the walk tripped on. Laderman's scheme has no identical factor-column pair at all.) We have retired the |cos| trip criterion; a merge signal requires a pair-sum rank-1 defect → 0 at bounded term norms. Nothing in this episode bears on whether rank-22 schemes exist: these paths do not approach one, and no conclusion about the families' closures is drawn.""

**Evidence.** Wave 45's exact follow-up on the harvested walk
states (signed cosines, pair-sum defects, fusion errors, and
the fresh-process verify.py rejections of both fused-22
candidates, 729/729 wrong each), and the Wave-47 gate's
independent re-derivation: the three shared-factor identities
exact over ℚ from the seed files (cn122 W 6 = 20, V 2 = 18,
V 5 = 8), Laderman's absence of any identical factor-column
pair, and the Perminov dir0 signed-cosine record re-checked
from the harvested states (factor cosines +0.99471 / −0.99734 /
+1.000000; signed product −0.99207; pair-sum norm 3.0000 →
1.7777), agreeing with Wave 45 to its recorded precision. Full
record in `data/walk-anatomy.md`.

**Scope.** A methods statement about the named runs (Wave 20
machinery, matmul-walk v3) only. The defect, fusion and
reconstruction numbers beyond the gate's re-derived legs stand
on Wave 45's record plus the verify.py rejections issued there.

**Would overclaim:** "the walk found the edge of the family /
approached rank 22" (the fused forms are O(1) away); "cn122
has three shared-factor pairs" unscoped (seven in total; the
three named are the tripping pairs); any use of the episode as
evidence for or against rank 22.

## Item 13 — transplant closure at unequal cardinalities, bank-wide

**Claim.** ""We extended the cross-scheme transplant census to unequal cardinalities across the whole enlarged bank: all subset sums of sizes 1–4 over the 60 distinct verified ⟨3,3,3⟩ schemes we hold (679,539 sums, exact), compared between adjacent cardinalities (2,1), (3,2), (4,3), within and across schemes. The only exact equalities anywhere are 277 hits between the rank-25 scheme we ourselves constructed by splitting one term of the rank-24 metaflip scheme in Wave 22 and that parent scheme — the split's own undoing, with counts 1, 23, 253 = C(23, k−2) exactly, whose assembled candidate is the parent scheme itself. There is no genuine cross-scheme subset-sum swap at any cardinality ≤ 4 in this pool; together with the earlier equal-cardinality censuses (depth ≤ 4 over the core 8 schemes), the transplant line is closed at all cardinalities ≤ 4 for the schemes we hold. Two independent exact computations agree on every hit and every count. Depth-5 comparisons were not run; nothing here is a statement about schemes outside the bank.""

**Evidence.** Two independent exact computations agree on
every hit and every count: the Wave-41 census (3-prime digest
index over sparse exact subset sums, every candidate
re-verified exactly) and the Wave-47 gate's re-derivation on a
21-scheme sub-pool by a different route (global-LCM integer
scaling, dense integer arrays, sha256 index with exact
confirmation — no modular digest), which reproduced the
complete hit census (277 hits, counts 1 / 23 / 253, zero
genuine) because every hit involves only split-25 and
metaflip-24, both in the sub-pool. Full record in
`data/transplants.md`.

**Scope.** The 60 distinct verified schemes of the enlarged
bank; subset sums of sizes 1–4; adjacent-cardinality
comparisons. Depth-5 comparisons were not run, and the gate's
second path re-derives the hit census, not the 679,539-sum
full-pool total.

**Would overclaim:** "transplants are impossible" without the
pool and cardinality bounds; "the basins are disconnected" as
a geometric statement (this is a subset-sum census over named
schemes, not a statement about the fibre's topology); any
implication for rank 22 beyond "this pool, this depth, no
swap".

## Item 14 — the delta table: wrong=1 neighbours across ranks 23–26

**Claim.** ""For each of six verified ⟨3,3,3⟩ schemes spanning ranks 23–26 (Laderman, Perminov's cn122, the two catalogue rank-24 schemes, our constructed rank-25 split, and our rank-26 block scheme), we computed the full single-drop battery exactly: the state left by dropping one term, and how many entries it gets wrong. A wrong=1 neighbour exists in exactly the schemes that have a unit term — Laderman (5, all naive), cn122 (3, all naive), proj-24 (1), lensC-26 (19, all naive) — and in none that do not (metaflip-24 and split-25, whose closest drops are 2 wrong). The near-miss structure does not soften gradually down the ranks 25→24→23; which flavour of wrong=1 neighbour a scheme offers is a property of its unit terms, not of its rank. Every wrong=1 state in the table is the standard flavour — one missing entry on the tensor's support, have 0 / want 1 — except one: proj-24's unique unit term sits off-support (its factors are e₅, −e₈, e₄, its single entry −1 at (5,8,4), where the tensor is zero), so its drop state has an extra entry to cancel rather than a missing one to fill: have +1 / want 0 at (5,8,4). That state is banked, and its repair instance is staged. The proj-24 and Laderman rows were re-derived by an independent exact computation for this gate, agreeing on every count; proj-24's battery had already been cross-checked drop-by-drop against the exact verifier in Wave 40.""

**Evidence.** Wave 40's exact single-drop batteries over the
six named schemes, with the proj-24 battery cross-checked
drop-by-drop (24/24) against fresh `verify.py mismatch` runs
in Wave 40 itself; and the Wave-47 gate's fresh exact battery,
which re-derived the proj-24 and Laderman rows in full,
agreeing on every count (proj-24: exactly 1 unit term, term 0,
−1 at (5,8,4), off-support; minimum drop wrong 1 attained once;
the minus-0 state have +1 / want 0 — Wave 40's sign correction
independently confirmed. Laderman: 5 unit terms, all naive,
all +1; distribution {1:5, 7:6, 8:8, 27:4}). cn122's unit
census (3, all naive) is independently re-derived by the
Wave-28 recount and by Item 12's gate leg. Full record in
`data/delta-table.md`.

**Scope.** Six named schemes. Recorded limit: the full drop
distributions of metaflip-24, split-25 and lensC-26 have no
second path beyond Wave 40's own record (plus a CLI spot-check
of metaflip-24's minimum); their unit counts (0, 0, 19) are
corroborated as stated in `data/delta-table.md`. The claim's
load-bearing rows do not rest on the un-recounted
distributions.

**Would overclaim:** the bare "iff" as a theorem about
arbitrary schemes (it is a table over six named schemes, and
at single-drop level the equivalence is near-definitional —
the content is the flavour and rank pattern); "the first
off-support wrong=1 state" unscoped (it is the first in this
campaign's bank, and the only one in the six-scheme table);
any implication that the staged repair instance bears on
rank 22 (a repair of proj-minus-0 would assemble a rank-23
scheme).

## Standing scope rules for everything above

- Every UNSAT comes from an encoding validated by a control (the
  same terms freed on a known-good scheme returns SAT and the
  candidate verifies exactly). Timeouts are recorded as
  "no conclusion" and appear in no claim.
- Every field is named: a statement over {0,±1}, quarter-integers,
  F₂, or ℚ says nothing about the others.
