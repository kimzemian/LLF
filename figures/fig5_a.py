from datasets import load_dataset, load_from_disk, concatenate_datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

# # copy_path = "/share/dean/tmp/github/train_copy"
# path = "/share/dean/gharchive/data/train"
# ds = load_from_disk(path)


# import matplotlib.pyplot as plt


# # Step 1: Compute min(first_create, first_push)
# def compute_min_create_push(example):
#     first_create = example.get("first_create")
#     first_push = example.get("first_push")

#     # Handle missing values
#     if first_create is None and first_push is None:
#         example["first_activity"] = None
#     elif first_create is None:
#         example["first_activity"] = first_push
#     elif first_push is None:
#         example["first_activity"] = first_create
#     else:
#         example["first_activity"] = min(first_create, first_push)

#     return example


# ds = ds.map(compute_min_create_push)


# # Step 1: Compute lags safely
# def compute_lags(example):
#     push = example.get("first_activity")
#     star = example.get("first_star")
#     fork = example.get("first_fork")

#     example["lag_star_push"] = (
#         star - push if star is not None and push is not None else None
#     )
#     example["lag_fork_push"] = (
#         fork - push if fork is not None and push is not None else None
#     )
#     return example


# ds = ds.map(compute_lags)

# # Step 2: Convert to pandas
# df = ds.select_columns(["lag_star_push", "lag_fork_push"]).to_pandas()
# df = df.dropna()

# save_path = "/share/dean/tmp/github/lag_df"
# df.to_csv(save_path + ".csv", index=False)


# # Load the preprocessed dataframe
# df = pd.read_csv("/share/dean/tmp/github/lag_df.csv")

# # Sort the values for a clean line plot
# sorted_star_lag = np.sort(df["lag_star_push"].values)
# sorted_fork_lag = np.sort(df["lag_fork_push"].values)

# # Plotting
# plt.figure(figsize=(8, 4))
# plt.plot(sorted_star_lag, label="Star - First Activity")
# plt.plot(sorted_fork_lag, label="Fork - First Activity")
# plt.xlabel("Repository Index (sorted)")
# plt.ylabel("Lag (Days)")
# plt.title("Lag Between First Activity and Stars/Forks")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.savefig(
#     "plots/github_lag_plot.pdf",
#     bbox_inches="tight",
# )  # Save the plot as a PNG file
# plt.show()


from datasets import load_from_disk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# --- Load dataset ---
ds = load_from_disk("/share/dean/gharchive/data/train")
df = ds.select_columns(["first_star", "first_fork"]).to_pandas().dropna()


# --- Sort and Plot ---
sorted_star = np.sort(df["first_star"].values)
sorted_fork = np.sort(df["first_fork"].values)


def thousands_formatter(x, _):
    if x < 1000:
        return f"{x/1000:.1f}k"
    elif x % 1000 == 0:
        return f"{int(x/1000)}k"
    else:
        return f"{x/1000:.1f}k"


plt.figure(figsize=(8, 6))
plt.plot(sorted_star + 1, label="First Star - First Push", color="green")
plt.plot(sorted_fork + 1, label="First Fork - First Push", color="purple")
plt.yscale("log")
plt.xlabel("Repository Index (sorted)", fontsize=22)
plt.ylabel("Lag (Days) - log scale", fontsize=22)
# plt.title("Lag Between First Activity and Star/Fork", fontsize=20)


plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.legend(fontsize=22)
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/github_lag_plot.pdf", bbox_inches="tight")
plt.show()
