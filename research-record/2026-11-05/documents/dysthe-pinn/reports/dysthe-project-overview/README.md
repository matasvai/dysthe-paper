# The Dysthe Project: a plain-language progress report

A six-page introduction for a reader with almost no mathematics or STEM
background. It covers work reviewed through 23 September 2026: early wave
spreading, nonlinear pulses and collisions, long optical simulations, the
optical PINN, kinetic-plasma FNO campaigns, and the supporting research tools.

- [Read the PDF](../../output/pdf/dysthe-project-overview.pdf)
- [Download the editable source bundle](../../output/pdf/dysthe-project-overview-source.zip)
- [Edit the LaTeX](report.tex)

The report uses everyday analogies, four vector figures, a short glossary,
and no equations. It separates numerical observations from established
results, distinguishes the optical, water-wave and plasma models, and
discloses unsuccessful tests as well as bounded successes. It reviews
archived experiments; no new simulation or training is claimed.

## Build

From this directory, compile the included source and figure PDFs:

```bash
tectonic report.tex
```

Alternatively, use a current LaTeX installation with `pdflatex report.tex`.
The delivered PDF was built and checked with Tectonic. The style and all
figure files are included; compilation does not require the original runs.

To redraw the four vector figures, install NumPy and Matplotlib, then run:

```bash
python3 build_figures.py
tectonic report.tex
```

`build_figures.py` uses only the included `overview_data.json`. That snapshot
contains the plotted numbers, headline numerical claims, and SHA-256 hashes
of the project records from which they came. It makes figure regeneration
portable without copying large training files.

`collect_evidence.py` refreshes that snapshot from the complete Dysthe
workspace, where this repository is the `dysthe-pinn` subdirectory. It is
provided for traceability, but is not needed for compilation or figure
regeneration. Some earlier wave records are outside this Git repository;
the exported snapshot is deliberately retained here.

## Interpretation and checks

- Figure 1 plots peak magnitude and integrated squared magnitude, each
  normalized to its own starting value. The second quantity is called a
  wave-content measure; the report does not identify it with heating or
  with total physical energy.
- Figure 2 uses only the optical stripe interval through simulation time 4
  supported by the archived refinement comparison. Its percentage measures
  transverse variation, not a change in peak height.
- Figure 4 compares the 24-step and 12-step models within study 78140.
  Particle and electric-field changes use the mean errors on the 44 fresh
  cases, averaged across the three training seeds. The energy change uses
  the worst drift across all 48 cases and three seeds. These are deliberately
  different summaries, labeled average errors and worst energy imbalance
  in the report. The figure is not a cross-campaign comparison.
- The 0.67% optical PINN figure is the maximum sampled relative L2 field
  error on its short evaluation interval, for one prescribed initial
  condition. It is not a guaranteed bound for every point or new problem.
- All six pages were rendered and visually inspected. Text extraction,
  vector-only figures, source hashes, and portable compilation were checked.
  `verification.json` records the checks and final PDF hash.

The report's numerical conclusions rest on the archived analyses and data,
not an independent rerun of the original physics or AI jobs. The source
bundle can reproduce the report and its plots, not the full experiments.
