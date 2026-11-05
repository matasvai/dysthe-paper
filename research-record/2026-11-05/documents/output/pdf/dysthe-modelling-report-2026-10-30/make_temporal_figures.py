#!/usr/bin/env python3
"""Regenerate temporal report figures from bundled plot arrays and full-grid diagnostics.
Use --poc PATH once to extract and checksum original results. Plot arrays are visualization-only.
"""
import argparse, hashlib, json, shutil
from pathlib import Path
import numpy as np
from scipy.signal import resample
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data'/'temporal'; DATA.mkdir(parents=True,exist_ok=True)
FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'serif','font.size':10,'axes.labelsize':10,'axes.titlesize':11,'pdf.fonttype':42,'ps.fonttype':42,'figure.constrained_layout.use':True,'axes.spines.top':False,'axes.spines.right':False,'legend.frameon':False,'savefig.bbox':'tight'})
FAMILIES=['packet','sideband','random']; TITLES=['Localized packet','Modulated wavetrain','Smooth random profile']
STYLES={'stability':('black','-'),'literal':('.4','--'),'nls':('.6',':'),'meanflow':('.25','-.')}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def extract(poc):
 manifest=[]
 for label in ['results','results-refined','results-audit']:
  src=poc/label
  summary=json.loads((src/'summary.json').read_text())
  (DATA/f'{label}-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
  for r in summary['cases']:
   if not r['qualified']:continue
   if r['T'] not in [8,16,32]:continue
   if r['model']!='stability' and (r['epsilon']!=.05 or r['T']!=16):continue
   p=src/r['artifact']['path'];assert sha(p)==r['artifact']['sha256']
   with np.load(p,allow_pickle=False) as z:
    fields=resample(z['fields'],256,axis=-1).astype(np.complex64)
    dest=DATA/(label+'-'+r['key']+'.npz')
    np.savez_compressed(dest,fields=fields,T=z['T'],s=np.arange(256)*40/256-20)
   manifest.append({'file':dest.name,'sha256':sha(dest),'original_file_sha256':sha(p),'usage':'Fourier-resampled to256 and complex64, visualization only; all metrics from full-grid JSON.'})
 domain=poc/'results-refined/domain-checks.json'
 if domain.exists():shutil.copy2(domain,DATA/'domain-checks.json')
 (DATA/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

def save(fig,name):fig.savefig(FIG/(name+'.pdf'));fig.savefig(FIG/(name+'.png'),dpi=130);plt.close(fig)
def record(label,family,eps=.05,kind='stability',T=16):
 s=json.loads((DATA/f'{label}-summary.json').read_text())
 return next(r for r in s['cases'] if r['family']==family and r['epsilon']==eps and r['model']==kind and r['T']==T)
def array(label,r):return np.load(DATA/(label+'-'+r['key']+'.npz'),allow_pickle=False)
def choose(family):
 r=record('results-audit',family)
 if r['qualified']:return 'results-audit',r
 return 'results-refined',record('results-refined',family,T=8)

def main():
 p=argparse.ArgumentParser();p.add_argument('--poc',type=Path);a=p.parse_args()
 if a.poc:extract(a.poc)
 records=[choose(f) for f in FAMILIES]
 fig,ax=plt.subplots(1,3,figsize=(7,2.35),sharey=True)
 for j,(label,r) in enumerate(records):
  z=array(label,r);x=z['s'];u=z['fields'][0]
  ax[j].plot(x,abs(u),'k',label='Magnitude');ax[j].plot(x,u.real,color='.55',ls='--',label='Real part');ax[j].set(title=TITLES[j],xlabel='$s$');ax[j].set_xlim(-20,20)
 ax[0].set_ylabel('Initial envelope $u(s,0)$');ax[-1].legend(fontsize=8)
 save(fig,'temporal-initial-profiles')
 fig,ax=plt.subplots(3,1,figsize=(7,6.05),sharex=True)
 for j,(label,r) in enumerate(records):
  z=array(label,r);im=ax[j].pcolormesh(z['s'],z['T'],abs(z['fields']),cmap='Greys',shading='auto',vmin=0,vmax=2.7,rasterized=False)
  ax[j].set(ylabel='$T$',title=TITLES[j]+f"; checked through $T={r['T']:g}$")
 ax[-1].set_xlabel('Moving coordinate $s$');cb=fig.colorbar(im,ax=ax,label='$|u(s,T)|$',shrink=.8);cb.solids.set_rasterized(False)
 save(fig,'temporal-evolution')
 fig,ax=plt.subplots(2,2,figsize=(7,4.7))
 for j,(label,r) in enumerate(records):
  rows=r['diagnostics']['rows'];t=np.array([x['T'] for x in rows]);sty=['-','--',':'][j]
  ax[0,0].plot(t,[x['peak_ratio'] for x in rows],color='k',ls=sty,label=TITLES[j])
  ax[0,1].plot(t,[x['h2_ratio'] for x in rows],color='k',ls=sty)
  ax[1,0].plot(t,[x['physical_envelope_peak'] for x in rows],color='k',ls=sty)
  ax[1,1].plot(t,[x['scaled_bandwidth_indicator'] for x in rows],color='k',ls=sty)
 for x,ylabel in zip(ax.flat,['Peak / initial peak','$H^2$ norm / initial $H^2$ norm','$\\epsilon\\,\\max_s|u|$','$\\epsilon\\,\\sigma_k$']):x.set(xlabel='$T$',ylabel=ylabel);x.grid(alpha=.18)
 fig.legend(*ax[0,0].get_legend_handles_labels(),loc='outside lower center',ncol=3,fontsize=8)
 save(fig,'temporal-observables')
 # Paired model differences only for cases with qualified reference in both variants.
 fig,ax=plt.subplots(1,3,figsize=(7,2.8),sharey=True)
 for j,f in enumerate(FAMILIES):
  base=record('results-audit',f);z=array('results-audit',base);t=z['T'];den=np.linalg.norm(z['fields'],axis=-1)
  for k in ['literal','nls','meanflow']:
   r=record('results-audit',f,kind=k)
   if not r['qualified'] or not base['qualified']:continue
   q=array('results-audit',r);d=np.linalg.norm(q['fields']-z['fields'],axis=-1)/den
   color,sty=STYLES[k];ax[j].plot(t,100*d,color=color,ls=sty,label={'literal':'Literal print','nls':'Cubic NLS','meanflow':'NLS + mean flow'}[k])
  ax[j].set(title=TITLES[j],xlabel='$T$');ax[j].grid(alpha=.18)
 ax[0].set_ylabel('Complex $L^2$ difference (%)');ax[-1].legend(fontsize=7)
 save(fig,'temporal-model-differences')
 # Coarse/finer comparisons at fixed T8 and stress-test T16, same target c=3/2.
 fig,ax=plt.subplots(1,2,figsize=(7,3.25))
 labels=['512 / 256','2048 / 1024','4096 / 2048']; x=np.arange(3)
 for j,f in enumerate(FAMILIES):
  vals=[];drifts=[]
  for lab,T in [('results',8),('results-refined',8),('results-audit',16)]:
   r=record(lab,f,T=T);vals.append(r['refinement']['grid']['h2']);drifts.append(r['diagnostics']['max_action_drift'])
  ax[0].semilogy(x,vals,['o-','s--','^:'][j],color='k',label=TITLES[j]);ax[1].semilogy(x,np.maximum(drifts,1e-16),['o-','s--','^:'][j],color='k')
 ax[0].axhline(1e-3,color='.5',ls='-.');ax[1].axhline(1e-6,color='.5',ls='-.')
 for q in ax:q.set_xticks(x,labels,rotation=12);q.set_xlabel('Fine / comparison grid (points)');q.grid(alpha=.18)
 ax[0].set_ylabel('Maximum grid comparison $E_2$');ax[1].set_ylabel('Maximum relative action drift');fig.legend(*ax[0].get_legend_handles_labels(),loc='outside lower center',ncol=3,fontsize=8)
 ax[0].set_title('$\\epsilon=0.05$; $T=8,8,16$ respectively');ax[1].set_title('Conservation and convergence differ')
 save(fig,'temporal-refinement')
 # Honest status matrix exposes stress failures; no measured error is a blow-up label.
 fig,ax=plt.subplots(figsize=(7,3.3));matrix=np.zeros((6,3));texts=[]
 for row,(f,e) in enumerate((f,e) for f in FAMILIES for e in [.05,.1]):
  tr=[]
  for col,(lab,T) in enumerate([('results',8),('results-refined',8),('results-audit',16)]):
   r=record(lab,f,eps=e,T=T);matrix[row,col]=1 if r['qualified'] else 0
   tr.append(('Pass' if r['qualified'] else 'Unresolved')+'\n'+f"$E_2^{{grid}}={r['refinement']['grid']['h2']:.1e}$")
  texts.append(tr)
 ax.imshow(matrix,cmap='Greys',vmin=-1,vmax=4,aspect='auto')
 for row in range(6):
  for col in range(3):ax.text(col,row,texts[row][col],ha='center',va='center',fontsize=9)
 ax.set_xticks(range(3),['512 points; $T=8$','2048 points; $T=8$','4096 points; $T=16$'])
 ax.set_yticks(range(6),[f'{TITLES[FAMILIES.index(f)]}, ε={e:g}' for f in FAMILIES for e in [.05,.1]])
 ax.tick_params(length=0);save(fig,'temporal-gates')
 # Machine-readable report numbers use full-grid diagnostics.
 rows=[]
 for label,r in records:
  d=r['diagnostics'];rows.append({'family':r['family'],'T':r['T'],'epsilon':r['epsilon'],'max_peak_ratio':max(x['peak_ratio'] for x in d['rows']),'max_h2_ratio':d['max_h2_ratio'],'max_steepness_indicator':max(x['physical_envelope_peak'] for x in d['rows']),'max_bandwidth_indicator':max(x['scaled_bandwidth_indicator'] for x in d['rows']),'grid_h2':r['refinement']['grid']['h2'],'step_h2':r['refinement']['step']['h2'],'max_action_drift':d['max_action_drift'],'nonlinear_times':r['T']/d['nonlinear_length'],'first_peak':d['focusing_peaks'][:1]})
 (DATA/'report-numbers.json').write_text(json.dumps(rows,indent=2)+'\n')
 print(json.dumps(rows,indent=2))
if __name__=='__main__':main()
