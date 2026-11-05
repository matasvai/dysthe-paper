#!/usr/bin/env python3
"""Reproduce spatial free-surface PINN figures from the included CSV data.

Ordinary use: python make_spatial_figures.py
Rebuild data first: add --run-root RAW --evidence AUDIT.json --config CONFIG.json.
The extraction preserves production complex64 Fourier interpolation and evaluates
all modes/stations without phase alignment, smoothing, or learned-band filtering.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import resample

MODEL = 'water-wave-dysthe-spatial-v1'
CASES = ['packet-008', 'sideband-008', 'random-008']
METHODS = ['none', 'inverse_1_plus_k2']
NAMES = {'none': 'Baseline', 'inverse_1_plus_k2': 'Conditioned'}
STYLE = {'none': {'color': '.4', 'linestyle': '--', 'linewidth': 1.4},
         'inverse_1_plus_k2': {'color': 'black', 'linestyle': '-', 'linewidth': 1.3}}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_csv(path, rows):
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path):
    with path.open() as handle:
        return list(csv.DictReader(handle))


def extract(args, report):
    audit = json.loads(args.evidence.read_text())
    config = json.loads(args.config.read_text())
    if sha(args.config) != audit['config_sha256'] or config['model_id'] != MODEL:
        raise ValueError('Evidence/configuration identity mismatch')
    length = config['length']
    rows, profiles, spectra, costs, residuals, checks = [], [], [], [], [], []
    expected = {(r['case_id'], r['scaling']): r for r in audit['fits']}
    maxima = []
    for case in CASES:
        saved = {}
        for method in METHODS:
            item = expected[(case, method)]
            source = args.run_root / f'{case}-{method}'
            paths = [(source/'fields.npz', item['prediction_reference_sha256']),
                     (source/'pinn-summary.json', item['summary_sha256'])]
            paths.extend((source/path, digest) for path, digest in item['checkpoints'].items())
            for path, digest in paths:
                actual = sha(path)
                if actual != digest:
                    raise ValueError(f'Hash mismatch: {path}')
                checks.append({'file': str(path.relative_to(args.run_root)), 'sha256': actual})
            with np.load(source/'fields.npz', allow_pickle=False) as archive:
                pred, truth, xi = archive['prediction'], archive['reference'], archive['xi']
            if pred.shape != (81, 256) or truth.shape != (81, 1024):
                raise ValueError('Unexpected original study dimensions')
            # This intentionally matches production: interpolate complex64 before
            # subtracting the complex128 truth. Do not filter high error modes.
            interpolated = resample(pred, truth.shape[-1], axis=-1)
            n = truth.shape[-1]
            k = 2*np.pi*np.fft.fftfreq(n, d=length/n)
            modes = np.rint(np.fft.fftfreq(n)*n).astype(int)
            transformed = np.fft.fft(truth, axis=-1)
            diff = np.fft.fft(interpolated-truth, axis=-1)
            errors = {f'h{order}': np.sqrt(np.sum((1+k*k)**order*abs(diff)**2, axis=-1)
                       / np.sum((1+k*k)**order*abs(transformed)**2, axis=-1))
                      for order in range(3)}
            errors['l2'] = errors.pop('h0')
            errors['peak'] = abs(abs(interpolated).max(axis=-1)-abs(truth).max(axis=-1))/abs(truth).max(axis=-1)
            measured = {key: float(values.max()) for key, values in errors.items()}
            for key, value in measured.items():
                if not np.isclose(value, item['errors'][key], rtol=5e-6, atol=2e-8):
                    raise ValueError(f'Recomputed maximum disagrees: {case}/{method}/{key}')
            maxima.append({'case_id': case, 'method': method, **measured})
            for j, distance in enumerate(xi):
                rows.append({'case_id': case, 'method': method, 'xi': distance,
                             **{key: values[j] for key, values in errors.items()}})
            weighted_power = (1+k*k)**2*abs(diff[-1])**2
            denominator = float(np.sum((1+k*k)**2*abs(transformed[-1])**2))
            # Signed powers retain both sidebands and all 1024 modes.
            for j in np.argsort(modes):
                spectra.append({'case_id': case, 'method': method, 'mode': modes[j], 'k': k[j],
                                'normalized_h2_error_power': weighted_power[j]/denominator})
            saved[method] = (interpolated[-1], truth[-1], xi)
            costs.append({'case_id': case, 'method': method, 'training_seconds': item['training_seconds'],
                          'total_elapsed_seconds': item['total_elapsed_seconds']})
            for slab, value in enumerate(item['full_residual_rms_relative_by_slab']):
                residuals.append({'case_id': case, 'method': method, 'slab': slab+1,
                                  'slab_start': .5*slab, 'slab_end': .5*(slab+1),
                                  'full_residual_rms_relative': value})
        if not np.array_equal(saved['none'][1], saved['inverse_1_plus_k2'][1]):
            raise ValueError('Paired methods have different numerical references')
        baseline, truth, xi = saved['none']
        conditioned = saved['inverse_1_plus_k2'][0]
        tau = np.arange(len(truth))*length/len(truth)-length/2
        for j, coordinate in enumerate(tau):
            profiles.append({'case_id': case, 'tau': coordinate,
                             'reference_real': truth[j].real, 'reference_imag': truth[j].imag,
                             'baseline_real': baseline[j].real, 'baseline_imag': baseline[j].imag,
                             'conditioned_real': conditioned[j].real, 'conditioned_imag': conditioned[j].imag})
    data = report/'data'
    for filename, values in [('spatial-pinn-stations.csv', rows), ('spatial-pinn-xi4-profiles.csv', profiles),
                             ('spatial-pinn-xi4-spectrum.csv', spectra), ('spatial-pinn-costs.csv', costs),
                             ('spatial-pinn-residuals.csv', residuals)]:
        write_csv(data/filename, values)
    verification = {'model_id': MODEL, 'formulation': 'spatial-free-surface-envelope',
                    'length': length, 'profile_coordinate': 'tau', 'evolution_coordinate': 'xi',
                    'run_root_at_verification': str(args.run_root.resolve()),
                    'source_audit_sha256': sha(args.evidence), 'config_sha256': sha(args.config),
                    'verified_files': checks, 'verified_file_count': len(checks),
                    'recomputed_maximum_errors': maxima, 'source_design': audit['design'],
                    'reference_qualification': audit['references'],
                    'metric_convention': 'All-station raw complex errors, no phase/translation alignment; original production complex64 interpolation before comparison to complex128 reference; all1024 modes retained.',
                    'limitations': ['Three validation inlets, one optimization seed (11).',
                                    'PINNs fitted through xi4, not unseen-distance forecasts.',
                                    'Recorded CPU fitting timers are single observations, not matched-accuracy speed benchmarks.',
                                    'Mode-spectrum display zoom does not filter the analysis; full signed spectrum is in CSV.',
                                    'Finite-distance numerical agreement is not a continuum smoothness or existence proof.']}
    (data/'spatial-pinn-verification.json').write_text(json.dumps(verification, indent=2)+'\n')


def numbers(rows, key):
    return np.array([float(row[key]) for row in rows])


def setup_style():
    plt.rcParams.update({'font.family': 'serif', 'font.serif': ['DejaVu Serif'],
        'font.size': 10, 'axes.labelsize': 10, 'axes.titlesize': 10.5,
        'legend.fontsize': 9, 'xtick.labelsize': 9, 'ytick.labelsize': 9,
        'mathtext.fontset': 'dejavuserif', 'axes.spines.top': False, 'axes.spines.right': False,
        'pdf.fonttype': 42, 'ps.fonttype': 42, 'savefig.facecolor': 'white'})


def save(fig, report, name):
    fig.text(.5, -.025, r'Three validation inlets; seed 11; fitted interval $0\leq\xi\leq4$.',
             ha='center', va='top', fontsize=8)
    fig.savefig(report/'figures'/name, bbox_inches='tight', pad_inches=.06)
    plt.close(fig)


def plot(report):
    setup_style()
    data = report/'data'
    stations = read_csv(data/'spatial-pinn-stations.csv')
    profiles = read_csv(data/'spatial-pinn-xi4-profiles.csv')
    spectra = read_csv(data/'spatial-pinn-xi4-spectrum.csv')
    costs = read_csv(data/'spatial-pinn-costs.csv')
    residuals = read_csv(data/'spatial-pinn-residuals.csv')
    # Every saved station is plotted; no running maximum or smoothing is used.
    fig, axes = plt.subplots(1, 3, figsize=(6.55, 2.6), sharey=True)
    for ax, case in zip(axes, CASES):
        for method in METHODS:
            rows = [r for r in stations if r['case_id']==case and r['method']==method]
            ax.semilogy(numbers(rows, 'xi'), 100*numbers(rows, 'h2'), label=NAMES[method], **STYLE[method])
        ax.axhline(5, color='.15', linestyle=':', linewidth=1, label='5% gate')
        ax.set_title(case); ax.set_xlabel(r'Distance $\xi$'); ax.set_xlim(0, 4)
        ax.set_ylim(1e-3, 50); ax.set_xticks([0, 2, 4]); ax.grid(axis='y', which='major', color='.9', linewidth=.5)
    axes[0].set_ylabel(r'Complex $H^2$ error (%)')
    axes[0].legend(loc='lower right', frameon=False)
    fig.suptitle('Spatial free-surface Dysthe: fitted-interval error', fontsize=11, y=1.025)
    fig.tight_layout(w_pad=.5)
    save(fig, report, 'spatial-pinn-error-growth.pdf')

    fig, axes = plt.subplots(3, 3, figsize=(6.55, 6.3), sharex='col')
    for col, case in enumerate(CASES):
        rows = [r for r in profiles if r['case_id']==case]
        tau = numbers(rows, 'tau')
        fields = {name: numbers(rows, name+'_real')+1j*numbers(rows, name+'_imag')
                  for name in ('reference','baseline','conditioned')}
        truth = fields['reference']; center = tau[np.argmax(abs(truth))]
        # First two rows use the entire periodic profile; middle row shows its
        # real component so phase-related discrepancies remain visible.
        axes[0,col].plot(tau, abs(truth), color='.7', linewidth=2.7, label='Reference')
        axes[1,col].plot(tau, truth.real, color='.7', linewidth=2.7)
        for key, method in [('baseline','none'), ('conditioned','inverse_1_plus_k2')]:
            axes[0,col].plot(tau, abs(fields[key]), label=NAMES[method], **STYLE[method])
            axes[1,col].plot(tau, fields[key].real, **STYLE[method])
            axes[2,col].plot(tau, 100*abs(fields[key]-truth)/max(abs(truth)), **STYLE[method])
        axes[0,col].set_title(case)
        axes[2,col].set_xlabel(r'Retarded time $\tau$')
        for ax in axes[:,col]:
            ax.set_xlim(-20,20); ax.set_xticks([-20,0,20]); ax.grid(axis='y', color='.92', linewidth=.5)
        # Inset gives a true amplitude zoom without changing the main coordinates.
        inset=axes[0,col].inset_axes([.52,.50,.46,.44])
        inset.plot(tau,abs(truth),color='.7',linewidth=2)
        for key, method in [('baseline','none'), ('conditioned','inverse_1_plus_k2')]:
            inset.plot(tau,abs(fields[key]),**{**STYLE[method],'linewidth':.9})
        mask=abs(tau-center)<=1.5
        lo=min(float(min(abs(v[mask]))) for v in fields.values()); hi=max(float(max(abs(v[mask]))) for v in fields.values())
        inset.set_xlim(center-1.5,center+1.5);inset.set_ylim(lo-.07*(hi-lo),hi+.07*(hi-lo));inset.set_xticks([]);inset.set_yticks([])
        inset.set_title('peak zoom',fontsize=7,pad=1)
    axes[0,0].set_ylabel(r'Envelope $|u|$'); axes[1,0].set_ylabel(r'Real part $\mathrm{Re}\,u$')
    axes[2,0].set_ylabel('Complex error /\nreference peak (%)')
    handles, labels = axes[0,0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.5,.965),
               frameon=False, ncol=3, fontsize=9)
    fig.suptitle(r'Spatial profiles at $\xi=4$: each inlet fitted separately',fontsize=11,y=1.005)
    fig.tight_layout(h_pad=.75,w_pad=.6,rect=(0,0,1,.94))
    save(fig,report,'spatial-pinn-profiles-xi4.pdf')

    # Phase is meaningful only where the envelope is appreciable. Curvature
    # errors below retain every point, including the tails omitted from phase.
    fig, axes = plt.subplots(2, 3, figsize=(6.55, 4.5), sharex='col')
    phase_rows, phase_summary = [], []
    for col, case in enumerate(CASES):
        rows = [r for r in profiles if r['case_id']==case]
        tau = numbers(rows, 'tau')
        truth = numbers(rows, 'reference_real')+1j*numbers(rows, 'reference_imag')
        length = len(tau)*(tau[1]-tau[0])
        k = 2*np.pi*np.fft.fftfreq(len(tau), d=length/len(tau))
        curvature_truth = np.fft.ifft(-k*k*np.fft.fft(truth))
        curvature_rms = float(np.sqrt(np.mean(abs(curvature_truth)**2)))
        for key, method in [('baseline','none'), ('conditioned','inverse_1_plus_k2')]:
            field = numbers(rows, key+'_real')+1j*numbers(rows, key+'_imag')
            support = (abs(truth)>.05*max(abs(truth))) & (abs(field)>.05*max(abs(field)))
            phase = np.angle(field*truth.conj())
            shown_phase = np.where(support, phase*180/np.pi, np.nan)
            curvature_error = abs(np.fft.ifft(-k*k*np.fft.fft(field-truth)))/curvature_rms
            axes[0,col].plot(tau, shown_phase, label=NAMES[method], **STYLE[method])
            axes[1,col].plot(tau, 100*curvature_error, **STYLE[method])
            phase_summary.append({'case_id': case, 'method': method,
                'phase_amplitude_threshold_fraction': .05,
                'amplitude_weighted_phase_rmse_radians': float(np.sqrt(
                    np.sum(abs(truth[support])**2*phase[support]**2)/np.sum(abs(truth[support])**2))),
                'excluded_reference_action_fraction': float(np.sum(abs(truth[~support])**2)/np.sum(abs(truth)**2)),
                'reference_curvature_rms': curvature_rms})
            for j,x in enumerate(tau):
                phase_rows.append({'case_id': case, 'method': method, 'tau': x,
                    'phase_error_radians': phase[j], 'phase_support': bool(support[j]),
                    'curvature_error_over_reference_curvature_rms': curvature_error[j]})
        axes[0,col].axhline(0,color='.8',linewidth=.5)
        axes[0,col].set_title(case);axes[1,col].set_xlabel(r'Retarded time $\tau$')
        for ax in axes[:,col]:
            ax.set_xlim(-20,20);ax.set_xticks([-20,0,20]);ax.grid(axis='y',color='.92',linewidth=.5)
    axes[0,0].set_ylabel('Phase error (deg)')
    axes[1,0].set_ylabel('Curvature error (%)')
    axes[0,0].legend(loc='lower left', frameon=False, fontsize=8)
    fig.suptitle(r'Spatial phase and curvature errors at $\xi=4$', fontsize=11,y=1.01)
    fig.tight_layout(h_pad=.8,w_pad=.6)
    save(fig,report,'spatial-pinn-phase-curvature.pdf')
    write_csv(data/'spatial-pinn-phase-curvature.csv',phase_rows)
    (data/'spatial-pinn-phase-summary.json').write_text(json.dumps(phase_summary,indent=2)+'\n')

    fig, axes=plt.subplots(1,3,figsize=(6.55,2.8),sharey=True)
    for ax,case in zip(axes,CASES):
        for method in METHODS:
            rows=[r for r in spectra if r['case_id']==case and r['method']==method]
            mode=numbers(rows,'mode').astype(int);power=numbers(rows,'normalized_h2_error_power')
            folded=np.array([power[abs(mode)==m].sum() for m in range(513)])
            ax.semilogy(np.arange(513),folded,label=NAMES[method],**STYLE[method])
        ax.axvspan(25,48,color='.94',zorder=-5);ax.axvline(48,color='.1',linestyle=':',linewidth=.8)
        ax.set_xlim(0,64);ax.set_ylim(1e-12,.1);ax.set_xticks([0,24,48,64]);ax.set_xlabel(r'Fourier mode $|m|$');ax.set_title(case)
        ax.grid(axis='y',color='.9',linewidth=.5)
    axes[0].set_ylabel(r'$H^2$ error power / $\|u_{\rm ref}\|_{H^2}^2$')
    axes[0].legend(loc='lower left',frameon=False)
    fig.suptitle(r'Spatial endpoint error spectrum at $\xi=4$ (display zoom)',fontsize=11,y=1.015)
    fig.tight_layout(w_pad=.5)
    save(fig,report,'spatial-pinn-mode-error.pdf')

    fig,ax=plt.subplots(figsize=(6.55,2.6));x=np.arange(3);width=.31
    for j,method in enumerate(METHODS):
        values=[float(next(r for r in costs if r['case_id']==case and r['method']==method)['training_seconds']) for case in CASES]
        bars=ax.bar(x+(j-.5)*width,values,width,label=NAMES[method],color='white' if j==0 else '.65',edgecolor='black',linewidth=.7,hatch='///' if j==0 else None)
        for bar,v in zip(bars,values):ax.text(bar.get_x()+bar.get_width()/2,v+.15,f'{v:.2f}',ha='center',va='bottom',fontsize=9)
    ax.set_xticks(x,CASES);ax.set_ylabel('Recorded fitting time (s)');ax.set_ylim(0,19)
    ax.set_title('Spatial PINNs: equal update budgets on CPU',fontsize=11);ax.legend(frameon=False,loc='upper left',ncol=2)
    fig.tight_layout();save(fig,report,'spatial-pinn-recorded-cost.pdf')

    fig,axes=plt.subplots(1,3,figsize=(6.55,2.55),sharey=True)
    for ax,case in zip(axes,CASES):
        for method in METHODS:
            rows=[r for r in residuals if r['case_id']==case and r['method']==method]
            ax.semilogy(numbers(rows,'slab'),numbers(rows,'full_residual_rms_relative'),marker='o',markersize=2.5,label=NAMES[method],**STYLE[method])
        ax.set_title(case);ax.set_xlabel('Fitted slab number');ax.set_xticks([1,4,8]);ax.grid(axis='y',color='.9',linewidth=.5)
    axes[0].set_ylabel('Full residual RMS /\ninlet RHS RMS');axes[0].legend(frameon=False,loc='lower left')
    fig.suptitle('Spatial Dysthe residual audit on complete periodic slices',fontsize=11,y=1.025)
    fig.tight_layout(w_pad=.5);save(fig,report,'spatial-pinn-residual-audit.pdf')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-root',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--run-root',type=Path);parser.add_argument('--evidence',type=Path);parser.add_argument('--config',type=Path)
    args=parser.parse_args();report=args.report_root
    (report/'data').mkdir(parents=True,exist_ok=True);(report/'figures').mkdir(parents=True,exist_ok=True)
    if any((args.run_root,args.evidence,args.config)):
        if not all((args.run_root,args.evidence,args.config)):parser.error('Extraction needs run-root, evidence and config together')
        extract(args,report)
    plot(report)

if __name__=='__main__':main()
