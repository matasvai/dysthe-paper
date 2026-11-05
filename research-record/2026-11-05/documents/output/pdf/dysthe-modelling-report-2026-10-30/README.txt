Dysthe modelling report — 30 October 2026

main.tex is the editable master. Figures are vector PDF; plotted diagnostics and plot arrays are under data/. All metrics are empirical and formulation-specific.

Compile in this directory with:
  pdflatex -interaction=nonstopmode -halt-on-error main.tex
  pdflatex -interaction=nonstopmode -halt-on-error main.tex

Requirements: a LaTeX installation with lmodern, amsmath, amsthm, mathtools, microtype, caption, booktabs, graphicx, hyperref, enumitem and standard packages.
The exported PDF was compiled with system pdfLaTeX, text-checked and visually inspected on all20pages. No unresolved references or overfull boxes remain. The app's separate live-preview compiler failed because its font map was unavailable and its Tectonic bundle could not download; this does not affect the delivered compiled PDF.

To regenerate the plotted figures from bundled data, use Python with NumPy, SciPy and Matplotlib, then:
  python make_spatial_figures.py
  python make_temporal_figures.py
  python make_temporal_bandwidth_figure.py
The MI figure is reproducible with mi_check.py in the separate proof-of-concept bundle.

Portable arrays are resampled display products; full-grid diagnostic values and source hashes are retained in JSON. Do not use these display arrays to recompute full-grid numerical acceptance tests. Full raw references remain in the local experiment directory; obtain or regenerate them for new numerical claims.

Read page1 for the meeting summary; pages4–8 for temporal findings,9–12 for spatial PINN evidence,13–15 for experiment design,16–18 for analytical interpretation and19 for the handoff. No new temporal PINN/FNO training or cluster execution is claimed.
