# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load price data
raw = pd.read_csv("data/nifty50_close.csv")

# Remove metadata rows from yfinance export
data = raw.iloc[2:].copy()
data.columns = ["Date", "Close"]

# Fix datatypes
data["Date"] = pd.to_datetime(data["Date"])
data["Close"] = pd.to_numeric(data["Close"])
data.set_index("Date", inplace=True)

# Compute log returns
data["log_return"] = np.log(data["Close"] / data["Close"].shift(1))
data.dropna(inplace=True)

# EWMA parameter (RiskMetrics standard)
lambda_ = 0.94

# Compute EWMA variance
data["ewma_var"] = data["log_return"].ewm(alpha=1 - lambda_).var()

# Convert variance to volatility and annualize
data["ewma_vol"] = np.sqrt(data["ewma_var"]) * np.sqrt(252)

# Plot EWMA volatility
plt.figure(figsize=(12, 6))
plt.gcf().canvas.manager.set_window_title(
    "NIFTY 50 EWMA Volatility (Annualized)"
)
plt.plot(data.index, data["ewma_vol"], label="EWMA Volatility", color="red")

plt.title("NIFTY 50 EWMA Volatility (Annualized)")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.grid(True)
plt.show()
