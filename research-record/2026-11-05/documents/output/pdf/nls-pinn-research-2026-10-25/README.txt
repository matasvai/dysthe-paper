NONLINEAR SCHRODINGER EQUATIONS AND PHYSICS-INFORMED LEARNING
Literature cutoff: 25 October 2026 (America/New_York).

Open report.tex in a LaTeX editor. All required style, section, reference,
and figure files are supplied relative to this directory.

Compile from this directory with:
  pdflatex -interaction=nonstopmode -halt-on-error report.tex
  pdflatex -interaction=nonstopmode -halt-on-error report.tex
  pdflatex -interaction=nonstopmode -halt-on-error report.tex

The document includes references.tex directly. references.bib is also
provided for reuse; BibTeX is not required to compile this report.
Figures are already included as vector PDFs. To regenerate them:
  python3 make_figures.py
This optional step requires NumPy and Matplotlib.

Contents:
  report.tex                 Main editable LaTeX source
  sections/*.tex             Editable report sections
  royden-report.sty           Minimal mathematical report styling
  references.tex             Typeset bibliography
  references.bib             Reusable bibliographic entries
  figures/*.pdf              Original vector figures
  make_figures.py            Figure generation source
  *sources.json              Primary-source metadata and evidence ledgers
  verification.json          Final artifact checks and limitations
  report.pdf                 Compiled report

Evidence:
This is a targeted literature review and proposed experimental program.
No literature experiment, public training code, HOS data, or local solver
qualification campaign was rerun. Code/data availability was checked where
stated. Preview-only access and preprint status are identified. The figures
are analytic illustrations and proposed study diagrams, not trained results.
The elementary NLS estimate is explanatory, not a new research theorem.

The active proposed physics is water-wave-dysthe-spatial-v1.
General Schrödinger literature is algorithmic background only.
All experimental sample sizes, thresholds, and schedules are proposals.
