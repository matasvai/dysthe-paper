"""Collect a small, traceable snapshot of the wider Dysthe project's results."""
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
used = {}

def source(name):
    path = PROJECT/name
    used[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return path

def read(name):
    return json.loads(source(name).read_text())

with source('results/norm_history.csv').open() as f:
    wave = [r for r in csv.DictReader(f) if r['epsilon2']=='1.0' and r['case']=='unshifted']
assert len(wave)==25
wave = {k:[float(r[k]) for r in wave] for k in ['t','linf','l2']}
growth = read('results/nonlinear/transverse_refined_fine_history.json')
nonlinear = read('results/nonlinear/analysis_summary.json')
linear_checks = read('results/verification.json')
spatial = read('results/spatial_reliability/summary.json')
research = read('results/research_experiments/summary.json')
restricted = read('results/restricted_decay/summary.json')
pinn = read('dysthe-pinn/results/evaluation-001/metrics.json')
pinn_audit = read('dysthe-pinn/results/evaluation-001/reference-audit.json')
late = read('dysthe-pinn/results/late-window-1024-2048/summary.json')
preview = read('dysthe-pinn/results/breathing-preview-12288/summary.json')
overnight = read('dysthe-pinn/reports/plasma-nonlinear-77761-analysis/analysis.json')
stability = read('dysthe-pinn/reports/plasma-stability-78140-review/analysis.json')
for p in ['README.md','nonlinear/README.md','dysthe-pinn/README.md',
          'report/nonlinear_solitary_wave_report.tex',
          'dysthe-pinn/reports/late-window-review/report.tex',
          'dysthe-pinn/reports/plasma-stability-78140-review/report.tex']:
    source(p)
baseline = stability['aggregates']['rollout12']
selected = stability['aggregates']['rollout24']
changes = {
    'Particle-pattern error':100*(selected['mean_distribution_error']['mean']/baseline['mean_distribution_error']['mean']-1),
    'Electric-field error':100*(selected['mean_electric_error']['mean']/baseline['mean_electric_error']['mean']-1),
    'Worst energy imbalance':100*(selected['max_energy_drift']['maximum']/baseline['max_energy_drift']['maximum']-1)
}
claims = {
    'linear_final_peak':wave['linf'][-1],
    'linear_total_wave_content_relative_change':max(abs((v/wave['l2'][0])**2-1) for v in wave['l2']),
    'linear_spatial_audit_passed':sum(r['passes_peak_screen'] for r in spatial),
    'linear_spatial_audit_cases':len(spatial),
    'additional_frequency_checks':research['sweep_total'],
    'restricted_decay_checks_passed':sum(r['passes_1pct_screen'] for r in restricted),
    'restricted_decay_checks_total':len(restricted),
    'nonlinear_profiles':len(nonlinear['profiles']),
    'maximum_profile_residual':max(r['profile_residual'] for r in nonlinear['profiles']),
    'refined_collision_excess_outside_cores':next(r['excess_tail_fraction'] for r in nonlinear['collisions'] if r['name']=='collision_refined_N8192_h0.000625'),
    'growth_initial_percent':100*growth[0]['transverse_fraction'],
    'growth_final_percent':100*growth[-1]['transverse_fraction'],
    'pinn_max_field_error_percent':100*pinn['max_relative_l2'],
    'pinn_training_updates':pinn['checkpoint_step'],
    'pinn_reference_audit_passed':pinn_audit['status']=='pass',
    'pinn_reference_grid_error':pinn_audit['comparisons']['grid']['max_relative_l2'],
    'long_optical_end':late['current_t'],
    'long_optical_status':late['status'],
    'coarse_optical_end':preview['current_t'],
    'coarse_optical_status':preview['status'],
    'first_plasma_training_seeds':len(overnight['seeds']),
    'latest_training_runs':stability['verification']['training_runs_checked'],
    'latest_tested_models':stability['verification']['evaluation_exports_checked'],
    'latest_random_cases':44,
    'latest_diagnostic_cases':4,
    'latest_passed_screens_per_model':[sum(v['passed'] for v in r['acceptance']['checks'].values()) for runs in stability['test'].values() for r in runs],
    'latest_control_worst_energy_percent':100*baseline['max_energy_drift']['maximum'],
    'latest_selected_worst_energy_percent':100*selected['max_energy_drift']['maximum'],
    'latest_changes_percent':changes,
    'latest_elapsed_hours':stability['session']['session_seconds']/3600
}
assert claims['nonlinear_profiles']==28
assert claims['pinn_max_field_error_percent']<.7 and claims['pinn_reference_audit_passed']
assert claims['latest_passed_screens_per_model']==[1]*6
data = dict(as_of='2026-09-23', claims=claims,
            linear=wave, optical_growth=growth,
            input_source_sha256=used,
            limits=['Archive synthesis, not a new experiment or independent rerun.',
                    'Optical, water-wave and kinetic-plasma models are distinct.',
                    'Plasma campaigns use different test sets and training budgets: no cross-campaign ranking.',
                    'No laboratory or naturally observed input data were evaluated in the reviewed experiments.'])
(HERE/'overview_data.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(claims,indent=2))
