# Market Data Sentiment Dashboard

 **[Check out the site](https://market-sentiment-dashboard-feeyuxwytyszxd5wvbaypm.streamlit.app)**

---

## About This Project

I built this dashboard to see if **Reddit sentiment about Tesla (TSLA) actually lines up with its stock price movements**. I was curious about how people talking about Tesla on Reddit might connect to what’s happening in the market, so I used this project to explore that and to get better at **Python, APIs, and data visualization**.

The dashboard scrapes Reddit posts about Tesla, runs sentiment analysis on them, pulls Tesla’s stock price data, and then visualizes it all so it’s easy to see how sentiment and price move over time. It also shows the top positive and negative posts for context, and calculates how closely sentiment and price changes are correlated.

This was a great way for me to combine **my interest in investing and coding while learning how to deploy a project people can actually use online**.

---

## What It Does

Scrapes posts from subreddits like `r/wallstreetbets` and `r/stocks` that mention Tesla or TSLA.  
Uses VADER sentiment analysis to score how positive or negative those posts are.  
Pulls recent TSLA price data.  
Shows an interactive chart with price and sentiment together.  
Calculates correlation between Reddit sentiment and Tesla’s price changes.  
Lists the top positive and negative Reddit posts.  
Fully deployed and easy to share with friends, on my resume, or on LinkedIn.

---

## Why I Made It

I wanted to:
- Practice using APIs and working with real-world data.
- Build something I could share on my resume and show to potential employers.
- Learn how to deploy an app so it’s actually live, not just on my computer.
- See if Reddit sentiment actually connects to stock price moves.

---

## Tech I Used

- **Python (pandas, requests, praw, yfinance)**
- **NLTK (VADER for sentiment)**
- **Plotly for interactive charts**
- **Streamlit for the dashboard**
- **Streamlit Cloud for deployment**
- **Git and GitHub for version control**

---

## How It Works

**Scraping Reddit:** Uses PRAW to grab recent posts about Tesla from selected subreddits.  
**Sentiment Analysis:** Runs VADER sentiment analysis on the titles of those posts.  
**Price Data:** Gets Tesla’s stock prices using yfinance.  
**Processing:** Combines sentiment data and price data by day to see if they move together.  
**Visualization:** Displays all of this on an interactive dashboard where you can explore the data.

---

## Repository Structure
- data: raw and processed data
- notebooks: analysis and testing
- scripts: scraping, sentiment, analysis scripts
- dashboard: Streamlit dashboard files
