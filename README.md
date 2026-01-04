# Volatility-Estimator

## Overview

This project builds a **volatility estimator** for the **NIFTY 50** index using historical price data. It focuses on measuring and comparing different volatility estimation methods to understand how market risk evolves over time. The goal is **risk analysis**, not price prediction or trading signal generation.

---

## Features

- Historical volatility computation using log returns
- Rolling volatility estimation (20, 60, 120 days)
- EWMA (Exponentially Weighted Moving Average) volatility
- Visual comparison of volatility models
- Event-based analysis using the COVID-19 market shock
- Clean, reproducible Python scripts

---

## Project Structure

```
Volatility_Estimator/
├── src/
│   ├── data_loader.py
│   ├── historical_volatility.py
│   ├── rolling_volatility.py
│   ├── ewma_volatility.py
│   └── compare_volatility.py
├── .gitignore
├── README.md
└── env/
```

---

## Project Index

- **Data Collection** – Fetches NIFTY 50 historical price data
- **Return Calculation** – Computes daily log returns
- **Historical Volatility** – Single-period volatility estimate
- **Rolling Volatility** – Time-varying volatility using fixed windows
- **EWMA Volatility** – Adaptive volatility with exponential weighting
- **Comparison & Visualization** – Side-by-side analysis of methods

---

## Methodology

### Annualizing Volatility

Volatility is first computed at a **daily frequency** using log returns. Since financial risk is commonly expressed on an **annual basis**, daily volatility is scaled accordingly.

#### Daily Volatility

Daily volatility is defined as the standard deviation of daily log returns:

$$
\sigma_{daily} = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} (r_t - \bar{r})^2}
$$

Where:
- $r_t$ is the daily log return
- $\bar{r}$ is the mean of daily returns
- $n$ is the number of observations

#### Annual Volatility

Assuming independent daily returns, variances add linearly over time:

$$
Var_{annual} = N \cdot \sigma_{daily}^2
$$

Taking the square root gives annualized volatility:

$$
\sigma_{annual} = \sigma_{daily} \cdot \sqrt{N}
$$

In practice, $N$ is approximated as **252 trading days**:

```python
annual_volatility = daily_volatility * sqrt(252)
```

---

## Rolling Volatility

Rolling volatility measures how market risk **changes over time** by computing volatility over a sliding window of recent returns.

### Rolling Window Setup

```python
windows = [20, 60, 120]
```

- **20 days** ≈ one trading month
- **60 days** ≈ one quarter
- **120 days** ≈ half a year

Each window answers:
> *How volatile has the market been recently over this time horizon?*

### Computation

```python
for window in windows:
    data[f"vol_{window}"] = (
        data["log_return"].rolling(window).std() * np.sqrt(252)
    )
```

Mathematically:

$$
\sigma_{roll,t} = \text{std}(r_{t-w+1}, \dots, r_t) \times \sqrt{252}
$$

### Interpretation

- **Short windows (20 days):** Highly reactive but noisy
- **Long windows (120 days):** Smoother but slower to respond
- Helps identify **volatility regimes** and market stress periods

---

## EWMA Volatility

EWMA volatility assigns **higher weight to recent returns** and exponentially decreasing weight to older observations. This allows volatility to react faster to sudden shocks while retaining memory of past behavior.

A decay factor $\lambda = 0.94$ is used (RiskMetrics standard).

---

## Event Analysis

A vertical marker is added to highlight the **COVID-19 market shock (April 15, 2020)**. This visualizes how different volatility models respond to extreme market stress.

---

## Key Observations

- EWMA volatility closely tracks short-term rolling volatility but reacts and decays faster during shocks
- Rolling 20-day volatility is highly reactive but discards past information abruptly
- Rolling 60-day volatility smooths noise but lags during regime changes
- Volatility clusters during periods of market stress

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/Jay061205/Volatility-Estimator.git
cd Volatility-Estimator
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Usage

Run individual scripts from the `src` directory:

```bash
python src/data_loader.py
python src/historical_volatility.py
python src/rolling_volatility.py
python src/ewma_volatility.py
python src/compare_volatility.py
```

---

## Roadmap

- Add realized volatility comparisons
- Experiment with different EWMA decay factors
- Extend analysis to other indices or asset classes
- Build an interactive dashboard

---

## Contribution

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project with proper attribution.

---

## Acknowledgements

- Yahoo Finance for historical data
- Pandas, NumPy, and Matplotlib for data analysis and visualization

