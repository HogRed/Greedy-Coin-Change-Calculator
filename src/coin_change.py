import pandas as pd
import numpy as np
import utils

def greedy_coin_change(amt, coin_denom):
    coin_denom.sort(reverse = True) # extra check if raw list passed in
    
    coin_dict = {}
    
    for coin in coin_denom:
        if amt == 0: # check for done
            break
        
        num_fit = amt // coin # find even number of splits
        amt -= (coin * num_fit) # get total amount to subtract
        coin_dict[str(coin)] = num_fit # add entry to dict
    
    if amt != 0:
        raise ValueError("Unable to make exact change with given denominations.")
        
    return coin_dict
            
def main():
    coin_list = utils.load_denominations('C:/Users/jtfai/HogRed-a-greedy-coin-change-calculator-lp/data/coin_denominations.csv')
    coin_list = utils.validate_denominations(coin_list)
    try:
        test_amounts = greedy_coin_change(67, [10,25,1])
        for k,v in test_amounts.items():
            print(f'Coin: {k}, Amount: {v}')
    except Exception as e:
        print(f'Exception occurred. {e}.')

main()