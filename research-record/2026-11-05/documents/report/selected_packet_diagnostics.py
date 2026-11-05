import sys,os,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
import numpy as np
import torch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from decay_dataset import setup,weighted
root=Path(__file__).resolve().parents[1];out=root/'results/selected_packets';rows=[]
for name in ['random_33','two_packets']:
 x,f,fh,w,K=setup(name,-1,0.,192,144)
 for t in np.linspace(0,8,17):
  u=torch.fft.ifftn(fh*torch.exp(1j*float(t)*w));v=weighted(fh,w,K,0.,float(t),.5)
  rows.append(dict(family=name,t=float(t),peak=float(u.abs().max()),weighted_peak=float(v.abs().max()),ratio=None if t==0 else float(t**(7/6)*v.abs().max()),l2=float(torch.linalg.vector_norm(u)*.75**1.5)))
 print(name,flush=True)
(out/'diagnostics.json').write_text(json.dumps(rows,indent=2))
(out/'config.json').write_text(json.dumps(dict(n=192,length=144,spacing=.75,times=np.linspace(0,8,17).tolist(),sign=-1,beta=0,alpha=.5,normalization='discrete L1=1',scope='Finite periodic-grid measurements. No new domain or resolution comparison.'),indent=2))
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#18384b','axes.labelcolor':'#18384b'})
fig,axs=plt.subplots(2,2,figsize=(10,6.7))
for name,label,color in [('random_33','Random seed 33','#6858ac'),('two_packets','Two packets','#b94a64')]:
 rr=[r for r in rows if r['family']==name];t=[r['t'] for r in rr]
 for ax,vals in zip(axs.flat,[[r['peak']*1000 for r in rr],[r['peak']/rr[0]['peak'] for r in rr],[r['weighted_peak']*1000 for r in rr],[r['ratio']*1000 for r in rr[1:]]]):ax.plot(t if len(vals)==17 else t[1:],vals,'o-',markersize=3,lw=2,c=color,label=label);ax.grid(alpha=.2);ax.set_xlabel('Time t')
axs[0,0].set(title='Unweighted envelope peak',ylabel='Sampled peak × 1000');axs[0,1].set(title='Peak relative to its initial value',ylabel='Peak / initial peak',ylim=(0,1.05));axs[1,0].set(title='Fractionally weighted peak',ylabel='Sampled weighted peak × 1000');axs[1,1].set(title='The compensated decay ratio',ylabel='R(t) × 1000')
axs[0,0].legend();fig.tight_layout();fig.savefig(out/'comparison.pdf');fig.savefig(out/'comparison.png',dpi=200);plt.close(fig)
lines=[]
for name,label in [('random_33','Random seed 33'),('two_packets','Two packets')]:
 rr=[r for r in rows if r['family']==name];last=rr[-1];drop=100*(1-last['peak']/rr[0]['peak']);drift=max(abs(r['l2']/rr[0]['l2']-1) for r in rr)
 lines.append(f"{label} & {rr[0]['peak']:.6f} & {last['peak']:.6f} & {drop:.1f}\\% & {last['ratio']:.6f} \\\\")
 print(name, 'drop',drop,'l2drift',drift,'R8',last['ratio'])
(root/'report/selected_packet_values.tex').write_text('\\newcommand{\\SelectedRows}{'+'\n'.join(lines)+'}\n')
