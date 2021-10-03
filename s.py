import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Lit Fiannce Dashboard")
tickers = ("^NSEI","^BSESN","^NSEBANK","SBIN.NS","RELIANCE.NS","INFY.NS","RTNINDIA.NS")

dropdown = st.multiselect("Pick your asset",tickers)

start = st.date_input("Start Date",value=pd.to_datetime('2021-01-01'))
end = st.date_input("End Date",value=pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod()-1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    # df=yf.download(dropdown,start,end)['Adj Close']
    df=relativeret(yf.download(dropdown,start,end)['Adj Close'])
    st.line_chart(df)
