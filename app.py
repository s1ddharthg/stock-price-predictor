import streamlit as st
import data_fetch
import model
import importlib
import os

importlib.reload(data_fetch)
importlib.reload(model)

from data_fetch import fetch_data
from model import run_prediction

st.set_page_config(
    page_title="Stock Price Predictor",
    page_icon="📈",
    layout="wide"
)

st.write("")
st.write("")

left, center, right = st.columns([1, 2, 1])

with center:

    st.markdown(
        "<h1 style='text-align: center;'>📈 Stock Price Predictor</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center;'>Predict future stock prices using market data. Visit <a href='https://finance.yahoo.com/' target='_blank'>Yahoo Finance</a> for more info</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    with st.container(border=True):

        st.subheader("Enter Stock Details")

        stock_input = st.text_input(
            "Stock Symbol",
            placeholder="AAPL, TSLA, MSFT..."
        )

        st.write("")
        predict_btn = st.button(
            "Predict Price",
            use_container_width=True
        )

    if predict_btn:
        if stock_input.strip():
            stock_input = stock_input.upper()
            csv_file = f"{stock_input}_historical_data.csv"

            with st.spinner("Fetching data and running prediction..."):
                try:
                    fetch_data(stock_input)
                    prediction = run_prediction(csv_file)

                    st.write("")
                    st.metric(
                        label=f"{stock_input} Predicted Price",
                        value=f"${prediction:.2f}"
                    )
                    st.success("Prediction completed successfully.")

                    if os.path.exists(csv_file):
                        os.remove(csv_file)

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a stock symbol.")