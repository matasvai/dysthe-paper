from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
plt.rcParams.update({"font.family":"serif","font.size":9,"pdf.fonttype":42})
fig, ax=plt.subplots(figsize=(6.5,2.8))
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
def box(x,y,w,h,text):
    ax.add_patch(Rectangle((x,y),w,h,facecolor="white",edgecolor="black",linewidth=.8))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",linespacing=1.3)
def arrow(x,y,X,Y):
    ax.add_patch(FancyArrowPatch((x,y),(X,Y),arrowstyle="-|>",mutation_scale=9,color="black",linewidth=.8))
box(.015,.68,.28,.26,"Complete initial fields\nIndependent group splits")
box(.36,.68,.30,.26,"Qualified Fourier reference\nGrid, step and domain checks")
box(.735,.68,.25,.26,"Frozen test fields\nNo test-time fitting")
arrow(.295,.81,.36,.81)
box(.09,.29,.33,.25,"Supervised FNO\nData + short rollout loss")
box(.55,.29,.36,.25,"Same FNO + physics (PINO)\nFull nonlocal equation residual")
arrow(.46,.68,.255,.54); arrow(.56,.68,.73,.54)
box(.16,.015,.68,.15,"Autonomous rollouts: error, wave events, useful distance and cost")
arrow(.255,.29,.36,.165); arrow(.73,.29,.64,.165)
arrow(.96,.68,.96,.13); arrow(.96,.13,.84,.09)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
fig.savefig(Path(__file__).with_name("comparison_design.pdf"),bbox_inches="tight",pad_inches=.03)
