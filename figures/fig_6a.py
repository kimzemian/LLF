import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

T = 1825  # 5 years
path = "/share/dean/github-data/"
days = np.arange(1, T + 1)
deep_orange = plt.get_cmap("Oranges")(0.8)
color_map = {
    "Log(# Pushes + 1)": "#d95f02",  # deep orange
    "Log(# Stars + 1)": "Green",  # forest green
    "Log(# Forks + 1)": "Purple",  # purple
}

# Load pickle file
with open(path + "github_correlations.pkl", "rb") as f:
    correlations = pickle.load(f)

# Plot
plt.figure(figsize=(8, 6))
for label in color_map:
    if label in correlations:
        plt.plot(
            days,
            correlations[label],
            label=label,
            linewidth=2.0,
            color=color_map[label],
        )

plt.xscale("log")
plt.ylim(-0.05, 1.05)
plt.xlabel("Day", fontsize=22)
plt.ylabel("Pearson coefficient with Forks @5yr", fontsize=22)
plt.legend(loc="upper left", fontsize=20, frameon=True)
plt.grid(alpha=0.3)
# plt.tight_layout()
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig("plots/github_correlation_coef.pdf")
plt.show()
