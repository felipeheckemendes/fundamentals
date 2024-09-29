"""PROBLEM
4.3.5 Duplicate Search
Duplicate Search Problem
Given an array of non-negative integers, check whether it contains identical elements.
Input: An array of non-negative integers.
Output: Check whether the array contains identical elements.
"""
"""SOLUTION
We can do this in linear time, by going through the array and storing in a hash maps all integers found.
When the first of them if found twice, we return earlier.
"""
def duplicate_search(arr):
    found = {}
    for element in arr:
        if element in found:
            return True
        else:
            found[element] = True
    return False

print(duplicate_search([4, 2, 7, 6, 8, 9, 2]))