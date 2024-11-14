# dashboard.py
import streamlit as st
import data_collection
import indicators
import model_predictions
import backtesting
import pandas as pd

# Dashboard title
st.title("Crypto Analysis Dashboard")

# Sidebar for user inputs
st.sidebar.header("Data Collection")
symbol = st.sidebar.selectbox("Select Cryptocurrency Pair", ["BTCUSDT", "ETHUSDT", "BNBUSDT"])
interval = st.sidebar.selectbox("Select Interval", ["1m", "5m", "15m", "1h", "1d"])

# Fetch historical data
st.header("Historical Data")
df = data_collection.get_data(symbol=symbol, interval=interval, limit=500)
st.write(df.tail())  # Display last few rows of data

# Calculate indicators
st.header("Indicators")
df['SMA_20'] = indicators.calculate_sma(df, window=20)
df['RSI'] = indicators.calculate_rsi(df)
df['MACD'] = indicators.calculate_macd(df)

# Display indicators
st.line_chart(df[['Close', 'SMA_20']])
st.line_chart(df['RSI'])
st.line_chart(df['MACD'])

# Model Predictions
st.header("Model Predictions")
df, model = model_predictions.train_model(df)
st.write(df[['Close', 'Prediction']].tail())

# Run Backtesting
st.header("Backtesting Results")
backtest_results = backtesting.run_backtest(df)
st.write(backtest_results)
