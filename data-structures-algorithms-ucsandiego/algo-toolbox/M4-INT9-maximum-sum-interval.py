"""PROBLEM
4.3.9 Maximum-Sum Interval
Maximum-Sum Interval Problem
Given an integer array, find its subarray with maximum sum.
Input: An integer array (a0,...,an−1).
Output: The maximum value of Sum(i=l -> r) ai = al + al+1 + ··· + ar among all intervals 0 ≤ l ≤ r ≤ n − 1.
"""
"""SOLUTION
The solution for this is to calculate the maximum sum of elements ending at each element, from left to right.
The one which has the biggest, wins.
"""
def max_sum(arr):
    max_sum = arr[0]
    max_sum_current = arr[0]
    for element in arr:
        if element + max_sum_current > element:
            max_sum_current = element + max_sum_current
        elif element > element + max_sum_current:
            max_sum_current = element
        if max_sum_current > max_sum:
            max_sum = max_sum_current
    return max_sum

print(max_sum([-7, 3, -2, 0, 7, -5, 4]))
