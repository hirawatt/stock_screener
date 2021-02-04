import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

## Shown here are the Stock Prices of Google!

""")

# define the ticker tickerSymbol
tickerSymbol = 'NOK'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')
# Open High     Low Close   Volume Dividends     Stock Splits

st.line_chart(tickerDf.Open)
st.line_chart(tickerDf.Volume)
