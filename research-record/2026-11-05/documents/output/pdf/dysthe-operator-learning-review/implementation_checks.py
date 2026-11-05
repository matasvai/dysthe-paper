#!/usr/bin/env python3
"""Independent arithmetic checks for the proposed water-wave ML implementation.

No active solver, learning module, saved training data, or checkpoint is imported.
All operations are evaluated on deterministic low-mode trigonometric fields.
These checks are not trained-model results, trajectory simulations, convergence
studies, existence certificates, or nonlinear stability results.

Run: python3 implementation_checks.py
Output: implementation_checks.json in this directory.
"""

from __future__ import annotations

import json
from pathlib import Path
import platform
import time

import numpy as np


N = 256
LENGTH = 2 * np.pi
TAU = -LENGTH / 2 + np.arange(N) * LENGTH / N
K = 2 * np.pi * np.fft.fftfreq(N, d=LENGTH / N)


def derivative(u, order=1):
    return np.fft.ifft((1j * K) ** order * np.fft.fft(u))


def abs_derivative(u):
    return np.fft.ifft(np.abs(K) * np.fft.fft(u)).real


def integral(u):
    return float(LENGTH * np.mean(u))


def physical_coefficients(u):
    """Coefficients of exp(i*k*tau), with tau beginning at -L/2."""
    return np.exp(1j * K * LENGTH / 2) * np.fft.fft(u) / N


def relative_error(actual, expected):
    scale = np.linalg.norm(expected)
    return float(np.linalg.norm(actual - expected) / (scale if scale else 1))


def full_rhs(u, epsilon):
    """Unprojected free-surface spatial RHS; low modes avoid circular aliasing."""
    rho = np.abs(u) ** 2
    du = derivative(u)
    return -1j * derivative(u, 2) - 1j * rho * u - epsilon * (
        8 * rho * du + 2 * u ** 2 * np.conj(du)
        + 2j * u * abs_derivative(rho)
    )


def real_imaginary_rhs(p, q, epsilon):
    """Separately expanded real system, independently coded from its formulas."""
    px, qx = derivative(p).real, derivative(q).real
    pxx, qxx = derivative(p, 2).real, derivative(q, 2).real
    rho = p * p + q * q
    mean = abs_derivative(rho)
    prhs = qxx + rho * q - epsilon * (
        (10 * p * p + 6 * q * q) * px + 4 * p * q * qx - 2 * q * mean
    )
    qrhs = -pxx - rho * p - epsilon * (
        4 * p * q * px + (6 * p * p + 10 * q * q) * qx + 2 * p * mean
    )
    return prhs + 1j * qrhs


def translate(u, shift):
    return np.fft.ifft(np.exp(-1j * K * shift) * np.fft.fft(u))


def linear_flow(u, h):
    return np.fft.ifft(np.exp(1j * h * K ** 2) * np.fft.fft(u))


def origin_checks(u, coefficient_dictionary):
    calculated = physical_coefficients(u)
    expected = np.zeros(N, dtype=complex)
    for mode, value in coefficient_dictionary.items():
        expected[int(mode) % N] = value
    reconstructed = np.sum(calculated[:, None] * np.exp(1j * K[:, None] * TAU[None, :]), axis=0)
    missing_origin = np.sum((np.fft.fft(u) / N)[:, None] * np.exp(1j * K[:, None] * TAU[None, :]), axis=0)
    result = {
        "coefficient_relative_error": relative_error(calculated, expected),
        "reconstruction_relative_error": relative_error(reconstructed, u),
        "wrong_origin_reconstruction_relative_error": relative_error(missing_origin, u),
        "correct_formula": "a_m=exp(i*k_m*L/2)*FFT(u)_m/N for exp(i*k_m*tau)",
    }
    assert result["coefficient_relative_error"] < 1e-12
    assert result["reconstruction_relative_error"] < 1e-12
    assert result["wrong_origin_reconstruction_relative_error"] > 0.1
    return result


def linear_checks(u):
    errors = []
    for mode in (-5, -1, 0, 2, 4):
        field = (0.7 + 0.13j) * np.exp(1j * mode * TAU)
        h = 0.037
        expected = field * np.exp(1j * h * mode ** 2)
        errors.append(relative_error(linear_flow(field, h), expected))
    generator_delta = 1e-6
    numerical_generator = (linear_flow(u, generator_delta) - linear_flow(u, -generator_delta)) / (2 * generator_delta)
    result = {
        "linear_symbol": "+i*k^2",
        "flow_multiplier": "exp(+i*h*k^2)",
        "max_plane_wave_relative_error": max(errors),
        "semigroup_relative_error": relative_error(linear_flow(linear_flow(u, 0.017), 0.031), linear_flow(u, 0.048)),
        "generator_central_difference_relative_error": relative_error(numerical_generator, -1j * derivative(u, 2)),
        "generator_difference_increment": generator_delta,
    }
    assert result["max_plane_wave_relative_error"] < 1e-12
    assert result["semigroup_relative_error"] < 1e-12
    assert result["generator_central_difference_relative_error"] < 1e-8
    return result


def invariant_checks(u, epsilon):
    rhs = full_rhs(u, epsilon)
    rho = np.abs(u) ** 2
    du = derivative(u)
    mass_rate = 2 * integral(np.real(np.conj(u) * rhs))
    # P=integral Im(conj(u)*u_tau); Q=integral |u|^4.
    # The continuum modified momentum is 2(P-epsilon*Q).
    p_rate = integral(np.imag(np.conj(rhs) * du + np.conj(u) * derivative(rhs)))
    q_rate = 4 * integral(rho * np.real(np.conj(u) * rhs))
    p_rate_integrated_by_parts = 2 * integral(np.imag(np.conj(rhs) * du))

    def p_functional(v):
        return integral(np.imag(np.conj(v) * derivative(v)))

    def q_functional(v):
        return integral(np.abs(v) ** 4)

    delta = 1e-5
    p_fd = (p_functional(u + delta * rhs) - p_functional(u - delta * rhs)) / (2 * delta)
    q_fd = (q_functional(u + delta * rhs) - q_functional(u - delta * rhs)) / (2 * delta)
    result = {
        "epsilon": epsilon,
        "mass_directional_rate": mass_rate,
        "P_directional_rate": p_rate,
        "Q_directional_rate": q_rate,
        "P_minus_epsilon_Q_directional_rate": p_rate - epsilon * q_rate,
        "P_integration_by_parts_discrepancy": abs(p_rate - p_rate_integrated_by_parts),
        "finite_difference_increment": delta,
        "P_directional_finite_difference": p_fd,
        "Q_directional_finite_difference": q_fd,
        "P_directional_finite_difference_discrepancy": abs(p_rate - p_fd),
        "Q_directional_finite_difference_discrepancy": abs(q_rate - q_fd),
    }
    assert abs(mass_rate) < 1e-11
    assert abs(p_rate - epsilon * q_rate) < 1e-11
    assert result["P_integration_by_parts_discrepancy"] < 1e-11
    assert result["P_directional_finite_difference_discrepancy"] < 1e-8
    assert result["Q_directional_finite_difference_discrepancy"] < 1e-6
    return result


def encode_complex_array(array):
    return np.stack((array.real, array.imag), axis=-1).tolist()


def mi_jacobian_checks():
    """Finite differences of the full nonlinear RHS in the rotating frame.

    The full RHS is evaluated first, then real and imaginary output fields are
    Fourier analyzed. Real cosine inputs isolate each matrix column. Matrix
    coefficients below are only comparison targets, never used to generate
    the finite-difference derivative.
    """
    amplitude = 0.8
    delta = 1e-5
    records = []
    for epsilon in (0.0, 0.025, 0.05):
        def rotating_rhs(w):
            field = amplitude + w
            return full_rhs(field, epsilon) + 1j * amplitude ** 2 * field

        background_defect = float(np.max(np.abs(rotating_rhs(np.zeros(N, dtype=complex)))))
        for mode in (-3, -2, -1, 0, 1, 2, 3):
            cosine = np.cos(mode * TAU)
            idx = mode % N
            input_mode_coefficient = physical_coefficients(cosine)[idx]
            measured = np.zeros((2, 2), dtype=complex)
            for column, direction in enumerate((cosine.astype(complex), 1j * cosine)):
                differential = (rotating_rhs(delta * direction) - rotating_rhs(-delta * direction)) / (2 * delta)
                measured[0, column] = physical_coefficients(differential.real)[idx] / input_mode_coefficient
                measured[1, column] = physical_coefficients(differential.imag)[idx] / input_mode_coefficient
            k = float(mode)
            a2 = amplitude ** 2
            expected = np.array([
                [-10j * epsilon * a2 * k, -k ** 2],
                [k ** 2 - 2 * a2 - 4 * epsilon * a2 * abs(k), -6j * epsilon * a2 * k],
            ], dtype=complex)
            discrepancy = float(np.max(np.abs(measured - expected)))
            records.append({
                "epsilon": epsilon, "amplitude": amplitude, "mode": mode,
                "background_defect": background_defect,
                "measured_matrix_real_imag": encode_complex_array(measured),
                "comparison_matrix_real_imag": encode_complex_array(expected),
                "maximum_entry_absolute_discrepancy": discrepancy,
                "measured_eigenvalues_real_imag": encode_complex_array(np.linalg.eigvals(measured)),
            })
            assert discrepancy < 1e-8
            assert background_defect < 1e-12
    return {
        "method": "Centered differences of F(a+w)+i*a^2*(a+w), using p=cos(k*tau) and q=cos(k*tau) separately",
        "linearization_convention": "u=exp(-i*a^2*xi)*(a+w), w=p+i*q with real p and q",
        "matrix_comparison": "[[-10i*epsilon*a^2*k,-k^2],[k^2-2a^2-4epsilon*a^2*|k|,-6i*epsilon*a^2*k]]",
        "finite_difference_increment": delta,
        "number_of_cases": len(records),
        "maximum_matrix_entry_absolute_discrepancy": max(r["maximum_entry_absolute_discrepancy"] for r in records),
        "records": records,
        "interpretation": "Arithmetic validation of the real-linear Fourier Jacobian. Its eigenvalues describe linearized sidebands, not nonlinear stability or global existence.",
    }


def main():
    start = time.perf_counter()
    coefficients = {-4: 0.07 + 0.02j, -1: 0.22 - 0.09j, 0: 0.6 + 0.13j, 2: -0.18 + 0.08j, 5: 0.04 - 0.05j}
    u = sum(value * np.exp(1j * mode * TAU) for mode, value in coefficients.items())
    epsilons = (0.0, 0.025, 0.05)
    phase, shift = 0.43, 0.37
    equivariance = []
    real_imaginary = []
    for epsilon in epsilons:
        rhs = full_rhs(u, epsilon)
        phase_error = relative_error(full_rhs(np.exp(1j * phase) * u, epsilon), np.exp(1j * phase) * rhs)
        translation_error = relative_error(full_rhs(translate(u, shift), epsilon), translate(rhs, shift))
        equivariance.append({"epsilon": epsilon, "phase_relative_error": phase_error, "translation_relative_error": translation_error})
        split_error = relative_error(real_imaginary_rhs(u.real, u.imag, epsilon), rhs)
        real_imaginary.append({"epsilon": epsilon, "relative_error": split_error})
        assert phase_error < 1e-11 and translation_error < 1e-11
        assert split_error < 1e-11
    result = {
        "purpose": "Independent arithmetic checks supporting a water-wave operator-learning implementation review",
        "not_claimed": ["trained-model accuracy", "long-distance trajectories", "numerical refinement qualification", "global existence", "nonlinear stability"],
        "implementation": "Independent NumPy formulas; no active repository imports",
        "python_version": platform.python_version(), "numpy_version": np.__version__,
        "grid": {"n": N, "length": float(LENGTH), "origin": "-L/2", "maximum_input_mode": 5, "maximum_exact_cubic_output_mode_bound": 15},
        "input_coefficients": {str(m): [float(z.real), float(z.imag)] for m, z in coefficients.items()},
        "origin_round_trip": origin_checks(u, coefficients),
        "linear_flow": linear_checks(u),
        "equivariance": {"phase_radians": phase, "translation": shift, "records": equivariance},
        "real_imaginary_rhs": real_imaginary,
        "directional_balances": {
            "definitions": {"mass": "integral |u|^2", "P": "integral Im(conj(u)*u_tau)", "Q": "integral |u|^4", "modified_momentum": "2*(P-epsilon*Q)"},
            "expected": "mass'=0 and P'=epsilon*Q' for the full continuum RHS",
            "records": [invariant_checks(u, epsilon) for epsilon in epsilons],
        },
        "modulational_jacobian": mi_jacobian_checks(),
        "passed": True,
    }
    result["elapsed_seconds"] = time.perf_counter() - start
    output = Path(__file__).resolve().with_suffix(".json")
    output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    summary = {
        "output": str(output), "passed": True,
        "origin_round_trip": result["origin_round_trip"], "linear_flow": result["linear_flow"],
        "max_phase_equivariance_relative_error": max(r["phase_relative_error"] for r in equivariance),
        "max_translation_equivariance_relative_error": max(r["translation_relative_error"] for r in equivariance),
        "max_real_imaginary_rhs_relative_error": max(r["relative_error"] for r in real_imaginary),
        "directional_balances": result["directional_balances"],
        "max_MI_matrix_entry_absolute_discrepancy": result["modulational_jacobian"]["maximum_matrix_entry_absolute_discrepancy"],
        "elapsed_seconds": result["elapsed_seconds"],
    }
    print(json.dumps(summary, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
