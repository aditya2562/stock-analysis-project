import pandas as pd
import yfinance as yf
from src.config import TICKERS, START_DATE, END_DATE, OUTPUT_FILE

def fetch_data():
    df = yf.download(
        tickers=TICKERS,
        start=START_DATE,
        end=END_DATE,
        group_by="ticker",
        auto_adjust=False,
        progress=False
    )

    return df

def reshape_data(df):
    frames = []

    for ticker in TICKERS:
        temp = df[ticker].copy()
        temp['Ticker'] = ticker
        temp.reset_index(inplace = True)
        frames.append(temp)

    final_df = pd.concat(frames, ignore_index=True)

    return final_df

    