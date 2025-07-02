import yfinance as yf
import pandas as pd

tsla = yf.download("TSLA", period="60d", interval="1d")

tsla = tsla[['Close']].reset_index()
tsla.columns = ['Date', 'Close']

tsla.to_csv("../data/tsla_price.csv", index=False)

print("worked")
