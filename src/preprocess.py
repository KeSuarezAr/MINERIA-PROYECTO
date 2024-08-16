import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


def preprocess_df(df):
    nltk.download("punkt")
    nltk.download("stopwords")

    df["translation"] = df["translation"].str.lower()
    df["translation"] = df["translation"].apply(word_tokenize)
    stop_words = set(stopwords.words("spanish"))
    df["translation"] = df["translation"].apply(lambda x: [word for word in x if word not in stop_words])
    df["translation"] = df["translation"].apply(lambda x: " ".join(x))

    # Feature Extraction
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["translation"])

    # Split the Dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, df["label"], test_size=0.2, random_state=42
    )

    return vectorizer, X_train, X_test, y_train, y_test
