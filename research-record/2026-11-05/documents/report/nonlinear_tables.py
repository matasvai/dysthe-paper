"""Rebuild report tables directly from the saved nonlinear experiment summaries."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=json.loads((R/'results/nonlinear/analysis_summary.json').read_text())
O=R/'report/nonlinear_tables';O.mkdir(exist_ok=True)
def num(x):
 if x==0:return '0'
 if abs(x)>=.001:return f'{x:.6g}'
 a,b=f'{x:.2e}'.split('e');return rf'{a}\times10^{{{int(b)}}}'
def table(name,header,rows):
 text='\\begin{tabular}{'+'r'*len(header)+'}\n\\toprule\n'+' & '.join(header)+r' \\'+'\n\\midrule\n'
 for row in rows:text+=' & '.join(str(v) for v in row)+r' \\'+'\n'
 text+='\\bottomrule\n\\end{tabular}\n';(O/(name+'.tex')).write_text(text)
def math(x):return '$'+num(x)+'$'
table('nls',['$N$','$L$','$h$','$e_{\\rm field}(20)$','$D_A$'],[[r['n'],r['L'],r['dt'],math(r['final_error']),math(r['mass_drift'])] for r in s['benchmark']])
table('profile_checks',['$N$','$L$','$A$','$\\max|F|$','$r_F$'],[[r['n'],r['L'],f"{r['mass']:.9f}",f"{r['peak']:.9f}",math(r['profile_residual'])] for r in s['profile_checks']])
table('branches',['$\\mu$','$s$','$\\epsilon$','$A$','$\\max|F|$','Iterations'],[[r['mu'],r['speed'],r['epsilon'],f"{r['mass']:.6f}",f"{r['peak']:.6f}",r['iterations']] for r in s['profiles'] if r['epsilon'] in [0,.05,.1,.15]])
table('propagation',['$\\epsilon$','$s$','$e_{\\rm field}(20)$','$e_{\\rm orb}(20)$','$D_A$','$D_{\\mathcal E}$'],[[r['epsilon'],r['speed'],math(r['error']),math(r['aligned']),math(r['mass_drift']),math(r['energy_drift'])] for r in s['propagation']])
rr=[]
for h,n in [(.01,'timestep_dysthe_0.01'),(.005,'timestep_dysthe_0.005'),(.0025,'prop_e0.15_s2'),(.00125,'timestep_dysthe_0.00125')]:
 d=json.loads((R/f'results/nonlinear/{n}.json').read_text())['diagnostics'];rr.append([h,math(d[-1]['complex_error']),math(d[-1]['aligned_error'])])
table('dysthe_time',['$h$','$e_{\\rm field}(20)$','$e_{\\rm orb}(20)$'],rr)
rr=[]
for r in s['collisions']:
 if r['epsilon']==0 and r['dt']==.0025:continue
 rr.append([r['epsilon'],r['n'],f"{r['L']:g}",r['dt'],f"{100*r['excess_tail_fraction']:.5f}",f"{r['outgoing_fits'][0]['aligned_error']:.5f}",f"{r['outgoing_fits'][1]['aligned_error']:.5f}",math(r['energy_drift'])])
table('collision',[r'$\epsilon$','$N$','$L$','$h$',r'$100\Delta R_6$',r'$e_+$',r'$e_-$',r'$D_{\mathcal E}$'],rr)
labels={'perturb_amplitude_-0.01':'Amplitude $-0.01$','perturb_amplitude_0.01':'Amplitude $+0.01$','perturb_phase_0.01':'Phase $0.01$','perturb_refined_0.01':'Amplitude $+0.01$, fine $h$','perturb_refined_0':'Unperturbed, fine $h$'}
table('perturb',['Initial change',r'$e_{\rm orb}(0)$',r'$e_{\rm orb}(40)$',r'$a(40)$',r'$D_A$'],[[labels[r['name']],math(r['initial_aligned']),math(r['final_aligned']),f"{r['translation']:.6f}",math(r['mass_drift'])] for r in s['perturbations']])
labels={'optical3d_stripe':'Unperturbed','optical3d_mixed':'Coarse','optical3d_mixed_time':'Coarse, half $h$','optical3d_mixed_grid':'First grid refinement','optical3d_mixed_domain':'Larger box','transverse_refined_fine':'A','transverse_refined_time':'B','transverse_refined_finer':'C','transverse_refined_length':'D','transverse_refined_xfine':'E'}
for name,rr in [('early',[r for r in s['transverse'] if r['final_t']==4]),('late',[r for r in s['transverse'] if r['final_t']==8])]:
 table(name,['Run',r'$V(T)$',r'$\|E(T)\|_\infty$',r'$D_A$',r'$\max S_{\rm edge}$'],[[labels[r['name']],f"{r['fraction']:.8f}",f"{r['peak']:.8f}",math(r['mass_drift']),math(r['spectral_edge'])] for r in rr])
print('Report tables built')
