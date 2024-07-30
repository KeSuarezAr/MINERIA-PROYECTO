import pandas as pd


def read_df():
    df = pd.read_csv("./data/spam_translated.csv", encoding="latin-1")
    return df
