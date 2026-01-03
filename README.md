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