import streamlit as st
import yfinance as finance
import random

st.title("Stock Market Monitoring App")
st.header("A web application to monitor random stock price")


def get_ticker(name):
    company = finance.Ticker(name)
    return company
 
#Randomly select two stock symbols
symbols = ["AAPL", "GOOGL", "AMZN", "FB", "TSLA"]
symbol1 = random.choice(symbols)
symbol2 = random.choice(symbols)
company1 = get_ticker(symbol1)
company2 = get_ticker(symbol2)
 
# fetches the data: Open, Close, High, Low and Volume
data1 = company1.history(period="3mo")
data2 = company2.history(period="3mo")
 
 
# markdown syntax
st.write(f"### {symbol1}")
st.write(company1.info['longBusinessSummary'])
st.write(data1)
 
# plots the graph
st.line_chart(data1.values)
 
st.write(f"### {symbol2}")
st.write(company2.info['longBusinessSummary'])
st.write(data2)

st.line_chart(data2.values)