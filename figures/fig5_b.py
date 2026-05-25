import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.lines import Line2D
from datasets import load_dataset, load_from_disk, concatenate_datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

path = "/share/dean/github-data/github_v2_features_train"
# Load dataset
ds = load_from_disk(path)

# Define horizon mappings
horiz_forks = {
    "30d": "cumulative_forks_30",
    "100d": "cumulative_forks_100",
    "1yr": "cumulative_forks_365",
    "5yr": "cumulative_forks_1825",
}
horiz_pushes = {
    "30d": "cumulative_pushes_w_creates_30",
    "100d": "cumulative_pushes_w_creates_100",
    "1yr": "cumulative_pushes_w_creates_365",
    "5yr": "cumulative_pushes_w_creates_1825",
}
horiz_watches = {
    "30d": "cumulative_stars_30",
    "100d": "cumulative_stars_100",
    "1yr": "cumulative_stars_365",
    "5yr": "cumulative_stars_1825",
}

# Setup
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True, sharey=True)

horizon_labels = list(horiz_forks.keys())
num_horizons = len(horizon_labels)

# Color maps
color_maps = [
    cm.get_cmap("Oranges", num_horizons + 4),
    cm.get_cmap("Greens", num_horizons + 4),
    cm.get_cmap("Purples", num_horizons + 4),
]
titles = ["Pushes", "Stars", "Forks"]
mappings = [horiz_forks, horiz_pushes, horiz_watches]
legends = []

# for ax, mapping, cmap, title in zip(axes, mappings, color_maps, titles):
#     legend = []
#     for i, h in enumerate(horizon_labels):
#         col = mapping[h]
#         d = np.asarray(ds[col])
#         d = d[d > 0]
#         bins = np.logspace(np.log10(d.min()), np.log10(d.max()), 100)
#         color = cmap(i + 3)
#         ax.hist(d, bins=bins, histtype="step", color=color, linewidth=1.5)
#         legend.append(Line2D([0], [0], color=color, lw=2, label=h))

#     ax.set_xscale("log")
#     ax.set_yscale("log")
#     ax.set_title(title, fontsize=14)
#     ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.6)
#     legends.append(legend)

# for ax, mapping, cmap, title in zip(axes, mappings, color_maps, titles):
#     legend = []
#     for i, h in enumerate(horizon_labels):
#         col = mapping[h]
#         d = np.asarray(ds[col])
#         d = d[d > 0]
#         bins = np.logspace(np.log10(d.min()), np.log10(d.max()), 100)
#         color = cmap(i + 3)
#         ax.hist(d, bins=bins, histtype="step", color=color, linewidth=1.5)
#         legend.append(Line2D([0], [0], color=color, lw=2, label=h))

#     ax.set_xscale("log")
#     ax.set_yscale("log")

#     ax.set_title(title, fontsize=20)
#     ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.6)
#     ax.legend(handles=legend, loc="upper right", fontsize=16, frameon=False)
#     plt.yticks(fontsize=16)

for ax, mapping, cmap, title in zip(axes, mappings, color_maps, titles):
    legend = []
    for i, h in enumerate(horizon_labels):
        col = mapping[h]
        d = np.asarray(ds[col])
        d = d[d > 0]
        bins = np.logspace(np.log10(d.min()), np.log10(d.max()), 100)
        color = cmap(i + 3)
        ax.hist(d, bins=bins, histtype="step", color=color, linewidth=1.5)
        legend.append(Line2D([0], [0], color=color, lw=2, label=h))

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title, fontsize=20)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.6)
    ax.legend(handles=legend, loc="upper right", fontsize=16, frameon=False)

    ax.tick_params(axis="y", labelsize=16)  # <-- add this here


# Labels
axes[-1].set_xlabel("Cumulative event count", fontsize=20)
for ax in axes:
    ax.set_ylabel("# repositories (log)", fontsize=20)

# Add stacked legends
# for i, legend_handles in enumerate(legends):
#     fig.legend(
#         handles=legend_handles,
#         loc="upper right",
#         bbox_to_anchor=(1, 1 - i * 0.02),
#         ncol=4,
#         frameon=False,
#         fontsize=11,
#         # title=titles[i],
#         title_fontsize=12,
#     )

plt.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for legends
plt.savefig(
    "plots/pretty_marginals_forks_pushes_watches.pdf",
    format="pdf",
    bbox_inches="tight",
)

plt.xticks(fontsize=16)

plt.show()
