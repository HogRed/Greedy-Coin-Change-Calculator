import pandas as pd
import numpy as np
import utils

def greedy_coin_change(amt, coin_denom):
    coin_denom.sort_values(by='denomination', ascending=False)
    coin_denom = coin_denom.values.tolist()
    coins_fixed = []
    for i in coin_denom:
        coins_fixed.append(i[0])
    print(coins_fixed)
    
    coin_dict = {}
    for coin in coins_fixed:
        if amt == 0:
            break
        
        num_fit = amt // coin
        amt -= (coin * num_fit)
        coin_dict[str(coin)] = num_fit
        
    return coin_dict
            
def main():
    coin_list = utils.load_denominations('C:/Users/jtfai/HogRed-a-greedy-coin-change-calculator-lp/data/coin_denominations.csv')
    test_amounts = greedy_coin_change(99, coin_list)
    for k,v in test_amounts.items():
        print(f'Coin: {k}, Amount: {v}')

main()