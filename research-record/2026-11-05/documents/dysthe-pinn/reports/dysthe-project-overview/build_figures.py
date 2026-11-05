"""Build vector diagrams and plots using only the included overview_data.json."""
import json
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-overview-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np

HERE=Path(__file__).resolve().parent
FIG=HERE/'figures'; FIG.mkdir(exist_ok=True)
data=json.loads((HERE/'overview_data.json').read_text())
plt.rcParams.update({'font.family':'serif','font.size':11,'pdf.fonttype':42,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'axes.linewidth':.7,'lines.linewidth':1.8,
                     'savefig.bbox':'tight','savefig.pad_inches':.06})

wave=data['linear'];progress=100*np.array(wave['t'])/wave['t'][-1]
fig,ax=plt.subplots(figsize=(6.1,2.2),layout='constrained')
ax.plot(progress,100*np.array(wave['linf'])/wave['linf'][0],color='k',label='Height of the strongest point')
ax.plot(progress,100*(np.array(wave['l2'])/wave['l2'][0])**2,color='.5',ls='--',label='Total wave-content measure')
ax.set(xlim=(0,100),ylim=(0,118),xlabel='Progress through this simulated journey (%)',ylabel='Starting value = 100%')
ax.legend(loc='lower left',frameon=False,fontsize=9)
ax.text(101,100,'100%',ha='left',va='center',fontsize=10)
ax.text(101,100*wave['linf'][-1],f"{100*wave['linf'][-1]:.0f}%",ha='left',va='center',fontsize=10)
fig.savefig(FIG/'spreading.pdf');plt.close(fig)

growth=data['optical_growth']
progress=100*np.array([r['t'] for r in growth])/growth[-1]['t']
values=100*np.array([r['transverse_fraction'] for r in growth])
fig,ax=plt.subplots(figsize=(6.1,2.05),layout='constrained')
ax.plot(progress,values,color='k');ax.scatter([0,100],values[[0,-1]],color='k',s=18,zorder=3)
ax.annotate('0.5% at the start',(0,values[0]),xytext=(12,30),textcoords='offset points',fontsize=10)
ax.annotate('4.8% at the end',(100,values[-1]),xytext=(-8,6),textcoords='offset points',ha='right',fontsize=10)
ax.set(xlim=(0,102),ylim=(0,5.2),xlabel='Progress through the checked interval (%)',ylabel='Unevenness (%)')
fig.savefig(FIG/'unevenness.pdf');plt.close(fig)

fig,ax=plt.subplots(figsize=(6.1,1.45),layout='constrained')
ax.set(xlim=(0,10.2),ylim=(0,2));ax.axis('off')
for x,title,desc in [(0,'Learn','Practise on examples'),(3.5,'Check','Choose when to stop'),(7,'Test','Try unseen examples')]:
    ax.add_patch(Rectangle((x,.65),3.1,1.2,facecolor='white',edgecolor='k',lw=.7))
    ax.text(x+1.55,1.43,title,ha='center',va='center',fontsize=13)
    ax.text(x+1.55,.95,desc,ha='center',va='center',fontsize=9.5)
for x in [3.1,6.6]:ax.add_patch(FancyArrowPatch((x+.04,1.25),(x+.36,1.25),arrowstyle='->',mutation_scale=12,lw=1))
ax.text(5.05,.21,'A lower practice score must still lead to better test predictions.',ha='center',fontsize=10)
fig.savefig(FIG/'learning.pdf');plt.close(fig)

changes=data['claims']['latest_changes_percent']
fig,ax=plt.subplots(figsize=(6.1,2.35),layout='constrained')
labels=list(changes);vals=list(changes.values());ys=np.arange(3)
ax.barh(ys,vals,color=['.25','.25','.75'],height=.53,edgecolor='k',lw=.5)
ax.axvline(0,color='k',lw=.8)
for y,value in zip(ys,vals):
    ax.text(value+2 if value>0 else value/2,y,f'{abs(value):.0f}% '+('larger' if value>0 else 'smaller'),
            ha='left' if value>0 else 'center',va='center',fontsize=10)
ax.set(yticks=ys,yticklabels=labels,xlim=(-97,92),xticks=[-50,0,50],xlabel='Change relative to the shorter-window model (%)')
ax.invert_yaxis()
ax.text(-55,-.6,'Smaller is better',ha='center',fontsize=9)
ax.text(52,-.6,'Larger is worse',ha='center',fontsize=9)
fig.savefig(FIG/'tradeoff.pdf');plt.close(fig)
print('Created four vector PDF figures from the included numerical snapshot.')
