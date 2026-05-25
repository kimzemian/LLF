import pickle
from datasets import load_from_disk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os
from tqdm import tqdm

# Font settings
rcParams.update(
    {
        "font.size": 20,  # All font sizes
        "xtick.labelsize": 18,  # Tick label size for x-axis
        "ytick.labelsize": 18,  # Tick label size for y-axis
    }
)

path = "/share/dean/arxiv-data/"

# Load correlations
with open(path + "correlations.pkl", "rb") as f:
    correlations = pickle.load(f)

# Constants
T = 1825  # 5 years
days = np.arange(1, T + 1)

deep_blue = plt.get_cmap("Blues")(0.8)
deep_orange = plt.get_cmap("Oranges")(0.8)

color_map = {
    "Log(# Citations + 1)": deep_orange,
    "Log(# Accesses + 1)": deep_blue,
}

# Plot
plt.figure(figsize=(8, 6))
for label, series in correlations.items():
    plt.plot(days, series, label=label, linewidth=2.0, color=color_map[label])

plt.xscale("log")
plt.ylim(-0.02, 1)
plt.xlabel("Day", fontsize=22)
plt.ylabel("Pearson coefficient with Citations @5yr", fontsize=20)
plt.legend(loc="upper left", fontsize=20, frameon=True)
plt.grid(alpha=0.3)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# plt.tight_layout()
plt.savefig("arxiv_plots/arxiv_correlation.pdf")
# , bbox_inches="tight")
plt.show()
