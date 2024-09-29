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
def merge_sort(arr, lower, upper, inversions):
    if lower == upper:
        return

    merge_sort(arr, lower, lower+(upper-lower)//2, inversions)
    merge_sort(arr, lower+(upper-lower)//2+1, upper, inversions)

    i, j = lower, lower+(upper-lower)//2+1
    temp = []
    while i <= lower+(upper-lower)//2 and j <= upper:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        if arr[i] > arr[j]:
            temp.append(arr[j])
            j += 1
            inversions[0] += len(arr[i:lower+(upper-lower)//2+1])
    for index in range(i, lower+(upper-lower)//2+1):
        temp.append(arr[index])
    for index in range(j, upper+1):
        temp.append(arr[index])
    for index in range(lower, upper+1):
        arr[index] = temp[index-lower]
    return arr

inversions = [0]
n = int(input())
arr = [int(element) for element in input().split()]
merge_sort(arr, 0, len(arr)-1, inversions)
print(inversions[0])