import nltk
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# FILE_NAME = "testText_Ad Blockers Can't Watch This - WAN Show November 3, 2023_1714497589.1880133.txt"
FILE_NAME = "testText_Ad Blockers Can't Watch This - WAN Show November 3, 2023_1714497589.1880133.txt"

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# new_words = {
#     "omg": 1,
#     "wtf": 1,
#     "sick": 1,
#     "cool": 1,
#     "holy": 1,
#     "what": 1,
#     "bruh": 1,
#     "goooo": 1,
# }

# sid.lexicon.update(new_words)

# Read messages from file
corpus = []
with open(os.path.join("output", FILE_NAME) , 'r') as file:
    for line in file:
        corpus.append(line.split('\t'))

# # last 10000 messages
# corpus = corpus[-10000:]

# Perform sentiment analysis on each message
sentiment_scores = []
for message in corpus:
    # Calculate sentiment score for each message
    scores = sid.polarity_scores(message[1])
    sentiment_scores.append(scores['compound'])  # Compound score represents overall sentiment


with open('sentiment.txt', 'w') as file:
    for i, score in enumerate(sentiment_scores):
        # file.write(f"Sentiment Score = {score}\t{corpus[i]}\n")
        file.write(f"{corpus[i][0]}\t{score}\n")
