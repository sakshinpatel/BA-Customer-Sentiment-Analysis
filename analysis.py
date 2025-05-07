import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load the cleaned data
df = pd.read_csv("BA_reviews_cleaned.csv")

# Basic EDA: Check for missing values and general stats
print("Basic Stats:")
print(df.describe())

# Sentiment Analysis: Function to determine sentiment polarity
def get_sentiment(review):
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

# Apply sentiment analysis to each review
df['sentiment'] = df['reviews'].apply(get_sentiment)

# Summary of sentiments
positive_reviews = df[df['sentiment'] > 0]
negative_reviews = df[df['sentiment'] < 0]
neutral_reviews = df[df['sentiment'] == 0]

print(f"Positive Reviews: {len(positive_reviews)}")
print(f"Negative Reviews: {len(negative_reviews)}")
print(f"Neutral Reviews: {len(neutral_reviews)}")

# Most frequent words
def get_most_frequent_words(text_data):
    words = ' '.join(text_data).lower()
    words = re.sub(r'[^\w\s]', '', words)  # Remove punctuation
    words_list = words.split()
    return Counter(words_list).most_common(10)

# Get most frequent words from the reviews
most_frequent_words = get_most_frequent_words(df['reviews'])

print("Most Frequent Words:")
print(most_frequent_words)

# Visualization: Word Cloud of most frequent words
wordcloud = WordCloud(width=800, height=400, max_words=200).generate(' '.join(df['reviews']))

# Display the WordCloud
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of British Airways Reviews")
plt.show()

# Optional: You can save the word cloud to a file
wordcloud.to_file("wordcloud_ba_reviews.png")

# Plot sentiment distribution
plt.figure(figsize=(10, 6))
df['sentiment'].hist(bins=50, color='blue', alpha=0.7)
plt.title('Sentiment Distribution of Reviews')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.show()

# Save the analysis result to a new file (optional)
df.to_csv("BA_reviews_with_sentiment.csv", index=False)

print("Analysis complete and results saved.")
