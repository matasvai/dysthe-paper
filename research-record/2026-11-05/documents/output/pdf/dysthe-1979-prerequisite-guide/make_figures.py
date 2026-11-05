"""Regenerate the guide's original vector PDF figures."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({
    "font.family": "serif", "font.size": 10, "axes.spines.top": False,
    "axes.spines.right": False, "axes.linewidth": 0.7,
    "pdf.fonttype": 42, "savefig.bbox": "tight",
})

x = np.linspace(-65, 65, 5000)
amplitude = 0.10 * np.exp(-(x / 27) ** 2)
fig, ax = plt.subplots(figsize=(6.35, 2.5))
ax.plot(x, amplitude * np.cos(x), color="black", lw=0.8,
        label="Real surface, illustrative")
ax.plot(x, amplitude, color="0.4", ls="--", lw=1.0, label=r"$+2|B|$")
ax.plot(x, -amplitude, color="0.4", ls="--", lw=1.0)
ax.set(xlabel="Position in carrier length units", ylabel="Surface elevation")
ax.legend(frameon=False, loc="upper right", fontsize=8)
fig.savefig(OUT / "carrier-envelope.pdf")
plt.close(fig)

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
fig, axes = plt.subplots(2, 1, figsize=(5.8, 3.85), sharex=True)
axes[0].plot(x, 1 + 0.25 * np.cos(x), color="black")
axes[0].set(ylabel=r"Intensity $I$", ylim=(0.65, 1.40))
axes[0].text(-6, 1.33, r"$I=1+0.25\cos x$", fontsize=9)
for depth, pattern in [(0, "-"), (-1, "--"), (-2, ":")]:
    axes[1].plot(x, -0.25 * np.exp(depth) * np.cos(x), pattern,
                 color="black", lw=1.1, label=f"z = {depth}")
axes[1].set(xlabel="Position x (modulation units)", ylabel=r"Current $\overline{\phi}_x$",
            ylim=(-0.30, 0.35))
axes[1].legend(frameon=False, ncol=3, loc="upper center", fontsize=8)
fig.tight_layout()
fig.savefig(OUT / "mean-flow.pdf")
plt.close(fig)

s = 0.10
lam = np.linspace(0, 0.31, 1200)
p = lam**2 / 8
nls = np.sqrt(np.maximum(p * (s*s - p), 0))
dysthe = np.sqrt(np.maximum(p * (s*s * (1 - lam) - p), 0))
fig, ax = plt.subplots(figsize=(6.35, 2.9))
ax.plot(lam, nls, "--", color="black", label="NLS")
ax.plot(lam, dysthe, "-", color="black", label="Dysthe retained radicand")
ax.set(xlabel=r"Longitudinal modulation wavenumber $\lambda$",
       ylabel=r"Growth rate $\gamma$", xlim=(0, 0.31), ylim=(0, 0.0058))
ax.legend(frameon=False, fontsize=9)
ax.ticklabel_format(axis="y", style="sci", scilimits=(-3, -3))
fig.tight_layout()
fig.savefig(OUT / "longitudinal-growth.pdf")
plt.close(fig)

s = np.linspace(0, 0.20, 600)
fig, axes = plt.subplots(1, 3, figsize=(6.4, 2.9))
curves = [
    (np.sqrt(2)*s, np.sqrt(2)*s*(1-np.sqrt(2)*s), r"Marginal $\Omega_c$"),
    (s*s/2, s*s*(1-2*s)/2, r"Maximum $\gamma_M$"),
    (s, s*(1-1.5*s), r"Fastest-mode $\mathrm{Re}\,\Omega_M$"),
]
for ax, (first, second, title) in zip(axes, curves):
    ax.plot(s, first, "--", color="black", lw=1.1, label="NLS")
    ax.plot(s, second, "-", color="black", lw=1.1, label="Dysthe expansion")
    ax.set(xlabel=r"Steepness $A_0$", title=title, xlim=(0, 0.2), ylim=(0, None))
    ax.set_xticks([0, 0.1, 0.2])
    ax.set_title(title, fontsize=9)
axes[0].legend(frameon=False, fontsize=7, loc="upper left")
fig.tight_layout(w_pad=1.5)
fig.savefig(OUT / "asymptotic-comparison.pdf")
plt.close(fig)
print("Created four vector PDF figures.")
