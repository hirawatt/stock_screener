import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

import os

pwd = os.getcwd()

DATA_URL = ("/home/vh/Desktop/finance/personal_fin/scripts/marketsdata/nsecm_20210104_bhavcopy.csv")
#DATA_UR= ("C:/Users/Divya/losers.csv")
df=pd.read_csv(DATA_URL)
#df1=pd.read_csv(DATA_UR)

st.title("Share Price analysis for May 2019 to May 2020:")
st.sidebar.title("Share Price analysis for May 2019 to May 2020:")
st.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")
st.sidebar.markdown("This application is a Share Price dashboard for Top 5 Gainers and Losers:")

st.sidebar.title("Gainers")
select = st.sidebar.selectbox('Symbol', ['Adani Green Energy', 'GMM Pfaudler', 'AGC Networks', 'Alkyl Amines Chem', 'IOL Chem & Pharma'], key='1')

if not st.sidebar.checkbox("Hide", True, key='1'):
    st.title("Gainers")
    if select == 'Adani Green Energy':
        for i in ['LOW', 'HIGH', 'CLOSE', 'OPEN']:
            df[i] = df[i].astype('float64')
            avg_20 = df.CLOSE.rolling(window=20, min_periods=1).mean()
            avg_50 = df.CLOSE.rolling(window=50, min_periods=1).mean()
            avg_200 = df.CLOSE.rolling(window=200, min_periods=1).mean()
            set1 = { 'x': df.TIMESTAMP, 'open': df.OPEN, 'close': df.CLOSE, 'high': df.HIGH, 'low': df.LOW, 'type': 'candlestick',}
            set2 = { 'x': df.TIMESTAMP, 'y': avg_20, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'blue' },'name': 'MA 20 periods'}
            set3 = { 'x': df.TIMESTAMP, 'y': avg_50, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'yellow' },'name': 'MA 50 periods'}
            set4 = { 'x': df.TIMESTAMP, 'y': avg_200, 'type': 'scatter', 'mode': 'lines', 'line': { 'width': 1, 'color': 'black' },'name': 'MA 200 periods'}
            data = [set1, set2, set3, set4]
            fig = go.Figure(data=data)
            st.plotly_chart(fig)
