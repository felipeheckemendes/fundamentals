"""
4.3.1 Count of an Element in a Sorted Array
Count of an Element in a Sorted Array Problem
Given a sorted integer array and an integer q, find the number of times q appears in the array.
Input: A sorted integer array (possibly with duplicates) and an integer q.
Output: The number of times q appears in the array
"""
"""SOLUTION
Considering the list is sorted:
In order to solve this problem in logn time, we just need to use binary_search to find the first and last element that matches.
The difference between the indexes of first and last + 1 is equal to the number of elements.
Since binary search has time complexity logn, the overall complexity if O(2*logn) = O(logn)
"""
def binary_search(arr, element, search_type='first'):
    lower, upper = 0, len(arr)-1
    while lower < upper:
        if search_type != 'last':
            mid = lower + (upper-lower)//2
            if arr[mid] < element:
                lower = mid + 1
            elif arr[mid] >= element:
                upper = mid
        elif search_type == 'last':
            mid = lower + (upper-lower+1)//2
            if arr[mid] <= element:
                lower = mid
            elif arr[mid] > element:
                upper = mid - 1
    if search_type != 'last':
        if arr[upper] == element:
            return upper
        else:
            return False
    elif search_type == 'last':
        if arr[lower] == element:
            return lower
        else:
            return False

def count_elements(arr, element):
    first = binary_search(arr, element, 'first')
    last = binary_search(arr, element, 'last')
    return last - first + 1 if first is not False and last is not False else 0


array = [1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 8, 9, 10]
element = 7
print(count_elements(array, element))

