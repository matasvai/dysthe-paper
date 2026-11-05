from pathlib import Path
import json,math
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'results/long_time/summary.json').read_text())
out=[]
for reg in ['homogeneous_minus','inhomogeneous_plus']:
    for family in ['gaussian','near_degeneracy']:
        a=next(r for r in rows if r['regime']==reg and r['family']==family and r['t']==128)
        b=next(r for r in rows if r['regime']==reg and r['family']==family and r['t']==256)
        gamma=7/6-math.log(b['ratio']/a['ratio'])/math.log(2)
        label='Homogeneous' if reg=='homogeneous_minus' else 'Inhomogeneous'
        name='Gaussian' if family=='gaussian' else 'Near degeneracy'
        out.append(' & '.join([label,name,f"{a['ratio']:.5f}",f"{b['ratio']:.5f}",f'{gamma:.3f}'])+r' \\')
s='\\newcommand{\\LongRows}{'+'\n'.join(out)+'}\n'
end=[r for r in rows if r['t']==256]
s+='\\newcommand{\\LongDomain}{'+f"{100*max(r['extra_domain_change'] for r in end):.3f}"+r'\%}'+'\n'
s+='\\newcommand{\\LongQuad}{'+f"{100*max(r['quadrature_relative_error'] for r in end):.3f}"+r'\%}'+'\n'
s+='\\newcommand{\\LongEdge}{'+f"{100*max(r['edge_to_peak'] for r in end):.3f}"+r'\%}'+'\n'
(root/'report/long_time_values.tex').write_text(s)
