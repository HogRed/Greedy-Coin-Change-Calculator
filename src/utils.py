import pandas as pd

def load_denominations(df):
    data = pd.read_csv(df)
    return data.sort_values(by='denomination', ascending=False)