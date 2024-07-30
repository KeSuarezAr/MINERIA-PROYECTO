import joblib


def save_model(classifier, vectorizer):
    joblib.dump(classifier, "models/spam_model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")
