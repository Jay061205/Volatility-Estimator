# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load cleaned price data
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

# Rolling window sizes
windows = [20, 60, 120]

# Compute rolling volatility (annualized)
for window in windows:
    data[f"vol_{window}"] = (
        data["log_return"]
        .rolling(window) # This is sliding window 
        .std()
        * np.sqrt(252)
    )

# Plot rolling volatility
plt.figure(figsize=(12, 6))

plt.plot(data.index, data["vol_20"], label="20-day Volatility")
plt.plot(data.index, data["vol_60"], label="60-day Volatility")
plt.plot(data.index, data["vol_120"], label="120-day Volatility")

plt.title("NIFTY 50 Rolling Volatility (Annualized)")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.grid(True)
plt.show()
