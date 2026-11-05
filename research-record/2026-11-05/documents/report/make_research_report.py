from pathlib import Path
import os,json
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'results/research_experiments';FIG=ROOT/'report/visuals'
def read(n):return json.loads((OUT/(n+'.json')).read_text())
a,s,q,i,f=map(read,['scaling','sweep','quadrature','identity','followup'])
fix={(r['name'],r['t']):r for r in f}
def ratio(r):return fix.get((r['name'],r['t']),{}).get('refined_ratio',r['ratio'])
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#18384b','axes.labelcolor':'#18384b'})
def finish(fig,name):fig.savefig(FIG/(name+'.pdf'),bbox_inches='tight');fig.savefig(FIG/(name+'.png'),dpi=150,bbox_inches='tight');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,3.4))
for fam,c in [('gaussian','#168f9a'),('smooth_bump','#d98542'),('random_33','#6858ac')]:
 rr=[r for r in a if r['family']==fam];axs[0].plot([r['t'] for r in rr],[1e3*r['ratio'] for r in rr],'o-',label=fam.replace('_',' '),color=c)
axs[0].set(xscale='log',xlabel='Time t (input width changes with t)',ylabel='R(t), units of 0.001',title='Rescaled inputs reproduce the same ratio');axs[0].legend(fontsize=8);axs[0].grid(alpha=.2)
fams=list(dict.fromkeys(r['family'] for r in a));errs=[max(r['relative_field_error'] for r in a if r['family']==fam) for fam in fams]
axs[1].barh([x.replace('_',' ') for x in fams],np.array(errs)*1e16,color='#168f9a');axs[1].set(xlabel='Relative field error, units of $10^{-16}$',title='All 11 input recipes');axs[1].invert_yaxis();fig.tight_layout();finish(fig,'research_scaling')
fig,axs=plt.subplots(2,2,figsize=(9,6),sharex=True,sharey=True)
for row,reg in enumerate(['homogeneous','inhomogeneous']):
 for col,sx in enumerate([3,6]):
  rr=sorted([r for r in s if r['regime']==reg and r['sx']==sx and r['group']=='axial sweep' and r['t']==16],key=lambda r:r['offset']);ax=axs[row,col]
  ax.plot([r['offset'] for r in rr],[1e3*ratio(r) for r in rr],'-',color='#168f9a',lw=2)
  for r in rr:
   patched=(r['name'],r['t']) in fix
   ax.scatter(r['offset'],ratio(r)*1e3,marker='D' if patched else 'o',color='#d98542' if patched else '#168f9a',s=40,zorder=3)
  ax.axvline(0,color='gray',ls=':',lw=1);ax.set(title=f'{reg.capitalize()}, longitudinal width {sx}',xlabel=r'Spectral offset $q_x+\beta$',ylabel='R(16), units of 0.001');ax.grid(alpha=.15)
fig.tight_layout();finish(fig,'research_sweep')
fig,axs=plt.subplots(1,2,figsize=(9,3.6))
for reg,col in [('homogeneous',0),('inhomogeneous',1)]:
 for name,label,c in [(reg+'_cancel','Zero integral','#d98542'),('homogeneous_sx3_offset0' if reg=='homogeneous' else 'inhomogeneous_unshifted_control','Gaussian control','#168f9a')]:
  rr=[r for r in s if r['name']==name];axs[col].plot([r['t'] for r in rr],[ratio(r)*1e3 for r in rr],'o-',label=label,color=c)
 axs[col].set(title=reg.capitalize(),xlabel='Time t',ylabel='R(t), units of 0.001',xticks=[4,8,16]);axs[col].legend(fontsize=8);axs[col].grid(alpha=.2)
fig.tight_layout();finish(fig,'research_cancellation')
fig,axs=plt.subplots(1,2,figsize=(9,3.5))
for reg,c in [('homogeneous','#168f9a'),('inhomogeneous','#d98542')]:
 rr=[r for r in i if r['regime']==reg];axs[0].plot([r['width'] for r in rr],[r['ratio']*1e3 for r in rr],'o-',label=reg,color=c)
axs[0].set(xlabel='Gaussian width (smaller means narrower)',ylabel='R(1), units of 0.001',title='Narrow inputs probe larger ratios');axs[0].legend(fontsize=8);axs[0].grid(alpha=.2)
for regime,fam,c in [('homogeneous_minus','gaussian','#168f9a'),('homogeneous_minus','near_degeneracy','#6858ac'),('inhomogeneous_plus','gaussian','#d98542'),('inhomogeneous_plus','near_degeneracy','#a64053')]:
 rr=[r for r in q if r['regime']==regime and r['family']==fam];axs[1].semilogy([r['t'] for r in rr],[r['relative_disagreement'] for r in rr],'o-',label=regime.split('_')[0]+' / '+('near' if fam=='near_degeneracy' else 'Gaussian'),color=c)
axs[1].set(xlabel='Time (fixed spatial evaluation points)',ylabel='Relative complex-field difference',title='Two quadrature implementations agree',xticks=[256,512,1024]);axs[1].legend(fontsize=7);axs[1].grid(alpha=.2);fig.tight_layout();finish(fig,'research_quadrature')
stats=dict(scaling_max_error=max(errs),sweep_total=len(s),sweep_initial_passed=sum(r['passes_screen'] for r in s),followups=len(f),followup_passed=sum(r['passes_followup'] for r in f),followup_max_change=max(r['domain_and_radial_change'] for r in f),followup_max_original_correction=max(r['original_to_refined'] for r in f),quadrature_max_disagreement=max(r['relative_disagreement'] for r in q),quadrature_256_disagreement=max(r['relative_disagreement'] for r in q if r['t']==256),quadrature_max_truncation_change=max(r['truncation_change'] for r in q),quadrature_warning_count=sum(len(r['warnings']) for r in q),identity_passed=sum(r['passes_screen'] for r in i))
assert len(a)==33 and len(s)==78 and len(q)==12 and len(i)==10 and len(f)==8
assert stats['quadrature_warning_count']==0
(OUT/'summary.json').write_text(json.dumps(stats,indent=2))
macros='\n'.join('\\newcommand{\\'+key+'}{'+val+'}' for key,val in {
 'ResearchScaleError':f"{stats['scaling_max_error']:.2g}",
 'ResearchPass':str(stats['sweep_initial_passed']),
 'ResearchFollowPass':str(stats['followup_passed']),
 'ResearchFollowChange':f"{100*stats['followup_max_change']:.4f}\\%",
 'ResearchCorrection':f"{100*stats['followup_max_original_correction']:.3f}\\%",
 'ResearchQuadError':f"{stats['quadrature_max_disagreement']:.2g}",
 'ResearchQuadTail':f"{stats['quadrature_max_truncation_change']:.2g}",
 }.items())
(ROOT/'report/research_values.tex').write_text(macros+'\n')
lines=['# Research-motivated experiments: results','',json.dumps(stats,indent=2),'','## Axial spectral sweep at t=16','','Ratios use the independent Gaussian follow-up where the original screen failed.','', '| Regime | sx | qx+beta | R(16) | Follow-up used |','|---|---:|---:|---:|---|']
for r in s:
 if r['t']==16 and r['group']=='axial sweep':lines.append(f"| {r['regime']} | {r['sx']} | {r['offset']} | {ratio(r):.7f} | {(r['name'],16) in fix} |")
lines+=['','## Interpretation','', 'Scaling agreement verifies the discrete implementation of an exact symmetry; it is not an independent whole-space convergence test.', 'The spectral sweep uses a 2% initial screen. Eight flagged measurements receive a separate radial Gaussian calculation and a 0.1% follow-up screen. Those screens assess tested changes, not certified errors.', 'The cancellation controls have zero spatial integral but Gaussian spectral tails; this is not a strict frequency-support-away-from-degeneracy experiment.', 'The approximate-identity test stops at width 0.75. Increasing ratios do not establish convergence to a kernel maximum or determine the optimal theorem constant.', 'At t=512 and 1024 the quadrature comparison keeps the t=256 peak coordinates fixed. It is a pointwise stress test, not a continuation of global peak decay curves.', 'The fixed-node implementation uses 512-point Gauss-Legendre on each regularized panel. The independent method uses adaptive Gauss-Kronrod on principal-phase-controlled panels with stationary points inserted and a separate cusp substitution. Neither is claimed to reproduce PathFinder or the cited saddle-point algorithms.', 'No new full nonlinear fluid simulation or naturally occurring dataset is included.', '', '## Reproduce','','Run research_experiments.py with scaling, sweep, quadrature, and identity arguments; run refine_research_flags.py; then python3 report/make_research_report.py. JSON checkpoints are retained per case.']
(OUT/'RESULTS.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(stats,indent=2))
