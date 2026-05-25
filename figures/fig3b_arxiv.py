from datasets import load_dataset, load_from_disk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
import numpy as np
import pandas as pd
from datetime import timedelta

path = "/share/dean/arxiv-data/cutoff_with_features"
ds = load_from_disk(path)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# --- PARAMETERS -------------------------------------------------------------
FIVE_YEARS_DAYS = 365 * 5
HORIZONS = [30, 100, 365]
GRID_SIZE = 60

# --- 1. Compute global vmax for shared color scale ---------------------------
all_counts = []
for h in HORIZONS:
    c, *_ = np.histogram2d(
        ds[f"log_dl_{h}"],
        ds["log_cites_1825"],
        bins=GRID_SIZE,
    )
    all_counts.append(c.max())

global_vmax = max(all_counts)
norm = LogNorm(vmin=1, vmax=global_vmax)

# --- 2. Plot hexbins ---------------------------------------------------------
fig, axes = plt.subplots(1, len(HORIZONS), figsize=(6 * len(HORIZONS), 5), sharey=True)

if len(HORIZONS) == 1:
    axes = [axes]

last_hb = None
for idx, (ax, h) in enumerate(zip(axes, HORIZONS)):
    last_hb = ax.hexbin(
        ds[f"log_dl_{h}"],
        ds["log_cites_1825"],
        gridsize=GRID_SIZE,
        cmap="viridis",
        norm=norm,
    )
    ax.set_xlabel(f"log(access+1) at {h}d", fontsize=26)
    # ax.set_title(f"log access({h} day)  vs  5-y citations", fontsize=20)
    if idx == 0:
        ax.set_ylabel("log(cites+1) at 5 years", fontsize=26)

    ax.tick_params(axis="both", which="major", labelsize=22)

# --- 3. Shared colorbar, exactly same height as plots ------------------------
fig.subplots_adjust(right=0.88)
pos = axes[0].get_position()
cbar_ax = fig.add_axes([0.90, pos.y0, 0.015, pos.height])
cbar = fig.colorbar(last_hb, cax=cbar_ax)
cbar.set_label("log(N+1) points", fontsize=26)
cbar.ax.tick_params(labelsize=22)

plt.savefig("arxiv_plots/hexbin_dl_cites_5y.pdf", bbox_inches="tight")
plt.show()
