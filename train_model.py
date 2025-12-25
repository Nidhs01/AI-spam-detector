import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load CSV with proper encoding
df = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only relevant columns from your CSV
df = df[['v1', 'v2']]   # select original columns
df.columns = ['label', 'message']  # rename for clarity

# Convert labels to numeric: 0 = ham, 1 = spam
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Features and labels
X = df['message']
y = df['label']

# Vectorize text
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save vectorizer and model
with open("spam_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("Training complete. Model saved as spam_model.pkl")
