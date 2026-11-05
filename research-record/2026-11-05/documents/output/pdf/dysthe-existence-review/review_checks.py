#!/usr/bin/env python3
"""Independent algebra/identity checks supporting the two-paper review.

These are finite Fourier identity checks, not trajectory integrations, trained
PINN results, existence certificates, or checks of the papers' derivations.
The implementation deliberately does not import the project's solvers.

Run from any directory:
    python3 /absolute/path/to/review_checks.py

Writes review_checks.json and a vector PDF beside this script. NumPy and
Matplotlib are required. The optional symbolic check uses SymPy when available.
"""

from __future__ import annotations

import json
from pathlib import Path
import platform
import time

import numpy as np


HERE = Path(__file__).resolve().parent


def mass_identity_checks():
    """Evaluate d/ds integral |u|^2 = 2 Re integral conjugate(u) RHS."""
    n, length = 512, 2 * np.pi
    x = np.arange(n) * length / n
    k = 2 * np.pi * np.fft.fftfreq(n, d=length / n)
    epsilon, beta = 0.05, 0.1

    def derivative(f, order=1):
        return np.fft.ifft((1j * k) ** order * np.fft.fft(f))

    def abs_derivative(f):
        return np.fft.ifft(np.abs(k) * np.fft.fft(f)).real

    def integral(f):
        return float(length * np.mean(f))

    def mass_rate(u, rhs):
        return 2 * integral(np.real(np.conj(u) * rhs))

    # All products have bandwidth far below the Nyquist frequency. Each
    # periodic trapezoidal quadrature is exact in exact arithmetic for the
    # trigonometric-polynomial integrands used in these checks.
    profiles = {
        "constant_plus_two_modes": {0: 0.7, 1: 0.16 + 0.09j, -2: 0.11 - 0.06j},
        "asymmetric_four_modes": {-3: 0.12 - 0.05j, -1: 0.3j, 0: 0.4, 2: -0.2 + 0.08j},
        "no_carrier_mode": {-5: 0.06 + 0.04j, -2: 0.24 - 0.1j, 3: 0.2 + 0.17j},
        "weak_modulation": {0: 0.9 + 0.1j, -1: 0.012j, 1: 0.02 - 0.01j},
        "broad_low_mode_packet": {-6: 0.03j, -3: 0.08, 0: 0.5, 2: 0.2j, 5: 0.07 - 0.04j},
    }
    # An arbitrary real field, not assumed to be an instantaneous function of
    # |u|^2. Thus this also checks the carrier's instantaneous action balance
    # when coupled through a real lagged mean field.
    arbitrary_real_mean = 0.4 + 0.3 * np.cos(2 * x) - 0.17 * np.sin(3 * x)
    rows = []
    for name, coefficients in profiles.items():
        u = sum(a * np.exp(1j * mode * x) for mode, a in coefficients.items())
        rho = np.abs(u) ** 2
        ux, uxx, uxxx = (derivative(u, order) for order in (1, 2, 3))
        mean = abs_derivative(rho)

        # Approved spatial free-surface equation, xi as evolution coordinate:
        # u_xi = -i u_xx - i rho u
        #        - eps(8 rho u_x + 2 u^2 conjugate(u_x) + 2i u |D|rho).
        spatial_without_mean = -1j * uxx - 1j * rho * u - epsilon * (
            8 * rho * ux + 2 * u ** 2 * np.conj(ux)
        )
        spatial_rhs = spatial_without_mean - 2j * epsilon * u * mean
        spatial_real_mean_rhs = spatial_without_mean - 2j * epsilon * u * arbitrary_real_mean

        # Schober-Islas Eq. (1.1), with H symbol -i sign(k):
        # i u_t + u_xx + 2 rho u
        # + eps[2u(1+i beta)|D|rho - 8i rho u_x + (i/2)u_xxx] = 0.
        # Multiplication by i yields the following evolution RHS.
        temporal_without_mean = 1j * uxx + 2j * rho * u + epsilon * (
            8 * rho * ux - 0.5 * uxxx
        )
        temporal_rhs = temporal_without_mean + 2j * epsilon * u * mean - 2 * epsilon * beta * u * mean
        temporal_real_mean_rhs = temporal_without_mean + 2j * epsilon * u * arbitrary_real_mean

        quadratic_mean = integral(rho * mean)
        rho_coeff = np.fft.fft(rho) / n
        quadratic_parseval = float(length * np.sum(np.abs(k) * np.abs(rho_coeff) ** 2))
        predicted_temporal_rate = -4 * epsilon * beta * quadratic_mean
        spatial_rate = mass_rate(u, spatial_rhs)
        temporal_rate = mass_rate(u, temporal_rhs)
        spatial_real_rate = mass_rate(u, spatial_real_mean_rhs)
        temporal_real_rate = mass_rate(u, temporal_real_mean_rhs)
        rows.append({
            "profile": name,
            "fourier_coefficients": {str(m): [float(a.real), float(a.imag)] for m, a in coefficients.items()},
            "spatial_v1_mass_rate": spatial_rate,
            "schober_islas_mass_rate": temporal_rate,
            "schober_islas_predicted_mass_rate": predicted_temporal_rate,
            "schober_islas_absolute_discrepancy": abs(temporal_rate - predicted_temporal_rate),
            "integral_rho_absD_rho": quadratic_mean,
            "parseval_nonnegative_value": quadratic_parseval,
            "parseval_absolute_discrepancy": abs(quadratic_mean - quadratic_parseval),
            "arbitrary_real_mean_spatial_mass_rate": spatial_real_rate,
            "arbitrary_real_mean_temporal_mass_rate": temporal_real_rate,
        })
    maxima = {
        "spatial_v1_absolute_mass_rate": max(abs(r["spatial_v1_mass_rate"]) for r in rows),
        "schober_islas_balance_absolute_discrepancy": max(r["schober_islas_absolute_discrepancy"] for r in rows),
        "parseval_absolute_discrepancy": max(r["parseval_absolute_discrepancy"] for r in rows),
        "arbitrary_real_mean_spatial_absolute_mass_rate": max(abs(r["arbitrary_real_mean_spatial_mass_rate"]) for r in rows),
        "arbitrary_real_mean_temporal_absolute_mass_rate": max(abs(r["arbitrary_real_mean_temporal_mass_rate"]) for r in rows),
    }
    tolerance = 1e-11
    assert all(v < tolerance for v in maxima.values()), maxima
    assert all(r["integral_rho_absD_rho"] > 0 for r in rows)
    assert all(r["schober_islas_mass_rate"] < 0 for r in rows)
    return {
        "n": n, "period": float(length), "epsilon": epsilon, "beta": beta,
        "hilbert_multiplier": "-i sign(k)", "abs_derivative_multiplier": "|k|",
        "absolute_tolerance": tolerance, "passed": True,
        "maxima": maxima, "profiles": rows,
        "interpretation": (
            "Roundoff-level verification of instantaneous mass-balance identities on five smooth "
            "periodic bandlimited fields. The arbitrary-real-mean check sets beta=0 and replaces "
            "the real |D|rho field by an independently chosen real M; it is not a simulation of "
            "the mean-field relaxation equation."
        ),
    }


def phase_lag_checks_and_figure():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    z = np.linspace(0, 3, 1201)
    exact = 1 / (1 - 1j * z)
    first_order = 1 + 1j * z
    observed_error = np.abs(exact - first_order)
    predicted_error = z ** 2 / np.sqrt(1 + z ** 2)
    error_discrepancy = float(np.max(np.abs(observed_error - predicted_error)))
    phase_discrepancy = float(np.max(np.abs(np.angle(exact) - np.angle(first_order))))
    assert error_discrepancy < 2e-14
    assert phase_discrepancy < 2e-14
    assert np.all(np.abs(exact[1:]) < 1)
    assert np.all(np.abs(first_order[1:]) > 1)

    plt.rcParams.update({
        "font.family": "serif", "font.size": 9,
        "axes.linewidth": 0.6, "pdf.fonttype": 42,
        "figure.facecolor": "white", "axes.facecolor": "white",
        "axes.spines.top": False, "axes.spines.right": False,
    })
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.05))
    axes[0].plot(z, np.abs(exact), color="black", lw=1.4, label=r"Exact $|G|=(1+z^2)^{-1/2}$")
    axes[0].plot(z, np.abs(first_order), color="0.45", lw=1.4, ls="--", label=r"First order $|1+iz|=(1+z^2)^{1/2}$")
    axes[0].axhline(1, color="0.72", lw=0.6, zorder=0)
    axes[0].set(xlabel=r"$z=\Omega\theta\geq 0$", ylabel="Magnitude", xlim=(0, 3), ylim=(0, 3.4))
    axes[0].legend(loc="upper left", frameon=False, fontsize=8)
    axes[1].plot(z, np.angle(exact), color="black", lw=1.4)
    axes[1].set(xlabel=r"$z=\Omega\theta\geq 0$", ylabel="Phase (radians)", xlim=(0, 3), ylim=(0, 1.6))
    axes[1].set_yticks([0, np.pi / 4, np.pi / 2], ["0", r"$\pi/4$", r"$\pi/2$"])
    axes[1].text(0.06, 0.93, r"$\arg G=\arg(1+iz)=\arctan z$", transform=axes[1].transAxes, va="top", fontsize=9)
    for ax in axes:
        ax.tick_params(width=0.6, length=3)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.94, bottom=0.24, wspace=0.30)
    fig.text(0.5, 0.045, r"$G=(1-iz)^{-1}$,   $|G-(1+iz)|=z^2/\sqrt{1+z^2}$.   The truncation is justified only for $|z|\ll1$.", ha="center", fontsize=9)
    out = HERE / "figures" / "phase_lag_response.pdf"
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, metadata={"Title": "Exact and first-order phase-lag response", "Subject": "Analytic transfer-function comparison; not trajectory or PINN results"})
    plt.close(fig)
    return {
        "z_range": [0, 3], "samples": len(z),
        "exact_response": "1/(1-i z)", "first_order_response": "1+i z",
        "absolute_error_identity": "z^2/sqrt(1+z^2)",
        "maximum_error_identity_discrepancy": error_discrepancy,
        "maximum_phase_difference": phase_discrepancy,
        "same_phase_exactly": "G=(1+i z)/(1+z^2), so both phases are arctan(z)",
        "at_z_1": {"exact_magnitude": float(1 / np.sqrt(2)), "first_order_magnitude": float(np.sqrt(2)), "phase_radians": float(np.pi / 4), "absolute_error": float(1 / np.sqrt(2))},
        "figure": str(out.relative_to(HERE)), "passed": True,
    }


def optional_deep_water_taylor_check():
    try:
        import sympy as sp
    except ImportError:
        return {"status": "not_run", "reason": "SymPy unavailable"}
    p, q, eta = sp.symbols("p q eta", real=True)
    # Omega=sqrt(g |k|), normalized by sqrt(g*k0), with k/k0=(1+p,q).
    omega = ((1 + eta * p) ** 2 + eta ** 2 * q ** 2) ** sp.Rational(1, 4)
    computed = sp.expand(sp.series(omega, eta, 0, 4).removeO()).subs(eta, 1)
    expected = 1 + p / 2 - p ** 2 / 8 + q ** 2 / 4 + p ** 3 / 16 - 3 * p * q ** 2 / 8
    difference = sp.simplify(computed - expected)
    assert difference == 0
    # The supplied 2026 paper uses exp[i(omega*t-k*x)] and an envelope
    # exp[i(K*X-Omega*T)]. Its inviscid linear sideband has q=k-epsilon*K.
    # Therefore Omega=(omega-sqrt(g*(k-epsilon*K)))/epsilon.
    eps, wave, carrier, freq = sp.symbols("epsilon K k omega", positive=True)
    slow_freq = freq * (1 - sp.sqrt(1 - eps * wave / carrier)) / eps
    slow_series = sp.series(slow_freq, eps, 0, 4).removeO().expand()
    required = freq * (wave/(2*carrier) + eps*wave**2/(8*carrier**2)
        + eps**2*wave**3/(16*carrier**3)
        + 5*eps**3*wave**4/(128*carrier**4))
    assert sp.simplify(slow_series - required) == 0
    return {
        "status": "passed", "sympy_version": sp.__version__,
        "normalized_dispersion": "omega/sqrt(g*k0)=((1+p)^2+q^2)^(1/4)",
        "definition": "p=longitudinal sideband wavenumber/k0; q=transverse sideband wavenumber/k0",
        "cubic_taylor_polynomial": str(computed),
        "symbolic_difference": str(difference),
        "2026_slow_frequency_series": str(slow_series),
        "2026_slow_frequency_symbolic_difference": "0",
        "required_cubic_Axxx_coefficient_in_F4": "-i*omega**2/(8*k**3)",
        "required_quartic_Axxxx_coefficient_in_F5": "-5*omega**2/(64*k**4)",
        "interpretation": "Independent linear deep-water dispersion identity; not a derivation or validation of nonlinear Dysthe coefficients.",
    }


def main():
    start = time.perf_counter()
    result = {
        "purpose": "Independent supporting identity checks for a paper review",
        "not_claimed": ["trajectory integration", "trained PINN", "existence proof", "stability proof", "complete verification of either paper's derivation"],
        "python_version": platform.python_version(), "numpy_version": np.__version__,
        "mass_balances": mass_identity_checks(),
        "phase_lag": phase_lag_checks_and_figure(),
        "deep_water_taylor": optional_deep_water_taylor_check(),
    }
    result["elapsed_seconds"] = time.perf_counter() - start
    out = HERE / "review_checks.json"
    out.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"output": str(out), "mass_maxima": result["mass_balances"]["maxima"], "phase_lag": result["phase_lag"], "deep_water_taylor": result["deep_water_taylor"], "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
