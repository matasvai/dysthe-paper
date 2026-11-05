# Dysthe work record through 5 November 2026

42 experiment, implementation and report entries. The chat appendix covers the project conversations reviewed for this compilation.

Dates below are qualified by their source; they are not all execution dates. This catalogue records completed work, negative results, repairs and plans. It makes no new existence or global-stability claim.

## Start here

- [Printable catalogue](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/catalogue/main.pdf)
- [Editable catalogue source](https://github.com/matasvai/dysthe-paper/tree/codex/research-record-2026-11-05/research-record/2026-11-05/catalogue).
- [Archived reports, sources and figures](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/README.md)
- [Experiment snapshots, compact results and raw-data manifest](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/README.md)
- [All project chats, including unrelated topics](CHATS.md).
- [Machine-readable catalogue](catalogue.json) and [date/name/status CSV](experiments.csv).

## Current findings and limits

- The spatial CPU comparison favored per-inlet slab PINNs among the learned methods; numerical integration remained faster. FNO/PINO did not pass the pilot gates.
- Returned GPU2 records include successful periodic reference calculations through xi=64, failed PINN gates, and random-input execution errors. Exact A100 hardware is not verified by that snapshot.
- October 27 conditioning and input-identity repairs passed bounded CPU validation. Repaired GPU generalization remains pending in the reviewed evidence.
- The separately versioned temporal model has qualified primary calculations through T=16, near-zero controls, and direct periodic linear evaluations through T=1024. Nonlinear T=1024 remains a smoke-tested target.
- Periodic recurrence and isolated-packet decay require separate conclusions. Finite computations do not prove global existence.

## Chronological index

| Date | Experiment or output | Scope | Recorded status |
|---|---|---|---|
| 2026-09-10 | [Formal checkpoint and research-meeting visual reports](#hist-checkpoint) | Historical formulation | completed historical report collection |
| 2026-09-10 | [Original optical-coordinate Fourier solution controls](#hist-lin-base) | Historical formulation | completed historical CPU experiment |
| 2026-09-10 | [Scaling, spectral, cancellation, concentration and quadrature tests](#hist-spectral-controls) | Historical formulation | completed historical CPU experiment |
| 2026-09-10 | [Gaussian weighted-decay extension and spatial audit at t = 256](#hist-weighted-256) | Historical formulation | completed historical CPU experiment |
| 2026-09-10 | [Artificial-input weighted-decay survey and t16 refinement](#hist-weighted-inputs) | Historical formulation | completed exploratory historical CPU experiment |
| 2026-09-12 | [Extended Gaussian weighted peak searches to t = 1024](#hist-weighted-1024) | Historical formulation | completed historical CPU experiment |
| 2026-09-14 | [Quadrature-packet intensity interpretation correction](#hist-interference-correction) | Historical formulation | completed correction with numerical controls |
| 2026-09-14 | [Three-coordinate optical stripe perturbations](#hist-optical-stripes) | Historical formulation | completed through T4; T8 unresolved |
| 2026-09-14 | [Canonical packet animation and phase viewer extension](#hist-packet-animation) | Historical formulation | completed historical visualization |
| 2026-09-14 | [NLS benchmark, spatial Dysthe profile continuation and collisions](#hist-solitary-spatial) | Historical formulation | completed historical CPU experiment |
| 2026-09-16 | [Moment cancellation and separated-band weighted decay](#hist-restricted-inputs) | Historical formulation | completed historical CPU experiment |
| 2026-09-17 | [Short-time A100 PINN benchmark for equation 1.27](#hist-optical-pinn) | Historical formulation | completed historical GPU training and reference audit |
| 2026-09-17 | [Historical optical sequential reference audit: T=2 passes and T=8 fails the peak grid gate](#hist-optical-reference-t8) | Historical formulation | Failed sampled peak grid-convergence screen at T=8; sequence stopped after T=2 passed |
| 2026-09-18 | [Historical optical fine-step trajectory to T=2048 and descriptive local oscillation fit](#hist-optical-late-window-2048) | Historical formulation | completed_unvalidated; descriptive fit completed |
| 2026-09-18 | [Historical optical coarse breathing preview: T=12288 target stopped at t=10321](#hist-optical-preview-10321) | Historical formulation | failed_diagnostics; stopped at t=10321 before target T=12288 |
| 2026-09-23 | [Nontechnical overview of the project and numerical/PINN methods](#doc-project-overview) | Historical formulation | Completed communication artifact |
| 2026-09-24 | [Retrospective of earlier Dysthe experiments and research reset](#doc-research-reset) | Historical formulation | Completed retrospective report; later active-scope decision supersedes optical proposals |
| 2026-09-30 | [Versioned water-wave spatial model and repository contracts](#spatial-scope-2026-09-30) | Active spatial water-wave | implemented |
| 2026-10-01 | [Bounded solitary-profile propagation and unrestricted perturbation smoke](#spatial-solitary-smoke-2026-10-01) | Active spatial water-wave | completed smoke |
| 2026-10-02 | [Solitary branch epsilon=0.025 grid/step/domain campaign](#spatial-solitary-gate1-2026-10-02) | Active spatial water-wave | completed computations |
| 2026-10-03 | [Before Reading Dysthe 1979: prerequisite guide](#doc-1979-guide) | Water-wave review | completed pedagogical report |
| 2026-10-16 | [Restricted complex-envelope formula editor and CPU execution](#spatial-custom-envelope-2026-10-16) | Active spatial water-wave | completed software and smoke |
| 2026-10-16 | [Stage-one analytic controls and response-relative domain refinement](#spatial-reference-stage1-2026-10-16) | Active spatial water-wave | completed bounded validation |
| 2026-10-16 | [Three-input numerical simulator demonstration](#spatial-small-simulator-2026-10-16) | Active spatial water-wave | completed bounded validation |
| 2026-10-23 | [Dysthe evolution: numerical evidence and existence](#doc-existence-review) | Water-wave review | completed literature/math review |
| 2026-10-25 | [NLS and physics-informed learning review](#doc-nls-pinn-literature) | Water-wave review | completed targeted literature review |
| 2026-10-25 | [Learning Dysthe evolution across initial wave fields](#doc-operator-protocol) | Water-wave review | completed literature-grounded protocol |
| 2026-10-26 | [Matched FNO/PINO and per-inlet spectral PINN pilot](#spatial-cpu-pilot-2026-10-26) | Active spatial water-wave | completed pilot |
| 2026-10-26 | [GPU2 long-distance campaign: retained reference successes and PINN failures](#spatial-gpu2-campaign-2026-10-26) | Active spatial water-wave | partly completed with failed gates |
| 2026-10-26 | [Staged distance workflow and CPU execution smoke](#spatial-long-workflow-2026-10-26) | Active spatial water-wave | completed workflow smoke |
| 2026-10-26 | [Verified periodic reference and differentiable Torch adapter](#spatial-reference-torch-2026-10-26) | Active spatial water-wave | implemented and tested |
| 2026-10-27 | [Dysthe solitary waves and published tests](#doc-solitons-published-tests) | Water-wave review | completed revised review of published cluster snapshot |
| 2026-10-27 | [Random-inlet identity repair and spectral PINN conditioning ablation](#spatial-h2-random-repair-2026-10-27) | Active spatial water-wave | completed cpu validation gpu rerun pending |
| 2026-10-30 | [Numerical evidence and a PINN research framework](#doc-modelling-report) | Water-wave review | completed research report |
| 2026-10-30 | [Temporal packet domain checks and neural representation floors](#temp-domain-representation) | Temporal water-wave extension | completed CPU diagnostics |
| 2026-10-30 | [Temporal high-steepness sideband timestep audit](#temp-h2-timestep-repair) | Temporal water-wave extension | completed CPU numerical repair |
| 2026-10-30 | [Direct periodic linear evolution through T = 1024](#temp-linear-1024) | Temporal water-wave extension | completed CPU exact-discrete-propagator experiment |
| 2026-10-30 | [Periodic and isolated nonlinear horizon ladder to T = 1024](#temp-long-horizon-targets) | Temporal water-wave extension | implemented and smoke-tested; production horizons not executed |
| 2026-10-30 | [Complex growth and phase check for temporal modulational instability](#temp-mi-controls) | Temporal water-wave extension | completed CPU control |
| 2026-10-30 | [Very-early nonlinear evolution and Gaussian cutoff audit](#temp-near-zero) | Temporal water-wave extension | completed CPU experiment |
| 2026-10-30 | [Original temporal Dysthe multi-profile numerical proof of concept](#temp-reference-t16) | Temporal water-wave extension | completed CPU primary reference through T16 |
| 2026-10-30 | [Nonlinear envelope visual companion across three initial profiles](#temp-visual-t4) | Temporal water-wave extension | completed CPU numerical visualization |

## Detailed records

<a id="hist-checkpoint"></a>
### HIST-CHECKPOINT — Formal checkpoint and research-meeting visual reports

**Date:** 2026-09-10. **Basis:** Explicit report and checkpoint dates.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed historical report collection.

- The formal checkpoint is 30 pages and the separate archival checkpoint is 32 pages. Both preserve their original canonical or optical model labels.

Limits or outstanding work:
- Later packet-interference correction must accompany the original interpretation.

Evidence:
- [dysthe_formal_checkpoint.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe_formal_checkpoint.pdf)
- [formal_report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/report/formal_report.tex)
- [README.md](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/latex/dysthe_formal_checkpoint/README.md)
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/checkpoints/2026-09-10/README.md)
- [dysthe_checkpoint_2026-09-10.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe_checkpoint_2026-09-10.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python report/build_checkpoint.py
```

<a id="hist-lin-base"></a>
### HIST-LIN-BASE — Original optical-coordinate Fourier solution controls

**Date:** 2026-09-10. **Basis:** Documented by September 10 checkpoint; exact execution timestamp not recorded in results/verification.json.

**Model:** Historical optical three-coordinate Dysthe equation (1.27), Dysthe3D-1.27; not active water-wave model. **Status:** completed historical CPU experiment.

- Nine Gaussian runs through t = 6 produced 225 norm records. Saved controls cover phase, reversibility, symmetry, grid and domain refinement, and independent quadrature.

Limits or outstanding work:
- These are not nonlinear water-wave results. Large full-field arrays can be regenerated.

Evidence:
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/verification.json)
- [norm_history.csv](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/norm_history.csv)
- [dysthe_report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/report/dysthe_report.tex)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python numerical_solutions.py
python report/make_tables.py
```

<a id="hist-spectral-controls"></a>
### HIST-SPECTRAL-CONTROLS — Scaling, spectral, cancellation, concentration and quadrature tests

**Date:** 2026-09-10. **Basis:** README research-batch heading and September 10 checkpoint.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed historical CPU experiment.

- The archive contains 33 scaling checks, 78 spectral and cancellation measurements with eight separately refined flags, and ten approximate-identity checks. Fixed-coordinate quadrature includes t = 512 and 1024.

Limits or outstanding work:
- The t = 512 and 1024 entries in this batch are fixed-coordinate checks, not new peak searches.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/research_experiments/summary.json)
- [RESULTS.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/research_experiments/RESULTS.md)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python research_experiments.py scaling
python research_experiments.py sweep
python research_experiments.py quadrature
python research_experiments.py identity
python refine_research_flags.py
```

<a id="hist-weighted-256"></a>
### HIST-WEIGHTED-256 — Gaussian weighted-decay extension and spatial audit at t = 256

**Date:** 2026-09-10. **Basis:** Included in September 10 checkpoint.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed historical CPU experiment.

- Four Gaussian-family curves extend through t = 256. Separate longitudinal-period and radial-domain changes, together with independent cusp-regularized integral checks, pass the stated 0.1 percent peak screen.

Limits or outstanding work:
- Finite sampled searches do not certify the whole-space supremum.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/long_time/summary.json)
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/spatial_reliability/summary.json)
- [RESULTS.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/spatial_reliability/RESULTS.md)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python long_time_decay.py
python spatial_reliability.py
```

<a id="hist-weighted-inputs"></a>
### HIST-WEIGHTED-INPUTS — Artificial-input weighted-decay survey and t16 refinement

**Date:** 2026-09-10. **Basis:** September 10 checkpoint date; exact batch dates unrecorded.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed exploratory historical CPU experiment.

- The survey covers 22 artificial fields in two regimes and 858 weighted measurements. Four selected families were independently refined through t = 16.

Limits or outstanding work:
- The weighted fractional-derivative maximum differs from the ordinary envelope L-infinity norm. Several initial results were sensitive to domain size.

Evidence:
- [manifest.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/decay_dataset/manifest.json)
- [weighted_decay.csv](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/decay_dataset/weighted_decay.csv)
- [refinement_checks.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/decay_dataset/refinement_checks.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python decay_dataset.py
python refine_decay.py
```

<a id="hist-weighted-1024"></a>
### HIST-WEIGHTED-1024 — Extended Gaussian weighted peak searches to t = 1024

**Date:** 2026-09-12. **Basis:** Prepared date in results/extended_decay/RESULTS.md.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed historical CPU experiment.

- Eight new case-time searches, covering four inputs at t = 512 and 1024, pass consistency checks after retained follow-ups. Finite-interval exponents vary by case.

Limits or outstanding work:
- No common asymptotic exponent or uniform theorem established.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/extended_decay/summary.json)
- [RESULTS.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/extended_decay/RESULTS.md)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python extend_decay.py
python refine_extended_decay.py
python report/summarize_extended_decay.py
```

<a id="hist-interference-correction"></a>
### HIST-INTERFERENCE-CORRECTION — Quadrature-packet intensity interpretation correction

**Date:** 2026-09-14. **Basis:** Chat turn date verified in Plan 3D Dysthe equation model; exact numerical execution timestamp remains unrecorded.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed correction with numerical controls.

- The original 90-degree pair has zero intensity cross-term at every time under the real-coefficient linear propagator. A separate zero-phase control demonstrates interference.

Limits or outstanding work:
- The correction changes the interpretation, not the original computed total field.

Evidence:
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/packet_alternative_views/README.md)
- [interference_control_checks.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/packet_alternative_views/interference_control_checks.json)
- [diagnostics.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/packet_alternative_views/diagnostics.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python make_packet_alternative_views.py
python make_interference_control.py
```

<a id="hist-optical-stripes"></a>
### HIST-OPTICAL-STRIPES — Three-coordinate optical stripe perturbations

**Date:** 2026-09-14. **Basis:** Nonlinear solitary-wave report date.

**Model:** Historical optical three-coordinate Dysthe equation (1.27), Dysthe3D-1.27; not active water-wave model. **Status:** completed through T4; T8 unresolved.

- Transverse variation grows from 0.5 percent to about 4.76 percent by T = 4. Reported fine-resolution comparisons are below 4.68e-4.

Limits or outstanding work:
- This is optical evidence only. The stripes are not fully localized 3D solitons, and T = 8 remains spatially unresolved.

Evidence:
- [transverse_summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/nonlinear/transverse_summary.json)
- [analysis_summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/nonlinear/analysis_summary.json)
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/nonlinear/README.md)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python -m nonlinear.experiments transverse
python -m nonlinear.refinements transverse
```

<a id="hist-packet-animation"></a>
### HIST-PACKET-ANIMATION — Canonical packet animation and phase viewer extension

**Date:** 2026-09-14. **Basis:** Chat turn date verified in Plan 3D Dysthe equation model; exact numerical execution timestamp remains unrecorded.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed historical visualization.

- Three stages of 65 frames extend through t = 256. A later phase viewer contains 122 snapshots through t = 2056. Checks of the displayed-coordinate domain and spacing are retained.

Limits or outstanding work:
- Central displayed peaks and quantized view data are not whole-space supremum measurements.

Evidence:
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/checkpoint_3_4_animations/README.md)
- [audit.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/checkpoint_3_4_animations/audit.json)
- [EXTENSION.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/packet_phase_interactive/EXTENSION.md)
- [extended_checks.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/packet_phase_interactive/extended_checks.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python animate_checkpoint_3_4.py
python output/packet_phase_interactive/extend_data.py
```

<a id="hist-solitary-spatial"></a>
### HIST-SOLITARY-SPATIAL — NLS benchmark, spatial Dysthe profile continuation and collisions

**Date:** 2026-09-14. **Basis:** Explicit report date and nonlinear/README.md.

**Model:** Historical spatial water-wave Dysthe, Fedele-Dutykh coefficient tuple (1,1,8,2,2); pre-repository-baseline implementation. **Status:** completed historical CPU experiment.

- The exact NLS benchmark has relative field error about 3.68e-9 at T = 20. All 28 continued profiles have discrete profile residual below 2e-11. The refined collision radiation proxy is about 1.8 percent outside two cores of radius six.

Limits or outstanding work:
- Discrete profiles and finite-distance tests do not establish continuum orbital stability or elastic soliton collisions.

Evidence:
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/nonlinear/README.md)
- [benchmark_summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/nonlinear/benchmark_summary.json)
- [profile_summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/nonlinear/profile_summary.json)
- [analysis_summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/nonlinear/analysis_summary.json)
- [nonlinear_solitary_wave_report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/report/nonlinear_solitary_wave_report.tex)
- [nonlinear_solitary_wave_report.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/nonlinear_solitary_wave_report.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python -m nonlinear.experiments benchmark
python -m nonlinear.experiments profiles
python -m nonlinear.experiments dynamics
python -m nonlinear.refinements collision
python -m nonlinear.analyze
```

<a id="hist-restricted-inputs"></a>
### HIST-RESTRICTED-INPUTS — Moment cancellation and separated-band weighted decay

**Date:** 2026-09-16. **Basis:** Explicit date in output/restricted_decay/restricted_decay.tex.

**Model:** Historical canonical three-coordinate linear propagator, w=kx^3+3*s*kx*(ky^2+kz^2)+3*beta*(ky^2+kz^2); not active water-wave model. **Status:** completed historical CPU experiment.

- The study contains 40 records through t = 256: 38 first-pass screens and two successful follow-ups. The separated-band finite-interval exponent is approximately 1.4992.

Limits or outstanding work:
- Original flags retained; finite-time behavior does not prove a decay theorem.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/restricted_decay/summary.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/results/restricted_decay/verification.json)
- [restricted_decay.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/restricted_decay/restricted_decay.tex)
- [restricted_input_decay_and_practical_model.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/restricted_input_decay_and_practical_model.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python restricted_decay.py
python report/build_restricted_report.py
```

<a id="hist-optical-pinn"></a>
### HIST-OPTICAL-PINN — Short-time A100 PINN benchmark for equation 1.27

**Date:** 2026-09-17. **Basis:** Checkpoint date in output/pinn_full_evaluation/report.tex; training summary has no wall-clock run date.

**Model:** Historical optical three-coordinate Dysthe equation (1.27), Dysthe3D-1.27; not active water-wave model. **Status:** completed historical GPU training and reference audit.

- The run completed 20,000 training steps on a recorded NVIDIA A100-PCIE-40GB GPU. Over 0 <= t <= 0.5, the sampled maximum relative L2 error is 0.006651002 and the peak error is 0.002147572. A separate fixed-period reference audit passes.

Limits or outstanding work:
- Single initial field and short window; no active water-wave transfer claim, whole-space result or long-time claim.

Evidence:
- [training-summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/pinn_full_evaluation/training-summary.json)
- [metrics.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/pinn_full_evaluation/metrics.json)
- [reference-audit.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/pinn_full_evaluation/reference-audit.json)
- [report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pinn_full_evaluation/report.tex)
- [pinn_full_training_evaluation.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/pinn_full_training_evaluation.pdf)

<a id="hist-optical-reference-t8"></a>
### HIST-OPTICAL-REFERENCE-T8 — Historical optical sequential reference audit: T=2 passes and T=8 fails the peak grid gate

**Date:** 2026-09-17. **Basis:** Dated public review in project chat Plan 3D Dysthe equation model, turn 01a0b0a9-0861-7b43-8c82-24ee257450d7 (America/New_York). This is the review date, not a separately recorded simulation start timestamp..

**Model:** Dysthe3D-1.27: historical three-coordinate optical equation, periodic domain of side lengths 12, full cubic nonlinearity and derivative correction. **Status:** Failed sampled peak grid-convergence screen at T=8; sequence stopped after T=2 passed.

- The retained sequence-summary.json has two stages: T=2 with status pass and T=8 with status fail and return code 2.
- At T=8, the largest sampled peak discrepancy between nested grids is 0.00795352933 (0.79535%), exceeding the 0.005 (0.5%) gate. The common-grid relative L2 discrepancy is 2.50306424e-6.
- Fine-grid time refinement gives maximum relative L2 discrepancy 5.54161170e-12 and peak discrepancy 1.04007004e-11. These small discrepancies do not cancel the failed peak grid screen.
- The retained implementation uses a NumPy Fourier integrating-factor RK4 reference. Its configuration contains neural training and CUDA fields, but this reference calculation does not instantiate a neural network.

Limits or outstanding work:
- Accuracy of the continuous spatial supremum is unresolved. The peak comparison samples each grid separately; it is not a certified continuum maximum.
- This is a fixed periodic domain. No domain-enlargement test, whole-space decay conclusion, global-existence theorem, or blowup finding follows.
- This optical model is preserved as research history and is not evidence for the active water-wave-dysthe-spatial-v1 baseline. Passing a reference screen would not establish PINN accuracy.

Evidence:
- [sequence-summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/results/long-reference-77502/sequence-summary.json)
- [long_time_reference.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/scripts/long_time_reference.py)
- [audit_reference.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/scripts/audit_reference.py)
- [reference.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/src/dysthe_pinn/reference.py)
- [long_t2.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/configs/long_t2.json)
- [long_t8.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/configs/long_t8.json)
- [review.png](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/long-reference-77502/review.png)

<a id="hist-optical-late-window-2048"></a>
### HIST-OPTICAL-LATE-WINDOW-2048 — Historical optical fine-step trajectory to T=2048 and descriptive local oscillation fit

**Date:** 2026-09-18. **Basis:** The retained report.tex is dated 18 September 2026; the public review turn 01a0b558-b1ba-7192-8bc4-6a1df4d36778 has the same local date. This dates the report/review, not an independently logged start timestamp..

**Model:** Dysthe3D-1.27: historical three-coordinate optical equation, periodic cube of side length 12; amplitude 0.3 cosine-power packet. **Status:** completed_unvalidated; descriptive fit completed.

- The trajectory integrates from t=0 to 2048 on a 64^3 grid with dt=0.01, 204800 steps, and 257 saved frames in the observation window [1024,2048]. It does not reset the initial packet at t=1024.
- The retained summary reports 18421.4701 seconds (5.1171 hours), maximum relative mass drift 7.39085032e-12, and maximum retained spectral-edge fraction 3.27698233e-18.
- Across integer diagnostic times in [1024,2048], the sampled peak ranges from 0.07376859 to 0.23707285, with mean 0.13071707. The fitted late log-log slope has R^2=0.0035077, so these samples do not support a useful single power-law decay fit.
- A separate local four-harmonic descriptive fit on [1536,1664] uses 129 samples, a fitted base period 11.48213, RMSE 0.00513424, and R^2=0.9849756. Withheld points selected the harmonic count before refitting all points.
- The original implementation is NumPy CPU reference integration. CUDA and network configuration entries are retained provenance; this run supplies no new long-time PINN prediction.

Limits or outstanding work:
- Long-time field and peak accuracy remain unresolved: the saved qualification explicitly records no grid/time refinement and unknown accumulated error before the observation window. Small mass drift is not a field-error bound.
- The harmonic fit is local description, not an independent test, a future-time forecast, a new PDE solution, or proof of a breather, soliton, recurrence, or asymptotic law.
- Periodic confinement and a mass-dependent lower bound obstruct interpreting the ordinary maximum as whole-space decay to zero. This historical optical trajectory is not active water-wave evidence.
- Production field/checkpoint arrays are not present in the inspected results directory; the archive preserves diagnostic summaries and code, rather than claiming full raw-field reproducibility.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/results/late-window-1024-2048/summary.json)
- [settings.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/results/late-window-1024-2048/settings.json)
- [review-statistics.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/reports/late-window-review/review-statistics.json)
- [oscillation-fit.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/reports/late-window-review/oscillation-fit.json)
- [fit_oscillations.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/reports/late-window-review/fit_oscillations.py)
- [report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-pinn/reports/late-window-review/report.tex)
- [late_window.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/src/dysthe_pinn/late_window.py)
- [reference.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/src/dysthe_pinn/reference.py)

<a id="hist-optical-preview-10321"></a>
### HIST-OPTICAL-PREVIEW-10321 — Historical optical coarse breathing preview: T=12288 target stopped at t=10321

**Date:** 2026-09-18. **Basis:** Dated public review turn 01a0b5c4-c0f4-70d3-851e-023e1d95bfe1 and the retained 18 September 2026 report. The run summary contains elapsed duration but no wall-clock start date..

**Model:** Dysthe3D-1.27: historical three-coordinate optical equation, periodic cube of side length 12; separate 32^3 coarse-grid preview. **Status:** failed_diagnostics; stopped at t=10321 before target T=12288.

- The separate preview uses dt=0.5 and 32^3 points, starts from t=0, targets T=12288, and records a detailed [1500,2500] observation window plus showcase windows.
- The retained summary reports 20642 steps, 726 saved frames, and 121.2381 seconds before stopping at t=10321. It leaves 3934 planned steps uncompleted.
- Maximum relative mass drift reaches 0.00100007306 (0.1000073%), exceeding the 0.001 stop threshold. Maximum recorded spectral-edge fraction is 2.65134688e-6.
- The retained focus-window statistics report peak values from 0.07372305 to 0.23691754 and effective-volume values from 164.36659 to 924.40993, with peak-volume correlation -0.9134428. These describe oscillatory concentration in the preview.
- The report records at most 1.04% sampled-peak disagreement with the earlier fine-step run at common integer times 1500 through 2048. This comparison changes the grid and time step together.

Limits or outstanding work:
- The operational mass-drift stop is a numerical diagnostic failure, not evidence of PDE blowup or loss of solution existence.
- Long-time field accuracy is unresolved, particularly beyond t=2048. The overlap check does not separate spatial and temporal errors or validate the complex field.
- Breathing-like concentration diagnostics do not establish a localized breather or soliton, and the trajectory is not a long-time PINN result.
- This is historical optical evidence on a periodic domain, not the active water-wave model or a whole-space decay test. Production frame arrays are not present in the inspected results directory.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/results/breathing-preview-12288/summary-selected-fields.derived.json)
- [settings.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/results/breathing-preview-12288/settings.json)
- [preview-statistics.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/reports/late-window-review/preview-statistics.json)
- [preview_addition.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-pinn/reports/late-window-review/preview_addition.tex)
- [build_preview_addition.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/reports/late-window-review/build_preview_addition.py)
- [late_window.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/src/dysthe_pinn/late_window.py)
- [breathing.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/src/dysthe_pinn/breathing.py)
- [breathing_preview.slurm](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-pinn/cluster/breathing_preview.slurm)

<a id="doc-project-overview"></a>
### DOC-PROJECT-OVERVIEW — Nontechnical overview of the project and numerical/PINN methods

**Date:** 2026-09-23. **Basis:** Dated project-chat delivery and historical publication commit.

**Model:** Historical mixed-model overview; models retain separate identities. **Status:** Completed communication artifact.

- Six-page equation-free overview with four figures explains numerical evolution, PINN fitting and the original research questions.

Limits or outstanding work:
- Communication material does not supply new solver validation or generalization evidence.

Evidence:
- [dysthe-project-overview.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-pinn/output/pdf/dysthe-project-overview.pdf)

<a id="doc-research-reset"></a>
### DOC-RESEARCH-RESET — Retrospective of earlier Dysthe experiments and research reset

**Date:** 2026-09-24. **Basis:** Dated project chat and original report; a review date, not a simulation timestamp.

**Model:** Separately labeled historical optical, canonical and water-wave formulations. **Status:** Completed retrospective report; later active-scope decision supersedes optical proposals.

- Ten-page retrospective with four vector figures and nine annotated references records the mismatch between original decay/stability questions and the available finite-window evidence. It preserves failed resolution checks and single-input PINN limitations.

Limits or outstanding work:
- Historical optical future-work suggestions are superseded by the September 30 water-wave-only scope decision.

Evidence:
- [report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-pinn/reports/dysthe-research-reset/report.tex)
- [dysthe-research-reset.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-pinn/output/pdf/dysthe-research-reset.pdf)

<a id="spatial-scope-2026-09-30"></a>
### spatial-scope-2026-09-30 — Versioned water-wave spatial model and repository contracts

**Date:** 2026-09-30. **Basis:** Git commit author date; administrative/model-contract milestone, not an experiment run.

**Model:** water-wave-dysthe-spatial-v1. **Status:** implemented.

- The approved active equation is the one-coordinate spatial free-surface Dysthe model, with xi as propagation distance and tau as retarded time. Scope guards prevent silently mixing model formulations.

Evidence:
- [model.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-core/docs/model.md)
- [scope.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-core/scope.json)
- [SCOPE.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/SCOPE.md)

<a id="spatial-solitary-smoke-2026-10-01"></a>
### spatial-solitary-smoke-2026-10-01 — Bounded solitary-profile propagation and unrestricted perturbation smoke

**Date:** 2026-10-01. **Basis:** Explicit completed-smoke date in docs/solitary-pilot.md.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed smoke.

- Three trajectories reach xi = 0.1 at epsilon = 0.025, using 34 profile iterations and 240 total propagation steps. The full profile residual is 2.0337e-11 and the control raw L2 error is 7.0939e-11. These results do not establish stability.

Limits or outstanding work:
- Grid, step and domain checks, together with signed unrestricted perturbations, are needed at meaningful horizons.

Evidence:
- [solitary-pilot.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/docs/solitary-pilot.md)
- [report.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/external/solitary-smoke-2026-10-01/solitary-smoke-001/report.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/external/solitary-smoke-2026-10-01/verification.json)

<a id="spatial-solitary-gate1-2026-10-02"></a>
### spatial-solitary-gate1-2026-10-02 — Solitary branch epsilon=0.025 grid/step/domain campaign

**Date:** 2026-10-02. **Basis:** started_utc and updated_utc in each retained status JSON.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed computations.

- Base, step-refined, grid-refined and enlarged-domain cases each reach xi = 20 with seven control or perturbed trajectories. A grid-run interruption was retained and followed by a successful restart. Completion alone does not qualify the domain response; the October 16 analysis provides that assessment.

Evidence:
- [e0.025-base-status.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/runs/20261002-e025-gate1-001/e0.025-base-status.json)
- [e0.025-step-status.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/runs/20261002-e025-gate1-001/e0.025-step-status.json)
- [e0.025-grid-status.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/runs/20261002-e025-gate1-001/e0.025-grid-status.json)
- [e0.025-domain-status.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/runs/20261002-e025-gate1-001/e0.025-domain-status.json)
- [report.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/runs/20261002-e025-gate1-001/e0.025-base/report.json)

<a id="doc-1979-guide"></a>
### DOC-1979-GUIDE — Before Reading Dysthe 1979: prerequisite guide

**Date:** 2026-10-03. **Basis:** verification.json date and guide.tex date.

**Model:** Original temporal potential-envelope derivation and stability formulas; separately mentions later spatial free-surface model. **Status:** completed pedagogical report.

- The guide has 31 pages, 13 modules, 14 exercises and four vector figures. It flags a coefficient inconsistency without claiming an authenticated erratum.

Limits or outstanding work:
- Illustrations and reduced formulas are not new empirical validation.

Evidence:
- [guide.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-1979-prerequisite-guide/guide.tex)
- [verification.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-1979-prerequisite-guide/verification.json)
- [dysthe-1979-prerequisite-guide.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-1979-prerequisite-guide.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
pdflatex guide.tex
```

<a id="spatial-custom-envelope-2026-10-16"></a>
### spatial-custom-envelope-2026-10-16 — Restricted complex-envelope formula editor and CPU execution

**Date:** 2026-10-16. **Basis:** checked_utc=2026-10-16T19:08:55.232239+00:00 in validation-summary.json.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed software and smoke.

- Checks include 13 parser tests, 20,000 fuzz samples without unexpected exceptions, nine custom integration tests, six simulator regressions and 16 installed-browser checks. Two tiny solves with N = 256, L = 40 and xi_end = 0.005 exercise custom formulas. No custom-input convergence campaign was performed.

Evidence:
- [validation-summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/custom-envelope-20261016/evidence/validation-summary.json)
- [core-preservation.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/custom-envelope-20261016/evidence/core-preservation.json)
- [formula-e2e.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/custom-envelope-20261016/evidence/formula-e2e.json)
- [custom-envelope.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/docs/custom-envelope.md)

<a id="spatial-reference-stage1-2026-10-16"></a>
### spatial-reference-stage1-2026-10-16 — Stage-one analytic controls and response-relative domain refinement

**Date:** 2026-10-16. **Basis:** Report date and dated task evidence directory.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed bounded validation.

- Controls cover analytic NLS and plane-wave solutions, a moving profile, a signed odd perturbation, and independent grid, step and domain comparisons. Sampled 1 percent response-relative domain horizons are xi = 5 for L = 160 versus 320, xi = 10 for L = 320 versus 640, and xi = 20 for L = 640 versus 1280. The final L = 640 versus 1280 discrepancy-to-response ratio is 0.0053783. FNO training was explicitly a no-go at that stage.

Limits or outstanding work:
- This is case-specific simulator qualification. It does not transfer to broad data-generation qualification.

Evidence:
- [stage-one-reference.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/docs/stage-one-reference.md)
- [decision.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/external/stage-one-2026-10-16/decision.json)
- [report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/external-stage-one-2026-10-16/report/report.tex)
- [report.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/external-stage-one-2026-10-16/report/report.pdf)

<a id="spatial-small-simulator-2026-10-16"></a>
### spatial-small-simulator-2026-10-16 — Three-input numerical simulator demonstration

**Date:** 2026-10-16. **Basis:** Report date and dated evidence directory.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed bounded validation.

- A solitary profile, a localized 2 percent perturbation and a complex Gaussian were each independently checked through xi = 4. Two-level grid, step and domain comparisons pass the declared demonstration gates. Each of the three cases has 81 snapshots. Numerical field export, desktop and mobile controls, and a bounded fresh CPU solve were checked. Custom cases remain exploratory.

Limits or outstanding work:
- New initial profiles need their own grid/step/domain qualification.

Evidence:
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/small-simulator-review-20261016/verification.json)
- [report.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/small-simulator-review-20261016/report/report.pdf)
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/runs/small-simulator-20261016/summary.json)
- [small-simulator.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/docs/small-simulator.md)

<a id="doc-existence-review"></a>
### DOC-EXISTENCE-REVIEW — Dysthe evolution: numerical evidence and existence

**Date:** 2026-10-23. **Basis:** verification.json and review.tex date.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed literature/math review.

- The 12-page review covers the 1979 paper and the supplied 2026 preprint. It distinguishes finite-Galerkin and global-ODE statements, residual controls, and infinite-dimensional existence. It includes no new propagation or neural training.

Limits or outstanding work:
- No continuum existence certificate.

Evidence:
- [review.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-existence-review/review.tex)
- [verification.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-existence-review/verification.json)
- [dysthe-existence-review.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-existence-review.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
pdflatex review.tex
```

<a id="doc-nls-pinn-literature"></a>
### DOC-NLS-PINN-LITERATURE — NLS and physics-informed learning review

**Date:** 2026-10-25. **Basis:** Literature cutoff in README/report and verification.json.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed targeted literature review.

- The 20-page review has 28 bibliography entries and proposes an experimental program for spatial water-wave Dysthe. General Schrodinger learning provides methodological context.

Limits or outstanding work:
- The reviewed paper experiments, code and HOS data were not rerun. Sample sizes and thresholds are proposals.

Evidence:
- [report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/nls-pinn-research-2026-10-25/report.tex)
- [verification.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/nls-pinn-research-2026-10-25/verification.json)
- [nls-pinn-research-2026-10-25.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/nls-pinn-research-2026-10-25.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
pdflatex report.tex
```

<a id="doc-operator-protocol"></a>
### DOC-OPERATOR-PROTOCOL — Learning Dysthe evolution across initial wave fields

**Date:** 2026-10-25. **Basis:** verification.json and review.tex date.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed literature-grounded protocol.

- The 18-page protocol defines multi-input FNO/PINO and per-field PINN comparisons, exact-equation controls, and long-distance evaluation. Only arithmetic checks were executed.

Limits or outstanding work:
- Protocol is proposed; this report trained no model.

Evidence:
- [review.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-operator-learning-review/review.tex)
- [verification.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-operator-learning-review/verification.json)
- [dysthe-operator-learning-review.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-operator-learning-review.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
pdflatex review.tex
```

<a id="spatial-cpu-pilot-2026-10-26"></a>
### spatial-cpu-pilot-2026-10-26 — Matched FNO/PINO and per-inlet spectral PINN pilot

**Date:** 2026-10-26. **Basis:** Dated report/result directory and publication commit; exact execution timestamp not serialized.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed pilot.

- FNO and PINO fail all held-out short-horizon and rollout accuracy gates. Four-slab per-inlet PINNs pass all six test case-seed pairs through xi = 2, with worst relative L2 error 0.009629655, H1 error 0.018814047 and peak error 0.010894324. The coarse numerical solve remains faster and more accurate. Per-inlet PINNs do not establish operator generalization.

Limits or outstanding work:
- Frozen held-out evaluation, CPU/CUDA parity and a full-cost comparison are needed before making an A100 claim.

Evidence:
- [report.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-experiments/results/cpu-pilot-2026-10-26/report.tex)
- [report.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/dysthe-experiments/results/cpu-pilot-2026-10-26/report.pdf)
- [protocol.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/cpu-pilot-2026-10-26/protocol.json)
- [environment-cpu.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/cpu-pilot-2026-10-26/environment-cpu.json)
- [aggregate-errors.csv](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/cpu-pilot-2026-10-26/data/aggregate-errors.csv)
- [timings.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/cpu-pilot-2026-10-26/data/timings.json)

<a id="spatial-gpu2-campaign-2026-10-26"></a>
### spatial-gpu2-campaign-2026-10-26 — GPU2 long-distance campaign: retained reference successes and PINN failures

**Date:** 2026-10-26. **Basis:** Campaign/export directory label; published2026-10-27 at723883f. Exact scheduler execution timestamps unavailable in committed metadata..

**Model:** water-wave-dysthe-spatial-v1. **Status:** partly completed with failed gates.

- Of 72 tasks, 24 completed, 28 stopped at a gate, 12 had execution errors and eight were not applicable. All 12 reference cases report qualification through xi = 64. All 24 evaluated packet or sideband PINN case-seed pairs fail the combined L2/H1/H2/peak gate at xi = 4. All 12 random-family PINN tasks have execution errors. The worst H2 validation and test errors are 0.30741433 and 0.22115310. Four packet domain tasks stop at xi = 8. Periodic qualification through xi = 64 does not qualify isolated packets.
- Positive GPU memory records support CUDA execution. The exact A100 model, driver, node and scheduler allocation are unavailable in the published contents. Each of the 24 PINN fits reports 94955520 peak GPU bytes.
- The per-fit sampled_interval_pass flag omits H2 and must not replace the authoritative long-distance status. Raw trajectories, checkpoints and 1097 hash-listed detailed JSON files remain outside the published snapshot.

Limits or outstanding work:
- Publish compact detailed diagnostics and hardware/job records, validate the H2 repair, and retain the examined old test cases as regressions.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/long-distance-gpu2-2026-10-26/summary.json)
- [manifest.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/long-distance-gpu2-2026-10-26/manifest.json)
- [identity.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/long-distance-gpu2-2026-10-26/identity.json)
- [gpu-provenance-audit.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-solitons-tests-2026-10-27/data/gpu-provenance-audit.json)

<a id="spatial-long-workflow-2026-10-26"></a>
### spatial-long-workflow-2026-10-26 — Staged distance workflow and CPU execution smoke

**Date:** 2026-10-26. **Basis:** Result-directory/report/commit date.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed workflow smoke.

- Reference targets xi = 4, 8, 16, 32 and 64 and PINN targets xi = 4, 8 and 16 were prepared. A tiny CPU workflow through xi = 0.2 has 24 tasks: 17 completed, three stopped at scientific gates and four were not applicable. Restart and replay evidence is retained. This smoke run does not execute the target horizons.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/long-distance-workflow-2026-10-26/summary.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/long-distance-workflow-2026-10-26/verification.json)
- [long-distance-a100.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/configs/long-distance-a100.json)
- [long-distance.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/docs/long-distance.md)

<a id="spatial-reference-torch-2026-10-26"></a>
### spatial-reference-torch-2026-10-26 — Verified periodic reference and differentiable Torch adapter

**Date:** 2026-10-26. **Basis:** Publication commit date and CPU-pilot verification record.

**Model:** water-wave-dysthe-spatial-v1. **Status:** implemented and tested.

- Saved verification reports 32 passing core tests. The shared Fourier reference and differentiable nonlinear right-hand side form the numerical baseline. Passing consistency tests does not prove continuum well-posedness.

Evidence:
- [reference-validation.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-core/docs/reference-validation.md)
- [spatial.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-core/src/dysthe_core/reference/spatial.py)
- [torch_spatial.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-core/src/dysthe_core/torch_spatial.py)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/dysthe-experiments/results/cpu-pilot-2026-10-26/verification.json)

<a id="doc-solitons-published-tests"></a>
### DOC-SOLITONS-PUBLISHED-TESTS — Dysthe solitary waves and published tests

**Date:** 2026-10-27. **Basis:** Review date and revised_at_utc in verification.json.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed revised review of published cluster snapshot.

- The 14-page report archives 29 result files from commit 723883f27a6b3489bfc36f55d9d15b52e8635ad0 and checks 28 metadata hashes. It adds a bounded projection calculation on a historical profile.

Limits or outstanding work:
- The reviewer submitted no HPC job. The original cluster snapshot lacks detailed H2, reference and random-exception evidence, along with exact GPU identification. The report provides no new solitary-wave propagation result.

Evidence:
- [README.txt](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-solitons-tests-2026-10-27/README.txt)
- [verification.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-solitons-tests-2026-10-27/verification.json)
- [review.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-solitons-tests-2026-10-27/review.tex)
- [projection-audit.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-solitons-tests-2026-10-27/data/projection-audit.json)
- [dysthe-solitons-tests-2026-10-27.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-solitons-tests-2026-10-27.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python make_figures.py
pdflatex review.tex
```

<a id="spatial-h2-random-repair-2026-10-27"></a>
### spatial-h2-random-repair-2026-10-27 — Random-inlet identity repair and spectral PINN conditioning ablation

**Date:** 2026-10-27. **Basis:** Dated CPU repair evidence and publication commits.

**Model:** water-wave-dysthe-spatial-v1. **Status:** completed cpu validation gpu rerun pending.

- Random-input failures reproduce last-bit differences across BLAS implementations when inputs are independently regenerated. Canonical arrays are now reused. The paired CPU ablation uses all K = 48 coefficients and scaling by 1/(1+k²), preserving the model and its expressivity. At xi = 4, with eight slabs, 400 updates per slab, one validation inlet per family and seed 11, all three unscaled cases fail and all three scaled cases pass the unchanged gates.
- H2 error fractions change from 0.26111873 to 0.01465812 for packets, from 0.12107568 to 0.00654749 for sidebands, and from 0.15850481 to 0.00215562 for random inputs. These are validation-selection results, not untouched-test generalization.
- All 72 software tests pass. The corrected export has 233 metadata files and 181 raw artifacts, with zero missing files and zero integrity findings. Repaired A100 accuracy and throughput have not been verified.

Limits or outstanding work:
- Run the frozen scaled and unscaled GPU candidate/control comparison, check CPU/CUDA parity, and evaluate fresh untouched test inlets with multiple seeds before qualifying longer distances.

Evidence:
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/h2-repair-2026-10-27/README.md)
- [full-horizon-ablation.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/h2-repair-2026-10-27/full-horizon-ablation.json)
- [random-failure-diagnosis.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/h2-repair-2026-10-27/random-failure-diagnosis.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/results/h2-repair-2026-10-27/verification.json)
- [h2-rerun.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/worktrees/h2-rerun/experiments/docs/h2-rerun.md)

<a id="doc-modelling-report"></a>
### DOC-MODELLING-REPORT — Numerical evidence and a PINN research framework

**Date:** 2026-10-30. **Basis:** main.tex and verification-report.json date.

**Model:** Temporal potential Dysthe primary plus separately labelled existing spatial PINN evidence. **Status:** completed research report.

- The 20-page report includes 12 vector figures. It combines temporal solver, refinement, modulational-instability and bandwidth evidence with spatial PINN phase and curvature analysis and a cluster handoff.

Limits or outstanding work:
- Portable arrays are display products, not full-grid reference truth; no new temporal training.

Evidence:
- [main.tex](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-modelling-report-2026-10-30/main.tex)
- [verification-report.json](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-modelling-report-2026-10-30/verification-report.json)
- [dysthe-modelling-report-2026-10-30.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-modelling-report-2026-10-30.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
pdflatex main.tex
```

<a id="temp-domain-representation"></a>
### TEMP-DOMAIN-REPRESENTATION — Temporal packet domain checks and neural representation floors

**Date:** 2026-10-30. **Basis:** Dated experiment-plan and verification records.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1. **Status:** completed CPU diagnostics.

- Four packet domain comparisons through T = 8 pass, with maximum common-interval H1 difference 0.00076044. Projection floors were measured at T = 2, 4, 8 and 16. K = 48 is inadequate for late temporal neural targets.

Limits or outstanding work:
- The public supplement --domain CLI targets T = 16; it is not the reproduction entry for the historical T = 8 record. Projection checks are not trained-model results.

Evidence:
- [domain-checks.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/results-refined/domain-checks.json)
- [representation-windows.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/representation-windows.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/verification.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python representation_windows.py
```

<a id="temp-h2-timestep-repair"></a>
### TEMP-H2-TIMESTEP-REPAIR — Temporal high-steepness sideband timestep audit

**Date:** 2026-10-30. **Basis:** Dated primary-results/report package.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1. **Status:** completed CPU numerical repair.

- For a sideband with epsilon = 0.1 at T = 16, a fine step of 0.0003125, with independent comparisons at step 0.000625 and N = 2048, reduces the apparent maximum H2 amplification from about 600.6 to 28.41724. All earlier failures are retained.

Limits or outstanding work:
- Repair concerns the numerical time step, not a proof of PDE regularity.

Evidence:
- [primary-results.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/primary-results.json)
- [result.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/results-time-audit/result.json)
- [rerun-verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/rerun-verification.json)
- [rerun_time_audit.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/rerun_time_audit.py)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python rerun_time_audit.py --output fresh-time-audit
```

<a id="temp-linear-1024"></a>
### TEMP-LINEAR-1024 — Direct periodic linear evolution through T = 1024

**Date:** 2026-10-30. **Basis:** DELIVERY-VERIFICATION.json and dated package.

**Model:** dysthe-1979-temporal-potential-1d-free-linear-control-v1. **Status:** completed CPU exact-discrete-propagator experiment.

- Three initial profiles were evaluated directly using the Fourier phase. Mode-power, action and refined spatial-peak checks pass through the selected T = 1024 snapshot.

Limits or outstanding work:
- These are periodic linear data, not evidence for nonlinear evolution to T = 1024 or isolated-packet decay.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/data/long-linear/summary.json)
- [long_linear.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/long_linear.py)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python long_linear.py --data fresh-data --output fresh-data/long-linear
```

<a id="temp-long-horizon-targets"></a>
### TEMP-LONG-HORIZON-TARGETS — Periodic and isolated nonlinear horizon ladder to T = 1024

**Date:** 2026-10-30. **Basis:** long_horizon/verification.json date.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1. **Status:** implemented and smoke-tested; production horizons not executed.

- Targets are T = 16, 32, 64, 128, 256, 512 and 1024. Periodic cases include Gaussian, random and two-packet inputs; isolated cases include Gaussian and two-packet inputs. Seven software tests pass. Two tiny Gaussian tracks pass T = 0.02 and 0.04. A failed monitor blocks later horizons.

Limits or outstanding work:
- This work is CPU-only, with no cluster submission. Cost extrapolations exclude diagnostics, retries and future refinement. Automatic restart is not implemented.

Evidence:
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/long_horizon/README.md)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/long_horizon/verification.json)
- [periodic-targets.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/long_horizon/configs/periodic-targets.json)
- [isolated-targets.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/long_horizon/configs/isolated-targets.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python long_horizon/run_long_horizon.py --config long_horizon/configs/periodic-targets.json --output fresh-periodic
python long_horizon/run_long_horizon.py --config long_horizon/configs/isolated-targets.json --output fresh-isolated
```

<a id="temp-mi-controls"></a>
### TEMP-MI-CONTROLS — Complex growth and phase check for temporal modulational instability

**Date:** 2026-10-30. **Basis:** Dated experiment-plan/package; temporal-mi-check.json has source/runtime provenance.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1 and dysthe-1979-temporal-potential-1d-literal-v1. **Status:** completed CPU control.

- Four coefficient/epsilon pairs each have three refinement trajectories through T = 4. Complex growing-mode, padded-right-hand-side and semidiscrete mass checks pass. Wrong-coefficient phase negative controls are rejected.

Limits or outstanding work:
- Growth alone does not distinguish c = 1 from c = 3/2. The test covers a tiny perturbation about one wavetrain.

Evidence:
- [temporal-mi-check.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/temporal-mi-check.json)
- [temporal-mi-check.csv](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/temporal-mi-check.csv)
- [mi_check.py](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/mi_check.py)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python mi_check.py --output-dir fresh-mi
```

<a id="temp-near-zero"></a>
### TEMP-NEAR-ZERO — Very-early nonlinear evolution and Gaussian cutoff audit

**Date:** 2026-10-30. **Basis:** DELIVERY-VERIFICATION.json and dated package.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1. **Status:** completed CPU experiment.

- The sampled times are 0, 1e-4, 1e-3 and 1e-2. Eight nonlinear Dysthe/NLS cases pass across three profiles plus a high-cutoff Gaussian. The initial Gaussian discrepancy is 3.77e-9 at cutoff 12 and falls to roundoff at cutoff 24.

Limits or outstanding work:
- Magnified tails require initial-projection control; no global-existence conclusion.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/data/near-zero/summary.json)
- [gaussian-tail-audit.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/data/gaussian-tail-audit.json)
- [early-late-verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/data/early-late-verification.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python audit_initial_tails.py --data fresh-data
python near_zero.py --data fresh-data --output fresh-data/near-zero
```

<a id="temp-reference-t16"></a>
### TEMP-REFERENCE-T16 — Original temporal Dysthe multi-profile numerical proof of concept

**Date:** 2026-10-30. **Basis:** experiment-plan.json date and dated report/package.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1. **Status:** completed CPU primary reference through T16.

- Packet, sideband and random profiles were tested at epsilon = 0.05 and 0.1. Six primary c = 3/2 trajectories qualified. Literal c = 1, NLS and mean-flow-only controls are separately versioned. The initial N = 4096 audit passed 21 of 24 cases. Two nonprimary high-epsilon controls remain unresolved after the primary repair.

Limits or outstanding work:
- Temporal potential model is separate from active spatial free-surface baseline; no temporal PINN/FNO or cluster execution.

Evidence:
- [README.md](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/README.md)
- [primary-results.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/primary-results.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/verification.json)
- [experiment-plan.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-original-poc-2026-10-30/experiment-plan.json)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python run.py --config config-audit.json --output fresh-audit
```

<a id="temp-visual-t4"></a>
### TEMP-VISUAL-T4 — Nonlinear envelope visual companion across three initial profiles

**Date:** 2026-10-30. **Basis:** DELIVERY-VERIFICATION.json and report date.

**Model:** dysthe-1979-temporal-potential-1d-stability-sign-v1. **Status:** completed CPU numerical visualization.

- Gaussian, smooth random and phase-offset two-packet inputs were compared under Dysthe, NLS and exact free-linear evolution through T = 4. Six nonlinear cases pass independent spatial and time checks. Outputs include a seven-page report, nine vector figures and an 81-frame animation.

Limits or outstanding work:
- The illustrative carrier is not physical surface elevation. The 3D plots show position, time and magnitude.

Evidence:
- [summary.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/data/summary.json)
- [verification.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/data/verification.json)
- [DELIVERY-VERIFICATION.json](https://github.com/matasvai/dysthe-experiments/blob/codex/research-record-2026-11-05/archive/2026-11-05/source/output/dysthe-nonlinear-visuals-2026-10-30/DELIVERY-VERIFICATION.json)
- [dysthe-nonlinear-visual-gallery-2026-10-30.pdf](https://github.com/matasvai/dysthe-paper/blob/codex/research-record-2026-11-05/research-record/2026-11-05/documents/output/pdf/dysthe-nonlinear-visual-gallery-2026-10-30.pdf)

Recorded reproduction commands (run in their original package directory; some require retained data):
```sh
python run_visual_cases.py --output fresh-data
python make_visuals.py --animate
```
