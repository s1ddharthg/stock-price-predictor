import streamlit as st
import data_fetch
import model
import importlib
importlib.reload(data_fetch)
importlib.reload(model)
from data_fetch import fetch_data
from model import run_prediction

st.title("Stock Price Predictor")

stock_input = st.text_input("Enter Stock Symbol")

if st.button("Predict"):
    if stock_input.strip():
        csv_file = f"{stock_input}_historical_data.csv"
        try:
            fetch_data(stock_input)
            prediction = run_prediction(csv_file)
            st.success(f"Predicted price for {stock_input}: ${prediction:.2f}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a stock symbol.")