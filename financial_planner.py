import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Set Streamlit app title
st.title("🚀 AI-Based Financial Planner 📈")

# Sidebar for user input
st.sidebar.header("Investment Preferences")
ticker = st.sidebar.text_input("Enter Stock Ticker Symbol (e.g., AAPL, TSLA, AMZN):", "AAPL")
horizon = st.sidebar.selectbox("Select Investment Horizon", ["Short Term (1M)", "Mid Term (6M)", "Long Term (1Y)"])
risk_tolerance = st.sidebar.slider("Select Your Risk Tolerance (1: Low, 5: High)", 1, 5, 3)

# Fetch stock data
def get_stock_data(ticker):
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=365 * 2)).strftime("%Y-%m-%d")
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Train a simple ML model for prediction
def predict_stock_price(stock_data, horizon_days):
    stock_data["Date"] = stock_data.index
    stock_data["Days"] = (stock_data["Date"] - stock_data["Date"].min()).dt.days
    X = stock_data["Days"].values.reshape(-1, 1)
    y = stock_data["Close"].values

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array([X[-1][0] + i for i in range(1, horizon_days + 1)]).reshape(-1, 1)
    predictions = model.predict(future_days)
    
    return predictions, future_days

# Get stock data
stock_data = get_stock_data(ticker)

# Define forecast period
if horizon == "Short Term (1M)":
    forecast_days = 30
elif horizon == "Mid Term (6M)":
    forecast_days = 180
else:
    forecast_days = 365

# Display stock summary
if not stock_data.empty:
    st.subheader(f"📊 {ticker} Stock Summary")
    
    stock = yf.Ticker(ticker)
    info = stock.info

    company_name = info.get("longName", "N/A")
    industry = info.get("industry", "N/A")
    market_cap = info.get("marketCap", "N/A")

    # Display company details
    st.write(f"**Company Name:** {company_name}")
    st.write(f"**Industry:** {industry}")

    col1, col2 = st.columns(2)
    col1.metric("Market Cap", f"${market_cap:,}" if market_cap != "N/A" else "N/A")
    col2.metric("Current Price", f"${info.get('currentPrice', 'N/A')}")

    col1.metric("52-Week High", f"${info.get('fiftyTwoWeekHigh', 'N/A')}")
    col2.metric("52-Week Low", f"${info.get('fiftyTwoWeekLow', 'N/A')}")


    # Generate predictions
    predictions, future_days = predict_stock_price(stock_data, forecast_days)

    # 📌 **Plot 1: Historical & Predicted Prices**
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(stock_data.index, stock_data["Close"], label="Historical Price", color="blue")
    ax1.plot([stock_data.index[-1] + timedelta(days=i) for i in range(1, forecast_days + 1)], 
             predictions, label="Predicted Price", color="red", linestyle="dashed")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Stock Price (USD)")
    ax1.legend()
    st.pyplot(fig1)

    # 📌 **Plot 2: Moving Averages (SMA & EMA)**
    stock_data["SMA50"] = stock_data["Close"].rolling(window=50).mean()
    stock_data["EMA20"] = stock_data["Close"].ewm(span=20, adjust=False).mean()
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(stock_data.index, stock_data["Close"], label="Closing Price", color="blue")
    ax2.plot(stock_data.index, stock_data["SMA50"], label="50-Day SMA", color="green", linestyle="dashed")
    ax2.plot(stock_data.index, stock_data["EMA20"], label="20-Day EMA", color="purple", linestyle="dashed")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Stock Price (USD)")
    ax2.legend()
    st.pyplot(fig2)

    # 📌 **Plot 3: Volatility Analysis**
    stock_data["Daily Return"] = stock_data["Close"].pct_change()
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.plot(stock_data.index, stock_data["Daily Return"], label="Daily Return", color="orange")
    ax3.axhline(0, color="black", linestyle="dashed", linewidth=0.8)
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Daily Return (%)")
    ax3.legend()
    st.pyplot(fig3)

    # Display investment advice
    st.subheader("💡 Investment Recommendation:")
    if risk_tolerance <= 2:
        advice = "🔹 **Low-risk:** Consider stable investments like ETFs or bonds."
    elif risk_tolerance <= 4:
        advice = "🔹 **Moderate-risk:** A balanced portfolio of growth and value stocks."
    else:
        advice = "🔹 **High-risk:** High-growth stocks with potential volatility."
    
    st.write(advice)
else:
    st.error("Stock data not found. Please enter a valid ticker symbol.")
