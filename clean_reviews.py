import pandas as pd

# Load the scraped data
df = pd.read_csv("BA_reviews.csv")

# Show first 5 rows before cleaning
print("Before cleaning:")
print(df.head())

# Remove unnecessary text like "✅ Trip Verified" and "Not Verified"
df["reviews"] = df["reviews"].str.replace("✅ Trip Verified", "", regex=False)
df["reviews"] = df["reviews"].str.replace("Not Verified", "", regex=False)
df["reviews"] = df["reviews"].str.strip()  # Remove extra whitespace

# Show first 5 rows after cleaning
print("\nAfter cleaning:")
print(df.head())

# Save cleaned data
df.to_csv("BA_reviews_cleaned.csv", index=False)
