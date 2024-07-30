def clean_df(df):
    df = df.drop(["v4", "v5"], axis=1)
    df = df.rename(columns={"v1": "label", "v2": "text", "v3": "translation"})

    return df
