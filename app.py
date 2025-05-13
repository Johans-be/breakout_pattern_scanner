import streamlit as st
from scanner import scan_ticker
import plotly.graph_objs as go

st.set_page_config(layout="wide")
st.title("🚀 Breakout Pattern Scanner")

ticker = st.text_input("Enter Stock Ticker", value="ASST").upper()
if ticker:
    result = scan_ticker(ticker)
    df = result['data']
    signals = result['signals']

    st.subheader(f"📊 Pattern Signals for {ticker}")
    for signal, val in signals.items():
        st.write(f"{signal}: {'✅' if val else '❌'}")

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index, open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'], name='Price'))
    fig.add_trace(go.Scatter(x=df.index, y=df['VWMA'], line=dict(color='orange'), name='VWMA'))
    st.plotly_chart(fig, use_container_width=True)