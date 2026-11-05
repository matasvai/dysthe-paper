"""Render the actual spatial-audit measurements into Markdown and LaTeX."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];out=root/'results/spatial_reliability'
rows=json.loads((out/'summary.json').read_text())
table=[];locations=[];md=['# Spatial reliability at t=256','',
    'Same four cases, alpha=1/2. Domain sizes and search ranges are changed separately.','',
    '| Equation / input | L: 32768 to 65536 | Radius: 2048 to 4096 | L: 65536 to 131072 | Integral discrepancy | Pass 0.1% peak screen |',
    '|---|---:|---:|---:|---:|---|']
for r in rows:
    c=r['checks'];p=r['continuum_candidate']
    label=('Homogeneous' if r['regime']=='homogeneous_minus' else 'Inhomogeneous')
    name='Gaussian' if r['family']=='gaussian' else 'Near degeneracy'
    keys=['first_longitudinal_change','transverse_expansion_change','second_longitudinal_change','final_spectral_integral_discrepancy']
    nums=[100*c[k] for k in keys]
    table.append(' & '.join([label,name]+[f'{v:.4f}\\%' for v in nums])+r' \\')
    locations.append(' & '.join([label,name,f"{p['ratio']:.7f}",f"{p['x']:.4f}",f"{p['r']:.4f}",f"{c['final_polished_location_drift']:.5f}"])+r' \\')
    md.append('| '+label+' / '+name+' | '+' | '.join(f'{v:.5f}%' for v in nums)+' | '+str(r['passes_peak_screen'])+' |')
s='\\newcommand{\\SpatialRows}{'+'\n'.join(table)+'}\n'
s+='\\newcommand{\\SpatialLocations}{'+'\n'.join(locations)+'}\n'
for key,macro,scale in [('final_polished_location_drift','SpatialLocationDrift',1),('final_polished_peak_drift','SpatialPeakDrift',100),('quadrature_tightening_change','SpatialQuadTighten',100),('boundary_to_peak','SpatialBoundary',100)]:
    value=scale*max(r['checks'][key] for r in rows)
    formatted=f'{value:.5f}'+('\\%' if scale==100 else '')
    if macro=='SpatialQuadTighten':
        a,b=f'{value:.2e}'.split('e');formatted='$'+a+r'\times10^{'+str(int(b))+r'}\%$'
    s+='\\newcommand{\\'+macro+'}{'+formatted+'}\n'
s+='\\newcommand{\\SpatialPassed}{'+str(sum(r['passes_peak_screen'] for r in rows))+'}\n'
assert all(r['continuum_candidate']['success'] and all(p['success'] for p in r['polished']) for r in rows),'An optimizer did not converge; report must disclose it.'
(root/'report/spatial_values.tex').write_text(s)
md+=['','## Candidate peak locations','',
    '| Equation / input | R(256), independent integral | x | r | Location drift between final periods |',
    '|---|---:|---:|---:|---:|']
for r in rows:
    p=r['continuum_candidate'];c=r['checks']
    md.append(f"| {r['regime']} / {r['family']} | {p['ratio']:.8f} | {p['x']:.5f} | {p['r']:.5f} | {c['final_polished_location_drift']:.6f} |")
md+=['','## Interpretation',
    'The 0.1% screen checks each domain expansion, the final locally optimized peak drift, and the independent integral discrepancy. It is a numerical tolerance, not a proof of global maximality.',
    'Longitudinal spacing remains 0.25 and radial spacing remains 2 during the broad scans. Local optimization evaluates continuous coordinates; it is not a full refinement of every radial cell.',
    'The extension annulus samples radii 2050,2052,...,4096, complementing the original 0,2,...,2048 grid.',
    'Independent integration splits at the fractional multiplier cusp and uses Gauss-Legendre orders 256 and 512 on 64 Gaussian-frequency panels plus the cusp split. The stored quadrature_tightening_change now denotes this order-doubling comparison.',
    'The change of variables k=-beta +/- u^2 regularizes each side of the cusp. Final values are recomputed with this formulation.',
    'The initial profiles are exactly L1-normalized Gaussian families. This result applies at t=256, alpha=1/2 and the two specified canonical regimes only.',
    'The calculation searches a finite domain; low boundary amplitudes and stable samples do not exclude all narrow or remote maxima.',
    'Numerical spatial stability strengthens the interpretation of these four computed ratios, but establishes neither an infinite-time decay theorem nor a counterexample.',
    'Reproduce with `python3 spatial_reliability.py` then `python3 report/make_spatial_tables.py`. Per-case JSON checkpoints permit resuming unchanged scans.']
(out/'RESULTS.md').write_text('\n'.join(md)+'\n')
