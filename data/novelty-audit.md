# NOVELTY AUDIT — matmul-pilot campaign, three candidate-original items

**Date:** 2026-11-22. **Scope:** literature research only. No solver runs, no
recomputation; every campaign number below is taken from the campaign's own
records (CHECKPOINT.md, REPORT.md incl. the Waves 2–9 addendum, wave REPORT.md
files, wave17/research/RESEARCH.md) and was **not** independently re-verified
by this audit. What this audit verifies is only the *literature position*.

**Verdict categories (fixed in advance):**
- **(i) EXPLICITLY PUBLISHED** — the same result/method appears in a cited source.
- **(ii) KNOWN-EQUIVALENT / IMPLICIT** — a published result implies or
  substantially contains it; the implication is explained.
- **(iii) NOT FOUND in the sources searched** — every source searched is
  listed. Category (iii) is **not** proof of novelty and must never be worded
  as such.

**Citation correction (applies to the campaign's own notes):** the flip-graph
paper of Kauers–Moosbauer is **arXiv:2212.01175** ("Flip Graphs for Matrix
Multiplication", ISSAC 2023). The identifier **arXiv:2210.04045**, cited for
flip graphs in the audit brief and in RESEARCH.md, is a different
Kauers–Moosbauer paper (the FBHHRBNRSSSHK 5×5-over-Z₂ result). Any public
note must use 2212.01175 for flip-graph claims.

---

## ITEM 1 — The covering-parity case split

### The campaign's claim, stated precisely

Let S be a rank-23 scheme for ⟨3,3,3⟩ over Q with coefficients in {0,±1}, and
let S⁻ be S with one term deleted, so S⁻ differs from the ⟨3,3,3⟩ tensor in
exactly one entry e (a "wrong=1 state"). A *repair instance* is: choose k terms
of S⁻, erase their coefficients, and ask whether the freed terms can be
rewritten over a stated coefficient set (e.g. {0,±1}, halves, quarters) so
that the full tensor is again correct. The campaign's method splits such an
instance into disjoint, exhaustive cases indexed by (a) **which of the freed
terms cover e** — i.e. have a nonzero factor product at entry e — and (b) the
**sign pattern** of those products at e. The split is forced by the
wrong-entry equation alone: the freed terms' products at e must sum to the
residual at e, which (over {0,±1}) requires an odd number of covering terms
with a determined sign balance. Each case is then an independent SAT/SMT
instance with the rest of the scheme frozen. Empirically (Wave 6): the free-4
instance {2,3,4,8} on Laderman's wrong=1 state was decided UNSAT in 16 cases
totalling ~26 solver-minutes, where the unsplit instance was still undecided
after 600 s and 1800 s of raw solving. The method was generalised across
Waves 7–15 (`wave7/parity/paritysplit.py`, `wave8/fractions/fracsplit.py`,
`wave13/split/crosssplit.py`, `wave15/five/fivesplit.py`), including a
213-case split for a halves free-4 instance and a derived 45-case split for a
free-5 instance.

### Verdict

**Composite.** The *problem framework* is **(ii) KNOWN-EQUIVALENT /
IMPLICIT**; the *specific split* is **(iii) NOT FOUND in the sources
searched**.

- Term-freeing with the rest of a known scheme frozen is published:
  Heule–Kauers–Seidl's "streamlining" restriction 2 instantiates ~50% of the
  variables of the Brent system with values from a known solution and solves
  for the rest, explicitly noting that solvers then find genuinely different
  schemes with partial overlap (arXiv:1905.10192, §3). Courtois–Bard–Hulme's
  SAT attack (arXiv:1108.2830) likewise works with partially fixed Brent
  systems. So "freeze most of a scheme, re-solve a freed part" is not new.
- Parity reasoning about Brent sums is also published, inside the encoding
  itself: Heule–Kauers–Seidl contrast the faithful "even" (parity) encoding of
  each Brent sum with a stricter "zero-or-two" predicate (arXiv:1905.10192,
  §3). That is parity at the level of clause encoding, not a case split.
- Exhaustive case decomposition as a SAT paradigm is published in general:
  cube-and-conquer (Heule–Kullmann–Marek, SAT 2016,
  doi:10.1007/978-3-319-40970-2_15) splits a formula into cubes solved
  independently. But cube-and-conquer splits on *variables chosen by
  lookahead heuristics*; no application of it to Brent equations or
  term-freeing was found, and the campaign's split is not a variable split —
  it is a *semantic* split derived from a single tensor entry's equation.
- The specific decomposition — cases keyed to the unique wrong entry of a
  wrong=1 state, by covering subset and sign pattern of the freed terms'
  products at that entry, used as an exhaustive SMT/SAT **decision**
  procedure (proving UNSAT of repair instances, not searching for solutions)
  — was **not found** in any source searched. The closest published
  neighbours all use partial fixing as a *search* heuristic with local-search
  solvers and discard hard instances after minutes (Heule–Kauers–Seidl §3);
  none states a covering/sign case analysis of a distinguished wrong entry,
  and none proves repair instances unsatisfiable.

### Sources searched for Item 1

Heule–Kauers–Seidl, arXiv:1905.10192 (J. Symb. Comput. 104, 2021) — read in
full; Heule–Kauers–Seidl, arXiv:1903.11391 (ISSAC 2019) — abstract and
introduction read (the 2021 journal version above is its extension and was
read in full); Courtois–Bard–Hulme, arXiv:1108.2830 — read in part (method
sections: SAT portfolio, partial fixing, mod-2 solutions lifted mod 4 and to
general rings); Kauers–Moosbauer, arXiv:2212.01175 — read in full;
Moosbauer–Poole, arXiv:2502.04514 (ISSAC 2025, doi:10.1145/3747199.3747566) —
read in full; Perminov, arXiv:2512.21980 — read in full; Heule–Kullmann–Marek
cube-and-conquer (SAT 2016) and overviews — read via the authors' published
slides/summaries; Palladinos, arXiv:2607.29291 (CDCL re-examination of the
Heule–Kauers–Seidl F₂ benchmark instances; an encoding-subtlety caution, not
a case-split method) — as recorded in the campaign's RESEARCH.md and the
auditor's earlier reading; Yang, arXiv:2502.12390 (an exact finite-field
decision procedure — an alternative decision method, not a covering split) —
as recorded in RESEARCH.md, **not re-read in full for this audit**.

---

## ITEM 2 — The rigidity facts

### 2(a) Drop-2/complete-1 impossible over all of Q for Laderman λ=1, λ=2 and Perminov cn122

**Campaign's claim.** For each of the three named rank-23 schemes, every one
of the C(23,2) = 253 pairs of terms was tested exactly: the pair's sum never
has tensor rank ≤ 1 over Q (759 pair tests in total), so no two terms of any
of these schemes can be merged into one — no rank-22 scheme arises from any
of them by a 2-to-1 merge.

**Verdict: (ii) KNOWN-EQUIVALENT / IMPLICIT for the test and, with a caveat,
for Laderman; (iii) NOT FOUND as an explicitly stated result for Perminov
cn122.**

- The merge test itself is published, twice. Heule–Kauers–Seidl, §8:
  "We have checked all schemes whether some of their summands can be merged
  together using tensor product arithmetic," with the criterion that summands
  sharing a factor (with the other factors linearly dependent) can be merged,
  concluding "Since none of our schemes admits a simplification of this kind,
  it remains open whether a scheme with 22 multiplications exists"
  (arXiv:1905.10192). Kauers–Moosbauer's Definition 2 ("reducible": a subset
  of terms with one factor family spanning a 1-dimensional space and another
  factor family linearly dependent) with Proposition 3 (reducible ⇒ a
  rank-(r−1) scheme exists) is the same notion generalised to subsets
  (arXiv:2212.01175). For a *pair* of terms the published criterion and the
  campaign's exact rank-1 residual test coincide in power: rank(tᵢ+tⱼ) ≤ 1
  forces the two terms to be proportional in at least two of the three
  modes, which is exactly the shared-factor situation — up to proportionality
  and sign conventions in the representatives, which this audit could not
  verify in Heule–Kauers–Seidl's implementation (**UNVERIFIED** detail).
- For Laderman λ=1: Heule–Kauers–Seidl certainly had Laderman's scheme in
  hand (their §7 discusses it by name), and §8 says "all schemes" — but in
  context that phrase most plausibly refers to the 13,000+ schemes of their
  own collection, and the passages read do not state explicitly that
  Laderman itself was run through the merge check. Coverage of Laderman by
  §8 is therefore **UNVERIFIED**, and the honest verdict for Laderman is
  (ii) with that caveat, not (i). Laderman λ=2 adds nothing: the λ-family
  shares one sparsity skeleton and λ only rescales coefficients, so the
  λ=2 statement follows from λ=1 by equivalence (campaign's own Wave 5
  finding, consistent with Sedoglavic's λ-parametrisation).
- For Perminov cn122 (December 2025): it postdates both merge-check papers
  and cannot be covered by them. Perminov's own paper (arXiv:2512.21980)
  reports no pair-merge test of cn122 — its objective was additive
  complexity (58 additions), reached by a ternary flip-graph walk. The one
  follow-up found, Sidebottom arXiv:2610.27451 (2026; seen via search-result
  text, **not read in full — UNVERIFIED** beyond its abstract-level
  description), applies exact minimisation to cn122 to reach 55 additions
  and mentions an orbit-wide computation over the Heule–Kauers–Seidl
  database — again about additions, not rank collapse. So the explicit
  statement "no pair of cn122's terms merges over Q" is **(iii) NOT FOUND**.

### 2(b) Perminov's flip component has no collapsible pair; ~133M triple tests find no 3-to-2 collapse

**Campaign's claim.** (1) Laderman's scheme admits no flip and no two-term
rewrite (Wave 6). (2) An exhaustive exploration of the flip-graph component
of Perminov's cn122 over {0,±1} visited 34,604 distinct rank-23 states
(100,459 steps); all 25.4M term pairs across those states were tested and
none is collapsible (best proximity: one pair with a single nonzero 2×2
minor, cn122's own pair (13,18)). (3) At every visited state, all
C(23,3) = 1,771 triples were run through a rank-≤2 flattening filter —
~133M triple tests over ~75k distinct rank-23 states — with zero passes;
the machinery was validated end-to-end on a planted rank-2 triple (detected,
decomposed, CLI-verified).

**Verdict: mixed — part (i), part (iii), with a published partial analogue.**

- Claim (1) is **(i) EXPLICITLY PUBLISHED**. Kauers–Moosbauer, §4, on the
  rank-≤23 flip graph over Z₂: "There are also components consisting of a
  single vertex. Laderman's scheme is such an example" (arXiv:2212.01175).
  Because a {0,±1} flip or pair-merge of Laderman would reduce mod 2 to a
  Z₂ flip/reduction, the published Z₂ isolation implies the campaign's
  {0,±1} statement. The campaign's Wave 6 phrasing of Laderman's isolation
  as a campaign finding must be demoted to a rediscovery/confirmation of
  Kauers–Moosbauer's published result.
- Claims (2) and (3) are **(iii) NOT FOUND**, with this partial overlap,
  stated exactly: Kauers–Moosbauer did determine entire connected components
  of the Z₂ rank-≤23 flip graph for the schemes their random walks reached
  from the standard algorithm — 584 components, 64,061 vertices in total —
  and their Algorithm 1 tests visited vertices (and one neighbour) for
  reducibility during walks. That is a published census at comparable scale,
  but it differs from the campaign's in every particular: different field
  (Z₂, not {0,±1} over Q), different component (reached from the standard
  algorithm in 2022; cn122 did not exist), reducibility checked
  opportunistically along walks rather than as an exhaustive pair census of
  one named component, and no triple test of any kind. Perminov's paper
  reports no component exploration of cn122 at all (a single ~30-minute
  addition-driven walk from the naive scheme). Moosbauer–Poole
  (arXiv:2502.04514) explores *symmetric* flip graphs for n = 5, 6 and only
  matches the bound 23 for n = 3; no ⟨3,3,3⟩ census.
- The campaign's triple filter is also strictly more general than the
  published reducibility notion: a rank-≤2 triple need not share a factor,
  so Definition 2 of Kauers–Moosbauer does not cover it even in principle
  for |I| = 3. No published 3-to-2 flattening sweep over rank-23 ⟨3,3,3⟩
  states was found.

### 2(c) Fully decided free-4 repair instances in {0,±1} on wrong=1 states

**Campaign's claim.** Five repair instances were decided completely, each
16/16 covering-parity cases UNSAT: Laderman free-4 {2,3,4,8} (Wave 6) and
{2,3,4,9} (Wave 7); Perminov minus-6 free-4 {14,3,2,21} (Wave 8), minus-13
free-4 {3,11,13,17} (Wave 11), minus-18 free-4 {1,8,11,13} (Wave 14) — so
each of Perminov's three wrong=1 states, and two Laderman neighbourhoods,
provably admit no repair within the freed terms over {0,±1} with the rest of
the scheme frozen.

**Verdict: (iii) NOT FOUND.** The underlying completion problem is published
as a *search* problem (Heule–Kauers–Seidl streamlining, §3; Kauers–Moosbauer
pose the adjacent open Question 5, whether reduction edges reachable from a
scheme can be found systematically), but no published source states or
proves the unsatisfiability of any specific frozen-rest repair instance for
a Laderman or Perminov wrong=1 state, over {0,±1} or any other coefficient
set. The Sedoglavic catalogue (fmm.univ-lille.fr) was checked directly: its
⟨3×3×3:23⟩ entry lists Laderman's scheme only, with stabilizer
(C₂×C₂)⋊S₃ and a commentary on scalar-operation counts (≥62, no better
variant in its orbits) — no reducibility, merge, or repair content.
Burichenko's automorphism work (arXiv:1508.01110: Aut(Laderman) ≅ S₄;
arXiv:2211.03404: no S₄×S₃-invariant scheme of length ≤ 23;
arXiv:2211.06485: automorphism constraints on any length ≤ 22 scheme)
concerns symmetry groups, not term repair, and contains no equivalent of
these instances.

### 2(d) The quarters free-3 {2,3,4} exclusion at 121/174 cases

**Campaign's claim.** For Laderman's wrong=1 state with terms {2,3,4} freed
over coefficients with denominators ≤ 4 ("quarters"), the derived exhaustive
split has 174 cases; 121 are decided, **all UNSAT**, covering 23 of 33 sign
patterns in full; 53 cases remain open (Wave 15 tally). This is a *partial*
exclusion and must always be worded as one.

**Verdict: (iii) NOT FOUND.** No published source addresses bounded-denominator
repair of a ⟨3,3,3⟩ wrong=1 state at all. (Published lifting work —
Courtois–Bard–Hulme's mod-2 → mod-4 lifting; Moosbauer–Poole's F₂ → ℤ
lifting via symmetry; the Hensel-lifting line recorded in RESEARCH.md —
goes in the opposite direction: it *constructs* lifts of found solutions
rather than excluding bounded-denominator repairs.)

### Sources searched for Item 2

All Item 1 sources, plus: Burichenko arXiv:1508.01110, arXiv:2211.03404,
arXiv:2211.06485 (passages on automorphism groups and symmetric-scheme
bounds); Sedoglavic's catalogue fmm.univ-lille.fr — front table and the
⟨3×3×3:23⟩ detail page read directly; Sidebottom arXiv:2610.27451 — search
excerpts only (**not read in full**); Perminov arXiv:2512.21980 read in full
(ternary flip-graph walk from the naive rank-27 scheme, plus operator,
~30 minutes on a laptop; objective 58 additions / 81 total scalar
operations; no component census, no pair or triple collapse test).

---

## ITEM 3 — The nullity diagnosis

### The campaign's claim, stated precisely

Wave 3 measured the Jacobian of the CP (Brent) map at the generic real
floating-point rank-23 solutions that ALS reliably produces (Wave 2: real
rank-23 at loss ≈ 2.8e-7): its nullity is **exactly 2r = 46** (r = 23; the
map has 621 unknowns and 729 equations). A nullity of 46 is precisely the
dimension of the per-term scaling torus (each term contributes 3 scalings
minus 1 constraint). The campaign concluded: at such points the local
solution fibre is *only* the scaling torus, so quantisation attraction
starting from generic numerical solutions is structurally stuck — there is
no local direction to slide along toward rational points — and rational
rank-23 decompositions must lie on special components of the solution
variety, not on the locus the generic numerical points sample. Caveat the
campaign's own records support: the measured points are numerical
*near*-solutions (residual ~1e-7), not exact ones, so the statement is about
the local geometry at/near those points.

### What is published

- **Heule–Kauers–Seidl (arXiv:1905.10192, §7):** the Brent solution set
  "has at least dimension 17 as an algebraic variety." Their construction:
  starting from a *specific known scheme*, free one whole factor-group of
  one term plus the complementary group elsewhere, turning the Brent system
  linear; positive-dimensional solution spaces give explicit parametrized
  families (the appendix exhibits a 17-parameter family, coefficients
  polynomial in the parameters, valid over arbitrary rings; Gröbner-checked
  independence). Parameter counts obtained for the classical schemes:
  **Laderman 0**, Courtois et al. 6, Oh et al. 10, Smirnov 14. An earlier
  3-parameter family is Johnson–McLoughlin 1986 (doi:10.1137/0215043).
- **Generic identifiability (background only):** for a *generic* tensor of
  format 9×9×9, decompositions of subgeneric rank r < 729/25 ≈ 29.2 are
  unique up to permutation and scaling (Chiantini–Ottaviani–Vannieuwenhoven
  and Bocci–Chiantini–Ottaviani; e.g. doi:10.1137/140970276). This concerns
  generic tensors. The matrix-multiplication tensor is maximally
  non-generic in this respect — Heule–Kauers–Seidl found 13,000+ mutually
  *inequivalent* rank-23 decompositions of it — so generic identifiability
  says nothing, globally, about the ⟨3,3,3⟩ decomposition set.
- **Berger–Absil–De Lathauwer–Jungers–Van Barel (J. Comput. Appl. Math.
  406 (2022) 113941, doi:10.1016/j.cam.2021.113941):** an algorithm to
  decide equivalence of polyadic decompositions of matmul tensors under the
  invariance group; applied to several formats, finding that two
  decompositions are very likely essentially different; plus a necessary
  criterion for a decomposition to be equivalent to one with integer
  entries. Adjacent to the campaign's quantisation question, but it
  computes no Jacobian, no nullity, and no local dimension at any point.

### Reconciliation — the two statements sit beside each other; neither contains or contradicts the other

The Brent rank-23 solution variety is **reducible and stratified: its local
dimension depends on the point**, and the published ≥17 family and the
campaign's nullity-46 measurement concern *different points*.

1. Heule–Kauers–Seidl's 17 parameters are witnessed by an explicit family
   through *their own SAT-found schemes* (and, with fewer parameters,
   through Smirnov's, Oh's, Courtois's schemes). Their numbers are
   dimensions of *slices*: their procedure freezes almost all coordinates
   at the base scheme's values and frees a structured subset, so it detects
   only deformations moving the freed coordinates exactly. It is a lower
   bound machine for the variety's dimension, not a local-dimension
   computation at a point — which is why "0 parameters for Laderman" does
   not mean Laderman is locally isolated (see point 2), and why the ≥17
   figure is not a claim about generic points.
2. At Laderman specifically, the local dimension is in fact large: the
   isotropy group of the ⟨3,3,3⟩ tensor, GL₃³ ⋊ S₃ (de Groote), has
   dimension 27 and acts on decompositions; Laderman's stabilizer is
   finite (Burichenko: Aut(Laderman) ≅ S₄, arXiv:1508.01110), so a
   27-dimensional orbit of distinct decompositions passes through
   Laderman, in addition to the 46 gauge directions (the two overlap at
   least in the 2-dimensional uniform-scaling subgroup; the exact
   tangent-space intersection was not re-derived in this audit —
   **UNVERIFIED** as an exact count, but the qualitative conclusion, local
   dimension at Laderman strictly above 46, is robust). The classical
   schemes live on high-dimensional loci.
3. The campaign's ALS points are different points: unstructured numerical
   near-solutions, not equivalent to any classical scheme and not on the
   published families. Nullity exactly 46 there says the variety is
   (near-)smooth of the minimal possible dimension at those points — the
   fibre is the gauge orbit and nothing else. A reducible variety can, and
   here apparently does, have both kinds of loci. So: the ≥17-dimensional
   manifold and the nullity-2r measurement **do not contradict** each
   other; they describe different strata. The campaign's inference — that
   quantisation attraction from generic starts has no local room to move,
   and rational points must be sought on special components — is
   *consistent with* the published picture (every published rational
   rank-23 scheme is highly structured: Laderman, the SAT-found families,
   Smirnov's parametrized schemes), but the nullity-46 measurement itself,
   and its use as a diagnosis of numerical quantisation, were **not found**
   in any published source.

### Verdict

**(iii) NOT FOUND** for the measurement and the diagnosis as stated — no
published Jacobian-nullity or local-dimension computation at rank-23
⟨3,3,3⟩ points was found, and no published statement that numerical
rank-23 solutions are isolated modulo scaling. The surrounding published
facts (variety dimension ≥ 17 via explicit families at special points;
generic-tensor identifiability, inapplicable globally to this tensor) are
**(ii)** — they frame, and are consistent with, the campaign's claim, but
they do not imply it: local dimension at the ALS points cannot be deduced
from the dimension of a family through other points.

### Sources searched for Item 3

Heule–Kauers–Seidl arXiv:1905.10192 (§7 and appendix, read in full);
Johnson–McLoughlin 1986 (as cited and discussed in Heule–Kauers–Seidl);
Chiantini–Ottaviani–Vannieuwenhoven, SIAM J. Matrix Anal. Appl.
(doi:10.1137/140970276) and the Bocci–Chiantini–Ottaviani line — abstracts
and statements read via search results and secondary presentations
(Vannieuwenhoven's published slides on conditioning of tensor rank
decompositions); Berger et al. 2022 (doi:10.1016/j.cam.2021.113941) —
abstract and introduction read; Burichenko arXiv:1508.01110 (automorphism
groups); Moosbauer–Poole arXiv:2502.04514 §2 (de Groote's isotropy group);
Kauers–Moosbauer arXiv:2212.01175 (normal forms / equivalence background);
plus targeted web searches on CP Jacobian nullity, rigid/isolated tensor
decompositions, and identifiability at this format, which returned only
the generic-tensor literature above.

---

## What may be claimed, and in what words

### Item 1 — covering-parity case split

- **Strongest honest wording:** "We decide term-repair instances for
  rank-23 ⟨3,3,3⟩ schemes by an exhaustive case split derived from the
  state's single wrong entry — cases indexed by which freed terms cover
  that entry and the sign pattern of their products there — reducing each
  instance to independent SAT/SMT sub-instances. Term-freeing with a frozen
  remainder follows Heule–Kauers–Seidl's streamlining; the covering/sign
  split itself, and its use to *prove* repair instances unsatisfiable, we
  have not found in the literature we searched [list]. In our runs it
  decided in minutes instances that resisted hours of unsplit solving."
- **Would overclaim:** "a new case-splitting method for SAT" (case
  decomposition is cube-and-conquer's home ground); "the first exhaustive
  treatment of term completion" without the "in the sources searched"
  qualifier and the streamlining credit; any wording implying the split is
  proven novel rather than not-found.

### Item 2 — rigidity facts

- **2(a) strongest honest wording:** "Applying the standard merge test
  (Heule–Kauers–Seidl §8; Kauers–Moosbauer Def. 2) exactly over Q, we
  verified that no pair of terms merges in Laderman's scheme (λ=1, and
  hence λ=2 by rescaling) or in Perminov's cn122 — 759 pairs. For cn122 we
  have not found this stated elsewhere."
- **2(a) would overclaim:** "we discovered that Laderman's scheme admits
  no merging pair" (the check and a negative outcome over a large scheme
  collection are published; Laderman's individual coverage by that check
  is unverified, so even the careful wording must present Laderman as a
  re-verification, not a first finding).
- **2(b) strongest honest wording:** "Laderman's scheme is an isolated
  vertex of the flip graph (Kauers–Moosbauer, arXiv:2212.01175); we
  confirmed this independently over {0,±1}. We enumerated the full
  {0,±1} flip component of Perminov's cn122 (34,604 states) and tested
  every term pair at every state (25.4M tests): no collapsible pair.
  Across ~75k visited rank-23 states we also ran all 1,771 triples per
  state through a rank-≤2 flattening filter (~133M tests): no 3-to-2
  collapse. We have not found either census in the literature searched;
  Kauers–Moosbauer's Z₂ component census (64,061 vertices) is the closest
  published analogue and covers different components over a different
  field."
- **2(b) would overclaim:** any sentence presenting Laderman's isolation
  as a campaign discovery; "the flip component of cn122" without the
  {0,±1} scope; "no rank-22 scheme is reachable" (the census excludes
  pair/triple collapses *at visited states of one component*, nothing
  more).
- **2(c) strongest honest wording:** "Five frozen-rest repair instances on
  wrong=1 states of Laderman and Perminov were decided completely (16/16
  exhaustive cases UNSAT each) over {0,±1}. We have not found published
  equivalents."
- **2(c) would overclaim:** dropping the scoping ("with the stated terms
  freed, the rest frozen, over {0,±1}") — e.g. "Perminov's scheme cannot
  be repaired" or "these neighbourhoods contain no rank-22 scheme."
- **2(d) strongest honest wording:** "For Laderman's wrong=1 state with
  terms {2,3,4} freed over quarter-integers, 121 of 174 exhaustive cases
  are decided, all UNSAT (23 of 33 sign patterns complete); the instance
  remains open." 
- **2(d) would overclaim:** calling it "the quarters exclusion" without
  "partial / 121 of 174" — the instance is **not** decided.

### Item 3 — nullity diagnosis

- **Strongest honest wording:** "At the generic real rank-23 solutions
  produced by numerical optimisation, we measured the CP Jacobian nullity
  to be exactly 2r = 46 — the scaling torus and nothing else — so those
  points are locally isolated modulo scaling, and quantisation from
  generic starts has no local direction to follow. This does not conflict
  with Heule–Kauers–Seidl's ≥17-dimensional family: that family passes
  through special, structured schemes, while the numerical points lie on
  a different, minimal-dimension stratum of the same variety. We have not
  found this measurement, or the diagnosis drawn from it, in the
  literature searched."
- **Would overclaim:** "rank-23 decompositions are isolated" (false
  globally — 13,000+ inequivalent decompositions and a ≥17-dimensional
  family are published); "the solution set has dimension 46" (the variety
  has higher-dimensional strata; 46 is the local dimension at the measured
  numerical points only); "rational points cannot be reached numerically"
  without the "from generic starts / by local attraction" scope.

---

## UNVERIFIED register

1. Whether Heule–Kauers–Seidl's §8 merge check was run on Laderman's
   scheme itself ("all schemes" is ambiguous in the text), and whether
   their implementation's merge criterion treats sign/proportionality
   exactly as the campaign's rank-1 residual test does. (Item 2a)
2. Sidebottom arXiv:2610.27451 was seen via search-result text only, not
   read in full; its description here is abstract-level. (Item 2a)
3. Yang arXiv:2502.12390 and Palladinos arXiv:2607.29291 are cited from
   the campaign's RESEARCH.md and earlier-session reading, not re-read in
   full for this audit. (Item 1)
4. The exact tangent-space intersection dimension between the isotropy
   orbit and the gauge torus at Laderman (used qualitatively in Item 3's
   reconciliation; the audit's own derivation from published inputs, not
   a published result).
5. All campaign-side numbers (case counts, tallies, test counts,
   nullities) are as recorded in the campaign's files; this audit checked
   the literature, not the computations.

## Master list of sources searched

Heule–Kauers–Seidl arXiv:1905.10192 (full) and arXiv:1903.11391
(abstract/introduction) · Courtois–Bard–Hulme arXiv:1108.2830 (in part) ·
Kauers–Moosbauer arXiv:2212.01175 (full) · Moosbauer–Poole arXiv:2502.04514
(full; ISSAC 2025, doi:10.1145/3747199.3747566) · Perminov arXiv:2512.21980
(full) · Burichenko arXiv:1508.01110, arXiv:2211.03404, arXiv:2211.06485 ·
Sedoglavic catalogue, fmm.univ-lille.fr (front table + ⟨3×3×3:23⟩ page) ·
Heule–Kullmann–Marek, cube-and-conquer, SAT 2016
(doi:10.1007/978-3-319-40970-2_15; via published summaries/slides) ·
Berger et al., J. Comput. Appl. Math. 406 (2022) 113941
(doi:10.1016/j.cam.2021.113941; abstract/introduction) ·
Chiantini–Ottaviani–Vannieuwenhoven (doi:10.1137/140970276) and
Bocci–Chiantini–Ottaviani (statements via search results/secondary
sources) · Johnson–McLoughlin 1986 (doi:10.1137/0215043; via
Heule–Kauers–Seidl) · Sidebottom arXiv:2610.27451 (search excerpts only) ·
Palladinos arXiv:2607.29291 and Yang arXiv:2502.12390 (via RESEARCH.md) ·
campaign files: TARGETS.md, CHECKPOINT.md, REPORT.md incl. Waves 2–9
addendum, wave17/research/RESEARCH.md.
