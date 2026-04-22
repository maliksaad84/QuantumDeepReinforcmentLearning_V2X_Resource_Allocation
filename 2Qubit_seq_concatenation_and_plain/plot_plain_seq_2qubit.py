import matplotlib
matplotlib.use('Agg')  # for server / GPU / no display

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Load both datasets
# -------------------------
df_old = pd.read_csv("reward_2qubit.csv")
df_seq = pd.read_csv("reward_2qubit_sequential_concat.csv")

# -------------------------
# Smoothing
# -------------------------
df_old["Smoothed"] = df_old["QDRL_2Q_Reward"].rolling(
    window=35, center=True, min_periods=1
).mean()

df_seq["Smoothed"] = df_seq["QDRL_2Q_SEQ_Reward"].rolling(
    window=35, center=True, min_periods=1
).mean()

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(10, 5))

# Raw curves
plt.plot(
    df_old["Episode"], df_old["QDRL_2Q_Reward"],
    alpha=0.20, linewidth=1.0, label="2Q Reuploading Raw"
)

plt.plot(
    df_seq["Episode"], df_seq["QDRL_2Q_SEQ_Reward"],
    alpha=0.20, linewidth=1.0, label="2Q Sequential+Concat Raw"
)

# Smoothed curves
plt.plot(
    df_old["Episode"], df_old["Smoothed"],
    linewidth=2.8, label="2Q Reuploading Smoothed"
)

plt.plot(
    df_seq["Episode"], df_seq["Smoothed"],
    linewidth=2.8, label="2Q Sequential+Concat Smoothed"
)

plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.title("2-Qubit QDRL: Reuploading vs Sequential Encoding + Concatenation")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save figure
plt.savefig("comparison_2q_reuploading_vs_seqconcat.png", dpi=300, bbox_inches='tight')
print("✅ Figure saved as comparison_2q_reuploading_vs_seqconcat.png")
