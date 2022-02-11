# Code to scrape tweets that does not need the Twitter API
# I ran this in powershell with file path set to folder location of scrape.py
# ran with cmd python .\scrape.py

import snscrape.modules.twitter as twitterScraper
import pandas as pd

scraper = twitterScraper.TwitterHashtagScraper("TacoBell")

tweets = []

for i, tweet in enumerate(scraper.get_items()):
    if i > 70000:
        break
    temp = [tweet.content, tweet.lang,
            tweet.date]
    tweets.append(temp)

df = pd.DataFrame(tweets)
csv_data = df.to_csv('tweets_hashtag.csv', index=True)
