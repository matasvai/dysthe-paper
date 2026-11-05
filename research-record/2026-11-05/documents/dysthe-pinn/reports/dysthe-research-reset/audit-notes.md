# Detailed audit ledger

Reviewed 24 September 2026. Paths are relative to the complete Dysthe workspace;
`dysthe-pinn/` identifies the nested Git repository. Expensive physics and training
runs were not repeated. The report is the edited synthesis of this ledger.

## Linear calculations

1. **Optical baseline.** Nine Gaussian runs, 225 norm records, times 0–6, with
   epsilon2 equal to 1, -1/3 or 0. Plane-wave error 2.176e-15, reversibility
   6.694e-16, symmetry 1.755e-16, L2 drift 1.11e-16; independent quadrature
   discrepancy at most 3.905e-9. Coarse sampled maxima differed by up to 0.556%
   despite excellent field refinement. Sources: `results/verification.json`,
   `results/norm_history.csv`.
2. **Broad weighted inputs.** Twenty-two fields, 858 measurements, times 0.25–4;
   random, modulated, chirped, compact and tapered algebraic recipes. Original
   domain effects reached 8.8%. Later selected tests through 16 passed 24 targeted
   2% case-time peak screens. These were not joint refinements on the largest box.
   In one near-degeneracy case at 16 the common-cube weighted-field difference was
   121.8% while peak difference was 0.621%. Source: `results/decay_dataset/`.
3. **Gaussian late-time peaks.** Twenty searches (four cases at five times
   16–256); the four time-256 cases passed the stronger 0.1% audit. Analytic
   transverse reduction reduced cost; independent regularized integration
   checked candidate points. A strong peak near x=-841 shows why central-window
   measurements were inadequate. Sources: `results/long_time/`,
   `results/spatial_reliability/`.
4. **Later extension.** Eight new searches at 512 and 1024 pass the 0.1% screen
   after one stored radial follow-up. The final-doubling effective exponents are
   1.0903 (homogeneous Gaussian), 1.0260 (homogeneous near-degeneracy), 1.3168
   (inhomogeneous Gaussian), and 1.1960 (inhomogeneous near-degeneracy). Candidate
   peaks switch between rings and the axis; one lies near x=-3227. These searches
   are distinct from the earlier fixed-point quadrature checks at the same times.
   Source: `results/extended_decay/`.
5. **Research checks.** Thirty-three scaling checks differ by at most 4.36e-16.
   Of 78 spectral/cancellation measurements, 70 initially passed 2%; eight
   independent follow-ups passed 0.1%. The largest correction to an original
   value was 2.288%. Ten approximate-identity checks reached width 0.75, not an
   arbitrarily narrow limit. Twelve quadrature comparisons had discrepancy at
   most 4.40e-12. None certifies a global supremum or optimal theorem constant.
   Source: `results/research_experiments/`.
6. **Restricted pilot.** Eight inputs at times 16, 32, 64, 128, 256. The summary
   retains 38 initial 1% passes; the two per-case follow-ups also pass. For the
   separated band, extending the radial search removed the boundary concern
   without moving the optimized maximum. For the centered band, finer radial
   sampling resolved the initial discrepancy. The Hermite-Gaussian final-doubling
   exponents for cancellation orders 0, 1, 2 are 1.04375, 1.35094, 1.49349 at
   width 3, and 1.07477, 1.28368, 1.42893 at width 6. The two smooth bands give
   1.49915 and 1.07055. Smooth-band L1 normalization changes by 5.096e-6 under
   refinement. Source: `results/restricted_decay/`.
7. **Visualizations and an interpretation correction.** Random and two-packet
   animations are not extra convergence studies. Under the real propagator,
   the original quadrature-phase pair is a+0.7 i b, with a and b real. Its
   intensity is a²+0.49b², with zero mutual cross-term (stored numerical residual
   below 1.6e-14). A separate zero-phase control shows interference. The original
   field calculation was unchanged; its interpretation was corrected. Source:
   `output/packet_alternative_views/README.md`.

Cubic scaling forbids a uniformly faster unrestricted homogeneous estimate with
only the same L1 input norm. Moment cancellation does not exclude rescaling.
An upper frequency cutoff alone does not exclude dilation toward zero either.
The useful question needs quantitative restrictions or scale-sensitive norms.
Finite pointwise accuracy also does not certify that a global maximum was found.

## Nonlinear water-wave branch

8. **Exact NLS reduction.** At time 20, N=1024, L=80, dt=.0025, field error is
   3.6834e-9; refinement is consistent with fourth order. At N=256 the field error
   is 2.8828e-3 despite action drift 1.8e-12. These are benchmarks of a known
   whole-line wave sampled on a checked periodic domain.
9. **Profiles and propagation.** Twenty-eight profiles across four branches,
   epsilon 0–.15, have maximum residual 1.9873e-11. One representative received
   independent grid/box checks. Its peak changes from 1.728655889 at L=80 to
   1.728564868 at L=320 even with a tiny profile residual. Twelve propagation
   cases reach time 20. The dt=.01 phase-sensitive error was 2.918% although
   aligned shape error was .0798%; dt=.00125 reduced field error to 1.703e-6.
10. **Perturbations.** Three disturbances reach time 40. The two 1% amplitude
    cases end with 2.488% and 2.614% aligned shape deviations; the phase case
    ends near .04065%. Only the positive amplitude case was repeated at half
    step. Fixed-profile phase/translation fitting does not account for evolving
    branch parameters and does not isolate radiative decay.
11. **Collisions.** One refined Dysthe geometry gives about 1.8% excess action
    outside prescribed radius-six cores; refinements yield .017821–.017841.
    The outgoing fixed-profile errors are about .23038 and .17784. The NLS
    control recovers shapes to about 7.98e-8 after alignment. Neither a universal
    radiation fraction nor a complete scattering result follows.

Source index: `results/nonlinear/analysis_summary.json`, `profile_checks.json`,
`timestep_dysthe_*`, `perturb_*`, `collision_refined_*` in that directory.
These are the spatial water-wave equation, not the three-coordinate optical PDE.

## Optical nonlinear branch and long evolution

12. **Stripe control.** The unperturbed stripe preserves transverse symmetry
    to roundoff. A symmetry-preserving calculation cannot establish transverse
    stability. The stripe is not localized in all three coordinates.
13. **Disturbance through time 4.** Relative transverse variation increases
    .00499994 → .0476074. The largest final pairwise field discrepancy across
    stored checks is 4.67691e-4. Grid, time and box checks support this early
    observation, although they are not a full tensor product of finest settings.
14. **Disturbance through time 8.** Spatial disagreement remains: final
    variation roughly .49 vs .58, peak roughly 3.55 vs 3.29, spectral-edge
    fraction up to .032. Time refinement improves action conservation without
    fixing spatial disagreement. The finer time-4 tests did not continue to 8.
    Enlarging the transverse box while repeating the same cosine does not test
    longer disturbance wavelengths. Sources: `results/nonlinear/transverse_*`
    and `optical3d_mixed_*`.
15. **Planned long reference sequence.** It passed at time 2 and stopped at 8.
    At 8, field grid difference is 2.503e-6, peak difference .0079535 versus a
    .005 tolerance, and time differences are tiny. This is a different issue
    from the strongly disturbed stripe above. Peak sampling is a possible
    explanation, not a demonstrated diagnosis. Source:
    `dysthe-pinn/results/long-reference-77502/sequence-summary.json`.
16. **Long periodic traces.** The 64³, dt=.01 run truly integrates 0–2048;
    `completed_unvalidated` and action drift 7.39e-12 do not establish phase
    accuracy. Its conserved-action peak floor is .0321432. The late power-law
    fit has R²=.00351; a descriptive four-harmonic fit over 1536–1664 has
    R²=.98498 and period 11.4821. It was not tested on independent future data.
    The separate 32³, dt=.5 preview failed its action threshold at 10321 before
    intended 12288. Do not splice it into the finer run or call its horizon
    validated. Sources: `dysthe-pinn/results/late-window-1024-2048/`,
    `results/breathing-preview-12288/`, `reports/late-window-review/` in that repo.
17. **Pilots and infrastructure.** Fixed-grid time-step comparisons reached
    only 32 on 32³ or 8 on 64³. For example, dt=.5 versus .01 at time 32 gives
    field difference .00021177. This does not validate time 10000. GPU smoke,
    exact resume, local time-1 late-window checks, and scripts planning windows
    near 5000 establish workflow capabilities, not additional resolved runs.

## Optical learning and fresh checks

18. **Original PINN.** One initial pulse, time 0–.5, 20,000 updates, 3584.13
    seconds. Maximum sampled field error .0066510, peak error .00214757,
    action drift .00180608. Separate short fixed-box reference audit passes.
    Outer `output/pinn_full_evaluation/` and nested evaluation records are copies
    of this one experiment. There is no held-out optical initial-field study or
    demonstrated matched-accuracy speed benefit. Changing the hard-coded initial
    condition requires retraining; a conditioned operator needs different inputs.

Fresh small checks: six original nonlinear unit tests; twelve nested tests in
`test_physics.py`, `test_resume.py`, `test_late_window.py`; and one cross-solver
nonseparable-field comparison, with RHS difference 8.4463e-18 and one-step
relative difference 3.1905e-20. The bundled `check_solver_agreement.py` reproduces
the latter when both source trees are available. No equation-implementation
mismatch was found. This does not substitute for full-horizon refinement.

There has been no fully localized three-coordinate optical existence search,
nonlinear radiation-decay fit, laboratory comparison, or dimensional calibration
in these archived wave studies. Their absence must not be described as failure
to find an object after a search that was never performed.
