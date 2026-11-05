"""Freeze the complete meeting narrative with a dated progress and restart record."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'meeting_report.tex').read_text()
s=s.replace('Dysthe research meeting: numerical dispersion, decay and reliability','Dysthe checkpoint: 10 September 2026')
s=s.replace('Research meeting / 10 September 2026','Checkpoint / 10 September 2026')
s=s.replace('RESEARCH MEETING / 10 SEPTEMBER 2026','WORK CHECKPOINT / 10 SEPTEMBER 2026')
s=s.replace('A three-dimensional study in the Dysthe research context','Progress record of the three-dimensional Dysthe numerical study')
s=s.replace('Position at this meeting.','Position at this checkpoint.')
s=s.replace('MEETING SUMMARY','CHECKPOINT SUMMARY')
s=s.replace('Decision proposed for the meeting.','Proposed continuation.')
s=s.replace('Meeting decision.','Decision for the next work session.')
s=s.replace('The immediate choice is between','The next work session can choose between')
s=s.replace('build\\_meeting\\_report.py','build\\_checkpoint.py')
s=s.replace('meeting\\_report.tex','checkpoint_2026_09_10.tex').replace('meeting_report.tex','checkpoint_2026_09_10.tex')
# Underscores in prose need TeX escaping, while \path accepts them directly.
s=s.replace('checkpoint_2026_09_10.tex',r'checkpoint\_2026\_09\_10.tex')
extra=r'''
\newpage
\phantomsection\label{checkpoint}\pdfbookmark[0]{Checkpoint: progression and completed work}{bookmark-checkpoint}
\eyebrow{CHECKPOINT / 10 SEPTEMBER 2026}
\section*{How the work developed}
This checkpoint records the work completed by September 10, 2026. It preserves the
full research narrative and adds a progress record for reviewing and resuming the
project. Preparing this checkpoint adds documentation, not new simulation results.

\textbf{Starting point: a numerical model.} We began with the supplied manuscript
and implemented a three-coordinate linear dispersive model. The optical baseline
established exact Fourier propagation and checks against special solutions,
independent integration, and changes in the spatial grid and box.

\textbf{Making the solution understandable.} We distinguished the complex envelope,
its magnitude, intensity, carrier oscillations, and illustrative water elevation.
Three-dimensional magnitude surfaces and planar slices made the simulated fields
visible. The fluid illustration explains the envelope idea; it is not a calibrated
reconstruction of the canonical three-coordinate solution.

\textbf{Refocusing on the research question.} The investigation moved from visual
spreading to the manuscript's weighted decay estimate. The compensated ratio
$R(t;f)$ became the central observable. Gaussian data supplied a starting point,
then eleven artificial input recipes broadened the tests to phases, spectral
locations, random packets and cancellation structures.

\textbf{Extending time and testing space.} The intermediate survey reached $16$.
Gaussian-specific reduction then allowed four cases to reach $256$. Subsequent
longitudinal and radial enlargements checked the identified peaks. This extension
does not transfer automatically to every input in the earlier finite-box survey.

\textbf{Experiments motivated by the literature.} Cubic scaling, curvature
degeneracies and oscillatory integration motivated additional checks. We completed
a spectral sweep, resolved all eight initially flagged measurements with separate
follow-ups, tested concentration and cancellation, and compared two integration
implementations at fixed spatial points through $1024$.

\textbf{Visual review and consolidation.} A collection of twenty figures was
prepared. Review figures 5--8 were selected for closer explanation, with additional
amplitude and weighted diagnostics for seed 33 and two phase-offset packets.
The complete report now brings these cases together with all earlier batches.

\callout{\textbf{The checkpoint conclusion.} We have a reproducible linear
numerical workflow and stronger spatial evidence for four Gaussian-based peaks
at $256$. We have not established a new uniform decay inequality, constructed a
counterexample, or simulated measured fluid data. The distinction is maintained
throughout the report.}

For a quick review, read the summary on page \pageref{summary}, the visual cases
on pages \pageref{randomvolume}--\pageref{pairslice}, and the discussion on page
\pageref{discussion}. The full batch inventory is on page \pageref{guide}.

\newpage
\phantomsection\label{restart}\pdfbookmark[0]{Checkpoint: evidence, files and restart plan}{bookmark-restart}
\eyebrow{CHECKPOINT / EVIDENCE AND RESTART RECORD}
\section*{What is saved, and what remains open}
\begin{center}\begin{tabular}{p{.27\linewidth}p{.64\linewidth}}\toprule
Status & Evidence and practical meaning\\\midrule
Completed: optical baseline & Nine Gaussian parameter/modulation cases plus a
two-packet example. These validate and illustrate a distinct optical formulation.\\
Completed: varied input survey & Eleven artificial recipes, two canonical regimes
and three fractional weights; selected inputs refined through $16$.\\
Completed: long-time audit & Four Gaussian-based cases through $256$, with all
four passing the stated 0.1\% spatial stability screen.\\
Completed: targeted follow-up & 78 spectral-sweep measurements, eight refined flags,
33 scaling checks and ten concentration tests.\\
Completed: later integration checks & Twelve pointwise comparisons through $1024$.
No global maxima at $512$ or $1024$ were located in this batch.\\
Open: selected visual cases & Their exact diagnostic series still needs its own
box and grid refinement before a reliable long-time extension.\\
Open: analytical conclusion & A stronger restricted-class estimate, limiting kernel
constant, or counterexample requires additional analysis and evidence.\\
Open: physical data & No measured data have been imported and no full nonlinear
water-wave simulation has been performed.\\\bottomrule
\end{tabular}\end{center}

\textbf{Where to find the evidence.} Paths below are relative to the project root
and are preserved in the checkpoint source archive.
\begin{center}\begin{tabular}{p{.38\linewidth}p{.53\linewidth}}\toprule
Location & Contents\\\midrule
\path{results/verification.json} & Optical numerical checks.\\
\path{results/decay_dataset/} & Input survey, intermediate curves and refinement.\\
\path{results/long_time/} & Gaussian decay curves and search records.\\
\path{results/spatial_reliability/} & Independent spatial audit and peak comparisons.\\
\path{results/research_experiments/} & Scaling, sweeps, flags, concentration, quadrature.\\
\path{results/selected_packets/} & Seed-33 and two-packet diagnostic series.\\
\path{output/figure_review/} & Complete twenty-figure collection and captions.\\
\path{research/literature_review.md} & Annotated literature and scaling argument.\\\bottomrule
\end{tabular}\end{center}

\textbf{Restart here.} Review the decision table on page \pageref{discussion}.
The two immediate numerical priorities are convergence for the selected visual
cases and global Gaussian peak searches at $512$ and $1024$. Before claiming an
improved exponent, specify the input class and norm: homogeneous cubic scaling
already obstructs a uniformly faster rate with the same unrestricted $L^1$ norm.

\textbf{Archive scope.} The source archive includes scripts, LaTeX, figure exports,
small results and a SHA-256 manifest. Large NPZ field arrays and the supplied
manuscript are excluded; the arrays can be regenerated from the scripts. The
manifest records included files, not a claim that every simulation was rerun today.
'''
anchor=r'\newpage'+'\n'+r'\phantomsection\label{guide}'
assert anchor in s
s=s.replace(anchor,extra+anchor,1)
(R/'checkpoint_2026_09_10.tex').write_text(s)
print('Wrote checkpoint source')
