#!/usr/bin/env python3
"""Reproduce temporal projection and carrier-band diagnostics from bundled CSV.

python make_temporal_bandwidth_figure.py
Optional full-field verification/extraction: --primary PRIMARY.json --source-root ROOT
The figure uses only epsilon=.05, c=1.5, three primary T<=16 trajectories.
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

CASES = ['packet', 'sideband', 'random']
CUTOFFS = [32, 48, 64, 128, 256, 512]
MODEL = 'dysthe-1979-temporal-potential-1d-stability-sign-v1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_csv(path, rows):
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def read_csv(path):
    with path.open() as handle:
        return list(csv.DictReader(handle))


def extract(report, primary_path, source_root):
    original = primary_path.read_bytes()
    primary = json.loads(original)
    cases = [c for c in primary['cases'] if c['epsilon'] == .05]
    if sorted(c['family'] for c in cases) != sorted(CASES):
        raise ValueError('Expected exactly three epsilon=.05 primary trajectories')
    projection, bands, verified = [], [], []
    for case in cases:
        if case['model_id'] != MODEL or not case['qualified'] or case['T'] != 16:
            raise ValueError('Expected qualified standard temporal-potential T16 data')
        source = source_root / case['source_array']
        digest = sha(source)
        if digest != case['artifact']['sha256']:
            raise ValueError('Full-field hash mismatch: '+str(source))
        with np.load(source, allow_pickle=False) as archive:
            field, T, s = archive['fields'], archive['T'], archive['s']
        n = field.shape[-1]
        length = n*(s[1]-s[0])
        mode = np.rint(np.fft.fftfreq(n)*n).astype(int)
        k = 2*np.pi*mode/length
        power = abs(np.fft.fft(field, axis=-1)/n)**2
        weighted = [power*(1+k*k)**order for order in range(3)]
        totals = [weight.sum(axis=-1) for weight in weighted]
        for cutoff in CUTOFFS:
            values = [np.sqrt(weight[:, abs(mode)>cutoff].sum(axis=-1)/total)
                      for weight, total in zip(weighted, totals)]
            for order, value in enumerate(values):
                target = case['representation_error_floor'][str(cutoff)][f'h{order}_omitted_relative_norm']
                if not np.isclose(max(value), target, rtol=1e-10, atol=1e-15):
                    raise ValueError('Projection recomputation disagrees with primary audit')
            for index, time in enumerate(T):
                projection.append({'family':case['family'], 'epsilon':.05, 'T':float(time),
                    'K':cutoff, **{f'h{order}_floor':float(value[index]) for order,value in enumerate(values)}})
        for threshold in [.25, .5, 1.]:
            outside = .05*abs(k)>=threshold
            action = power[:,outside].sum(axis=-1)/totals[0]
            h2 = weighted[2][:,outside].sum(axis=-1)/totals[2]
            target = case['carrier_relative_bands'][str(threshold)]
            if not np.isclose(max(action), target['maximum_action_fraction'], rtol=1e-10, atol=1e-15):
                raise ValueError('Action-band recomputation disagrees')
            if not np.isclose(max(h2), target['maximum_h2_squared_fraction'], rtol=1e-10, atol=1e-15):
                raise ValueError('H2-band recomputation disagrees')
            for index, time in enumerate(T):
                bands.append({'family':case['family'], 'epsilon':.05, 'T':float(time),
                    'threshold':threshold, 'action_fraction':float(action[index]),
                    'h2_squared_fraction':float(h2[index])})
        verified.append({'family':case['family'], 'source_array':case['source_array'],
            'sha256':digest, 'grid':n, 'length':length, 'step':case['step'],
            'saved_times':len(T), 'qualified':case['qualified'], 'refinement':case['refinement']})
    data = report/'data'
    write_csv(data/'temporal-projection-floors.csv', projection)
    write_csv(data/'temporal-carrier-band-fractions.csv', bands)
    (data/'temporal-bandwidth-primary-snapshot.json').write_bytes(original)
    metadata={'model_id':MODEL, 'epsilon':.05, 'c':1.5, 'maximum_saved_T':16,
        'primary_snapshot_sha256':hashlib.sha256(original).hexdigest(),
        'verified_full_fields':verified,
        'projection_formula':'f_s(K,T)^2=sum_{|m|>K}(1+k_m^2)^s |u_hat_m(T)|^2 / sum_m(1+k_m^2)^s |u_hat_m(T)|^2; k_m=2*pi*m/L.',
        'projection_interpretation':'At each saved T, orthogonal Fourier projection minimizes relative Hs error among fields supported in |m|<=K. The figure reports maxima over saved T, which lower-bound continuous-interval worst-case error. No neural fit is included.',
        'carrier_band_formula':'B_s(b,T)=sum_{epsilon*|k_m|>=b}(1+k_m^2)^s |u_hat_m(T)|^2 / sum_m(1+k_m^2)^s |u_hat_m(T)|^2, s=0 or2.',
        'carrier_interpretation':'Right panel shows separate sampled maxima of action and H2 squared fractions. Their maximizing times need not coincide. b=.5 is an illustrative diagnostic, not a universal physical-validity cutoff.',
        'limitations':['Finite-periodic-reference diagnostics, not a continuum existence or water-wave approximation certificate.',
            'The K48 obstruction applies to outputs restricted to |m|<=48 on this L40 temporal domain; it is not a claim that no PINN can approximate these trajectories.',
            'Projection norms are square roots of omitted weighted-energy fractions; the carrier-band panel deliberately shows squared-norm fractions.']}
    (data/'temporal-bandwidth-verification.json').write_text(json.dumps(metadata,indent=2)+'\n')


def plot(report):
    data=report/'data'
    projection=read_csv(data/'temporal-projection-floors.csv')
    bands=read_csv(data/'temporal-carrier-band-fractions.csv')
    plt.rcParams.update({'font.family':'serif','font.size':10,'axes.labelsize':10,
        'axes.titlesize':10.5,'xtick.labelsize':9,'ytick.labelsize':9,
        'mathtext.fontset':'dejavuserif','pdf.fonttype':42,'ps.fonttype':42,
        'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(6.55,3.15),gridspec_kw={'width_ratios':[1.1,1]})
    styles=[('black','-','o'),('.35','--','s'),('.6','-.','^')]
    summary=[]
    for family,(color,linestyle,marker) in zip(CASES,styles):
        floors=[max(float(r['h2_floor']) for r in projection if r['family']==family and int(r['K'])==K) for K in CUTOFFS]
        axes[0].plot(CUTOFFS,100*np.array(floors),color=color,linestyle=linestyle,
                     marker=marker,markersize=3.5,label=family.capitalize(),linewidth=1.2)
        bb=[r for r in bands if r['family']==family and float(r['threshold'])==.5]
        summary.append({'family':family, 'maximum_h2_projection_floors':dict(zip(CUTOFFS,floors)),
            'maximum_action_fraction_outside_band':max(float(r['action_fraction']) for r in bb),
            'maximum_h2_squared_fraction_outside_band':max(float(r['h2_squared_fraction']) for r in bb)})
    axes[0].set_xscale('log',base=2)
    axes[0].set_xticks(CUTOFFS,[str(K) for K in CUTOFFS]);axes[0].set_xlim(29,560)
    axes[0].set_ylim(0,85);axes[0].set_yticks([0,20,40,60,80])
    axes[0].axhline(5,color='.65',ls=':',lw=.9)
    axes[0].axvline(48,color='.65',ls=':',lw=.9)
    axes[0].text(520,6.8,'5%',ha='right',va='bottom',fontsize=8,color='.35')
    axes[0].set_xlabel(r'Maximum retained mode $K$')
    axes[0].set_ylabel(r'Sampled-max $H^2$ error floor (%)')
    axes[0].set_title('Fourier representation limit')
    axes[0].legend(frameon=False,fontsize=8,loc='upper right')
    positions=np.arange(3);width=.33
    for j,(key,label,color,hatch) in enumerate([
        ('maximum_action_fraction_outside_band','Action','white','///'),
        ('maximum_h2_squared_fraction_outside_band',r'$H^2$ squared','.65',None)]):
        values=np.array([item[key] for item in summary])*100
        bars=axes[1].bar(positions+(j-.5)*width,values,width,
            color=color,edgecolor='black',linewidth=.6,hatch=hatch,label=label)
        for bar,value in zip(bars,values):
            axes[1].text(bar.get_x()+bar.get_width()/2,value*1.12,
                         f'{value:.3f}' if value<1 else f'{value:.2f}',
                         ha='center',va='bottom',fontsize=7.5)
    axes[1].set_yscale('log');axes[1].set_ylim(.01,80)
    axes[1].set_xticks(positions,[s.capitalize() for s in CASES],fontsize=8)
    axes[1].set_ylabel('Sampled-max fraction (%)')
    axes[1].set_title(r'Outside $\epsilon|k|\geq0.5$')
    axes[1].legend(frameon=False,fontsize=8,loc='upper left',ncol=2,
                   bbox_to_anchor=(-.02,1.015),columnspacing=.8)
    for ax in axes:ax.grid(axis='y',color='.92',linewidth=.5);ax.set_axisbelow(True)
    fig.suptitle(r'Temporal potential Dysthe: $c=1.5$, $\epsilon=0.05$, $0\leq T\leq16$',fontsize=11,y=1.025)
    fig.text(.5,-.025,'Saved-time maxima; 0.5 is a bandwidth diagnostic, not a universal validity threshold.',
             ha='center',va='top',fontsize=8)
    fig.tight_layout(w_pad=.8)
    figure=report/'figures'/'temporal-representation-bandwidth.pdf'
    fig.savefig(figure,bbox_inches='tight',pad_inches=.06);plt.close(fig)
    (data/'temporal-bandwidth-figure-summary.json').write_text(json.dumps({
        'cases':summary,'figure_sha256':sha(figure),'script_sha256':sha(__file__)},indent=2)+'\n')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report-root',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--primary',type=Path);parser.add_argument('--source-root',type=Path)
    args=parser.parse_args();report=args.report_root
    (report/'data').mkdir(exist_ok=True,parents=True);(report/'figures').mkdir(exist_ok=True,parents=True)
    if args.primary or args.source_root:
        if not (args.primary and args.source_root):parser.error('Specify both primary and source-root')
        extract(report,args.primary,args.source_root)
    plot(report)


if __name__=='__main__':main()
