import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
data = pd.read_csv("drl_reward_3500.csv")  # your DRL file

# Moving average function
def moving_avg(x, window=7):
    return x.rolling(window=window, min_periods=1).mean()

# Compute moving average
data["DRL_MA"] = moving_avg(data["DRL_Reward"], window=7)

# Plot
plt.figure(figsize=(10,6))

# Raw curve (faint, optional)
plt.plot(data["Episode"], data["DRL_Reward"],
         linestyle='-', marker='+', alpha=0.3, label="DRL (Raw)")

# Smoothed curve (main)
plt.plot(data["Episode"], data["DRL_MA"],
         linestyle='-', linewidth=2.5, label="DRL (Smoothed)")

# Labels
plt.xlabel("Episodes", fontsize=12)
plt.ylabel("Average Return", fontsize=12)
plt.title("Average Return vs Episodes (DRL)", fontsize=14)

# Grid & legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Save figure
plt.savefig("drl_reward_plot.png", dpi=300, bbox_inches='tight')

# Show plot
plt.show()