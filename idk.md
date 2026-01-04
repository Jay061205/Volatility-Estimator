# Volatility-Estimator

This project builds a volatility estimator for the NIFTY 50 index using historical price data. It computes daily log returns and estimates historical volatility to quantify market risk. The focus is on measuring risk dynamics rather than predicting prices or generating trading signals.

## Methodology

### Annualizing Volatility

In this project, volatility is first computed at a daily frequency using log returns. Since financial risk is commonly expressed on an annual basis, daily volatility is scaled to obtain an annualized measure.

### 1. Daily Volatility

Daily volatility is defined as the standard deviation of daily log returns:

$$
\sigma_{daily} = \sqrt{\frac{1}{n-1} \sum_{t=1}^{n} (r_t - \bar{r})^2}
$$

**Where:**
* $r_t$ represents the daily log return
* $\bar{r}$ is the mean of daily returns
* $n$ is the total number of observations

### 2. Annual Volatility

To obtain annual volatility, we use the statistical property that variances of independent returns add linearly over time. For $N$ trading days in a year:

$$
Var_{annual} = N \cdot \sigma_{daily}^2
$$

Since volatility is the square root of variance, annual volatility is given by:

$$
\sigma_{annual} = \sigma_{daily} \cdot \sqrt{N}
$$

In practice, the number of trading days in a year is approximated as **252**, leading to:

```python
annual_volatility = daily_volatility * sqrt(252)
```

## Rolling Volatility

Rolling volatility measures how market risk changes over time by computing volatility over a sliding window of recent returns instead of using the entire dataset.

### Rolling Window Setup

We define specific window sizes to capture different time horizons:

```python
windows = [20, 60, 120]
```
20 days $\approx$ one trading month60 days $\approx$ one quarter120 days $\approx$ half a yearEach window answers the question: “How volatile has the market been recently over this specific period?”

# Computing Rolling Volatility

The rolling volatility is computed by iterating through the defined windows:
```python
for window in windows:
    data[f"vol_{window}"] = (
        data["log_return"]
        .rolling(window)
        .std()
        * np.sqrt(252)
    )
```

Breakdown of the Calculation:
1. data["log_return"]: Selects the daily log return series.

2. .rolling(window): Creates a sliding window of size $w$ that moves forward one day at a time.

3. .std(): Computes the standard deviation of log returns within each window.

4. * np.sqrt(252): Annualizes the rolling daily volatility.

Mathematically, the annualized rolling volatility $\sigma_{roll}$ for a window size $w$ at time $t$ is:
$$
\sigma_{\text{roll}, t} = \text{std}(r_{t-w+1}, \dots, r_t) \times \sqrt{252}
$$

### Output & Interpretation

The script generates a new column for each window:
* `vol_20`
* `vol_60`
* `vol_120`

Each column contains an annualized volatility value for every date, based only on the most recent observations.

* **Shorter windows ($N=20$):** Respond quickly to market shocks but are noisier.
* **Longer windows ($N=120$):** Respond more slowly but provide smoother volatility trends.
* **Risk Regimes:** This approach helps identify periods of high stress versus calm that a single static volatility number cannot capture.