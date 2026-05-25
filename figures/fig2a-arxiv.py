import matplotlib.pyplot as plt
from datasets import load_dataset, load_from_disk, concatenate_datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
from matplotlib.ticker import FuncFormatter

# path = "/share/dean/arxiv-data/cutoff_with_features"
# ds = load_from_disk(path)


# # Function to find first nonzero index
# def first_nonzero_idx(arr):
#     nonzeros = np.nonzero(arr)[0]
#     return int(nonzeros[0]) if len(nonzeros) > 0 else -1


# # Map function to create new keys
# def add_firsts(example):
#     example["first_access_time"] = first_nonzero_idx(example["cumulative_accesses"])
#     example["first_citation_time"] = first_nonzero_idx(
#         example["cumulative_citations_offset"]
#     )
#     return example


# # Apply map
# ds = ds.map(add_firsts)

# # Filter out invalid rows
# valid_ds = ds.filter(
#     lambda x: x["first_access_time"] >= 0 and x["first_citation_time"] >= 0
# )

# # Compute difference
# differences = np.array(valid_ds["first_citation_time"]) - np.array(
#     valid_ds["first_access_time"]
# )

# # Sort for line plot
# sorted_diff = np.sort(differences)

# # save
# np.save("/share/dean/arxiv-data/citation_delay.npy", sorted_diff)

# load
sorted_diff = np.load("/share/dean/arxiv-data/citation_delay.npy")


def thousands_formatter(x, _):
    if x < 1000:
        return f"{x/1000:.1f}k"
    elif x % 1000 == 0:
        return f"{int(x/1000)}k"
    else:
        return f"{x/1000:.1f}k"


plt.figure(figsize=(8, 5))  # slightly larger
plt.plot(sorted_diff, color="#d95f02")

plt.xlabel("Paper Index (sorted)", fontsize=20)
plt.ylabel("Citation Lag (Days) - log scale", fontsize=20)
# plt.title(
#     "Citation Lag After First Access", fontsize=20, pad=20
# )  # Add padding to avoid clipping

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.yscale("log")
# plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

plt.grid(True)

# These two lines will stop all label clipping:
# plt.tight_layout()
# plt.subplots_adjust(left=0.15)  # Manually shift left margin
plt.subplots_adjust(top=0.88, left=0.18, bottom=0.18)

plt.savefig("arxiv_plots/citation_delay_sorted.pdf", pad_inches=0.2)
# bbox_inches="tight"
plt.show()
