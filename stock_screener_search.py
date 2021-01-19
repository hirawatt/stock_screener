import yfinance as yf
import streamlit as st
import pandas as pd
import datetime

st.write("""
# Simple Stock Price App
""")

# Selection box
tickerSymbol = st.selectbox("Stock: ",
                     ['GOOGL', 'AAPL', 'AMZN'])

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# write company website
stock_info = tickerData.info
#st.write(stock_info)

st.write("""
## Shown here are the Stock Prices of """, tickerSymbol
)

today = datetime.date.today()
yesterday = today + datetime.timedelta(days=-1)
start_date = st.sidebar.date_input('Start date', yesterday)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')
# slider
# year = st.slider("Select the no. of years", 2000, 2020)
# start_date = str(year) + '-3-30'

# print the level
# format() is used to print value
# of a variable at a specific position
# st.text('Selected: {}'.format(year))

# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start=start_date, end=end_date)
# Open High     Low Close   Volume Dividends     Stock Splits
st.line_chart(tickerDf.Volume)

# radio button
status = st.radio("Select Open or Close: ", ('Open', 'CLose'))

if (status == 'Open'):
    st.success("Open Price")
    st.line_chart(tickerDf.Open)
else:
    st.success("Close Price")
    st.line_chart(tickerDf.Close)
