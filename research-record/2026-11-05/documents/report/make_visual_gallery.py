"""Reproducible qualitative views; distinct from the t=256 peak audit."""
import sys, os, json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.ndimage import zoom
import torch
from decay_dataset import setup, weighted
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'report/visuals'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titleweight':'bold','axes.labelcolor':'#18384b','text.color':'#18384b','axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})
colors=['#168f9a','#d98542','#6858ac']
def save(fig,name):
 fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight',dpi=160);fig.savefig(OUT/(name+'.png'),bbox_inches='tight',dpi=140);plt.close(fig)
def mesh(v, level, x):
 # Marching tetrahedra, consistent six-tetrahedron decomposition of each cube.
 corners=np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]])
 tet=[[0,1,2,6],[0,2,3,6],[0,3,7,6],[0,7,4,6],[0,4,5,6],[0,5,1,6]]
 vals=np.stack([v[a:a+v.shape[0]-1,b:b+v.shape[1]-1,c:c+v.shape[2]-1] for a,b,c in corners],axis=-1)
 active=(vals.min(-1)<level)&(vals.max(-1)>=level)
 bases=np.argwhere(active); vv=vals[active]; triangles=[]
 for ids in tet:
  tv=vv[:,ids]; good=(tv.min(1)<level)&(tv.max(1)>=level)
  for base,values in zip(bases[good],tv[good]):
   p=base+corners[ids]; ins=np.flatnonzero(values>=level); outs=np.flatnonzero(values<level)
   def edge(i,j):return p[i]+(level-values[i])/(values[j]-values[i])*(p[j]-p[i])
   if len(ins)==1:triangles.append([edge(ins[0],j) for j in outs])
   elif len(ins)==3:triangles.append([edge(outs[0],j) for j in ins])
   else:
    a,b=ins;c,d=outs; ac,ad,bc,bd=edge(a,c),edge(a,d),edge(b,c),edge(b,d)
    triangles.extend([[ac,ad,bc],[ad,bd,bc]])
 return np.asarray(triangles)*(x[1]-x[0])+x[0]
def volume(ax,v,x,color):
 # Threshold is a fraction of each snapshot's full-volume sampled maximum.
 tri=mesh(v,.3*v.max(),x)
 coll=Poly3DCollection(tri,facecolor=color,edgecolor='none',alpha=.8,rasterized=True)
 ax.add_collection3d(coll); ax.set(xlim=(-18,18),ylim=(-18,18),zlim=(-18,18),xlabel='$x$',ylabel='$y$',zlabel='$z$')
 ax.set_box_aspect((1,1,1));ax.view_init(23,-55)
 for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_ticks([-15,0,15]);axis.pane.fill=False
fig=plt.figure(figsize=(9,11)); cuts,meta=[],[]
for row,seed in enumerate([11,22,33]):
 x,f,fh,w,K=setup(f'random_{seed}',-1,0.,128,96)
 xx=x.numpy(); idx=np.flatnonzero(abs(xx)<=18)
 fields=[f,torch.fft.ifftn(fh*torch.exp(4j*w))]
 for col,u in enumerate(fields):
  a=u.abs().numpy(); crop=a[np.ix_(idx,idx,idx)]; assert crop.max()==a.max()
  ax=fig.add_subplot(3,2,row*2+col+1,projection='3d');volume(ax,crop,xx[idx],colors[row]);ax.set_title(f'Seed {seed}  |  t = {4*col}\npeak = {a.max():.3g}',pad=5)
  meta.append({'seed':seed,'t':4*col,'sampled_peak':float(a.max()),'l2':float(torch.linalg.vector_norm(u)*.75**1.5)})
 cuts.append((seed,xx,fields[0][:,64,64].numpy(),fields[1][:,64,64].numpy()))
 if seed==33:
  weighted33=weighted(fh,w,K,0.,4,.5).abs().numpy(); amp33=fields[1].abs().numpy(); complex33=fields[1].numpy()
fig.subplots_adjust(hspace=.25,wspace=.05,top=.96,bottom=.04);save(fig,'random_volumes')
fig,axs=plt.subplots(3,2,figsize=(9,8),sharex=True)
for row,(seed,xx,f,u) in enumerate(cuts):
 scale=np.max(abs(f))
 for col,v in enumerate([f,u]):
  env=abs(v)/scale; carrier=np.real(v*np.exp(3j*xx))/scale
  ax=axs[row,col];ax.fill_between(xx,-env,env,color=colors[row],alpha=.12);ax.plot(xx,carrier,color='#18384b',lw=.9);ax.plot(xx,env,color=colors[row],lw=1.8);ax.plot(xx,-env,color=colors[row],lw=1.1)
  ax.set(xlim=(-18,18),ylim=(-1.12,1.12),title=f'Seed {seed}  |  t = {4*col}',ylabel='Slice amplitude / initial slice peak');ax.grid(alpha=.15)
for ax in axs[-1]:ax.set_xlabel('$x$ at $y=z=0$')
fig.tight_layout();save(fig,'random_carriers')
sel=np.flatnonzero(abs(xx)<=18); X,Y=np.meshgrid(xx[sel],xx[sel],indexing='ij')
u=complex33[np.ix_(sel,sel,[64])][:,:,0]; env=abs(u); carrier=np.real(u*np.exp(3j*X));norm=env.max()
fig=plt.figure(figsize=(8,4));ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,carrier/norm,cmap='coolwarm',linewidth=0,rasterized=True,rcount=49,ccount=49)
ax.plot_wireframe(X,Y,env/norm,rstride=4,cstride=4,color='#168f9a',lw=.6,alpha=.7)
ax.set(xlabel='$x$',ylabel='$y$',zlim=(-1,1.1),title='Carrier and positive envelope / relative amplitude');ax.view_init(24,-65);ax.set_box_aspect((1.7,1,.55),zoom=1.5);ax.set_xticks([-15,0,15]);ax.set_yticks([-15,0,15]);ax.set_zticks([-1,0,1]);fig.savefig(OUT/'hero.pdf',dpi=160);fig.savefig(OUT/'hero.png',dpi=140);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(9,3.7))
for ax,v,title in zip(axs,[amp33,weighted33],['Envelope magnitude $|S(4)f|$','Weighted magnitude $|W(4)|$']):
 im=ax.imshow(v[np.ix_(sel,[64],sel)][:,0,:].T,origin='lower',extent=[xx[sel[0]]-.375,xx[sel[-1]]+.375]*2,cmap='magma');ax.set(title=title,xlabel='$x$',ylabel='$z$ at $y=0$');fig.colorbar(im,ax=ax,shrink=.8,format='%.1e')
fig.tight_layout();save(fig,'weighted_comparison')
summary=json.loads((ROOT/'results/spatial_reliability/summary.json').read_text())
fig,ax=plt.subplots(figsize=(9,3.8)); yy=np.arange(4); labels=['Homogeneous / Gaussian','Homogeneous / near degeneracy','Inhomogeneous / Gaussian','Inhomogeneous / near degeneracy']
for j,(key,label,c) in enumerate([('first_longitudinal_change','First length doubling','#168f9a'),('second_longitudinal_change','Second length doubling','#6858ac'),('final_spectral_integral_discrepancy','Independent integral','#d98542')]):
 ax.barh(yy+(j-1)*.22,[100*s['checks'][key] for s in summary],height=.19,label=label,color=c)
ax.axvline(.1,color='#a54046',ls='--',lw=1.5,label='0.1% screening target');ax.set(yticks=yy,yticklabels=labels,xlabel='Relative difference (%)',xlim=(0,.108));ax.invert_yaxis();ax.grid(axis='x',alpha=.15);ax.legend(loc='lower right',fontsize=8);fig.tight_layout();save(fig,'reliability')
(OUT/'gallery_manifest.json').write_text(json.dumps({'purpose':'Qualitative gallery, not a new whole-space bound check','grid':128,'length':96,'spacing':.75,'regime':'homogeneous_minus','seeds':[11,22,33],'isosurface_fraction':.3,'carrier_wavenumber_illustrative':3,'records':meta},indent=2))
print('Gallery complete',flush=True)
