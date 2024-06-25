import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import joblib

nltk.download("punkt")
nltk.download("stopwords")

df = pd.read_csv("data/spam.csv", encoding="latin-1")
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
df = df.rename(columns={"v1": "label", "v2": "text"})

# Preprocess text data
df["text"] = df["text"].str.lower()
df["text"] = df["text"].apply(word_tokenize)
stop_words = set(stopwords.words("english"))
df["text"] = df["text"].apply(lambda x: [word for word in x if word not in stop_words])
df["text"] = df["text"].apply(lambda x: " ".join(x))

# Feature Extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Split the Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, df["label"], test_size=0.2, random_state=42
)

# Train a classification model, such as Multinomial Naive Bayes
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Evaluate the model's performance using metrics like accuracy and classification report
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:")
print(report)

# Save the model and vectorizer
joblib.dump(classifier, "models/spam_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")