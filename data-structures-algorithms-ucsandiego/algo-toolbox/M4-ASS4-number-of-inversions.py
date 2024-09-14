"""
4.2.5 Number of Inversions
Number of Inversions Problem
Compute the number of inversions in a sequence of integers.
Input: A sequence of n integers a1 ,...,an.
Output: The number of inversions in the sequence, i.e., the number of indices i < j such that ai > aj.

Input format. The first line contains an integer n, the next one contains a sequence of integers a1 ,...,an.
Output format. The number of inversions in the sequence.
Constraints. 1 ≤ n ≤ 30000, 1 ≤ ai ≤ 10**9 for all 1 ≤ i ≤ n
"""
def merge_sort(arr, inversions):
    if len(arr)<=1:
        return arr

    i, j, result = 0, 0, []
    left, right = merge_sort(arr[:len(arr)//2], inversions),merge_sort(arr[len(arr)//2:], inversions)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions[0] += len(left[i:])
    return result + left[i:] + right[j:]

inversions = [0]
n = int(input())
arr = [int(element) for element in input().split()]
arr = merge_sort(arr, inversions)
print(inversions[0])