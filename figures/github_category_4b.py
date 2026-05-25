import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from datasets import load_dataset, load_from_disk, concatenate_datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle


path = "/share/dean/github-data/"
with open("categories.pkl", "rb") as f:
    caties = pickle.load(f)
with open("counts.pkl", "rb") as f:
    counts = pickle.load(f)

# Convert to list in case they're tuples
categories = list(caties)
counts = list(counts)
print(f"Number of categories: {len(categories)}")

# Get top 20 from the end (since already sorted ascending)
top_categories = categories[-15:]
top_counts = counts[-15:]

# Dark-to-pale palette
palette = sns.color_palette("Blues", n_colors=len(top_categories))

# Plot
plt.figure(figsize=(8, 5))
plt.bar(x=top_categories, height=top_counts, color=palette)
plt.xlabel("Platform", fontsize=20)
plt.ylabel("Number of Repositories", fontsize=20)
# plt.title("Top 20 Platforms by Number of Repositories", fontsize=16)
plt.xticks(rotation=45, ha="right", fontsize=20)
plt.yticks(fontsize=16)

# Format y-axis to use 'k' instead of 1000s
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x/1000)}k"))

plt.tight_layout()
plt.savefig("plots/github_platform_distribution_top15.pdf")
plt.show()
