import os,json
os.environ.setdefault('MPLCONFIGDIR','/tmp/dysthe-mpl')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image,PageBreak,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from matplotlib.font_manager import findfont
for name,family,weight in [("GuideSerif","DejaVu Serif","normal"),("GuideBold","DejaVu Serif","bold"),("GuideSans","DejaVu Sans","normal")]:
 from matplotlib.font_manager import FontProperties
 pdfmetrics.registerFont(TTFont(name,findfont(FontProperties(family=family,weight=weight))))
pdfmetrics.registerFontFamily("GuideSerif",normal="GuideSerif",bold="GuideBold",italic="GuideSerif",boldItalic="GuideBold")
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
x=np.linspace(-12,12,1200);a=np.exp(-x*x/30)
fig,axs=plt.subplots(2,1,figsize=(8,4),layout='constrained')
for ax,ph,lab in zip(axs,[0,np.pi/2],['One ripple pattern','Same envelope; ripples shifted by a quarter cycle']):
 ax.plot(x,a*np.cos(3*x+ph),color='#236480',lw=1);ax.plot(x,a,'--',color='#ad493f',lw=1.7);ax.plot(x,-a,'--',color='#ad493f',lw=1.7);ax.set(xlim=(-12,12),ylim=(-1.1,1.1),title=lab,ylabel='Illustrative elevation');ax.spines[['top','right']].set_visible(False);ax.set_xticks([])
axs[-1].set_xlabel('Position');fig.savefig(OUT/'envelope_and_phase.png',dpi=180);plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(8,3),layout='constrained')
for ax,shape in zip(axs,[False,True]):
 for amp,col,lab in [(1,'#236480','Start'),(.25,'#d08a39','Later, illustrative')]:
  env=amp*np.exp(-x*x/(30 if amp==1 else 100));ax.plot(x,env/(amp if shape else 1),color=col,label=lab,lw=2)
 ax.set(xlabel='Position',ylabel='Displayed height',ylim=(0,1.1),title='Current peak: shape rescaled' if shape else 'Initial peak: amplitude preserved');ax.legend(fontsize=8);ax.spines[['top','right']].set_visible(False)
fig.savefig(OUT/'normalization.png',dpi=180);plt.close(fig)
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='BodyGuide',fontName='GuideSerif',fontSize=11,leading=15,spaceAfter=10));styles.add(ParagraphStyle(name='HeadingGuide',fontName='GuideBold',fontSize=22,leading=26,spaceAfter=16));styles.add(ParagraphStyle(name='SubGuide',fontName='GuideBold',fontSize=14,leading=18,spaceBefore=8,spaceAfter=8));styles.add(ParagraphStyle(name='CaptionGuide',fontName='GuideSans',fontSize=9,leading=12,textColor=colors.HexColor('#455666'),spaceAfter=12))
story=[];md=[]
def title(s):story.append(Paragraph(s,styles['HeadingGuide']));md.append('# '+s+'\n')
def sub(s):story.append(Paragraph(s,styles['SubGuide']));md.append('## '+s+'\n')
def p(s):story.append(Paragraph(s,styles['BodyGuide']));md.append(s.replace('<b>','').replace('</b>','')+'\n')
def pic(path,w,h,cap):story.extend([Image(str(path),width=w,height=h),Paragraph(cap,styles['CaptionGuide'])]);md.append(cap+'\n')
def page():story.append(PageBreak())
title('Reading the wave pictures')
p('A beginner\'s prerequisite guide to the phase-colored envelope viewer. No prior physics or complex-number knowledge is assumed. Research checkpoint: 14 September 2026.')
sub('The picture in one sentence')
p('We start with two localized groups of waves and use a simplified mathematical rule to see how their envelope spreads and changes. The colored hill tells us the local wave amplitude and phase. <b>It is not a literal hill of water.</b>')
p('Imagine a short train of ripples on a pond: the ripples near the middle are tall, and those near the ends are smaller. A smooth outline around their tops is the envelope. We compute that slower outline and its phase, rather than drawing every physical crest as part of the simulation.')
pic(OUT/'envelope_and_phase.png',475,238,'Illustration, not simulation data. Dashed curves bound the ripples. Shifting the ripples within the same outline changes phase while leaving envelope magnitude unchanged.')
p('The current viewer comes from the earlier <b>linear canonical model</b>. It is a simplified dispersive evolution used in the research. It is distinct from our later nonlinear Dysthe solitary-wave and collision experiments. Without additional scaling and reconstruction, its axes cannot be read as measured water-surface coordinates or elevations.')
page();title('1. Amplitude and phase: two pieces of information')
sub('Amplitude: how strong is the wave here?')
p('Amplitude measures the size of an oscillation. In a water-wave analogy it would relate to how high a ripple rises above its resting level. Our computed envelope magnitude is nonnegative: its height describes strength, not whether a particular physical crest is above or below the resting surface. It is not velocity.')
sub('Phase: where are we within an oscillation?')
p('Think of two clocks whose hands rotate at the same rate. One can be a quarter turn ahead of the other. Waves have an analogous position in their cycle: crest, descending through the middle, trough, and rising through the middle.')
p('The viewer uses cyclic colors to display that phase. A change of color does not mean hotter water, higher pressure, or faster flow. The two ends of the phase legend, minus pi and plus pi, mean the same cycle position. A full turn is 2 pi; a quarter turn is pi/2.')
sub('Why use a complex number?')
p('A complex number is a convenient way to store amplitude and phase together, like an arrow with a length and a direction. Its length is the magnitude; its angle is the phase. The imaginary part does not represent imaginary water or another physical height axis.')
p('If we choose an illustrative fast carrier, we can turn the envelope into a ripple drawing by combining its magnitude and phase with that carrier and taking the real part. That is what the earlier carrier close-ups do. The carrier was added for interpretation; it was not inferred from a measured fluid experiment.')
p('Near zero amplitude, phase is hard to interpret: a tiny change can rotate the arrow substantially. The viewer omits regions below 1% of its current sampled peak, so phase colors do not fill the display with negligible tails.')
page();title('2. How to read the interactive surface')
p('The two horizontal directions are x and z in a slice at y = 0. The vertical direction is envelope magnitude, not a third spatial direction. Rotating the view changes your viewpoint; it does not change the solution.')
sub('The most important control: Height scale')
p('<b>Initial peak</b> uses the same amplitude reference at every time. A displayed height of 0.1 means one tenth of the original reference peak. Use this setting when asking whether the wave is getting weaker.')
p('<b>Current peak</b> rescales each snapshot so its largest sampled value has height 1. This makes its shape easy to see even after it has become very small. A tall hill in this mode is not evidence that the wave retained its original strength.')
pic(OUT/'normalization.png',475,178,'Illustration of the two display rules. The later curve is weaker and wider. Rescaling it by its own maximum hides the amplitude decrease, while preserving the change of shape.')
sub('What the time slider means')
p('The slider selects 122 computed snapshots from t = 0 to 2056. The spacing is finer early and wider later; equal slider movements do not necessarily represent equal time intervals. Read the printed t value.')
p('Time and position are dimensionless model coordinates. <b>t = 2056 does not mean 2056 seconds</b>, and x = 10 does not mean ten metres. Converting to a particular experiment requires the physical scales and a justified relationship between that experiment and this canonical model.')
p('The camera shows an expanding central region, not every outgoing ripple. Its changing spatial range is printed. The separate magnitude-level-surface viewer has a different meaning: there all three axes are spatial coordinates, and the surface joins points having the same magnitude.')
page();title('3. Why does the packet spread and weaken?')
sub('A packet contains many wave components')
p('A localized packet is built from a mixture of wavelengths and directions. In a dispersive model these components accumulate phase differently. Their combined pattern changes shape and develops spreading, oscillatory tails. A useful analogy is a group of runners who start together and spread out because they move differently; it is an analogy for wave-pattern evolution, not for the movement of individual fluid particles.')
p('Dispersion can reduce the largest local amplitude without friction removing the signal. The present model has no damping term. For sufficiently localized whole-space solutions, it preserves the integral of squared envelope magnitude. The pattern can therefore become weaker locally while that total stays fixed. This mathematical conserved quantity is not, by itself, a calibrated measurement of the fluid\'s physical energy.')
sub('What our current calculation actually shows')
p('The sampled peak in the displayed central region falls to about 4.65% of its initial reference by t = 256 and about 0.64% by t = 2056. These are computed amplitude ratios, not water heights in centimetres. They are also not a new proven decay law or certified whole-space maximum.')
p('Try t = 0, 64, 256, and 2056 with the height scale set to Initial peak. Then switch to Current peak and repeat. The first pass shows the loss of local strength. The second pass shows the changing geometry that the first pass makes increasingly hard to see.')
sub('What is moving?')
p('A moving peak is a feature of the wave pattern. It is not a tagged parcel of water. Similarly, the envelope and the individual carrier crests need not travel together. The current model does not provide fluid-particle paths, velocity vectors, or pressure fields.')
page();title('4. Overlap, interference, and solitary waves')
sub('A correction specific to our two packets')
p('Our initial packets have different strengths, and the second starts a quarter cycle out of phase. For this particular linear equation, a real initial field stays real as it evolves. The two contributions therefore remain in quadrature: one is real and the other purely imaginary, up to signs.')
p('Consequently their squared magnitudes add without an extra intensity cross-term. They can overlap and change their combined outline, but their original quarter-cycle pairing does not produce mutual reinforcement or cancellation in that squared magnitude. The earlier interpretation suggesting otherwise was incorrect for this chosen model and initial condition.')
p('To show genuine positive and negative interference, we made a separately labeled control with the initial phase offset set to zero. Its red regions reinforce and its blue regions cancel. Those colors belong to an interference map; they do not have the same meaning as the colors in the phase viewer.')
sub('Why this is not a soliton demonstration')
p('A solitary wave maintains a localized traveling shape through a balance that often involves both dispersion and nonlinearity. This viewer includes only linear dispersion. A rescaled hill that remains visible at late times is not evidence of a soliton: Current peak forces every snapshot back to height 1.')
p('Our nonlinear solver experiments are a separate part of the project. They test computed traveling waves, perturbations, collisions, and transverse response. Their conclusions must be assessed using their own equations and numerical checks, not transferred from this animation.')
sub('What you can safely take away')
p('The current viewer shows how a specified model redistributes a localized wave envelope, how its local strength decreases, and how its phase varies across space. It is a way to understand wave-pattern evolution. Predicting a particular tank, ocean wave, or optical experiment would additionally require physical units, suitable initial data, the appropriate model, and validation against that setting.')
p('Basis: formal checkpoint, Section 3.4; the phase viewer extension records; and the packet-visualization correction note. The two drawings here are explanatory illustrations, not new experiments.')

def footer(c,d):
 c.saveState();c.setFont('GuideSans',9);c.setFillColor(colors.HexColor('#5b6470'));c.drawString(54,30,'Reading the wave pictures | Beginner\'s guide');c.drawRightString(558,30,str(d.page));c.restoreState()
doc=SimpleDocTemplate(str(ROOT/'output/pdf/wave_visualizations_beginners_guide.pdf'),pagesize=(612,792),rightMargin=54,leftMargin=54,topMargin=50,bottomMargin=50,title='Reading the wave pictures: a beginner\'s guide',author='Research checkpoint')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
(OUT/'guide.md').write_text('\n'.join(md))
print('Guide created')
