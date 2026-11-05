"""Illustrative narrowband deep-water packet, separate from the optical solver."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Leading-order narrowband illustration: no packet dispersion or nonlinear correction.
g=9.81; wavelength=4.; k=2*np.pi/wavelength
omega=np.sqrt(g*k); cp=omega/k; cg=cp/2
amplitude=.08; sigma=9.
x=np.linspace(-28,38,700); y=np.linspace(-12,12,120)
X,Y=np.meshgrid(x,y)
A=amplitude*np.exp(-X**2/(2*sigma**2)-Y**2/(2*6.**2))
Z=A*np.cos(k*X)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(10,7.2),layout='constrained')
gs=fig.add_gridspec(3,1,height_ratios=[2.1,1,1])
ax=fig.add_subplot(gs[0],projection='3d')
ax.plot_surface(X,Y,Z,cmap='Blues',vmin=-amplitude,vmax=amplitude,
                rcount=90,ccount=350,linewidth=0,antialiased=True,rasterized=True)
ax.plot(x,np.zeros_like(x),amplitude*np.exp(-x*x/(2*sigma*sigma)),
        color='#d47d29',lw=2.5,label='Envelope along the centerline')
ax.set(xlabel='x (m)',ylabel='y (m)',zlabel='',
       title='Water surface: several crests form one larger wave packet')
ax.set_xticks([-20,0,20,40]);ax.set_yticks([-10,0,10]);ax.set_zticks([-.08,0,.08])
ax.tick_params(labelsize=8,pad=0)
ax.set_box_aspect((3.7,1.5,.65),zoom=1.5); ax.view_init(elev=24,azim=-65)
ax.legend(loc='upper left',fontsize=9)
for i,t in enumerate([0.,4.]):
    a=fig.add_subplot(gs[i+1])
    env=amplitude*np.exp(-(x-cg*t)**2/(2*sigma*sigma))
    eta=env*np.cos(k*x-omega*t)
    a.fill_between(x,-.11,eta,color='#d4e8f0')
    a.plot(x,eta,color='#236f9c',lw=1.5,label='Water surface')
    a.plot(x,env,color='#d47d29',lw=2,label='Envelope bounds')
    a.plot(x,-env,color='#d47d29',lw=1.5,ls='--')
    a.axvline(cg*t,color='#d47d29',ls=':',lw=1.5)
    a.plot(cp*t,amplitude*np.exp(-((cp-cg)*t)**2/(2*sigma*sigma)),
           'o',color='#923953',ms=6,label='Same carrier phase')
    a.set(xlim=(-28,38),ylim=(-.11,.13),ylabel='Elevation (m)',
          title=f'Centerline at t = {t:g} s: packet center {cg*t:.1f} m; phase marker {cp*t:.1f} m')
    a.grid(alpha=.15)
    if i==0:a.legend(loc='upper right',fontsize=8,ncol=3)
    else:a.set_xlabel('Distance along propagation, x (m)')
out=Path(__file__).resolve().parent/'figures'
fig.savefig(out/'water_packet.pdf')
fig.savefig(out/'water_packet.png',dpi=160)
plt.close(fig)
