import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

class SentimentAnalyzer:
    def __init__(self, input_csv_path, output_csv_path):
        self.input_csv_path = input_csv_path
        self.output_csv_path = output_csv_path
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_csv_path)
        print(f"✅ Loaded data with {len(self.df)} rows from {self.input_csv_path}")

    def filter_tsla_posts(self):
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        # Filter for 'TSLA' or 'Tesla' in title, case-insensitive
        self.df = self.df[
            self.df['title'].str.contains('TSLA', case=False, na=False) |
            self.df['title'].str.contains('Tesla', case=False, na=False)
        ]
        print(f"✅ Filtered to {len(self.df)} posts containing 'TSLA' or 'Tesla' in the title.")

    def compute_sentiment(self):
        if self.df is None:
            raise ValueError("Data not loaded or filtered.")
        # Run sentiment analysis on *title only* for clarity
        self.df['title_clean'] = self.df['title'].fillna('')
        sentiment_scores = self.df['title_clean'].apply(lambda text: self.sia.polarity_scores(text))
        self.df['compound'] = sentiment_scores.apply(lambda x: x['compound'])
        self.df['pos'] = sentiment_scores.apply(lambda x: x['pos'])
        self.df['neu'] = sentiment_scores.apply(lambda x: x['neu'])
        self.df['neg'] = sentiment_scores.apply(lambda x: x['neg'])
        print("✅ Sentiment scoring completed on titles.")

    def save_results(self):
        if self.df is None:
            raise ValueError("Data not loaded or sentiment not computed.")
        self.df.to_csv(self.output_csv_path, index=False)
        print(f"✅ Results saved to {self.output_csv_path}")

if __name__ == "__main__":
    analyzer = SentimentAnalyzer(
        input_csv_path="../data/tsla_reddit_posts.csv",
        output_csv_path="../data/tsla_reddit_sentiment.csv"
    )
    analyzer.load_data()
    analyzer.filter_tsla_posts()
    analyzer.compute_sentiment()
    analyzer.save_results()
