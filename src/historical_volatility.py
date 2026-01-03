# Importing Libraries
import pandas as pd     #Importing Pandas
import numpy as np      #Importing Numpy

raw = pd.read_csv("data/nifty50_close.csv")     # reading the csv file that is created 
print(raw.head(5))  # Printing the first 5 rows from the csv data file, just to be sure :)

data = raw.iloc[2:].copy()      # iloc: To remove metadata rows added by yfinance export
data.columns = ["Date", "Close"]    # Make sure date and close columns exist and if not make one

data["Date"] = pd.to_datetime(data["Date"]) # Convert the date column into actual pandas datetime to operate efficiently
data["Close"] = pd.to_numeric(data["Close"]) # Convert Close column in pure numeric form
data.set_index("Date", inplace=True)    # Choosing Date as the main index and removing the empty cells

print(data.head())  # Printing first 5 columns again to be sure
print(data.dtypes)  # As we converted the types, this makes sure that it is successfully converted into desired datatype

# Compute log returns
data['log_return'] = np.log(data['Close'] / data['Close'].shift(1)) 
# The above mathematical logic is necessary to understand so below is a good practical explanation
# Log returns are calculated as ln(Pt / Pt-1), where:
# Pt   = today's closing price
# Pt-1 = yesterday's closing price
#
# Log returns are preferred because:
# - they are additive over time
# - they behave better statistically
# - they are standard in volatility calculations
#
# For small price changes, log returns are approximately equal to simple returns.


data.dropna(inplace=True) # Removing empty spaces

daily_vol = data['log_return'].std()    # Calculating the standard deviation of the log_return, which is daily volatility
# Standard deviation is a statistical measure showing how spread out data points are from the mean (average) of a dataset.
annual_vol = daily_vol * np.sqrt(252)   # This needs a good explanation (refer below comments)
# Annualized volatility is obtained by scaling daily volatility
# by the square root of the number of trading days.
#
# This follows from the statistical rule that variances add over time,
# and volatility is the square root of variance.
#
# 252 is used as an approximation for the number of trading days in a year.


print(f"Daily Volatility: {daily_vol:.6f}") # Simply printing daily volatility upto 6 decimals
print(f"Annualized Volatility: {annual_vol:.2%}") # Simply printing annualized volatility with 2 decimals and percent symbol
