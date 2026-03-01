import pandas as pd

def load_denominations(df):
    data = pd.read_csv(df)
    return data.sort_values(by='denomination', ascending=False)

def validate_denominations(denominations):
    # if-else to check if a list or read in as csv file
    if not isinstance(denominations, list):
        denominations = denominations.values.tolist()
        
        fixed_denominations = []
        
        for i in denominations:
            fixed_denominations.append(i[0])
            
        fixed_denominations.sort(reverse = True)
    else:
        fixed_denominations = []
        
        for i in denominations:
            fixed_denominations.append(i)
        
        fixed_denominations.sort(reverse = True)
    
    # valid input check
    for i in fixed_denominations:
        if int(i) > 0 and type(i) == int:
            pass
        else:
            raise ValueError("Incorrect Denomination format.")
        
    return fixed_denominations