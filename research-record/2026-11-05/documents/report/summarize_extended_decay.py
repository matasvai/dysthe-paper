from pathlib import Path
import os,json,csv
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];O=R/'results/extended_decay'
old=json.loads((R/'results/long_time/summary.json').read_text());audit=json.loads((R/'results/spatial_reliability/summary.json').read_text())
new=[json.loads(p.read_text()) for p in sorted(O.glob('*_512.json'))+sorted(O.glob('*_1024.json'))];new=[a for a in new if a.get('complete')]
def passed(a):return a['passes_screen'] or a.get('followup',{}).get('passes_screen',False)
rows=[]
for a in old:
 c=dict(regime=a['regime'],family=a['family'],t=a['t'],peak=a['peak'],ratio=a['ratio'],x=a['x_peak'],r=a['r_peak'],source='previous long-time batch')
 if a['t']==256:
  d=next(b['continuum_candidate'] for b in audit if b['regime']==a['regime'] and b['family']==a['family']);c.update({k:d[k] for k in ['peak','ratio','x','r']});c['source']='previous spatial audit'
 rows.append(c)
for a in new:rows.append({k:a[k] for k in ['regime','family','t','peak','ratio','x','r']}|{'source':'new search: pass' if passed(a) else 'new search: flagged'})
rows.sort(key=lambda a:(a['regime'],a['family'],a['t']))
for reg in ['homogeneous_minus','inhomogeneous_plus']:
 for fam in ['gaussian','near_degeneracy']:
  seq=[a for a in rows if a['regime']==reg and a['family']==fam]
  for i,a in enumerate(seq):
   a['effective_exponent']=None if i==0 else float(-np.log(a['peak']/seq[i-1]['peak'])/np.log(a['t']/seq[i-1]['t']))
with (O/'decay_history.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
for typ in ['ratios','exponents']:
 fig,axs=plt.subplots(2,2,figsize=(11,7),layout='constrained',sharex=True)
 for i,reg in enumerate(['homogeneous_minus','inhomogeneous_plus']):
  for j,fam in enumerate(['gaussian','near_degeneracy']):
   ax=axs[i,j];seq=[a for a in rows if a['regime']==reg and a['family']==fam];color=['#225ea8','#b35806'][i]
   if typ=='ratios':xx=[a['t'] for a in seq];yy=[a['ratio'] for a in seq]
   else:xx=[np.sqrt(seq[k-1]['t']*a['t']) for k,a in enumerate(seq) if k];yy=[a['effective_exponent'] for a in seq[1:]];ax.axhline(7/6,color='black',ls='--',lw=1,label='Target exponent 7/6');ax.set_ylim(.65,1.4)
   ax.plot(xx,yy,'o-',color=color,lw=1.8)
   for a in seq:
    if a['source']=='new search: flagged':ax.text(.02,.95,'Unresolved check: see report',transform=ax.transAxes,va='top',color='red')
   ax.axvline(256,color='#777777',ls=':',lw=1);ax.set_xscale('log',base=2);ax.set_xticks([16,32,64,128,256,512,1024],labels=['16','32','64','128','256','512','1024']);ax.grid(alpha=.2)
   ax.set_title(('Homogeneous' if i==0 else 'Inhomogeneous')+'\n'+('Gaussian' if j==0 else 'near-degeneracy packet'))
   ax.annotate(f'{yy[-1]:.5f}' if typ=='ratios' else f'{yy[-1]:.3f}',(xx[-1],yy[-1]),xytext=(-6,9) if typ=='ratios' and i==1 and j==0 else ((-6,-18) if typ=='ratios' else (-4,9)),textcoords='offset points',ha='right',bbox=dict(facecolor='white',edgecolor='none',alpha=.85,pad=1))
 fig.supxlabel('Evolution parameter t' if typ=='ratios' else 'Geometric midpoint of each time-doubling interval')
 fig.supylabel('Compensated weighted peak R(t)' if typ=='ratios' else 'Effective decay exponent p')
 fig.suptitle('Longer-time weighted decay: new spatial peak searches' if typ=='ratios' else 'Finite-interval decay rates; dashed line marks 7/6',fontsize=14)
 for ext in ['png','svg']:fig.savefig(O/f'{typ}.{ext}',dpi=180)
 plt.close(fig)
lines=['# Weighted decay extended to t=1024','', 'Prepared 12 September 2026. New linear Gaussian-family calculations; no nonlinear/soliton experiment is claimed.','',
 'The observable is M(t)=|| |Dx+beta|^(1/2) S(t)f ||infinity, with exact continuum ||f||1=1. The compensated ratio is R=t^(7/6) M(t). Four cases are searched at each of 512 and 1024. Earlier values through 128 are retained; the t=256 values are from the stronger spatial audit.','',
 '## Main findings', '', 'The inhomogeneous Gaussian has effective exponent 1.3168 over 512 to 1024. The inhomogeneous near-degeneracy ratio peaks among sampled times at 512 and decreases at 1024, yielding exponent 1.1960. The homogeneous Gaussian gives 1.0903, while the homogeneous near-degeneracy case gives 1.0260 and its identified dominant candidate shifts from an off-axis ring to r=0. These differing finite-interval behaviors do not establish one common asymptotic exponent.', '', '## Results','', '| Regime | Input | t | R(t) | Effective exponent from preceding doubling | x peak | r peak | Screen |','|---|---|---:|---:|---:|---:|---:|---|']
for a in rows:
 if a['t']>=256:lines.append(f"| {a['regime']} | {a['family']} | {a['t']} | {a['ratio']:.8f} | {a['effective_exponent']:.4f} | {a['x']:.4f} | {a['r']:.4f} | {a['source']} |")
lines+=['','![Compensated ratios](ratios.png)','', '![Finite-interval exponents](exponents.png)','',
 'The dotted vertical line marks the previous endpoint t=256. Larger effective exponents mean faster weighted-peak decay. Plot panels use separate vertical scales for R(t).', '', '## Numerical checks','', 'Full longitudinal/radial searches compare L=32768 and 65536 at dx=0.5 and dr=4 on 0<=r<=4096. A separate annulus extends the search to r=8192 at dr=2. The inner search is repeated with dx=0.25 and dr=2. Candidate seeds from multiple radial rows are locally optimized using non-periodic Gaussian integration.','',
 'At the best candidate, Gauss-Legendre orders 512 and 1024 are compared, together with a separate phase-partitioned adaptive Gauss-Kronrod calculation and 12-versus-14-standard-deviation frequency truncation. Fourier sums are compared at L=65536 and 131072 at the SAME candidate coordinates; the last comparison is pointwise, not another full-domain search.','',
 '| Case | t | Length change | Grid change | Independent integral discrepancy | Largest-period Fourier discrepancy | Annulus boundary / peak | Pass |','|---|---:|---:|---:|---:|---:|---:|---|']
for a in new:
 c=a['checks'];lines.append(f"| {a['regime']}/{a['family']} | {a['t']} | {c['length_change']:.3%} | {c['grid_change']:.3%} | {c['adaptive_disagreement']:.3e} | {c['spectral_integral_disagreement']:.3e} | {a['scans']['annulus']['edge']/a['peak']:.3e} | {passed(a)} |")
lines+=['',f"Completed {len(new)}/8 new case-time searches; {sum(passed(a) for a in new)} pass the stated 0.1% consistency screen.",'',
 '## Follow-up of initial flags','', 'Original screen failures are retained in the per-case JSON. When present, a followup record repeats the full inner radial search at dr=1 (and dr=0.5 if needed), at fixed L=65536 and dx=0.25, then compares independently optimized peaks. The outer annulus retains dr=2. The Pass column includes successful follow-ups; this does not erase the initial coarse-grid sensitivity.', '', 'The annulus-boundary column measures its longitudinal edge and r=8192 endpoint. The raw outer_boundary_fraction field in the first-run JSON is conservatively the maximum over both inner and annular scan boundaries; it includes the interior r=4096 interface and is not an exclusively outer-domain statistic.', '', '## Interpretation limits','', 'Effective exponents describe one doubling interval, not fitted asymptotic laws. A growing compensated ratio may still approach a bounded limit. Neither slower finite-time decay nor a change of dominant peak establishes a counterexample to a uniform bound with unspecified constant.','',
 'The searches are finite and sampled. Radial refinement and multiple local starts strengthen reliability but do not certify the continuum global supremum or exclude every narrow missed peak. The t=256 audit and the present extension use different checks, so the old audit is not transferred by assertion.','',
 'These four inputs are Gaussian-based and permit exact transverse reduction. Other artificial inputs, measured data and nonlinear solitary waves have not been evolved in this batch.','',
 'Reproduce with `python3 extend_decay.py`, `python3 refine_extended_decay.py`, and `python3 report/summarize_extended_decay.py`. Per-case JSON files retain search settings, seeds, optimizers, quadrature diagnostics, and flags. Earlier checkpoint reports are unchanged.']

for a in new:
 if a.get('followup'):
  for level,d in a['followup']['levels'].items():lines.append(f"Follow-up {a['regime']}/{a['family']} at t={a['t']}, dr={level}: successive sampled-peak change {d['grid_change']:.5%}; independently optimized peak change {d['candidate_peak_change']:.3e}.")
(O/'RESULTS.md').write_text('\n'.join(lines)+'\n')
print('Summarized',len(new),'new measurements')
