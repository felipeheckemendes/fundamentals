"""
4.2.4 Speeding-up RandomizedQuickSort
Speeding-up RandomizedQuickSort Problem
Sort a given sequence of numbers (that may contain duplicates) using a modification of RandomizedQuickSort that works in O(nlogn) expected time.
Input: An integer array with n elements that may contain duplicates.
Output: Sorted array (generated using a modification of RandomizedQuickSort) that works in O(nlogn) expected time

Input format. The first line of the input contains an integer n. The next line contains a sequence of n integers a0 ,a1 ,...,an−1.

Output format. Output this sequence sorted in non-decreasing order.

Constraints. 1 ≤ n ≤ 10**5 ; 1 ≤ ai ≤ 10**9 for all 0 ≤ i < n.
"""
"""SOLUTION
The solution was already implemented by me previously, as study after the classes.
Here I just take the implementation already done and apply the standart input and output required by assignement
"""
import random

def quick_sort_random_3partition(arr, lower, upper):
    if lower>=upper:
        return

    pivot_index = random.randint(lower, upper)
    arr[lower], arr[pivot_index] = arr[pivot_index], arr[lower]
    m1, i, m2 = lower, lower+1, upper
    while i <= m2:
        if arr[i] < arr[m1]:
            arr[m1], arr[i] = arr[i], arr[m1]
            m1 += 1
            i += 1
        elif arr[i] == arr[m1]:
            i += 1
        elif arr[i] > arr[m1]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
    quick_sort_random_3partition(arr, lower, m1-1)
    quick_sort_random_3partition(arr, m2+1, upper)

n = int(input())
arr = [int(element) for element in input().split()][:n]
quick_sort_random_3partition(arr, 0, n-1)
print(" ".join(map(str, arr)))