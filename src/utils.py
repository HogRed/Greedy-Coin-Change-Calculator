import pandas as pd

def load_denominations(df):
    data = pd.read_csv(df)
    return data.sort_values(by='denomination', ascending=False)

def validate_denominations(denominations):
    for i in denominations:
        if i > 0 and type(i) == int:
            pass
        else:
            raise ValueError("Incorrect Denomination format.")