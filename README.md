# Stock Price Predictor

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white)](https://predictstockprices.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![yfinance](https://img.shields.io/badge/yfinance-Yahoo!-400090?style=flat-square&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

An end-to-end Machine Learning web application built with Streamlit that predicts the next day's stock price using historical market data. The prediction engine uses Support Vector Regression (SVR) trained on the last 30 days of historical stock closing prices fetched directly from Yahoo Finance.

The live application is deployed and available at: https://predictstockprices.streamlit.app/

## Workflow

1. **User Input**: The user enters a stock ticker symbol (e.g., AAPL, MSFT, TSLA) into the Streamlit user interface.
2. **Data Acquisition**: The application uses the `data_fetch` module to download 30 days of historical daily market data from the Yahoo Finance API via `yfinance`.
3. **Model Processing**: The `model` module processes the downloaded CSV file, builds a Support Vector Regression (SVR) model with a Radial Basis Function (RBF) kernel, fits it onto the historical close prices, and calculates the prediction for the next trading day.
4. **Display**: The predicted stock price is presented to the user, and temporary data files are cleaned up from the server storage.

## Repository Structure

- `app.py`: The Streamlit web interface containing layout configuration, text fields, status spinners, and clean error alert handling.
- `data_fetch.py`: Downloads historical market data from the yfinance API, executes basic validation to ensure the ticker is valid, and handles file writes.
- `model.py`: Parses historical close prices, manages data formatting, initializes SVR, runs the regression fit, and computes the prediction scalar.
- `requirements.txt`: Project dependencies and version specifications.
- `.gitignore`: Specifies files and folders for Git to ignore (e.g., virtual environments, local CSV files, and caches).

## Installation and Execution

To run this application locally, follow these steps:

### Prerequisites

Ensure you have Python installed (version 3.9 or higher is recommended).

### Setup Virtual Environment

Create and activate a virtual environment to manage dependencies cleanly:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Run Streamlit App

Launch the local development server:

```bash
streamlit run app.py
```

The application will automatically open in your default browser at `http://localhost:8501`.

## Machine Learning Details

The forecasting engine uses Support Vector Regression (SVR) with the following parameters:
- **Kernel**: Radial Basis Function (RBF)
- **C (Penalty Parameter)**: 1e3
- **Gamma**: 0.1

The SVR model is fit to the time indices mapping to closing prices. It performs regression over the historical time window to project the close price for the subsequent trading date.

## License

This project is licensed under the MIT License. See the LICENSE file for details.