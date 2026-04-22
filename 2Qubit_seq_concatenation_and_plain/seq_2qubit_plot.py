import matplotlib
matplotlib.use('Agg')  # IMPORTANT for server / no display

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("reward_2qubit_sequential_concat.csv")

# Smoothing
df["Smoothed"] = df["QDRL_2Q_SEQ_Reward"].rolling(
    window=35, center=True, min_periods=1
).mean()

# Plot
plt.figure(figsize=(10, 5))

plt.plot(df["Episode"], df["QDRL_2Q_SEQ_Reward"], 
         alpha=0.3, linewidth=1.2, label="Raw Reward")

plt.plot(df["Episode"], df["Smoothed"], 
         linewidth=2.8, label="Smoothed Reward")

plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.title("QDRL 2-Qubit Sequential Encoding + Concatenated Measurements")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

# ✅ Save instead of show
plt.savefig("qdrl_2q_seq_plot.png", dpi=300, bbox_inches='tight')

print("✅ Figure saved as qdrl_2q_seq_plot.png")