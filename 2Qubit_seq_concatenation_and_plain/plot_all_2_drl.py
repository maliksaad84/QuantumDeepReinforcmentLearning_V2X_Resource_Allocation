import matplotlib
matplotlib.use('Agg')  # for GPU/server

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Load data
# -------------------------
df_drl = pd.read_csv("drl_reward_2500.csv")
df_2q_old = pd.read_csv("reward_2qubit.csv")
df_2q_seq = pd.read_csv("reward_2qubit_sequential_concat.csv")

# -------------------------
# Truncate DRL to 1500 episodes
# -------------------------
df_drl = df_drl[df_drl["Episode"] <= 1500]

# -------------------------
# Smoothing
# -------------------------
window = 35

df_drl["Smoothed"] = df_drl["DRL_Reward"].rolling(
    window=window, center=True, min_periods=1
).mean()

df_2q_old["Smoothed"] = df_2q_old["QDRL_2Q_Reward"].rolling(
    window=window, center=True, min_periods=1
).mean()

df_2q_seq["Smoothed"] = df_2q_seq["QDRL_2Q_SEQ_Reward"].rolling(
    window=window, center=True, min_periods=1
).mean()

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(10, 5))

# Raw curves (light)
plt.plot(df_drl["Episode"], df_drl["DRL_Reward"],
         color='blue', alpha=0.15, linewidth=1.0, label="DRL Raw")

plt.plot(df_2q_old["Episode"], df_2q_old["QDRL_2Q_Reward"],
         color='green', alpha=0.15, linewidth=1.0, label="2Q Reuploading Raw")

plt.plot(df_2q_seq["Episode"], df_2q_seq["QDRL_2Q_SEQ_Reward"],
         color='red', alpha=0.15, linewidth=1.0, label="2Q Seq+Concat Raw")

# Smoothed curves (main)
plt.plot(df_drl["Episode"], df_drl["Smoothed"],
         color='blue', linewidth=3.0, label="DRL")

plt.plot(df_2q_old["Episode"], df_2q_old["Smoothed"],
         color='green', linewidth=3.0, label="2Q Reuploading")

plt.plot(df_2q_seq["Episode"], df_2q_seq["Smoothed"],
         color='red', linewidth=3.0, label="2Q Seq+Concat")

# Labels
plt.xlabel("Episodes")
plt.ylabel("Reward")
#plt.title("DRL vs 2-Qubit QDRL (Reuploading vs Sequential + Concat)")

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save figure
plt.savefig("comparison_drl_vs_2q_all.png", dpi=300, bbox_inches='tight')

print("✅ Figure saved as comparison_drl_vs_2q_all.png")
