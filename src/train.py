from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB


def train_model(x_train, x_test, y_train, y_test):
    # Train a classification model, such as Multinomial Naive Bayes
    classifier = MultinomialNB()
    classifier.fit(x_train, y_train)

    # Evaluate the model's performance using metrics like accuracy and classification report
    y_pred = classifier.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(report)

    return classifier