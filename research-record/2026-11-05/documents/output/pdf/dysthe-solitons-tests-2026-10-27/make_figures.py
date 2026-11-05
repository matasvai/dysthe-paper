"""Rebuild vector figures from the archived review data; no PDE or ML training."""
from pathlib import Path
import csv
import json
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/dysthe-review-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'serif', 'font.size': 10,
                     'pdf.fonttype': 42, 'ps.fonttype': 42,
                     'axes.spines.top': False, 'axes.spines.right': False})
rows = list(csv.DictReader((ROOT / 'data/cpu-errors.csv').open()))
methods = ['pinn_slabs', 'pinn_scratch', 'pinn_nls_warm', 'fno', 'pino']
names = ['Slab PINN', 'Global PINN', 'NLS-warm PINN', 'FNO', 'PINO']
values = [100 * float(next(r for r in rows if r['method'] == m and
          r['split'] == 'test' and float(r['horizon']) == 2)['max_l2']) for m in methods]
fig, ax = plt.subplots(1, 2, figsize=(7, 2.8), layout='constrained')
ax[0].barh(names[::-1], values[::-1], color=['.65', '.4', '.8', '.6', '.2'])
ax[0].set_xscale('log')
ax[0].set_xlabel(r'Worst test relative $L^2$ error (%)')
ax[0].set_title(r'CPU pilot through $\xi=2$')
ax[0].axvline(1, ls=':', color='k', lw=1)
ax[0].set_xlim(.5, 110)
for i, v in enumerate(values[::-1]):
    ax[0].text(v * 1.08, i, f'{v:.2f}', va='center', fontsize=9)
for m, name, style in [('fno', 'FNO', '-o'), ('pino', 'PINO', '--s'),
                        ('pinn_slabs', 'Slab PINN', ':^')]:
    selected = sorted([r for r in rows if r['method'] == m and r['split'] == 'test'],
                      key=lambda r: float(r['horizon']))
    ax[1].plot([float(r['horizon']) for r in selected],
               [100 * float(r['max_l2']) for r in selected], style, color='k',
               label=name, ms=4, lw=1.2)
ax[1].axhline(1, ls=':', color='.5', lw=.8)
ax[1].set_yscale('log')
ax[1].set_xlabel(r'Propagation distance $\xi$')
ax[1].set_ylabel(r'Worst test $L^2$ error (%)')
ax[1].set_title('Error growth with distance')
ax[1].legend(frameon=False, fontsize=8)
fig.savefig(ROOT / 'figures/cpu-comparison.pdf')
plt.close(fig)

audit = json.loads((ROOT / 'data/projection-audit.json').read_text())
profile = audit['data']['stored_Dysthe_eps0.025_mu2']
fig, ax = plt.subplots(figsize=(6.8, 2.7), layout='constrained')
for name, label, style in [('relative_l2', r'$L^2$', '-o'),
                          ('relative_h1', r'$H^1$', '--s'),
                          ('relative_h2', r'$H^2$', ':^')]:
    ax.plot([r['K'] for r in profile], [100*r[name] for r in profile],
            style, color='k', label=label, ms=5)
ax.axhline(5, color='.6', lw=.8)
ax.text(390, 5, r'5% $H^2$ field gate', ha='right', va='bottom', fontsize=8)
ax.axhline(.5, color='.6', lw=.8, ls='--')
ax.text(390, .5, '0.5% proposed projection budget', ha='right', va='bottom', fontsize=8)
ax.set_yscale('log')
ax.set_xticks([48, 96, 192, 256, 384])
ax.set_xlabel(r'Retained Fourier cutoff $K$ on a period $L=160$')
ax.set_ylabel('Unavoidable relative error (%)')
ax.set_ylim(4e-5, 120)
ax.legend(frameon=False, loc='lower left', ncol=3)
fig.savefig(ROOT / 'figures/projection-floor.pdf')
plt.close(fig)
summary = json.loads((ROOT / 'data/gpu2-snapshot/summary.json').read_text())
metrics = ['l2', 'h1', 'h2', 'peak']
tolerances = np.array([.01, .05, .05, .05])
fig, ax = plt.subplots(figsize=(6.4, 2.2), layout='constrained')
x = np.arange(4)
for offset, split, color in [(-.18, 'validation', '.3'), (.18, 'test', '.75')]:
    row = next(r for r in summary['pinn_aggregates'] if r['split'] == split and r['horizon'] == 4)
    ratios = np.array([row['worst_errors'][m] for m in metrics]) / tolerances
    ax.bar(x + offset, ratios, width=.34, color=color, label=split.capitalize())
    for xx, yy in zip(x + offset, ratios):
        ax.text(xx, yy + .08, f'{yy:.2f}', ha='center', va='bottom', fontsize=8)
ax.axhline(1, color='k', ls='--', lw=1)
ax.set_xticks(x, [r'$L^2$', r'$H^1$', r'$H^2$', 'Peak amplitude'])
ax.set_ylabel('Worst error / gate')
ax.set_ylim(0, 7)
ax.legend(frameon=False, ncol=2, loc='upper left', fontsize=9)
fig.savefig(ROOT / 'figures/gpu-gates.pdf')
plt.close(fig)
print('Wrote three vector PDF figures from saved numerical records.')
