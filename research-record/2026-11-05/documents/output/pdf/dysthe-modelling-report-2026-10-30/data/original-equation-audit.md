# Original temporal Dysthe model audit — 30 October 2026

Internal scientific audit for the planned proof of concept; no existing solver, model label, or report was modified. Formulae below use the forward Fourier convention `exp(-ikx)` and inverse modes `exp(ikx)`. The analytic calculations are independent derivations, not empirical findings.

## Recommendation and source status

Use an explicitly new **one-horizontal-coordinate temporal velocity-potential-envelope** model with the standard coefficients `(c,b)=(3/2,-1/4)` in (T) below. Describe it as **later-standard and consistent with Dysthe (1979), Section 3**, while documenting the printed Section 2 discrepancy. Do not call it the literal printed (2.19) or claim an authenticated erratum. Preserve the literal alternative `(c,b)=(1,-1/4)` as a separately labelled audit comparator if useful.

Suggested explicit IDs:

- `water-wave-dysthe-temporal-potential-1d-standard-v1`: `(c,b)=(3/2,-1/4)`, third-order linear dispersion, deep-water `-|D|` mean-flow closure.
- `water-wave-dysthe-temporal-potential-1d-1979-printed-v1`: `(c,b)=(1,-1/4)`, the literal printed (2.19) reduced as described below.
- Existing `water-wave-dysthe-spatial-v1` remains the separately approved spatial free-surface-envelope problem; its runs are not evidence for either new temporal variant.

**Original scan rechecked visually:** supplied `Dysthe-NoteModificationNonlinear-1979.pdf`, printed pp. 109–110 (PDF pages 6–7). In (2.19), the displayed term really is `+ (i/2)|A|^2 A_x` on the right. Division by `2i`, moving terms left, and substitution of the retained mean-flow boundary condition yield `c=1`. The printed amplitude/phase equations (3.2)–(3.3), however, have `+1/4` and `+7/4` derivative coefficients before mean-flow elimination; these instead require `c=3/2`. Replacing only that printed plus by a minus would reconcile them, but this is an algebraic inference, not a sourced erratum.

**Independent primary corroboration, visually checked:** Shemer & Dorfman (2008), printed pp. 932–933, equations (3)–(6), states the surface-envelope equation with self-steepening coefficient `3/2`, conjugate coefficient `+1/4`, and `+ik_0 a phi_x`. The first paragraph on p. 933 explicitly states that the potential-envelope version used by Dysthe and Lo–Mei has the opposite conjugate sign. Its boundary condition is `phi_z=(omega_0/2)(|a|^2)_x`. With the stated carrier convention, this establishes `(3/2,-1/4)` and the negative `|D|` term for the normalized potential model. It corroborates the standard equation, without certifying a typographic correction to the original.

Primary URL: https://npg.copernicus.org/articles/15/931/2008/npg-15-931-2008.pdf ; DOI https://doi.org/10.5194/npg-15-931-2008 . Downloaded `/tmp/shemer-dorfman2008.pdf`; checked rendered pages `/tmp/shemer-dorfman2008-eq.png` and `/tmp/shemer-dorfman2008-sign.png`.

Trulsen (2006), *Weakly nonlinear and stochastic properties of ocean wave fields*, §4.3, (4.15), also displays the equivalent derivative combination `(7/4)|A|^2 A_x-(1/4)A(|A|^2)_x`, together with `+iA phi_x` and `phi_z=(1/2)(|A|^2)_x`. Expanding the density derivative gives `(3/2)|A|^2 A_x-(1/4)A^2 bar(A)_x`. The chapter identity was verified through the author's UiO publication list and publisher DOI; the accessible full-text transcription was inspected, but its original page image was not retrieved. Use Shemer–Dorfman as the visually verified corroboration.

Primary bibliographic links: https://doi.org/10.1007/978-3-211-69356-8_2 ; https://www.mn.uio.no/math/english/people/aca/karstent/index.html . Author-linked archive: https://hdl.handle.net/11250/4858559 .

Lo & Mei (1985), JFM 150, 395–416, DOI https://doi.org/10.1017/S0022112085000180 : publisher abstract verified, but this audit could not retrieve its full PDF (mirror timed out). Do not attribute directly verified equation numbers or signs to Lo–Mei on that basis. Shemer–Dorfman's explicit comparison supplies the corroboration. Trulsen–Dysthe (1996), DOI https://doi.org/10.1016/S0165-2125(96)00020-0 , broadens the bandwidth model; it is not a license to add those higher linear terms to this version.

**Caution about a conflicting convenient source:** Fedele & Dutykh (2012), Eq. (1.1), prints temporal potential `beta=+1/4` and a positive Hilbert term, while describing the surface coefficient as negative. This conflicts with the above primary temporal convention. Their spatial equation is the basis of the existing spatial project, but their temporal display must not be used to erase this discrepancy. URL https://arxiv.org/html/1110.3605v3 .

## Equation, normalization and mean flow

Let `rho=|A|^2`, let `D=|D_x|` have symbol `|k|`, and consider

\[
A_t+\tfrac12 A_x+\tfrac i8 A_{xx}-\tfrac1{16}A_{xxx}
+\tfrac i2\rho A+c\rho A_x+bA^2\bar A_x
-\tfrac i2 A D\rho=0. \tag{T}
\]

The standard variant has `c=3/2,b=-1/4`; the literal comparator has `c=1,b=-1/4`. All signs refer to the equation with every term on the left.

Original (2.6), printed p. 107, defines `A` as the first-harmonic velocity-potential envelope and `B` as the surface-elevation envelope, with carrier `exp(i(k_0 x-omega_0 t))`. Original (2.18), p. 109, uses normalized coordinates `x=k_0 x_phys`, `t=omega_0 t_phys`, normalized potential envelope `A=2k_0^2 A_phys/omega_0`, and mean potential `bar(phi)=2k_0^2 bar(phi_phys)/omega_0`. These factors make the uniform normalized amplitude equal to steepness. A temporal input is an initial *spatial* profile `A(x,0)`, not a wavemaker time trace.

Original (2.11), (2.20)–(2.21) give the mean harmonic extension in `z<0`; after discarding the higher-order `bar(zeta)_t`, `bar(phi)_z=rho_x` at `z=0`. Decay at depth gives, for nonzero horizontal Fourier mode,

\[
\widehat{\bar\phi}(k,z)=i\operatorname{sgn}(k)\widehat\rho(k)e^{|k|z},
\qquad \bar\phi_x=-D\rho.
\]

The derivative's zero mode is zero. Before eliminating `bar(phi)_z`, the original equation contains it explicitly; its contribution changes the local derivative coefficients. It must not be omitted twice or retained again after using (T). The original full equation has two horizontal coordinates; (T) is an explicit `y`-independent restriction. Periodizing the envelope is a further numerical-domain choice.

The exact coordinate change `X=x-t/2`, `T=t` removes only the group advection. If computational variables instead use `A=epsilon u`, `X=epsilon(x-t/2)`, `S=epsilon^2 t`, the corresponding model is

\[
u_S+\tfrac i8u_{XX}+\tfrac i2|u|^2u
+\epsilon[-\tfrac1{16}u_{XXX}+c|u|^2u_X
+bu^2\bar u_X-\tfrac i2u|D_X|(|u|^2)]=0.\tag{S}
\]

Report which scaling is actually used. An additional epsilon in (T) would double-count the original smallness convention.

## Exact controls for the specified truncated PDE

### Linear propagator and nonlinear plane wave

For (T), the linear frequency and evolution multiplier are

\[
\omega_{\rm lin}(k)=\tfrac k2-\tfrac{k^2}8+\tfrac{k^3}{16},
\qquad \widehat{A}(k,t)=e^{-it\omega_{\rm lin}(k)}\widehat{A}(k,0).
\]

In the group frame, remove `k/2`. For `a>0`, `A=a exp(i(kx-omega t))` is an exact solution of (T), since `D rho=0`, with

\[
\omega(k,a)=\omega_{\rm lin}(k)+\tfrac{a^2}{2}+(c-b)a^2 k.
\]

Thus the standard last coefficient is `7/4`, and the literal one is `5/4`. A nonzero envelope wavenumber is needed to discriminate these variants by this test; the spatially constant nonlinear wavetrain is identical in both. These are exact identities of the truncated model, not exact Euler-wave dispersion relations.

### Modulational instability, including the retained-model correction

Put `A=a[1+p+iq] exp(-ia^2t/2)` and linearize in real `p,q`. For `b=-1/4`,

\[
\begin{aligned}
p_t+\tfrac12p_x-\tfrac1{16}p_{xxx}+(c-\tfrac14)a^2p_x-\tfrac18q_{xx}&=0,\\
q_t+\tfrac12q_x-\tfrac1{16}q_{xxx}+(c+\tfrac14)a^2q_x+\tfrac18p_{xx}
+a^2p-a^2Dp&=0.
\end{aligned}
\]

For perturbation `exp(i(ell x-Omega t))`, define `P=ell^2/8`, `d=ell/2+ell^3/16`. The exact characteristic equation of this linearization is

\[
[\Omega-d-(c-\tfrac14)a^2\ell]
[\Omega-d-(c+\tfrac14)a^2\ell]
=P[P-a^2(1-|\ell|)].
\]

Consequently

\[
\Omega=d+c a^2\ell\ \pm\
\sqrt{P[P-a^2(1-|\ell|)]+\tfrac1{16}a^4\ell^2},
\]

and, when its radicand is negative,

\[
\gamma_{\rm model}^2=P[a^2(1-|\ell|)-P]-\tfrac1{16}a^4\ell^2.
\]

**The two c variants have the same growth rate about this background. They differ in real modulation frequency/drift. Growth alone cannot detect the printed sign issue.** Test the complex eigenvalue or evolving phase as well.

Dysthe's (3.6), printed p. 110, agrees with this determinant for `c=3/2`. His (3.7) omits the last `a^4 ell^2/16` under the root. With `a,ell=O(epsilon)`, the leading radicand is `O(epsilon^4)`, its mean-flow correction is `O(epsilon^5)`, and the omitted term is `O(epsilon^6)`. Terms absent from the fourth-order envelope equation can also affect that order. Therefore:

- Test an implementation against the **exact retained-model** eigenvalue.
- Compare with the **formal 1979** prediction `gamma_1979^2=P[a^2(1-|ell|)-P]`, explicitly labelled as truncation.
- The latter gives `ell_max=2a-3a^2+O(a^3)` and `gamma_max=a^2/2-a^3+O(a^4)`, reproducing (3.10)–(3.11). Do not use the formal zero at steepness 0.5 as a stability result.
- Close to a marginal root, the square-root expansion is not uniform. For a periodic box, only `ell=2pi n/L` are available, so a continuous-band maximum may not be represented.

For the scaled equation (S), replace `d` by `epsilon ell^3/16`, the drift by `epsilon c a^2 ell`, the mean factor by `1-epsilon|ell|`, and the last radicand term by `epsilon^2 a^4 ell^2/16`. Its `a` is the amplitude of `u`, not original steepness.

Independent floating-point substitution check: on 512 Fourier nodes, nonzero plane waves for both c values gave maximum defects below `1.2e-13`; a centered finite-difference check of the displayed linearization gave maximum error `5.2e-8` at perturbation step `1e-6`. This is an algebra/implementation sanity check, not a solver-convergence result.

## What can be proved cheaply, and what remains conditional

For smooth periodic solutions of (T), the mass `M=integral |A|^2 dx` is constant. The linear terms are skew-adjoint; the pure cubic and nonlocal terms have purely imaginary pointwise mass pairing; the two derivative nonlinearities contribute `-(c+b) integral rho rho_x dx=0` to `M'`. For (S) the same identity holds, with the derivative contribution multiplied by epsilon. This does **not** assert conservation of the usual cubic-NLS Hamiltonian.

For an **exact orthogonal finite Fourier Galerkin system**, this identity and finite-dimensional polynomial ODE continuation prove global existence at each fixed cutoff. Indeed the coefficient vector remains in a bounded mass ball. However `||A_K||_{H^s} <= (1+k_K^2)^{s/2} ||A_K||_2` grows with cutoff. This supplies no uniform continuum regularity bound, no convergence theorem, and no global-stability theorem for an explicit time-stepping algorithm. Aliased collocation is not automatically the exact Galerkin system.

For the analytical-PDE audience, the genuine next questions are: identify local well-posedness and the continuation space for this exact potential variant on the chosen periodic domain; establish uniform bounds for high derivatives; and distinguish spectrum broadening from a discretization defect or departure from the narrowband physical regime. Numerically bounded H2 on a fixed interval is finite-time evidence, not all-order smoothness, and not proof for arbitrary initial profiles.

Literature scope must remain explicit. Mosincat–Pilod–Saut establish small-data global well-posedness/scattering in `L2(R2)` and local theory in `Hs(R2), s>0`, for the equation(s) stated in their paper; this is not automatically a theorem for our periodic one-dimensional potential model. Heller–Shao's periodic paper studies multilinear/Strichartz estimates and obstructions; its displayed (1.1) uses conjugate coefficient **+1/4**, and must not be cited as a completed local/global theorem for our **−1/4** equation. Do not assert that no relevant theorem exists: say the report has not supplied a theorem matching this exact formulation/domain.

Primary links: https://arxiv.org/abs/2007.01613 ; https://arxiv.org/abs/2112.12734 ; https://math.mit.edu/research/highschool/primes/materials/2021/Heller-Shao.pdf .

A PINN output `v` is a candidate trajectory. The defect is `r=v_t-F(v)`, including the nonlocal term and the initial mismatch. A Gronwall error formula is legitimate **only after** establishing the needed stability estimate in a stated norm, accounting for derivative/nonlocal loss. For example, conditional on `d||u-v||_X/dt <= C(t)||u-v||_X+||r||_X`, one obtains `||u-v||(t) <= exp(integral C)[||u0-v0||+integral ||r||]`. This displayed hypothesis is the hard analytical step; the derivative nonlinearity prevents importing a cubic-NLS estimate merely by changing constants.

A more rigorous proposed endpoint is a verified residual-to-solution argument: define `G(u)=(u_t-F(u),u(0)-u0)` between appropriate trajectory and residual Banach spaces. For a bounded injective preconditioner `A:Y->X`, verify `||AG(v)||<=Y0` and `sup_ball ||I-ADG(u)||<=Z(r)<1` with `Y0+Z(r)r<=r`. Banach contraction for `T(u)=u-AG(u)` then gives a unique zero in the closed radius-r ball, provided G is C1 there and all bounds hold for the full infinite-dimensional problem. Fourier tails, temporal coverage, quadrature, rounding and initial data need certified bounds; a collocation loss alone does not meet these requirements. This is a proposed certificate, not one obtained in the pilot.

## Bounded proof-of-concept interpretation

Use a few controlled spatial initial profiles: a weakly perturbed uniform wavetrain for the complex MI test; a smooth localized packet for focusing, drift and front/back asymmetry; and a small family of random-phase narrowband profiles for sensitivity. Measure amplitude, phase, H1/H2, mass defect, resolved spectral tail, and signed perturbation gain; refine grid and time independently before interpreting later dynamics. Keep model-variant differences separate from learned-solver error. A model-consistency audit plus reproducible numerical controls and a transparently labelled PINN comparison is a useful proof of concept; neither “new Dysthe physics” nor a smoothness theorem is required to make it useful.
