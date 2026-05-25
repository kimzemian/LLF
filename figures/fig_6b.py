import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from datasets import load_from_disk
import os

# path = "/share/dean/github-data/github_v2_features_train"
# ds = load_from_disk(path)

# --- PARAMETERS -------------------------------------------------------------
FIVE_YEARS_DAYS = 365 * 5
HORIZONS = [30, 100, 365]
GRID_SIZE = 60


# # --- Add summed pushes+stars key for each horizon ---------------------------
# def add_pushes_stars(example, horizon):
#     push = example[f"cumulative_pushes_w_creates_{horizon}"]
#     stars = example[f"cumulative_stars_{horizon}"]
#     return {f"log_cumulative_pushes_stars_{horizon}": np.log1p(push + stars)}


# for h in HORIZONS:
#     ds = ds.map(lambda e: add_pushes_stars(e, h))
# ds.save_to_disk("/share/dean/github-data/github_v2_features_train_pushes_plus_stars")
ds = load_from_disk(
    "/share/dean/github-data/github_v2_features_train_pushes_plus_stars"
)
# --- 1. Compute global vmax for shared color scale ---------------------------
all_counts = []
for h in HORIZONS:
    c, *_ = np.histogram2d(
        ds[f"log_cumulative_pushes_stars_{h}"],
        ds["log_cumulative_forks_1825"],
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
        ds[f"log_cumulative_pushes_stars_{h}"],
        ds["log_cumulative_forks_1825"],
        gridsize=GRID_SIZE,
        cmap="viridis",
        norm=norm,
    )
    ax.set_xlabel(f"log(push+stars) @{h}d", fontsize=26)
    if idx == 0:
        ax.set_ylabel("log(forks + 1) @ 5yr", fontsize=26)
    ax.tick_params(axis="both", labelsize=22)

# --- 3. Shared colorbar -----------------------------------------------------
fig.subplots_adjust(right=0.88)
pos = axes[0].get_position()
cbar_ax = fig.add_axes([0.90, pos.y0, 0.015, pos.height])
cbar = fig.colorbar(last_hb, cax=cbar_ax)
cbar.set_label("log N points", fontsize=26)
cbar.ax.tick_params(labelsize=22)

out_dir = "/share/dean/plots"
os.makedirs(out_dir, exist_ok=True)
plt.savefig("plots/predicting_forks_pushes_plus_stars.pdf", bbox_inches="tight")
plt.show()
