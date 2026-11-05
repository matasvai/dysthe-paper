# Before Reading Dysthe (1979)

This guide assumes PDE and linear algebra familiarity and teaches the
water-wave and asymptotic background from the beginning. Start with
Sections 2-5, then 6-7, and use Sections 8-10 beside the original paper.
Section 11 contains 14 exercises with answers. The guide is 31 pages.

## Files

- `guide.pdf`: compiled and visually checked guide.
- `guide.tex`: main editable LaTeX source.
- `sections/`: the 13 source modules, including two appendices.
- `royden-report.sty`: report formatting and mathematical environments.
- `figures/`: four original vector PDF figures.
- `make_figures.py`: optional figure regeneration; requires NumPy and Matplotlib.
- `verification.json`: provenance and verification record.

All LaTeX inputs and figure references are relative to this folder.
The guide can be compiled independently of the original paper PDF.

## Compile

From this directory, run `pdflatex -interaction=nonstopmode -halt-on-error guide.tex`
twice to resolve references and the contents table. A standard TeX Live
installation with the included packages is sufficient. Regenerating the
figures is optional; the required PDF figures are already included.

The app's built-in compiler was attempted but could not obtain its uncached
Tectonic bundle. The installed pdfLaTeX compiler successfully generated this
PDF. Live editor preview remains unverified; this source also uses supporting
files that the built-in standalone compiler may not support.

## Sources and limits

The primary source is the user-supplied scan of K. B. Dysthe, *Note on a
modification to the nonlinear Schrodinger equation for application to deep
water waves*, Proceedings of the Royal Society A 369 (1979), 105-114,
doi:10.1098/rspa.1979.0154. The supplied PDF contains a JSTOR cover plus
ten paper pages. Printed pages 105-114 correspond to PDF pages 2-11.
The original source is not duplicated in this package.

Section 8.3 and Appendix A flag apparent internal coefficient inconsistencies
in the supplied scan. The printed equation (2.19) is preserved; the main
stability derivation explicitly starts from the paper's printed (3.2)-(3.3).
No authoritative publisher correction was verified, and no solver equation
has been changed. This guide is pedagogical, not an implementation contract.

The guide derives the main prerequisite and stability calculations but does
not reproduce every nonlinear product in the paper's intermediate Q.
Full-equation and experimental comparisons are reported from the paper;
they have not been independently rerun or digitized. The four figures show
illustrations and reduced formulas, not new empirical water-wave evidence.
The later spatial free-surface model is identified separately in Appendix B.

Verification comprised successful compilation with no remaining warnings,
text and reference checks, visual inspection of all 31 pages, checks of key
algebraic identities, and confirmation that the figure PDFs contain no
raster images and that the report fonts are embedded. These checks do not
constitute a rigorous error theorem for the asymptotic model.
