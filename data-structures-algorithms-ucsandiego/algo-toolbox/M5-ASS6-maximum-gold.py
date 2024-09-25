"""PROBLEM
5.2.6 Maximum Amount of Gold
Maximum Amount of Gold Problem
Given a set of gold bars of various weights and a backpack that can hold at most W pounds, place as much gold as possible into the backpack.
Input: A set of n gold bars of integer weights w1,...,wn and a backpack that can hold at most W pounds.
Output: A subset of gold bars of maximum total weight not exceeding W.

Input format. 
The first line of the input contains an integer W (capacity of the backpack) and the number n of gold bars. 
The next line contains n integers w1,...,wn defining the weights of the gold bars.
Output format. The maximum weight of gold bars that fits into a backpack of capacity W .
"""
def maximum_gold(target_capacity, gold_bars):
    matrix = [[0 for element in range(target_capacity+1)] for element in gold_bars + [0]]

    for j in range(1, len(matrix[0])):
        for i in range(1, len(matrix)):
            matrix[i][j] = max(
                matrix[i-1][j],
                matrix[i-1][j-gold_bars[i-1]] + gold_bars[i-1] if matrix[i][j-gold_bars[i-1]] + gold_bars[i-1] <= j else float('-inf')
            )
    return matrix

target, n = [int(element) for element in input().split()[:2]]
gold_bars = [int(element) for element in input().split()[:n]]
result = maximum_gold(target, gold_bars)
print(result[len(result)-1][len(result[0])-1])