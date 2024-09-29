"""PROBLEM STATEMENT
4.2.3 Majority Element
Majority Element Problem
Check whether a given sequence of numbers contains an element that appears more than half of the times.

Input: A sequence of n integers.

Output: 1, if there is an element that is repeated more than n/2 times, and 0 otherwise.

Input format. The first line contains an integer n, the next one contains a sequence of n non-negative integers. a0 ,...,an−1.

Output format. Output 1 if the sequence contains an element that appears more than n/2 times, and 0 otherwise.

Constraints. 1 ≤ n ≤ 10**5 ; 0 ≤ ai ≤ 10**9 for all 0 ≤ i < n.
"""
"""SOLUTION 1
The key insight on this problem is to realize that if an element appears more than half of the times, than this element necessarily appears at the middle of a sorted list.

The solution to this problem will be:
1st: Sort the list
2nd: Find the element on the middle
3rd: Count if this element appears more than len/2 on the list.
    -> To count the element, we will use binary search to find the first appearance of the element and the last. This way, the counting will take only logn, instead of n.

This solution works very well for an ordered list, because in such case it would not be necessary to order it.
All the work required would be O(logn) for finding the first occurance, and O(logn) for the second, that is O(2*logn) = O(logn)
However, since the problem does not state that the array is sorted, extra time is required for sorting.
With the sorting step, the complexity is O(n*logn + 2*logn) = O(n*logn)
Since this is not optimal for unsorted lists, we shall provide a second solution for unsorted lists, which has running time of O(n)
"""

def quick_sort(arr, lower, upper):
    # print(arr, lower, upper)
    if upper <= lower:
        return arr

    m1, i, m2 = lower, lower+1, upper
    while m2>=i:
        if arr[i] < arr[m1]:
            arr[i], arr[m1] = arr[m1], arr[i]
            i += 1
            m1 += 1
        elif arr[i] == arr[m1]:
            i += 1
        elif arr[i] > arr[m1]:
            arr[i], arr[m2] = arr[m2], arr[i]
            m2 -= 1
    quick_sort(arr, lower, m1-1)
    quick_sort(arr, m2+1, upper)
    return arr

def binary_search(arr, search_element, first=True):
    left, right = 0, len(arr) - 1
    if first == True:
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] < search_element:
                left = mid + 1
            elif arr[mid] >= search_element:
                right = mid
        return right if arr[right] == search_element else -1
    elif first == False:
        while left < right:
            mid = left + (right-left+1)//2
            if arr[mid] <= search_element:
                left = mid
            elif arr[mid] > search_element:
                right = mid - 1
        return right if arr[right] == search_element else -1

def majority_element(arr):
    quick_sort(arr, 0, len(arr)-1)
    middle_element_frequency = binary_search(arr, arr[(len(arr)-1)//2], False) - binary_search(arr, arr[(len(arr)-1)//2], True) + 1
    if middle_element_frequency > len(arr)/2:
        return 1
    else:
        return 0

"""SOLUTION 2
The solution 2 just counts how many times each element appears. 
If any of them exceeds the half the total number of elemtns, it returns 1.
Otherwise, it returns 0.
This has runtime of n, because dictionaries are hash maps, and so the lookups have O(1)
Since we have a constant ammount of work for each element on the array, the worst case is O(n)

Since the problem statement does not indicate that the list is sorted, we will use this second soluction as our final solution.
Even though this exercise comes from the divide and conquer module, take note that no divide and conquer strategy is used on this solution.
"""
def majority_element2(arr):
    counts = {}
    length = len(arr)
    for element in arr:
        if element in counts:
            counts[element] += 1
            if counts[element] > length/2:
                return 1
        else:
            counts[element] = 1
    return 0

n = int(input())
arr = [int(element) for element in input().split()][:n]
print(majority_element2(arr))