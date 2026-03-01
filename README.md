# Greedy Coin Change Calulator

This is a project that showcases a functional greedy coin change calculator. It is able to efficiently determine the minimum number of coins that are neceesary for any amount given, using the largest denominations of coins available. It showcases how to manage real-world input data and to build structures for business logic that are clear and correct.

This repository also is able to handle edge cases (negative inputs, wrongly sorted values, data in lists or read in as a csv). This is important for showcasing system resiliency and features important when building systems that need to be reliable, especially in the world of financial applications.

The project also features a full suite of unit tests using the unittest framework in Python, highlighting the importance of test-driven development to help make sure code created is accurate, maintainable, and able to be used in production.

This is a great project to practice greedy algorithm design, data validation, error handling, and learning to automate testing skills. This is useful for any software development process.

The solution in this repository is my own creation after reading the specs given by the project leader, Ronnie Rahman, on the Manning Live Project for ["Greedy Coin Change Calculator"](https://www.manning.com/liveproject/a-greedy-coin-change-calculator).

## How to Run

Once the project has been cloned, you can download the versions of the packages used for this project to ensure everything runs correctly (recommended to have a virtual environment set up):
```bash
pip install -r requirements.txt
```

In order to test out the functionality, you can navigate to the src/ folder and run:

```python
python coin_change.py
```

You can of course modify the data / function call as you see fit.

## Using unittest

In order to run the unit tests, navigate to the project root and run:

```python
python -m unittest discover tests
```
