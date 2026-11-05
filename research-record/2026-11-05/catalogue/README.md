# Editable dated work catalogue

`main.tex` is the editable report and `royden-report.sty` is its local style. `main.pdf` is the visually checked 15-page compilation dated 5 November 2026. It links the full experiment and chat indexes; the original reports live in `../documents/`.

Build with XeLaTeX twice from this directory:

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Required fonts are Latin Modern Roman and Liberation Serif. The latter preserves a Cyrillic character in one original chat title. Standard TeX packages include fontspec, microtype, longtable, array, needspace and those loaded by the local style. This source requires XeLaTeX or a compatible Unicode engine; the desktop editor default PDFLaTeX build is unsuitable.

The new catalogue was compiled and every rendered page inspected. Original archived report sources were checked for copied-file identity and literal dependencies but were not all rebuilt or scientifically revalidated. No new numerical experiment or training run is claimed by this publication.
