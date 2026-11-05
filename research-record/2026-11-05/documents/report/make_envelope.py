"""Generate the explanatory envelope diagram (not an additional PDE experiment)."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/dysthe-mpl')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

s = np.linspace(-10, 10, 3000)
envelope = np.exp(-s**2 / 18)
wave = envelope * np.cos(12*s)
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False})
fig, (ax, lower) = plt.subplots(2, 1, figsize=(9, 4.7), sharex=True,
                              layout='constrained', height_ratios=[1.5, 1])
ax.fill_between(s, -envelope, envelope, color='#e8f0f5')
ax.plot(s, wave, color='#236f9c', lw=1, label='Rapidly oscillating real field')
ax.plot(s, envelope, color='#d47d29', lw=2.3, label=r'Envelope bounds $+|E|$ and $-|E|$')
ax.plot(s, -envelope, color='#d47d29', lw=2.3)
ax.set(ylabel='Field amplitude', ylim=(-1.2, 1.6),
       title='The envelope follows the height of the rapid oscillations')
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.axhline(0, color='gray', lw=.5)
lower.plot(s, envelope, color='#d47d29', lw=2.3, label=r'Magnitude $|E|$ (shown in our solution plots)')
lower.plot(s, envelope**2, color='#923953', lw=2, ls='--', label=r'Normalized intensity $|E|^2$')
lower.set(xlabel=r'Coordinate along an illustrative slice, $s$',
          ylabel='Normalized value', ylim=(0,1.12), xlim=(-10,10))
lower.legend(loc='upper right', fontsize=9, frameon=False)
for a in (ax,lower): a.grid(alpha=.15)
out=Path(__file__).resolve().parent/'figures'
out.mkdir(exist_ok=True)
fig.savefig(out/'envelope_explanation.pdf')
plt.close(fig)
