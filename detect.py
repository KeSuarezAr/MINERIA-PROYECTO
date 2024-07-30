import joblib

loaded_model = joblib.load("models/spam_model.pkl")
loaded_vectorizer = joblib.load("models/vectorizer.pkl")

email = ["500 Nuevos móviles desde 2004, MUST GO! Txt: NOKIA a No: 89545 y recoger el tuyo hoy!From ONLY 1 www.4-tc.biz 2optout 087187262701.50gbp/mtmsg18"]
email = loaded_vectorizer.transform(email)

prediction = loaded_model.predict(email)

if prediction[0] == "spam":
    print("This email is spam.")
else:
    print("This email is not spam.")
