import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
stock_symbol = 'AAPL' # Example: Apple Inc.
start_date = '2026-06-01'
end_date = '2026-06-29'

# Download the data
data = yf.download(stock_symbol, start=start_date, end=end_date)

# Export to CSV
data.to_csv(f'{stock_symbol}_historical_data.csv')
print(f"File saved successfully!")
