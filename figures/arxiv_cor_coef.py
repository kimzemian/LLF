from datasets import load_from_disk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

import numpy as np
import matplotlib.pyplot as plt
from datasets import load_from_disk
from tqdm import tqdm


path = "/share/dean/arxiv-data/cutoff_with_features"
ds = load_from_disk(path)


# Constants
T = 1825  # 5 years
days = np.arange(1, T + 1)

# Keys and display labels
event_keys = {
    "Log(# Citations + 1)": "cumulative_citations_offset",
    "Log(# Accesses + 1)": "cumulative_accesses",
}


deep_blue = plt.get_cmap("Blues")(0.8)  # value ∈ [0, 1]; higher = darker
deep_orange = plt.get_cmap("Oranges")(0.8)  # value ∈ [0, 1]; higher = darker
# Color palette

color_map = {
    "Log(# Citations + 1)": deep_orange,  # deep orange
    "Log(# Accesses + 1)": deep_blue,
}

# Precompute target (final forks @ day 1825)
y = np.log1p(
    np.array(ds.map(lambda ex: {"target": ex["cumulative_citations"][T - 1]})["target"])
)

# Precompute log-transformed cumulative curves
X_all = {
    label: np.log1p(np.stack([ex[key][:T] for ex in ds]))
    for label, key in event_keys.items()
}

# Compute correlations
correlations = {
    label: [np.corrcoef(X[:, t], y)[0, 1] for t in tqdm(range(T))]
    for label, X in X_all.items()
}

# save the correlations
path = "/share/dean/arxiv-data/"
with open(path + "correlations.pkl", "wb") as f:
    pickle.dump(correlations, f)


# Plot
plt.figure(figsize=(8, 6))
for label, series in correlations.items():
    plt.plot(days, series, label=label, linewidth=2.0, color=color_map[label])

plt.xscale("log")
plt.ylim(-0.02, 1.05)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Pearson coefficient with Citations by Year 5", fontsize=12)
plt.legend(loc="lower right", fontsize=10, frameon=True)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.tight_layout()
plt.savefig("arxiv_plots/arxiv_correlation.pdf", bbox_inches="tight")
plt.show()
