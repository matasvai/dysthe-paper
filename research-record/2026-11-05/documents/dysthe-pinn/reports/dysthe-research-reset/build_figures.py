"""Draw vector-only figures from the bundled compact evidence snapshot."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'evidence.json').read_text())
plt.rcParams.update({'font.family':'serif','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.linewidth':.7,'pdf.fonttype':42,'ps.fonttype':42,'savefig.bbox':'tight'})
def save(fig,name):
    fig.savefig(HERE/'figures'/f'{name}.pdf');plt.close(fig)
fig,ax=plt.subplots(figsize=(6.4,2.45),layout='constrained')
for m,label,style,marker in [(3,r'Band $0.5<k_x<1$', '-', 'o'),(4,r'Band $-0.25<k_x<0.25$', '--','s')]:
    rows=sorted([x for x in D['restricted'] if x['m']==m],key=lambda x:x['t'])
    t=np.array([x['t'] for x in rows]);y=np.array([x['peak'] for x in rows]);y/=y[0]
    ax.loglog(t,y,style,marker=marker,color='black',markersize=4,label=label)
ax.loglog(t,(t/t[0])**(-1.5),':',color='.55',label=r'Reference slope $-3/2$')
ax.set(xticks=t,xlabel='Evolution parameter t',ylabel=r'Weighted peak / peak at $t=16$')
ax.set_xticklabels([str(int(x)) for x in t]);ax.legend(frameon=False,fontsize=9)
save(fig,'restricted_decay')
fig,ax=plt.subplots(figsize=(6.4,2.35),layout='constrained')
a=D['optical_growth'];ax.plot([x['t'] for x in a],[100*x['transverse_fraction'] for x in a],'-o',color='black',markersize=3)
ax.set(xlabel='Optical propagation parameter t',ylabel='Transverse variation (%)',xlim=(0,4),ylim=(0,5.25))
ax.text(.05,4.8,'One prescribed disturbance; checked interval only',fontsize=9)
save(fig,'stripe_growth')
fig,axes=plt.subplots(1,2,figsize=(6.4,2.35),layout='constrained')
a=D['late_peak'];t=np.array([x['t'] for x in a]);y=np.array([x['peak'] for x in a]);floor=D['claims']['periodic_floor']
for ax,mask,title in [(axes[0],np.ones(len(t),dtype=bool),'Full archived trace'),(axes[1],(t>=1536)&(t<=1664),'One late interval')]:
    ax.plot(t[mask],y[mask],color='black',linewidth=.7)
    ax.axhline(floor,color='.45',linestyle='--',linewidth=.9)
    ax.set(xlabel='Propagation parameter t',title=title,ylim=(0,.32))
axes[0].set_ylabel('Sampled envelope peak')
axes[1].text(1540,.041,'Action-imposed floor',fontsize=8)
save(fig,'periodic_peak')
fig,ax=plt.subplots(figsize=(6.4,2.35),layout='constrained')
a=D['pinn'];t=[x['t'] for x in a]
for key,label,style in [('relative_l2','Complex-field relative L2 error','-'),('relative_peak_error','Sampled-peak relative error','--'),('pinn_relative_mass_drift','Absolute relative action drift',':')]:
    ax.plot(t,[100*abs(x[key]) for x in a],style,color='black',label=label)
ax.set(xlabel='Optical propagation parameter t',ylabel='Error or drift (%)',xlim=(0,.5));ax.legend(frameon=False,fontsize=9,loc='upper left')
save(fig,'pinn_errors')
print('Generated four vector PDF figures.')
