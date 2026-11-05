"""Restyle the saved checkpoint as a conventional mathematics article."""
from pathlib import Path
import re
R=Path(__file__).resolve().parent
src=(R/'checkpoint_2026_09_10.tex').read_text()
chunks={}
for part in src.split(r'\newpage')[1:]:
 m=re.search(r'\\label\{([^}]+)\}',part)
 if m:chunks[m[1]]=part
preamble=r'''\documentclass[10pt,letterpaper]{article}
\usepackage[margin=.9in]{geometry}
\usepackage{amsmath,amssymb,graphicx,booktabs,hyperref}
\hypersetup{hidelinks,pdftitle={Numerical investigations of three-dimensional cubic dispersion and weighted decay},pdfauthor={}}
\numberwithin{equation}{section}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{definition}[proposition]{Definition}
\newcommand{\norm}[1]{\left\|#1\right\|}
\newcommand{\takeaway}[1]{\par\medskip\noindent\textbf{Remark.} #1\par\medskip}
\newcommand{\callout}[1]{\par\medskip\noindent #1\par\medskip}
\DeclareFontShape{OT1}{cmr}{m}{n}{<->cmr10}{}
\DeclareMathSizes{8}{10}{7}{7}\DeclareMathSizes{12}{12}{7}{7}
\DeclareMathSizes{9}{10}{7}{7}\DeclareMathSizes{10}{10}{7}{7}
\DeclareFontShape{OT1}{cmr}{bx}{n}{<->cmbx10}{}
\DeclareFontShape{TU}{lmr}{m}{n}{<->\UnicodeFontFile{lmroman10-regular}{\UnicodeFontTeXLigatures}}{}
\DeclareFontShape{TU}{lmr}{bx}{n}{<->\UnicodeFontFile{lmroman10-bold}{\UnicodeFontTeXLigatures}}{}
\DeclareFontShape{TU}{lmr}{m}{it}{<->\UnicodeFontFile{lmroman10-italic}{\UnicodeFontTeXLigatures}}{}
\setlength{\parindent}{1.2em}
\setlength{\parskip}{3pt}
\setlength{\emergencystretch}{1.5em}
\renewcommand{\topfraction}{.9}\renewcommand{\bottomfraction}{.8}
\renewcommand{\textfraction}{.08}\renewcommand{\floatpagefraction}{.65}
\input{computed_values.tex}\input{refinement_values.tex}\input{long_time_values.tex}
\input{selected_packet_values.tex}\input{research_values.tex}\input{spatial_values.tex}
\title{Numerical Investigations of Three-Dimensional\\Cubic Dispersion and Weighted Decay}
\author{}
\date{Research checkpoint: September 10, 2026}
\begin{document}
\maketitle
\begin{abstract}
We document numerical experiments for linear three-dimensional cubic propagators
arising in the Dysthe research context. The principal observable is the normalized
weighted peak $t^{7/6}\|\,|D_x+\beta|^{1/2}S(t)f\|_\infty/\|f\|_1$.
The study combines Fourier propagation for varied artificial initial data with
Gaussian-specific transverse integration, spatial refinement, and independent
oscillatory quadrature. Four Gaussian-based decay curves are computed through
$t=256$, where all four candidate maxima pass a 0.1\% spatial stability screen.
Additional experiments examine cubic scaling, spectral location, cancellation
and concentration. Three-dimensional level surfaces and planar slices illustrate
selected random and two-packet solutions. The computations establish numerical
consistency within the tested settings; they establish neither a new uniform
upper bound nor a counterexample. A scaling argument explains why an improved
homogeneous exponent requires a modified input class or right-hand-side norm.
\end{abstract}
\noindent\textbf{Keywords:} cubic dispersion; Dysthe equation; weighted decay;
Fourier methods; oscillatory integrals; numerical convergence.
\tableofcontents
\clearpage
'''
figs={
'weighted_comparison.pdf':('weight','Unweighted envelope magnitude and fractionally weighted magnitude for seed 33 at $t=4$.'),
'envelope_explanation.pdf':('envelope','Envelope magnitude, carrier oscillations and normalized intensity.'),
'water_packet.pdf':('water','Illustrative water-wave packet and the distinction between group and phase motion.'),
'05_random_seed_33_volumes.png':('randomvolume','Seed 33: three-dimensional magnitude level surfaces at $t=0,4,8$ (review-collection figure 5).'),
'06_random_seed_33_slices_and_waves.png':('randomslice','Seed 33: planar magnitude slices and illustrative carrier traces (review-collection figure 6).'),
'07_two_interfering_packets_volumes.png':('pairvolume','Two phase-offset packets: magnitude level surfaces at $t=0,4,8$ (review-collection figure 7).'),
'08_two_interfering_packets_slices_and_waves.png':('pairslice','Two phase-offset packets: planar slices and carrier traces (review-collection figure 8).'),
'comparison.pdf':('diagnostics','Unweighted and weighted diagnostics for the two selected inputs.'),
'decay_256.pdf':('long','Compensated weighted peaks for four Gaussian-based cases through $t=256$.'),
'reliability.pdf':('reliability','Relative changes in candidate weighted peaks under the spatial audit at $t=256$.'),
'families_clear.pdf':('survey','Initial eleven-family weighted-decay survey in two canonical regimes.'),
'refined_clear.pdf':('refined','Intermediate-time weighted-decay curves and refinement checks through $t=16$.'),
'research_scaling.pdf':('scaling','Matched-grid cubic scaling checks for eleven input recipes.'),
'research_sweep.pdf':('sweep','Dependence of compensated peaks on spectral offset and longitudinal width.'),
'research_cancellation.pdf':('cancellation','Compensated peaks for Gaussian and zero-integral initial data.'),
'research_quadrature.pdf':('quadrature','Concentration tests at $t=1$ and independent pointwise quadrature comparisons through $t=1024$.'),
'peak_decay.pdf':('opticalpeaks','Optical baseline: sampled peak magnitudes for the parameter and modulation cases.'),
'slices.pdf':('opticalslices',r'Optical baseline: $y=0$ magnitude slices for $\varepsilon_2=1$.'),
'widths.pdf':('widths','Optical baseline: intensity widths in the three coordinate directions.'),
'generic.pdf':('generic','Optical baseline: a non-Gaussian two-packet initial profile and its propagated magnitude.')}
refs={'5':'randomvolume','6':'randomslice','7':'pairvolume','8':'pairslice','S1':'diagnostics','A1':'opticalpeaks','A2':'opticalslices','A3':'widths','A4':'generic'}
def fig(width,path):
 key,cap=figs[Path(path).name]
 return '\n'+r'\begin{figure}[!htbp]\centering'+'\n'+r'\includegraphics[width='+width+r'\linewidth]{'+path+'}\n'+r'\caption{'+cap+r'}\label{fig:'+key+'}\n'+r'\end{figure}'+'\n'
def clean(key,title=None):
 c=chunks[key]
 c=re.sub(r'\\phantomsection\\label\{[^}]+\}\\pdfbookmark\[0\]\{[^}]*\}\{[^}]*\}','',c)
 c=re.sub(r'\\(?:eyebrow|tagline)\{[^}]*\}','',c)
 c=re.sub(r'\\input\{[^}]+\}','',c)
 c=c.replace(r'\end{document}','')
 c=re.sub(r'\\section\*\{([^}]*)\}',lambda m:r'\subsection{'+(title or re.sub(r'^\d+\. ','',m[1]))+r'}\label{'+key+'}',c,count=1)
 if r'\label{'+key+'}' not in c:c=r'\subsection{'+title+r'}\label{'+key+'}\n'+c
 c=re.sub(r'\\textbf\{Figure (?:[5-8]|S1|A[1-4])\.[^}]*\}\s*','',c)
 c=re.sub(r'Figures 5--8',r'Figures~\\ref{fig:randomvolume}--\\ref{fig:pairslice}',c)
 for a,b in [('5','7'),('6','8')]:c=c.replace(f'Figures {a} and {b}',r'Figures~\ref{fig:'+refs[a]+r'} and~\ref{fig:'+refs[b]+'}')
 c=re.sub(r'Figure (S1|A[1-4]|[5-8])\b',lambda m:r'Figure~\ref{fig:'+refs[m[1]]+'}',c)
 c=re.sub(r'\\pic\{([^}]+)\}\{([^}]+)\}',lambda m:fig(m[1],m[2]),c)
 c=re.sub(r'\\begin\{center\}\\includegraphics\[width=([^\]]*)\\linewidth\]\{([^}]+)\}\\end\{center\}',lambda m:fig(m[1] or '1',m[2]),c)
 c=c.replace(r'\[',r'\begin{equation}').replace(r'\]',r'\end{equation}')
 c=c.replace('on this page','in this experiment').replace('The comparison is explained on the next\npage.','The integration comparison is discussed below.')
 c=c.replace('this combined report','this report').replace('this combined\nreport','this report')
 return c.strip()+'\n'
parts=[preamble]
def section(title,keys):
 parts.append(r'\section{'+title+'}\n')
 for key,title in keys:parts.append(clean(key,title))
section('Introduction and research objective',[('summary','Scope and principal findings'),('target','Canonical propagator and weighted observable')])
parts.append(r'''
\begin{definition}[Compensated weighted peak]
For nonzero initial data $f\in L^1(\mathbb R^3)$ for which the weighted solution
is bounded, define
\begin{equation}\label{eq:diagnostic}
\mathcal R_{s,\beta}(t;f)
=\frac{t^{7/6}\|\,|D_x+\beta|^{1/2}S_{s,\beta}(t)f\|_{L^\infty(\mathbb R^3)}}
{\|f\|_{L^1(\mathbb R^3)}},\qquad t>0.
\end{equation}
\end{definition}
The notation $R(t;f)$ used below denotes this quantity with the regime understood.
The proposed estimate asserts a constant independent of $t$ and $f$; it does not
assert monotonicity in $t$. Numerical maxima approximate the continuum norm in
\eqref{eq:diagnostic} only to the extent supported by the stated checks.
The primary manuscript is cited as~\cite{MPSdraft}.
''')
section('Interpretation of the computed fields',[('envelope','Envelope, carrier and intensity'),('fluid','Illustrative fluid interpretation')])
section('Selected three-dimensional solutions',[('randomvolume','Random packet: magnitude level surfaces'),('randomslice','Random packet: slices and carrier reconstruction'),('pairvolume','Two phase-offset packets: linear interference'),('pairslice','Two-packet slices and carrier reconstruction'),('selecteddiag','Amplitude and weighted diagnostics')])
section('Decay experiments and spatial reliability',[('survey','Initial survey of eleven input families'),('refined','Intermediate-time refinement'),('longresults','Gaussian-based computations through $t=256$'),('reliability','Spatial stability of candidate maxima')])
section('Experiments motivated by analytical structure',[('research','Cubic scaling and its numerical verification'),('research2','Spectral location and degeneracy'),('research3','Cancellation and concentration'),('research4','Independent oscillatory quadrature')])
# Replace informal scaling discussion by a precisely scoped proposition and proof.
old=parts[-4]
start=old.index(r'\textbf{What scaling says about the research question.}')
old=old[:start]+r'''
\begin{proposition}[Obstruction to a faster uniform homogeneous rate]
Fix $s\in\{-1,1\}$ and $\beta=0$. Suppose a constant $C$ satisfies
\begin{equation}
\|\,|D_x|^{1/2}S_{s,0}(t)f\|_\infty\le C t^{-\gamma}\|f\|_1
\end{equation}
for every Schwartz function $f$ and every $t\ge1$. Then $\gamma\le7/6$.
\end{proposition}
\noindent\textit{Proof.}
For $f_\lambda(X)=\lambda^3f(\lambda X)$, homogeneity gives
\begin{equation}
|D_x|^{1/2}S_{s,0}(t)f_\lambda(X)
=\lambda^{7/2}\bigl[|D_x|^{1/2}S_{s,0}(\lambda^3t)f\bigr](\lambda X),
\qquad \|f_\lambda\|_1=\|f\|_1.
\end{equation}
Choose $f$ whose Fourier transform is smooth, compactly supported away from
$k_x=0$, and nonzero. The weighted solution at time one then has a finite,
strictly positive supremum $A$. For $0<\lambda\le1$, apply the hypothesized bound
at $t=\lambda^{-3}$ to obtain
\begin{equation}
\lambda^{7/2}A\le C\lambda^{3\gamma}\|f\|_1.
\end{equation}
If $\gamma>7/6$, division by $\lambda^{7/2}$ and passage to $\lambda\to0$
contradict $A>0$.\hfill$\square$

\noindent\textbf{Remark.} This analytical deduction does not prove the upper
bound with exponent $7/6$, determine its optimal constant, or settle fixed-input
asymptotics. The fixed inhomogeneous symbol with $\beta=1$ does not have the same
scaling symmetry.
'''
parts[-4]=old
section('Discussion and further questions',[('discussion','Interpretation of the evidence and proposed continuation')])
# Keep the existing annotated discussion, add conventional numbered references.
section('Relation to the literature',[('literature','Analytical and numerical context')])
parts.append(r'''
The cited analytical background comprises~\cite{BAKS,MPS2021,GKS}; numerical
integration references are~\cite{Olver,HKL,GHH}. Physical interpretation is
informed by~\cite{GKSfluid,Salmon}. These works supply context and motivation,
not validation of the present finite computational searches.
\clearpage\begin{thebibliography}{9}
\bibitem{MPSdraft} R. Mosincat, D. Pilod and J.-C. Saut,
\emph{On Third Order Nonlinear Schr\"odinger Equations}, supplied manuscript,
January 22, 2026, Section 6.
\bibitem{BAKS} M. Ben-Artzi, H. Koch and J.-C. Saut,
Dispersion estimates for third order equations in two dimensions,
\emph{Comm. Partial Differential Equations} 28 (2003), 1943--1974.
\href{https://doi.org/10.1081/PDE-120025491}{doi:10.1081/PDE-120025491}.
\bibitem{MPS2021} R. Mosincat, D. Pilod and J.-C. Saut,
Global well-posedness and scattering for the Dysthe equation in $L^2(\mathbb R^2)$,
\emph{J. Math. Pures Appl.} 149 (2021), 73--97.
\href{https://arxiv.org/abs/2007.01613}{arXiv:2007.01613}.
\bibitem{GKS} R. Grande, K. M. Kurianski and G. Staffilani,
On the nonlinear Dysthe equation, \emph{Nonlinear Analysis} 207 (2021), 112292.
\href{https://arxiv.org/abs/2006.13392}{arXiv:2006.13392}.
\bibitem{Olver} S. Olver, Moment-free numerical approximation of highly oscillatory
integrals with stationary points, \emph{European J. Appl. Math.} (2007).
Assessment limited to the publisher abstract.
\bibitem{HKL} D. Huybrechs, A. B. J. Kuijlaars and N. Lejon,
A numerical method for oscillatory integrals with coalescing saddle points,
\emph{SIAM J. Numer. Anal.} (2019).
\href{https://arxiv.org/abs/1806.06549}{arXiv:1806.06549}.
\bibitem{GHH} A. Gibbs, D. P. Hewett and D. Huybrechs,
Numerical evaluation of oscillatory integrals via automated steepest descent
contour deformation, \emph{J. Comput. Phys.} 501 (2024), 112787.
\href{https://arxiv.org/abs/2307.07261}{arXiv:2307.07261}.
\bibitem{GKSfluid} P. Guyenne, A. Kairzhan and C. Sulem,
Hamiltonian Dysthe equation for three-dimensional deep-water gravity waves,
\emph{Multiscale Model. Simul.} 20 (2022), 349--378.
\href{https://doi.org/10.1137/21M1432788}{doi:10.1137/21M1432788}.
\bibitem{Salmon} R. Salmon, \emph{Introduction to Ocean Waves}, Chapter 2,
pp. 25--26, \href{https://www-pord.ucsd.edu/rsalmon/111.textbook.pdf}{online text}.
\end{thebibliography}
\clearpage\appendix
''')
section('Optical baseline and verification',[('optical','Equation and numerical method'),('optical11','Peak evolution and parameter dependence'),('optical12','Spatial slices'),('optical13','Directional spreading and generic initial data'),('optical14','Verification and interpretation limits')])
section('Canonical numerical methods and audits',[('intermediate','Intermediate-time Fourier computations'),('longmethods','Gaussian reduction and long-time searches'),('spatialaudit','Detailed spatial audit at $t=256$'),('selectedmethods','Selected-case computation')])
section('Checkpoint record and reproducibility',[('checkpoint','Progression of the investigation'),('restart','Status and evidence map')])
# Remove the obsolete page-based route table; retain complete batch inventory.
g=chunks['guide'];g=g[g.index(r'\textbf{Experiment inventory}'):]
parts.append(r'\subsection{Experiment inventory}\label{guide}'+'\n'+g)
text='\n'.join(parts)+r'\end{document}'+'\n'
text=text.replace(r'\texttt{python3 report/make\_long\_time\_tables.py}',r'\path{python3 report/make_long_time_tables.py}')
text=text.replace(r'\textbf{Experiment inventory}\par',r'\noindent')
text=text.replace('All curves on this page','All curves for these inputs')
text=text.replace('The comparison is explained on the next\npage.','The comparison is explained in the following subsection.')
text=text.replace('this page','this subsection')
text=text.replace(r'\path{report/checkpoint\_2026\_09\_10.tex}',r'\path{formal_report.tex}')
text=text.replace(r'report/checkpoint\_2026\_09\_10.tex',r'formal\_report.tex')
text=text.replace(r'checkpoint\_2026\_09\_10.tex',r'formal\_report.tex')
text=text.replace(r'build\_checkpoint.py',r'build\_formal\_report.py')
text=text.replace('are preserved in the checkpoint source archive.','are preserved in the full checkpoint archive; the LaTeX edition contains the report source and figure assets.')
text=text.replace('The source archive includes scripts, LaTeX, figure exports,\nsmall results and a SHA-256 manifest.', 'The full checkpoint archive includes scripts, LaTeX, figure exports,\nsmall results and a SHA-256 manifest. The separate formal LaTeX package contains the article and its figure assets.')
(R/'formal_report.tex').write_text(text)
print('Wrote formal report')
