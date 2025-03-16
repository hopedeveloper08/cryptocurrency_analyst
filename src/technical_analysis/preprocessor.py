def preprocessor(df):
    df.columns = df.columns.str.lower()
    df.drop(columns=['volume'], inplace=True)
    df = df.iloc[:-1, :]
    return df
