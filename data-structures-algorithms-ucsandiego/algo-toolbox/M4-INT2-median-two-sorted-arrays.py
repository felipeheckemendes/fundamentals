"""
4.3.2 Median of Two Sorted Arrays
Median of Two Sorted Arrays Problem
Find the median of two equally-sized sorted arrays. 
Input: Two sorted arrays a0 ≤ a1 ≤ ··· ≤ an−1 and b0 ≤ b1 ≤ ··· ≤ bn−1 of integers of the same size.
Output: The median cn−1 of their sorted union c0 ≤ c1 ≤ ··· ≤ c2n−1.
"""
"""SOLUTION
We won't merge the two arrays, because merging would result in linear time O(n).
We are going to profit from the fact that the arrays are sorted, and use a binary search strategy to find the splits on the arrays (i and j), such that 
-> all elements on array 1 that combe before and up to arr[i] and all elements before and up to arr[j] are smaller than all elements after the same index.
"""

def median_of_sorted_arrays(arr1, arr2):
    lower1, lower2 = 0, 0
    upper1, upper2 = len(arr1) - 1, len(arr2) - 1
    found = False
    while not found:
        mid1, mid2 = lower1 + (upper1-lower1)//2, lower2 + (upper2-lower2)//2
        if max(arr1[mid1], arr2[mid2]) < min(arr1[mid1+1], arr2[mid2+1]):
            found = True
        else:
            if arr1[mid1] > min(arr1[mid1+1], arr2[mid2+1]):
                upper1 = mid1 - 1
            if arr2[mid2] > min(arr1[mid1+1], arr2[mid2+1]):
                upper2 = mid2 - 1
            if arr1[mid1] < min(arr1[mid1+1], arr2[mid2+1]):
                lower1 = mid1 + 1
            if arr2[mid2] < min(arr1[mid1+1], arr2[mid2+1]):
                lower2 = mid2 + 1
    median = max(arr1[mid1], arr2[mid2])
    return median

print(median_of_sorted_arrays([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

