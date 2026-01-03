# Importing libraries
import yfinance as yf # This is a yahoo finance library which has real-time stock prices
import pandas as pd # Pandas to manage and manipulate data
import matplotlib.pyplot as plt # To plot the graph

symbol = "^NSEI"   # Storing NIFTY 50 stock in symbol as it is listed as "^NSEI" in yfinance 
start_date = "2018-01-01"   # Start date
end_date = None   # till today

data = yf.download(symbol, start=start_date, end=end_date)  # Using yfinance we gather the data with the following info

data = data[['Close']]  # Only choosing the 'close' dataframe/column
data.dropna(inplace=True)   # Remove any empty cells

print(data.head())  # show the first 5 rows of the data
print(data.tail())  # show the last 5 rows of the data

data.to_csv("data/nifty50_close.csv")   # Storing that data in the csv file 

data['Close'].plot(title="NIFTY 50 Close Price") # Plotting a graph of close column of the data and naming a title
plt.xlabel("Years")
plt.ylabel("Prices")
plt.show()  # Showing the graph