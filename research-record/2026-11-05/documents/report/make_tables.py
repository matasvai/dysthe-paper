"""Build LaTeX values from actual numerical results; no manually entered measurements."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
r=json.loads((root/'results/verification.json').read_text())
def sci(x):
    s=f'{x:.2e}'; a,b=s.split('e')
    return '$'+a+r'\times10^{'+str(int(b))+'}$'
def cmd(name,value): return '\\newcommand{\\'+name+'}{'+value+'}\n'
text=''
for name,key in [('MassError','l2_max_relative_drift'),('SymmetryError','xy_symmetry_max_error'),
                 ('PlaneError','plane_wave_max_error'),('ReverseError','reversibility_relative_l2'),
                 ('QuadError','quadrature_max_absolute_error')]:
    text+=cmd(name,sci(r['checks'][key]))
text+=cmd('PeakPercent',f"{100*max(d['relative_difference'] for d in r['peak_sampling']):.3f}")
text+=cmd('Runtime',f"{r['wall_seconds']:.1f}")
eps=lambda e:'$-1/3$' if e<0 else f'${e:g}$'
rows=[]
for d in r['final']:
    rows.append(' & '.join([eps(d['epsilon2']),d['case'].replace('_',' '),f"{d['linf']:.3f}"]+[f'{v:.3f}' for v in d['width']])+r' \\')
text+=cmd('FinalRows','\n'.join(rows))
rows=[]
for n in [32,64,96]:
    rows.append(f'${n}^3$ & '+' & '.join(sci(d['relative_l2']) for d in r['convergence'] if d['n']==n)+r' \\')
text+=cmd('GridRows','\n'.join(rows))
rows=[]
for e in [1.,-1/3,0.]:
    vals=[sci(d['common_cube_relative_l2']) for d in r['domains'] if d['epsilon2']==e]
    vals.append(sci(max(d['relative_l2'] for d in r['large_box'] if d['epsilon2']==e)))
    rows.append(eps(e)+' & '+' & '.join(vals)+r' \\')
text+=cmd('DomainRows','\n'.join(rows))
(root/'report/computed_values.tex').write_text(text)
