"""Plot the analytical asymptotic boundary for one target with r=1."""
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from check_ladders import constants

HERE = Path(__file__).resolve().parent
r = 1.
rows = []
for lam in np.logspace(-7, 4, 400):
    c = constants(r, float(lam))
    rows.append({"lambda": float(lam), "u": c["epsilon_n_limit"],
                 "v": c["epsilon_E_limit"]})
rows.sort(key=lambda x: x["u"])
u0 = r*r
v0 = .5*r*math.sinh(2*r)-r*r
vinf = 2*(math.cosh(r)-1)**2
xs = np.r_[u0, [x["u"] for x in rows]]
ys = np.r_[v0, [x["v"] for x in rows]]
assert np.all(np.diff(xs) >= -1e-12)
assert np.min(ys) >= vinf-1e-12
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,
                     "axes.spines.top":False,"axes.spines.right":False,
                     "svg.fonttype":"path"})
fig, ax = plt.subplots(figsize=(7.6,4.8), constrained_layout=True)
ax.fill_between(xs,ys,.88,color="#dceef1",alpha=.85)
ax.plot(xs,ys,color="#087f8c",lw=2.5,label="Attainable boundary")
ax.axhline(vinf,color="#9d591f",lw=1.5,ls="--",
           label=f"Photon infimum: {vinf:.6f}")
ax.scatter([u0],[v0],color="#22313d",s=42,zorder=5)
ax.annotate("Fewest modes",(u0,v0),(1.16,.842),
            arrowprops={"arrowstyle":"-","color":"#22313d"},
            color="#22313d",ha="left",fontsize=10)
points=[]
for lam,offset in [(.1,(12,16)),(.01,(14,18))]:
    c=constants(r,lam); u,v=c["epsilon_n_limit"],c["epsilon_E_limit"]
    points.append({"lambda":lam,"u":u,"v":v})
    ax.scatter([u],[v],s=30,color="#087f8c",zorder=5)
    ax.annotate(rf"$\lambda={lam:g}$",(u,v),xytext=offset,
                textcoords="offset points",fontsize=10,color="#075f68")
ax.text(2.15,.775,"Feasible budgets",ha="center",color="#45656a")
ax.set(xlim=(.97,2.7),ylim=(.57,.87),
       xlabel=r"Normalized catalyst mode budget  $u=\varepsilon n$",
       ylabel=r"Normalized photon budget  $v=\varepsilon E$",
       title="Mode and photon costs for one squeezed pair (r = 1)")
ax.grid(axis="y",color="#d6dde1",lw=.6,alpha=.7)
ax.legend(loc="upper right",frameon=False,fontsize=10)
fig.savefig(HERE/"tradeoff.svg")
fig.savefig(HERE.parent.parent/"tradeoff_preview.png",dpi=160)
data={"target_r":r,"minimum_mode":{"u":u0,"v":v0},
      "photon_infimum":vinf,"marked_contacts":points,"curve":rows}
(HERE/"tradeoff_curve.json").write_text(json.dumps(data,indent=2)+"\n")
print(json.dumps({k:v for k,v in data.items() if k!="curve"},indent=2))
