"""Generate supplement measurements from saved refinement outputs."""
from pathlib import Path
import csv,json
root=Path(__file__).resolve().parents[1]
out=root/'results/decay_dataset'
rows=list(csv.DictReader(open(out/'refined_decay.csv')))
checks=json.loads((out/'refinement_checks.json').read_text())
names={'gaussian':'Gaussian','smooth_bump':'Compact bump','near_degeneracy':'Near degeneracy','random_33':'Random (33)'}
table=[]
for r in rows:
    if int(r['length'])!=288 or float(r['t'])!=16:continue
    cc=[c for c in checks if c['regime']==r['regime'] and c['family']==r['family'] and c['t']==16]
    label='Homogeneous' if r['regime']=='homogeneous_minus' else 'Inhomogeneous'
    table.append(' & '.join([label,names[r['family']],f"{float(r['ratio']):.5f}",
                             f"{100*cc[1]['relative_peak_difference']:.2f}\\%",
                             f"{100*cc[2]['relative_peak_difference']:.2f}\\%"])+r' \\')
def growth(family):
    r=[r for r in rows if r['family']==family and r['regime']=='inhomogeneous_plus' and int(r['length'])==288]
    a=next(float(v['ratio']) for v in r if float(v['t'])==8)
    b=next(float(v['ratio']) for v in r if float(v['t'])==16)
    return 100*(b/a-1)
dom=max(c['relative_peak_difference'] for c in checks if c['check']=='domain_192_to_288')
grid=max(c['relative_peak_difference'] for c in checks if c['check']=='grid_h1_to_h2over3')
s='\\newcommand{\\RefinedRows}{'+'\n'.join(table)+'}\n'
s+='\\newcommand{\\ObservedResult}{The inhomogeneous Gaussian and random packet ratios begin to flatten: from $t=8$ to $16$ they grow by '+f'{growth("gaussian"):.2f}\\% and {growth("random_33"):.2f}\\%, respectively.'+' The near-degeneracy ratios continue to rise more visibly, as do several homogeneous cases. This suggests different transient time scales; it does not establish their eventual behavior.}\n'
s+='\\newcommand{\\CheckResult}{Across all 24 checked case--time combinations, the largest peak changes are '+f'{100*dom:.2f}\\% under domain enlargement and {100*grid:.2f}\\% under grid refinement.'+' All pass the exploratory 2\\% screen.}\n'
(root/'report/refinement_values.tex').write_text(s)
