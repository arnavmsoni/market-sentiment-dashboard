import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("TSLA Reddit Sentiment Dashboard with Price Correlation")

# Loading sentiment data
df_sentiment = pd.read_csv("data/tsla_reddit_sentiment.csv")
df_sentiment['created_utc'] = pd.to_datetime(df_sentiment['created_utc'])
sentiment_daily = df_sentiment[['created_utc', 'compound']].copy()
sentiment_daily = sentiment_daily.set_index('created_utc').resample('D').mean().dropna().reset_index()

# Loading price data
df_price = pd.read_csv("data/tsla_price.csv")
df_price['Date'] = pd.to_datetime(df_price['Date'])


df_merged = pd.merge(sentiment_daily, df_price, left_on='created_utc', right_on='Date')
df_merged['Price_Change_%'] = df_merged['Close'].pct_change() * 100

#Graph
st.subheader("Sentiment vs. Price Over Time (Dual Axis)")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df_merged['Date'],
        y=df_merged['Close'],
        name="TSLA Close Price",
        yaxis="y1",
        line=dict(color='deepskyblue')
    )
)

fig.add_trace(
    go.Scatter(
        x=df_merged['Date'],
        y=df_merged['compound'],
        name="Sentiment (compound)",
        yaxis="y2",
        line=dict(color='orange')
    )
)

fig.update_layout(
    yaxis=dict(
        title="TSLA Close Price",
        side="left"
    ),
    yaxis2=dict(
        title="Sentiment (compound)",
        overlaying="y",
        side="right"
    ),
    xaxis_title="Date",
    legend=dict(x=0.01, y=0.99),
    height=500,
    margin=dict(l=40, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)

# top posts section
st.subheader("Top Positive Posts")
top_pos = df_sentiment.sort_values('compound', ascending=False).head(5)
st.write(top_pos[['created_utc', 'title', 'compound', 'url']])

st.subheader("Top Negative Posts")
top_neg = df_sentiment.sort_values('compound').head(5)
st.write(top_neg[['created_utc', 'title', 'compound', 'url']])

st.caption("Built with Reddit + VADER sentiment, yfinance price data, and Streamlit with Plotly for dual-axis analysis.")
