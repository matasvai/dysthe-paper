# Reading the wave pictures

A beginner's prerequisite guide to the phase-colored envelope viewer. No prior physics or complex-number knowledge is assumed. Research checkpoint: 14 September 2026.

## The picture in one sentence

We start with two localized groups of waves and use a simplified mathematical rule to see how their envelope spreads and changes. The colored hill tells us the local wave amplitude and phase. It is not a literal hill of water.

Imagine a short train of ripples on a pond: the ripples near the middle are tall, and those near the ends are smaller. A smooth outline around their tops is the envelope. We compute that slower outline and its phase, rather than drawing every physical crest as part of the simulation.

Illustration, not simulation data. Dashed curves bound the ripples. Shifting the ripples within the same outline changes phase while leaving envelope magnitude unchanged.

The current viewer comes from the earlier linear canonical model. It is a simplified dispersive evolution used in the research. It is distinct from our later nonlinear Dysthe solitary-wave and collision experiments. Without additional scaling and reconstruction, its axes cannot be read as measured water-surface coordinates or elevations.

# 1. Amplitude and phase: two pieces of information

## Amplitude: how strong is the wave here?

Amplitude measures the size of an oscillation. In a water-wave analogy it would relate to how high a ripple rises above its resting level. Our computed envelope magnitude is nonnegative: its height describes strength, not whether a particular physical crest is above or below the resting surface. It is not velocity.

## Phase: where are we within an oscillation?

Think of two clocks whose hands rotate at the same rate. One can be a quarter turn ahead of the other. Waves have an analogous position in their cycle: crest, descending through the middle, trough, and rising through the middle.

The viewer uses cyclic colors to display that phase. A change of color does not mean hotter water, higher pressure, or faster flow. The two ends of the phase legend, minus pi and plus pi, mean the same cycle position. A full turn is 2 pi; a quarter turn is pi/2.

## Why use a complex number?

A complex number is a convenient way to store amplitude and phase together, like an arrow with a length and a direction. Its length is the magnitude; its angle is the phase. The imaginary part does not represent imaginary water or another physical height axis.

If we choose an illustrative fast carrier, we can turn the envelope into a ripple drawing by combining its magnitude and phase with that carrier and taking the real part. That is what the earlier carrier close-ups do. The carrier was added for interpretation; it was not inferred from a measured fluid experiment.

Near zero amplitude, phase is hard to interpret: a tiny change can rotate the arrow substantially. The viewer omits regions below 1% of its current sampled peak, so phase colors do not fill the display with negligible tails.

# 2. How to read the interactive surface

The two horizontal directions are x and z in a slice at y = 0. The vertical direction is envelope magnitude, not a third spatial direction. Rotating the view changes your viewpoint; it does not change the solution.

## The most important control: Height scale

Initial peak uses the same amplitude reference at every time. A displayed height of 0.1 means one tenth of the original reference peak. Use this setting when asking whether the wave is getting weaker.

Current peak rescales each snapshot so its largest sampled value has height 1. This makes its shape easy to see even after it has become very small. A tall hill in this mode is not evidence that the wave retained its original strength.

Illustration of the two display rules. The later curve is weaker and wider. Rescaling it by its own maximum hides the amplitude decrease, while preserving the change of shape.

## What the time slider means

The slider selects 122 computed snapshots from t = 0 to 2056. The spacing is finer early and wider later; equal slider movements do not necessarily represent equal time intervals. Read the printed t value.

Time and position are dimensionless model coordinates. t = 2056 does not mean 2056 seconds, and x = 10 does not mean ten metres. Converting to a particular experiment requires the physical scales and a justified relationship between that experiment and this canonical model.

The camera shows an expanding central region, not every outgoing ripple. Its changing spatial range is printed. The separate magnitude-level-surface viewer has a different meaning: there all three axes are spatial coordinates, and the surface joins points having the same magnitude.

# 3. Why does the packet spread and weaken?

## A packet contains many wave components

A localized packet is built from a mixture of wavelengths and directions. In a dispersive model these components accumulate phase differently. Their combined pattern changes shape and develops spreading, oscillatory tails. A useful analogy is a group of runners who start together and spread out because they move differently; it is an analogy for wave-pattern evolution, not for the movement of individual fluid particles.

Dispersion can reduce the largest local amplitude without friction removing the signal. The present model has no damping term. For sufficiently localized whole-space solutions, it preserves the integral of squared envelope magnitude. The pattern can therefore become weaker locally while that total stays fixed. This mathematical conserved quantity is not, by itself, a calibrated measurement of the fluid's physical energy.

## What our current calculation actually shows

The sampled peak in the displayed central region falls to about 4.65% of its initial reference by t = 256 and about 0.64% by t = 2056. These are computed amplitude ratios, not water heights in centimetres. They are also not a new proven decay law or certified whole-space maximum.

Try t = 0, 64, 256, and 2056 with the height scale set to Initial peak. Then switch to Current peak and repeat. The first pass shows the loss of local strength. The second pass shows the changing geometry that the first pass makes increasingly hard to see.

## What is moving?

A moving peak is a feature of the wave pattern. It is not a tagged parcel of water. Similarly, the envelope and the individual carrier crests need not travel together. The current model does not provide fluid-particle paths, velocity vectors, or pressure fields.

# 4. Overlap, interference, and solitary waves

## A correction specific to our two packets

Our initial packets have different strengths, and the second starts a quarter cycle out of phase. For this particular linear equation, a real initial field stays real as it evolves. The two contributions therefore remain in quadrature: one is real and the other purely imaginary, up to signs.

Consequently their squared magnitudes add without an extra intensity cross-term. They can overlap and change their combined outline, but their original quarter-cycle pairing does not produce mutual reinforcement or cancellation in that squared magnitude. The earlier interpretation suggesting otherwise was incorrect for this chosen model and initial condition.

To show genuine positive and negative interference, we made a separately labeled control with the initial phase offset set to zero. Its red regions reinforce and its blue regions cancel. Those colors belong to an interference map; they do not have the same meaning as the colors in the phase viewer.

## Why this is not a soliton demonstration

A solitary wave maintains a localized traveling shape through a balance that often involves both dispersion and nonlinearity. This viewer includes only linear dispersion. A rescaled hill that remains visible at late times is not evidence of a soliton: Current peak forces every snapshot back to height 1.

Our nonlinear solver experiments are a separate part of the project. They test computed traveling waves, perturbations, collisions, and transverse response. Their conclusions must be assessed using their own equations and numerical checks, not transferred from this animation.

## What you can safely take away

The current viewer shows how a specified model redistributes a localized wave envelope, how its local strength decreases, and how its phase varies across space. It is a way to understand wave-pattern evolution. Predicting a particular tank, ocean wave, or optical experiment would additionally require physical units, suitable initial data, the appropriate model, and validation against that setting.

Basis: formal checkpoint, Section 3.4; the phase viewer extension records; and the packet-visualization correction note. The two drawings here are explanatory illustrations, not new experiments.
