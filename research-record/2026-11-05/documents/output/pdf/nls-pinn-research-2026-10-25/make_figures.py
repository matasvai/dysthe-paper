"""Regenerate the report's two vector-only scientific figures.

Requires NumPy and Matplotlib. Both figures are explanatory illustrations:
neither contains newly measured PINN performance or experimental results.
"""

from pathlib import Path
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/nls-pinn-research-matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "mathtext.fontset": "dejavuserif",
    "font.size": 8.5,
    "axes.titlesize": 9.5,
    "axes.labelsize": 8.5,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7.4,
    "axes.linewidth": 0.7,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
})


def phase_drift():
    delta = 0.02
    s = np.linspace(0.0, 100.0, 1001)
    field_error = 2.0 * np.abs(np.sin(delta * s / 2.0))
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 3.15))
    fig.subplots_adjust(left=0.085, right=0.98, bottom=0.21,
                        top=0.77, wspace=0.34)
    fig.suptitle("Analytic NLS example (not a trained model)",
                 y=0.97, fontsize=10.5)
    fig.text(0.5, 0.865,
             r"$q(s,y)=e^{2is},\quad v(s,y)=e^{i(2+\delta)s},\quad\delta=0.02$",
             ha="center", fontsize=9)

    ax = axes[0]
    ax.plot(s, np.ones_like(s), color="0.15", linewidth=2.8,
            label=r"$|q|=1$")
    ax.plot(s, np.ones_like(s), color="0.75", linewidth=1.5,
            linestyle=(0, (4, 2.5)), label=r"$|v|=1$")
    ax.set(xlim=(0, 100), ylim=(0.84, 1.16),
           xlabel=r"Evolution coordinate $s$", ylabel="Amplitude")
    ax.set_yticks([0.9, 1.0, 1.1])
    ax.set_title("(a) Identical amplitudes", loc="left", pad=7)
    ax.legend(frameon=False, loc="upper left")
    ax.text(0.04, 0.06, "Same initial field.\nMass and Hamiltonian agree\nfor every $s$.",
            transform=ax.transAxes, fontsize=8.1, va="bottom")

    ax = axes[1]
    ax.plot(s, field_error, color="0.08", linewidth=1.6,
            label="Relative complex-field error")
    ax.plot(s, np.zeros_like(s), color="0.5", linewidth=1.0,
            linestyle=(0, (5, 2.5)), label="Amplitude / invariant defect")
    ax.plot(s, np.full_like(s, delta), color="0.05", linewidth=1.25,
            linestyle=":", label=r"Residual magnitude $|r|=0.02$")
    ax.set(xlim=(0, 100), ylim=(-0.10, 2.5),
           xlabel=r"Evolution coordinate $s$", ylabel="Defect or relative error")
    ax.set_title("(b) Accumulating phase error", loc="left", pad=7)
    ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
    ax.legend(frameon=False, loc="upper left", handlelength=2.3)
    ax.text(0.47, 0.27, r"$2|\sin(\delta s/2)|$", transform=ax.transAxes,
            fontsize=9, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    for ax in axes:
        ax.set_xticks([0, 50, 100])
        ax.tick_params(direction="out", length=3, width=0.7)

    fig.text(0.5, 0.04,
             r"Exact formulas for $iq_s+q_{yy}+2|q|^2q=0$ on a finite periodic interval.",
             ha="center", fontsize=8)
    fig.savefig(OUT / "phase-drift.pdf", metadata={
        "Title": "Analytic NLS phase drift despite identical amplitude and invariants",
        "Subject": "Exact analytic illustration, not trained-model output",
    })
    plt.close(fig)


def experiment_design():
    fig = plt.figure(figsize=(6.3, 3.8))
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")
    ax.text(0.5, 0.975, "Proposed validation sequence", ha="center",
            va="top", fontsize=11)
    ax.text(0.5, 0.915, "Three evidence levels; no new results are claimed",
            ha="center", va="top", fontsize=8.8)

    x_positions = [0.015, 0.355, 0.695]
    width, bottom, height = 0.29, 0.59, 0.235
    boxes = [
        ("1. Same-equation data",
         "Resolved spatial Dysthe\nKnown fields and parameters\nIsolate learning / solver error"),
        ("2. Independent HOS truth",
         "Separate potential-flow data\nVerified envelope conversion\nTest model discrepancy"),
        ("3. Laboratory evidence",
         "Measured wave elevations\nWithheld validation sensors\nTest external validity"),
    ]
    for x, (title, body) in zip(x_positions, boxes):
        ax.add_patch(Rectangle((x, bottom), width, height,
                               facecolor="white", edgecolor="0.25", linewidth=0.8))
        ax.text(x + width / 2, bottom + height - 0.045, title,
                ha="center", va="center", fontsize=8.6)
        ax.text(x + width / 2, bottom + 0.092, body,
                ha="center", va="center", fontsize=7.9, linespacing=1.6)
    for x in [0.305, 0.645]:
        ax.add_patch(FancyArrowPatch((x + 0.006, bottom + height / 2),
                                    (x + 0.044, bottom + height / 2),
                                    arrowstyle="-|>", mutation_scale=9,
                                    color="0.2", linewidth=0.8))

    # All evidence levels share the same comparisons and validation protocol.
    for center in [x + width / 2 for x in x_positions]:
        ax.add_patch(FancyArrowPatch((center, bottom - 0.01), (center, 0.515),
                                    arrowstyle="-|>", mutation_scale=8,
                                    color="0.4", linewidth=0.7))
    ax.add_patch(Rectangle((0.015, 0.315), 0.97, 0.19,
                           facecolor="white", edgecolor="0.25", linewidth=0.8))
    ax.text(0.5, 0.465, "Same observations and comparable tuning budgets",
            ha="center", va="center", fontsize=9)
    ax.text(0.5, 0.405, "Fixed NLS   |   Retuned NLS   |   Fixed Dysthe",
            ha="center", va="center", fontsize=8.7)
    ax.text(0.5, 0.35, "Numerical baseline: regularized spectral-solver assimilation",
            ha="center", va="center", fontsize=8.5)

    ax.add_patch(FancyArrowPatch((0.5, 0.305), (0.5, 0.26),
                                arrowstyle="-|>", mutation_scale=9,
                                color="0.3", linewidth=0.8))
    ax.add_patch(Rectangle((0.015, 0.055), 0.97, 0.195,
                           facecolor="white", edgecolor="0.25", linewidth=0.8))
    ax.text(0.5, 0.208, "Withhold whole packets and measurement locations",
            ha="center", va="center", fontsize=9)
    ax.text(0.5, 0.15,
            "Separate reconstruction between gauges from downstream prediction.",
            ha="center", va="center", fontsize=8.5)
    ax.text(0.5, 0.095,
            "Measure complex-field error, phase, peaks, uncertainty and total cost.",
            ha="center", va="center", fontsize=8.3)
    fig.savefig(OUT / "experiment-design.pdf", metadata={
        "Title": "Proposed three-level evidence design for water-wave Dysthe learning",
        "Subject": "Proposed experiments, not completed measurements",
    })
    plt.close(fig)


if __name__ == "__main__":
    phase_drift()
    experiment_design()
    print("Created figures/phase-drift.pdf and figures/experiment-design.pdf")
