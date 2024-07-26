class CleanDataFrame:

    def CleanDf(df):
        df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1, inplace=True)
        df.dropna(inplace=True, axis=1)
        df.rename(columns={"v1": "label", "v2": "text"})

        return df
