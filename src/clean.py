def clean_df(df):
    df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    df = df.rename(columns={"v1": "label", "v2": "text"})

    return df
