from pathlib import Path
import re
R=Path(__file__).resolve().parent
u=(R/'unified_report.tex').read_text();m=(R/'selected_packets_mock.tex').read_text()
preamble=u.split('\\begin{document}')[0]
preamble=preamble.replace('Waves, dispersion and decay: a visual numerical study','Dysthe research meeting: numerical dispersion, decay and reliability').replace('WAVES, DISPERSION AND DECAY','DYSTHE / NUMERICAL DECAY STUDY').replace('Numerical study','Research meeting / 10 September 2026')
preamble=preamble.replace('\\DeclareMathSizes{9}{10}{7}{5}','\\DeclareMathSizes{9}{10}{7}{7}\\DeclareMathSizes{10}{10}{7}{7}')
preamble+=r'''
\newcommand{\tagline}[1]{\eyebrow{#1}}
\newcommand{\callout}[1]{\par\smallskip\colorbox{pale}{\parbox{.96\linewidth}{\vspace{5pt}#1\vspace{5pt}}}\par\smallskip}
\input{selected_packet_values.tex}
\begin{document}
'''
uc=u.split('\\begin{document}',1)[1].split('\\end{document}')[0].split('\\newpage')
mc=m.split('\\begin{document}',1)[1].split('\\end{document}')[0].split('\\newpage')
pages=[]
def add(label,title,body):
 pages.append('\\newpage\n\\phantomsection\\label{'+label+'}\\pdfbookmark[0]{'+title+'}{bookmark-'+label+'}\n'+body)
cover=r'''\thispagestyle{empty}
\eyebrow{RESEARCH MEETING / 10 SEPTEMBER 2026}
{\color{navy}\Huge Numerical dispersion,\\[3pt] decay and reliability}\par
{\Large A three-dimensional study in the Dysthe research context}\par
\vspace{8pt}
\textbf{Research question.} Can numerical experiments support the claimed weighted
decay estimate, reveal inputs that approach its limiting behavior, or produce
reliable evidence against it?
\pic{1}{../output/figure_review/07_two_interfering_packets_volumes.png}
\textbf{A visual starting point.} Two phase-offset packets evolve under the
homogeneous linear canonical operator. The visible shapes are three-dimensional
magnitude level surfaces, not water elevations. Figures 5--8 are developed in the
main text and retain their review-collection identifiers.
\callout{\textbf{Position at this meeting.} The strongest numerical result is
spatial stability of four candidate weighted maxima at $t=256$. A broader set of
inputs demonstrates sensitivity to spectral location, width and cancellation.
No new uniform decay bound or counterexample has been established.}
\begin{center}\begin{tabular}{ll}\toprule
Completed & Current scope\\\midrule
Long-time decay curves & Four Gaussian-based cases through $t=256$\\
Spatial audit & All four pass a 0.1\% numerical stability screen\\
Targeted data sweep & 26 inputs; 78 case--time measurements\\
Independent integration & 12 pointwise comparisons through $t=1024$\\\bottomrule
\end{tabular}\end{center}
\vfill
{\small This report consolidates the optical baseline, canonical decay experiments,
visual case studies, literature review and reproducible numerical checks. The
full nonlinear water-wave system and measured-fluid data remain outside the
completed computations.}
'''
add('cover','Title and scope',cover)
add('summary','Executive summary',r'''\eyebrow{MEETING SUMMARY}
\section*{What the work establishes}
We have developed a numerical workflow for linear cubic dispersion in three
independent spatial coordinates, with a visual explanation of wave envelopes and
an explicit connection to the weighted estimate in the supplied manuscript.
The workflow separates finite-box FFT experiments from Gaussian-specific
whole-space transverse integration.

\textbf{1. The observable matters.} Ordinary envelope peaks describe visible
spreading. The estimate instead controls a fractionally weighted solution. At
$\alpha=1/2$ and $p=\infty$, the diagnostic is
\[
 R(t;f)=t^{7/6}\big\||D_x+\beta|^{1/2}S(t)f\big\|_\infty/\|f\|_1.
\]
A rising ratio on a finite interval is compatible with a bounded estimate; the
manuscript does not specify a numerical failure threshold.

\textbf{2. The most reliable long-time evidence is spatial.} For four
Gaussian-based cases at $256$, two longitudinal enlargements and an independent
radial extension pass the 0.1\% screen. The largest final change in locally
refined peak magnitude is 0.00459\%, and peak-location drift is below 0.0008
spatial units. These are consistency measurements, not certified global error bounds.

\textbf{3. Input structure changes finite-time behavior.} The targeted sweep
contains 26 inputs at three times. Seventy of 78 measurements pass the first 2\%
screen; all eight flagged measurements pass a subsequent 0.1\% follow-up. The
largest correction to an original fine-grid peak is 2.288\%. Narrower normalized
Gaussian inputs produce larger ratios at $t=1$. A zero-integral input produces an
almost flat inhomogeneous ratio from $8$ to $16$, within tested numerical differences.

\textbf{4. The selected visual cases make the interpretation concrete.} Seed 33
and the two-packet input lose about 60.4\% and 41.1\% of their sampled envelope
peaks by $t=8$. Their $L^2$ norms remain numerically constant. These are examples
of dispersion and linear interference, not dissipative fluid simulations.

\textbf{5. Scaling restricts what a stronger theorem could mean.} For the
homogeneous symbol, cubic scaling rules out replacing $7/6$ by a larger exponent
in an estimate uniform over all $L^1$ inputs with the same right-hand side.
This deduction does not prove the upper bound or settle fixed-input asymptotics.
It motivates studying constants, near-extremal behavior and restricted input classes.
\callout{\textbf{Decision proposed for the meeting.} Prioritize convergence of
the selected random and two-packet cases, then global peak searches at $512$ and
$1024$ for the Gaussian families. Use spectral localization and cancellation to
formulate a restricted-class question before attempting a stronger decay claim.}
''')
add('guide','Reading guide and experiment inventory',r'''\eyebrow{HOW TO USE THIS REPORT}
\section*{A visual narrative with a technical record}
The main text connects the preferred figures to the mathematical question. The
technical record keeps the earlier optical calculations and numerical checks
available without interrupting that narrative. Links below jump to the relevant pages.
\begin{center}\begin{tabular}{p{.77\linewidth}r}\toprule
Topic & Page\\\midrule
\hyperref[target]{Model, diagnostic and interpretation} & \pageref{target}\\
\hyperref[envelope]{Envelope and fluid interpretation} & \pageref{envelope}\\
\hyperref[randomvolume]{Selected figures 5--8: random and two-packet cases} & \pageref{randomvolume}\\
\hyperref[selecteddiag]{Supplementary diagnostics for the selected cases} & \pageref{selecteddiag}\\
\hyperref[longresults]{Long-time decay curves and spatial reliability} & \pageref{longresults}\\
\hyperref[survey]{Broader data survey and intermediate refinement} & \pageref{survey}\\
\hyperref[research]{Research-motivated scaling, spectral and quadrature tests} & \pageref{research}\\
\hyperref[discussion]{Discussion and proposed next steps} & \pageref{discussion}\\
\hyperref[literature]{Literature and its relevance} & \pageref{literature}\\
\hyperref[optical]{Technical record: optical baseline and verification} & \pageref{optical}\\
\hyperref[intermediate]{Technical record: canonical methods and audits} & \pageref{intermediate}\\
\hyperref[selectedmethods]{Technical record: selected visual cases} & \pageref{selectedmethods}\\\bottomrule
\end{tabular}\end{center}
\textbf{Experiment inventory}\par
\begin{tabular}{p{.30\linewidth}p{.63\linewidth}}\toprule
Batch & What is included\\\midrule
Optical baseline & Nine Gaussian parameter/modulation cases with 225 time records,
plus one two-packet example.\\
Initial canonical survey & Eleven recipes in two regimes; 858 weighted measurements
at 13 times and three fractional weights.\\
Intermediate refinement & Four families in two regimes; 24 checked case--time
combinations through $16$.\\
Long-time extension & Two Gaussian families in two regimes, at five time doublings
from $16$ through $256$.\\
Research follow-up & 33 scaling checks, 78 sweep measurements, eight follow-ups,
ten concentration tests, twelve quadrature comparisons.\\
Figure review and selected cases & Twenty review figures; eighteen new spatial
snapshots across six recipes; 34 additional time records for the two selected cases.\\\bottomrule
\end{tabular}

Batches reuse some input recipes and times, so these counts describe saved
measurements rather than distinct independent experiments. All initial fields
actually simulated are artificial. Natural data sources were identified but not
imported, reconstructed or simulated.
''')
model=r'''\eyebrow{MODEL AND RESEARCH TARGET}
\section*{A canonical linear propagator in three coordinates}
We use the Fourier convention $\widehat f(k)=\int f(X)e^{-ik\cdot X}\,dX$ and
\[
 S_{s,\beta}(t)f=\mathcal F^{-1}(e^{itw_{s,\beta}}\widehat f),\qquad
 w_{s,\beta}=k_x^3+3s k_x(k_y^2+k_z^2)+3\beta(k_y^2+k_z^2).
\]
The tested regimes are $(s,\beta)=(-1,0)$ and $(1,1)$. They follow the symbols
used in the proofs of Propositions 6.2--6.3 in the supplied manuscript. Its printed
phase signs in (6.1) are inconsistent; the computations consistently use $+itw$.
The earlier optical baseline uses a different coordinate formulation, retained
separately in the technical record.
'''+uc[5].split(r'\section*{Which quantity must decay?}',1)[1]
add('target','Model and weighted decay diagnostic',model)
env=uc[1].replace('on page 5',r'on page \pageref{randomslice}')
add('envelope','Understanding the envelope',env);add('fluid','Fluid interpretation',uc[2])
sel=[]
for c in mc:
 c=c.replace('\\pic{','\\pic{1}{').replace('page 5',r'page \pageref{selecteddiag}')
 sel.append(c)
first=sel[0][sel[0].index('\\pic{1}{'):].split('\\vfill')[0]
add('randomvolume','Figure 5: random packet volume',r'\eyebrow{SELECTED VISUAL CASES / FIGURE 5}\section*{Random seed 33: deformation of a localized packet}'+'\n'+first)
add('randomslice','Figure 6: random packet slices',sel[1]);add('pairvolume','Figure 7: two-packet volume',sel[2])
pair=sel[3].replace('A useful pairing for the final report.','Why these figures are paired.');add('pairslice','Figure 8: two-packet slices',pair)
add('selecteddiag','Selected-case amplitude and weighted diagnostics',sel[4])
add('longresults','Decay curves through t=256',uc[6]);add('reliability','Spatial reliability overview',uc[7]);add('survey','Eleven-family input survey',uc[8]);add('refined','Intermediate refinement overview',uc[9].split('\\textbf{Technical record follows.}')[0])
research=(R/'research_section.tex').read_text().replace(r'\pic{.97}',r'\pic{.88}');researchpages=research.split('\\newpage')
for i,c in enumerate(researchpages):
 if c.strip():add('research' if i==1 else f'research{i}',f'Research experiments {i}',c)
add('discussion','Discussion and meeting decisions',r'''\eyebrow{DISCUSSION}
\section*{What can be concluded, and what would change that conclusion?}
\textbf{The numerical conclusion.} The experiments support the reproducibility
of the implemented linear model and the stability of identified peaks under
specified computational changes. They reveal pronounced dependence on initial
spectral center, bandwidth and phase. Those observations are useful for selecting
harder tests; they do not establish a uniform operator bound.

\textbf{Why the current curves are not counterexamples.} The constant in the
claimed estimate is unspecified. An increasing ratio over five time doublings
could still approach a finite limit, and a sampled maximum can be distorted by
spatial truncation. A serious counterexample candidate would need growth that
survives independent refinement and a mathematical argument establishing why it
cannot remain bounded, or a contradiction to an independently established constant.

\textbf{Why faster decay for a subclass remains interesting.} The homogeneous
scaling obstruction applies to an unrestricted $L^1$ formulation. Extra moment
conditions, quantified spectral localization or additional weighted norms change
the class and may change the question. The present cancellation example alone
does not specify or prove such an improved estimate. Its Gaussian spectral tails
also mean it is not supported strictly away from degeneracies.

\begin{center}\begin{tabular}{p{.25\linewidth}p{.65\linewidth}}\toprule
Priority & Proposed next step and criterion\\\midrule
1. Selected cases & Enlarge and refine the exact seed-33 and two-packet weighted
calculations. Require stable full-volume candidate maxima before extending time.\\
2. Later Gaussian times & Perform global searches at $512$ and $1024$; the completed
pointwise quadrature comparison is a prerequisite, not a substitute.\\
3. Restricted input class & Choose a precise cancellation or spectral-support
condition; derive its expected asymptotic behavior before fitting a numerical exponent.\\
4. Kernel sharpness & Continue the normalized concentration sequence with separate
frequency-tail, quadrature and spatial checks; seek evidence of a limiting kernel norm.\\
5. Physical validation & Specify a water-wave envelope model and physical scales,
then reconstruct a surface and compare with suitable measured or Euler data.\\\bottomrule
\end{tabular}\end{center}
\callout{\textbf{Meeting decision.} The immediate choice is between extending the
well-checked Gaussian time window and strengthening convergence for the more
visually informative non-Gaussian cases. Both advance the project, but they answer
different questions and should retain separate evidence standards.}

The project archive retains original and refined values separately, including
failed initial screens. This distinction is essential for interpreting changes
in a curve as physical dispersion rather than changes in the computation.
''')
add('literature','Literature and relevance',r'''\eyebrow{LITERATURE}
\section*{Analytical tools, numerical methods and physical interpretation}
\textbf{Primary research target.} R. Mosincat, D. Pilod and J.-C. Saut,
\emph{On Third Order Nonlinear Schr\"odinger Equations}, supplied manuscript dated
January 22, 2026. Section 6 gives the three-dimensional canonical estimates under
study. The local supplied version remains our reference; no public replacement
version was verified in the literature search.

\textbf{Cubic dispersion and spectral geometry.} M. Ben-Artzi, H. Koch and
J.-C. Saut (2003), \href{https://doi.org/10.1081/PDE-120025491}{\emph{Dispersion Estimates
for Third Order Equations in Two Dimensions}}, CPDE 28, 1943--1974. Their study of
cubic normal forms and degenerate stationary points motivates deliberately moving
packet spectra across curvature-degenerate sets. It is a two-dimensional methodological
precedent, not a theorem for our three-dimensional weighted operator.

\textbf{Nonlinear Dysthe theory.} R. Mosincat, D. Pilod and J.-C. Saut (2021),
\href{https://arxiv.org/abs/2007.01613}{\emph{Global well-posedness and scattering for
the Dysthe equation in $L^2(\mathbb R^2)$}}, JMPA 149, 73--97. Small-data scattering
places the linear estimates in a nonlinear context. The regularity sharpness in
that work is distinct from sharpness of the decay exponent studied here.
R. Grande, K. M. Kurianski and G. Staffilani (2021),
\href{https://arxiv.org/abs/2006.13392}{\emph{On the nonlinear Dysthe equation}},
Nonlinear Analysis 207, 112292, develops anisotropic estimates relevant to the
importance of direction and frequency localization.

\textbf{Oscillatory integration.} S. Olver (2007),
\href{https://www.cambridge.org/core/journals/european-journal-of-applied-mathematics/article/abs/momentfree-numerical-approximation-of-highly-oscillatory-integrals-with-stationary-points/0E02A1874E775BB219E5A2CE2DC0221B}{\emph{Moment-free numerical approximation of highly oscillatory integrals with stationary points}},
provides an early stationary-point-aware approach; our assessment used the publisher abstract.
D. Huybrechs, A. B. J. Kuijlaars and N. Lejon (2019),
\href{https://arxiv.org/abs/1806.06549}{\emph{A Numerical Method for Oscillatory Integrals
with Coalescing Saddle Points}}, and A. Gibbs, D. P. Hewett and D. Huybrechs (2024),
\href{https://arxiv.org/abs/2307.07261}{\emph{Numerical evaluation of oscillatory integrals
via automated steepest descent contour deformation}}, JCP 501, 112787, motivate
more robust independent quadrature. Our phase-partitioned adaptive method is not
an implementation of their algorithms and does not inherit their guarantees.

\textbf{Physical surface reconstruction.} P. Guyenne, A. Kairzhan and C. Sulem
(2022), \href{https://doi.org/10.1137/21M1432788}{\emph{Hamiltonian Dysthe Equation for
Three-Dimensional Deep-Water Gravity Waves}}, MMS 20, 349--378, develops a refined
free-surface reconstruction and comparisons with Euler simulations. Here the
fluid domain is three-dimensional but the surface has two horizontal coordinates.
It supplies a route to physical validation, not validation of our current optical
or canonical snapshots.

\textbf{Access and scope.} These references were checked against author papers,
preprints and publisher records on September 9, 2026. The fuller annotated note
and the scaling derivation are included in \path{research/literature_review.md}.
The review is targeted rather than exhaustive.
''')
for i in range(10,15):
 c=uc[i]
 for n in [3,4,5,6]:c=c.replace(f'Figure {n}',f'Figure A{n-2}')
 c=c.replace('unified\\_report.tex','meeting\\_report.tex')
 add('optical' if i==10 else f'optical{i}',f'Optical technical record {i-9}',c)
add('intermediate','Canonical intermediate checks',uc[15].replace('unified\\_report.tex','meeting\\_report.tex'))
method=uc[16].split('\\input{spatial_section.tex}')[0].replace('unified\\_report.tex','meeting\\_report.tex');add('longmethods','Long-time Gaussian method',method)
audit=(R/'spatial_section.tex').read_text().replace('\\newpage','',1);add('spatialaudit','Detailed spatial audit at t=256',audit)
selectedmethod=sel[5].replace('What was computed, and how to use this draft','Selected-case method and reliability')
start=selectedmethod.find('\\textbf{Research context.}')
end=selectedmethod.find('\\begingroup\\raggedright\\textbf{Reproduction.}')
selectedmethod=selectedmethod[:start]+selectedmethod[end:]
selectedmethod=selectedmethod.replace('selected\\_packets\\_mock.tex','meeting\\_report.tex').replace('selected_packets_mock.tex','meeting_report.tex').replace('this draft','this report')
add('selectedmethods','Selected-case technical record',selectedmethod)
# Remove legacy numbered eyebrows and stale hard-coded reading-route references.
body=''.join(pages)
body=body.replace(r'build\_unified.py',r'build\_meeting\_report.py')
body=body.replace('are supplied in the accompanying snapshot archive.', 'are saved in the project snapshot archive and can be regenerated from the included solver.')
body=re.sub(r'\\eyebrow\{0\d / ',r'\\eyebrow{',body)
body=body.replace('The figures on page 5',r'The figures on page \pageref{randomslice}')
body=body.replace('The subsequent audit\nrefines the four endpoint ratios in the technical table at the end of this report.',r'The subsequent audit refines the four endpoint ratios on page \pageref{spatialaudit}.')
(R/'meeting_report.tex').write_text(preamble+body+'\n\\end{document}\n')
print('Built',len(pages),'planned pages')
