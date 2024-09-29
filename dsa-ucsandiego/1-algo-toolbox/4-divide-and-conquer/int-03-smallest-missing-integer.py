"""PROBLEM
4.3.3 Smallest Missing Element in a Sorted Array
Smallest Missing Element in a Sorted Array
Problem
Given a sorted array of distinct non-negative integers, find the smallest integer that does not appear in this array.
Input: A sorted array of distinct non-negative integers.
Output: The smallest integer that does not appear in this array.
"""
"""SOLUTION
1st: Determine the distance between first element and first index.
2nd: If no missing numbers, this distance would remain the same (given that all numbers are distinct)
3rd: Use a binary approach to find the first element where the distance is not the same as that of the first element.
"""
def smallest_missing_int(arr):
    first_distance = arr[0] - 0
    distance = float('inf')
    lower, upper = 0, len(arr)-1
    while lower < upper:
        mid = lower + (upper - lower)//2
        if arr[mid] - mid > first_distance:
            upper = mid
        elif arr[mid] - mid <= first_distance:
            lower = mid + 1
    return arr[mid-1]+1

print(smallest_missing_int([-1, 0, 1, 10, 11, 12]))
        
