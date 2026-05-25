import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import timedelta
from matplotlib.ticker import FuncFormatter
from datasets import load_dataset, load_from_disk, concatenate_datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

# path = "/share/dean/gharchive/batches_v2/"
# # Define the batch folders to load (last 4 batches)
# batch_folders = ["batch_2", "batch_3", "batch_4", "batch_5"]

# # Load each dataset from disk
# datasets = []
# for folder in batch_folders:
#     dataset = load_from_disk(path + folder)
#     datasets.append(dataset)
#     print(f"Loaded dataset from {folder}")

# # Combine all datasets
# ds = concatenate_datasets(datasets)
# print(f"Combined dataset has {len(ds)} examples")

ds = load_from_disk("/share/dean/gharchive/data/train")
ds.set_format("numpy")
# Method 1: Set global font sizes (recommended for consistency)
# Adjust these values to make fonts larger/smaller
# plt.rcParams.update(
#     {
#         "font.size": 14,  # Base font size
#         "axes.titlesize": 18,  # Title font size
#         "axes.labelsize": 16,  # Axis label font size
#         "xtick.labelsize": 14,  # X-axis tick label size
#         "ytick.labelsize": 14,  # Y-axis tick label size
#         "legend.fontsize": 14,  # Legend font size
#         "figure.titlesize": 20,  # Figure title size
#     }
# )

# # Constants
# DAYS_IN_YEAR = 365
# idx_1yr = DAYS_IN_YEAR - 1
# idx_5yr = 5 * DAYS_IN_YEAR - 1

# Get 'start' dates
start_dates = np.array([x["created_date"] for x in ds])

# Plot histogram of repo creation times
plt.figure(figsize=(8, 4))
plt.hist(start_dates, bins=100, color="#4C72B0")
# plt.title("Distribution of Repository Creation Times")
plt.xlabel("Creation Date", fontsize=20)
plt.ylabel("Repository Count", fontsize=18)
plt.xticks(rotation=45, ha="right", fontsize=20)
plt.yticks(fontsize=16)

plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x/1000)}k"))

plt.tight_layout()
plt.savefig(
    "plots/repo_creation_times.pdf",
    format="pdf",
    bbox_inches="tight",
)
plt.show()
