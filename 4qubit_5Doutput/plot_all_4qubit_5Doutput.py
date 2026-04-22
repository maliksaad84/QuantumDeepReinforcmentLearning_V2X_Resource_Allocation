import matplotlib
matplotlib.use('Agg')  # for server / GPU / no display

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Load data
# -------------------------
df_4q = pd.read_csv("reward_4qubit.csv")
df_4q_5d = pd.read_csv("reward_4qubit_5d.csv")

# -------------------------
# Smoothing
# -------------------------
window = 35

df_4q["Smoothed"] = df_4q["QDRL_4Q_Reward"].rolling(
    window=window, center=True, min_periods=1
).mean()

df_4q_5d["Smoothed"] = df_4q_5d["QDRL_4Q_5D_Reward"].rolling(
    window=window, center=True, min_periods=1
).mean()

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(10, 5))

# Raw curves
plt.plot(
    df_4q["Episode"], df_4q["QDRL_4Q_Reward"],
    color='blue', alpha=0.15, linewidth=1.0, label="4Q Raw"
)

plt.plot(
    df_4q_5d["Episode"], df_4q_5d["QDRL_4Q_5D_Reward"],
    color='red', alpha=0.15, linewidth=1.0, label="4Q + 5D Head Raw"
)

# Smoothed curves
plt.plot(
    df_4q["Episode"], df_4q["Smoothed"],
    color='blue', linewidth=3.0, label="4Q"
)

plt.plot(
    df_4q_5d["Episode"], df_4q_5d["Smoothed"],
    color='red', linewidth=3.0, label="4Q + 5D Head"
)

# Labels and style
plt.xlabel("Episodes")
plt.ylabel("Reward")
#plt.title("4-Qubit QDRL: 4D Head vs 5D Head")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save
plt.savefig("comparison_4q_vs_4q_5d.png", dpi=300, bbox_inches='tight')
print("✅ Figure saved as comparison_4q_vs_4q_5d.png")
