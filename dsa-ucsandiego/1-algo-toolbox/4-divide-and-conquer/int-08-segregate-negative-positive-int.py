"""PROBLEM
4.3.8 Segregate Negative and Positive Integers
Segregate Negative and Positive Integers Problem
Given an array of distinct integers, output an array containing the same integers where all negative numbers appear first (in the original order), followed by all positive numbers (in the original order).
Input: An array of distinct positive and negative integers.
Output: An array containing the same integers where all negative numbers appear first (in the original order), followed by all positive numbers (in the original order).
"""
"""SOLUTION
Create two temporary arrays for negative and positive integers.
Iterate the input array an append elements based on being positive or negative.
Return the concatenation of both
"""
def segregate_negative_positive_integers(arr):
    negative = []
    positive = []
    for element in arr:
        if element >= 0:
            positive.append(element)
        else:
            negative.append(element)
    return negative + positive

print(segregate_negative_positive_integers([1, 2, 3, -1, -2, -3, 4, 5, 6, -4, -5, -6]))