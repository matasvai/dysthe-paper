# Returning to Dysthe

A ten-page retrospective of the original Dysthe experiments, reviewed on
24 September 2026. Plasma studies are outside this report's scope.

- [Read the PDF](../../output/pdf/dysthe-research-reset.pdf)
- [Download the editable source bundle](../../output/pdf/dysthe-research-reset-source.zip)
- [Edit the LaTeX](report.tex)

The report distinguishes the three-coordinate optical equation, canonical
linear dispersion experiments, and the separate spatial water-wave Dysthe
model. It covers successful and unsuccessful tests, questions never directly
tested, mathematical obstructions, priorities, and nine annotated primary
references. Four figures are vector PDFs.

Important corrections to the earlier overview: Gaussian-family weighted peak
searches extend through time 1024; the restricted-input pilot passes all 40
case-time screens when its two stored follow-ups are counted. These are
numerical consistency screens, not rigorous accuracy certificates.

## Rebuild

With Tectonic installed, run from this directory:

```bash
tectonic report.tex
```

The source, style and figure PDFs are self-contained. To regenerate figures,
install NumPy and Matplotlib and run:

```bash
python3 build_figures.py
tectonic report.tex
```

`evidence.json` contains compact plot data, selected numerical claims and
source-file hashes. `collect_evidence.py` refreshes it from the complete
Dysthe workspace, where this repository is the `dysthe-pinn` subdirectory.
The earlier wave records outside this Git repository are not needed to build
the report from the included snapshot.

`check_solver_agreement.py` documents the new, small comparison of the two
existing optical implementations. It requires both the outer `nonlinear`
package and this repository's `src` package; its docstring gives the command.
It is not a long-time accuracy test. No expensive simulations or training were
repeated for this review.

## Interpretation and verification

- Restricted-decay curves show derivative-weighted peaks, normalized separately
  at time 16. They must not be read as raw optical envelope amplitudes.
- The stripe figure shows transverse variation, not peak error or an established
  exponential instability rate. Only the checked interval through time 4 is shown.
- The periodic trace is an exploratory calculation; its action-imposed peak floor
  explains why it cannot certify decay to zero in an unbounded domain.
- PINN curves describe one training run and one initial field through time 0.5.
  They do not demonstrate operator generalization.
- The original six nonlinear tests, twelve nested optical workflow/physics tests,
  and cross-implementation microcheck passed during this review.
- The final PDF was compiled without LaTeX warnings, text-extracted, and all ten
  pages visually checked. No raster image objects occur in the final PDF.
- `verification.json` records the final checks and document hash. The source ZIP
  reproduces the document and figures; it does not reproduce every physics run.
