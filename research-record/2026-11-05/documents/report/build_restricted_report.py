from pathlib import Path
import sys,json,os
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from restricted_decay import C,spectrum
OUT=ROOT/'output/restricted_decay';rows=json.loads((ROOT/'results/restricted_decay/summary.json').read_text())
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
colors=['#174a7e','#c65d16','#23815b']
fig,axes=plt.subplots(1,2,figsize=(9,3.3),layout='constrained')
x=np.linspace(-15,15,1001);z=x/3;k=np.linspace(-1.25,1.25,1001)
for m in range(3):
 h=[np.ones_like(z),z,z*z-1][m]
 axes[0].plot(x,h*np.exp(-z*z/2)/(3*np.sqrt(2*np.pi)*C[m]),label=f'Order {m}',color=colors[m])
 axes[1].plot(k,abs(spectrum(k,3,m)),color=colors[m],label=f'Order {m}')
axes[0].axhline(0,color='k',lw=.5);axes[0].set(xlabel='Longitudinal position x',ylabel='Signed normalized longitudinal input')
axes[1].set(xlabel='Longitudinal frequency k',ylabel='Fourier magnitude')
for ax in axes:ax.legend();ax.grid(alpha=.2)
fig.savefig(OUT/'inputs.png',dpi=180);plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(9,3.5),layout='constrained')
for j,s in enumerate([3,6]):
 for m in range(3):
  rr=sorted([a for a in rows if a['sx']==s and a['m']==m],key=lambda a:a['t']);tt=np.array([a['t'] for a in rr]);pp=np.array([a['peak'] for a in rr]);p=-np.diff(np.log2(pp))
  axes[j].plot(tt[1:],p,'o-',label=f'Order {m}',color=colors[m])
 axes[j].axhline(7/6,color='k',ls='--',lw=1,label='7/6 reference');axes[j].axhline(1.5,color='gray',ls=':',label='3/2 candidate')
 axes[j].set(xscale='log',xlabel='End of doubling interval',ylabel='Effective weighted-decay exponent',title=f'Longitudinal width {s}');axes[j].set_xticks([32,64,128,256],labels=['32','64','128','256']);axes[j].minorticks_off();axes[j].grid(alpha=.2);axes[j].legend(fontsize=8)
fig.savefig(OUT/'cancellation.png',dpi=180);plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(9,3.4),layout='constrained')
for m,label,col in [(4,'Band crossing k=0','#174a7e'),(3,'Band separated from k=0','#c65d16')]:
 axes[0].plot(k,abs(spectrum(k,3,m)),label=label,color=col)
 rr=sorted([a for a in rows if a['m']==m],key=lambda a:a['t']);tt=np.array([a['t'] for a in rr]);pp=np.array([a['peak'] for a in rr]);axes[1].plot(tt[1:],-np.diff(np.log2(pp)),'o-',label=label,color=col)
axes[0].set(xlabel='Longitudinal frequency k',ylabel='Normalized Fourier magnitude');axes[0].axvline(0,color='k',ls=':',lw=1)
axes[1].set(xscale='log',xlabel='End of doubling interval',ylabel='Effective weighted-decay exponent');axes[1].set_xticks([32,64,128,256],labels=['32','64','128','256']);axes[1].axhline(1.5,color='gray',ls=':',label='3/2 candidate')
for ax in axes:ax.minorticks_off();ax.legend(fontsize=8);ax.grid(alpha=.2)
fig.savefig(OUT/'gap.png',dpi=180);plt.close(fig)
lines=[]
for s,m,label in [(3,0,'Gaussian'),(3,1,'Zero mean'),(3,2,'Two moments'),(6,0,'Gaussian'),(6,1,'Zero mean'),(6,2,'Two moments'),(3,4,'Band crossing zero'),(3,3,'Separated band')]:
 rr=sorted([a for a in rows if a['sx']==s and a['m']==m],key=lambda a:a['t']);p=-np.log2(rr[-1]['peak']/rr[-2]['peak']);lines.append(f'{label} & {s if m<3 else "--"} & {p:.4f} & {rr[-1]["ratio"]:.6f} '+r'\\')
(OUT/'table.tex').write_text(r'\begin{tabular}{lrrr}\toprule Input & Width $s$ & $p_{[128,256]}$ & $R(256)$\\\midrule'+'\n'+'\n'.join(lines)+'\n'+r'\bottomrule\end{tabular}')
print('Rows',len(rows),'passes',sum(a['passes_1pct_screen'] or a.get('followup',{}).get('passes_1pct_screen',False) for a in rows))
