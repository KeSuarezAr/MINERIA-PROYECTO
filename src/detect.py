import joblib

loaded_model = joblib.load("models/spam_model.pkl")
loaded_vectorizer = joblib.load("models/vectorizer.pkl")

new_email = ["Congratulations! You've won a prize. Claim it now."]
new_email = loaded_vectorizer.transform(new_email)

prediction = loaded_model.predict(new_email)

if prediction[0] == "spam":
    print("This email is spam.")
else:
    print("This email is not spam.")
