Dysthe Solitary Waves and the Published Tests
Review date: 27 October 2026
Revised after results publication 723883f27a6b3489bfc36f55d9d15b52e8635ad0.

Main source: review.tex
Compiled report: review.pdf
Style: royden-report.sty
Figures: figures/*.pdf (vector plots with embedded fonts)
Plot source: make_figures.py
Data/provenance: data/

Rebuild from this directory:
    python make_figures.py
    pdflatex -interaction=nonstopmode -halt-on-error review.tex
    pdflatex -interaction=nonstopmode -halt-on-error review.tex

NumPy and Matplotlib are needed only to regenerate the figures. The supplied
PDF figures suffice for a LaTeX rebuild without Python. A standard pdfLaTeX
installation with amsmath, amsthm, mathtools, geometry, graphicx, booktabs,
hyperref, lmodern, microtype, array, longtable and enumitem is required.

Evidence boundaries:
- data/cpu-errors.csv is copied from the published 26 October CPU pilot.
- data/workflow-summary.json is the tiny CPU workflow check, not an A100 run.
- data/long-distance-config.json is the proposed production configuration.
- data/remote-audit.json is the EARLIER pre-cluster-push audit and fresh isolated
  software check of the exact published experiments/core/learning commits.
- data/gpu2-snapshot/ archives all 29 files added in the new results commit.
- data/gpu-provenance-audit.json verifies 28 published metadata hashes and
  unchanged source hashes. It identifies the unpublished evidence required
  for independent checking of detailed reference and derivative-error claims.
- data/gpu-science-audit.json and data/gpu-old-gates-audit.json summarize the
  new coverage and the difference between older field-only gates and the full
  long-distance gate, which also checks H2 error.
- data/published-suite.log is the fresh 39-test verification log.
- data/projection-audit.json is a NEW bounded projection calculation on a
  historical solitary profile. It records its original path and checksums.
- data/projection-spectrum.csv contains normalized Fourier powers for that
  Dysthe profile and the analytic NLS seed. For r=0,1,2, multiply powers by
  (1+k^2)^r and take sqrt(discarded sum / total sum) to reproduce the floors.
- The raw solitary NPZ and historical neural PT/NPZ files are not bundled.
- No scientific propagation campaign was rerun and no A100 job was submitted
  by this review. New cluster records were reviewed, with detailed numerical
  diagnostics, hardware locks and random-family exception logs still absent
  from the pushed snapshot. Proposed solitary-study changes were not implemented.

The report distinguishes profile existence, spectral calculations,
finite-distance numerical robustness and global mathematical results.
See verification.json for artifact validation.
