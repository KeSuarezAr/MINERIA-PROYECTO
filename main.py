from src.preprocess import preprocess_df
from src.train import train_model
from src.save_model import save_model
from src.clean import clean_df
from src.read import read_df

print("hi")

df = read_df()
df = clean_df(df)

vectorizer, X_train, X_test, y_train, y_tests = preprocess_df(df)

classifier = train_model(X_train, X_test, y_train, y_tests)

save_model(classifier, vectorizer)
