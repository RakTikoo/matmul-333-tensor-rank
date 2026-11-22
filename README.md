# The 3×3 matrix multiplication tensor: verified findings around rank 23

Computational findings on the rank of the ⟨3,3,3⟩ matrix multiplication
tensor, obtained by an exact-methods campaign in November 2026. The rank
over ℚ is known to satisfy 19 ≤ R ≤ 23 (Bläser 2003; Laderman 1976).
**This repository claims no new decomposition and no rank-22 scheme.**
What it contains is a set of exact, machine-checkable measurements and
exclusions around the two best-known rank-23 schemes — Laderman's
(arXiv-era catalogue: Sedoglavic's FMM collection) and Perminov's cn122
(arXiv:2512.21980) — each shipped with the certificates and code needed
to re-verify it independently.

## Headline result: exact Jacobian kernel dimensions at the two schemes

For the Brent system of a rank-23 decomposition (729 equations, 621
factor entries), we computed the Jacobian kernel **exactly over ℚ** at
both schemes, by two independent implementations that agree:

| point | dim ker J | trivial tangents | excess |
|---|---|---|---|
| Laderman (1976) | 76 | 70 | **6** |
| Perminov cn122 (2025) | 94 | 70 | **24** |

The trivial tangents at any exact decomposition are the 46-dimensional
rescaling torus plus the 26-dimensional tangent space of the isotropy
orbit (27 Lie parameters, 1-dimensional action kernel), overlapping in
2 dimensions: 46 + 26 − 2 = 70. The excess — the kernel dimension
beyond all trivial tangents — is **6 at Laderman and 24 at Perminov**.

Consequences, stated at exactly the strength proved:

- Perminov's excess of 24 is consistent with Perminov lying on the
  ≥17-dimensional family of rank-23 schemes whose existence
  Heule–Kauers–Seidl established (ISSAC 2019 / JSC 2021).
- Laderman's excess of 6 is below 17, so Laderman does not lie on a
  smooth 17-dimensional part of that family: the variety is stratified
  and local dimension is point-dependent.
- This reconciles the published ≥17 with the nullity of exactly
  2r = 46 measured at generic numerical rank-23 points (see
  `claims.md`, Item 3): those points decompose a perturbed tensor,
  whose stabiliser is trivial.

Certificates: `certificates/kernel_laderman.npz` and
`certificates/kernel_perminov.npz` contain exact rational kernel bases;
every vector satisfies J·v = 0 over ℤ, checkable in minutes.
Two independent computations: `code/moduli_exact.py` (mod-p rank +
CRT/rational reconstruction) and `code/rigor_check.py` (a from-scratch
adversarial re-implementation: fresh primes, exact integer matvecs,
independent construction of the trivial tangent spaces, Bareiss exact
ranks). Their agreement is the result's evidence.

## Other findings (precise wordings and scopes in `claims.md`)

1. **A covering-parity case split** for deciding term-repair instances:
   an exhaustive split derived from a wrong=1 state's single wrong
   entry, indexed by which freed terms cover that entry and the sign
   pattern of their products there. It decided in minutes instances
   that resisted hours of unsplit SMT solving. Term-freeing itself
   follows Heule–Kauers–Seidl's streamlining; the split and its use as
   an unsatisfiability proof we have not found in the literature
   searched (audit in `data/novelty-audit.md`).
2. **Five completely decided repair instances** (16/16 exhaustive
   cases UNSAT each, coefficients in {0,±1}, stated terms freed, rest
   frozen) on wrong=1 states of Laderman and Perminov.
3. **A census of Perminov's {0,±1} flip component**: 34,604 states,
   every term pair tested at every state (25.4M tests), no collapsible
   pair; and ~133M triple tests through a rank-≤2 flattening filter
   across ~75k visited rank-23 states, no 3-to-2 collapse. (Laderman's
   flip-graph isolation is published by Kauers–Moosbauer,
   arXiv:2212.01175; we confirm it independently and claim nothing for
   it.)
4. **Pair-merge exclusions over all of ℚ**: the standard merge test
   applied exactly shows no pair of terms merges in Laderman (λ=1,
   hence λ=2) or in Perminov cn122 — 759 pairs. For cn122 we have not
   found this stated elsewhere.
5. **A completely decided quarters exclusion**: for Laderman's
   wrong=1 state with terms {2,3,4} freed over quarter-integers
   {0, ±1, ±1/2, ±1/4, ±3/4}, all 174 exhaustive cases are decided,
   all UNSAT (33 of 33 sign patterns complete), as of 2026-11-22.
   The instance is **fully decided** — no quarters completion of
   the freed triple exists. Full record in
   `data/quarters-status-2026-11-22.md`.

## Verify it yourself

```bash
python3 code/verify.py check certificates/laderman_r23_Q.json      # VERIFIED, 0/729 over Q
python3 code/verify.py check certificates/perminov_cn122_r23_Q.json # VERIFIED, 0/729 over Q
python3 code/check_kernels.py  # pins dim ker J = 76 / 94 from both sides (needs numpy)
```

`code/check_kernels.py` is the packaged, self-contained
re-verification of the headline numbers. `code/moduli_exact.py`,
`code/moduli_float.py` and `code/rigor_check.py` are the original
campaign scripts, archived as run for provenance — they reference
the campaign's internal file layout and are not the packaged entry
point.

`verify.py` uses exact rational arithmetic (`fractions.Fraction`);
floats are rejected. Both scheme files are **literature schemes**,
included as the objects of study, not as campaign results.

## What this is not

- No rank-22 (or lower) decomposition over any field is claimed.
- Timeouts in the underlying campaign were recorded as "no
  conclusion", never as impossibility; every UNSAT above comes from a
  control-validated encoding (a known-good scheme with the same terms
  freed returns SAT and verifies).
- Novelty statements are of the form "not found in the sources
  searched", with the search documented in `data/novelty-audit.md` —
  they are not proofs of priority.

## Layout

- `claims.md` — every claim at its strongest honest wording, with its
  scope and the wording that would overclaim it.
- `code/` — the exact verifier, the case-split drivers, both kernel
  computations and the independent rigor check.
- `certificates/` — the two literature schemes, the exact kernel
  bases, and the rigor run log.
- `data/` — the novelty audit, the flip-component census, the
  triple-sweep and decided-instance reports, the quarters status.

## License

MIT (code and text). The two scheme files are the work of Laderman
(1976) and Perminov (2025) and are redistributed for verification.

## Author

RakTikoo — an independent computational campaign, November 2026.
