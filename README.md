# Volatility-Estimator
This project builds a volatility estimator for the NIFTY 50 index using historical price data. It computes daily log returns and estimates historical volatility to quantify market risk. The focus is on measuring risk dynamics rather than predicting prices or generating trading signals.

Annualizing Volatility

In this project, volatility is first computed at a daily frequency using log returns. Since financial risk is commonly expressed on an annual basis, daily volatility is scaled to obtain an annualized measure.

Daily Volatility

Daily volatility is defined as the standard deviation of daily log returns:

𝜎
daily
=
1
𝑛
−
1
∑
𝑡
=
1
𝑛
(
𝑟
𝑡
−
𝑟
ˉ
)
2
σ
daily
	​

=
n−1
1
	​

t=1
∑
n
	​

(r
t
	​

−
r
ˉ
)
2
	​


where:

𝑟
𝑡
r
t
	​

 represents the daily log return

𝑟
ˉ
r
ˉ
 is the mean of daily returns

𝑛
n is the total number of observations

Annual Volatility

To obtain annual volatility, we use the statistical property that variances of independent returns add linearly over time. For 
𝑁
N trading days in a year:

Var
annual
=
𝑁
⋅
𝜎
daily
2
Var
annual
	​

=N⋅σ
daily
2
	​


Since volatility is the square root of variance, annual volatility is given by:

𝜎
annual
=
𝜎
daily
⋅
𝑁
σ
annual
	​

=σ
daily
	​

⋅
N
	​


In practice, the number of trading days in a year is approximated as 252, leading to:

annual_volatility = daily_volatility * sqrt(252)


This transformation converts daily risk into a comparable annualized metric while preserving the statistical properties of return variability.