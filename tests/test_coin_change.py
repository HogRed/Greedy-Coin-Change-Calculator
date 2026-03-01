import sys
import os

# add the parent directory of the current file to sys.path
# makes it easy to find for python -m unittest discover tests
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from src.coin_change import greedy_coin_change
from src.utils import load_denominations, validate_denominations

class CoinTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        coin_denom = load_denominations('C:/Users/jtfai/HogRed-a-greedy-coin-change-calculator-lp/data/coin_denominations.csv')
        print(coin_denom)
        valid_denom = validate_denominations(coin_denom)
        self.denominations = valid_denom
    
    def test_change_for_67(self):
        actual_result = greedy_coin_change(67, self.denominations)
        expected_result = {'25': 2, '10': 1, '1': 7}
        self.assertEqual(actual_result,expected_result, 'The function failed for 67.')
        
    def test_change_for_99(self):
        actual_result = greedy_coin_change(99, self.denominations)
        expected_result = {'25': 3, '10': 2, '1': 4}
        self.assertEqual(actual_result,expected_result, 'The function failed for 99.')
    
    def test_edge_case_1(self):
        ''' tests for greedy_coin_change(7, [25,10,5])'''
        with self.assertRaises(ValueError):
            greedy_coin_change(7, [25,10,5])

    def test_edge_case_2(self):
        '''tests with unsorted input'''
        actual_results = greedy_coin_change(67, [10,25,1])
        expected_result = {'25':2, '10': 1, '1': 7}
        self.assertEqual(actual_results, expected_result, 
                         'The function failed for greedy_coin_change(67, [10,25,1]).')
    
    def test_invalid_input(self):
        '''makes sure negative input is rejected'''
        with self.assertRaises(ValueError):
            validate_denominations([5,0,-1])
            
if __name__ == '__main__':
    unittest.main()