import pandas as pd
import numpy as np
import utils

def greedy_coin_change(amt, coin_denom):
    #print(coin_denom)
    
    coin_dict = {}
    
    for coin in coin_denom:
        if amt == 0:
            break
        
        num_fit = amt // coin
        amt -= (coin * num_fit)
        coin_dict[str(coin)] = num_fit
    
    if amt != 0:
        raise ValueError("Unable to make exact change with given denominations.")
        
    return coin_dict
            
def main():
    coin_list = utils.load_denominations('C:/Users/jtfai/HogRed-a-greedy-coin-change-calculator-lp/data/coin_denominations.csv')
    coin_list = utils.validate_denominations(coin_list)
    try:
        test_amounts = greedy_coin_change(35, coin_list)
        for k,v in test_amounts.items():
            print(f'Coin: {k}, Amount: {v}')
    except Exception as e:
        print(f'Exception occurred. {e}.')

main()