"""PROBLEM
4.3.6 Minimal Element in a Circularly Sorted Array
Minimal Element in a Circularly Sorted Array Problem
Given a circularly sorted array of distinct integers, find the minimal element in this array.
Input: A circularly sorted array of distinct integers.
Output: Minimal element in this array.
"""
"""SOLUTION
The solution to this is using binary search. 
The criteria to move up is if mid element is higher than lower. 
If mid element is smaller than lower, move down.
If however, the next element to mid is smaller than itself, then the next element is the lowest term, since the array is circulary sorted, this is the turning point
Finally, if we keep going up untill the end of the array and we don't find the turning point, this means that there is no turning point, and the array is simply sorted, and so the first element is the least.
"""
def minimal_element_search(arr):
    lower, upper = 0, len(arr)-1
    while lower < upper:
        mid = lower + (upper - lower)//2
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]
        if arr[mid] >= arr[lower]:
            lower = mid + 1
        elif arr[mid] < arr[lower]:
            upper = mid
    return arr[0]

print(minimal_element_search([3, 4, 5, 6, 7, 8, 1, 2]))
