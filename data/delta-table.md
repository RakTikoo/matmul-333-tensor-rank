# The delta table — wrong=1 neighbours across ranks 23–26

**Date:** 2026-11-23. **Set (named, finite):** six verified
⟨3,3,3⟩ schemes over ℚ — Laderman (rank 23), Perminov's cn122
(rank 23), the two catalogue rank-24 schemes (metaflip-24 and
proj-24), the constructed rank-25 split of metaflip-24, and the
campaign's rank-26 block scheme (lensC-26). **Quantities per
scheme:** the unit-term census (count, positions, values, naive
vs off-support), and the full single-drop battery — for each
term, the number of wrong entries of the state that dropping it
leaves (equivalently, the nonzero-entry count of the dropped
term's tensor). Measured in Wave 40; gated in Wave 47.

## The claim, at its approved wording

"For each of six verified ⟨3,3,3⟩ schemes spanning ranks 23–26 (Laderman, Perminov's cn122, the two catalogue rank-24 schemes, our constructed rank-25 split, and our rank-26 block scheme), we computed the full single-drop battery exactly: the state left by dropping one term, and how many entries it gets wrong. A wrong=1 neighbour exists in exactly the schemes that have a unit term — Laderman (5, all naive), cn122 (3, all naive), proj-24 (1), lensC-26 (19, all naive) — and in none that do not (metaflip-24 and split-25, whose closest drops are 2 wrong). The near-miss structure does not soften gradually down the ranks 25→24→23; which flavour of wrong=1 neighbour a scheme offers is a property of its unit terms, not of its rank. Every wrong=1 state in the table is the standard flavour — one missing entry on the tensor's support, have 0 / want 1 — except one: proj-24's unique unit term sits off-support (its factors are e₅, −e₈, e₄, its single entry −1 at (5,8,4), where the tensor is zero), so its drop state has an extra entry to cancel rather than a missing one to fill: have +1 / want 0 at (5,8,4). That state is banked, and its repair instance is staged. The proj-24 and Laderman rows were re-derived by an independent exact computation for this gate, agreeing on every count; proj-24's battery had already been cross-checked drop-by-drop against the exact verifier in Wave 40."

## The table

| scheme | rank | unit terms | min single-drop wrong | drops attaining it |
|---|---|---|---|---|
| Laderman | 23 | 5, all naive, all +1 | 1 | the 5 unit terms {2, 19, 20, 21, 22} |
| Perminov cn122 | 23 | 3, all naive | 1 | the 3 unit terms (drops 6, 13, 18) |
| metaflip-24 | 24 | 0 | 2 | — |
| proj-24 | 24 | 1, off-support, −1 at (5,8,4) | 1 | drop 0 only |
| split-25 (constructed) | 25 | 0 | 2 | — |
| lensC-26 | 26 | 19, all naive | 1 | the 19 unit terms |

Full drop-wrong distributions, for the two rows re-derived by
the gate's independent battery:

- **Laderman:** {1:5, 7:6, 8:8, 27:4} (wrong count : number of
  drops).
- **proj-24:** {1:1, 2:1, 3:3, 4:4, 6:2, 8:2, 9:1, 12:5, 16:1,
  18:2, 24:1, 27:1}; term 0 has U column +1 at row 5 only, V
  column −1 at row 8 only, W column +1 at row 4 only, and its
  term tensor's single entry is −1 at flat position 481 =
  (5,8,4), where T = 0. The minus-0 state's one wrong entry is
  at (5,8,4), **have +1 / want 0** — the full scheme's other
  terms contribute +1 there, which term 0 existed to cancel;
  dropping it leaves that +1 uncancelled. (Wave 40's sign
  correction, independently confirmed by the gate.)

## Second path and recorded limit

The Wave-47 gate re-derived the **proj-24 and Laderman rows
with fresh exact code**, agreeing on every count above,
including the have +1 / want 0 sign; both schemes verify 0/729
as full sums under the gate's own arithmetic. proj-24's battery
had additionally been cross-checked drop-by-drop (24/24)
against fresh `verify.py mismatch` runs in Wave 40. cn122's
unit census (3, all naive) is independently re-derived by the
Wave-28 gate's recount and by the Wave-47 gate's G4 leg.

**Recorded limit:** the full drop distributions of metaflip-24,
split-25 and lensC-26 have no second path beyond Wave 40's own
record (with a CLI spot-check of metaflip-24's minimum: drop
wrong 2 at term 14). Their unit-term counts (0, 0, 19) are
corroborated — lensC-26's by the Wave-32 gate's duplicate
grouping, metaflip-24's and split-25's by the Wave-41 candidate
pool built from the same batteries — but corroboration is not
an independent recount of those three distributions. The
claim's load-bearing rows (proj-24's unique off-support seed;
the existence pattern across all six) rest only on each row's
unit count and minimum, which are independently held where it
matters.

## Scope

The "exists ⟺ has a unit term" pattern is an observation over
these six named schemes, and at single-drop level it is close
to definitional (a 1-wrong drop is a 1-entry term tensor); the
content of the table is the flavour split and the rank pattern,
not the bare equivalence. proj-24's wrong=1 state is the only
off-support one **in this table** and the first in the
campaign's bank; its staged repair instance (19 exhaustive
cases, derived in Wave 40) tests whether that state is isolated
— a repair would assemble a rank-23 scheme, and nothing here
bears on rank 22.
