import praw
import nltk
from get_all_tickers import get_tickers as gt

# Download these libraries for the NLTK if you haven't already.
# nltk.download('punkt')
# nltk.download('words')
# nltk.download('stopwords')

r = praw.Reddit(
    client_id="##############",
    client_secret="##############################",
    password="######",
    user_agent="os:ticker-scraper:1.0 (by u/<your-username-here>)",
    username="<your-username>",
)

# Used for frequencies and comparisons.
words = []
tickers = gt.get_tickers()
threads = ['RobinHoodPennyStocks', 'wallstreetbets', 'StockMarket']

# Parse submissions and comments.
for thread in threads:
    for submission in r.subreddit(thread).new(limit=25):
        print(submission.title)

        # Tokenize the title, body, and comment body throughout the submission.
        submission.comments.replace_more()
        words += nltk.tokenize.word_tokenize(submission.title)
        words += nltk.tokenize.word_tokenize(submission.selftext)

        for comment in submission.comments.list():
            words += nltk.tokenize.word_tokenize(comment.body)

# Display frequencies for ticker words.
for word, frequency in nltk.FreqDist(words).most_common():
    if word in tickers and len(word) >= 3:
        print('%s [%d]' % (word, frequency))
