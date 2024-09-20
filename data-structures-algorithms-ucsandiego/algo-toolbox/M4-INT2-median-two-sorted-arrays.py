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
    n = len(arr1) + len(arr2)
    if len(arr2) < len(arr1): # Place the smallest arr as first, so that the median when len1 + len2 is odd will be r2, which is the longest
        arr1, arr2 = arr2, arr1
    found = False
    lower, upper = 0, len(arr1) - 1
    while not found:
        mid1 = lower + (upper - lower+1)//2
        l1 = float('-inf') if mid1 < 1 else arr1[mid1-1] # We use infinities so that the found True condition returns when we get to the edges
        r1 = float('inf') if mid1 > len(arr1)-1 else arr1[mid1]

        mid2 = n - len(arr1) - mid1 - 1
        l2 = float('-inf') if mid2 < 1 else arr2[mid2-1]
        r2 = float('inf') if mid2 > len(arr2)-1 else arr2[mid2]

        if l1 <= r2 and l2 <= r1:
            found = True
        elif l1 > r2:
            upper = mid1 - 1
        elif l2 > r1:
            lower = mid1 + 1
    if n % 2 == 0: median = (r1 + r2)/2
    else: median = r2
    return median

print(median_of_sorted_arrays([1, 10, 15, 30, 38], [5, 17, 20, 30, 45, 46]))

