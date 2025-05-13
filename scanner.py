import sys
import os
sys.path.append(os.path.dirname(__file__))

import yfinance as yf
import pandas as pd
import ta
from patterns.dual_break import detect_dual_break
from patterns.stair_step import detect_stair_step
from patterns.sideways_hold import detect_sideways_hold
from patterns.triangle_breakout import detect_triangle_breakout

def get_data(ticker, interval="5m", period="2d"):
    df = yf.download(ticker, interval=interval, period=period)
    df.dropna(inplace=True)
    df['VWMA'] = ta.volume.VolumeWeightedAveragePrice(
        high=df['High'], low=df['Low'], close=df['Close'], volume=df['Volume']
    ).volume_weighted_average_price()
    return df

def scan_ticker(ticker):
    df = get_data(ticker)
    signals = {
        "Dual Break": detect_dual_break(df),
        "Stair-Step Flags": detect_stair_step(df),
        "Sideways Hold": detect_sideways_hold(df),
        "Pre-Market Triangle": detect_triangle_breakout(df)
    }
    return {"data": df, "signals": signals}