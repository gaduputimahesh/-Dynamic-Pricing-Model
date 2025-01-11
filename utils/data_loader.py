import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    return df.dropna()

def merge_data(*dfs):
    return pd.concat(dfs, axis=1)
