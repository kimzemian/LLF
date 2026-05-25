import matplotlib.pyplot as plt
import numpy as np
from datasets import load_from_disk
from matplotlib.colors import LogNorm
from matplotlib.lines import Line2D
import matplotlib.cm as cm

# Load dataset
path = "/share/dean/arxiv-data/cutoff_with_features"
ds = load_from_disk(path)

# Horizon labels and corresponding keys
horizons = {
    "30d": "30",
    "100d": "100",
    "1yr": "365",
    "5yr": "1825",
}

# Colormaps
blue_cmap = cm.get_cmap("Blues", len(horizons) + 4)
orange_cmap = cm.get_cmap("Oranges", len(horizons) + 4)

# Keys and titles
keys = ["dl", "cites"]
titles = ["Cumulative Accesses", "Cumulative Citations"]
cmaps = [blue_cmap, orange_cmap]

# Setup figure
fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=False, sharey=False)

for ax, key_prefix, title, cmap in zip(axes, keys, titles, cmaps):
    legend = []
    for i, (label, suffix) in enumerate(horizons.items()):
        key = f"{key_prefix}_{suffix}"
        d = np.asarray(ds[key])
        d = d[d > 0]
        bins = np.logspace(np.log10(d.min()), np.log10(d.max()), 100)
        color = cmap(i + 3)
        ax.hist(d, bins=bins, histtype="step", color=color, linewidth=1.5)
        legend.append(Line2D([0], [0], color=color, lw=2, label=label))

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title(title, fontsize=20)
    ax.set_ylabel("# Repositories (log)", fontsize=18)
    ax.legend(handles=legend, loc="upper right", fontsize=14, frameon=False)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.6)
    ax.tick_params(axis="both", labelsize=14)

axes[-1].set_xlabel("Cumulative Count", fontsize=18)

plt.tight_layout()
plt.savefig("plots/accesses_citations_marginals.pdf", format="pdf", bbox_inches="tight")
plt.show()
