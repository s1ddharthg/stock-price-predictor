import yfinance as yf
import pandas as pd
from datetime import date, timedelta

def fetch_data(stock_symbol):
    data = yf.download(stock_symbol, start=date.today()-timedelta(days=30), end=date.today())
    if data.empty:
        raise ValueError(f"No data found for symbol '{stock_symbol}'")
    data.to_csv(f'{stock_symbol}_historical_data.csv')