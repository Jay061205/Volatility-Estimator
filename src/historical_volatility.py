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
# Suppose if today's price is Pt and yesterday's price is Pt-1
# then the formula is as follows: (Pt - Pt-1)/Pt-1
# Practical example is suppose Pt = 5 and Pt-1 = 4
# According to formula 5-4/4 = 1/4 = 0.25
# if we Multiply this 0.25 with 4, 0.25 * 4 = 1
# and add that to 4, 4+1 = 5
# We get the todays price which is the log_return
# That's the whole explanation that was needed so far

data.dropna(inplace=True) # Removing empty spaces

daily_vol = data['log_return'].std()    # Calculating the standard deviation of the log_return, which is daily volatility
# Standard deviation is a statistical measure showing how spread out data points are from the mean (average) of a dataset.
annual_vol = daily_vol * np.sqrt(252)   # calculating the ann

print(f"Daily Volatility: {daily_vol:.6f}") # Simply printing daily volatility upto 6 decimals
print(f"Annualized Volatility: {annual_vol:.2%}") # Simply printing annualized volatility with 2 decimals and percent symbol
