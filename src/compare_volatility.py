# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load price data
raw = pd.read_csv("data/nifty50_close.csv")

# Clean yfinance metadata
data = raw.iloc[2:].copy()
data.columns = ["Date", "Close"]

data["Date"] = pd.to_datetime(data["Date"])
data["Close"] = pd.to_numeric(data["Close"])
data.set_index("Date", inplace=True)

# Compute log returns
data["log_return"] = np.log(data["Close"] / data["Close"].shift(1))
data.dropna(inplace=True)

# Rolling volatility (annualized)
data["vol_20"] = data["log_return"].rolling(20).std() * np.sqrt(252)
data["vol_60"] = data["log_return"].rolling(60).std() * np.sqrt(252)

# EWMA volatility
lambda_ = 0.94
data["ewma_vol"] = (
    np.sqrt(data["log_return"].ewm(alpha=1 - lambda_).var())
    * np.sqrt(252)
)

event_date = pd.to_datetime("2020-04-15")

# Plot comparison
plt.figure(figsize=(12, 6))
plt.gcf().canvas.manager.set_window_title(
    "NIFTY 50 Volatility Comparison"
)

plt.plot(data.index, data["vol_20"], label="Rolling 20-day Volatility", alpha=0.8)
plt.plot(data.index, data["vol_60"], label="Rolling 60-day Volatility", alpha=0.8)
plt.plot(data.index, data["ewma_vol"], label="EWMA Volatility (λ = 0.94)", linewidth=2)

# Mark COVID crash
plt.axvline(
    event_date,
    color="black",
    linestyle="--",
    linewidth=1,
    alpha=0.8,
    label="COVID Crash (April 15, 2020)"
)


plt.title("NIFTY 50 Volatility Comparison")
plt.xlabel("Date")
plt.ylabel("Annualized Volatility")
plt.legend()
plt.grid(True)
plt.show()
