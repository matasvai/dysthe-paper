"""Refresh the compact report snapshot from the original workspace; no simulation."""
import hashlib, json, math
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
hashes = {}
def read(rel):
    p = ROOT / rel
    hashes[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return json.loads(p.read_text())
restricted=[]
for p in sorted((ROOT/'results/restricted_decay').glob('s*_m*_t*.json')):
    x=read(str(p.relative_to(ROOT)))
    restricted.append({k:x[k] for k in ('sx','sy','m','t','peak','ratio','x','r','passes_1pct_screen')} | {'passes_after_followup': bool(x['passes_1pct_screen'] or x.get('followup',{}).get('passes_1pct_screen',False))})
extended=read('results/extended_decay/summary.json')
extended=[{k:x[k] for k in ('regime','family','t','peak','ratio','x','r','passes_screen')} for x in extended]
for row in extended:
    case=read(f"results/extended_decay/{row['regime']}_{row['family']}_{int(row['t'])}.json")
    row['passes_after_followup']=bool(row['passes_screen'] or case.get('followup',{}).get('passes_screen', False))
assert all(x['passes_after_followup'] for x in extended)
for p in (ROOT/'results/extended_decay').glob('*.json'):
    # Record the separately stored follow-up as well as summary provenance.
    hashes[str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
nonlinear=read('results/nonlinear/analysis_summary.json')
growth=read('results/nonlinear/transverse_refined_fine_history.json')
metrics=read('dysthe-pinn/results/evaluation-001/metrics.json')
training=read('dysthe-pinn/results/training-001/summary.json')
late=read('dysthe-pinn/results/late-window-1024-2048/summary.json')
preview=read('dysthe-pinn/results/breathing-preview-12288/summary.json')
for rel in ['results/verification.json','results/spatial_reliability/summary.json','results/research_experiments/summary.json','results/restricted_decay/config.json','results/restricted_decay/verification.json','dysthe-pinn/results/evaluation-001/reference-audit.json','dysthe-pinn/results/long-reference-77502/sequence-summary.json','dysthe-pinn/results/time-step-pilot/summary.json','dysthe-pinn/results/overnight-time-step-pilot/summary.json','dysthe-pinn/reports/late-window-review/review-statistics.json','dysthe-pinn/reports/late-window-review/oscillation-fit.json']:
    read(rel)
for rel in ['results/norm_history.csv','results/decay_dataset/RESULTS.md','results/decay_dataset/REFINEMENT.md','results/decay_dataset/refinement_checks.json','results/long_time/summary.json','output/packet_alternative_views/README.md','results/nonlinear/profile_checks.json','results/nonlinear/timestep_dysthe_0.01.json','results/nonlinear/timestep_dysthe_0.00125.json']:
    p=ROOT/rel
    hashes[rel]=hashlib.sha256(p.read_bytes()).hexdigest()
slopes=[]
for sx,m in sorted({(x['sx'],x['m']) for x in restricted}):
    a={x['t']:x['peak'] for x in restricted if (x['sx'],x['m'])==(sx,m)}
    slopes.append({'sx':sx,'m':m,'p_128_256':math.log(a[128]/a[256],2)})
claims={
 'restricted_initial_passes':sum(x['passes_1pct_screen'] for x in restricted),
 'restricted_passes_after_followup':sum(x['passes_after_followup'] for x in restricted),
 'restricted_count':len(restricted),
 'growth_initial_percent':100*growth[0]['transverse_fraction'],
 'growth_final_percent':100*growth[-1]['transverse_fraction'],
 'pinn_max_relative_l2':metrics['max_relative_l2'],
 'pinn_max_relative_peak_error':metrics['max_relative_peak_error'],
 'pinn_max_action_drift':metrics['max_pinn_relative_mass_drift'],
 'pinn_updates':metrics['checkpoint_step'],
 'periodic_floor':math.sqrt(late['rows'][0]['mass']/math.prod(late['config']['domain']['lengths'])),
 'late_status':late['status'],'late_end':late['current_t'],
 'late_action_drift':late['max_relative_mass_drift'],
 'preview_status':preview['status'],'preview_end':preview['current_t'],
 'preview_action_drift':preview['max_relative_mass_drift'],
}
assert claims['restricted_count']==40 and claims['restricted_passes_after_followup']==40
out={'as_of':'2026-09-24','qualification':'Archived simulations re-audited; no new long simulation or training. Curves are numerical observations, not rigorous error bounds.','claims':claims,'restricted':restricted,'restricted_slopes':slopes,'extended':extended,'optical_growth':growth,'pinn':metrics['rows'],'late_peak':[{'t':x['t'],'peak':x['peak']} for x in late['rows']],'source_sha256':hashes}
(HERE/'evidence.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(claims,indent=2))
