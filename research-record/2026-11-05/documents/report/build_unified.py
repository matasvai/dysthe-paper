from pathlib import Path
R=Path(__file__).resolve().parent
original=(R/'dysthe_report.tex').read_text()
refinement=(R/'decay_refinement.tex').read_text()
long=(R/'long_time_section.tex').read_text()
preamble=r'''\documentclass[10pt,letterpaper]{article}
\usepackage[margin=.75in]{geometry}
\usepackage{amsmath,amssymb,graphicx,booktabs,xcolor,hyperref,fancyhdr}
\definecolor{navy}{HTML}{18384B}\definecolor{teal}{HTML}{168F9A}\definecolor{pale}{HTML}{EAF4F4}
\hypersetup{colorlinks=true,linkcolor=teal,urlcolor=teal,pdftitle={Waves, dispersion and decay: a visual numerical study},pdfauthor={Dysthe numerical study}}
\pagestyle{fancy}\fancyhf{}\lhead{\small\color{navy}WAVES, DISPERSION AND DECAY}\rhead{\small\color{teal}Numerical study}\cfoot{\color{navy}\thepage}
\setlength{\headheight}{14pt}\setlength{\parindent}{0pt}\setlength{\parskip}{6pt}
\newcommand{\norm}[1]{\left\|#1\right\|}
\newcommand{\eyebrow}[1]{{\color{teal}\normalsize\bfseries #1}\par}
\newcommand{\takeaway}[1]{\par\smallskip\colorbox{pale}{\parbox{.96\linewidth}{\vspace{5pt}\textbf{Read this first.} #1\vspace{5pt}}}\par\smallskip}
\newcommand{\pic}[2]{\begin{center}\includegraphics[width=#1\linewidth]{#2}\end{center}}
\input{computed_values.tex}\input{refinement_values.tex}\input{long_time_values.tex}
\DeclareMathSizes{9}{10}{7}{5}
\DeclareFontShape{OT1}{cmr}{bx}{n}{<->cmbx10}{}
\begin{document}
\thispagestyle{empty}
\eyebrow{A VISUAL NUMERICAL STUDY / SEPTEMBER 2026}
{\color{navy}\Huge Waves, dispersion\\[4pt] and decay}\par
{\Large From individual crests to a three-dimensional decay test}
\pic{1}{visuals/hero.pdf}
\textbf{A wave inside its envelope.} The colored surface is an illustrative carrier
reconstruction on a slice of random seed 33 at $t=4$. The teal mesh follows its
positive envelope. Height means relative amplitude; this is not a third spatial
coordinate or a measured water surface.
\takeaway{The latest computation gives stronger spatial support for four candidate
peaks at $t=256$: all pass a 0.1\% stability screen. It does not yet establish a
sharper decay theorem or a counterexample.}
\textbf{The reading route}\par
\begin{tabular}{@{}ll@{}}
\textcolor{teal}{02--03} & Understand the envelope and the fluid analogy.\\
\textcolor{teal}{04--06} & Explore random 3D packets and the weighted diagnostic.\\
\textcolor{teal}{07--10} & Read the long-time results and the broader data collection.\\
\textcolor{teal}{11--18} & Inspect equations, numerical checks, and reproduction details.\\
\textcolor{teal}{19--22} & Explore the new research-motivated experiments.
\end{tabular}
\vfill
{\small Scope: linear optical dispersion and canonical weighted propagators associated
with the supplied Dysthe manuscript. The full nonlinear water-wave system is not simulated.}
\newpage
\eyebrow{01 / READING A WAVE}
\section*{The magnitude is the height of an envelope}
The complex envelope carries amplitude and phase. Its magnitude tells us how
large the local oscillations can be; it is not velocity. A carrier supplies the
rapid crests and troughs inside that slowly varying outline.
\pic{1}{figures/envelope_explanation.pdf}
\takeaway{The oscillating curve is the wave. The upper and lower outlines are
$+|E|$ and $-|E|$. A magnitude plot shows that outline, without drawing each crest.}
The schematic reconstruction is
\[u_{\rm carrier}=\operatorname{Re}\{E\,e^{i\phi_{\rm carrier}}\}.\]
Phase matters: two envelopes with the same magnitude can produce different crest
positions and different interference. The figures on page 5 retain the simulated
complex phase and add a visible carrier for illustration.

Optical intensity is proportional to $|E|^2$. A peak magnitude of $0.47$ corresponds
to about $0.22$ of the initial peak intensity when the initial amplitude is one.
Spreading can lower this peak while preserving the integral of $|E|^2$.

\textbf{Units and normalization.} Computations are dimensionless. The early optical
Gaussian examples start at peak one. Canonical decay inputs instead have $L^1=1$.
Their small numerical amplitudes reflect this different normalization and should
not be compared directly with the optical peaks.
\newpage
\eyebrow{02 / A FLUID ANALOGY}
\section*{What a packet looks like on water}
A group contains several crests: they grow toward its center and fade near its
edges. The envelope is an outline of their amplitude, not another material surface.
\pic{.94}{figures/water_packet.pdf}
For small-amplitude deep-water gravity waves, $c_g=c_p/2$: individual crests
move through the group. The dots in the lower panels track phase and group position,
not water parcels. This illustration uses wavelength 4 m and amplitude 0.08 m,
with vertical exaggeration. It omits spreading, nonlinear corrections and breaking.
\takeaway{A surface plot has two horizontal coordinates and elevation. Our 3D
field has three independent coordinates: its amplitude must be shown by color,
slices, or level surfaces, as on the next page.}
{Fluid interpretation: R. Salmon, \href{https://www-pord.ucsd.edu/rsalmon/111.textbook.pdf}{\emph{Introduction to Ocean Waves}}, Chapter 2, pp. 25--26. This is an explanatory analogy, not output from a fluid solver.}
\newpage
\eyebrow{03 / THREE REPRODUCIBLE RANDOM CASES}
\section*{A volume can stretch, split and move}
\pic{.68}{visuals/random_volumes.pdf}
{\small Each surface encloses $|S(t)f|\geq0.3\max|S(t)f|$ on the sampled volume.
All axes are spatial, with the same viewing window. Thresholds follow each
snapshot's own peak: compare shape here, and use the printed peaks to compare
amplitude. These are three fixed seeds, not a statistical sample.}
\newpage
\eyebrow{04 / LOOKING INSIDE THOSE PACKETS}
\section*{The individual oscillations remain visible}
\pic{1}{visuals/random_carriers.pdf}
The dark curves show $\operatorname{Re}\{S(t)f(x,0,0)e^{3ix}\}$; colored outlines
show $\pm|S(t)f(x,0,0)|$. Each row uses its initial slice peak as a fixed divisor,
so changes in amplitude remain visible between its two panels.
\takeaway{An envelope does not erase individual waves. It describes their local
amplitude and phase; an extra carrier reconstructs oscillations. The carrier
wavenumber 3 here is chosen for readability, not inferred from physical data.}
{\small Gallery computation: homogeneous canonical symbol, $128^3$ periodic grid,
length 96, spacing 0.75, seeds 11/22/33. Each input is a Gaussian window times 12
random Fourier modes, normalized to discrete $L^1=1$. These are qualitative
short-time views; the $t=256$ spatial audit does not apply to them.}
\newpage
\eyebrow{05 / FROM PICTURES TO AN INEQUALITY}
\section*{Which quantity must decay?}
A shrinking envelope peak is suggestive, but the paper bounds a different field:
a fractional Fourier multiplier is applied before taking its maximum.
\[W(t)=|D_x+\beta|^{1/2}S(t)f,\qquad
\widehat W=|k_x+\beta|^{1/2}e^{itw}\widehat f.\]
\pic{1}{visuals/weighted_comparison.pdf}
\textbf{Same input, different quantity.} Seed 33 at $t=4$, on the $y=0$ plane.
Each panel has its own amplitude scale. The right panel is the field used in the
inequality; it is not surface elevation or velocity.
\[\boxed{R(t;f)=\frac{t^{7/6}\|W(t)\|_\infty}{\|f\|_1}\leq C}\]
For $\alpha=1/2$, the predicted comparison rate is $t^{-7/6}$. The constant must
be independent of input and time at fixed equation parameters.
\begin{center}\begin{tabular}{ll}\toprule
If the ratio $R(t)$ is\ldots & The weighted peak behaves\ldots\\\midrule
Flat & Like $t^{-7/6}$ over that interval.\\
Falling & Faster than $t^{-7/6}$ over that interval.\\
Rising & Slower than $t^{-7/6}$ over that interval.\\\bottomrule
\end{tabular}\end{center}
\takeaway{The claim is boundedness, not monotonicity. A rising finite curve can
still approach a finite constant. Many inputs make the experiment more searching;
they do not by themselves turn it into a uniform theorem.}
\newpage
\eyebrow{06 / THE LONG-TIME RESULT}
\section*{Following four cases through $t=256$}
\pic{1}{../results/long_time/decay_256.pdf}
The inhomogeneous Gaussian ratio falls at late times; the other three rise over
the last doubling. Those are finite-time trends, not asymptotic conclusions.
\begin{center}\small\begin{tabular}{llrrr}\toprule
Equation & Input & $R(128)$ & $R(256)$ & Local exponent\\\midrule
\LongRows\bottomrule\end{tabular}\end{center}
The exponent is $-\log[M(256)/M(128)]/\log2$, where $M=\|W\|_\infty$.
Compare it with $7/6\simeq1.167$; it describes one time doubling only.
These curves and entries retain the long-time batch values. The subsequent audit
refines the four endpoint ratios in the technical table at the end of this report.
\takeaway{We now have a longer observation window. The strongest result is the
improved reliability of its four endpoint peaks, shown next. No counterexample
or stronger uniform exponent has been established.}
\newpage
\eyebrow{07 / CAN WE TRUST THE SPATIAL COMPUTATION?}
\section*{Enlarge the search, then compare again}
At fixed $t=256$, we increased the longitudinal period from 32,768 to 65,536 and
then 131,072. Separately, the radial search grew from 2,048 to 4,096. The broad
search retained $\Delta x=0.25$ and $\Delta r=2$, followed by local peak optimization.
\pic{1}{visuals/reliability.pdf}
\takeaway{All four cases pass the 0.1\% numerical screen. The largest final
change in refined peak magnitude is 0.00459\%; the largest location drift is
0.00079 spatial units.}
An independent non-periodic integral agrees within 0.0026\% at the candidate peaks.
Extending the radial search found no larger sampled maximum. These checks support
stability under the tested changes, rather than supplying a rigorous error bound.

\textbf{Why length matters.} The inhomogeneous near-degeneracy peak is near
$x=-841$ at $t=256$. It lies far outside the length-288 box used for the earlier
experiments. A long-time curve on that old box could confuse periodic recirculation
with whole-space behavior.

\textbf{What remains unresolved.} A finite search and local refinement can miss a
narrow or distant maximum. This audit covers four Gaussian-based cases at one time
and one derivative weight. It does not transfer automatically to random inputs.
\newpage
\eyebrow{08 / BEYOND A SINGLE GAUSSIAN}
\section*{Eleven families make the test more varied}
\pic{.98}{../results/decay_dataset/families_clear.pdf}
{\small Original short-time survey: two equation regimes per panel, $\alpha=1/2$,
length-96 box. These curves remain exploratory finite-box measurements. Recipes
include compact, anisotropic, chirped, tapered algebraic and random inputs.
The three random seeds shown earlier belong to this collection. No measured
fluid dataset has been imported.}
\newpage
\eyebrow{09 / A MORE CAREFUL INTERMEDIATE WINDOW}
\section*{Four families checked through $t=16$}
\pic{1}{../results/decay_dataset/refined_clear.pdf}
Curves use a length-288 cube at spacing 1. Dots identify the checked times
$t=4,8,16$ passing the exploratory 2\% peak-change screen in both domain and grid
comparisons; intermediate times were not independently checked.
\takeaway{Across 24 checked case--time combinations, the largest domain peak
change is 1.62\% and the largest grid peak change is 0.94\%. This supports the
intermediate-time comparisons, with weaker tolerances than the four-case endpoint audit.}
\textbf{Next scientific step.} Extend the reliable time window for more recipes,
keeping input normalization fixed and testing spatial stability at each new stage.
A candidate contradiction needs sustained growth that survives those checks;
strengthening a uniform theorem needs an argument covering its full input class.

\textbf{Technical record follows.} The remaining pages retain the equations,
optical baseline results, detailed refinement tables and reproducible algorithms.
The optical plots use an unweighted field and a different normalization from the
canonical ratio experiments; they explain dispersion but are not direct bound tests.
'''
# Preserve the original optical technical record, with obsolete future-work wording removed.
optical=original.split('\\section*{1. Equation and numerical model}',1)[1].split('\\end{document}')[0]
optical='\\newpage\n\\eyebrow{TECHNICAL RECORD / OPTICAL BASELINE}\n\\section*{1. Equation and numerical model}'+optical
optical=optical.replace('Weighted diagnostics and a longer, independently\nconverged time window are the next experiments.','The weighted experiments earlier in this combined report address that separate diagnostic.')
optical=optical.replace('Compile this source from \\texttt{report/}.','Compile \\texttt{unified\\_report.tex} from \\texttt{report/}.')
# Intermediate checks, followed by the long-time algorithm and the latest audit.
inter=refinement.split('\\section*{What was refined, and what the results support}',1)[1].split('\\input{long_time_section.tex}')[0]
inter='\\newpage\n\\eyebrow{TECHNICAL RECORD / CANONICAL PROPAGATOR}\n\\section*{Weighted equation and intermediate checks}\n'+r'''We use $S(t)f=\mathcal F^{-1}(e^{itw}\widehat f)$ with
\[w=k_x^3+3s k_x(k_y^2+k_z^2)+3\beta(k_y^2+k_z^2),\]
where $(s,\beta)=(-1,0)$ or $(1,1)$. This follows the proofs of Propositions
6.2--6.3; the signs printed in (6.1) are inconsistent. The weighted multiplier is
$|k_x+\beta|^{1/2}$. These are canonical coordinates, not a numerical conversion
of the optical baseline above.
'''+inter
method='\\newpage\n'+long.split('\\newpage\n',2)[2]
method=method.replace('updated supplement.','combined numerical study.').replace('report/decay\\_refinement.tex','report/unified\\_report.tex')
inter += r'''
\textbf{Visual gallery reproduction.} Run \texttt{python3 report/make\_visual\_gallery.py}.
The script records seeds, grid, normalization, peak values and $L^2$ norms in
\texttt{report/visuals/gallery\_manifest.json}. Rebuild this combined source with
\texttt{python3 report/build\_unified.py}, then compile \texttt{report/unified\_report.tex}.
'''
(R/'unified_report.tex').write_text(preamble+optical+inter+method+'\n\\input{spatial_section.tex}\n\\input{research_section.tex}\n\\end{document}\n')
print('Unified LaTeX written')
