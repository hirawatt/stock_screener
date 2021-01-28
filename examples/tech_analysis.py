import yfinance as yf
import ta
import pandas as pd
import matplotlib.pyplot as plt

power = yf.Ticker("POWERGRID.NS")
df = power.history(start="2020-01-01", end='2020-09-04')
df.head()

# Simple Moving Average
df['MA'] = ta.trend.SMAIndicator(df['Close'], 20)
df[['Close','MA']].plot(figsize=(12,12))
plt.show()

# Exponential Moving Average
df['EMA'] = ta.trend.EMAIndicator(df['Close'], 20)
df[['Close','EMA']].plot(figsize=(12,10))
plt.show()
'''
# Average Directional Movement Index(Momentum Indicator)
df['avg'] = ta.trend.ADXIndicator(df['High'],df['Low'], df['Close'], 20)
df[['avg']].plot(figsize=(12,10))

# Bollinger Bands
df['up_band'], df['mid_band'], df['low_band'] = ta.BBANDS(df['Close'], timeperiod =20)
df[['Close','up_band','mid_band','low_band']].plot(figsize=(12,10))
plt.show()
'''
# Relative Strength index (RSI)
df['Relative'] = ta.momentum.rsi(df['Close'], 14)
df['Relative'].plot(figsize=(12,10))
plt.show()

#
