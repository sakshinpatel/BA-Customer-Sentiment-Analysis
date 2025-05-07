import matplotlib.pyplot as plt

# Data from your analysis (positive, negative, and neutral reviews)
sentiment_data = {
    'Sentiment': ['Positive', 'Negative', 'Neutral'],
    'Count': [614, 375, 11]  # Replace these with the actual counts
}

# Creating a bar graph
plt.figure(figsize=(8, 6))
plt.bar(sentiment_data['Sentiment'], sentiment_data['Count'], color=['green', 'red', 'gray'])
plt.title('Sentiment Distribution of Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')

# Displaying the chart
plt.show()
