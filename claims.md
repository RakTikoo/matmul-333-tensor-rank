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

## Item 15 — the repairs closure: 1,843/1,843 cases UNSAT

**Claim.** ""The repair front is decided at its registered scope. For each of seven banked near-miss states — six 22-term wrong=2 states from rank-23 parents and the one off-support wrong=1 state (proj-24 minus term 0) — we enumerated every covering-parity case of the free-4 repair move (four terms freed, coefficients in {0, ±1}, the other terms frozen, over Q): 1,843 cases in total. All 1,843 are UNSAT, with the encoder's control gate passed in the same run and its control artefacts re-verified exactly at home. No rank-22 scheme is reachable by this repair move from any of these seven states, and the off-support state has no free-4 {0,±1} repair to a new rank-23 scheme either. The closure is scoped to this move, this free-set size, and this coefficient set; other repair settings are separate fronts.""

**Evidence.** The Wave 51 run (laptop, generalised
parity-split driver) decided all seven instances: six
wrong=2 instances at 304 cases each and the off-support
wrong=1 instance at 19 cases, summing to 1,843, with 0 SAT,
0 no-conclusion and 0 not-attempted. The encoder's control
gate passed in the same run, and the control artefacts were
re-judged at home in fresh `verify.py` processes (all
VERIFIED). Full record in `data/repairs-closure.md`.

**Scope.** The free-4 repair move (four terms freed,
coefficients in {0,±1}, the rest frozen) over ℚ, on the seven
named states. An UNSAT excludes a covering vector for the
freed terms on that seed — not a neighbourhood in the
continuous sense.

**Would overclaim:** "repairs are impossible" without the
scope; any suggestion the closure bears on rank 22 in
general.

## Item 16 — the new-basins front fully decided: 336/336

**Claim.** ""The new-basins free-4 front is fully decided. The 21 wrong=1 states obtained in Wave 39 from nine orbit-distinct catalogue schemes generated 336 free-4 {0,±1} repair cases over Q; all 336 are UNSAT (21/21 instances decided, controls passed). No rank-22 scheme is reachable by this repair move from any of these 21 states.""

**Evidence.** The completed Kaggle run decided 21/21
instances (16 cases each, 336 total), all UNSAT, controls
passed in-session. The 21 states derive from nine solven-eu
catalogue schemes proven pairwise orbit-distinct in Wave 39.
Full record in `data/repairs-closure.md`.

**Scope.** The same free-4 {0,±1} move, on these 21 states.
The tally may be summed with Item 15's only as "2,179 decided
repair cases across the two fronts", each front named.

**Would overclaim:** dropping "by this repair move from
these states"; merging the two fronts' tallies without
naming both.

## Item 17 — the walk line closure

**Claim.** ""The walk line is closed. The gauge-fixed re-walk built after the Wave 45 artefact anatomy (term-norm cap at 3× the seed maximum, defect-monotone exception, a trip defined as defect < 0.05 at bounded norms) ran in all five registered directions; every direction stalled. Under the line's pre-registered rule, the walk approach to rank reduction from these seeds is closed. This complements the v1.3.0 walk-anatomy item: the earlier trips were cancellation artefacts, and the corrected instrument finds no genuine approach either.""

**Evidence.** The completed walk4 run: all five registered
directions STALL, no TRIP, under the criterion pre-registered
when the instrument was built (defect < 0.05 at bounded term
norms). This is the decider run that follows Item 12's
anatomy; the two items are distinct — Item 12 is about the
old monitor's artefact, this one is the corrected
instrument's verdict. Full record in `data/walk-anatomy.md`
(v1.4.0 extension).

**Scope.** These seeds, this instrument, this criterion.

**Would overclaim:** "walks cannot reach rank 22";
presenting this item as re-proving Item 12.

## Item 18 — the hinge free-4 front, partial: 631/3,072

**Claim.** ""Of the 3,072 free-4 {0,±1} repair cases derived from the 192 hinge wrong=1 states of Wave 48, 631 have been decided — all UNSAT (39 of 192 instances fully decided, one further instance partially). The remaining 2,441 cases are not yet attempted; this front is partial, and no front-level conclusion is drawn from it.""

**Evidence.** The 192 states derive from Wave 48's hinge
construction (84 exact schemes from re-factorising cn122's
seven shared-factor pairs). The completed run decided 631
cases, all UNSAT: instances I000–I038 fully, I039 at 7/16;
2,441 cases were not attempted. Full record in
`data/partial-fronts.md`.

**Scope.** A partial front: decided cases only, with the
denominator and the not-attempted count always attached.

**Would overclaim:** any phrasing implying the hinge front
is decided or closed; "631 UNSAT" without 3,072 and 2,441.

## Item 19 — the proj24-family free-4 front, partial: 943/1,140

**Claim.** ""Of the 1,140 free-4 {0,±1} repair cases derived from the 60 wrong=1 drop states of the Wave 55 shear families (on the exact rank-24 parents proj24 and metaflip24), 943 have been decided — all UNSAT (49 of 60 instances fully decided, one partially). The remaining 197 cases are not yet attempted; the front is partial. A repair here would have assembled an exact rank-23 scheme, not a rank-22 one; the front's value is ladder connectivity (Wave 66), and the wording must keep that scope.""

**Evidence.** The 60 states are single drops from the Wave
55 shear families on the exact rank-24 parents proj24 (6
pairs) and metaflip24 (1 pair), 19 cases per instance. The
completed run decided 943 cases, all UNSAT: 49/60 instances
fully, one at 12/19; 197 not attempted. Full record in
`data/partial-fronts.md`.

**Scope.** The parents are rank 24 and the states 23-term: a
repair here assembles an exact rank-23 scheme, not a rank-22
one. The front's value is ladder connectivity.

**Would overclaim:** presenting these as rank-22 repair
cases; implying the front is closed.

## Item 20 — the shear-family free-4 front, partial, with the lost run disclosed

**Claim.** ""Of the 14,016 free-4 {0,±1} repair cases derived from the 876 wrong=1 states of Wave 56, 414 have been decided — all UNSAT (25 of the 360 instances in the completed kernel, covering the Kauers, cn97 and c88 parents). The companion kernel's run (the cn119 and cn120 instances, 8,256 cases) was lost when its interactive session ended before the results could be harvested; the partial verdicts observed during that session are unrecoverable and are **not** counted anywhere in this release. A committed re-run is queued. The shear-family front is therefore mostly undecided: 5,346 cases in the completed kernel were not attempted, and the lost kernel's 8,256 cases stand wholly undecided.""

**Evidence.** Wave 56 derived 876 wrong=1 states from five
C0-gated rank-23 parents (468 exact shear variants). The
Kauers/cn97/c88 kernel completed on budget: 414 UNSAT, 0 SAT,
25/360 instances fully decided, 5,346 not attempted. The
cn119/cn120 kernel's run was lost (interactive session ended
before harvest); its ~45 observed partial verdicts are
unrecoverable and are counted nowhere in this release. Full
record in `data/partial-fronts.md`.

**Scope.** The honest decided fraction of the surviving
record is 414/5,760; of the staged family, 414/14,016 with
the loss stated.

**Would overclaim:** any shear-family total that silently
sums decided and lost runs; counting any verdict from the
lost session.

## Item 21 — rulers at cn122: no rank drop on the lines or the flat planes

**Claim.** ""At Perminov's rank-23 scheme cn122 (Jacobian nullity 94 over Q, excess 24 over the trivial span), we computed the exact straight lines in the rank-23 variety through the point. Within the searched scope — all directions in two-dimensional coordinate planes of the kernel basis, plus the shear lines — there are exactly 21 ruler directions; 114 of the 153 two-planes spanned by pairs of the 18 flat basis rulers are themselves entirely flat. Along all 21 lines there is no term-zero event and no two-term proportionality event at any rational parameter: no rank drop occurs anywhere on them (42 sampled schemes on the lines were verified exactly). Extending the scan to the flat planes: no term vanishes anywhere in any of the 134 flat planes, and for all 596 tested (plane, term-pair) combinations the simultaneous proportionality ideal is the unit ideal, so no two terms merge at any point of those planes, even over ℂ. Random directions are never rulers (0 of 3,000 sampled at cn122; 0 of 3,000 at Laderman, which has no shear lines at all). Scopes: directions supported on three or more kernel basis vectors outside the flat planes are not excluded, and the plane merge scan covers the restricted pair set stated in our record.""

**Evidence.** Exact rational computation at cn122: Jacobian
nullity 94 (Laderman's 76 reproduced as control); 21 ruler
directions from the structured hunt in two-dimensional
coordinate planes of the kernel basis plus the shear lines;
114 of 153 pair-spanned two-planes fully flat; 42/42 schemes
sampled on the lines verified exactly; term-zero in none of
the 134 flat planes; for all 596 tested (plane, pair)
combinations the simultaneous 3-slot minor ideal has
Gröbner basis [1]. Full record in `data/rulers-and-gg611.md`.

**Scope.** The named lines and planes and the restricted
pair set stated in the record; directions supported on three
or more kernel basis vectors outside the flat planes are not
excluded. The Laderman leg is sampling plus pair census, not
the full structured search.

**Would overclaim:** "the rank-23 variety near cn122
contains no rank drop" unscoped; "no lines exist at
Laderman"; calling the flat-plane result a statement about
the whole variety.

## Item 22 — gg611, the unique grip-gain scheme

**Claim.** ""Exactly one point on the 21 ruler lines through cn122 strictly increases the identical-factor pair count: the t = 1 point of one shear line, with 8 pairs — cn122's seven plus a (6,15) pair in the first factor that cn122 itself does not have. That scheme (gg611) is banked and verified exactly (rank 23 over Q). Its shear family gives 96 exact variants (93 new to our bank) and 150 new 22-term wrong=1 states, from which 2,400 free-4 repair cases are derived and staged. The other three candidate points on the lines are pair swaps at count 7, not gains — we record this correction of Wave 57's preliminary reading in the same place.""

**Evidence.** The grip-gain census over all 21 ruler lines
found exactly one strict gain; the scheme is banked and was
fresh-verified exactly (rank 23 over ℚ, 0/729) — and the
shipped file `data/gg611_r23_Q.json` verifies with this
repository's `code/verify.py`. Its shear family: 96 exact
variants (93 new), 150 distinct wrong=1 states, 2,400 free-4
cases derived. Full record in `data/rulers-and-gg611.md`.

**Scope.** gg611 is a rank-23 scheme on a known line through
a literature scheme, not a new kind of scheme. The 2,400
cases are staged, not decided.

**Would overclaim:** calling gg611 a new kind of scheme;
implying the 2,400 cases are decided.

## Item 23 — the Hensel bridge: calibration and a native-point conversion

**Claim.** ""We built and calibrated a 3-adic (Hensel) lifting bridge from F3 decompositions to Q, in the spirit of the lifting steps used in recent flip-graph work (Khoruzhii–Gelß–Pokutta, ISSAC 2026): a non-singular F3 point of a decomposition system is Newton-lifted to Z/3⁴² and its coordinates are rationally reconstructed. Calibration: Perminov's cn122 and Laderman's scheme, reduced mod 3, lift and reconstruct **entry-identically**, and both reconstructions verify exactly over Q; the Jacobian ranks mod 3 reproduce the known over-Q nullities (94 and 76). The bridge also converts genuinely new finite-field points, not only reductions of known schemes: a solver-found F3-native rank-7 decomposition of ⟨2,2,2⟩, differing from Strassen's scheme mod 3 in 13 entries, lifts to a verified rank-7 scheme over Q that is not entry-identical to Strassen's. The bridge changes the value of our F3 searches — any future non-singular F3 rank-22 point would lift the same way — but it finds nothing by itself, and non-singularity of a hypothetical F3 point would have to be checked when one exists.""

**Evidence.** Both controls lift and reconstruct
entry-identically and verify fresh over ℚ; the mod-3
Jacobian ranks reproduce the over-ℚ nullities (94, 76). The
F3-native ⟨2,2,2⟩ rank-7 point differs from Strassen mod 3 in
13 entries; its lift verifies over ℚ and is not
entry-identical to Strassen's. Full record in
`data/hensel-bridge.md`.

**Scope.** A methods calibration. Hensel lifting of
finite-field decompositions is published prior art
(Khoruzhii–Gelß–Pokutta, ISSAC 2026; Moosbauer–Poole); the
bridge converts non-singular points only, and finds nothing
by itself.

**Would overclaim:** "we invented Hensel lifting for
decompositions"; "an F3 rank-22 scheme would give a ℚ
rank-22 scheme" without the non-singularity condition;
presenting the ⟨2,2,2⟩ scheme as new mathematics.

## Item 24 — one-signedness: the 11,777-state census and the 2,010-vs-1 sign census

**Claim.** ""Across every unit-residual near-miss state this campaign has banked, the residual is one-signed without exception: 11,777 on-support wrong=1 states (1,282 of the 22-term class and 10,495 of the 25-term class, generated by unit-term drops from verified schemes and their shear variants) have residual +E_e — a single missing entry on the tensor's support — in 11,777 of 11,777 cases. The matching sign census of unit terms themselves finds the same asymmetry: in our 53-file scheme bank and in the complete Heule–Kauers–Seidl population of 17,376 rank-23 schemes, unit terms number 2,010 positive against exactly 1 negative — and the single negative unit term is proj-24's off-support term, whose drop state is the campaign's only −E_e state, at an off-support entry, with 23 terms. No on-support −E_e state is known to us in any of this material. This is a census of the named pools, not a theorem: a rank-22 scheme, if one exists, need not arise from these pools, and the pattern's force is that a whole class of repair constructions (opposite-sign state surgery) is starved by it — the manufacturing of an on-support −E_e state is the named precondition for reviving that class.""

**Evidence.** Exact censuses of the named pools: 1,282
22-term-class states (Waves 56/58 drop pools) and 10,495
25-term-class states (Wave 67, the lensC family), residual
+E_e in 11,777/11,777; unit terms 128 positive vs 1 negative
in the 53-file bank and 1,882 positive vs 0 negative in the
complete Heule–Kauers–Seidl population — the HKS positive
tally reproducing Item 11's census count exactly. Full
record in `data/one-signedness.md`.

**Scope.** A census of the named pools, not a theorem. The
25-term class comes from a single parent family (lensC and
its variants); that composition is part of the claim.

**Would overclaim:** "unit residuals are always positive" as
a universal claim; "one-signedness theorem"; any use of the
census as evidence that rank 22 does not exist.

## Item 25 — Singer Γ39 over F3: exact non-existence

**Claim.** ""One symmetric ansatz is excluded exactly. Let Γ39 be the order-39 group generated by a Singer cycle of order 13 in GL(3,3) and the Frobenius map, acting on rank-1 tensors over F3 by simultaneous conjugation (with the transposed action on the third leg that the stored form of the multiplication tensor requires). The Γ39-fixed subspace of the tensor space has dimension 31, but every sum of whole Γ39-orbits of rank-1 tensors lands in a fixed 17-dimensional subspace of it, and the multiplication tensor is not in that subspace. Therefore no Γ39-equivariant decomposition of ⟨3,3,3⟩ into 22 terms over F3 exists, for any orbit partition. The obstruction is arithmetic, not numerical: the group order is divisible by the characteristic, and the norm map's image is too small (a modular norm gap). Parameter counting alone would not have excluded this ansatz. This is a statement about this one ansatz over F3; it is not evidence about rank 22 in general, and symmetric non-existence results for other groups over ℂ are in the literature (Burichenko).""

**Evidence.** Exact linear algebra over F3: dim Fix(Γ39) =
31; the span of all orbit sums of sizes 1, 3, 13 has
dimension 17 and excludes T; counts cross-checked by an
independent numpy path. The parameter count alone would not
have excluded the ansatz. Full record in
`data/symmetric-ansatze.md`.

**Scope.** This one ansatz (this group, this action) over
F3. Symmetric non-existence results for other groups over ℂ
are in the literature (Burichenko).

**Would overclaim:** "symmetric rank-22 schemes don't
exist"; any implication for the C13-only ansatz (Item 27 —
the norm gap does not extend to it); "first non-existence
proof for a symmetric ansatz".

## Item 26 — involution pairing: killed on paper

**Claim.** ""A second ansatz family is excluded by counting alone. If a rank-22 decomposition were invariant under an involution of the tensor's symmetry group, its terms would split into swapped pairs and fixed terms; the involution leaves 365 independent equations on the 729-entry tensor space, while every pairing pattern of 22 terms supplies at most 286 effective unknowns — short by at least 79 in all cases, over Q and over F3 alike. No involution-paired rank-22 decomposition exists. (An order-2 group halves the equations but barely compresses the terms; that asymmetry is the whole obstruction.)""

**Evidence.** The fixed space of the involution on the 729
entries has dimension 365 (direct sign count; Burnside
cross-check (729+1)/2 = 365; identical over F3). Per-partition
effective unknowns run 275–286 against 365 independent
equations — short by 79–90 in every partition 22 = 2k + f.
Full record in `data/symmetric-ansatze.md`.

**Scope.** Involution-paired decompositions, over ℚ and F3
alike. Order-2-containing groups are a separate question
(the census, Item 31, treats them separately, and some
survive its filters).

**Would overclaim:** extending the kill to all
order-2-containing groups; calling the count a theorem about
symmetric schemes in general.

## Item 27 — the C13-only Singer ansatz: feasibility verdict BUILD

**Claim.** ""The C13-only residue of the Singer idea survives the tests that killed its parent. A rank-1 tensor fixed by the order-13 Singer cycle is exactly a triple of elements of GF(27) (one per factor, in the commutant field), so the nine fixed terms of the only viable partition (one 13-orbit plus nine fixed terms) contribute 63 effective unknowns; the full system has 88 effective unknowns against 93 equations — the nearest-to-square full rank-22 ansatz we have measured. Unlike the Γ39 case (Item 11), there is no norm gap: the orbit sums alone span the whole 93-dimensional fixed space and the multiplication tensor lies in their span. We record the honest counterweight in the same place: a discrete count of the ansatz's image falls short of the equation count (log₃ 80.46 against 93), so a solution would require the tensor to be special beyond linear reachability. The system is specified in full in our record; a solver run on it is in flight and undecided at the time of this release. Nothing here is evidence that a C13-equivariant scheme exists.""

**Evidence.** The fixed rank-1 tensors are parametrised
exactly by triples of GF(27) elements (count re-derived from
the parametrisation: (27−1)³/(3−1)² = 4,394); orbit sums
span the full 93-dimensional fixed space and T lies in their
span; the system is 108 raw / 88 effective unknowns against
93 equations. The discrete counterweight (log₃ 80.46 vs 93)
is recorded in the claim itself. Full record in
`data/symmetric-ansatze.md`.

**Scope.** A feasibility study and a specification — not a
result about existence. The solver run is in flight and
undecided at the date of this release.

**Would overclaim:** "promising construction" or any
existence-flavoured phrasing; quoting margin −5 without the
discrete shortfall 12.54; implying the launched run has
produced a verdict.

## Item 28 — the lensC pipeline: 612 variants, 10,495 states, 167,920 cases staged

**Claim.** ""Our own rank-26 scheme lensC carries 51 identical-factor pairs, the most of any scheme in our bank. Its full shear family — 612 variants, every one exact-verified and new — yields 10,495 distinct 25-term wrong=1 states by unit-term drops, all of the standard flavour (these are the 25-term half of the Item 10 census). From them we derived 10,495 free-4 repair instances (167,920 cases). The scope matters: a repair of one of these states would be an exact rank-**25** scheme — the first rung of the ladder down from 26 — not a rank-22 candidate. A 1,792-case selection has been built into a solver kernel; the family is staged, not decided.""

**Evidence.** The parent passed the C0 gate (fresh
`verify.py` VERIFIED, exact rank 26, 0/729) before anything
was counted on it; the pair census reproduced 51; all 612
shear variants exact, distinct and new (408/612 with entries
outside {0,±1}); 10,495 distinct 25-term wrong=1 states, all
standard flavour; instances derived with the generalised
driver (regression-verified identical on a decided instance
first). Full record in `data/lensc-pipeline.md`.

**Scope.** A repair of one of these states assembles an
exact rank-25 scheme — the ladder's first rung — not a
rank-22 candidate. The family is staged, not decided.

**Would overclaim:** any wording letting a reader take the
lensC instances as rank-22 searches; the inflated figures
(1,326 variants / 11,901 states / 226,119 cases) that
appeared in one internal handoff and are not the record;
"richest scheme" without "in our bank".

## Item 29 — the border line: conversion equivalence and the ALS calibration anatomy

**Claim.** ""Three border-rank statements, all scoped. (1) The often-imagined shortcut does not exist: requiring a 21-term Laurent family to satisfy the tensor identity to *all* orders is exactly the statement R ≤ 21, and the 22-term version is exactly R ≤ 22; a single extra term can push the first defect one order higher only when that defect is itself rank 1, and killing all defects is the original problem. The border-plus-one route is equivalent in difficulty to exact rank. (2) Border rank 21 for ⟨3,3,3⟩ is proved in the literature only through Schönhage's asymptotic sum inequality — the saving lives in the limit over direct sums and tensor powers; no explicit 21-term Laurent family for the single tensor appears in any source we could access, and an earlier version of our own strategy document claimed otherwise and has been corrected. (3) Our numerical route to a border family failed its calibration, and we measured why: on Bini's border-10 family for ⟨3,2,2⟩ the search does show the genuine border signature (residual falling as a power law in the factor norms, exponent 3.58 against a predicted 3), and high-precision polishing drives the defect to 1.6e-76 — but the point it converges to is a *generic* point of a solution component with 106 genuine moduli (Jacobian nullity 126, of which only 20 are gauge), so its coordinates admit no low-degree algebraic description for exact reconstruction to find. The failure is genericity, not precision. The border line is parked, with three named revivals in our record (pattern-constrained solves, homotopy from Bini's rational point, α-theory certification).""

**Evidence.** The equivalence is proved in the record
(order-by-order analysis of the Laurent identity; the
defect-push requires the first defect to be rank 1). The
literature finding rests on the sources searched
(Schönhage's bound via the asymptotic sum inequality; no
explicit single-tensor family found). The anatomy is
measured: Bini calibration — judge leg PASS, the border
signature observed (α = 3.58, R² = 0.991), extraction FAIL;
Gauss–Newton polish to defect 1.64e-76; Jacobian rank
194/288, nullity 126 = 20 gauge + 106 genuine moduli; PSLQ
reconstruction failing with the generic signature. Full
record in `data/border-line.md`.

**Scope.** A negative-results / anatomy item, grouped under
negative results, never under constructions. The α = 3.58
fit is a calibration observation on ⟨3,2,2⟩, not a discovery
about ⟨3,3,3⟩.

**Would overclaim:** "border rank 21 is unproven" (it is
proven, by the asymptotic argument; what does not exist in
print is the explicit family); "we almost reconstructed a
border family" (no ALS-derived candidate ever passed the
exact pre-screen, so none was judged).

## Item 30 — the wrong=5 state over F3 and its closed neighbourhood

**Claim.** ""Over F3, the closest near-miss our searches have produced is a 22-term state with exactly 5 wrong entries of 729 (GPU grammar annealing, 3.68×10¹² aggregate steps; harvested and re-judged exactly at home). All five defects are missing entries on the tensor's support — the one-signed flavour of Item 10. The state's local neighbourhood is now closed exactly, in three senses. (i) Weights: over all 3²² coefficient assignments the minimum wrong count is 5 — the annealer's weights were already optimal for its term shapes. (ii) Shapes: freeing the factors inside the state's own support template gives an unsatisfiable system, for an exact reason — the five defect entries are precisely the support entries no monomial of the template can reach; widening the supports by all cyclic shifts still leaves the entry (1,3,0) unreachable. (iii) Swaps: replacing any one term by any menu shape that covers (1,3,0) (136 such shapes; 35 swaps keep every support entry reachable) gives 35 systems, all unsatisfiable. So no single-term perturbation of this state is an F3 rank-22 scheme. This is a statement about one state's neighbourhood over F3; two-term swaps and swaps on widened supports are explicitly not covered, and nothing here is evidence about rank 22 over Q.""

**Evidence.** The state is shipped as `data/wrong5-state.json`
(sha256 2883c3c2…31c) and re-judged by the packaged
`code/checkp.py`: wrong = 5/729, defects exactly (1,3,0),
(3,2,5), (4,4,4), (6,0,6), (7,5,8), all got-0/want-1. The
three closures: the exact linear minimum over coefficient
assignments is 5 (729×22 system, rank 22, inconsistent;
feasibility UNSAT at budgets 1–4); the own-support template
(74 unknowns) is UNSAT for the stated reachability reason,
as are the widened templates (144 and 213 unknowns); the 35
reachability-passing swap systems are 35/35 UNSAT with
planted controls 2/2 PASS. Full record in
`data/wrong5-case-study.md`.

**Scope.** One state's neighbourhood over F3. Two-term swaps
and swaps on widened supports are explicitly not covered;
nothing here is evidence about rank 22 over ℚ.

**Would overclaim:** "closest known F3 near-miss" (no
literature category supports "known" — the claim says
"closest our searches have produced"); "the F3 floor is 5"
(an annealing-floor observation, not a bound, and not gated
here).

## Item 31 — the symmetry census over F3: three survivors, D13/Q12 not realisable

**Claim.** ""We censused the group actions that could organise a rank-22 decomposition over F3, passing each through two exact filters — a parameter count (unknowns vs independent equations, per orbit partition of 22) and a reachability test (the tensor must lie in the span of the group's orbit sums; this is the test that kills ansätze whose group order is divisible by 3). Of the conjugation-type actions in GL(3,3) and the translation family, exactly three survive both filters, and we publish their specifications: the octahedral group S4 acting by conjugation (31 independent equations; best partition short by 3 effective unknowns, and by 2.26 in the discrete count — the closest-to-balanced symmetric ansatz we have measured); a translation action of C3×C3 (type P1) whose best partition has 9 *more* effective unknowns than equations, the only positive-margin symmetric instance we have found; and a second translation type (P2) short by 1. Two candidate groups cannot act at all: exhaustive search over all 11,232 elements of GL(3,3) shows no element inverts the Singer cycle (so the dihedral group D13 is not realisable over F3), and no element satisfies the dicyclic relations (Q12 likewise). Two further candidates (A4; permutation S3×C2) survive only under a raw parameter count and are excluded under the effective count, which we argue is the correct convention for their action type; both counts are in our record. The census does not cover mixed conjugation × leg-permutation actions beyond the previously studied S3, and a survivor is a specification for a solver system, not evidence that a scheme exists — the S4 and translation systems are being built; the S3 and C13 systems (Items 13 and the Wave 60 design) are already in flight. Symmetric-exclusion results for other groups over ℂ are in the literature (Burichenko).""

**Evidence.** The census pipeline was validated by
reproducing the earlier waves' numbers exactly (the Γ39
kill, the involution count, the C13 counts). S4: 31
equations, 76/103 partitions passing both filters, best
margin −3 effective, best discrete shortfall 2.26.
Translation P1: margin +9 effective, shortfall 5.46; P2: −1
effective, shortfall 6.51. D13: exhaustive over all 11,232
elements of GL(3,3) — the Singer normaliser (order 78)
achieves conjugation powers exactly {1,3,9}, zero elements
invert the Singer cycle, all 144 C13 subgroups conjugate.
Q12: all 2,600 order-6 elements tested against the Sylvester
condition. A4 and permutation S3×C2 pass F1 only under the
raw count and are killed under the effective count, with
both counts preserved in the record. Full record in
`data/symmetry-census.md`.

**Scope.** The census covers conjugation-isotropy actions,
the translation family, and the previously studied
leg-permuting S3; mixed conjugation × leg-permutation
actions beyond that S3 are not covered. A survivor is a
specification, not existence evidence.

**Would overclaim:** "complete census of symmetry groups";
"C3×C2" anywhere (the group is C3×C3); presenting a
survivor's margin as existence evidence; "first symmetry
census".

## Item 32 — the substitution machine: a validated instrument with below-literature bounds

**Claim.** ""We implemented the substitution method for tensor-rank lower bounds in the automated form of Wang (2026) and validated the instrument end-to-end: on ⟨2,2,2⟩ it reproduces Wang's 10 restriction orbits, certifies rank ≥ 7 over both F2 and F3, and its backtracking search then *completes* at target 8 with a negative — the sound answer, since the exact rank is 7. Run on ⟨3,3,3⟩, our implementation certifies rank ≥ 14 over F2 and ≥ 12 over F3. These bounds are **weaker than the published ones** — 19 over any field (Bläser 2003) and at least 21 over F2 (Wang; Yang et al., 2026) — and we publish them only as the instrument's measured reach, with the stall anatomy: our canonicalisation used the monomial subgroup, the restriction lattice grew to 3,389 orbits by dimension 3 (Wang's full-group treatment needs 496 in total), and the budget died before the strong leaves could fire. Closing the gap is a compiled full-group reimplementation, whose specification is in our record. The value of the item is a working, control-validated lower-bound machine whose certificates are checkable line by line — not a bound.""

**Evidence.** Controls over both fields: ⟨2,2,2⟩ yields
exactly 10 restriction orbits (Wang's count), certifies
rank ≥ 7 over F2 (1.8 s) and F3 (88 s), and backtracking
completes negatively at target 8 — the sound answer, the
exact rank being 7. On ⟨3,3,3⟩ the certified bounds are ≥ 14
over F2 (a dimension-2 restriction raised 9 → 14 by the
substitution bootstrap, target 15 completed not-provable;
242 states carry bounds ≥ 12) and ≥ 12 over F3 (targeted
certificate; the full F3 lattice run timed out on
canonicalisation cost). Stall anatomy: monomial-subgroup
canonicalisation grew the lattice to 3,389 orbits by
dimension 3 against Wang's 496 in total, so the
Hopcroft–Kerr leaves never fired. Full record in
`data/substitution-machine.md`.

**Scope.** A validation/methods item. The published bounds
are strictly stronger: 19 over any field (Bläser 2003),
at least 21 over F2 (Wang; Yang et al., 2026).

**Would overclaim:** "we prove rank ≥ 14 / ≥ 12" as a
headline without the below-literature sentence in the same
paragraph; citing the 2026 F2 endgame (22; = 23) inside this
item (it is stated, as others' work, in the release notes'
literature section); implying the F3 number is the best
known over F3 (Bläser's 19 holds over F3 too).

## Item 33 — the learned near-partition pattern (labelled speculative bet)

**Claim.** ""Support shapes carry a learnable signature of near-exactness. On a corpus of 7,255 support templates (drop-one supports of our banked exact rank-23 schemes as positives-by-proxy; random menu subsets and fake-scheme drops as negatives), a random forest separates the classes perfectly on a scheme-held-out split (AUC 1.0000), where a reachability-only baseline is at chance (0.5320). The signature: near-exact shapes are sparse near-partitions of the target — about 91% of the entries that must be hit are covered exactly once, overlap between terms is minimal, and almost no coverage is wasted on entries that must stay zero; symmetry/orbit features carry no signal. We state the limit in the same place: the signature is necessary-looking, not sufficient. The model's ten best-scoring new proposals, all passing full reachability, were exact-tested — all ten are provably empty. The pattern's use is as a pre-filter for future template enumerations; it is not a construction, and the positives are proxies (supports of rank-23 schemes minus a term), since no exact rank-22 template exists to train on.""

**Evidence.** Corpus of 7,255 templates, 35 exact features
each; group-split holdout by scheme (1,779 rows): random
forest AUC 1.0000 against the reachability-only baseline's
0.5320, passing the pre-registered +0.02 rule. Pattern
numbers: nnz/triple 7.0 vs 12.0; 91% of support entries
covered exactly once (negatives 21%); zero-entry mean
coverage 0.37 vs 2.20; overlap mean 1.83 vs 5.36; symmetry
features at importances ≤ 0.00014. Exact tests: 12,000
mutants → 1,279 reachability-passing → top 10 by score →
10/10 UNSAT over F3 (0.7–16.6 s). Full record in
`data/near-partition-pattern.md`.

**Scope.** A pattern statement about this corpus. The
positives are proxies (supports of rank-23 schemes minus a
term), since no exact rank-22 template exists to train on;
part of the separation rides on sparsity, as recorded in the
data file.

**Would overclaim:** "machine learning finds rank-22
candidates" (it found none — 10/10 UNSAT is part of the
claim); quoting AUC 1.0000 without the corpus definition and
the proxy caveat; "near-partition" as a property of all
exact schemes.

## Item 34 — GPU evaluator benchmark

**Claim.** ""Our F3 annealing evaluator, ported to an RTX 4070 laptop GPU (CuPy), sustains 172.9 million steps per second on the rank-22-over-F3 annealing workload — about 25× the same machine's compiled CPU annealer and about 1,800× this project's VM CPU baseline. Before any campaign run, the GPU evaluator's wrong-counts were checked against the exact home evaluator on a 16-state battery (16/16 agreement, the home evaluator itself cross-checked against the exact mod-3 judge), and full- assembly recount audits ran clean over ~65 billion cumulative steps. All exact verification remained on CPU throughout: the GPU proposes states; only the exact layer judges them.""

**Evidence.** RTX 4070 Laptop GPU (CuPy): 172.9M steps/s
(32.30B steps / 186.8 s); laptop CPU (gcc -O2) 6.90M steps/s;
VM CPU ~96k steps/s — ratios ≈25.1× and ≈1,800×, both
clearing the pre-registered ≥10× porting rule. The GPU
evaluator agreed with the exact home evaluator on a 16-state
battery (16/16; the home evaluator itself cross-checked
against `checkp.py`), and full-assembly recount audits ran
clean over ~65 billion cumulative steps. Full record in
`data/gpu-benchmark.md`.

**Scope.** A benchmark of this evaluator on this workload
and hardware. All exact verification remained on CPU.

**Would overclaim:** "1,800× speedup" without naming both
baselines (the honest same-machine figure is 25.1×); any
implication that GPU throughput bears on the exact searches'
decidability.

## Standing scope rules for everything above

- Every UNSAT comes from an encoding validated by a control (the
  same terms freed on a known-good scheme returns SAT and the
  candidate verifies exactly). Timeouts are recorded as
  "no conclusion" and appear in no claim.
- Every field is named: a statement over {0,±1}, quarter-integers,
  F₂, or ℚ says nothing about the others.
