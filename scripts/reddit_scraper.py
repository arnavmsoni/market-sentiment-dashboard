import praw
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# variables loading
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# reddit instances
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

#scraping
print(f"Authenticated as: {reddit.user.me()}")

subreddits = ["wallstreetbets", "stocks", "investing", "options"]
search_query = "TSLA"
limit_per_subreddit = 50  # number of posts per subreddit

posts = []

for sub in subreddits:
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.search(search_query, sort="new", limit=limit_per_subreddit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "created_utc": datetime.fromtimestamp(submission.created_utc),
            "score": submission.score,
            "url": submission.url,
            "num_comments": submission.num_comments,
            "subreddit": sub
        })

# saving data
df = pd.DataFrame(posts)
df.to_csv("../data/tsla_reddit_posts.csv", index=False)
print(f"✅ Scraped {len(df)} TSLA posts")
