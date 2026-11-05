"""Compare the two existing optical Fourier implementations on one smooth 3D field.

Run from the parent Dysthe workspace with:
    PYTHONPATH=.:dysthe-pinn/src OPENBLAS_NUM_THREADS=4 python3 dysthe-pinn/reports/dysthe-research-reset/check_solver_agreement.py

This checks finite cross-implementation consistency, not continuum accuracy.
"""
import json
import numpy as np

from nonlinear.solver import FourierModel
from dysthe_pinn.reference import SpectralReference

with open('dysthe-pinn/configs/smoke.json') as stream:
    config = json.load(stream)
config['domain']['lengths'] = [2 * np.pi] * 3
config['reference']['shape'] = [16] * 3
config['physics'] = {'epsilon1': 0.13, 'epsilon2': 0.21}

original = FourierModel(
    (16,) * 3, (2 * np.pi,) * 3,
    kind='optical', epsilon1=0.13, epsilon2=0.21,
)
pinn_reference = SpectralReference(config)
x, y, z = np.meshgrid(*original.axes, indexing='ij')
u = (
    0.2 * np.exp(1j * (x + y + z))
    + 0.1j * np.exp(1j * (2 * x - y))
    + 0.07 * np.exp(-1j * z)
)
v = np.fft.fftn(u) * original.mask
rhs_original = original.rhs_hat(v)
rhs_reference = pinn_reference.rhs(v)
step_original = original.stepper(0.002)(v)
step_reference = pinn_reference.step(v, 0.002)

result = {
    'case': 'same nonseparable 3D initial field in both current optical solvers',
    'shape': [16] * 3,
    'epsilon1': 0.13,
    'epsilon2': 0.21,
    'dt': 0.002,
    'rhs_relative_difference': float(
        np.linalg.norm(rhs_original - rhs_reference) / np.linalg.norm(rhs_reference)
    ),
    'step_relative_difference': float(
        np.linalg.norm(step_original - step_reference) / np.linalg.norm(step_reference)
    ),
    'identical_retained_mode_masks': bool(np.array_equal(original.mask, pinn_reference.mask)),
}
assert result['identical_retained_mode_masks']
assert result['rhs_relative_difference'] < 1e-13
assert result['step_relative_difference'] < 1e-13
print(json.dumps(result, indent=2))
