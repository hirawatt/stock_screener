import yfinance as yf
import streamlit as st
import pandas as pd
import datetime
from scripts.Download_BhavCopy import download_nsecm_bhavcopy
import os

st.title('Simple Stock Price App')

# Selection box
tickerSymbol = st.selectbox("Stock: ",
                     ['GOOGL', 'AAPL', 'AMZN'])

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# write company website
stock_info = tickerData.info
#st.write(stock_info)

st.header('Stock Prices of')

today = datetime.date.today()
yesterday = today + datetime.timedelta(days=-1)
random = datetime.datetime(2010, 10, 10)
start_date = st.sidebar.date_input('Start date', random)
end_date = st.sidebar.date_input('End date', today)

select_date = st.sidebar.date_input('Select Date', today)

if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

pwd = os.getcwd()
bhavcopyfile = download_nsecm_bhavcopy(select_date)
st.success(select_date)
bc_file = pwd + bhavcopyfile
print(pwd)

#sp_500_sectors = [IT, Materials, Utilities, Communication Services, Financial, Healthcare, Industrials, Energy, Consumer Staples, Consumer Discretionary]
#chart_data = [Symbol, Company Age, Sector, ]

def stock_data(nrows):
    data = pd.read_csv(bc_file, nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 200 rows of data into the dataframe.
data = load_data(200)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

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
st.subheader('Volume of Stock')
st.line_chart(tickerDf.Volume)

# radio button
status = st.radio("Select Open or Close: ", ('Close', 'Open'))

if (status == 'Open'):
    st.success("Open Price")
    st.line_chart(tickerDf.Open)
else:
    st.success("Close Price")
    st.line_chart(tickerDf.Close)
